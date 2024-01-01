import React from "react";
import OrderCard from "./OrderCard";
import { OrderInfo } from "../../redux/order/orderSlice";

interface OrderListProps {
    orders: OrderInfo[];
}

const OrderItem: React.FC<OrderListProps> = ({ orders }) => {
    return (
        <div className="flex justify-between items-center pt-4">
            {orders.map((order: OrderInfo) => (
                <OrderCard key={order.id} order={order} />
            ))}
        </div>
    );
};

export default OrderItem;
