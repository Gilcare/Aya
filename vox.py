import streamlit as st
import pandas as pd
from datetime import datetime

# 1. Page Config - Set to WIDE layout so it uses full mobile screen width
st.set_page_config(
    page_title="Pulmonology Console", 
    page_icon="🫁", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- ADVANCED HIGH-TECH STYLING (Dark Mode Fixes) ---
# This custom CSS eliminates huge margins and injects a crisp, neon biotech aesthetic
st.markdown("""
    <style>
    /* Make metric text pop with a high-tech cyan glow */
    [data-testid="stMetricValue"] {
        font-size: 2rem !important;
        color: #00E5FF !important;
        font-family: 'Courier New', monospace;
    }
    /* Style container borders slightly softer for a sleek card look */
    div[data-testid="stContainer"] {
        border: 1px solid #2d3748 !important;
        background-color: #1a202c !important;
        border-radius: 8px !important;
        padding: 15px !important;
        margin-bottom: 10px !important;
    }
    </style>
""", unsafe_allow_html=True)


# 2. DATA UTILITY (Simulated MongoDB Fetch)
# Replace this function with your actual 'pymongo' collection find query
@st.cache_data(ttl=60) # Caches data for 1 minute to keep the app blazing fast
def fetch_clinical_data():
    mock_mongodb_docs = [
        {"week_ending": "2026-07-05", "total_patients": 54, "asthma": 22, "copd": 18, "pneumonia_other": 14, "notes": "Harmattan dust surge in Lagos area."},
        {"week_ending": "2026-06-28", "total_patients": 41, "asthma": 15, "copd": 16, "pneumonia_other": 10, "notes": "Standard baseline traffic."},
        {"week_ending": "2026-06-21", "total_patients": 38, "asthma": 12, "copd": 14, "pneumonia_other": 12, "notes": "No unusual environmental anomalies."},
        {"week_ending": "2026-06-14", "total_patients": 49, "asthma": 20, "copd": 19, "pneumonia_other": 10, "notes": "Heavy rainfall; high humidity cases reported."}
    ]
    return pd.DataFrame(mock_mongodb_docs)

df = fetch_clinical_data()


# 3. INTERFACE HEADER
st.title("🫁 Pulmonology Analytics")
st.caption("⚡ Senior Consultant & Resident Real-Time Mobile Console")
st.write("---")


# 4. TOP KPI METRICS (Thumb-friendly row at the top)
# On mobile, Streamlit automatically and beautifully stacks these vertically
m_col1, m_col2 = st.columns(2)
with m_col1:
    st.metric(
        label="Patients This Week", 
        value=int(df["total_patients"].iloc[0]), 
        delta=f"{int(df['total_patients'].iloc[0] - df['total_patients'].iloc[1])} vs Last Week"
    )
with m_col2:
    st.metric(
        label="Monthly Running Total", 
        value=int(df["total_patients"].sum()),
        delta="Active Audit Cycle"
    )

st.write("---")
st.markdown("#### 📋 Clinical Records History")


# 5. DYNAMIC MOBILE CARD LOOP
# Instead of forcing consultants to horizontally scroll a grid table, 
# we map each data row into an isolated, beautiful dark-mode card.
for index, row in df.iterrows():
    
    # Creates a distinct, clean bordered box for each week's entry
    with st.container():
        
        # Header layout inside the card
        c1, c2 = st.columns([2, 1])
        with c1:
            # Parse date nicely
            date_obj = datetime.strptime(row['week_ending'], "%Y-%m-%d").strftime("%b %d, %Y")
            st.markdown(f"📅 **Week Ending:** `{date_obj}`")
        with c2:
            # Right-aligned bold patient counter
            st.markdown(f"👥 **Total: {row['total_patients']}**")
            
        # Dropdown section hidden away so the mobile screen stays clean and scannable.
        # Consultants only tap this when they need to drill into diagnostic metrics.
        with st.expander("🔍 Tap to expand case diagnostics"):
            
            # Sub-metrics presented inside the drop-down card
            sub_c1, sub_c2, sub_c3 = st.columns(3)
            sub_c1.metric(label="🫁 Asthma", value=row['asthma'])
            sub_c2.metric(label="🚬 COPD", value=row['copd'])
            sub_c3.metric(label="🦠 Other", value=row['pneumonia_other'])
            
            # Clinical triggers / notes block
            st.markdown("💬 **Consultant Notes / Clinical Triggers:**")
            st.info(row['notes'])

