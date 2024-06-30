import CameraButton from "./components/CameraButton";
import ConnectWalletButton from "./components/ConnectWalletButton";
import LocationButton from "./components/LocationButton";
import WeatherApiButton from "./components/WeatherApiButton";


export default function Home() {
  return (
    <main>
      <div className="flex flex-col gap-3 divide-y-2 p-2">
        <h1 className="text-6xl">Sustain Better
          <ConnectWalletButton/>
          </h1>
        <LocationButton />
        <WeatherApiButton />
        <CameraButton />
      </div>
    </main>
  );
}
