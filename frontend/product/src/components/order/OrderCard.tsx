import { OrderInfo } from "../../redux/order/orderSlice";

interface ProductListProps {
    order: OrderInfo;
  }


const OrderCard: React.FC<ProductListProps> = ({ order }) => {
  return (
    <div className="w-[33%] max-w-xs mx-auto overflow-hidden bg-white shadow-lg rounded-lg">
        <div className="p-4">
          <h3 className="text-xl font-medium text-gray-800">{order.product_name}</h3>
          <p className="mt-2 text-gray-600">{order.quantity}</p>
          <p className="mt-2 text-green-600">${order.order_date}</p>
        </div>
      </div>
  )
}

export default OrderCard