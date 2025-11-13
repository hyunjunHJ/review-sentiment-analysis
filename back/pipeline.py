from transformers import pipeline

import os
os.environ["CUDA_VISIBLE_DEVICES"] = ""
# translator + sentiment-analysis 모델 묶어서 endpoint 넘겨줌
def trans_senti(prompt:str):         #prompt:str):
    prompt=prompt

    translator = pipeline("translation", 
                        model="facebook/m2m100_418M",
                        device=-1)

    translated = translator(prompt, src_lang="en", tgt_lang="ko")
    #text
    print(translated, translated[0]['translation_text'])
    
    sentimental = pipeline(task="sentiment-analysis",
              model='Copycats/koelectra-base-v3-generalized-sentiment-analysis',
              framework='pt',
              device=-1)
   
    # [{'translation_text': "Pedro Pascalqa qatiqnintam reto-fuerzaman pusan, huk rikchaq rikch'ayniyoq rikch'ayniyoq rikch'ayniyoqman."}] 
    # [{'label': '1 star', 'score': 0.5432569980621338}]

    result = sentimental( translated[0]['translation_text'])

    response={'translation_text':translated[0]['translation_text'],
            'label':result[0]['label'], 'score':result[0]['score']}   
    
    return response


