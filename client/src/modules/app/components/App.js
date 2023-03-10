import React from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import { AuthContextProvider } from "../../auth/context/UserContext";
import PrivateRoute from "../../auth/components/PrivateRoute";
import Homee from "./Homee";
import Home from "./Home";
import Login from "../../auth/components/Login";
import Register from "../../auth/components/Register";
import Logout from "../../auth/components/Logout";

function App() {
  return (
    <AuthContextProvider>
      <BrowserRouter>
        <Routes>
          <Route path="/" exact element={<Homee />} /> //this only checks the
          current login status and sets state accordingly, then should redirect
          <Route path="/login" element={<Login />} />
          <Route element={<PrivateRoute />}>
            <Route path="/home" element={<Home />} />
          </Route>
          <Route element={<PrivateRoute />}>
            <Route path="/logout" element={<Logout />} />
          </Route>
          <Route path="/register" element={<Register />} />
        </Routes>
      </BrowserRouter>
    </AuthContextProvider>
  );
}

export default App;
