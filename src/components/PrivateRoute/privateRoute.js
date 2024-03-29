import React from "react";
import { useSelector } from "react-redux";
import { Navigate, Outlet } from "react-router-dom";

function PrivateRoute() {
    const user = useSelector((state) => state.user.data);
    return (user?.id) ? <Outlet /> : <Navigate to="/login" />;
}

export default PrivateRoute;