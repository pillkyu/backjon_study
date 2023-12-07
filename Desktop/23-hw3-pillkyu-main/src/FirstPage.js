import React from "react";
import { Link } from 'react-router-dom';
import './FirstPage.css'; 


function FirstPage(props){
    const ClickEvent = () => {
        console.log('페이지 이동.');
    };
    

return(
<>
    <div>
        <h1>{props.stuID}</h1> 
    </div>
    <div>
    <h1>{props.stuName}</h1>
    </div>
    <div>
    <Link to="/TreeVisualization">
        <h2><button className="customButton" onClick = {ClickEvent}  >HW3</button>    </h2>
    </Link>
    </div>
</>
    );
}
FirstPage.defaultProps = { name: '이름없음' };


export default FirstPage;