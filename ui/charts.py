import matplotlib.pyplot as plt
import streamlit as st


def show_skill_chart(matched, missing):

    st.subheader("📊 Skills Match Overview")

    if len(matched) + len(missing) == 0:
        st.info("No skills available.")
        return

    fig, ax = plt.subplots(figsize=(5, 5))

    ax.pie(
        [len(matched), len(missing)],
        labels=["Matched", "Missing"],
        autopct="%1.1f%%",
        startangle=90
    )

    ax.axis("equal")

    st.pyplot(fig)