import os
import pandas as pd
import streamlit as st


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Biodiversity Planner",
    page_icon="🌿",
    layout="wide",
)


# ============================================================
# SESSION STATE
# ============================================================

if "searched" not in st.session_state:
    st.session_state.searched = False

if "show_alternatives" not in st.session_state:
    st.session_state.show_alternatives = False


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
<style>

/* ============================================================
   GLOBAL
   ============================================================ */

.stApp {
    background: #f7f8f3;
}

.block-container {
    max-width: 1180px;
    padding-top: 1.5rem;
    padding-bottom: 4rem;
}


/* ============================================================
   HEADER
   ============================================================ */

.brand {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 2.5rem;
}

.brand-icon {
    font-size: 1.8rem;
}

.brand-name {
    font-size: 1.05rem;
    font-weight: 750;
    color: #26352b;
}


/* ============================================================
   HERO
   ============================================================ */

.hero {
    margin-bottom: 2.8rem;
}

.hero-title {
    font-size: 3.4rem;
    line-height: 1.03;
    letter-spacing: -0.055em;
    font-weight: 800;
    color: #1e2c23;
    max-width: 780px;
    margin-bottom: 1rem;
}

.hero-highlight {
    color: #4d7d55;
}

.hero-description {
    font-size: 1.05rem;
    line-height: 1.7;
    color: #6d766f;
    max-width: 650px;
}


/* ============================================================
   PLANNER
   ============================================================ */

.planner-wrapper {
    background: #ffffff;
    border: 1px solid #e3e9e1;
    border-radius: 20px;
    padding: 1.7rem 1.8rem 1.8rem 1.8rem;
    margin-bottom: 1.5rem;
    box-shadow: 0 10px 35px rgba(35, 55, 40, 0.05);
}

.planner-title {
    font-size: 1.25rem;
    font-weight: 750;
    color: #26352b;
    margin-bottom: 0.25rem;
}

.planner-description {
    font-size: 0.88rem;
    color: #7a837c;
    margin-bottom: 0;
}


/* ============================================================
   INPUTS
   ============================================================ */

div[data-baseweb="select"] > div {
    border-radius: 10px !important;
    border-color: #dce4da !important;
    background: #fbfcfa !important;
    min-height: 44px;
}

div[data-baseweb="select"] > div:hover {
    border-color: #6c9273 !important;
}

label {
    color: #3b493f !important;
    font-weight: 650 !important;
}


/* ============================================================
   BUTTONS
   ============================================================ */

.stButton > button {
    width: 100%;
    min-height: 48px;
    border-radius: 10px;
    border: none;
    background: #47764f;
    color: white;
    font-weight: 700;
    font-size: 0.95rem;
    transition:
        background 0.15s ease,
        transform 0.15s ease;
}

.stButton > button:hover {
    background: #365f3e;
    color: white;
}

.stButton > button:active {
    transform: translateY(1px);
}


/* ============================================================
   MOBILE NAVIGATION
   ============================================================ */

.mobile-results-nav {
    margin-bottom: 1.5rem;
}

.mobile-results-nav-title {
    color: #26352b;
    font-size: 1rem;
    font-weight: 750;
    margin-bottom: 0.15rem;
}

.mobile-results-nav-subtitle {
    color: #7a837c;
    font-size: 0.75rem;
}


/* Back button */

.st-key-mobile_back_button button {
    width: auto !important;
    min-width: 105px;
    background: transparent !important;
    color: #47764f !important;
    border: 1px solid #d6e0d4 !important;
    font-size: 0.82rem !important;
    min-height: 40px !important;
}

.st-key-mobile_back_button button:hover {
    background: #edf4ec !important;
    color: #365f3e !important;
}


/* ============================================================
   RESULTS HEADER
   ============================================================ */

.results-header {
    margin-bottom: 1.5rem;
}

.results-eyebrow {
    font-size: 0.75rem;
    font-weight: 750;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #6f846f;
    margin-bottom: 0.35rem;
}

.results-title {
    font-size: 1.75rem;
    font-weight: 800;
    color: #26352b;
    margin-bottom: 0.25rem;
}

