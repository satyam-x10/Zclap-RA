export const response ={
    "received": true,
    "jsonData": {
        "generation_prompt": "A Pigeon skateboarding with other Pigeons in street full of people, few of the Pigeons are flying too",
        "target_frame_rate": 2,
        "pipeline_mode": "bus",
        "report_format": "detailed",
        "criteria": {
            "ingestion": [
                "video_ingestion_agent"
            ],
            "analysis": [
                "temporal_analysis_agent",
                "semantic_analysis_agent",
                "dynamics_robustness_agent",
                "generalization_agent"
            ],
            "feature_extractor": [
                "perception_agent"
            ],
            "synthesis": [
                "reasoning_agent"
            ],
            "reporting": [
                "reporting_agent"
            ],
            "controller": [
                "coordinator_agent"
            ],
            "others": []
        }
    },
    "fileData": {
        "filename": "Sora_3.mp4",
        "content_type": "video/mp4",
        "size": 0
    },
    "savedTo": "data/uploads\\20250419051008_Sora_3.mp4",
    "analysis": {
        "temporal_analysis": {
            "temporal_coherence": 0.8012999892234802,
            "motion_statistics": {
                "mean_motion": 13.3887,
                "motion_std_dev": 4.6877,
                "spike_frames": []
            },
            "scene_transitions": []
        },
        "semantic_analysis": {
            "semantic_consistency_score": 0.5916000008583069,
            "semantic_segments": [
                {
                    "start": 0,
                    "end": 0,
                    "tag": "a group of pigeons are running down the street"
                },
                {
                    "start": 1,
                    "end": 1,
                    "tag": "a group of pigeons flying over a city street"
                },
                {
                    "start": 2,
                    "end": 2,
                    "tag": "a pigeon is on the street"
                },
                {
                    "start": 3,
                    "end": 4,
                    "tag": "a person riding a skateboard down a street"
                },
                {
                    "start": 5,
                    "end": 5,
                    "tag": "a pigeon is walking across a zebra crossing street"
                },
                {
                    "start": 6,
                    "end": 6,
                    "tag": "a bird is riding on the street in the city"
                },
                {
                    "start": 7,
                    "end": 8,
                    "tag": "a person riding a skateboard down a street"
                },
                {
                    "start": 9,
                    "end": 9,
                    "tag": "a bird is sitting on the street next to a skateboard"
                }
            ],
            "entity_map": {
                "a": [
                    0,
                    9
                ],
                "group": [
                    0,
                    1
                ],
                "of": [
                    0,
                    1
                ],
                "pigeons": [
                    0,
                    1
                ],
                "are": [
                    0,
                    0
                ],
                "running": [
                    0,
                    0
                ],
                "down": [
                    0,
                    8
                ],
                "the": [
                    0,
                    9
                ],
                "street": [
                    0,
                    9
                ],
                "flying": [
                    1,
                    1
                ],
                "over": [
                    1,
                    1
                ],
                "city": [
                    1,
                    6
                ],
                "pigeon": [
                    2,
                    5
                ],
                "is": [
                    2,
                    9
                ],
                "on": [
                    2,
                    9
                ],
                "person": [
                    3,
                    8
                ],
                "riding": [
                    3,
                    8
                ],
                "skateboard": [
                    3,
                    9
                ],
                "walking": [
                    5,
                    5
                ],
                "across": [
                    5,
                    5
                ],
                "zebra": [
                    5,
                    5
                ],
                "crossing": [
                    5,
                    5
                ],
                "bird": [
                    6,
                    9
                ],
                "in": [
                    6,
                    6
                ],
                "sitting": [
                    9,
                    9
                ],
                "next": [
                    9,
                    9
                ],
                "to": [
                    9,
                    9
                ]
            }
        },
        "dynamics_robustness": {
            "dynamics_robustness_score": 0.5916000008583069,
            "high_motion_zones": [],
            "scene_transitions": [],
            "analysis": "Significant loss of consistency during dynamic scenes."
        },
        "generalization": {
            "generalisation_score": 0.4239000082015991,
            "diversity_index": 0.7,
            "repetition_ratio": 0.4,
            "visual_variability": 0.19869999587535858,
            "semantic_score": 0.5916,
            "matched_tags": [
                "flying",
                "pigeon",
                "in",
                "pigeons",
                "street"
            ],
            "overfitting_warning": false,
            "analysis": "Poor generalization — high redundancy or overfitting.",
            "most_common_sentence": "a person riding a skateboard down a street"
        },
        "reasoning": {
            "final_reasoning_score": 0.6105,
            "verdict": "Disjointed",
            "explanation": "🧠 Temporal Coherence: 0.80 | Semantic Score: 0.59 | Dynamics: 0.59 | Generalization: 0.42.\nVerdict: **Disjointed**.",
            "full_breakdown": {
                "semantic_summary": "Semantic performance not described.",
                "dynamics_analysis": "Significant loss of consistency during dynamic scenes.",
                "generalisation_analysis": "Poor generalization — high redundancy or overfitting."
            }
        }
    }
}