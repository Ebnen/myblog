

const Sidebar = () => {
  return (
    <aside className="bg-white/50 backdrop-blur-md text-white w-64 p-4 ">
      <ul className="space-y-4">
        <li><a href="#" className="block hover:bg-blue-800 p-2 rounded">Home</a></li>
        <li><a href="#" className="block hover:bg-blue-800 p-2 rounded">Trending</a></li>
        <li><a href="#" className="block hover:bg-blue-800 p-2 rounded">Profile</a></li>
        <li><a href="#" className="block hover:bg-blue-800 p-2 rounded">Job</a></li>
        <li><a href="#" className="block hover:bg-blue-800 p-2 rounded">Settings</a></li>
        <li><a href="#" className="block hover:bg-blue-800 p-2 rounded">Logout</a></li>
      </ul>
    </aside>
  );
};

export default Sidebar;
