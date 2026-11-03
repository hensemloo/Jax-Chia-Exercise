function UserCard({name = "Anonymous", role = "User",age = 0,isActive = false}) {
  return (
    <div>
      <h2>{name}</h2>
      <p> Age:{age}</p>
      <p> Role:{role}</p>
      <p> Status:{isActive ? "Active" : "Inactive"}</p>
    </div>
  );
}

export default UserCard;