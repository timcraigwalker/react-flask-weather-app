import React from "react";
import { Navigate, Outlet } from "react-router-dom";

function PrivateRoute({user}) {
    return (user && user.id) ? <Outlet /> : <Navigate to="/login" />;
}

export default PrivateRoute;