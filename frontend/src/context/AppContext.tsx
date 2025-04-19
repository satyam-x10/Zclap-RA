import React, {
  createContext,
  useContext,
  useState,
  ReactNode,
  Dispatch,
  SetStateAction,
} from "react";
import { DefaultEvaluationCriteria } from "../utils/Constants";

// Define types
interface AppContextType {
  jsonData: any;
  setJsonData: Dispatch<SetStateAction<any>>;
  fileData: any;
  setFileData: Dispatch<SetStateAction<any>>;
  haveResults: boolean;
  setHaveResults: Dispatch<SetStateAction<boolean>>;
  responseData: any;
  setResponseData: Dispatch<SetStateAction<any>>;
  loading: boolean;
  setLoading: Dispatch<SetStateAction<boolean>>;
  formData: any;
  setFormData: Dispatch<SetStateAction<any>>;
}

// Create context with default (undefined will force provider use)
const AppContext = createContext<AppContextType | undefined>(undefined);

// Provider component
export const AppProvider = ({ children }: { children: ReactNode }) => {
  const [jsonData, setJsonData] = useState<any>(null);
  const [fileData, setFileData] = useState<any>({});
  const [formData, setFormData] = useState(DefaultEvaluationCriteria(fileData));

  const [haveResults, setHaveResults] = useState(false);
  const [responseData, setResponseData] = useState<any>(null);
  const [loading, setLoading] = useState(false);

  return (
    <AppContext.Provider
      value={{
        jsonData,
        setJsonData,
        fileData,
        setFileData,
        haveResults,
        setHaveResults,
        responseData,
        setResponseData,
        loading,
        setLoading,
        formData,
        setFormData,
      }}
    >
      {children}
    </AppContext.Provider>
  );
};

// Custom hook
export const useAppContext = (): AppContextType => {
  const context = useContext(AppContext);
  if (!context) {
    throw new Error("useAppContext must be used within an AppProvider");
  }
  return context;
};
