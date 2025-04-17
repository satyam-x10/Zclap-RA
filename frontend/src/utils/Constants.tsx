export const DefaultEvaluationCriteria = {
  prompt: "A tiger walking through a jungle",
  frame_sampling_rate: 2,
  pipeline_mode: "default", // One of: default, ring, star , tree 
  report_format: "detailed", // One of: minimal, detailed, verbose, pdf
  criteria: {
    ingestion: {
      video_ingestion_agent: true,
    },
    analysis: {
      temporal_analysis_agent: true,
      semantic_analysis_agent: true,
      dynamics_robustness_agent: false,
      generalization_agent: true,
    },
    feature_extractor: {
      perception_agent: false,
    },
    synthesis: {
      reasoning_agent: true,
    },
    reporting: {
      reporting_agent: true,
    },
    controller: {
      coordinator_agent: true,
    },
  },
};

export const ProjectDescriptionPrimary =
  "After uploading the video, you can proceed to the next step where this file will be used for analysis or processing. This tool supports temporal segmentation, AI-based labeling, and preview playback directly from the browser. Please ensure your video is trimmed and properly formatted.";
export const ProjectDescriptionSecondary =
  "If you have any questions or need assistance, please refer to our documentation or contact support.";
