import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Main from './views/main';
import Detail from './components/Detail';
function App() {
    return (
    <div className="App">
         <Routes>
             <Route element={<Main/>} path="/" />
             <Route element={<Detail/>} path="/api/product/:id" />
        </Routes>
    </div>
    );
}
export default App;



