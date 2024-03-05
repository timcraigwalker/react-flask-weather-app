import { Avatar, Box, Button, Container, CssBaseline, Grid, TextField, Typography } from "@mui/material";
import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Link } from "react-router-dom";
import { authLogin } from "../redux/slices/authSlice";

const Login = () => {
    const dispatch = useDispatch();
    const auth = useSelector((state) => state.auth);

    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [loginErrorMessage, setLoginErrorMessage] = useState(null);

    const handleLogin = async () => {
        // TODO: Check email and password are set before calling endpoint
        dispatch(authLogin({email, password}));
    };

    useEffect(() => {
        if(auth?.isError) {
            setLoginErrorMessage(auth.error?.message);
        }
    }, [auth])

    return (
        <>
            <Container component="main" maxWidth="xs">
                <CssBaseline />
                <Box 
                    sx={{
                        marginTop: 8,
                        display: "flex",
                        flexDirection: "column",
                        alignItems: "center",
                    }}
                >
                    <Avatar sx={{ m: 1, bgcolor: "secondary.main" }} ></Avatar>
                    <Typography component="h1" variant="h5">
                        Log in
                    </Typography>
                    <Box sx={{ mt: 1 }}>
                        <TextField
                            margin="normal"
                            required
                            fullWidth
                            id="email"
                            label="Email Address"
                            name="email"
                            autoComplete="email"
                            autoFocus
                            value={email}
                            onChange={(e) => setEmail(e.target.value)}
                        />
                        <TextField
                            margin="normal"
                            required
                            fullWidth
                            name="password"
                            label="Password"
                            type="password"
                            id="password"
                            autoComplete="current-password"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)} 
                        />
                        {loginErrorMessage}
                        <Button
                            type="button"
                            fullWidth
                            variant="contained"
                            sx={{ mt: 3, mb: 2 }}
                            onClick={handleLogin}
                        >
                            Log In
                        </Button>
                        <Grid container>
                            <Grid item xs>
                                {/*<Link href="#" variant="body2">
                                    {"Forgot password?"}
                                </Link>*/}
                            </Grid>
                            <Grid item>
                                <Link to="/register" variant="body2">
                                    {"Don't have an account? Register"}
                                </Link>
                            </Grid>
                        </Grid>
                    </Box>
                </Box>
            </Container>
        </>
    );
};
 
export default Login;