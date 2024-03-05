import { Avatar, Box, Button, Container, CssBaseline, TextField, Typography } from "@mui/material";
import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Link } from 'react-router-dom';
import { authRegister } from "../redux/slices/authSlice";

const Register = () => {
    const dispatch = useDispatch();
    const auth = useSelector((state) => state.auth);

    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [confirmPassword, setConfirmPassword] = useState("");
    const [registerErrorMessage, setRegisterErrorMessage] = useState(null);

    const handleRegistration = () => {
        // TODO: Check email and password are set before calling endpoint
        // TODO: Check password and confirm password match
        dispatch(authRegister({email, password}));
    }

    useEffect(() => {
        if(auth?.isError) {
            setRegisterErrorMessage(auth.error?.message);
        }
    }, [auth])

    return (
        <>
            <Container component="main" maxWidth="xs">
                <CssBaseline />
                <Box 
                    sx={{
                        marginTop: 8,
                        display: 'flex',
                        flexDirection: 'column',
                        alignItems: 'center',
                    }}
                >
                    <Avatar sx={{ m: 1, bgcolor: 'secondary.main' }} ></Avatar>
                    <Typography component="h1" variant="h5">
                        Register
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
                            value={password}
                            onChange={(e) => setPassword(e.target.value)} 
                        />
                        <TextField
                            margin="normal"
                            required
                            fullWidth
                            name="confirmPassword"
                            label="Confirm Password"
                            type="password"
                            id="confirmPassword"
                            value={confirmPassword}
                            onChange={(e) => setConfirmPassword(e.target.value)} 
                        />
                        {registerErrorMessage}
                        <Button
                            type="button"
                            fullWidth
                            variant="contained"
                            sx={{ mt: 3, mb: 2 }}
                            onClick={handleRegistration}
                        >
                            Register
                        </Button>
                        <Link to="/login" variant="body2">
                            {"Already have an account? Login"}
                        </Link>
                    </Box>
                </Box>
            </Container>
        </>
    );
};
 
export default Register;