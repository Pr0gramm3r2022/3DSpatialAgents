import streamlit as st
import time # Used to simulate the agent's work time

# --- Configuration and Title ---
st.set_page_config(
    page_title="Gemini Spatial Reasoning Agent",
    layout="wide"
)

st.title("🛰️ Spatial Reasoning Agent for Wearables")
st.caption("Multimodal Analysis using Gemini Robotics-ER 1.5 and Multi-Agent Architecture")

# --- Agent Interaction Form ---
with st.form("agent_form"):
    # 1. User Goal (Text Input for Planner Agent)
    analysis_goal = st.text_area(
        "📝 **1. Define Your Spatial Analysis Goal** (e.g., 'Find the best location for a new traffic sensor' or 'Verify that all safety checks are completed for the yellow valve.')",
        height=150,
        placeholder="Enter your detailed request here..."
    )

    # 2. File Upload (Image/Video Input for Analyzer Agent)
    uploaded_file = st.file_uploader(
        "📹 **2. Upload Image or Video Data** (The live feed context)",
        type=["jpg", "jpeg", "png", "mp4", "mov"],
        accept_multiple_files=False
    )

    # 3. Optional Parameters (Simulating other API inputs)
    col1, col2 = st.columns(2)
    with col1:
        dataset_type = st.selectbox(
            "Select Data Type:",
            options=["Infrastructure Photo", "Maintenance Video", "GeoJSON Context"],
            index=1
        )
    with col2:
        max_duration = st.number_input(
            "Max Video Analysis Duration (sec):",
            min_value=1,
            max_value=60,
            value=10
        )

    # Submission Button
    submitted = st.form_submit_button("🚀 Run Multi-Agent Analysis")

# --- Agent Processing Logic ---
if submitted:
    if not analysis_goal or not uploaded_file:
        st.error("Please provide both an **Analysis Goal** and **upload a file** to proceed.")
    else:
        # --- PHASE 1: Planner Agent (Input Sanitization & Planning) ---
        st.info("🤖 **Planner Agent** is executing (Input Sanitization & Plan Generation)...")
        st.markdown(f"> **Goal Received:** *{analysis_goal[:50]}...*")

        # Simulate security check (Planner Agent's role)
        if "delete database" in analysis_goal.lower():
             st.error("🚨 **SECURITY ALERT:** Prompt Injection detected! Aborting request.")
        else:
            with st.spinner("Analyzing plan complexity..."):
                time.sleep(1.5) # Simulate latency
            
            # --- PHASE 2: Analyzer Agent (Execution & Data Synthesis) ---
            st.success("✅ Planner Agent complete. Passing execution to **Analyzer Agent**.")
            st.subheader("Analyzer Agent Output (The Raw Data)")

            # Display the uploaded file
            st.image(uploaded_file, caption=uploaded_file.name, use_column_width=True)

            with st.spinner(f"Analyzing {uploaded_file.name} for spatial context using Gemini Robotics-ER 1.5..."):
                time.sleep(4) # Simulate complex model inference time

            # Simulating structured output (The Analyzer's output)
            raw_analysis_data = {
                "object_id": "VALVE-4C",
                "location_3d": [1.5, 0.8, 2.1],
                "confidence": 0.98,
                "required_action": "Tighten 1/4 turn",
                "time_observed": time.strftime("%H:%M:%S")
            }
            st.json(raw_analysis_data)
            
            # --- PHASE 3: Presenter Agent (Formatting & Final Insight) ---
            st.success("✅ Analyzer Agent complete. Passing raw data to **Presenter Agent**.")
            
            # The Presenter Agent converts the JSON/Dict into a simple, actionable insight
            final_insight = (
                f"**Final Insight for Wearable Display:** Target object **VALVE-4C** located **1.5 meters ahead, 0.8 meters left, and 2.1 meters up**. "
                f"The required next step is: **{raw_analysis_data['required_action']}**."
            )

            st.markdown("---")
            st.subheader("💡 **Final Actionable Insight** (Presenter Output)")
            st.markdown(f"### {final_insight}")