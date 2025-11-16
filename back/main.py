from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from schemas import ChatbotResponse, ChatbotInput
from pipeline import trans_senti

#fastapi 기본 환경변수 구조 (pydantic BaseSettings없이)
# from dotenv import load_dotenv
# import os


# load_dotenv(dotenv_path=".env")
# port = int(os.getenv("PORT", 8000))
#스크립트실행?

app = FastAPI()

# #CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 배포할 땐 실제 프론트 도메인으로 제한
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


#endpoint
@app.post('/sentiment', response_model=ChatbotResponse)
async def translate_sentiment(input:ChatbotInput):
    prompt=input.prompt
    answer= trans_senti(prompt)

    return answer

# response: {'translation_text': '그런데네가그런일을 Tom에게말하지않도록좋아야합니다.',
#             'label': '1 star', 'score': 0.3381156623363495}

#명령어 치기 귀찮을대 서버 띄우기위함
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=PORT)