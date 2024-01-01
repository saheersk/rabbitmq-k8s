import { configureStore } from "@reduxjs/toolkit";
import userSlice, { type UserData } from "../redux/auth/userSlice";
import productSlice, { productData } from "../redux/product/productSlice";
import orderSlice, { orderData } from "../redux/order/orderSlice";


export interface UserReducer {
    user: UserData;
}

export interface ProductReducer {
    product: productData;
}

export interface OrderReducer {
    order: orderData;
}

const store = configureStore({
    reducer: {
        user: userSlice,
        product: productSlice,
        order: orderSlice
    }
});

export default store;