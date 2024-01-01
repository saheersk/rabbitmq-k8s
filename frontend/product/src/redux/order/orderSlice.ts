import { createSlice } from '@reduxjs/toolkit';

export type OrderInfo = {
    id: number;
    user_id: number;
    product_name: string;
    quantity: string;
    order_date: string;
}

export type orderData = {
    orders: OrderInfo[];
}

type OrderPayload = {
    payload: OrderInfo[];
    type: string;
}

const initialState: orderData = {
    orders: [],
}

const orderSlice = createSlice({
    name: "order",
    initialState,
    reducers: {
        allOrder: (state, action: OrderPayload) => {
            state.orders = action.payload
        },
    }
});

export const { allOrder } = orderSlice.actions;

export default orderSlice.reducer;