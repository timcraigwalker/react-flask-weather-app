import { createAsyncThunk, createSlice } from '@reduxjs/toolkit';

export const authRegister = createAsyncThunk(
    "authRegister",
    async (user, { rejectWithValue }) => {
        const requestOptions = {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(user),
            credentials: "include"
        };

        try {
            const response = await fetch("api/auth/register", requestOptions);
            if(response.ok) return await response.json();
            return rejectWithValue(await response.json());
        } catch (error) {
            return rejectWithValue(error.response.json());
        }
    }
);

export const authLogin = createAsyncThunk(
    "authLogin",
    async (user, { rejectWithValue }) => {
        const requestOptions = {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(user),
            credentials: "include"
        };

        try {
            const response = await fetch("api/auth/login", requestOptions);
            if(response.ok) return await response.json();
            return rejectWithValue(await response.json());
        } catch (error) {
            return rejectWithValue(error.response.json());
        }
    }
);

export const authLogout = createAsyncThunk("authLogout", async (_, { rejectWithValue }) => {
    try {
        const response = await fetch("api/auth/logout");
        return response.json();
    } catch (error) {
        return rejectWithValue(error.response.json());
    }
});

const authSlice = createSlice({
    name: "auth",
    initialState: {
        isLoading: false,
        authorized: false,
        isError: false,
        error: {}
    },
    extraReducers: (builder) => {
        // Auth Register Cases
        builder.addCase(authRegister.pending, (state, action) => {
            state.isLoading = true;
        })
        builder.addCase(authRegister.fulfilled, (state, action) => {
            state.isLoading = false;
            state.authorized = true;
        })
        builder.addCase(authRegister.rejected, (state, action) => {
            state.isError = true;
            state.error = action.payload;
        })
        // Auth Login Cases
        builder.addCase(authLogin.pending, (state, action) => {
            state.isLoading = true;
        })
        builder.addCase(authLogin.fulfilled, (state, action) => {
            state.isLoading = false;
            state.authorized = true;
        })
        builder.addCase(authLogin.rejected, (state, action) => {
            state.isError = true;
            state.error = action.payload;
        })
        // Auth Logout Cases
        builder.addCase(authLogout.pending, (state, action) => {
            state.isLoading = true;
        })
        builder.addCase(authLogout.fulfilled, (state, action) => {
            state.isLoading = false;
            state.authorized = false;
        })
        builder.addCase(authLogout.rejected, (state, action) => {
            state.isError = true;
        })
    }
});

export default authSlice.reducer;

