import Content from "./Content";
import { Trending } from "./trending";

const Main = ({ children}) => {
  return (
    <main className="flex-grow p-4 ">
      <div className="bg-white w-[100%] h-[100%]  grid grid-cols-[1.8fr_1fr] gap-1 ">
       <Content/>
       <Trending/>
      </div>
    </main>
  );
};

export default Main;

