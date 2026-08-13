# 🏗️ Data Pipeline Architecture

## Biodiversity & Native Planting Planner

**Team:** Vanguard Strategists  
**Program:** Grow with Google BUILD Stage  
**SDG:** Goal 15 — Life on Land

## 1. Overview

The Biodiversity & Native Planting Planner uses a multi-stage data pipeline to transform information from multiple sources into structured datasets used by the recommendation application.

The pipeline separates:
1. Data collection
2. Data cleaning
3. Data standardization
4. Data integration
5. Feature engineering
6. Data validation
7. Application delivery

## 2. High-Level Architecture

```text
┌─────────────────────────────┐
│      External Sources       │
├─────────────────────────────┤
│ Missouri Botanical Garden   │
│ Lady Bird Johnson WFC       │
│ USDA PLANTS Database        │
│ Pollinator Dataset          │
│ iNaturalist API             │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│       Raw Data Layer        │
│          data/raw/          │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│      Cleaning Layer         │
├─────────────────────────────┤
│ Duplicate Removal            │
│ Missing-Value Handling       │
│ Name Standardization         │
│ Type Conversion              │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│   Integration & Processing  │
├─────────────────────────────┤
│ Taxonomy Resolution         │
│ Dataset Integration         │
│ State Relationships         │
│ Pollinator Aggregation      │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│    Feature Engineering      │
├─────────────────────────────┤
│ Sunlight Features           │
│ Water Features              │
│ Pollinator Features         │
│ Bloom Features              │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│      Data Validation        │
├─────────────────────────────┤
│ Completeness                │
│ Consistency                 │
│ Validity                    │
│ Relationships               │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│      Processed Data         │
├─────────────────────────────┤
│ plants_app.csv              │
│ plant_states.csv            │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│    Recommendation Engine    │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│    Streamlit Application    │
└─────────────────────────────┘
```

## 3. External Data Layer

```text
Native Distribution
        +
Gardening Characteristics
        +
Taxonomy
        +
Pollinator Interactions
        +
Plant Images
        ↓
Integrated Plant Information
```

## 4. Raw Data Layer

Raw source files are stored under:

```text
data/raw/
```

## 5. Cleaning Layer

The cleaning stage addresses:
- Duplicate records
- Missing values
- Inconsistent names
- Inconsistent categories
- Formatting differences
- Incorrect data types

## 6. Standardization Layer

Standardization makes data from different sources compatible.

This can include:
- Plant-name normalization
- State-name normalization
- Identifier standardization
- Category normalization
- Data-type conversion

## 7. Integration Layer

The integration layer combines information from different datasets using plant identifiers and standardized plant information.

## 8. Taxonomy Layer

Taxonomic information supports consistent plant identification and helps prevent naming differences from creating duplicate conceptual records.

## 9. Feature Engineering Layer

### Sunlight

```text
supports_full_sun
supports_part_shade
supports_shade
```

### Water

```text
supports_low_water
supports_medium_water
supports_high_water
```

### Pollinators

```text
supports_bee_observed
supports_butterfly_observed
supports_hummingbird_observed
supports_moth_observed
supports_fly_observed
supports_beetle_observed
supports_wasp_observed
```

## 10. Validation Layer

Processed data should be checked for:
- Completeness
- Consistency
- Validity
- Uniqueness
- Relationship integrity
- Expected field types

## 11. Processed Data Layer

The application relies primarily on:

```text
data/processed/plants_app.csv
data/processed/plant_states.csv
```

`plants_app.csv` contains plant-level information and recommendation features.

`plant_states.csv` contains plant-to-state relationships.

## 12. Recommendation Layer

The recommendation engine receives:

```text
State
Sunlight
Water
Pollinator
```

and applies filtering logic:

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
Recommendations
```

## 13. Application Layer

The Streamlit application handles:
- User input
- Dataset loading
- Recommendation filtering
- Plant results
- Plant details
- Image display
- Empty-result handling

## 14. Separation of Responsibilities

```text
Data Layer
    ↓
Validated Dataset
    ↓
Recommendation Layer
    ↓
Presentation Layer
```

This separation allows data processing and application development to evolve independently.

## 15. Reproducibility

The repository contains processing resources and documentation so team members and future developers can understand:
- Where data originated
- How data was processed
- How datasets are connected
- Which fields the application uses
- How recommendations are generated

## 16. Future Architecture

```text
Scheduled Data Collection
          ↓
Automated Cleaning
          ↓
Automated Integration
          ↓
Automated Validation
          ↓
Dataset Versioning
          ↓
Application Update
```

## 17. Summary

```text
Multiple Sources
       ↓
Clean
       ↓
Standardize
       ↓
Integrate
       ↓
Engineer Features
       ↓
Validate
       ↓
Application Dataset
       ↓
Recommendation Engine
       ↓
Native Plant Planner
```
