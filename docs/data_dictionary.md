# 📖 Data Dictionary

## Biodiversity & Native Planting Planner

## 1. Purpose

This document describes the important fields used by the Biodiversity & Native Planting Planner.

Main application datasets:

```text
data/processed/plants_app.csv
data/processed/plant_states.csv
```

## 2. Plant Identification Fields

| Field | Description |
|---|---|
| `plant_id` | Identifier used to connect plant records |
| `display_name` | Plant name displayed by the application |
| `common_name` | Common plant name |
| `scientific_name` | Scientific botanical name |
| `plant_family` | Botanical family |
| `plant_type` | General plant type |

## 3. Sunlight Fields

| Field | Description |
|---|---|
| `supports_full_sun` | Indicates support for full-sun conditions |
| `supports_part_shade` | Indicates support for part-shade conditions |
| `supports_shade` | Indicates support for shade conditions |

## 4. Water Fields

| Field | Description |
|---|---|
| `supports_low_water` | Indicates suitability for low-water conditions |
| `supports_medium_water` | Indicates suitability for medium-water conditions |
| `supports_high_water` | Indicates suitability for high-water conditions |

## 5. Pollinator Fields

| Field | Description |
|---|---|
| `supports_bee_observed` | Bee interaction observed |
| `supports_butterfly_observed` | Butterfly interaction observed |
| `supports_hummingbird_observed` | Hummingbird interaction observed |
| `supports_moth_observed` | Moth interaction observed |
| `supports_fly_observed` | Fly interaction observed |
| `supports_beetle_observed` | Beetle interaction observed |
| `supports_wasp_observed` | Wasp interaction observed |

## 6. Soil Fields

| Field | Description |
|---|---|
| `soil_description` | Description of suitable soil conditions |
| `soil_moisture` | Preferred soil moisture |
| `soil_ph` | Soil pH information |

## 7. Maintenance and Climate Fields

| Field | Description |
|---|---|
| `maintenance` | Plant maintenance requirement |
| `zone_min` | Minimum hardiness zone |
| `zone_max` | Maximum hardiness zone |

## 8. Bloom Fields

| Field | Description |
|---|---|
| `bloom_color` | Recorded bloom colors |
| `bloom_jan` through `bloom_dec` | Monthly bloom indicators |

The application converts monthly Boolean fields into a readable bloom-season description.

## 9. Image Fields

| Field | Description |
|---|---|
| `image_url` | URL used for plant image display |
| `image_source` | Source of the plant image |

## 10. State Dataset

### `plant_states.csv`

| Field | Description |
|---|---|
| `plant_id` | Plant identifier matching the application dataset |
| `native_state` | U.S. state associated with the plant's native distribution |

## 11. Dataset Relationship

```text
plants_app.csv
      │
      │ plant_id
      ▼
plant_states.csv
      │
      ▼
Native State Relationship
```

## 12. Recommendation Fields

The recommendation engine primarily uses:

```text
plant_id

supports_full_sun
supports_part_shade
supports_shade

supports_low_water
supports_medium_water
supports_high_water

supports_bee_observed
supports_butterfly_observed
supports_hummingbird_observed
supports_moth_observed
supports_fly_observed
supports_beetle_observed
supports_wasp_observed
```

## 13. Data Types

Recommendation fields are expected to behave as Boolean values:

```text
True
False
```

Descriptive plant fields are generally text. Numeric fields such as hardiness zones may be represented numerically.

## 14. Dictionary Maintenance

Update this document whenever:
- A new application field is introduced.
- An existing field changes meaning.
- A new recommendation criterion is added.
- Dataset structure changes.
- A new external source is integrated.
