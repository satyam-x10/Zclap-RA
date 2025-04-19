import { Editor } from "@monaco-editor/react";
import React, { useEffect, useState } from "react";
import { DefaultEvaluationCriteria } from "../../utils/Constants";
import { useAppContext } from "../../context/AppContext";

const JsonOutput = () => {
  const { editorValue } =
    useAppContext();

  return (
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
  );
};

export default JsonOutput;
