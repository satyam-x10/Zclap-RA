import React from "react";
import { useAppContext } from "../../context/AppContext";
import useForm from "../../hooks/useForm";
import {
  ALL_AGENTS,
  PIPELINE_MODES,
  REPORT_FORMATS,
} from "../../utils/Constants";

const UserForm = () => {
  const { formData } = useAppContext();
  const { handleInputChange, handleAgentToggle } = useForm();

  return (
    <div>
      <div className="form-group">
        <label>Video File</label>
        <input
          className="not-editable"
          type="text"
          placeholder="Select a video file"
          value={formData.video_file || ""}
          onChange={(e) => handleInputChange("video_file", e.target.value)}
        />
      </div>
      <div className="form-group">
        <label>Prompt</label>
        <textarea
          placeholder="Enter the prompt that was used to generate the video"
          value={formData.prompt}
          onChange={(e) => handleInputChange("prompt", e.target.value)}
        />
      </div>
      <div className="form-group">
        <label>Frame Rate</label>
        <input
          type="number"
          placeholder="Enter the frame rate , default is 2"
          value={formData.frame_rate}
          onChange={(e) =>
            handleInputChange("frame_rate", parseInt(e.target.value) || 0)
          }
        />
      </div>
      <div className="form-group">
        <label>Pipeline Mode</label>
        <select
          value={formData.pipeline_mode}
          onChange={(e) => handleInputChange("pipeline_mode", e.target.value)}
        >
          {PIPELINE_MODES.map((mode) => (
            <option key={mode} value={mode}>
              {mode}
            </option>
          ))}
        </select>
      </div>
      <div className="form-group">
        <label>Report Format</label>
        <select
          value={formData.report_format}
          onChange={(e) => handleInputChange("report_format", e.target.value)}
        >
          {REPORT_FORMATS.map((format) => (
            <option key={format} value={format}>
              {format}
            </option>
          ))}
        </select>
      </div>
      <div className="form-group">
        <label>Select Agents by Category</label>
        {Object.entries(ALL_AGENTS).map(([category, agents]) => (
          <div key={category} style={{ marginBottom: "10px" }}>
            <strong style={{ textTransform: "capitalize" }}>
              {category.replace(/_/g, " ")}
            </strong>
            <div className="agent-checkbox-group">
              {agents.map((agent) => {
                const isPrimary = category === "primary_agent";

                return (
                  <label
                    key={agent}
                    style={{
                      display: "block",
                      marginLeft: "10px",
                      opacity: isPrimary ? 0.6 : 1,
                    }}
                  >
                    <input
                      type="checkbox"
                      checked={
                        isPrimary
                          ? true
                          : formData.agents[category]?.includes(agent)
                      }
                      disabled={isPrimary}
                      onChange={() => {
                        if (!isPrimary) {
                          handleAgentToggle(category, agent);
                        }
                      }}
                    />

                    {agent}
                  </label>
                );
              })}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default UserForm;