.results-description {
    color: #737d75;
    font-size: 0.9rem;
    line-height: 1.5;
}

.result-count {
    display: inline-block;
    margin-top: 0.7rem;
    background: #e7f1e8;
    color: #3e6844;
    padding: 0.35rem 0.7rem;
    border-radius: 999px;
    font-size: 0.78rem;
    font-weight: 700;
}


/* ============================================================
   GARDEN SUMMARY
   ============================================================ */

.garden-summary {
    display: flex;
    flex-wrap: wrap;
    gap: 0.45rem;
    margin-top: 0.9rem;
}

.summary-pill {
    display: inline-flex;
    align-items: center;
    background: #f0f4ed;
    color: #526554;
    border: 1px solid #e3e9e1;
    border-radius: 999px;
    padding: 0.32rem 0.58rem;
    font-size: 0.72rem;
    font-weight: 650;
}


/* ============================================================
   PLANT CARD
   ============================================================ */

.plant-card {
    background: #ffffff;
    border: 1px solid #e1e7df;
    border-radius: 16px;
    padding: 0.8rem;
    height: 100%;
    box-shadow: 0 5px 20px rgba(35, 55, 40, 0.035);
}

.plant-name {
    font-size: 1.08rem;
    font-weight: 750;
    color: #29372e;
    margin-top: 0.85rem;
    line-height: 1.35;
}

.plant-scientific {
    color: #7a837c;
    font-size: 0.82rem;
    font-style: italic;
    margin-top: 0.15rem;
    margin-bottom: 0.7rem;
}

.plant-info {
    font-size: 0.8rem;
    color: #59645c;
    line-height: 1.7;
}

.tag-row {
    margin-bottom: 0.65rem;
}

.tag {
    display: inline-block;
    background: #f0f4ed;
    color: #526554;
    border-radius: 6px;
    padding: 0.28rem 0.45rem;
    margin-right: 0.25rem;
    margin-bottom: 0.25rem;
    font-size: 0.7rem;
    font-weight: 650;
}

.tag.match {
    background: #edf7ed;
    color: #2f6b37;
    border: 1px solid #cfe4d1;
}

.tag.no-match {
    background: #faf4f2;
    color: #87645d;
    border: 1px solid #eadbd7;
}

.match-score {
    display: inline-block;
    margin-top: 0.45rem;
    margin-bottom: 0.15rem;
    color: #4c654f;
    font-size: 0.72rem;
    font-weight: 750;
}

.match-box {
    background: #f5f8f3;
    border: 1px solid #e3eae1;
    border-radius: 9px;
    padding: 0.6rem 0.7rem;
    margin: 0.75rem 0;
    color: #4e5f52;
    font-size: 0.76rem;
    line-height: 1.5;
}

.match-title {
    color: #365f3e;
    font-weight: 750;
    margin-bottom: 0.15rem;
}

.source {
    color: #939b95;
    font-size: 0.68rem;
    margin-top: 0.7rem;
}


/* ============================================================
   IMAGE PLACEHOLDER
   ============================================================ */

.image-placeholder {
    height: 220px;
    background: #edf2eb;
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 3rem;
}


/* ============================================================
   EMPTY STATE
   ============================================================ */

.empty-state {
    background: #ffffff;
    border: 1px solid #e2e8e0;
    border-radius: 18px;
    text-align: center;
    padding: 3rem 1.5rem;
}

.empty-icon {
    font-size: 2.4rem;
}

.empty-title {
    color: #344238;
    font-size: 1.2rem;
    font-weight: 750;
    margin-top: 0.5rem;
}

.empty-description {
    color: #788178;
    max-width: 500px;
    margin: 0.5rem auto 0 auto;
    line-height: 1.6;
}


/* ============================================================
   EXPANDER
   ============================================================ */

div[data-testid="stExpander"] {
    border: 1px solid #e4e9e3;
    border-radius: 9px;
    background: #fbfcfa;
}


/* ============================================================
   FOOTER
   ============================================================ */

