# 번역 + 감성 분석 – 설치 가이드

FastAPI(백엔드) + React/Vite(프론트엔드) 기반의 번역·감성 분석과제
아래 순서대로 실행

---

## 백엔드 설정 fasapi

```bash
cd back
```
```
conda create -n fastapi python=3.11 -y
conda activate fastapi
```
### 패키지 설치
```pip install -r requirements.txt```
### 서버실행
```uvicorn main:app --reload --port 8000```

## 프론트엔드 설정 react(vite)
```cd ../front```

### 패키지 설치
```npm install```

### 개발 서버 실행
```npm run dev```


