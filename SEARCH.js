import "./search.css"
import JSONDATA from "./searchdata.json"

function App() {
    return(
        <div className="App">
            <input type="text" placeholder="Search..."
            {JSONDATA.map((val, key)=> {
                return <div> {val.first_name}</div>
            })}
        </div>
    );
}

export default App;