.footer {
    margin-top: 4rem;
    padding-top: 1.5rem;
    border-top: 1px solid #dfe5dc;
    text-align: center;
    color: #89918a;
    font-size: 0.75rem;
}


/* ============================================================
   MOBILE SCREEN SWITCHING
   ============================================================

   Streamlit adds:
       st-key-search_visible
       st-key-search_hidden
       st-key-results_visible
       st-key-results_hidden

   to keyed containers.

   Desktop:
       Everything remains visible.

   Mobile:
       Hide whichever screen is marked "hidden".
*/


@media (max-width: 768px) {

    .st-key-search_hidden {
        display: none !important;
    }

    .st-key-results_hidden {
        display: none !important;
    }

}


/* ============================================================
   TABLET
   ============================================================ */

@media (max-width: 900px) {

    .block-container {
        padding-left: 1.25rem;
        padding-right: 1.25rem;
    }

    .hero-title {
        font-size: 2.8rem;
    }

}


/* ============================================================
   PHONE
   ============================================================ */

@media (max-width: 600px) {

    .block-container {
        padding-left: 0.85rem;
        padding-right: 0.85rem;
        padding-top: 1rem;
        padding-bottom: 2.5rem;
    }

    .brand {
        margin-bottom: 1.5rem;
    }

    .brand-icon {
        font-size: 1.55rem;
    }

    .brand-name {
        font-size: 0.95rem;
    }

    .hero {
        margin-bottom: 1.5rem;
    }

    .hero-title {
        font-size: 2.25rem;
        line-height: 1.05;
        letter-spacing: -0.045em;
        margin-bottom: 0.8rem;
    }

    .hero-description {
        font-size: 0.9rem;
        line-height: 1.6;
    }

    .planner-wrapper {
        padding: 1.15rem;
        border-radius: 16px;
    }

    .planner-title {
        font-size: 1.1rem;
    }

    .planner-description {
        font-size: 0.82rem;
        line-height: 1.5;
    }

    div[data-baseweb="select"] > div {
        min-height: 46px;
    }

    .results-header {
        margin-bottom: 1.1rem;
    }

    .results-title {
        font-size: 1.5rem;
        line-height: 1.15;
    }

    .results-description {
        font-size: 0.82rem;
    }

    .garden-summary {
        gap: 0.3rem;
    }

    .summary-pill {
        font-size: 0.67rem;
        padding: 0.3rem 0.5rem;
    }

    .plant-name {
        font-size: 1.05rem;
    }

    .plant-scientific {
        font-size: 0.78rem;
    }

    .plant-info {
        font-size: 0.78rem;
    }

    .match-box {
        font-size: 0.73rem;
    }

    .image-placeholder {
        height: 205px;
    }

    .footer {
        margin-top: 2.5rem;
        font-size: 0.68rem;
        line-height: 1.6;
    }

}


/* ============================================================
   VERY SMALL PHONES
   ============================================================ */

@media (max-width: 380px) {

    .hero-title {
        font-size: 2rem;
    }

    .results-title {
        font-size: 1.4rem;
    }

    .image-placeholder {
        height: 185px;
    }

}

