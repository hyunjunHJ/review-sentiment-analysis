from transformers import pipeline
# import onnxruntime # 그냥 torch깔았음..

# examples
# src = [
#     "Pedro Pascal leads the team back to the retro-future in colorful new version.",
#     "David Corenswet and Rachel Brosnahan soar, but the script is kryptonite.",
#     "Scarlett Johansson and Jonathan Bailey help the franchise roar back to life.",
#     "This musical adaptation hits the right notes, but lacks visual variety.",
#     "Ridley Scott sequel is epic old-fashioned movie-making with a star turn from Paul Mescal.",
#     "Ana de Armas kills busloads of people in giddy, ruthless, orgy of violence.",
#     "Clint Bentley's soft-spoken Western is one of the most quietly beautiful films of the year.",
#     "Dwayne Johnson's Oscar effort is missing teeth, but not from getting punched in the face.",
#     "Francis Ford Coppola's Megalopolis is bloated and unforgivably dull.",
#     "The absolute authority and force of Daniel Day-Lewis carries this movie in the end, and what a pleasure to see his return to the screen.",
# ]

# translator + sentiment-analysis 모델 묶어서 endpoint 넘겨줌
def trans_senti(prompt:str):         #prompt:str):
    prompt=prompt

    translator = pipeline("translation", 
                        model="Helsinki-NLP/opus-mt-tc-bible-big-mul-mul")

    translated = translator(">>kr<< "+ prompt)
    #text
    print(translated, translated[0]['translation_text'])

    #변수가 많아지면 for문 사용여부
    src=""

    sentimental = pipeline('sentiment-analysis',
                        model= "nlptown/bert-base-multilingual-uncased-sentiment")
    # 0번째 배열의 translation_text
    # [{'translation_text': "Pedro Pascalqa qatiqnintam reto-fuerzaman pusan, huk rikchaq rikch'ayniyoq rikch'ayniyoq rikch'ayniyoqman."}] 
    # [{'label': '1 star', 'score': 0.5432569980621338}]

    result = sentimental( translated[0]['translation_text'])

    #test
    print(translated)
    print(result)
    print('trans_type(trans_text):',type(translated[0]['translation_text']))
    print('result_type(label):',type(result[0]['label']))
    print('result_type(score):', type(result[0]['score']))

    response={'translation_text':translated[0]['translation_text'],
            'label':result[0]['label'], 'score':result[0]['score']}
    
    #test
    print("response:",response)
    print("type:", type(response))

    # api넘길때 JSON?Dict? 파싱 용이, pydantic valdiation용이, GPT>다중모델 파이프라인일때 중요
    return response

#반환값 확인용 test - 추후 삭제
