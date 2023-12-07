import FirstPage from './FirstPage';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

import './App.css';
import TreeVisualization from './TreeVisualization';


function App() {
 
  return (
    <>
    <Router>
      <Routes>
        <Route path="/" element={<FirstPage stuID = "2020204005" stuName = "정필규" />} />
        <Route path="/TreeVisualization" element={<TreeVisualization />} />
      </Routes>
    </Router>
    
    </>
  );
}

export default App;
