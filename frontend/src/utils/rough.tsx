export const response = {
    "analysis": {
        "aesthetic_agent": {
            "brightness_mean": 101.36,
            "brightness_std": 11.7,
            "bad_brightness_ratio": 0,
            "avg_colorfulness": 18.5,
            "aesthetic_score": 0.185,
            "summary": "Poor visual aesthetics — likely dull, noisy, or overexposed frames."
        },
        "caption_alignment_agent": {
            "filtered_prompt_words": [
                "full",
                "walking",
                "skateboarding",
                "car",
                "other",
                "street",
                "traffics",
                "people",
                "pigeons",
                "pigeon"
            ],
            "matched_words": [
                "walking",
                "car",
                "street",
                "pigeons",
                "pigeon"
            ],
            "match_ratio": 0.5,
            "summary": "Moderate reflection of prompt."
        },
        "dynamics_robustness_agent": {
            "dynamics_robustness_score": 0.459,
            "high_motion_zones": [
                8,
                10
            ],
            "scene_transitions": [],
            "summary": "Significant loss of consistency during dynamic scenes."
        },
        "generalization_agent": {
            "generalisation_score": 0.49050000309944153,
            "diversity_index": 0.8,
            "repetition_ratio": 0.2,
            "visual_variability": 0.16580000519752502,
            "semantic_score": 0.5737,
            "matched_tags": [
                "walking",
                "car",
                "street",
                "pigeons",
                "pigeon"
            ],
            "overfitting_warning": false,
            "most_common_sentence": "a person riding a skateboard down a street",
            "summary": "Poor generalization — high redundancy or overfitting."
        },
        "motion_agent": {
            "motion_mean": 14.3738,
            "motion_std_dev": 4.5157,
            "motion_min": 0,
            "motion_max": 19.665,
            "burst_frames": [
                8,
                10
            ],
            "static_frames": [
                0
            ],
            "summary": "Mostly stable motion with a few active regions."
        },
        "perception_agent": {
            "visual_embeddings": null,
            "semantic_tags": null,
            "unique_tags": [
                "middle",
                "running",
                "riding",
                "group",
                "skateboarder",
                "flying",
                "front",
                "pigeon",
                "down",
                "person",
                "rides",
                "car",
                "bird",
                "skateboard",
                "york",
                "busy",
                "pigeons",
                "over",
                "walking",
                "birds",
                "new",
                "air",
                "sitting",
                "cat",
                "skates",
                "city",
                "street",
                "across"
            ],
            "motion_vectors": null,
            "scene_changes": [
                false,
                false,
                false,
                false,
                false,
                false,
                false,
                false,
                false,
                false,
                false,
                false,
                false,
                false,
                false
            ],
            "brightness_series": [
                93.85442418981482,
                88.22328125,
                76.43469618055556,
                90.6869849537037,
                99.10844618055556,
                102.43451967592593,
                105.03334780092592,
                117.58670138888888,
                114.24506944444444,
                116.00817708333334,
                118.49377025462962,
                106.17765625,
                91.33096354166666,
                98.73363715277777,
                102.0140943287037
            ]
        },
        "reasoning_agent": {
            "reasoning_trace": [
                "Temporal coherence is 0.77, indicating inconsistent transitions.",
                "Semantic consistency is 0.57, suggesting semantic drift.",
                "Dynamics robustness score is 0.46, reflecting how stable the video remains under motion.",
                "Generalization score is 0.49, showing how well the video avoids overfitting and redundancy.",
                "Prompt-to-caption alignment is 0.50, indicating prompt relevance.",
                "Semantic redundancy is 0.20, moderate or low repetition.",
                "Aesthetic score is 0.18, which suggests visual issues."
            ],
            "summary": "Temporal coherence is 0.77, indicating inconsistent transitions. Semantic consistency is 0.57, suggesting semantic drift. Dynamics robustness score is 0.46, reflecting how stable the video remains under motion. Generalization score is 0.49, showing how well the video avoids overfitting and redundancy. Prompt-to-caption alignment is 0.50, indicating prompt relevance. Semantic redundancy is 0.20, moderate or low repetition. Aesthetic score is 0.18, which suggests visual issues."
        },
        "redundancy_agent": {
            "semantic_redundancy": 0.2,
            "visual_variability": 0.16580000519752502,
            "summary": "Moderate redundancy — content repeats observed."
        },
        "reporting_agent": {
            "scorecard": {
                "temporal": 0.7743,
                "semantic": 0.5737,
                "dynamics": 0.459,
                "generalization": 0.4905,
                "aesthetic": 0.185,
                "redundancy": 0.8,
                "caption_alignment": 0.5
            },
            "average_score": 0.5404,
            "verdict": "Moderate quality with room for improvement.",
            "reasoning_trace": [
                "Temporal coherence is 0.77, indicating inconsistent transitions.",
                "Semantic consistency is 0.57, suggesting semantic drift.",
                "Dynamics robustness score is 0.46, reflecting how stable the video remains under motion.",
                "Generalization score is 0.49, showing how well the video avoids overfitting and redundancy.",
                "Prompt-to-caption alignment is 0.50, indicating prompt relevance.",
                "Semantic redundancy is 0.20, moderate or low repetition.",
                "Aesthetic score is 0.18, which suggests visual issues."
            ],
            "summary": "Temporal coherence is 0.77, indicating inconsistent transitions. Semantic consistency is 0.57, suggesting semantic drift. Dynamics robustness score is 0.46, reflecting how stable the video remains under motion. Generalization score is 0.49, showing how well the video avoids overfitting and redundancy. Prompt-to-caption alignment is 0.50, indicating prompt relevance. Semantic redundancy is 0.20, moderate or low repetition. Aesthetic score is 0.18, which suggests visual issues."
        },
        "semantic_analysis_agent": {
            "semantic_consistency_score": 0.5737,
            "semantic_segments": null,
            "entity_map": null,
            "sample_tags": [
                "a group of pigeons are running down the street",
                "a group of birds are flying over a street",
                "a group of pigeons are flying in the air",
                "a pigeon is on the street",
                "a bird is sitting on the street in the middle of the city",
                "a cat is walking across the street in a city",
                "a person riding a skateboard down a street",
                "a skateboarder is riding down the street",
                "a pigeon skates across a busy street in new york",
                "a bird is riding on the street in the city"
            ]
        },
        "temporal_analysis_agent": {
            "temporal_coherence": 0.7743,
            "mean_motion": 15.4005,
            "motion_std_dev": 2.457,
            "spike_frames": [],
            "scene_transitions": []
        },
        "transition_agent": {
            "hard_cut_frames": [],
            "semantic_transitions": [],
            "transition_density": 0,
            "summary": "Mostly continuous scenes with minimal cuts."
        },
        "video_ingestion_agent": {
            "frames": null,
            "metadata": {
                "original_fps": 30,
                "target_fps": 3,
                "frame_dimensions": [
                    720,
                    480
                ],
                "duration_seconds": 5,
                "total_frames_extracted": 15
            }
        }
    },
    "frame_rate": 3,
    "meta_agents": [
        "reasoning_agent",
        "reporting_agent"
    ],
    "parsed_config_json": {
        "video_file": "Sora_3.mp4",
        "prompt": "a pigeon skateboarding with other pigeons in a street full of people walking and car traffics",
        "frame_rate": 3,
        "pipeline_mode": "sequential",
        "report_format": "summary",
        "agents": {
            "primary_agents": [
                "video_ingestion_agent",
                "perception_agent",
                "temporal_analysis_agent",
                "semantic_analysis_agent",
                "dynamics_robustness_agent",
                "generalization_agent"
            ],
            "secondary_agents": [
                "aesthetic_agent",
                "motion_agent",
                "redundancy_agent",
                "transition_agent",
                "caption_alignment_agent"
            ],
            "meta_agents": [
                "reasoning_agent",
                "reporting_agent"
            ]
        }
    },
    "pipeline_mode": "sequential",
    "primary_agents": [
        "video_ingestion_agent",
        "perception_agent",
        "temporal_analysis_agent",
        "semantic_analysis_agent",
        "dynamics_robustness_agent",
        "generalization_agent"
    ],
    "prompt": "a pigeon skateboarding with other pigeons in a street full of people walking and car traffics",
    "report_format": "summary",
    "secondary_agents": [
        "aesthetic_agent",
        "motion_agent",
        "redundancy_agent",
        "transition_agent",
        "caption_alignment_agent"
    ],
    "video_file_path": "data/uploads\\20250421014144_Sora_3.mp4",
    "conversations": {
        "messages": [
            {
                "agent": "video_ingestion_agent",
                "content": "The video has poor aesthetic quality due to likely dullness, noise, or overexposure in the frames.  \n"
            },
            {
                "agent": "perception_agent",
                "content": "The video exhibits poor aesthetic quality, likely due to dullness, noise, or overexposure in the frames, as indicated by a low aesthetic score (0.185) and a brightness mean value suggesting  potential variations.    \n"
            },
            {
                "agent": "semantic_analysis_agent",
                "content": "The video exhibits poor aesthetic quality, likely due to dullness, noise, or overexposure, indicated by a low aesthetic score (0.185) . Further analysis reveals significant variations in brightness.  \n"
            },
            {
                "agent": "temporal_analysis_agent",
                "content": "The video exhibits poor temporal coherence (0.7743), indicating inconsistent transitions.  This weak coherence likely contributes to the overall poor aesthetic quality of the video.  \n"
            },
            {
                "agent": "dynamics_robustness_agent",
                "content": "The video exhibits poor aesthetic quality likely due to dullness, noise, or overexposure as indicated by a very low aesthetic score (0.185) and reports of  brightness variations.  \n"
            },
            {
                "agent": "generalization_agent",
                "content": "The video exhibits poor aesthetic quality due to low brightness, variations in brightness, and potential noise or dullness. \n\n\nAdditionally, it lacks generalization, showing high redundancy and potentially overfitting.  \n"
            },
            {
                "agent": "motion_agent",
                "content": "The video exhibits poor aesthetic quality due to low brightness, variations in brightness, and potential noise or dullness in the frames. Motion is mostly stable with a few active regions (frames 8 and 10) but generally lacks strong visual dynamism. \n\n\n"
            },
            {
                "agent": "transition_agent",
                "content": "The video exhibits poor aesthetic quality due to low brightness, significant variations in brightness, and potentially dull or noisy frames. \n\n\n"
            },
            {
                "agent": "caption_alignment_agent",
                "content": "The video exhibits poor aesthetic quality due to low brightness, significant brightness variations, and potentially dull or noisy frames. \n"
            },
            {
                "agent": "redundancy_agent",
                "content": "The video suffers from poor aesthetic quality likely due to dullness, noise, or overexposure, as indicated by the low aesthetic score (0.185) and variation in brightness. \n\nThere's moderate redundancy in the content, but generally the video lacks significant visual dynamism and exhibits inconsistent transitions.  \n"
            },
            {
                "agent": "aesthetic_agent",
                "content": "The video exhibits poor aesthetic quality due to low brightness, significant brightness variations, and potential dullness or noise.  The average brightness is 101.36 with a standard deviation of 11.7, which suggests inconsistency.  The low aesthetic score of 0.185 further supports this assessment. \n"
            },
            {
                "agent": "reasoning_agent",
                "content": "The video suffers from poor aesthetic quality due to dullness, noise, or overexposure. Brightness fluctuates significantly,  further contributing to the visual issues.  While the video isn't overly repetitive, it lacks strong visual dynamism and exhibits inconsistent transitions. \n"
            },
            {
                "agent": "reporting_agent",
                "content": "The video exhibits poor aesthetic quality due to several factors:\n\n* **Low brightness uniformity:** Significant fluctuations in brightness throughout the video contribute to a visually jarring experience.\n* **Potential dullness, noise, or overexposure:** These issues are indicated by a low aesthetic score and reported by multiple agents. \n* **Inconsistent transitions:** The video lacks smooth transitions, impacting its overall flow and coherence.\n\nWhile the video isn't overly repetitive, it lacks strong visual dynamism and exhibits inconsistent transitions, further detracting from its aesthetic appeal.  \n"
            }
        ]
    }
}