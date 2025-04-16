import React from "react";
import JsonEditor from "../JsonEditor/JsonEditor";
import FilePicker from "../FilePicker/FilePicker";
import "./HomePage.css";
import { fetchVideoData } from "../../ApiServices/VideoApi";

const HomePage = () => {
  const [jsonData, setJsonData] = React.useState<any>(null);
  const [fileData, setFileData] = React.useState<any>(null);

  const handleNextStep = () => {
    console.log("JSON Data:", jsonData);
    console.log("File Data:", fileData);

    
    fetchVideoData({ jsonData, fileData })
      .then((data) => {
        console.log("Fetched video data:", data);
      })
      .catch((error) => {
        console.error("Error fetching video data:", error);
      }
    );
  };

  return (
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
        Next Step
      </button>
    </div>
  );
};

export default HomePage;
