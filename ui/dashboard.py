import streamlit as st


def show_dashboard(score):

    st.subheader("🎯 ATS Dashboard")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("ATS Score", f"{score}%")

        st.progress(score / 100)

    with col2:

        if score >= 90:
            st.success("Outstanding Match 🟢")

        elif score >= 80:
            st.success("Excellent Match ✅")

        elif score >= 70:
            st.warning("Good Match 🟡")

        elif score >= 50:
            st.warning("Average Match ⚠️")

        else:
            st.error("Needs Improvement 🔴")