import streamlit as st
import pandas as pd

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="UK Music Market Analysis",
    layout="wide"
)

# ================= LOAD DATA =================
df = pd.read_csv("Atlantic_United_Kingdom.csv")

# ================= TITLE =================
st.title("🎵 UK Top 50 Playlist Analysis Dashboard")
st.write("Insights of UK music market structure")

# ================= SIDEBAR FILTER =================
st.sidebar.header("Filters")

artist_search = st.sidebar.text_input("Search Artist")

df_filtered = df.copy()

if artist_search:
    df_filtered = df_filtered[
        df_filtered['artist'].str.contains(artist_search, case=False, na=False)
    ]

# ================= KPI METRICS =================
unique_artists = df_filtered['artist'].nunique()
explicit_share = round(df_filtered['is_explicit'].mean() * 100, 2)

st.markdown("## 📊 Overview")

col1, col2, col3 = st.columns(3)

col1.metric("Unique Artists", unique_artists)
col2.metric("Explicit Share %", explicit_share)
col3.metric("Total Songs", len(df_filtered))

st.success("Analyzing UK music trends with filters and KPIs.")

# ================= ARTIST ANALYSIS =================
st.markdown("## 🎤 Artist Analysis")

top_artists = df_filtered['artist'].value_counts().head(10)
st.bar_chart(top_artists)

# ================= CONTENT ANALYSIS =================
st.markdown("## 🔥 Content Analysis")

st.bar_chart(df_filtered['is_explicit'].value_counts())

# ================= ALBUM TYPE =================
st.subheader("💿 Album Type Distribution")

st.bar_chart(df_filtered['album_type'].value_counts())

# ================= COLLABORATION =================
st.subheader("🤝 Collaboration Analysis")

df_filtered['is_collab'] = df_filtered['artist'].astype(str).str.contains("&")

st.bar_chart(df_filtered['is_collab'].value_counts())

# ================= DURATION =================
st.subheader("⏱ Song Duration Analysis")

df_filtered['duration_min'] = df_filtered['duration_ms'] / 60000

st.bar_chart(df_filtered['duration_min'])

# ================= DATA PREVIEW =================
st.markdown("## 📁 Data Preview")

st.dataframe(df_filtered)