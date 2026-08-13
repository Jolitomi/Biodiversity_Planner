# 🔄 Data Handoff Guide

## Biodiversity & Native Planting Planner

**Team:** Vanguard Strategists

## 1. Purpose

This document describes how processed data moves from the analytics workflow into the application.

## 2. Overall Pipeline

```text
Raw Sources
     ↓
Raw Data
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
Streamlit Application
```

## 3. Raw Data

Raw datasets are maintained in:

```text
data/raw/
```

Original source data should generally not be modified directly.

## 4. Processing Stage

The processing stage handles:
- Cleaning
- Standardization
- Data integration
- Taxonomy resolution
- Feature engineering
- Pollinator aggregation
- Data validation

## 5. Application Dataset

The primary application dataset is:

```text
data/processed/plants_app.csv
```

It contains plant information and recommendation fields required by the application.

## 6. State Relationship Dataset

The application also uses:

```text
data/processed/plant_states.csv
```

This dataset connects plants with native-state relationships through `plant_id`.

## 7. Application Handoff

The primary datasets handed from the data workflow to the application are:

```text
plants_app.csv
plant_states.csv
```

## 8. Application Loading

The application loads the processed files from the repository's processed-data directory.

Conceptually:

```python
plants_df = pd.read_csv(app_data_path)
states_df = pd.read_csv(state_data_path)
```

## 9. User Input Handoff

The application collects:

```text
State
Sunlight
Water
Pollinator
```

The interface maps these choices to dataset fields.

Examples:

```text
Full Sun
    ↓
supports_full_sun
```

```text
Low Water
    ↓
supports_low_water
```

```text
Bee
    ↓
supports_bee_observed
```

## 10. State Filtering

```text
Selected State
      ↓
plant_states.csv
      ↓
Matching plant_id values
```

The matching IDs are used against the main plant dataset.

## 11. Recommendation Filtering

```text
Native Plants
      ↓
Sunlight Match
      ↓
Water Match
      ↓
Pollinator Match
      ↓
Final Recommendations
```

## 12. Output Handoff

Filtered records are passed to the presentation layer.

The application can display:
- Plant image
- Plant name
- Scientific name
- Plant family
- Plant type
- Hardiness zones
- Maintenance
- Soil information
- Moisture
- pH
- Bloom information
- Image source

## 13. Validation Before Handoff

```text
[ ] Required files exist
[ ] Required columns exist
[ ] plant_id values are present
[ ] State relationships are valid
[ ] Recommendation fields contain expected values
[ ] Plant names are available where expected
[ ] Image URLs are valid where available
[ ] No unexpected schema changes exist
```

## 14. Handoff Principle

The application should consume validated processed data rather than raw external data.

```text
External Sources
      ↓
Data Processing
      ↓
Validated Processed Data
      ↓
Application
```

## 15. Future Improvements

```text
Data Collection
      ↓
Automated Processing
      ↓
Automated Validation
      ↓
Dataset Publication
      ↓
Application
```

Automation would reduce manual intervention and make future dataset updates more reproducible.
