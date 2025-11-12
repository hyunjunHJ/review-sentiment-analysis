from pydantic import BaseModel

class ChatbotResponse(BaseModel):
    prompt:str