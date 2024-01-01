import { createSlice } from '@reduxjs/toolkit';

export type ProductInfo = {
    id: number;
    title: string;
    description: string;
    image: string;
}

export type productData = {
    products: ProductInfo[];
}

type ProductPayload = {
    payload: ProductInfo[];
    type: string;
}

const initialState: productData = {
    products: [],
}

const productSlice = createSlice({
    name: "product",
    initialState,
    reducers: {
        allProduct: (state, action: ProductPayload) => {
            state.products = action.payload
        },
    }
});

export const { allProduct } = productSlice.actions;

export default productSlice.reducer;