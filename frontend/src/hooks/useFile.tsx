import React, { useEffect, useRef, useState } from "react";
import { useAppContext } from "../context/AppContext";

const useFile = () => {
  const { setFileData } = useAppContext();
  const [file, setFile] = useState();
  const [preview, setPreview] = useState(null);
  const [isDragging, setIsDragging] = useState(false);
  const inputRef = useRef(null);
  const videoRef = useRef(null);

  useEffect(() => {
    if (!file) {
      setPreview(null);
      return;
    }
    if (file.type.startsWith("video/")) {
      const objectUrl = URL.createObjectURL(file);
      setPreview(objectUrl);
      return () => URL.revokeObjectURL(objectUrl);
    }
  }, [file]);

  const handleFile = (f) => {
    if (!f) return;
    const maxSize = 1024 * 1024 * 1024; // 1 GB
    const isValidType = f.type.startsWith("video/");
    if (f.size <= maxSize && isValidType) {
      setFile(f);
      setFileData(f); // Pass the file to parent component
    } else {
      alert("File must be a video and less than 1GB.");
    }
  };

  const handleDragEvents = (e, type) => {
    e.preventDefault();
    if (type === "enter") setIsDragging(true);
    else if (type === "leave") setIsDragging(false);
  };

  const handleDrop = (e) => {
    e.preventDefault();
    setIsDragging(false);
    handleFile(e.dataTransfer.files[0]);
  };

  const handleSelectFile = (e) => {
    e.preventDefault();
    handleFile(e.target.files[0]);
  };
  const formatFileSize = (bytes) => {
    if (bytes < 1024) return bytes + " B";
    else if (bytes < 1024 * 1024) return (bytes / 1024).toFixed(2) + " KB";
    else return (bytes / (1024 * 1024)).toFixed(2) + " MB";
  };

  return {
    file,
    preview,
    isDragging,
    inputRef,
    videoRef,
    handleFile,
    handleDragEvents,
    handleDrop,
    handleSelectFile,
    formatFileSize,
  };
};

export default useFile;
