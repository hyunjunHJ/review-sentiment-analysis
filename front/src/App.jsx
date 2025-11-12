import React, { useState } from 'react';

const App = () => {
  const [inputText, setInputText] = useState('')

  const onHandleSubmit =(e)=>{
    e.preventDefault();
    console.log(inputText);
  };

  return (
    <div>
      <h1>Test Hello</h1>
      <form onSubmit={onHandleSubmit}>
        <input type="text" value={inputText} onChange={(e)=>setInputText(e.target.value)} />
        <button type="submit">번역 및 분석</button>
      </form>
      

    </div>
  );
};

export default App;