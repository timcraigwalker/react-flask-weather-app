import React, { useEffect } from "react";
import {
  Route,
  BrowserRouter as Router,
  Routes
} from "react-router-dom";
import "./App.css";

import { useDispatch, useSelector } from "react-redux";
import Header from "./components/Header/header";
import PrivateRoute from "./components/PrivateRoute/privateRoute";
import PublicRoute from "./components/PublicRoute/publicRoute";
import Home from "./pages/home";
import Login from "./pages/login";
import Register from "./pages/register";
import { fetchUser } from "./redux/slices/userSlice";

function App() {
  const dispatch = useDispatch();
  const state = useSelector((state) => state);
  console.log("state", state);

  useEffect(() => {
    dispatch(fetchUser());
  }, [dispatch]);

  return (
      <Router>
        <Header />
        <div className="container">
          <Routes>
            <Route exact path="/" element={<PrivateRoute />}>
              <Route exact path="/" element={<Home />} />
            </Route>

            <Route path="/login" element={<PublicRoute />}>
              <Route path="/login" element={<Login />} />
            </Route>

            <Route path="/register" element={<PublicRoute />}>
              <Route path="/register" element={<Register />} />
            </Route>
          
          </Routes>
        </div>
      </Router>
  );
}

export default App;
