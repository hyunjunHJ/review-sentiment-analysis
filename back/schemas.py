from pydantic import BaseModel

class ChatbotInput(BaseModel):
    prompt:str


# {'translation_text':translated[0]['translation_text'],
#             'label':result[0]['label'], 'score':result[0]['score']}


class ChatbotResponse(BaseModel):
    translation_text:str
    label:str
    score:float     # round해서 소수 둘쨰짜리까지 or %형태로 출력 가능
