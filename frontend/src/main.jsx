import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import "./index.css";
import HomePage from "./components/HomePage/HomePage.js";
import { AppProvider } from "./context/AppContext.js";

createRoot(document.getElementById("root")).render(
  <StrictMode>
    <AppProvider>
      <HomePage />
    </AppProvider>
  </StrictMode>,
);
