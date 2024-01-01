import { Route, Routes } from "react-router-dom";
import Home from "./view/Home";
import SignUp from "./view/SignUp";
import Login from "./view/Login";
import Order from "./view/Order";

function App() {
    return (
        <>
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/sign-up" element={<SignUp />} />
                <Route path="/login" element={<Login />} />
                <Route path="/order/:id" element={<Order />} />
            </Routes>
        </>
    );
}

export default App;
