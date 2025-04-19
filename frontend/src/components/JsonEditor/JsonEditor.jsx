import React, { useState, useEffect } from "react";
import Editor from "@monaco-editor/react";
import "./JsonEditor.css";
import { DefaultEvaluationCriteria } from "../../utils/Constants";
import FilePicker from "../FilePicker/FilePicker";
import {
  PIPELINE_MODES,
  REPORT_FORMATS,
  ALL_AGENTS,
} from "../../utils/Constants";

export default function JsonEditor({ setJsonData, setFileData, fileData }) {
  const [formData, setFormData] = useState(DefaultEvaluationCriteria(fileData));
  const [editorValue, setEditorValue] = useState(
    JSON.stringify(DefaultEvaluationCriteria(fileData), null, 2)
  );

  useEffect(() => {
    setFormData(DefaultEvaluationCriteria(fileData));
    setEditorValue(
      JSON.stringify(DefaultEvaluationCriteria(fileData), null, 2)
    );
    setJsonData(DefaultEvaluationCriteria(fileData));
  }, [fileData]);

  const updateJson = (updated) => {
    setFormData(updated);
    const updatedStr = JSON.stringify(updated, null, 2);
    setEditorValue(updatedStr);
    setJsonData(updated);
  };

  const handleInputChange = (key, value) => {
    const updated = { ...formData, [key]: value };
    updateJson(updated);
  };

  const handleAgentToggle = (category, agent) => {
    const currentAgents = formData.agents[category] || [];
    const isSelected = currentAgents.includes(agent);

    const updatedAgents = isSelected
      ? currentAgents.filter((a) => a !== agent)
      : [...currentAgents, agent];

    const updated = {
      ...formData,
      agents: {
        ...formData.agents,
        [category]: updatedAgents,
      },
    };

    updateJson(updated);
  };

  return (
    <div
      className="json-editor-container"
      style={{ display: "flex", flexDirection: "row", gap: "20px" }}
    >
      {/* FORM SIDE */}
      <div className="editor-form" style={{ flex: 1 }}>
        <h2 className="editor-title">Evaluation Config</h2>
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
              onChange={(e) =>
                handleInputChange("pipeline_mode", e.target.value)
              }
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
              onChange={(e) =>
                handleInputChange("report_format", e.target.value)
              }
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
        <FilePicker setFileData={setFileData} />
      </div>

      {/* READ-ONLY JSON EDITOR */}
      <div className="editor-content" style={{ flex: 1 }}>
        <h2 className="editor-title">Live JSON Preview</h2>
        <Editor
          defaultLanguage="json"
          value={editorValue}
          theme="vs-dark"
          options={{
            readOnly: true,
            minimap: { enabled: false },
            fontSize: 16,
            scrollBeyondLastLine: false,
            folding: true,
            lineNumbers: "off",
            renderLineHighlight: "all",
            tabSize: 2,
            automaticLayout: true,
            lineHeight: 26,
            scrollbar: {
              vertical: "auto",
              horizontal: "auto",
            },
          }}
        />
      </div>
    </div>
  );
}
