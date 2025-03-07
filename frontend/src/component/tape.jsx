import Sidebar from "./sidebar";
import Main from "./body"

const Tape = () => {
  return (
    <>
    <div className="h-screen flex flex-grow">
        <Sidebar/>
        <Main/>
      
    </div>
    </>
  )
}

export default Tape
