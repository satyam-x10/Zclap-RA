// Dark-themed VideoAnalysisDashboard
import React, { useState } from "react";
import { Bar } from "react-chartjs-2";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
} from "chart.js";
// import { response } from "../../utils/rough";

ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend);

const Result = ({response}) => {
  const [activeTab, setActiveTab] = useState("analysis");
  const { analysis, conversations, prompt } = response;

  const scoreLabels = Object.keys(analysis.reporting_agent.scorecard);
  const scoreData = Object.values(analysis.reporting_agent.scorecard);

  const chartData = {
    labels: scoreLabels.map(label => label.charAt(0).toUpperCase() + label.slice(1)),
    datasets: [
      {
        label: 'Scores',
        data: scoreData,
        backgroundColor: scoreData.map(score =>
          score < 0.4 ? 'rgba(229, 62, 62, 0.6)' :
          score < 0.7 ? 'rgba(236, 201, 75, 0.6)' :
          'rgba(56, 161, 105, 0.6)'
        ),
        borderColor: scoreData.map(score =>
          score < 0.4 ? '#e53e3e' :
          score < 0.7 ? '#ecc94b' :
          '#38a169'
        ),
        borderWidth: 1
      }
    ]
  };

  const chartOptions = {
    responsive: true,
    scales: {
      y: {
        beginAtZero: true,
        max: 1,
        ticks: {
          color: "#e2e8f0",
          callback: (value) => value.toFixed(1)
        },
        grid: {
          color: "rgba(255, 255, 255, 0.1)"
        }
      },
      x: {
        ticks: {
          color: "#e2e8f0"
        },
        grid: {
          color: "rgba(255, 255, 255, 0.1)"
        }
      }
    },
    plugins: {
      legend: { display: false },
      tooltip: {
        callbacks: {
          label: (context) => `Score: ${context.raw.toFixed(2)}`
        }
      }
    }
  };

  const styles = {
    container: {
      fontFamily: 'Arial, sans-serif',
      maxWidth: '1000px',
      margin: '0 auto',
      padding: '20px',
      backgroundColor: '#1a202c',
      borderRadius: '8px',
      color: '#e2e8f0',
      width: '100%',
      height: '100%',
      overflowY: 'auto',
      
    },
    header: { marginBottom: '20px', textAlign: 'center' },
    title: { fontSize: '24px', color: '#f7fafc', marginBottom: '5px' },
    subtitle: { fontSize: '16px', color: '#a0aec0' },
    prompt: {
      backgroundColor: '#2d3748',
      padding: '10px 15px',
      borderRadius: '5px',
      marginBottom: '20px',
      fontStyle: 'italic',
      fontSize: '16px'
    },
    tabContainer: {
      display: 'flex',
      gap: '10px',
      borderBottom: '1px solid #4a5568',
      marginBottom: '20px'
    },
    tab: {
      padding: '10px 20px',
      cursor: 'pointer',
      borderRadius: '5px 5px 0 0',
      fontWeight: '500',
      backgroundColor: '#2d3748',
      border: '1px solid #4a5568',
      borderBottom: 'none',
      color: '#cbd5e0'
    },
    activeTab: {
      backgroundColor: '#1a202c',
      borderTop: '2px solid #63b3ed',
      position: 'relative',
      top: '1px'
    },
    contentContainer: {
      backgroundColor: '#2d3748',
      padding: '20px',
      borderRadius: '5px'
    },
    scoreHeader: {
      fontSize: '18px',
      marginBottom: '15px',
      fontWeight: '500',
      color: '#e2e8f0'
    },
    summaryBox: {
      backgroundColor: '#1e293b',
      padding: '15px',
      borderRadius: '5px',
      marginBottom: '20px',
      borderLeft: '4px solid #63b3ed'
    },
    scoreGauge: {
      height: '300px',
      marginBottom: '30px'
    },
    grid: {
      display: 'grid',
      gridTemplateColumns: 'repeat(auto-fill, minmax(300px, 1fr))',
      gap: '15px'
    },
    agentBox: {
      backgroundColor: '#1a202c',
      border: '1px solid #4a5568',
      padding: '15px',
      borderRadius: '5px'
    },
    agentTitle: {
      fontSize: '16px',
      fontWeight: '500',
      marginBottom: '8px',
      display: 'flex',
      justifyContent: 'space-between',
      color: '#cbd5e0'
    },
    agentContent: { fontSize: '14px', lineHeight: '1.5', color: '#a0aec0' },
    scoreValue: {
      display: 'inline-block',
      padding: '3px 8px',
      borderRadius: '3px',
      fontWeight: '500',
      fontSize: '14px',
      marginLeft: '10px'
    },
    messageContainer: {
      marginBottom: '15px',
      padding: '12px',
      backgroundColor: '#1e293b',
      borderRadius: '5px',
      border: '1px solid #4a5568'
    },
    messageAgent: {
      fontWeight: '500',
      color: '#63b3ed',
      marginBottom: '5px'
    },
    messageContent: { fontSize: '14px', lineHeight: '1.5', color: '#cbd5e0' },
    metadataGrid: {
      display: 'grid',
      gridTemplateColumns: 'repeat(auto-fill, minmax(200px, 1fr))',
      gap: '10px'
    },
    metadataItem: {
      backgroundColor: '#1e293b',
      padding: '10px',
      borderRadius: '5px',
      border: '1px solid #4a5568'
    },
    metadataTitle: {
      fontSize: '14px',
      fontWeight: '500',
      color: '#cbd5e0',
      marginBottom: '5px'
    },
    metadataValue: { fontSize: '16px', color: '#edf2f7' }
  };

  const formatScore = (score) => {
    const scoreNum = parseFloat(score);
    const color = scoreNum < 0.4 ? '#e53e3e' : scoreNum < 0.7 ? '#ecc94b' : '#38a169';
    return (
      <span style={{ ...styles.scoreValue, backgroundColor: color + '33', color }}>
        {scoreNum.toFixed(2)}
      </span>
    );
  };

  const renderAnalysisTab = () => (
    <div>
      <h3 style={styles.scoreHeader}>Overall Score: {formatScore(analysis.reporting_agent.average_score)}</h3>
      <div style={styles.summaryBox}>
        <p><strong>Verdict:</strong> {analysis.reporting_agent.verdict}</p>
        <p><strong>Summary:</strong> {analysis.reporting_agent.summary}</p>
      </div>
      <h3 style={styles.scoreHeader}>Score Breakdown</h3>
      <div style={styles.scoreGauge}>
        <Bar data={chartData} options={chartOptions} />
      </div>
      <h3 style={styles.scoreHeader}>Detailed Analysis</h3>
      <div style={styles.grid}>
        {Object.entries(analysis).map(([agentName, agentData]) => {
          if (["reasoning_agent", "reporting_agent"].includes(agentName)) return null;
          const displayName = agentName.replace(/_agent$/, '')
            .split('_').map(w => w.charAt(0).toUpperCase() + w.slice(1)).join(' ');
          const score = analysis.reporting_agent.scorecard[agentName.replace(/_agent$/, '')];
          return (
            <div key={agentName} style={styles.agentBox}>
              <div style={styles.agentTitle}>
                {displayName} {score !== undefined && formatScore(score)}
              </div>
              <div style={styles.agentContent}>{agentData.summary??"This agentnt doesnt provide any summary"}</div>
            </div>
          );
        })}
      </div>
    </div>
  );

  const renderConversationsTab = () => (
    <div>
      <h3 style={styles.scoreHeader}>Agent Conversations</h3>
      {conversations.messages.map((msg, idx) => (
        <div key={idx} style={styles.messageContainer}>
          <div style={styles.messageAgent}>
            {msg.agent.replace(/_agent$/, '').split('_').map(w => w.charAt(0).toUpperCase() + w.slice(1)).join(' ')}
          </div>
          <div style={styles.messageContent}>{msg.content}</div>
        </div>
      ))}
    </div>
  );

  const renderMetadataTab = () => {
    const { analysis, conversations, ...metadata } = response;
  
    const renderValue = (value) => {
      if (Array.isArray(value)) {
        return (
          <ul style={{ margin: 0, paddingLeft: '1rem', overflowWrap: 'anywhere' }}>
            {value.map((item, index) => (
              <li key={index}>{item}</li>
            ))}
          </ul>
        );
      } else if (typeof value === 'object' && value !== null) {
        return (
          <div style={{ paddingLeft: '0.5rem' }}>
            {Object.entries(value).map(([k, v]) => (
              <div key={k} style={{ marginBottom: '0.25rem', overflowWrap: 'anywhere' }}>
                <strong>{k}:</strong> {Array.isArray(v) ? renderValue(v) : String(v)}
              </div>
            ))}
          </div>
        );
      } else {
        return (
          <span style={{ wordWrap: 'break-word', overflowWrap: 'anywhere', whiteSpace: 'pre-wrap' }}>
            {String(value)}
          </span>
        );
      }
    };
  
    return (
      <div>
        <h3 style={styles.scoreHeader}>Video Metadata</h3>
        <div style={styles.metadataGrid}>
          {Object.entries(metadata).map(([key, value]) => (
            <div key={key} style={{ ...styles.metadataItem, maxWidth: '100%', overflowWrap: 'anywhere' }}>
              <div style={{ ...styles.metadataTitle, overflowWrap: 'anywhere' }}>{key}</div>
              <div style={{ ...styles.metadataValue, overflowWrap: 'anywhere' }}>
                {renderValue(value)}
              </div>
            </div>
          ))}
        </div>
      </div>
    );
  };
  

  return (
    <div style={styles.container}>
      <div style={styles.header}>
        <h1 style={styles.title}>Video Analysis Dashboard</h1>
        <p style={styles.subtitle}>Review AI-generated insights from the video.</p>
      </div>
      <div style={styles.prompt}>Prompt: {prompt}</div>
      <div style={styles.tabContainer}>
        {["analysis", "conversations", "metadata"].map(tab => (
          <div
            key={tab}
            style={{
              ...styles.tab,
              ...(activeTab === tab ? styles.activeTab : {})
            }}
            onClick={() => setActiveTab(tab)}
          >
            {tab.charAt(0).toUpperCase() + tab.slice(1)}
          </div>
        ))}
      </div>
      <div style={styles.contentContainer}>
        {activeTab === "analysis" && renderAnalysisTab()}
        {activeTab === "conversations" && renderConversationsTab()}
        {activeTab === "metadata" && renderMetadataTab()}
      </div>
    </div>
  );
};

export default Result;