</style>
""",
    unsafe_allow_html=True,
)


# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def load_datasets():

    base_dir = os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )

    plants_path = os.path.join(
        base_dir,
        "data",
        "processed",
        "plants_app.csv",
    )

    states_path = os.path.join(
        base_dir,
        "data",
        "processed",
        "plant_states.csv",
    )

    plants_df = pd.read_csv(plants_path)
    states_df = pd.read_csv(states_path)

    return plants_df, states_df


# ============================================================
# RECOMMENDATION ENGINE
# ============================================================

def get_native_plants(
    plants_df,
    states_df,
    state,
):

    state_matches = states_df[
        states_df["native_state"]
        .astype(str)
        .str.strip()
        .str.lower()
        == state.strip().lower()
    ]

    native_ids = state_matches["plant_id"].unique()

    return plants_df[
        plants_df["plant_id"].isin(native_ids)
    ].copy()


def _is_true(series):
    return (
        series
        .fillna(False)
        .astype(str)
        .str.strip()
        .str.lower()
        .isin(["true", "1", "yes", "y"])
    )


def get_recommendations(
    plants_df,
    states_df,
    state,
    sunlight_col,
    water_col,
    pollinator_col=None,
):
    """Return ONLY plants that match every selected condition."""

    results = get_native_plants(plants_df, states_df, state).copy()

    if results.empty:
        return results

    results["sunlight_match"] = _is_true(results[sunlight_col])
    results["water_match"] = _is_true(results[water_col])

    if pollinator_col is None:
        results["pollinator_match"] = True
    else:
        results["pollinator_match"] = _is_true(results[pollinator_col])

    # IMPORTANT: the normal results screen is STRICT.
    # A plant must match sunlight + water + pollinator.
    exact_mask = (
        results["sunlight_match"]
        & results["water_match"]
        & results["pollinator_match"]
    )

    results = results.loc[exact_mask].copy()

    # Every plant returned by this function is an exact match.
    results["match_score"] = 8

    return results.reset_index(drop=True)


def get_alternatives(
    plants_df,
    states_df,
    state,
    sunlight_col,
    water_col,
    pollinator_col=None,
):
    """Return native alternatives ranked by how many preferences match."""

    results = get_native_plants(
        plants_df,
        states_df,
        state,
    )

    if results.empty:
        return results

    results["sunlight_match"] = _is_true(
        results[sunlight_col]
    )

    results["water_match"] = _is_true(
        results[water_col]
    )

    if pollinator_col is not None:
        results["pollinator_match"] = _is_true(
            results[pollinator_col]
        )
    else:
        results["pollinator_match"] = True

    results["match_score"] = (
        results["sunlight_match"].astype(int) * 3
        + results["water_match"].astype(int) * 3
        + results["pollinator_match"].astype(int) * 2
    )

    # Alternatives are only a fallback. Never overwhelm the user with
    # the full list of native plants; show the strongest few only.
    return (
        results
        .sort_values(
            by="match_score",
            ascending=False,
            kind="stable",
        )
        .head(6)
        .reset_index(drop=True)
    )

# ============================================================
# HELPERS
# ============================================================

def clean(value, fallback="N/A"):

    if pd.isna(value):
        return fallback

    value = str(value).strip()

    if not value or value.lower() == "nan":
        return fallback

    return value


def get_bloom_months(row):

    months = [
        ("jan", "Jan"),
        ("feb", "Feb"),
        ("mar", "Mar"),
        ("apr", "Apr"),
        ("may", "May"),
        ("jun", "Jun"),
        ("jul", "Jul"),
        ("aug", "Aug"),
        ("sep", "Sep"),
        ("oct", "Oct"),
        ("nov", "Nov"),
        ("dec", "Dec"),
    ]

    result = []

    for key, label in months:

        value = row.get(
            f"bloom_{key}"
        )

        if (
            value is True
            or str(value).lower() == "true"
        ):
            result.append(label)

    return (
        ", ".join(result)
        if result
        else "N/A"
    )


def get_pollinator_label(
    pollinator
):

    if (
        pollinator
        == "🌱 Any / No Preference"
    ):
        return "No pollinator preference"

    return pollinator


# ============================================================
# HEADER
# ============================================================

st.markdown(
    """
<div class="brand">
    <div class="brand-icon">🌿</div>
    <div class="brand-name">Native Planner</div>
</div>
""",
    unsafe_allow_html=True,
)


# ============================================================
# HERO
#
# The key changes depending on the current state.
#
# Desktop:
#   Always visible.
#
# Mobile:
#   Visible before search.
#   Hidden after search.
# ============================================================

hero_key = (
    "hero_visible"
    if not st.session_state.searched
    else "hero_hidden"
)


with st.container(
    key=hero_key
):

    st.markdown(
        """
<div class="hero">

<div class="hero-title">
Find plants that belong
<span class="hero-highlight">
in your garden.
</span>
</div>

<div class="hero-description">
Discover native plants matched to your local environment,
gardening conditions, and the pollinators you want to support.
</div>

