# 🌱 Biodiversity & Native Planting Planner

### UN Sustainable Development Goal 15 — Life on Land

**Team:** Vanguard Strategists  
**Program:** Grow with Google BUILD Stage  
**Project Topic:** Biodiversity & Native Planting Planner

## 🌿 Project Overview

The Biodiversity & Native Planting Planner is a data-driven web application designed to help gardeners discover native plants suitable for their local gardening conditions while supporting local pollinators.

Users select:
- 📍 U.S. State
- ☀️ Sunlight availability
- 💧 Water availability
- 🦋 Preferred pollinator

The system filters the processed plant dataset and presents matching native plant recommendations.

## 🎯 Problem Statement

Urban gardeners often lack simple, automated tools that help them identify native plant species suitable for their local gardening conditions while supporting local pollinator populations.

## 💡 Our Solution

The project combines information from multiple public data sources into structured, application-ready datasets and uses them in a Streamlit recommendation application.

```text
Public Data Sources
        ↓
Data Collection
        ↓
Data Cleaning
        ↓
Data Standardization
        ↓
Data Integration
        ↓
Feature Engineering
        ↓
Data Validation
        ↓
Application Dataset
        ↓
Recommendation Engine
        ↓
Streamlit Application
```

## 🎯 Project Objectives

- Promote the use of native plants.
- Encourage biodiversity-friendly gardening.
- Support local pollinators.
- Make plant selection easier for gardeners.
- Demonstrate practical data analytics.
- Combine data analytics with application development.
- Support UN SDG 15 — Life on Land.

## 👥 Team — Vanguard Strategists

| Team Member | Grow with Google Track | Contribution |
|---|---|---|
| Ayotomiwa Omojola | Data Analytics | Data sourcing, cleaning, integration, feature engineering and analytics |UI/UX design and application interface development
| Hanan Kassim | Advanced Data Analytics | Data analysis, validation and dataset development | Data Sourcing
| Adrian Denis | IT Automation with Python | Application development, automation and recommendation logic |
| Favour Asomba | Cybersecurity | Security considerations and review |

## 🌎 Geographic Scope

The current project focuses on the United States and uses state-level native plant relationships.

## 🔎 Application Features

### State Selection
Users select a U.S. state from the available state data.

### ☀️ Sunlight Selection
- Full Sun
- Part Shade
- Shade

### 💧 Water Selection
- Low Water
- Medium Water
- High Water

### 🦋 Pollinator Selection
- Bee
- Butterfly
- Hummingbird
- Moth
- Fly
- Beetle
- Wasp

### 🌱 Plant Recommendations

The recommendation engine identifies plants that:
1. Are associated with the selected state.
2. Match the selected sunlight condition.
3. Match the selected water condition.
4. Match the selected pollinator condition.

### 🌿 Plant Information

Depending on data availability, results can include:
- Plant name
- Scientific name
- Plant family
- Plant type
- Hardiness zones
- Maintenance
- Soil description
- Soil moisture
- Soil pH
- Bloom color
- Bloom season
- Plant image
- Image source

## 🧠 Recommendation Engine

The current recommendation system uses deterministic filtering rather than machine learning.

```text
Selected State
      ↓
Native Plant IDs
      ↓
Sunlight Match
      ↓
Water Match
      ↓
Pollinator Match
      ↓
Matching Plants
```

## 🖥️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Data manipulation |
| NumPy | Data processing |
| Streamlit | Web application |
| Jupyter Notebook | Data analysis and exploration |
| iNaturalist API | Plant image sourcing |


## 🚀 Running the Application

### Clone the Repository

```bash
git clone https://github.com/Jolitomi/Biodiversity_Planner.git
cd Biodiversity_Planner
```

### Create a Virtual Environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Launch the Application

```bash
streamlit run app/app.py
```

## 📊 Data Sources

| Source | Purpose |
|---|---|
| Missouri Botanical Garden | Native plant distribution |
| Lady Bird Johnson Wildflower Center | Plant and gardening characteristics |
| USDA PLANTS Database | Botanical taxonomy |
| Pollinator Interaction Dataset | Pollinator observations |
| iNaturalist API | Plant images |

See the supporting documentation in `docs/`.

## 🔄 Data Pipeline

```text
External Data Sources
        ↓
Raw Data
        ↓
Cleaning
        ↓
Standardization
        ↓
Integration
        ↓
Feature Engineering
        ↓
Validation
        ↓
Processed Datasets
        ↓
Recommendation Engine
        ↓
Streamlit Application
```

## 📱 Responsive Interface

The application is designed to work across desktop and mobile screen sizes, with emphasis on clear hierarchy, compact information presentation, touch-friendly controls and readability.

## ⚠️ Limitations

- Current geographic scope is U.S. states.
- Some plant records may have incomplete information.
- Image availability depends on the underlying image data.
- Recommendations currently use deterministic filtering.
- The application depends on the quality and availability of external data.

## 🔮 Future Improvements

- Recommendation ranking
- County-level recommendations
- Interactive maps
- Seasonal planting recommendations
- Garden-size recommendations
- Expanded geographic coverage
- Biodiversity impact indicators
- More detailed pollinator information
- Advanced plant search

## 🌍 UN SDG 15 — Life on Land

The project supports **United Nations Sustainable Development Goal 15: Life on Land** by making it easier for users to discover native plants and make biodiversity-conscious planting decisions.

## 🤝 Collaboration

The project was developed as a cross-functional team combining data analytics, advanced analytics, application development, cybersecurity and environmental problem-solving.

## 📚 Documentation

- `docs/project_documentation.md`
- `docs/data_source_guide.md`
- `docs/data_dictionary.md`
- `docs/data_handoff.md`
- `docs/data_pipeline_architecture.md`

## How to Run / View the Project

### Prerequisites
- Python 3.9+
- pip

### Setup

1. Clone the repository:
```bash
   git clone https://github.com/Jolitomi/Biodiversity_Planner.git
   cd Biodiversity_Planner
```

2. Install dependencies:
```bash
   pip install pandas streamlit
```

3. Run the application from the repository root (required — the app uses relative paths to `data/processed/`):
```bash
   streamlit run app/app.py
```

4. Your browser should open automatically. If not, go to the Local URL shown in the terminal (typically `http://localhost:8501`).

### Data
The application-ready dataset lives at `data/processed/plants_app.csv`.
