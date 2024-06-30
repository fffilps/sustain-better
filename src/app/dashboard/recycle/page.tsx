import CameraButton from "@/app/components/CameraButton";
import { Button } from "@vechain/dapp-kit-ui";

export default function Page() {
  return (
    <div className="flex flex-col gap-20 p-20 items-center">
      <div className="flex flex-row gap-20">
        {/* trash item capturing region */}
        <div className="max-w-sm bg-white border border-gray-200 rounded-lg shadow dark:bg-gray-800 dark:border-gray-700 text-white p-8">
          <h5 className="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">
            Trash Item
          </h5>
          <CameraButton />
        </div>

        {/* trash bin capturing region */}
        <div className="max-w-sm bg-white border border-gray-200 rounded-lg shadow dark:bg-gray-800 dark:border-gray-700 text-white p-8">
          <h5 className="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">
            Trash Bin
          </h5>
          <CameraButton />
        </div>
      </div>

      {/* button for image processing and detection using AI/tensorflow
      implement onClick() function */}
      <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 border border-blue-700 rounded w-1/5">
        Generate
      </button>
    </div>
  );
}
