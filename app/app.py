import os
import sys
import pandas as pd


def load_datasets():
  """Loads the processed datasets produced by the Data Analytics team."""
  base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
  app_data_path = os.path.join(base_dir, "data", "processed", "plants_app.csv")
  state_data_path = os.path.join(
      base_dir, "data", "processed", "plant_states.csv"
  )

  try:
    plants_df = pd.read_csv(app_data_path)
    states_df = pd.read_csv(state_data_path)
    return plants_df, states_df
  except FileNotFoundError as e:
    print(f"\n❌ Error loading dataset: {e}")
    sys.exit(1)


def get_user_selection(prompt_text, options_dict):
  """Presents numeric options to the user and securely validates input."""
  print(f"\n{prompt_text}")
  keys = list(options_dict.keys())
  for idx, key in enumerate(keys, 1):
    print(f"  [{idx}] {key}")

  while True:
    choice = input("\nEnter choice (number or name): ").strip()
    if choice.isdigit() and 1 <= int(choice) <= len(keys):
      selected_key = keys[int(choice) - 1]
      return options_dict[selected_key]

    for key in keys:
      if choice.lower() == key.lower():
        return options_dict[key]

    print("⚠️ Invalid input. Please select a valid option from the list.")


def get_recommendations(plants_df, states_df, state, sun_col, water_col, pol_col):
  """Filters plants native to the chosen state that match the selected conditions."""
  # 1. Get plant IDs native to selected state
  state_matches = states_df[
      states_df["native_state"].str.lower() == state.lower()
  ]
  native_ids = state_matches["plant_id"].unique()

  # 2. Filter main dataset
  mask = (
      (plants_df["plant_id"].isin(native_ids))
      & (plants_df[sun_col] == True)
      & (plants_df[water_col] == True)
  )

  if pol_col is not None:
    mask = mask & (plants_df[pol_col] == True)

  return plants_df[mask]


def main():
  print("=" * 65)
  print("🌱 Biodiversity & Native Planting Planner (UN SDG Goal 15) 🐝")
  print("=" * 65)

  plants_df, states_df = load_datasets()

  # Extract valid unique states
  valid_states = sorted(states_df["native_state"].dropna().unique().tolist())
  state_options = {s: s for s in valid_states}

  sunlight_options = {
      "Full Sun": "supports_full_sun",
      "Partial Shade": "supports_part_shade",
      "Full Shade": "supports_shade",
  }

  water_options = {
      "Low Water": "supports_low_water",
      "Medium Water": "supports_medium_water",
      "High Water": "supports_high_water",
  }

  pollinator_options = {
      "Bees": "supports_bee_observed",
      "Butterflies": "supports_butterfly_observed",
      "Hummingbirds": "supports_hummingbird_observed",
      "Moths": "supports_moth_observed",
      "Any / No Preference": None,
  }

  # Step 1: State Selection
  print("\n📍 Step 1: Select your State")
  while True:
    state_input = input("Enter your US State (e.g., California, Texas): ").strip()
    matched = [s for s in valid_states if s.lower() == state_input.lower()]
    if matched:
      selected_state = matched[0]
      break
    print("⚠️ State not recognized. Please check spelling and try again.")

  # Steps 2-4: Condition Selection
  selected_sun = get_user_selection(
      "☀️ Step 2: Select Sunlight Condition", sunlight_options
  )
  selected_water = get_user_selection(
      "💧 Step 3: Select Water Availability", water_options
  )
  selected_pol = get_user_selection(
      "🦋 Step 4: Select Target Pollinator", pollinator_options
  )

  # Run recommendation engine
  print(f"\n🔍 Searching native plants for {selected_state}...")
  results = get_recommendations(
      plants_df,
      states_df,
      selected_state,
      selected_sun,
      selected_water,
      selected_pol,
  )

  # Output recommendations
  print("-" * 65)
  if results.empty:
    print("No exact matches found. Try broadening your water or pollinator criteria!")
  else:
    print(f"✅ Found {len(results)} matching native plant(s):\n")
    for idx, (_, row) in enumerate(results.iterrows(), 1):
      name = row.get("display_name") or row.get("scientific_name")
      sci_name = row.get("scientific_name", "")
      img = row.get("image_url", "No image link available")
      habit = row.get("growth_habit", "N/A")

      print(f"  {idx}. 🌿 {name} ({sci_name})")
      print(f"     🌱 Habit: {habit}")
      print(f"     🖼️  Image: {img}")
      print()


if __name__ == "__main__":
  main()