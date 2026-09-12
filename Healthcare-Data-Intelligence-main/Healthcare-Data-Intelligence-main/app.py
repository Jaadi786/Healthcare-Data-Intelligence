import streamlit as st

st.set_page_config(
    page_title="Healthcare Intelligence",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------------------------------------------------------------------------
# Sidebar branding (small logo + app name shown above the navigation list)
# ---------------------------------------------------------------------------
st.logo("assets/logo.svg", icon_image="assets/logo.svg")

# ---------------------------------------------------------------------------
# Explicit navigation: controls sidebar order, titles and icons directly,
# instead of relying on raw filenames (fixes the plain "app" label and lets
# us group Settings at the end).
# ---------------------------------------------------------------------------
home = st.Page("views/home.py", title="Home", icon="🏠", default=True)
risk = st.Page("pages/1_Patient_Risk.py", title="Patient Risk", icon="👤")
priority = st.Page("pages/2_Patient_Priority.py", title="Patient Priority", icon="🚨")
demand = st.Page("pages/3_Demand_Prediction.py", title="Demand Prediction", icon="📈")
resource = st.Page("pages/4_Resource_Allocation.py", title="Resource Allocation", icon="🛏️")
analytics = st.Page("pages/5_Analytics.py", title="Analytics", icon="📊")
settings = st.Page("pages/6_Settings.py", title="Settings", icon="⚙️")

pg = st.navigation(
    {
        "Overview": [home],
        "Modules": [risk, priority, demand, resource, analytics],
        "": [settings],
    }
)
pg.run()
