# agents/meta/reasoning_agent.py

from data.Config import config

agent_manifest = {
    "agent_name": "reasoning_agent",
    "purpose": "Synthesizes outputs from all agents to create a reasoning trace.",
}

async def run() -> None:
    try:
        temporal = config.analysis.temporal_analysis_agent.get("temporal_coherence", None)
        semantic = config.analysis.semantic_analysis_agent.get("semantic_consistency_score", None)
        dynamics = config.analysis.dynamics_robustness_agent.get("dynamics_robustness_score", None)
        general = config.analysis.generalization_agent.get("generalisation_score", None)
        caption_align = config.analysis.caption_alignment_agent.get("match_ratio", None)
        redundancy = config.analysis.redundancy_agent.get("semantic_redundancy", None)
        aesthetic = config.analysis.aesthetic_agent.get("aesthetic_score", None)

        trace = []

        if temporal is not None:
            trace.append(f"Temporal coherence is {temporal:.2f}, indicating {'smooth' if temporal > 0.8 else 'inconsistent'} transitions.")
        if semantic is not None:
            trace.append(f"Semantic consistency is {semantic:.2f}, suggesting {'stable alignment' if semantic > 0.7 else 'semantic drift'}.")
        if dynamics is not None:
            trace.append(f"Dynamics robustness score is {dynamics:.2f}, reflecting how stable the video remains under motion.")
        if general is not None:
            trace.append(f"Generalization score is {general:.2f}, showing how well the video avoids overfitting and redundancy.")
        if caption_align is not None:
            trace.append(f"Prompt-to-caption alignment is {caption_align:.2f}, indicating prompt relevance.")
        if redundancy is not None:
            trace.append(f"Semantic redundancy is {redundancy:.2f}, {'high' if redundancy > 0.6 else 'moderate or low'} repetition.")
        if aesthetic is not None:
            trace.append(f"Aesthetic score is {aesthetic:.2f}, which suggests visual {'appeal' if aesthetic > 0.7 else 'issues'}.")

        summary = " ".join(trace)

        config.analysis.reasoning_agent = {
            "reasoning_trace": trace,
            "summary": summary
        }

        print(f"[reasoning_agent] Summary generated.")
    except Exception as e:
        config.analysis.reasoning_agent = {
            "reasoning_trace": [],
            "summary": f"Reasoning failed: {str(e)}"
        }
        print(f"[reasoning_agent] Error: {e}")
