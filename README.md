# CyberPulse: Cybersecurity Threat Analytics Dashboard

## 📊 Project Overview

CyberPulse is an interactive analytics dashboard that helps organizations understand global cybersecurity threat patterns, identify high-risk sectors, and evaluate defense mechanism effectiveness. This project transforms raw cyber-incident data into actionable intelligence through advanced clustering and visualization techniques.


## 🚀 Key Features

- **Global Threat Visualization**: Interactive choropleth maps showing financial impact by country
- **Industry Analysis**: Detailed breakdown of attacks by industry sector
- **Threat Profiling**: AI-powered clustering of incidents into distinct threat categories
- **Defense Evaluation**: Analysis of defense mechanism effectiveness
- **Time Series Analysis**: Trends in cyber attacks over time
- **Interactive Filters**: Dynamic filtering by year, industry, country, and threat type

## 🛠️ Installation

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Setup Instructions

1. Clone this repository:
```bash
git clone https://github.com/Ravikant2003/CyberPulse-Cybersecurity-Threat-Analytics-Dashboard.git
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Place your dataset in the `data/raw/` directory with the filename `cyber_threats.csv`

## 📈 Usage

### Data Preparation
```bash
python src/data_cleaner.py
```

### Machine Learning Model Training
```bash
python src/model_trainer.py
```

### Launch the Dashboard
```bash
streamlit run app/dashboard.py
```

## 📁 Project Structure

```
cyberpulse-threat-analytics/
├── data/
│   ├── raw/                 # Original dataset
│   └── processed/           # Cleaned and processed data
├── notebooks/               # Jupyter notebooks for EDA
├── src/                     # Source code for data processing and ML
│   ├── data_cleaner.py      # Data cleaning and preprocessing
│   └── model_trainer.py     # ML model training
├── app/                     # Streamlit dashboard application
│   └── dashboard.py         # Main dashboard application
├── models/                  # Trained ML models
├── requirements.txt         # Python dependencies
└── README.md               # Project documentation
```

## 🔮 Machine Learning Approach

The project uses K-Means clustering to categorize cyber incidents into distinct threat profiles based on:

1. **Financial Impact**: Monetary losses from attacks
2. **User Impact**: Number of affected users
3. **Resolution Time**: Time taken to resolve incidents

The algorithm automatically determines the optimal number of clusters using silhouette scoring, ensuring data-driven segmentation of threats.


## 🎯 Business Applications

This dashboard helps organizations:

- Identify high-risk sectors and regions
- Allocate security resources more effectively
- Understand the effectiveness of different defense mechanisms
- Prepare for emerging threat patterns
- Make data-driven decisions about cybersecurity investments


## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Dataset source: https://www.kaggle.com/datasets/atharvasoundankar/global-cybersecurity-threats-2015-2024?
