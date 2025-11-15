import React, { useState } from "react";
import axios from "axios";
import "./App.css";

const mockReview = [
  // Very Good
  "Life-saving service! The team went above and beyond to help me meet my deadline at the last minute.",
  // Good
  "Reliable and easy to use interface, definitely makes my daily workflow much smoother.",
  // Neutral
  "Updates are frequent, but they seem to just move buttons around without adding any real value.",
];

const App = () => {
  const [inputText, setInputText] = useState("");
  const [result, setResult] = useState(null);

  const onhandleSubmit = async (e) => {
    e.preventDefault();
    console.log(inputText);

    try {
      const res = await axios.post(
        "http://localhost:8081/sentiment",
        {
          prompt: inputText,
        },
        {
          headers: {
            "Content-Type": "application/json",
          },
        }
      );
      setResult(res.data);
      return res;
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

      <form onSubmit={onhandleSubmit} className="input-area">
        <input
          type="text"
          value={inputText}
          placeholder="리뷰 문장을 입력하세요"
          onChange={(e) => setInputText(e.target.value)}
        />
        <button type="submit" className="button-primary">
          번역 및 분석
        </button>
      </form>

      {result && (
        <div className="result-box">
          <h3 className="title">분석 결과</h3>

          <p className="result-line">
            <b>번역:</b> {result.translation_text}
          </p>
          <p className="result-line">
            <b>감정:</b> {result.label == "1" ? "긍정" : "부정"}
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
