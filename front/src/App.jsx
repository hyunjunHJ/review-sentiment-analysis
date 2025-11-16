import React, { useState } from "react";
import axios from "axios";
import "./App.css";

// 환경변수 또는 기본 포트
const API_URL = import.meta.env.VITE_API_URL || "http://localhost:8000";

const mockReview = [
  "Life-saving service! The team went above and beyond to help me meet my deadline at the last minute.",
  "Reliable and easy to use interface, definitely makes my daily workflow much smoother.",
  "Updates are frequent, but they seem to just move buttons around without adding any real value.",
];

const App = () => {
  const [inputText, setInputText] = useState("");
  const [result, setResult] = useState(null);

  const onhandleSubmit = async (e) => {
    e.preventDefault();

    try {
      const res = await axios.post(
        `${API_URL}/sentiment`,
        { prompt: inputText },
        { headers: { "Content-Type": "application/json" } }
      );
      setResult(res.data);
    } catch (err) {
      console.error(err);
      alert("번역, 감정분석 실패");
    }
  };

  return (
    <div className="container">
      <h2 className="main-title">리뷰 감정 분석</h2>
      <h3 className="title">Sample data</h3>

      <div className="sample-box">
        <ul className="sample-list">
          {mockReview.map((mock, idx) => (
            <li key={idx}>{mock}</li>
          ))}
        </ul>
      </div>

      <h3 className="title">영어 원문 입력</h3>

      {/* 인풋 박스 */}
      <form id="main-form" onSubmit={onhandleSubmit} className="input-area">
        <input
          type="text"
          value={inputText}
          placeholder="리뷰 문장을 입력하세요"
          onChange={(e) => setInputText(e.target.value)}
        />
      </form>

      {/* 버튼을 폼 밖으로 분리 */}
      <div className="button-row">
        <button type="submit" form="main-form" className="button-primary">
          번역 및 분석
        </button>
      </div>

      {/* 결과 박스 */}
      {result && (
        <div className="result-box">
          <h3 className="title">분석 결과</h3>

          <p className="result-line">
            <b>번역:</b> {result.translation_text}
          </p>
          <p className="result-line">
            <b>감정:</b> {result.label === "1" ? "긍정" : "부정"}
          </p>
          <p className="result-line">
            <b>점수:</b> {Math.round(result.score * 100) / 100}
          </p>
        </div>
      )}
    </div>
  );
};

export default App;
