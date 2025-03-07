
// const Navbar = () => {
//   return (
//     <>
//     <nav className='bg-white/50 backdrop-blur-md border border-white/30 p-4 w-full h-16 text-white flex justify-between items-center'> 
//     <div className="text-xl font-bold">MyApp</div>
//     {/* <button id="sidebarToggle" className="md:hidden bg-blue-700 p-2 rounded">☰</button> */}
//     <div className="hidden md:flex space-x-4">
//       <a href="#" className="hover:underline">Home</a>
//       <a href="#" className="hover:underline">About</a>
//       <a href="#" className="hover:underline">Contact</a>
//     </div>
    
//     </nav>
//     <div className="max-w-60    h-screen bg-white/50 backdrop-blur-md border border-white/30 text-white">
//       <ul className="p-4 space-y-4">
//         <li><a href="#" className="block hover:bg-blue-800 p-2 rounded">Profile</a></li>
//         <li><a href="#" className="block hover:bg-blue-800 p-2 rounded">Trending</a></li>
//         <li><a href="#" className="block hover:bg-blue-800 p-2 rounded">Message</a></li>
//         <li><a href="#" className="block hover:bg-blue-800 p-2 rounded">Settings</a></li>
//         <li><a href="#" className="block hover:bg-blue-800 p-2 rounded">Job</a></li>
//         <li><a href="#" className="block hover:bg-blue-800 p-2 rounded">Logout</a></li>
        
//       </ul>
    
    
//     </div>




//     </>

//   )
// }

// export default Navbar


const Navbar = () => {
  return (
    <nav className="bg-white/50  text-white p-4 flex justify-between items-center ">
        <div className="hidden md:flex space-x-4">
        <a href="#" className="hover:underline">Home</a>
      
      </div>
      <input type="text" placeholder="Search" className="px-10 py-1 border-2 text-black rounded-lg focus:outline-none w-130"/>
      <div className="flex items-center space-x-4">
       
      <button  className=" bg-blue-700 p-2 rounded">
        POST
      </button>
      <img src="./assets/images/pp.jpg" alt="User Profile"  className="w-13 h-13 border-2 rounded-full"
    />
      
      </div>
    </nav>
  );
};

export default Navbar;
