import { createAsyncThunk, createSlice } from '@reduxjs/toolkit';
import { authLogin, authLogout, authRegister } from './authSlice';

export const fetchUser = createAsyncThunk("fetchUser", async (_, {rejectWithValue}) => {
    try {
        const response = await fetch("api/user");
        if(response.ok) return response.json();
        return rejectWithValue("Unauthorized");
    } catch (error) {
        return rejectWithValue(error.response.json());
    }
});

const userSlice = createSlice({
    name: "user",
    initialState: {
        isLoading: false,
        data: {},
        isError: false
    },
    extraReducers: (builder) => {
        // Fetch User Cases
        builder.addCase(fetchUser.pending, (state, action) => {
            state.isLoading = true;
        })
        builder.addCase(fetchUser.fulfilled, (state, action) => {
            state.isLoading = false;
            state.data = action.payload;
        })
        builder.addCase(fetchUser.rejected, (state, action) => {
            state.isError = true;
        })
        // Auth User Cases
        builder.addCase(authRegister.fulfilled, (state, action) => {
            state.isLoading = false;
            state.data = action.payload;
        })
        builder.addCase(authLogin.fulfilled, (state, action) => {
            state.isLoading = false;
            state.data = action.payload;
        })
        builder.addCase(authLogout.fulfilled, (state, action) => {
            state.isLoading = false;
            state.data = {};
        })
    }
});

export default userSlice.reducer;

