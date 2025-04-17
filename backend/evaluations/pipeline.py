from agents.video_ingestion_agent import run as ingest_video
from agents.temporal_analysis_agent import run as eval_temporal
from agents.semantic_analysis_agent import run as eval_semantic
from agents.dynamics_robustness_agent import run as eval_dynamics
from agents.generalization_agent import run as eval_generalization
from agents.perception_agent import run as extract_perception
from agents.reasoning_agent import run as reason
from agents.reporting_agent import run as report

def run_pipeline(video_path: str, prompt: str = ""):
    memory = {}

    # Step 1: Ingest video
    memory["video_frames"] = ingest_video(video_path)

    # Step 2: Perception (optional shared features)
    memory["frame_embeddings"] = extract_perception(memory["video_frames"])["frame_embeddings"]

    # Step 3: Temporal coherence analysis
    memory["temporal_coherence_score"] = eval_temporal(memory["video_frames"])["temporal_coherence_score"]

    # Step 4: Semantic consistency analysis
    memory["semantic_consistency_score"] = eval_semantic(memory["video_frames"], prompt)["semantic_consistency_score"]

    # Step 5: Dynamic scene robustness
    memory["dynamic_scene_handling_score"] = eval_dynamics(memory["video_frames"])["dynamic_scene_handling_score"]

    # Step 6: Generalization analysis (depends on semantic score)
    memory["generalization_score"] = eval_generalization(
        memory["video_frames"],
        memory["semantic_consistency_score"]
    )["generalization_score"]

    # Step 7: Reasoning — combine scores into insights
    score_dict = {
        "temporal_coherence": memory["temporal_coherence_score"],
        "semantic_consistency": memory["semantic_consistency_score"],
        "dynamic_scene_handling": memory["dynamic_scene_handling_score"],
        "generalization": memory["generalization_score"]
    }
    insight_dict = reason(score_dict)

    # Step 8: Reporting — final output
    final_report = report(score_dict, insight_dict)

    return final_report
