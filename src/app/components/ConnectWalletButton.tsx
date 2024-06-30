"use client";
import React, { ReactElement, useEffect, useState } from "react";
import dynamic from "next/dynamic";
import {
  WalletButton,
  useWallet,
  WalletConnectOptions,
  useWalletModal,
} from "@vechain/dapp-kit-react";

import { Button } from "@chakra-ui/react";

const DAppKitProvider = dynamic(
  async () => {
    const { DAppKitProvider: _DAppKitProvider } = await import(
      "@vechain/dapp-kit-react"
    );
    return _DAppKitProvider;
  },
  {
    ssr: false,
  },
);

const walletConnectOptions: WalletConnectOptions = {
  projectId: "a0b855ceaf109dbc8426479a4c3d38d8",
  metadata: {
    name: "Sample VeChain dApp",
    description: "A sample VeChain dApp",
    url: typeof window !== "undefined" ? window.location.origin : "",
    icons: [
      typeof window !== "undefined"
        ? `${window.location.origin}/images/logo/my-dapp.png`
        : "",
    ],
  },
};

const ConnectWalletButton = (): ReactElement => {
  const [apiResponse, setApiResponse] = useState<object | undefined>();
  return (
    <DAppKitProvider
      genesis="test"
      logLevel="DEBUG"
      nodeUrl="https://testnet.vechain.org/"
      usePersistence
      walletConnectOptions={walletConnectOptions}
    >
      <div className="container">
        <WalletButton />
      </div>
    </DAppKitProvider>
  );
};

export default ConnectWalletButton;
