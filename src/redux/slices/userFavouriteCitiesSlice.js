import { createAsyncThunk, createSlice } from '@reduxjs/toolkit';

export const fetchFavouriteCities = createAsyncThunk(
    "fetchFavouriteCities",
    async (user, { rejectWithValue }) => {
        try {
            const response = await fetch(`api/user/${user.id}/favourite_cities`);
            return response.json();
        } catch (error) {
            return rejectWithValue(error.response.json());
        }
    }
);

const userFavouriteCitiesSlice = createSlice({
    name: "userFavouriteCities",
    initialState: {
        isLoading: false,
        data: [],
        isError: false
    },
    extraReducers: (builder) => {
        // Fetch Favourite Cities Cases
        builder.addCase(fetchFavouriteCities.pending, (state, action) => {
            state.isLoading = true;
        })
        builder.addCase(fetchFavouriteCities.fulfilled, (state, action) => {
            state.isLoading = false;
            state.data = action.payload;
        })
        builder.addCase(fetchFavouriteCities.rejected, (state, action) => {
            state.isError = true;
        })
    }

});

export default userFavouriteCitiesSlice.reducer;