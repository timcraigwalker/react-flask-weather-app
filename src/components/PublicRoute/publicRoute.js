import React from "react";
import { useSelector } from "react-redux";
import { Navigate, Outlet } from "react-router-dom";

function PublicRoute() {
    const user = useSelector((state) => state.user.data);
    return (user?.id) ? <Navigate to="/" /> : <Outlet />;
}

export default PublicRoute;