import { useAppContext } from "../context/AppContext";
import { fetchVideoData } from "../ApiServices/VideoApi";

export const useAppFunctions = () => {
  const {
    jsonData,
    fileData,
    setJsonData,
    setFileData,
    setHaveResults,
    setResponseData,
    setLoading,
  } = useAppContext();

  const handleNextStep = async () => {
    console.log("JSON Data:", jsonData);
    console.log("File Data:", fileData);

    setHaveResults(false);
    setResponseData(null);
    setLoading(true);

    await fetchVideoData({ jsonData, fileData })
      .then((data) => {
        console.log("Fetched video data:", data);
        setResponseData(data);
        setHaveResults(true);
      })
      .catch((error) => {
        console.error("Error fetching video data:", error);
      });
    setLoading(false);
  };

  return {
    handleNextStep,
  };
};
