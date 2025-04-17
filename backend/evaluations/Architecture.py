def define_research_architecture(pipeline_mode, active_agents):
    prompt = "Evaluate the video based on the selected criteria."
    history = []
    flow = []

    def pass_prompt(from_agent, to_agent):
        flow.append({
            "from": from_agent,
            "to": to_agent,
            "prompt": prompt,
            "history": history.copy()
        })
        history.append(f"Prompt passed from {from_agent} to {to_agent}")

    if pipeline_mode == "default":
        for i in range(len(active_agents) - 1):
            pass_prompt(active_agents[i], active_agents[i + 1])

    elif pipeline_mode == "ring":
        for i in range(len(active_agents)):
            from_agent = active_agents[i]
            to_agent = active_agents[(i + 1) % len(active_agents)]
            pass_prompt(from_agent, to_agent)

    elif pipeline_mode == "tree":
        root = active_agents[0]
        for i in range(1, len(active_agents)):
            parent = active_agents[(i - 1) // 2]  # binary tree pattern
            pass_prompt(parent, active_agents[i])

    elif pipeline_mode == "star":
        center = "coordinator_agent" if "coordinator_agent" in active_agents else active_agents[0]
        for agent in active_agents:
            if agent != center:
                pass_prompt(center, agent)

    return history
