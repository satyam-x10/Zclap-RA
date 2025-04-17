export const DefaultEvaluationCriteria = {
  generation_prompt: "A tiger walking through a jungle",
  frame_sampling_rate: 2,
  pipeline_mode: "bus", // One of: bus, ring, star , tree 
  report_format: "detailed", // One of: minimal, detailed, verbose, pdf
  criteria : {
    ingestion: [
      "video_ingestion_agent"
    ],
    analysis: [
      "temporal_analysis_agent",
      "semantic_analysis_agent",
      "dynamics_robustness_agent", 
      "generalization_agent"
    ],
    feature_extractor: [
      "perception_agent" 
    ],
    synthesis: [
      "reasoning_agent"
    ],
    reporting: [
      "reporting_agent"
    ],
    controller: [
      "coordinator_agent"
    ],
    others: []
  }  
};


export const ProjectDescriptionPrimary =
  "After uploading the video, you can proceed to the next step where this file will be used for analysis or processing. This tool supports temporal segmentation, AI-based labeling, and preview playback directly from the browser. Please ensure your video is trimmed and properly formatted.";
export const ProjectDescriptionSecondary =
  "If you have any questions or need assistance, please refer to our documentation or contact support.";
