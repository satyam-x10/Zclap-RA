import React from "react";
import ConfigAndFilePicker from "../JsonEditor/JsonEditor";
import "./HomePage.css";
import Result from "../Research/Result";
import { useAppContext } from "../../context/AppContext";
import { useAppFunctions } from "../../hooks/useAppFunctions";

const HomePage = () => {
  const { haveResults, loading } = useAppContext();
  const { handleNextStep } = useAppFunctions();

  return (
    <div>
      {!haveResults && (
        <div>
          <div className="homepage-container">
            <div className="half-container">
              <ConfigAndFilePicker />
            </div>
          </div>

          <button className="btn btn-primary next" onClick={handleNextStep}>
            {loading ? "Loading..." : "Next"}
          </button>
        </div>
      )}
      {haveResults && <Result />}
    </div>
  );
};

export default HomePage;
