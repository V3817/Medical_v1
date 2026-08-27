from fastapi import FastAPI

from pydantic import BaseModel


import uvicorn

from ai_agent import (
    agent,
    response_parser,
    trigger_emergency_alert,
    EMERGENCY_KEYWORDS
)

# ---------------- APP INIT ---------------- #

app = FastAPI(

    title="Medical AI Assistant API",

    version="1.0.0"
)


# ---------------- REQUEST SCHEMA ---------------- #

class ChatRequest(BaseModel):

    user_message: str

# ---------------- RESPONSE SCHEMA ---------------- #

class ChatResponse(BaseModel):

    response: str

    tool_used: str

# ---------------- ROUTE ---------------- #

@app.post(
    "/chat",
    response_model=ChatResponse
)

def chat_endpoint(request: ChatRequest):

    user_message = request.user_message.strip()

    # ---------------- VALIDATION ---------------- #

    if not user_message:

        return {
            "response": "Message cannot be empty.",
            "tool_used": "none"
        }

    lower_input = user_message.lower()

    # ---------------- EMERGENCY OVERRIDE ---------------- #

    if any(
        keyword in lower_input
        for keyword in EMERGENCY_KEYWORDS
    ):

        trigger_emergency_alert.func(
            user_message
        )

        return {
            "response": (
                "Emergency support alert triggered. "
                "Please contact emergency services "
                "or a healthcare professional immediately."
            ),

            "tool_used": "trigger_emergency_alert"
        }

    # ---------------- NORMAL AGENT FLOW ---------------- #

    try:

        response = agent.invoke({

            "messages": [
                {
                    "role": "user",
                    "content": user_message
                }
            ]
        })

        parsed_response = response_parser(
            response
        )

        return {
            "response": parsed_response[
                "final_response"
            ],

            "tool_used": parsed_response[
                "tool_used"
            ]
        }

    except Exception as e:

        return {
            "response": (
                f"Agent Error: {str(e)}"
            ),

            "tool_used": "none"
        }
    
@app.get("/health")
def health_check():

    return {
        "status": "healthy"
    }    

# ---------------- MAIN ---------------- #

if __name__ == "__main__":

    uvicorn.run(

        "main:app",

        host="0.0.0.0",

        port=8000,

        reload=True
    )