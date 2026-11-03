function ProductList(){
    const products = [
        {id:1,name:"Product 1",price:10},
        {id:2,name:"Product 2",price:20},
    ];

    return (
        <div className="product-list">
            {products.map(product => (
                <ProductCard key={product.id} {...product} />
            ))}
        </div>
    );
}

export default ProductList;