</div>
""",
        unsafe_allow_html=True,
    )


# ============================================================
# DATA
# ============================================================

try:

    plants_df, states_df = load_datasets()

except FileNotFoundError:

    st.error(
        "Dataset files not found. Please check "
        "data/processed/."
    )

    st.stop()


# ============================================================
# OPTIONS
# ============================================================

states = sorted(
    states_df["native_state"]
    .dropna()
    .unique()
    .tolist()
)


sunlight_map = {
    "Full Sun": "supports_full_sun",
    "Part Shade": "supports_part_shade",
    "Shade": "supports_shade",
}


water_map = {
    "Low Water": "supports_low_water",
    "Medium Water": "supports_medium_water",
    "High Water": "supports_high_water",
}


pollinator_map = {
    "🐝 Bees": "supports_bee_observed",
    "🦋 Butterflies": "supports_butterfly_observed",
    "🐦 Hummingbirds": "supports_hummingbird_observed",
    "🦋 Moths": "supports_moth_observed",
    "🪰 Flies": "supports_fly_observed",
    "🪲 Beetles": "supports_beetle_observed",
    "🐝 Wasps": "supports_wasp_observed",
    "🌱 Any / No Preference": None,
}


# ============================================================
# SEARCH SCREEN
#
# Desktop:
#   Always visible.
#
# Mobile:
#   Visible before clicking Find My Plants.
#   Hidden after clicking Find My Plants.
# ============================================================

search_key = (
    "search_visible"
    if not st.session_state.searched
    else "search_hidden"
)


with st.container(
    key=search_key
):

    # --------------------------------------------------------
    # PLANNER INTRO
    # --------------------------------------------------------

    st.markdown(
        """
<div class="planner-wrapper">

<div class="planner-title">
Plan your garden
</div>

<div class="planner-description">
Tell us about your space and we'll find suitable native plants.
</div>

</div>
""",
        unsafe_allow_html=True,
    )


    # --------------------------------------------------------
    # ROW 1
    # --------------------------------------------------------

    col1, col2 = st.columns(2)


    with col1:

        state = st.selectbox(
            "📍 Where is your garden?",
            states,
            key="state_select",
        )


    with col2:

        sunlight = st.selectbox(
            "☀️ How much sunlight?",
            list(sunlight_map.keys()),
            key="sunlight_select",
        )


    # --------------------------------------------------------
    # ROW 2
    # --------------------------------------------------------

    col3, col4 = st.columns(2)


    with col3:

        water = st.selectbox(
            "💧 How much water is available?",
            list(water_map.keys()),
            key="water_select",
        )


    with col4:

        pollinator = st.selectbox(
            "🦋 Which pollinator do you want to support?",
            list(pollinator_map.keys()),
            key="pollinator_select",
        )


    st.markdown(
        "<div style='height:8px'></div>",
        unsafe_allow_html=True,
    )


    # --------------------------------------------------------
    # FIND BUTTON
    # --------------------------------------------------------

    find_button = st.button(
        "🌱 Find My Plants",
        use_container_width=True,
        key="find_plants_button",
    )


    if find_button:

        st.session_state.selected_state = state
        st.session_state.selected_sunlight = sunlight
        st.session_state.selected_water = water
        st.session_state.selected_pollinator = pollinator
        st.session_state.show_alternatives = False

        st.session_state.searched = True

        st.rerun()


# ============================================================
# RESULTS SCREEN
#
# Desktop:
#   Always visible after search.
#
# Mobile:
#   Hidden before search.
#   Visible after search.
# ============================================================

results_key = (
    "results_visible"
    if st.session_state.searched
    else "results_hidden"
)


with st.container(
    key=results_key
):

    if st.session_state.searched:

        # ----------------------------------------------------
        # GET SAVED SEARCH VALUES
        # ----------------------------------------------------

        state = st.session_state.selected_state
        sunlight = st.session_state.selected_sunlight
        water = st.session_state.selected_water
        pollinator = (
            st.session_state.selected_pollinator
        )


        # ----------------------------------------------------
        # MOBILE NAVIGATION
        # ----------------------------------------------------

        mobile_nav_left, mobile_nav_right = st.columns(
            [1, 2]
        )


        with mobile_nav_left:

            back_button = st.button(
                "← Search",
                key="mobile_back_button",
            )


        with mobile_nav_right:

            st.markdown(
                """
