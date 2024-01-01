import { useDispatch, useSelector } from "react-redux";
import OrderItem from "./OrderItem";
import { OrderReducer, UserReducer } from "../../store/store";
import { useEffect } from "react";
import axios, { AxiosError, AxiosResponse } from "axios";
import { ORDER_URL } from "../../axiosConfig";
import { allOrder } from "../../redux/order/orderSlice";

function AllOrder() {
    const dispatch = useDispatch();
    const orders = useSelector((state: OrderReducer) => state.order.orders);
    const id = useSelector((state: UserReducer) => state.user.data?.user_id);
    const userData = useSelector((state: UserReducer) => state.user.data);

    const token = userData?.token?.access;

    useEffect(() => {
        if (token) {
            axios
                .get(`${ORDER_URL}/order/${id}/`, {
                    headers: {
                        Authorization: `Bearer ${token}`,
                    },
                })
                .then((response: AxiosResponse) => {
                    console.log(response.data);
                    dispatch(allOrder(response.data.orders));
                })
                .catch((err: AxiosError) => {
                    console.log(err, "err");
                });
        }
    }, [id, token]);

    return (
        <div className="app">
            <h1 className="text-center font-bold text-3xl">Order List</h1>
            <OrderItem orders={orders} />
        </div>
    );
}

export default AllOrder;
