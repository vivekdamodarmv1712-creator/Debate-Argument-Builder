import streamlit as st
from datetime import datetime

from debate_argument_builder.crew import DebateArgumentBuilder


# ---------------- UI CONFIG ---------------- #
st.set_page_config(
    page_title="AI Debate Argument Builder",
    page_icon="⚖️",
    layout="wide"
)


def main():

    st.title("⚖️ AI Debate Argument Builder")
    st.caption("Generate strong arguments, counterarguments, and rebuttals using AI agents.")

    # ---------------- SIDEBAR ---------------- #
    st.sidebar.header("📌 Debate Setup")

    topic = st.sidebar.text_input(
        "Enter Debate Topic",
        placeholder="e.g. Should AI be regulated?"
    )

    side = st.sidebar.selectbox(
        "Choose Your Side",
        ["for", "against"]
    )

    run_button = st.sidebar.button("🚀 Generate Debate Brief")

    # ---------------- MAIN ---------------- #
    if run_button:

        if not topic.strip():
            st.sidebar.error("⚠️ Please enter a debate topic.")
            return

        inputs = {
            "topic": topic,
            "side": side,
            "current_year": str(datetime.now().year)
        }

        with st.spinner("🤖 AI is building your debate brief..."):
            result = DebateArgumentBuilder().crew().kickoff(inputs=inputs)

        # Output mapping (based on your 3 tasks)
        try:
            arguments = result.tasks_output[0].raw
            counterarguments = result.tasks_output[1].raw
            rebuttals = result.tasks_output[2].raw
        except Exception:
            st.error("⚠️ Error reading crew output. Check task order in crew.py.")
            return

        st.success("✅ Debate Brief Generated!")

        # ---------------- TABS ---------------- #
        tab1, tab2, tab3 = st.tabs(
            ["🧠 Arguments", "⚔️ Counterarguments", "🔁 Rebuttals"]
        )

        with tab1:
            st.subheader("Arguments for your side")
            st.text_area("Arguments", arguments, height=400)

        with tab2:
            st.subheader("Opposition Arguments")
            st.text_area("Counterarguments", counterarguments, height=400)

        with tab3:
            st.subheader("Rebuttals")
            st.text_area("Rebuttals", rebuttals, height=400)

        # Download full brief
        full_text = f"""
DEBATE TOPIC: {topic}
SIDE: {side}

=== ARGUMENTS ===
{arguments}

=== COUNTERARGUMENTS ===
{counterarguments}

=== REBUTTALS ===
{rebuttals}
"""

        st.download_button(
            "⬇️ Download Debate Brief",
            full_text,
            file_name=f"debate_brief_{datetime.now().strftime('%Y%m%d_%H%M')}.txt"
        )

    else:
        st.info("👈 Enter a topic and select your side to generate a debate brief.")

        st.markdown("""
        ### ✨ What this app does:
        - Generates 4 strong arguments
        - Predicts opponent counterarguments
        - Writes powerful rebuttals
        - Creates a complete debate brief

        ### 🚀 How to use:
        1. Enter topic
        2. Choose side (for/against)
        3. Click Generate
        """)


if __name__ == "__main__":
    main()