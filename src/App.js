import React, { createContext, useEffect, useState } from "react";
import {
  Route,
  BrowserRouter as Router,
  Routes
} from "react-router-dom";
import "./App.css";

import Header from "./components/Header/header";
import PrivateRoute from "./components/PrivateRoute/privateRoute";
import Home from "./pages/home";
import Login from "./pages/login";
import Register from "./pages/register";

const AuthContext = createContext(null);

function App() {
  const [user, setUser] = useState({});

  useEffect(() => {
    fetch("api/user")
    .then(async (response) => {
        const userResponse = await response.json();
        if(response.status === 200)
        {
          setUser(userResponse);
        }
    })
    .catch((error) => console.error(error));
  }, []);

  return (
      <Router>
        <Header user={user}/>
        <div className="container">
          <Routes>
            <Route path="/test" element={<PrivateRoute user={user} />}>
              <Route path="/test" element={<Home user={user} />} />
            </Route>
            
            <Route exact path="/" element={<Home user={user} />} />
            <Route path="/login" element={<Login user={user} />} />
            <Route path="/register" element={<Register user={user} />} />
          </Routes>
        </div>
      </Router>
  );
}

export default App;
