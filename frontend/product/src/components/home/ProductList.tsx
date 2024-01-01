import { ProductInfo } from "../../redux/product/productSlice";
import ProductCard from "./ProductCard";

interface ProductListProps {
    products: ProductInfo[];
}

const ProductList: React.FC<ProductListProps> = ({ products }) => {

    return (
        <div className="flex justify-between items-center pt-4">
            {products.map((product: ProductInfo) => (
                <ProductCard key={product.id} product={product} />
            ))}
        </div>
    );
};

export default ProductList;