<div class="mobile-results-nav">

<div class="mobile-results-nav-title">
Your garden results
</div>

<div class="mobile-results-nav-subtitle">
Native plants matched to your selections
</div>

</div>
""",
                unsafe_allow_html=True,
            )


        if back_button:

            st.session_state.searched = False
            st.session_state.show_alternatives = False

            st.rerun()


        # ----------------------------------------------------
        # RECOMMENDATIONS
        # ----------------------------------------------------

        exact_results = get_recommendations(
            plants_df,
            states_df,
            state,
            sunlight_map[sunlight],
            water_map[water],
            pollinator_map[pollinator],
        )

        alternatives = get_alternatives(
            plants_df,
            states_df,
            state,
            sunlight_map[sunlight],
            water_map[water],
            pollinator_map[pollinator],
        )

        # ----------------------------------------------------
        # STRICT RESULT FLOW
        # ----------------------------------------------------
        # Exact matches always win. Alternatives are NEVER shown
        # automatically, even if they exist.
        if not exact_results.empty:
            results = exact_results.copy()
            showing_alternatives = False
            # If exact matches exist, alternatives must not remain
            # visible from a previous interaction.
            st.session_state.show_alternatives = False
        elif st.session_state.show_alternatives:
            results = alternatives.copy()
            showing_alternatives = True
        else:
            results = exact_results.copy()
            showing_alternatives = False


        # ----------------------------------------------------
        # RESULTS HEADER
        # ----------------------------------------------------

        result_word = (
            "plant"
            if len(results) == 1
            else "plants"
        )

        if showing_alternatives:
            results_eyebrow = "OTHER OPTIONS"
            results_title = "Here are some alternatives"
            results_description = (
                f"These native plants match some of your preferences in {state}."
            )
        elif results.empty:
            results_eyebrow = "NO EXACT MATCHES"
            results_title = "No plants found"
            results_description = (
                f"We couldn't find a native plant in {state} that matches all your selections."
            )
        else:
            results_eyebrow = "YOUR RECOMMENDATIONS"
            results_title = "Plants picked for your garden"
            results_description = (
                f"Native plants matching all your selected conditions in {state}."
            )


        pollinator_label = (
            get_pollinator_label(
                pollinator
            )
        )


        st.markdown(
            f"""
<div class="results-header">

<div class="results-eyebrow">
{results_eyebrow}
</div>

<div class="results-title">
{results_title}
</div>

<div class="results-description">
{results_description}
</div>

<div class="result-count">
{len(results)} {result_word} found
</div>

<div class="garden-summary">

<span class="summary-pill">
📍 {state}
</span>

<span class="summary-pill">
☀️ {sunlight}
</span>

<span class="summary-pill">
💧 {water}
</span>

<span class="summary-pill">
{pollinator_label}
</span>

</div>

</div>
""",
            unsafe_allow_html=True,
        )


        # ----------------------------------------------------
        # NO EXACT RESULTS
        # ----------------------------------------------------

        if results.empty:

            st.markdown(
                f"""
<div class="empty-state">

<div class="empty-icon">
🌱
</div>

<div class="empty-title">
No exact matches found
</div>

<div class="empty-description">
We couldn't find a native plant in {state} that matches all of your selected conditions.
</div>

</div>
""",
                unsafe_allow_html=True,
            )

            if not st.session_state.show_alternatives and not alternatives.empty:
                show_alternatives = st.button(
                    "🌿 Show Other Alternatives",
                    use_container_width=True,
                    key="show_alternatives_button",
                )

                if show_alternatives:
                    st.session_state.show_alternatives = True
                    st.rerun()

            elif alternatives.empty:
                st.markdown(
                    f"""
