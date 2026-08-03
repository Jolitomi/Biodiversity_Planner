# 🌱 Biodiversity & Native Planting Planner

**UN Sustainable Development Goal 15 – Life on Land**

A data-driven recommendation system that helps urban gardeners discover native plants suitable for their growing conditions while supporting local biodiversity and pollinators.

---

# Project Overview

The Biodiversity & Native Planting Planner is a web-based recommendation tool designed to encourage sustainable urban gardening by helping users select native plants based on their gardening conditions.

The application recommends plants using factors such as:

- ☀️ Sunlight availability
- 💧 Water availability
- 🌿 Available growing space
- 🦋 Preferred pollinators
- 📍 Native U.S. state distribution

The project integrates multiple public datasets into a unified recommendation dataset that powers the application.

---

# Project Objectives

The project aims to:

- Promote native plant gardening
- Support pollinator conservation
- Encourage biodiversity in urban environments
- Simplify plant selection for home gardeners
- Demonstrate practical data engineering and analytics techniques

---

# Team

## Team Name

**Vanguard Strategists**

---

## Data Analytics

- Ayotomiwa
- Hanan

### Responsibilities

- Dataset sourcing
- Data cleaning
- Feature engineering
- Dataset integration
- Master dataset creation
- Data validation

---

## IT Automation

- Adrian

### Responsibilities

- Recommendation engine
- Backend development
- Application logic
- User input filtering

---

## Cybersecurity

- Favour

### Responsibilities

- Repository security
- Input validation
- Secure deployment
- Security review

---

# Project Scope

The recommendation engine focuses on the **United States**.

Reasons:

- Native plants differ by region.
- Reliable public datasets are available.
- Scope is manageable.
- Enables accurate recommendations.

---

# Data Sources

The project integrates the following datasets.

| Dataset | Purpose |
|----------|---------|
| Missouri Botanical Garden | Native plant distribution |
| Lady Bird Johnson Wildflower Center | Gardening characteristics |
| USDA PLANTS Database | Botanical taxonomy |
| Pollinator Interaction Dataset | Pollinator observations |
| iNaturalist API *(Future)* | Plant images |

See:

**docs/data_source_guide.md**

for complete details.

---

# Data Pipeline

```text
Raw Data
    │
    ▼
Cleaning
    │
    ▼
Standardization
    │
    ▼
Feature Engineering
    │
    ▼
USDA Taxonomy Resolution
    │
    ▼
Pollinator Aggregation
    │
    ▼
Coverage Validation
    │
    ▼
plants_master.csv
    │
    ▼
plants_app.csv
    │
    ▼
Recommendation Engine
```

---

# Repository Structure

```text
biodiversity-planner/

├── data/
│   ├── raw/
│   ├── processed/
│   └── review/
│
├── notebooks/
│
├── docs/
│   ├── data_source_guide.md
│   ├── data_dictionary.md
│   ├── data_handoff.md
│   └── data_pipeline_architecture.png
│
├── app/
│
├── requirements.txt
│
└── README.md
```

---

# Final Datasets

## plants_master.csv

Complete integrated dataset.

Contains:

- All merged source data
- Taxonomy
- Gardening information
- Pollinator observations

Used for:

- Analytics
- Maintenance
- Future enhancements

---

## plants_app.csv

Application-ready dataset.

Contains:

- Recommendation features
- Engineered Boolean columns
- Display information
- Placeholder image fields

Used by:

- Recommendation engine
- Web application

---

## plant_states.csv

Normalized state lookup table.

---

## data_quality_report.csv

Validation summary.

---

# Technologies

- Python
- Pandas
- NumPy
- Jupyter Notebook

Future:

- Streamlit / Flask
- iNaturalist API

---

# Application Workflow

```text
User selects:

State
↓

Sunlight
↓

Water

↓

Preferred Pollinator

↓

Recommendation Engine

↓

Recommended Native Plants
```

---

# Current Status

✅ Dataset sourcing completed

✅ Data cleaning completed

✅ Feature engineering completed

✅ USDA taxonomy integration completed

✅ Pollinator aggregation completed

✅ Master dataset completed

✅ Application dataset completed

🔄 Web application development in progress

---

# Future Improvements

- Integrate plant images
- Recommendation ranking
- Interactive map
- County-level recommendations
- Expanded pollinator coverage
- International support

---

# Documentation

Project documentation is available in the **docs/** folder.

- Data Source Guide
- Data Dictionary
- Data Handoff Guide
- Architecture Diagram

---

# License

This project is developed for educational purposes.

Users should comply with the licensing requirements of each external dataset used.

---

# Acknowledgements

We gratefully acknowledge the following organizations for providing publicly available datasets:

- Missouri Botanical Garden
- Lady Bird Johnson Wildflower Center
- United States Department of Agriculture (USDA)
- Pollinator dataset contributors
- iNaturalist

---

# UN Sustainable Development Goal

This project supports:

**🌍 SDG 15 – Life on Land**

by encouraging the use of native plants to strengthen biodiversity, support pollinators, and promote sustainable urban ecosystems.