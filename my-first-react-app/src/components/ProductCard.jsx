function ProductCard({
  name = "Product Name",
  price = 0,
  image = "https://www-file.honor.com/content/dam/honor/global/products/smartphone/honor-magic7/assets/imgs/section-even/img1@2x.webp", // Changed to a sample breakfast image URL for display
  isOnSale = false,
}) {
  // Calculate a styled price string
  const formattedPrice = price > 0 ? `$${price.toFixed(2)}` : "Free";

  // Inline styles for demonstration (in a real app, use CSS Modules or a library)
  const cardStyle = {
    border: "1px solid #ddd",
    borderRadius: "8px",
    padding: "16px",
    width: "300px",
    fontFamily: "Arial, sans-serif",
    boxShadow: "0 2px 4px rgba(0,0,0,0.1)",
    margin: "10px",
  };

  const imageStyle = {
    width: "100%",
    height: "200px",
    objectFit: "cover", // Important for responsive images
    borderRadius: "4px",
  };

  const saleBadgeStyle = {
    position: "absolute",
    top: "10px",
    right: "10px",
    backgroundColor: "red",
    color: "white",
    padding: "4px 8px",
    borderRadius: "4px",
    fontWeight: "bold",
    fontSize: "12px",
  };

  return (
    <div style={{ ...cardStyle, position: "relative" }}>
      {isOnSale && <span style={saleBadgeStyle}>SALE</span>}
      <img src={image} alt={name} style={imageStyle} />
      <h3>{name}</h3>
      <p style={{ fontWeight: "bold", color: price > 0 ? "#333" : "green" }}>
        {formattedPrice}
      </p>
      <button
        style={{
          backgroundColor: "blue",
          color: "white",
          padding: "8px 16px",
          border: "none",
          borderRadius: "4px",
          cursor: "pointer",
        }}
      >
        Add to Cart
      </button>
    </div>
  );
}

export default ProductCard;
