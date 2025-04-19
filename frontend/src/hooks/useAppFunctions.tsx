import { useAppContext } from "../context/AppContext";
import { fetchVideoData } from "../ApiServices/VideoApi";

export const useAppFunctions = () => {
  const { jsonData, fileData, setHaveResults, setResponseData, setLoading } =
    useAppContext();

  const validatedata = () => {
    // Validate the jsonData and fileData here
    if (!fileData.name) {
      return false;
    }
    if (!jsonData.prompt) {
      return false;
    }

    return true;
  };

  const handleNextStep = async () => {
    const isValid = validatedata();
    if (!isValid) {
      console.error("Invalid data");
      alert("Please select a file and enter a prompt.");
      return;
    }

    setHaveResults(false);
    setResponseData(null);
    setLoading(true);

    await fetchVideoData({ jsonData, fileData })
      .then((data) => {
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
