# Biodiversity & Native Planting Planner
## Data Dictionary

### Dataset
**plants_app.csv**

This dataset is the primary dataset used by the recommendation engine. Each row represents one native plant.

---

## Identity

| Column | Description |
|---------|-------------|
| plant_id | Unique identifier for each plant |
| scientific_name | Accepted scientific name |
| common_name | Common plant name |
| display_name | Preferred display name shown in the application |
| plant_family | Botanical family |

---

## Geographic Information

| Column | Description |
|---------|-------------|
| native_states | Pipe-separated list of U.S. states where the plant is native |

Example

Texas | Oklahoma | Louisiana

---

## Growth Characteristics

| Column | Description |
|---------|-------------|
| growth_habit | Tree, Shrub, Herb, Vine, etc. |
| plant_type | General plant category |
| zone_min | Minimum USDA hardiness zone |
| zone_max | Maximum USDA hardiness zone |
| maintenance | Maintenance requirement |
| soil_description | Preferred soil description |
| soil_moisture | Soil moisture preference |
| soil_ph | Preferred soil pH |

---

## Sunlight

| Column | Description |
|---------|-------------|
| supports_full_sun | Suitable for full sun |
| supports_part_shade | Suitable for partial shade |
| supports_shade | Suitable for shade |

---

## Water

| Column | Description |
|---------|-------------|
| supports_low_water | Suitable for low water |
| supports_medium_water | Suitable for medium water |
| supports_high_water | Suitable for high water |

---

## Bloom Information

| Column | Description |
|---------|-------------|
| bloom_color | Flower color |

Monthly bloom indicators

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

Each column contains:

- TRUE → blooms during that month
- FALSE → does not bloom

---

## Pollinator Support

| Column | Description |
|---------|-------------|
| supports_bee_observed | Bee interactions observed |
| supports_butterfly_observed | Butterfly interactions observed |
| supports_hummingbird_observed | Hummingbird interactions observed |
| supports_moth_observed | Moth interactions observed |
| supports_fly_observed | Fly interactions observed |
| supports_beetle_observed | Beetle interactions observed |
| supports_wasp_observed | Wasp interactions observed |

These fields indicate observations from the pollinator dataset and should not be interpreted as exhaustive ecological relationships.

---

## Images

| Column | Description |
|---------|-------------|
| image_url | URL of plant image |
| image_source | Source of plant image (e.g., iNaturalist) |


---

## Dataset Flags

| Column | Description |
|---------|-------------|
| has_ladybird_data | Indicates whether gardening attributes were available |
| has_pollinator_data | Indicates whether pollinator observations were available |
