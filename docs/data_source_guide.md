# Biodiversity & Native Planting Planner
## Data Source Guide

**Project:** Biodiversity & Native Planting Planner

**UN Sustainable Development Goal:** SDG 15 – Life on Land

**Team:** Vanguard Strategists

---

# Purpose

This document describes the datasets used in the Biodiversity & Native Planting Planner, including their sources, purpose, contribution to the project, and how they were processed.

The project integrates multiple publicly available datasets because no single dataset contains all the information required to recommend native plants based on gardening conditions while supporting biodiversity.

---

# Data Sources Overview

| Dataset | Organization | Purpose | Role in Project |
|----------|--------------|---------|-----------------|
| Missouri Botanical Garden (MoBot) | Missouri Botanical Garden | Native plant information | Primary (backbone) dataset |
| Climate Smart Gardening Dataset | Lady Bird Johnson Wildflower Center (via Zenodo) | Gardening characteristics | Plant attributes |
| USDA PLANTS Database | United States Department of Agriculture (USDA) | Botanical taxonomy | Scientific name validation |
| Pollinator Interaction Dataset | Zenodo | Pollinator observations | Biodiversity enrichment |
| iNaturalist API  | iNaturalist | Plant images | Application enhancement |

---

# 1. Missouri Botanical Garden (MoBot)

## Purpose

The Missouri Botanical Garden dataset serves as the primary dataset for this project.

It provides:

- Native U.S. state distribution
- Scientific names
- Common names
- Plant type
- Sunlight requirements
- Moisture requirements
- Maintenance level
- USDA hardiness zones
- Bloom period

---

## Source

**Organization**

Missouri Botanical Garden

**Website**

https://zenodo.org/records/17941612 

---

## Why This Dataset Was Selected

This dataset was selected because it:

- Covers native plants across all 50 U.S. states.
- Provides reliable botanical information.
- Includes state-level native distribution.
- Serves as an ideal backbone for the recommendation system.

---

## Project Processing

The dataset was:

- Downloaded as individual state worksheets.
- Combined into a single dataset.
- Standardized.
- Cleaned.
- Assigned unique plant IDs.
- Used as the backbone of the master dataset.

### Contribution

- **20,091** plant-state records
- **997** unique native plant species

---

# 2. Climate Smart Gardening Dataset (Lady Bird Johnson Wildflower Center)

## Purpose

This dataset provides detailed gardening characteristics that complement the MoBot dataset.

It includes:

- Growth habit
- Bloom color
- Bloom period
- Water use
- Light requirements
- Soil moisture
- Soil pH
- Wildlife value
- Commercial availability
- Propagation information

---

## Source

**Dataset**

Climate Smart Gardening Dataset

**Repository**

Zenodo

**Official Record**

https://zenodo.org/records/17941612

---

## Why This Dataset Was Selected

This dataset contains detailed horticultural attributes that are essential for filtering recommendations based on user gardening preferences.

---

## Project Processing

The dataset was cleaned and standardized before feature engineering.

The following recommendation features were created.

### Sunlight Features

- supports_full_sun
- supports_part_shade
- supports_shade

### Water Features

- supports_low_water
- supports_medium_water
- supports_high_water

### Bloom Month Features

- bloom_jan
- bloom_feb
- bloom_mar
- bloom_apr
- bloom_may
- bloom_jun
- bloom_jul
- bloom_aug
- bloom_sep
- bloom_oct
- bloom_nov
- bloom_dec

---

# 3. USDA PLANTS Database

## Purpose

The USDA PLANTS Database serves as the taxonomic authority for this project.

It provides:

- USDA plant symbols
- Accepted scientific names
- Scientific synonyms
- Plant families

---

## Source

**Organization**

United States Department of Agriculture (USDA)

**Official Download Page**

https://plants.sc.egov.usda.gov/downloads

---

## Why This Dataset Was Selected

Different datasets frequently use different scientific names for the same plant species.

The USDA database provides an authoritative reference that enables:

- Scientific name validation
- Synonym resolution
- USDA symbol mapping
- Family identification

---

## Project Processing

Three reference tables were created.

### Accepted Species Table

Contains accepted scientific names.

### Synonym Crosswalk

Maps outdated scientific names to accepted names.

### USDA Code Crosswalk

Maps USDA plant symbols to accepted scientific names.

These reference tables were used to standardize the Lady Bird Johnson dataset before merging.

---

# 4. Pollinator Interaction Dataset

## Purpose

This dataset provides observed interactions between flowering plants and pollinators.

Observed pollinator groups include:

- Bees
- Butterflies
- Hummingbirds
- Moths
- Flies
- Beetles
- Wasps

---

## Source

**Repository**

Zenodo

**Official Record**

https://zenodo.org/records/6824025

---

## Why This Dataset Was Selected

The Biodiversity & Native Planting Planner promotes biodiversity by recommending plants that support pollinators.

