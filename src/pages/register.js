import { Avatar, Box, Button, Container, CssBaseline, TextField, Typography } from "@mui/material";
import React, { useState } from "react";
import { Link, useNavigate } from 'react-router-dom';

const Register = () => {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [confirmPassword, setConfirmPassword] = useState("");
    const [registerErrorMessage, setRegisterErrorMessage] = useState(null);
    const navigate = useNavigate();


    const handleRegistration = () => {
        // TODO: Check email and password are set before calling endpoint
        // TODO: Check password and confirm password match

        const requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email, password }),
            credentials: "include"
        };
        return fetch('api/auth/register', requestOptions)
        .then((response) => response.json())
        .then((responseJson) => {
            if (responseJson["id"]) {
                // Redirect to the home page after registration
                navigate("/"); 
            } else {
                setRegisterErrorMessage(responseJson["message"]);
            }
        })
        .catch((error) => {console.error(error);});
    }

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