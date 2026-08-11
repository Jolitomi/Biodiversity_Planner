How to test this locally:
1. Pull down the latest branch:
git fetch origin
git checkout feature/backend-engine

2. Install the required dependencies:
Make sure you have both Streamlit and Pandas installed in your environment:
pip install streamlit pandas

3. Run the web application:
You must run this from the absolute root of the repository (Biodiversity_Planner/) so the relative file paths to the data/processed/ folder map correctly:

streamlit run app/app.py
The application will automatically open in your default web browser (typically at http://localhost:8501).