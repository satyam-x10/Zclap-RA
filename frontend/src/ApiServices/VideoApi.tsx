import axios from "axios";

const BASE_URL = "http://localhost:8000/api";

export const fetchVideoData = async (videoAndConfigData) => {

  console.log("Video and config data:", videoAndConfigData);
  
  try {
    const formData = new FormData();
    formData.append("jsonData", JSON.stringify(videoAndConfigData.jsonData)); // Convert JSON to string
    formData.append("fileData", videoAndConfigData.fileData); // Raw File object

    const res = await axios.post(`${BASE_URL}/analyse`, formData, {
      headers: {
        "Content-Type": "multipart/form-data",
      },
    });

    return res.data;
  } catch (err) {
    console.error("Error fetching video data:", err);
    throw err;
  }
};
