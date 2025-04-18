import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))



from agents.video_ingestion_agent import run as ingest_video
from agents.temporal_analysis_agent import run as eval_temporal
from agents.semantic_analysis_agent import run as eval_semantic
from agents.dynamics_robustness_agent import run as eval_dynamics
from agents.generalization_agent import run as eval_generalization
from agents.perception_agent import run as extract_perception
from agents.reasoning_agent import run as reasoning_agent
from agents.reporting_agent import run as reporting_agent


# Actual agent function mapping
available_agents = {
    "video_ingestion_agent": ingest_video,
    "temporal_analysis_agent": eval_temporal,
    "semantic_analysis_agent": eval_semantic,
    "dynamics_robustness_agent": eval_dynamics,
    "generalization_agent": eval_generalization,
    "perception_agent": extract_perception,
    "reasoning_agent": reasoning_agent,
    "reporting_agent": reporting_agent
}

agent_pipeline = {
    "level_1": {
        "agents": ["video_ingestion_agent"],
        "output": ["video"]
    },
    "level_2": {
        "agents": ["perception_agent"],
        "input_from": "level_1",
        "output": ["features", "frames", "motion_vectors", "scene_boundaries"]
    },
    "level_3": {
        "agents": [
            "temporal_analysis_agent",
            "semantic_analysis_agent",
            "dynamics_robustness_agent",
            "generalization_agent"
        ],
        "input_from": "level_2",
        "output": ["aspect_scores", "reasoning", "flags"]
    },
    "level_4": {
        "agents": ["reasoning_agent"],
        "input_from": "level_3",
        "output": ["consolidated_insights", "summary", "recommendations"]
    },
    "level_5": {
        "agents": ["reporting_agent"],
        "input_from": "level_4",
        "output": ["final_report", "scorecard", "formatted_summary"]
    }
}


async def define_research_architecture(video_file="video.mp4"):
    data_store = {"video_file": video_file}

    for level in sorted(agent_pipeline.keys()):
        level_info = agent_pipeline[level]
        agent_names = level_info["agents"]
        print(f"Processing {level} with agents: {', '.join(agent_names)}")
        if "input_from" in level_info:
            prev_outputs = agent_pipeline[level_info["input_from"]]["output"]
            input_data = {k: data_store.get(k) for k in prev_outputs if k in data_store}
        else:
            input_data = {"video_file": video_file}

        for agent_name in agent_names:
            agent_fn = available_agents.get(agent_name)
            if agent_fn is None:
                print(f"Skipping agent '{agent_name}' — not available.")
                continue

            print(f"Running agent: {agent_name}")
            try:
                result = agent_fn(input_data)
                if isinstance(result, dict):
                    data_store.update(result)
                else:
                    data_store[agent_name] = result
            except Exception as e:
                print(f"Error in agent '{agent_name}': {e}")

    return data_store

async def  start_analysis (video_path,parsed_json):
    print(f"Starting analysis for video: {video_path}")
    # Example usage
    input_data = {
        "video_file": video_path,
        "prompt": parsed_json["generation_prompt"],
    }

    frames = await ingest_video(input_data,parsed_json["target_frame_rate"])
    perception_data = await extract_perception(frames)

    temporal_input = {
    "video_frames": frames["video_frames"],
    "motion_vectors": perception_data["motion_vectors"],
    "visual_embeddings": perception_data["features"]["visual_embeddings"],
    "semantic_tags": perception_data["features"]["semantic_tags"],
    "unique_tags": perception_data["features"]["unique_tags"],
}

    temporal_data = await eval_temporal(temporal_input)
    semantic_data = await eval_semantic(temporal_input)

    dynamic_robustness_input = {
    "motion_vectors": perception_data["motion_vectors"],
    "scene_transitions": temporal_data["scene_transitions"],
    "semantic_consistency_score": semantic_data["semantic_consistency_score"],
    "semantic_tags": perception_data["features"]["semantic_tags"],
    "motion_vectors": perception_data["motion_vectors"],
    }

    dynamics_data = await eval_dynamics(dynamic_robustness_input)

    generalisation_input = {
    "generation_prompt": input_data["prompt"],   
    "unique_tags": perception_data["features"]["unique_tags"],
    "semantic_tags": perception_data["features"]["semantic_tags"],
    "semantic_consistency_score": semantic_data["semantic_consistency_score"],
    "visual_embeddings": perception_data["features"]["visual_embeddings"]
}
    generalised_data = await eval_generalization(generalisation_input)

    reasoning_input = {
    "temporal_coherence": temporal_data["temporal_coherence"],
    "semantic_consistency_score": semantic_data["semantic_consistency_score"],
    "dynamics_robustness_score": dynamics_data["dynamics_robustness_score"],
    "generalisation_score": generalised_data["generalisation_score"],
    "overfitting_warning": generalised_data["overfitting_warning"],
    "generalisation_analysis": generalised_data["analysis"],
    "dynamics_analysis": dynamics_data["analysis"]
    }

    reasoning_data =await reasoning_agent(reasoning_input)

    all_agents_data= {
        "temporal_analysis": temporal_data,
        "semantic_analysis": semantic_data,
        "dynamics_robustness": dynamics_data,
        "generalization": generalised_data,
        "reasoning": reasoning_data,
    }
    return all_agents_data
