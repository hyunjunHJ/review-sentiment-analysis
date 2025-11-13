from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from schemas import ChatbotResponse, ChatbotInput
from pipeline import trans_senti

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
    answer= trans_senti(prompt)

    return answer

# response: {'translation_text': '그런데네가그런일을 Tom에게말하지않도록좋아야합니다.',
#             'label': '1 star', 'score': 0.3381156623363495}