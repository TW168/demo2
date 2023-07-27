import streamlit as st



tab1, tab2 = st.tabs(["Tab1", "Tab2"])
with tab1:
    st.header("Tab 1")
with tab2:
    st.header("Tab 2")