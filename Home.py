import streamlit as st
import pandas as pd
import numpy as np
import random
import datetime


# Sidebar navigation
# pages = ["Dashboard", "Reports", "Supplier Insights", "Fruit Shelf Life"]
# page = st.sidebar.selectbox("Select a page", pages)

# Random Data Generators
def generate_fruit_data():
    fruit_types = ["🍎 Apple", "🍌 Banana", "🍊 Orange", "🥭 Mango", "🍑 Peach"]
    quality = ["Fresh", "Ripe", "Spoiled"]
    data = {
        "Fruit": [random.choice(fruit_types) for _ in range(100)],
        "Quality": [random.choice(quality) for _ in range(100)],
        "Tested At": [datetime.datetime.now() - datetime.timedelta(minutes=random.randint(0, 1000)) for _ in range(100)]
    }
    return pd.DataFrame(data)

def generate_supplier_data():
    suppliers = ["FarmFresh Co.", "Nature's Best", "Tropical Imports", "Green Valley"]
    fruit_types = ["🍎 Apple", "🍌 Banana", "🍊 Orange", "🥭 Mango", "🍑 Peach"]
    data = {
        "Supplier": [random.choice(suppliers) for _ in range(50)],
        "Fruit": [random.choice(fruit_types) for _ in range(50)],
        "Quality Score": [random.randint(60, 100) for _ in range(50)],
        "Shipment Date": [datetime.date.today() - datetime.timedelta(days=random.randint(0, 15)) for _ in range(50)]
    }
    return pd.DataFrame(data)

def generate_ripeness_prediction():
    fruit_types = ["🍎 Apple", "🍌 Banana", "🍊 Orange", "🥭 Mango", "🍑 Peach"]
    days_to_spoil = [random.randint(1, 7) for _ in fruit_types]
    return pd.DataFrame({
        "Fruit": fruit_types,
        "Days to Ripen": [random.randint(0, 3) for _ in fruit_types],
        "Days to Spoil": days_to_spoil
    })

st.set_page_config(
    page_title="🍉 Welcome to Fruit Quality Assistant",
    layout="centered"
)

st.title("🍇 Fruit Quality Control Assistant")
st.markdown("#### 🍏 Making fruit management smarter, fresher, and juicier!")


st.markdown("""
Welcome to our intelligent fruit quality control dashboard — an all-in-one tool designed to assist **supermarkets**, **suppliers**, and even **individual users**!

---

### 🍽️ What You Can Explore:

- **📊 Dashboard:**  
  Real-time visual overview of tested fruits and their quality (Fresh, Ripe, Spoiled).

- **📄 Reports:**  
  Auto-generated detailed reports for quality analysis and decision making.

- **🚛 Supplier Insights:**  
  Understand which suppliers are delivering the freshest fruits.

- **⏳ Fruit Shelf Life:**  
  Estimate when your fruit will ripen or spoil using fun visuals.

---

### 🤖 Future LLM Features (Showcase)

We're integrating smart language capabilities! Here's a **preview chatbot** that helps answer fruit-related questions:

""")

# Simple LLM-style mock chatbot widget
user_question = st.text_input("Ask me anything about your fruit 🍌", placeholder="e.g., When will my banana go bad?")
if user_question:
    fake_answers = [
        "Based on average shelf life, your banana might spoil in 2–3 days.",
        "If your fruit has brown spots and smells fermented, it’s probably past its prime.",
        "You can store it in the fridge to extend freshness!",
        "Try turning your overripe fruit into a smoothie or jam. 🍓",
        "That mango sounds ready to eat — enjoy it before tomorrow!"
    ]
    st.info(f"🤖 Assistant: {random.choice(fake_answers)}")

st.markdown("---")
st.success("Use the sidebar to explore the features ➡️")