This dataset provides real observation records that enrich plant recommendations.

---

## Project Processing

Processing steps included:

- Cleaning scientific names
- Standardizing taxonomy
- Removing ambiguous plant names
- Classifying pollinator families into broader groups
- Aggregating observations to one record per plant
- Creating Boolean pollinator features

Examples include:

- supports_bee_observed
- supports_butterfly_observed
- supports_hummingbird_observed

---

# 5. iNaturalist API

## Purpose
The iNaturalist API provides plant images for the application.

Fields added:
- image_url
- image_source

---

## Current Status
Integrated. Photo URLs sourced via the iNaturalist taxa API, matched by scientific name, and merged into:
- plants_master.csv
- plants_app.csv

Coverage: 894 of 997 species (89.7%). Remaining gaps are mostly botanical varieties/subspecies not indexed at that granularity on iNaturalist.

---

# Dataset Relationships

```text
                    USDA PLANTS
                         ▲
                         │
                         │
MoBot ───────────────────┼──────── Climate Smart Gardening
                         │
                         ▼
              Pollinator Interaction Dataset
                         │
                         ▼
                 plants_master.csv
                         │
                         ▼
                  plants_app.csv
```

---

# Dataset Processing Summary

| Dataset | Original Records | Final Contribution |
|----------|----------------:|-------------------|
| Missouri Botanical Garden | 20,091 | 997 unique native plant species |
| Climate Smart Gardening | 4,049 | Gardening attributes and engineered recommendation features |
| USDA PLANTS | Reference dataset | Taxonomic validation and synonym resolution |
| Pollinator Interaction Dataset | 67,954 observations | 325 summarized plant records |
| Application Dataset | 997 | Recommendation-ready dataset |

---

# Known Limitations

## Pollinator Coverage

Only exact scientific-name matches were merged into the final application dataset.

Consequently:

- Observed pollinator interactions are available for only a subset of plants.
- A missing observation does **not** indicate that a plant does not support a particular pollinator.

---

## Images

Images
894 of 997 species (89.7%) have an image_url populated, sourced from iNaturalist.
The remaining 103 species — mostly botanical varieties/subspecies — had no match in iNaturalist's database and have no image.

---

## Geographic Scope

The project currently focuses on the **United States** because:

- Native plant distributions vary significantly by country.
- Reliable public datasets are readily available.
- The project scope is appropriate for the available development timeline.
- The narrower scope allows for more accurate recommendations.

---

# Final Deliverables

The Data Analytics team produced the following datasets.

| Dataset | Purpose |
|----------|---------|
| plants_master.csv | Complete integrated dataset for analytics and future maintenance |
| plants_app.csv | Application-ready dataset used by the recommendation engine |
| plant_states.csv | Normalized plant-to-state lookup table |
| data_quality_report.csv | Summary of data validation and coverage |

The recommendation engine should load **plants_app.csv** for all filtering and recommendation operations.

---

# Download References

| Dataset | Official Source |
|----------|-----------------|
| Missouri Botanical Garden (MoBot) | https://zenodo.org/records/17941612 |
| Climate Smart Gardening Dataset | https://zenodo.org/records/17941612 |
| USDA PLANTS Database | https://plants.sc.egov.usda.gov/downloads |
| Pollinator Interaction Dataset | https://zenodo.org/records/6824025 |
| iNaturalist API  | https://api.inaturalist.org/v1/ |

---

## Reproducing the Dataset

To reproduce the application dataset:

1. Download the latest versions of all datasets from the official sources listed above.
2. Place the files into the `data/raw/` directory using the expected folder structure.
3. Open the Jupyter Notebook:

```text
01_build_master_dataset.ipynb
```

4. Run all cells from top to bottom.

The notebook performs the complete data preparation workflow, including:

- Importing raw datasets
- Cleaning and standardizing data
- Normalizing scientific names
- Resolving USDA accepted names and synonyms
- Engineering recommendation features
- Aggregating pollinator observations
- Validating data quality
- Building the master dataset
- Exporting the final datasets

5. Verify that the processed datasets are created in the `data/processed/` directory.

Expected outputs:

```text
plants_master.csv
plants_app.csv
plant_states.csv
data_quality_report.csv
```

Expected validation results:

| Validation | Expected Result |
|------------|----------------:|
| Master dataset rows | 997 |
| Unique plant IDs | 997 |
| Duplicate plant IDs | 0 |
| Missing scientific names | 0 |
| Plants with Lady Bird data | 817 |
| Plants with pollinator observations | 22 |

---

# Contact

**Team:** Vanguard Strategists

### Data Analytics

- Ayotomiwa
- Hanan

### IT Automation

- Adrian

### Cybersecurity

- Favour

For questions regarding the datasets, preprocessing pipeline, or application dataset, please contact the Data Analytics team.
