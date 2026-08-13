# 🌱 Biodiversity & Native Planting Planner
## Project Documentation

**Team:** Vanguard Strategists  
**Program:** Grow with Google BUILD Stage  
**UN SDG:** Goal 15 — Life on Land

## 1. Project Background

Urban gardening provides opportunities to support biodiversity within developed environments. However, choosing suitable native plants can be difficult because information about native status, growing requirements, taxonomy, and pollinator relationships is often distributed across multiple sources.

The Biodiversity & Native Planting Planner was developed to simplify this process by combining plant and ecological information into a recommendation application.

## 2. Problem Statement

Urban gardeners lack simple, automated tools that help them identify native plant species suitable for their local gardening conditions while supporting local pollinator populations.

## 3. Project Goal

The goal is to create a practical tool that allows users to discover native plants based on their location and gardening conditions.

## 4. Project Objectives

1. Collect relevant plant and ecological data.
2. Clean and standardize information from different sources.
3. Integrate the datasets.
4. Create application-ready recommendation features.
5. Validate the processed data.
6. Develop a recommendation engine.
7. Build an interactive Streamlit application.
8. Present plant information clearly.
9. Support UN SDG 15.

## 5. Project Scope

The current application focuses on the United States. Users select state, sunlight, water availability and preferred pollinator. The system returns plants matching those criteria.

## 6. Target Users

- Urban gardeners
- Home gardeners
- Beginner gardeners
- Native plant enthusiasts
- Pollinator-conscious gardeners
- People interested in biodiversity-friendly landscaping

## 7. Solution Architecture

```text
External Data
      ↓
Data Processing
      ↓
Application Dataset
      ↓
Recommendation Engine
      ↓
Streamlit Interface
      ↓
User Recommendations
```

## 8. Data Processing

The workflow includes data collection, cleaning, standardization, taxonomy resolution, feature engineering and validation.

## 9. Recommendation Logic

The recommendation engine uses rule-based filtering:

```text
Selected State
      ↓
Native Plant IDs
      ↓
Sunlight Filter
      ↓
Water Filter
      ↓
Pollinator Filter
      ↓
Final Recommendations
```

## 10. Application Architecture

```text
Streamlit Interface
        │
        ├── User Inputs
        ├── Dataset Loading
        ├── Recommendation Logic
        └── Results Display
                 │
                 ▼
          Plant Information
```

## 11. Dataset Loading

The application loads:

```text
data/processed/plants_app.csv
data/processed/plant_states.csv
```

## 12. User Flow

```text
Open Application
      ↓
Select State
      ↓
Select Sunlight
      ↓
Select Water
      ↓
Select Pollinator
      ↓
Generate Recommendations
      ↓
View Plant Results
```

## 13. Plant Result Information

Depending on availability:
- Plant name
- Scientific name
- Family
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

## 14. Empty Results

If no plants satisfy the selected criteria, the application informs the user and encourages them to adjust their conditions.

## 15. Data Quality

The project considers:
- Completeness
- Consistency
- Validity
- Uniqueness
- Referential integrity

## 16. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming |
| Pandas | Data manipulation |
| NumPy | Data processing |
| Streamlit | Web application |
| Jupyter Notebook | Data analysis |
| iNaturalist API | Plant images |

## 17. Testing

Testing focuses on dataset loading, state filtering, sunlight filtering, water filtering, pollinator filtering, recommendation output, empty results, image display, plant details and responsive behavior.

## 18. Limitations

- U.S. state-level geographic scope.
- Some plant records may be incomplete.
- Some plants may not have images.
- Recommendations use deterministic filtering.
- External data quality affects results.

## 19. Future Development

- Recommendation ranking
- County-level recommendations
- Interactive maps
- Seasonal planting guidance
- Garden-size recommendations
- Expanded geographic coverage
- Biodiversity impact scoring
- Advanced search

## 20. SDG 15 Alignment

The project supports **UN SDG 15 — Life on Land** by helping users identify native plants and make biodiversity-conscious planting decisions.

## 21. Conclusion

The project demonstrates how public ecological datasets can be transformed into an interactive environmental application combining data collection, analytics, processing, recommendation logic and a Streamlit interface.
