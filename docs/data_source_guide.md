# 📊 Data Source Guide

## Biodiversity & Native Planting Planner

**Team:** Vanguard Strategists

## 1. Purpose

This document describes the external sources used by the project and the role each source plays in the data pipeline.

## 2. Source Overview

| Source | Primary Purpose |
|---|---|
| Missouri Botanical Garden | Native plant distribution |
| Lady Bird Johnson Wildflower Center | Plant and gardening characteristics |
| USDA PLANTS Database | Botanical taxonomy |
| Pollinator Interaction Dataset | Pollinator observations |
| iNaturalist API | Plant images |

## 3. Missouri Botanical Garden

Information from the Missouri Botanical Garden contributes to understanding plant distribution and native status.

The processed relationship is represented using:

```text
plant_id
native_state
```

These relationships are stored in:

```text
data/processed/plant_states.csv
```

## 4. Lady Bird Johnson Wildflower Center

This source contributes plant and gardening characteristics such as sunlight requirements, water requirements, soil conditions, soil moisture, soil pH, maintenance, bloom characteristics and plant type.

## 5. USDA PLANTS Database

The USDA PLANTS Database supports botanical taxonomy and standardized plant identification.

Relevant information can include scientific names, common names, classifications and plant families.

## 6. Pollinator Interaction Dataset

Pollinator interaction data provides information about observed relationships between plants and pollinator groups.

Application-ready fields include:

```text
supports_bee_observed
supports_butterfly_observed
supports_hummingbird_observed
supports_moth_observed
supports_fly_observed
supports_beetle_observed
supports_wasp_observed
```

## 7. iNaturalist

iNaturalist is used as a source of plant images. The application can display the plant image and image source.

## 8. Data Integration

```text
Native Distribution
        +
Gardening Characteristics
        +
Taxonomy
        +
Pollinator Data
        +
Image Metadata
        ↓
Integrated Plant Dataset
```

## 9. Data Cleaning

Processing may include:
- Duplicate removal
- Missing-value handling
- Name standardization
- Data-type conversion
- Category normalization
- Identifier matching
- Formatting corrections

## 10. Data Quality

The project considers completeness, consistency, validity, uniqueness, relationship integrity and image availability.

## 11. Attribution

The project acknowledges the organizations and contributors whose public data and resources support this educational project.

Any future redistribution or commercial use should comply with the relevant terms, licensing and attribution requirements of the original sources.

## 12. Summary

```text
Where is the plant native?
        +
How does it grow?
        +
Which pollinators interact with it?
        +
What does it look like?
        ↓
Useful plant recommendation
```
