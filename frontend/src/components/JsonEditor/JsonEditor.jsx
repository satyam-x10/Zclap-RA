import React, { useState, useEffect } from "react";
import "./JsonEditor.css";
import FilePicker from "../FilePicker/FilePicker";
import UserForm from "./VideoForm";
import JsonOutput from "./JsonOutput";

export default function ConfigAndFilePicker() {

  return (
    <div
      className="json-editor-container"
      style={{ display: "flex", flexDirection: "row", gap: "20px" }}
    >
      {/* FORM SIDE */}
      <div className="editor-form" style={{ flex: 1 }}>
        <h2 className="editor-title">Evaluation Config</h2>
        <UserForm />
        <FilePicker />
      </div>

      {/* READ-ONLY JSON EDITOR */}
      <JsonOutput />
    </div>
  );
}