<div class="empty-description" style="text-align:center; margin-top:1rem;">
There are no native plants in our dataset for {state}.
</div>
""",
                    unsafe_allow_html=True,
                )


        # ----------------------------------------------------
        # RESULTS CARDS
        # ----------------------------------------------------

        else:

            # Defensive guard: normal results must never contain a
            # partial match. If this screen is not showing alternatives,
            # only exact 8/8 records are allowed through to the cards.
            if not showing_alternatives:
                results = results[
                    results["match_score"] == 8
                ].copy().reset_index(drop=True)

            if showing_alternatives:
                st.markdown(
                    """
<div class="match-box">

<div class="match-title">
Showing alternatives
</div>

These plants are native to your selected location but do not match every preference. They are ranked by the number of conditions they match.

</div>
""",
                    unsafe_allow_html=True,
                )

            # ------------------------------------------------
            # Desktop uses 3 columns.
            #
            # Mobile uses the same columns structurally,
            # but each result occupies its own row.
            # ------------------------------------------------

            for start in range(
                0,
                len(results),
                3,
            ):

                result_row = results.iloc[
                    start:start + 3
                ]


                cols = st.columns(3)


                for col, (_, row) in zip(
                    cols,
                    result_row.iterrows(),
                ):

                    with col:

                        # ====================================
                        # CARD START
                        # ====================================

                        st.markdown(
                            """
<div class="plant-card">
""",
                            unsafe_allow_html=True,
                        )


                        # ====================================
                        # IMAGE
                        # ====================================

                        image_url = row.get(
                            "image_url"
                        )


                        if (
                            pd.notna(image_url)
                            and str(
                                image_url
                            ).strip()
                            and str(
                                image_url
                            ).lower()
                            != "nan"
                        ):

                            try:

                                st.image(
                                    image_url,
                                    use_container_width=True,
                                )

                            except Exception:

                                st.markdown(
                                    """
<div class="image-placeholder">
🌱
</div>
""",
                                    unsafe_allow_html=True,
                                )

                        else:

                            st.markdown(
                                """
<div class="image-placeholder">
🌱
</div>
""",
                                unsafe_allow_html=True,
                            )


                        # ====================================
                        # NAME
                        # ====================================

                        name = clean(
                            row.get(
                                "display_name"
                            ),
                            clean(
                                row.get(
                                    "common_name"
                                ),
                                "Unknown plant",
                            ),
                        )


                        scientific = clean(
                            row.get(
                                "scientific_name"
                            )
                        )


                        st.markdown(
                            f"""
<div class="plant-name">
{name}
</div>

<div class="plant-scientific">
{scientific}
</div>
""",
                            unsafe_allow_html=True,
                        )


                        # ====================================
                        # MATCH STATUS / TAGS
                        # ====================================

                        # These flags come directly from the recommendation
                        # engine. Exact-result cards are 8/8; partial matches
                        # are only possible after the user opens alternatives.
                        sunlight_match = bool(
                            row.get("sunlight_match", False)
                        )

                        water_match = bool(
                            row.get("water_match", False)
                        )

                        pollinator_match = bool(
                            row.get("pollinator_match", False)
                        )

                        match_score = int(
                            row.get("match_score", 0)
                        )

                        if match_score == 8:
                            match_label = "Excellent match"
                        elif match_score >= 6:
                            match_label = "Strong match"
                        elif match_score >= 3:
                            match_label = "Partial match"
                        else:
                            match_label = "Native alternative"

                        sunlight_class = (
                            "match" if sunlight_match else "no-match"
                        )

                        water_class = (
                            "match" if water_match else "no-match"
                        )

                        sunlight_mark = "✓" if sunlight_match else "✕"
                        water_mark = "✓" if water_match else "✕"

                        if (
                            pollinator
                            == "🌱 Any / No Preference"
                        ):
                            pollinator_tag = (
                                '<span class="tag match">'
                                '🌱 Any pollinator'
                                '</span>'
                            )
                        else:
                            pollinator_class = (
                                "match"
                                if pollinator_match
                                else "no-match"
                            )
                            pollinator_mark = (
                                "✓"
                                if pollinator_match
                                else "✕"
                            )
                            pollinator_tag = (
                                f'<span class="tag {pollinator_class}">'
                                f'{pollinator} {pollinator_mark}'
                                '</span>'
                            )

                        st.markdown(
                            f"""
