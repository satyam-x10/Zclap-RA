import React from "react";
import { useAppContext } from "../context/AppContext";

const useForm = () => {
  const { setJsonData, formData, setFormData, setEditorValue } =
    useAppContext();

  const updateJson = (updated) => {
    setFormData(updated);
    const updatedStr = JSON.stringify(updated, null, 2);
    setEditorValue(updatedStr);
    setJsonData(updated);
  };

  const handleInputChange = (key, value) => {
    const updated = { ...formData, [key]: value };
    updateJson(updated);
  };

  const handleAgentToggle = (category, agent) => {
    const currentAgents = formData.agents[category] || [];
    const isSelected = currentAgents.includes(agent);

    const updatedAgents = isSelected
      ? currentAgents.filter((a) => a !== agent)
      : [...currentAgents, agent];

    const updated = {
      ...formData,
      agents: {
        ...formData.agents,
        [category]: updatedAgents,
      },
    };

    updateJson(updated);
  };

  return {
    updateJson,
    handleInputChange,
    handleAgentToggle,
  };
};

export default useForm;
