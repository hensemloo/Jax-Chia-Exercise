function Jsxexamples() {
  const name = "John Doe";
  const age = 30;
  const isStudent = true;
  const skills = ["JavaScript", "React", "Node.js"];
  const islearningReact = true;

  return(
    <div>{/* Single parent element*/}
    {/* 1.Embedding Javascript expressions */}
      <h1>Hello,{name}!</h1>

    {/* 2. Conditional rendering */}
     <p>{islearningReact ? "Currently learning React!" : "React expert"}</p>

    {/* 3. Using classname instead of class */}
        <div className="skill-container">
            <h3>Skills:</h3>

    {/* 4. Rendering lists */}        
     <ul>
        {skills.map((skills, index) => (
          <li key={index}>{skills}</li>
        ))}
      </ul>
    </div>

     {/* self-closing tags */}
    <img src="/vite.svg" alt="Vite logo" />
  <br />
  <hr />  
  </div>
  )
}

export default Jsxexamples;
   