<div class="match-score">
{match_label} · {match_score}/8
</div>

<div class="tag-row">

<span class="tag {sunlight_class}">
☀️ {sunlight} {sunlight_mark}
</span>

<span class="tag {water_class}">
💧 {water} {water_mark}
</span>

{pollinator_tag}

</div>
""",
                            unsafe_allow_html=True,
                        )


                        # ====================================
                        # QUICK INFO
                        # ====================================

                        bloom = (
                            get_bloom_months(
                                row
                            )
                        )


                        maintenance = clean(
                            row.get(
                                "maintenance"
                            )
                        )


                        moisture = clean(
                            row.get(
                                "soil_moisture"
                            )
                        )


                        st.markdown(
                            f"""
<div class="plant-info">

🌸 <strong>Bloom:</strong>
{bloom}
<br>

🛠 <strong>Maintenance:</strong>
{maintenance}
<br>

💧 <strong>Moisture:</strong>
{moisture}

</div>
""",
                            unsafe_allow_html=True,
                        )


                        # ====================================
                        # WHY THIS PLANT
                        # ====================================

                        matched_conditions = []
                        unmatched_conditions = []

                        if sunlight_match:
                            matched_conditions.append(
                                sunlight.lower()
                            )
                        else:
                            unmatched_conditions.append(
                                sunlight.lower()
                            )

                        if water_match:
                            matched_conditions.append(
                                water.lower()
                            )
                        else:
                            unmatched_conditions.append(
                                water.lower()
                            )

                        if pollinator != "🌱 Any / No Preference":
                            if pollinator_match:
                                matched_conditions.append(
                                    f"your {pollinator.lower()} preference"
                                )
                            else:
                                unmatched_conditions.append(
                                    f"your {pollinator.lower()} preference"
                                )

                        if matched_conditions:
                            matched_text = (
                                ", ".join(matched_conditions)
                            )
                        else:
                            matched_text = "none of the selected conditions"

                        if unmatched_conditions:
                            unmatched_text = (
                                ", ".join(unmatched_conditions)
                            )
                            explanation = (
                                f"Native to {state} and matches "
                                f"{matched_text}. It does not specifically "
                                f"match {unmatched_text}, so it is shown "
                                f"as a native alternative."
                            )
                        else:
                            explanation = (
                                f"Native to {state} and matches "
                                f"{matched_text}."
                            )

                        st.markdown(
                            f"""
<div class="match-box">

<div class="match-title">
Why this plant?
</div>

{explanation}

</div>
""",
                            unsafe_allow_html=True,
                        )


                        # ====================================
                        # DETAILS
                        # ====================================

                        with st.expander(
                            "View plant details"
                        ):

                            st.markdown(
                                f"""
**Family:** {clean(
    row.get("plant_family")
)}

**Plant type:** {clean(
    row.get("plant_type")
)}

**Hardiness zones:** {clean(
    row.get("zone_min")
)} – {clean(
    row.get("zone_max")
)}

**Soil:** {clean(
    row.get("soil_description")
)}

**Soil pH:** {clean(
    row.get("soil_ph")
)}

**Bloom color:** {clean(
    row.get("bloom_color")
)}
"""
                            )


                        # ====================================
                        # SOURCE
                        # ====================================

                        source = row.get(
                            "image_source"
                        )


                        if pd.notna(source):

                            st.markdown(
                                f"""
<div class="source">
Image source: {source}
</div>
""",
                                unsafe_allow_html=True,
                            )


                        # ====================================
                        # CARD END
                        # ====================================

                        st.markdown(
                            "</div>",
                            unsafe_allow_html=True,
                        )


                # Space between rows

                st.markdown(
                    "<div style='height:1.5rem'></div>",
                    unsafe_allow_html=True,
                )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
<div class="footer">

<strong>
Biodiversity & Native Planting Planner
</strong>

<br>

Vanguard Strategists ·
Grow with Google BUILD Stage ·
UN SDG 15: Life on Land

</div>
""",
    unsafe_allow_html=True,
)
