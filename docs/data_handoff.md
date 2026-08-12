# Biodiversity & Native Planting Planner
## Data Handoff Document

Prepared by:
Data Analytics Team

---

# Overview

The Data Analytics team prepared and integrated multiple public datasets into a production-ready application dataset for the Biodiversity & Native Planting Planner.

The objective was to provide a clean, standardized dataset suitable for filtering native plants based on user gardening preferences.

---

# Datasets Used

## Missouri Botanical Garden (MoBot)

Purpose

- Native plant information
- State distribution
- Basic gardening attributes

---

## Lady Bird Johnson Dataset

Purpose

- Growth habit
- Water requirements
- Light requirements
- Bloom characteristics
- Soil information

---

## USDA PLANTS

Purpose

- Accepted taxonomy
- USDA symbols
- Scientific name validation
- Plant family

---

## Pollinator Dataset

Purpose

- Observed plant-pollinator interactions

---

# Processing Performed

The following preprocessing steps were completed.

## Data Cleaning

- Removed duplicate records
- Standardized column names
- Standardized text formatting
- Normalized scientific names
- Normalized USDA symbols

---

## Feature Engineering

Boolean recommendation features were created.

Examples

- supports_full_sun
- supports_low_water
- bloom_jul
- supports_bee_observed

These fields allow efficient filtering within the recommendation engine.

---

## USDA Taxonomy Resolution

Scientific names were validated using USDA accepted names.

Synonyms were resolved through the USDA synonym crosswalk.

---

## Pollinator Aggregation

Pollinator observations were aggregated so that each plant appears only once in the final dataset.

---

# Final Deliverables

## plants_master.csv

Complete integrated dataset.

Purpose

Long-term storage and future analytics.

---

## plants_app.csv

Application dataset.

Purpose

Primary dataset for the recommendation engine.

The web application should load this dataset.

---

## plant_states.csv

Normalized plant-state lookup table.

Purpose

Future expansion and relational querying.

---

## data_quality_report.csv

Summary statistics describing dataset completeness.

---

# Data Quality Summary

Total native plants

997

Plants with Ladybird information

817

Plants with pollinator observations

22

Duplicate plant IDs

0

Missing scientific names

0

---

# Known Limitations

The pollinator dataset contains limited exact-name matches with the native plant dataset.

Only plants with exact scientific-name matches were merged.

As a result, pollinator coverage should be interpreted as observed interactions within the available dataset rather than a complete representation of all pollinator relationships.

---

# Recommendation Engine Usage

The recommendation engine should load:

plants_app.csv

The application should filter using Boolean columns rather than text matching.

Example

supports_full_sun

supports_low_water

supports_bee_observed

This provides significantly faster filtering and simpler application logic.

---

# Future Enhancements

- Improve taxonomic matching
- Add recommendation scoring
- Expand support beyond the United States
