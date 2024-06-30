import CameraButton from "@/app/components/CameraButton";
import { Button } from "@vechain/dapp-kit-ui";

export default function Page() {
  return (
    <div className="flex flex-col gap-20">
      <div className="flex flex-row gap-20">
        <div className="flex flex-col">
        <p>Trash Item</p>
        <CameraButton/>
        </div>
        
        <div className="flex flex-col">
        <p>Trash Bin</p>
        <CameraButton/>
        </div>
      </div>
      <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 border border-blue-700 rounded w-1/5">
      Generate
    </button>
    </div>
  )
}
