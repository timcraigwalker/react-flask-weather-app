import { configureStore } from '@reduxjs/toolkit';
import authReducer from './slices/authSlice';
import userFavouriteCitiesReducer from './slices/userFavouriteCitiesSlice';
import userReducer from './slices/userSlice';

export const store = configureStore({
    reducer: {
        user: userReducer,
        auth: authReducer,
        userFavouriteCities: userFavouriteCitiesReducer
    }
});