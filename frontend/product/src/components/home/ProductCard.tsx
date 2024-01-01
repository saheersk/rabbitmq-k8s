import axios, { AxiosError, AxiosResponse } from "axios";
import { ProductInfo } from "../../redux/product/productSlice";
import { PRODUCT_URL } from "../../axiosConfig";
import { useSelector } from "react-redux";
import { UserReducer } from "../../store/store";

interface ProductListProps {
    product: ProductInfo;
}

const ProductCard: React.FC<ProductListProps> = ({ product }) => {
    const userData = useSelector((state: UserReducer) => state.user.data);

    const token = userData?.token?.access;

    const handleOrder = (id: number) => {
        axios
            .post(`${PRODUCT_URL}/product/add/${id}/`)
            .then((response: AxiosResponse) => {
                console.log(response.data);
            })
            .catch((err: AxiosError) => {
                console.log(err, "err");
            });
    };

    return (
        <div className="w-[33%] max-w-xs mx-auto overflow-hidden bg-white shadow-lg rounded-lg">
            <img className="w-full h-48 object-cover" src={product.image} alt={product.title} />
            <div className="p-4">
                <h3 className="text-xl font-medium text-gray-800">{product.title}</h3>
                <p className="mt-2 text-gray-600">{product.description}</p>
                <button
                    onClick={() => handleOrder(product.id)}
                    className="mt-4 bg-blue-500 text-white rounded-full px-4 py-2 hover:bg-blue-700"
                >
                    Add to Order
                </button>
            </div>
        </div>
    );
};

export default ProductCard;
