from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from schemas import ChatbotResponse

app = FastAPI()


# #CORS
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # 배포할 땐 실제 프론트 도메인으로 제한
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


#endpoint

@app.post('/sentiment', response_model=ChatbotResponse)
async def translate_sentiment(prompt:str):
    return {"prompt":prompt}

