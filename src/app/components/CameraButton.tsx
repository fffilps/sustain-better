"use client";
// source: https://www.npmjs.com/package/react-webcam
// source: https://dev.to/sababg/react-webcam-typescript-gh2
import { useRef, useState, useCallback } from "react";
import Webcam from "react-webcam";
import Image from "next/image";

const videoConstraints = {
  width: 720,
  height: 360,
  facingMode: "user",
};

export const CameraButton = () => {
  const [isCaptureEnable, setCaptureEnable] = useState<boolean>(false);
  const webcamRef = useRef<Webcam>(null);
  const [url, setUrl] = useState<string | null>(null);
  const capture = useCallback(() => {
    const imageSrc = webcamRef.current?.getScreenshot();
    if (imageSrc) {
      setUrl(imageSrc);
    }
  }, [webcamRef]);

  return (
    <div className="py-2">
      <header>
        <h1>camera app</h1>
      </header>
      {isCaptureEnable || (
        <button
          className="bordered rounded-md bg-orange-300 p-4"
          onClick={() => setCaptureEnable(true)}
        >
          start
        </button>
      )}
      {isCaptureEnable && (
        <>
          <div>
            <button onClick={() => setCaptureEnable(false)}>end </button>
          </div>
          <div>
            <Webcam
              audio={false}
              width={540}
              height={360}
              ref={webcamRef}
              screenshotFormat="image/jpeg"
              videoConstraints={videoConstraints}
            />
          </div>
          <button onClick={capture}>capture</button>
        </>
      )}
      {url && (
        <>
          <div>
            <button
              onClick={() => {
                setUrl(null);
              }}
            >
              delete
            </button>
          </div>
          <div>
            <Image
              src={url}
              alt="Screenshot"
              width={videoConstraints.width}
              height={videoConstraints.height}
            />
          </div>
        </>
      )}
    </div>
  );
};

export default CameraButton;
