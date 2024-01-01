import { useDispatch, useSelector } from "react-redux";
import ProductList from "./ProductList";
import { useEffect } from "react";
import { PRODUCT_URL } from "../../axiosConfig";
import axios, { AxiosError, AxiosResponse } from "axios";
import { allProduct } from "../../redux/product/productSlice";
import type { ProductReducer } from "../../store/store";

function AllProduct() {
    const dispatch = useDispatch();
    const products = useSelector((state: ProductReducer) => state.product.products);

    useEffect(() => {
        axios
            .get(`${PRODUCT_URL}/product/all/`)
            .then((response: AxiosResponse) => {
                console.log(response.data.products);
                dispatch(allProduct(response.data.products));
            })
            .catch((err: AxiosError) => {
                console.log(err, "err");
            });
    }, []);

    return (
        <div className="app">
            <h1 className="text-center font-bold text-3xl">Product List</h1>
            <ProductList products={products} />
        </div>
    );
}

export default AllProduct;
