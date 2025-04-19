import React from "react";
import JsonEditor from "../JsonEditor/JsonEditor";
import FilePicker from "../FilePicker/FilePicker";
import "./HomePage.css";
import { fetchVideoData } from "../../ApiServices/VideoApi";
import Result from "../Research/Result";

const HomePage = () => {
  const [jsonData, setJsonData] = React.useState<any>(null);
  const [fileData, setFileData] = React.useState<any>(null);
  const [haveResults, setHaveResults] = React.useState(false);
  const [responseData, setResponseData] = React.useState<any>(null);

  const [loading, setLoading] = React.useState(false);

  const handleNextStep = () => {
    console.log("JSON Data:", jsonData);
    console.log("File Data:", fileData);

    setHaveResults(false);
    setResponseData(null);
    setLoading(true);

    fetchVideoData({ jsonData, fileData })
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

  return (
    <div>
      {!haveResults && (
        <div>
          <div className="homepage-container">
            <div className="half-container">
              <JsonEditor setJsonData={setJsonData} />
            </div>
            <div className="half-container">
              <FilePicker setFileData={setFileData} />
            </div>
          </div>

          <button className="btn btn-primary next" onClick={handleNextStep}>
            {loading ? "Loading..." : "Next"}
          </button>
        </div>
      )}
      {haveResults && <Result response={responseData}  />}
    </div>
  );
};

export default HomePage;
