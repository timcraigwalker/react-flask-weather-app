import { AccountCircle } from "@mui/icons-material";
import { AppBar, IconButton, Menu, MenuItem, Toolbar, Typography } from "@mui/material";
import { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useNavigate } from "react-router";
import { authLogout } from "../../redux/slices/authSlice";

const Header = () => {
    const dispatch = useDispatch();
    const user = useSelector((state) => state.user.data);

    const navigate = useNavigate();
    const [anchorEl, setAnchorEl] = useState(null);

    const handleLogout = async () => {
        const requestOptions = {
            method: "POST",
            headers: { "Content-Type": "application/json" }
        };
        const response = await fetch("api/auth/logout", requestOptions);
        if(response.status === 200){
            dispatch(authLogout());
            //navigate("/login");
        }
    }

    const handleMenu = (event) => {
        setAnchorEl(event.currentTarget);
    };

    const handleMenuClose = () => {
        setAnchorEl(null);
    };

    return (
        <AppBar position="static">
            <Toolbar>
                <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
                    Weather App
                </Typography>
                { user?.id && (
                    <div>
                    <IconButton
                        size="large"
                        aria-label="account of current user"
                        aria-controls="menu-appbar"
                        aria-haspopup="true"
                        onClick={handleMenu}
                        color="inherit"
                    >
                        <AccountCircle />
                    </IconButton>
                    <Menu
                        id="menu-appbar"
                        anchorEl={anchorEl}
                        anchorOrigin={{
                        vertical: "top",
                        horizontal: "right",
                        }}
                        keepMounted
                        transformOrigin={{
                        vertical: "top",
                        horizontal: "right",
                        }}
                        open={Boolean(anchorEl)}
                        onClose={handleMenuClose}
                    >
                        <MenuItem onClick={handleLogout}>Logout</MenuItem>
                    </Menu>
                    </div>
                )}
            </Toolbar>
        </AppBar>
    )
}

export default Header;