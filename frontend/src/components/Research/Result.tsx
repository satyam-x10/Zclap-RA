import React, { useState } from "react";
import { response } from "../../utils/rough";
import { Bar } from "react-chartjs-2";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
} from "chart.js";

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
);

const Result = ({ response }) => {
  const [tab, setTab] = useState("config");

  const { jsonData, fileData, analysis } = response;
  const criteria = jsonData.criteria;

  // Create dynamic score data from analysis object
  const scoreData = Object.entries(analysis).reduce((acc, [key, value]) => {
    // Skip the "reasoning" key as it doesn't contain a score
    if (key === "reasoning") return acc;

    // Find the score in the value object
    const scoreKey = Object.keys(value).find(
      (k) => k.includes("score") || k.includes("coherence"),
    );
    if (scoreKey) {
      // Format the key for display (remove _analysis suffix, replace underscores with spaces, capitalize)
      const formattedKey = key
        .replace("_analysis", "")
        .replace(/_/g, " ")
        .split(" ")
        .map((word) => word.charAt(0).toUpperCase() + word.slice(1))
        .join(" ");

      // Add the score data
      acc.push({
        key: formattedKey,
        value: value[scoreKey],
        originalKey: key,
      });
    }
    return acc;
  }, []);

  // Generate a color palette based on the number of items
  const generateColorPalette = (count) => {
    const baseColors = [
      "#4361ee",
      "#3a86ff",
      "#00b4d8",
      "#0096c7",
      "#4cc9f0",
      "#5390d9",
      "#6930c3",
      "#7400b8",
    ];
    return Array(count)
      .fill()
      .map((_, i) => baseColors[i % baseColors.length]);
  };

  const colors = generateColorPalette(scoreData.length);

  const chartOptions = {
    responsive: true,
    plugins: {
      legend: {
        position: "top",
      },
      title: {
        display: true,
        text: "Performance Analysis",
        font: {
          size: 16,
          weight: "bold",
        },
      },
      tooltip: {
        backgroundColor: "rgba(0, 0, 0, 0.8)",
        titleFont: {
          size: 14,
        },
        bodyFont: {
          size: 13,
        },
        padding: 10,
        cornerRadius: 4,
      },
    },
    scales: {
      y: {
        beginAtZero: true,
        max: 1,
        ticks: {
          stepSize: 0.1,
        },
        grid: {
          color: "rgba(0, 0, 0, 0.05)",
        },
      },
      x: {
        grid: {
          display: false,
        },
      },
    },
  };

  const scoreChart = {
    labels: scoreData.map((item) => item.key),
    datasets: [
      {
        label: "Evaluation Scores",
        data: scoreData.map((item) => item.value),
        backgroundColor: colors,
        borderWidth: 1,
        borderRadius: 4,
      },
    ],
  };

  const renderConfigTab = () => (
    <div className="content-container">
      <div className="section">
        <h3 className="section-title">Generation Parameters</h3>
        <div className="parameter-grid">
          {Object.entries(jsonData)
            .filter(([key]) => key !== "criteria") // Exclude criteria as it's shown separately
            .map(([key, value]) => (
              <div key={key} className="parameter-item">
                <span className="parameter-label">
                  {key
                    .split("_")
                    .map((word) => word.charAt(0).toUpperCase() + word.slice(1))
                    .join(" ")}
                  :
                </span>
                <span className="parameter-value">
                  {typeof value === "object" ? JSON.stringify(value) : value}
                </span>
              </div>
            ))}
        </div>
      </div>

      <div className="section">
        <h3 className="section-title">Agent Criteria</h3>
        <div className="criteria-grid">
          {Object.entries(criteria).map(([key, agents]) => (
            <div key={key} className="criteria-item">
              <h4 className="criteria-name">
                {key
                  .split("_")
                  .map((word) => word.charAt(0).toUpperCase() + word.slice(1))
                  .join(" ")}
              </h4>
              <ul className="agent-list">
                {agents.map((agent, i) => (
                  <li key={i}>{agent}</li>
                ))}
              </ul>
            </div>
          ))}
        </div>
      </div>
    </div>
  );

  const renderFileTab = () => (
    <div className="content-container">
      <div className="file-details">
        <h3 className="section-title">File Information</h3>
        <div className="file-grid">
          {Object.entries(fileData).map(([key, value]) => (
            <div key={key} className="file-item">
              <span className="file-label">
                {key
                  .split("_")
                  .map((word) => word.charAt(0).toUpperCase() + word.slice(1))
                  .join(" ")}
                :
              </span>
              <span className="file-value">
                {typeof value === "object" ? JSON.stringify(value) : value}
              </span>
            </div>
          ))}
          {response.savedTo && (
            <div className="file-item">
              <span className="file-label">Saved Path:</span>
              <span className="file-value">{response.savedTo}</span>
            </div>
          )}
        </div>
      </div>
    </div>
  );

  const renderAnalysisTab = () => (
    <div className="content-container">
      <div className="chart-container">
        <Bar data={scoreChart} options={chartOptions} />
      </div>

      <div className="analysis-details">
        <h3 className="section-title">Analysis Details</h3>
        <div className="analysis-grid">
          {scoreData.map((item) => (
            <div key={item.originalKey} className="analysis-item">
              <h4 className="analysis-name">{item.key}</h4>
              <div className="analysis-score">
                <div
                  className="score-bar"
                  style={{
                    width: `${item.value * 100}%`,
                    backgroundColor: colors[scoreData.indexOf(item)],
                  }}
                ></div>
                <span className="score-value">{item.value.toFixed(2)}</span>
              </div>
            </div>
          ))}
        </div>
      </div>

      <div className="verdict-section">
        <h3 className="section-title">Reasoning Verdict</h3>
        <div className="verdict-content">
          <p className="verdict-text">
            <span className="verdict-highlight">
              {analysis.reasoning.verdict}
            </span>{" "}
            – {analysis.reasoning.explanation}
          </p>
        </div>
      </div>
    </div>
  );

  const renderTab = () => {
    switch (tab) {
      case "config":
        return renderConfigTab();
      case "file":
        return renderFileTab();
      case "analysis":
        return renderAnalysisTab();
      default:
        return <div>Invalid tab</div>;
    }
  };

  // Tab configuration for dynamic tabs
  const tabs = [
    { id: "config", label: "Configuration" },
    { id: "file", label: "File Details" },
    { id: "analysis", label: "Analysis Results" },
  ];

  return (
    <div className="result-container">
      <div className="tabs">
        {tabs.map((tabItem) => (
          <button
            key={tabItem.id}
            onClick={() => setTab(tabItem.id)}
            className={`tab ${tab === tabItem.id ? "active" : ""}`}
          >
            {tabItem.label}
          </button>
        ))}
      </div>
      <button
        onClick={() => window.location.reload()}
        style={{
          float: "right",
          position: "relative",
          top: "0px",
          right: "0px",
        }}
      >
        home
      </button>
      <div className="tab-content">{renderTab()}</div>
      <style jsx>{`
        .result-container {
          font-family:
            "Inter",
            -apple-system,
            BlinkMacSystemFont,
            "Segoe UI",
            Roboto,
            sans-serif;
          max-width: 900px;
          margin: 0 auto;
          background-color: #ffffff;
          border-radius: 8px;
          box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
          overflow: hidden;
        }

        .tabs {
          display: flex;
          border-bottom: 1px solid #e5e7eb;
          background-color: #f9fafb;
        }

        .tab {
          padding: 16px 24px;
          border: none;
          background: none;
          font-size: 15px;
          font-weight: 500;
          color: #6b7280;
          cursor: pointer;
          transition: all 0.2s ease;
          position: relative;
        }

        .tab:hover {
          color: #111827;
          background-color: rgba(0, 0, 0, 0.02);
        }

        .tab.active {
          color: #1e40af;
          font-weight: 600;
        }

        .tab.active::after {
          content: "";
          position: absolute;
          bottom: 0;
          left: 0;
          right: 0;
          height: 3px;
          background-color: #1e40af;
        }

        .tab-content {
          padding: 24px;
        }

        .content-container {
          display: flex;
          flex-direction: column;
          gap: 24px;
        }

        .section {
          margin-bottom: 24px;
        }

        .section-title {
          font-size: 18px;
          font-weight: 600;
          color: #374151;
          margin-bottom: 16px;
          padding-bottom: 8px;
          border-bottom: 1px solid #f3f4f6;
        }

        .parameter-grid,
        .file-grid,
        .analysis-grid {
          display: grid;
          grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
          gap: 16px;
        }

        .parameter-item,
        .file-item {
          display: flex;
          flex-direction: column;
          gap: 4px;
        }

        .parameter-label,
        .file-label {
          font-size: 14px;
          font-weight: 500;
          color: #6b7280;
        }

        .parameter-value,
        .file-value {
          font-size: 15px;
          color: #111827;
          word-break: break-word;
        }

        .criteria-grid {
          display: grid;
          grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
          gap: 20px;
        }

        .criteria-item {
          border: 1px solid #f3f4f6;
          border-radius: 6px;
          padding: 16px;
          background-color: #fafafa;
        }

        .criteria-name {
          font-size: 16px;
          font-weight: 600;
          color: #374151;
          margin-bottom: 8px;
        }

        .agent-list {
          list-style-type: none;
          padding: 0;
          margin: 0;
        }

        .agent-list li {
          padding: 6px 0;
          font-size: 14px;
          color: #4b5563;
          border-bottom: 1px dashed #e5e7eb;
        }

        .agent-list li:last-child {
          border-bottom: none;
        }

        .chart-container {
          height: 400px;
          margin-bottom: 32px;
        }

        .analysis-item {
          border: 1px solid #f3f4f6;
          border-radius: 6px;
          padding: 16px;
          background-color: #fafafa;
        }

        .analysis-name {
          font-size: 16px;
          font-weight: 600;
          color: #374151;
          margin-bottom: 12px;
        }

        .analysis-score {
          position: relative;
          height: 24px;
          background-color: #e5e7eb;
          border-radius: 12px;
          overflow: hidden;
        }

        .score-bar {
          height: 100%;
          border-radius: 12px;
          transition: width 0.5s ease;
        }

        .score-value {
          position: absolute;
          right: 10px;
          top: 50%;
          transform: translateY(-50%);
          font-size: 14px;
          font-weight: 600;
          color: #fff;
          text-shadow: 0 0 2px rgba(0, 0, 0, 0.5);
        }

        .verdict-section {
          background-color: #f9fafb;
          border-radius: 6px;
          padding: 16px;
        }

        .verdict-content {
          background-color: white;
          border-radius: 6px;
          padding: 16px;
          border: 1px solid #e5e7eb;
        }

        .verdict-text {
          font-size: 15px;
          line-height: 1.6;
          color: #374151;
        }

        .verdict-highlight {
          font-weight: 600;
          color: #1e40af;
        }
      `}</style>
    </div>
  );
};

export default Result;
