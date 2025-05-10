
import streamlit as st
import pandas as pd
import numpy as np
import random
import datetime
from PIL import Image
from ultralytics import YOLO

# Page config
st.set_page_config(
    page_title="🍉 Welcome to Fruit Quality Assistant",
    layout="centered"
)

st.title("🍇 Fruit Quality Control Assistant")
st.markdown("#### 🍏 Making fruit management smarter, fresher, and juicier!")

# Intro section
st.markdown("""
---

Welcome to our intelligent **Fruit Quality Control Dashboard** — an all-in-one tool designed for **supermarkets**, **suppliers**, and **individual users** to ensure the highest standards of freshness.

### 🍽️ Features of the Dashboard

- **📊 Real-time Quality Overview**  
  Visualize fruit conditions: *Fresh*, *Ripe*, or *Spoiled* with image classification and stats.

- **📄 Detailed Reports**  
  Generate summaries and analytics of fruit conditions across batches.

- **🚛 Supplier Insights**  
  Track which suppliers deliver the best quality and when.

- **⏳ Shelf Life Estimation**  
  Predict days until ripening or spoilage using smart modeling.

---
""")

# SDGs Goals Section
st.markdown("## 🌱 Sustainability Goals We Support")
st.markdown("""
Our mission aligns with the United Nations Sustainable Development Goals (SDGs). Here's how our system contributes to a better world:
""")

def goal_card(img_path, title, desc):
    col1, col2 = st.columns([1, 4])
    with col1:
        st.image(img_path, width=80)
    with col2:
        st.markdown(f"**{title}**")
        st.markdown(desc)
    st.markdown("---")

goal_card(
    "./Images/TheGlobalGoals_Icons_Color_Goal_2.png",
    "Goal 2: Zero Hunger",
    "Our system reduces food waste by detecting spoilage early, ensuring more fruit reaches those who need it most."
)

goal_card(
    "./Images/TheGlobalGoals_Icons_Color_Goal_9.png",
    "Goal 9: Industry, Innovation, and Infrastructure",
    "By leveraging AI, we're modernizing agricultural practices for smarter sorting and inspection."
)

goal_card(
    "./Images/TheGlobalGoals_Icons_Color_Goal_12.png",
    "Goal 12: Responsible Consumption and Production",
    "We minimize post-harvest loss through smart detection, enabling sustainable and efficient distribution."
)

st.success("Use the sidebar to explore reports, suppliers, and shelf life tools ➡️")
