import React from 'react';

export const EvaluationCriteriaOptions = {
  report_format: [
    { value: 'minimal', label: 'Minimal' },
    { value: 'detailed', label: 'Detailed' },
    { value: 'verbose', label: 'Verbose' },
    { value: 'pdf', label: 'PDF' },
  ],
  pipeline: [
    { value: 'bus', label: 'bus' },
    { value: 'ring', label: 'Ring' },
    { value: 'star', label: 'Star' },
    { value: 'tree', label: 'Tree' },
  ],
};

const JsonGuide = () => (
  <div style={{ maxHeight: '400px', overflowY: 'scroll', padding: '1rem', backgroundColor: '#1F2937', borderRadius: '0.5rem', marginBottom: '2rem', color: '#D1D5DB', lineHeight: '1.6' }}>
    <h2 style={{ fontSize: '1.25rem', color: 'white', marginBottom: '0.5rem' }}>📘 JSON Configuration Guide</h2>
    <p>This configuration form allows you to define the behavior and structure of the video evaluation pipeline using a simple JSON object. You can customize which agents are active and how the evaluation system operates.</p>

    <p><strong>criteria:</strong> This section controls which agents are activated in the pipeline, grouped by type. Each agent can be toggled <code>true</code> or <code>false</code>:</p>
    <ul style={{ marginLeft: '1rem' }}>
      <li><strong>ingestion</strong>: video ingestion logic</li>
      <li><strong>analysis</strong>: multiple agents such as temporal, semantic, robustness, generalization</li>
      <li><strong>feature_extractor</strong>: perception-level embedding extraction</li>
      <li><strong>synthesis</strong>: combines multiple agent outputs into final reasoning</li>
      <li><strong>reporting</strong>: builds the final user-facing report</li>
      <li><strong>controller</strong>: manages the agent execution flow</li>
    </ul>

    <p><strong>options:</strong> These additional settings further define how your evaluation runs:</p>
    <ul style={{ marginLeft: '1rem' }}>
      <li><strong>prompt</strong>: A text description of expected video content (required if using <code>semantic_analysis_agent</code>)</li>
      <li><strong>frame_sampling_rate</strong>: Integer indicating how many frames to skip (e.g., 2 = every second frame)</li>
      <li><strong>pipeline</strong>: Defines the agent communication topology. Options:
        <ul>
          {EvaluationCriteriaOptions.pipeline.map(opt => <li key={opt.value}><code>{opt.value}</code>: {opt.label} layout</li>)}
        </ul>
      </li>
      <li><strong>report_format</strong>: Controls how detailed the final output is:
        <ul>
          {EvaluationCriteriaOptions.report_format.map(opt => <li key={opt.value}><code>{opt.value}</code>: {opt.label}</li>)}
        </ul>
      </li>
    </ul>
  </div>
);

export default function EditorGuide() {
  return (
    <div style={{ backgroundColor: '#111827', color: 'white', minHeight: '100vh', padding: '2rem' }}>
      <h1 style={{ fontSize: '2rem', fontWeight: 'bold', textAlign: 'center', marginBottom: '2rem' }}>🧪 Configure Evaluation Criteria</h1>
      <JsonGuide />
      {/* Your configuration form goes here */}
    </div>
  );
}