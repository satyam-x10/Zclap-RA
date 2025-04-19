import React, { useState, useRef, useEffect } from "react";
import "./FilePicker.css"; // We'll define this CSS file content below
import useFile from "../../hooks/useFile";
export default function FilePicker() {
  const { file, setFile,isDragging,handleDrop,inputRef,handleSelectFile,preview,formatFileSize,videoRef } = useFile();

  return (
    <div className="file-picker-page">
      {/* TOP SECTION - VIDEO UPLOAD */}
      <div className="file-picker-container">
        <div className="file-picker-header">
          <h2 className="file-picker-title">Video Upload</h2>
          <p className="file-picker-subtitle">
            Select or drag a video file to upload
          </p>
        </div>

        {!file ? (
          <div
            className={`file-picker-dropzone ${isDragging ? "dragging" : ""}`}
            onDrop={handleDrop}
            onDragOver={(e) => e.preventDefault()}
            onDragEnter={(e) => handleDragEvents(e, "enter")}
            onDragLeave={(e) => handleDragEvents(e, "leave")}
            onClick={() => inputRef.current.click()}
          >
            <input
              ref={inputRef}
              type="file"
              accept="video/*"
              className="file-input"
              onChange={handleSelectFile}
            />

            <div className="file-picker-icon">
              {/* Video Icon */}
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="48"
                height="48"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                strokeWidth="2"
                strokeLinecap="round"
                strokeLinejoin="round"
              >
                <polygon points="23 7 16 12 23 17 23 7"></polygon>
                <rect x="1" y="5" width="15" height="14" rx="2" ry="2"></rect>
              </svg>
            </div>

            <p className="file-picker-prompt">
              {isDragging ? "Drop video here" : "Click or drag a video file"}
            </p>
            <p className="file-picker-hint">
              Supports MP4, WebM, MOV (max 1GB)
            </p>
          </div>
        ) : (
          <div className="file-preview-container">
            <div className="video-preview-wrapper">
              {preview && (
                <video
                  ref={videoRef}
                  src={preview}
                  className="video-preview"
                  controls
                />
              )}
            </div>

            <div className="file-info-container">
              <div className="file-info-content">
                <div className="file-details">
                  <h3 className="file-name" title={file.name}>
                    {file.name}
                  </h3>
                  <p className="file-metadata">
                    {file.type} • {formatFileSize(file.size)}
                  </p>
                </div>

                <div className="file-actions">
                  <button
                    onClick={() => inputRef.current.click()}
                    className="btn btn-secondary"
                  >
                    Replace
                  </button>
                  <button
                    onClick={() => setFile(null)}
                    className="btn btn-danger"
                  >
                    Remove
                  </button>
                </div>
              </div>
            </div>

            <input
              ref={inputRef}
              type="file"
              accept="video/*"
              className="file-input"
              onChange={handleSelectFile}
            />
          </div>
        )}

        <div className="file-size-info">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            className="info-icon"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth="2"
              d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
            />
          </svg>
          Maximum file size: 1GB
        </div>
      </div>

      {/* BOTTOM SECTION - DESCRIPTION BOX */}
      {/* <div className="file-description-box">
        <h3 className="description-title">Project Description</h3>
        <p className="description-text">
          {ProjectDescriptionPrimary}
        </p>
        <p className="description-text">
          {ProjectDescriptionSecondary}
        </p>
      </div>      
            */}
    </div>
  );
}
