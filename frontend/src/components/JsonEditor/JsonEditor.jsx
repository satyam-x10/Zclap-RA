import React, { useState, useEffect } from "react";
import Editor from "@monaco-editor/react";
import "./JsonEditor.css";
import { DefaultEvaluationCriteria } from "../../utils/Constants";

export default function JsonEditor({setJsonData}) {
  const onChange = (updatedJson) => {
    console.log("Updated JSON:", updatedJson);
  };

  const [json, setJson] = useState(DefaultEvaluationCriteria);
  const [editorValue, setEditorValue] = useState(JSON.stringify(json, null, 2));
  const [error, setError] = useState(null);

  useEffect(() => {
    if (DefaultEvaluationCriteria) {
      setJson(DefaultEvaluationCriteria);
      setJsonData(DefaultEvaluationCriteria);
      setEditorValue(JSON.stringify(DefaultEvaluationCriteria, null, 2));
    }
  }, [DefaultEvaluationCriteria]);

  const handleEditorChange = (value) => {
    setEditorValue(value);
    try {
      if (value) {
        const parsed = JSON.parse(value);
        setJson(parsed);
        setJsonData(parsed);
        setError(null);
        onChange && onChange(parsed);
      }
    } catch (e) {
      setError(e.message);
    }
  };

  const copyToClipboard = () => {
    navigator.clipboard.writeText(editorValue);
    const button = document.getElementById("copy-button");
    const originalText = button.innerText;
    button.innerText = "Copied!";
    setTimeout(() => {
      button.innerText = originalText;
    }, 2000);
  };

  const formatJson = () => {
    try {
      const parsed = JSON.parse(editorValue);
      const formatted = JSON.stringify(parsed, null, 2);
      setEditorValue(formatted);
    } catch (e) {
      setError(e.message);
    }
  };

  return (
    <div className="json-editor-container">
      <div className="editor-header">
        <h2 className="editor-title">JSON Editor</h2>
        <div className="editor-actions">
          <button
            id="copy-button"
            className="action-button"
            onClick={copyToClipboard}
            title="Copy to clipboard"
          >
            Copy
          </button>
          <button
            className="action-button"
            onClick={formatJson}
            title="Format JSON"
          >
            Format
          </button>
        </div>
      </div>

      <div className="editor-content">
        <Editor
          // height="400px"
          defaultLanguage="json"
          value={editorValue}
          theme="vs-dark"
          onChange={handleEditorChange}
          options={{
            minimap: { enabled: false },
            fontSize: 20,
            scrollBeyondLastLine: false,
            folding: true,
            lineNumbers: "on",
            renderLineHighlight: "all",
            tabSize: 2,
            formatOnPaste: true,
            automaticLayout: true,
            scrollbar: {
              vertical: "auto",
              horizontal: "auto",
            },
          }}
        />
      </div>

      {error ? (
        <div className="editor-footer error">
          <span className="error-icon">⚠️</span> {error}
        </div>
      ) : (
        <div className="editor-footer">
          <span className="status-text">Valid JSON</span>
          <span className="json-stats">
            {Object.keys(json).length} top-level keys | {editorValue.length}{" "}
            characters
          </span>
        </div>
      )}
    </div>
  );
}
