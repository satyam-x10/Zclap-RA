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
import VideoForm from "./VideoForm";
import JsonOutput from "./JsonOutput";
import { useAppContext } from "../../context/AppContext";
export default function ConfigAndFilePicker() {
  const {
    setJsonData,
    fileData,
    setFileData,
    haveResults,
    responseData,
    loading,
    formData,
    setFormData,
  } = useAppContext();

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
        <VideoForm
          formData={formData}
          handleInputChange={handleInputChange}
          PIPELINE_MODES={PIPELINE_MODES}
          REPORT_FORMATS={REPORT_FORMATS}
          ALL_AGENTS={ALL_AGENTS}
          handleAgentToggle={handleAgentToggle}
        />
        <FilePicker setFileData={setFileData} />
      </div>

      {/* READ-ONLY JSON EDITOR */}
      <JsonOutput />
    </div>
  );
}
