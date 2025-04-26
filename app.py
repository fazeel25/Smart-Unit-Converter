import streamlit as st

# Set up page configuration for better UI
st.set_page_config(page_title="Unit Master – Convert Anything", layout="wide")

# Custom title and description with emojis for better engagement
st.title("🔁 **Unit Master** – Smart Unit Converter")
st.markdown("Effortlessly convert between **Length**, **Weight**, **Temperature**, and **Volume**. Choose your units and let us do the math! 🤓")

# Unit categories to select from
categories = ["Length", "Weight", "Temperature", "Volume"]
selected_category = st.selectbox("Choose a category 📊", categories, key="category")

# Conversion logic function
def convert_units(category, value, from_unit, to_unit):
    try:
        if category == "Length":
            units = {"Meter": 1, "Kilometer": 1000, "Mile": 1609.34, "Inch": 0.0254}
        elif category == "Weight":
            units = {"Gram": 1, "Kilogram": 1000, "Pound": 453.592, "Ounce": 28.3495}
        elif category == "Volume":
            units = {"Milliliter": 1, "Liter": 1000, "Gallon": 3785.41}
        elif category == "Temperature":
            if from_unit == to_unit:
                return value
            if from_unit == "Celsius":
                return value * 9 / 5 + 32 if to_unit == "Fahrenheit" else value + 273.15
            elif from_unit == "Fahrenheit":
                return (value - 32) * 5 / 9 if to_unit == "Celsius" else ((value - 32) * 5 / 9) + 273.15
            elif from_unit == "Kelvin":
                return value - 273.15 if to_unit == "Celsius" else ((value - 273.15) * 9 / 5) + 32
        return value * units[from_unit] / units[to_unit]
    except Exception as e:
        st.error(f"Something went wrong: {e}")
        return None

# Units per category
unit_options = {
    "Length": ["Meter", "Kilometer", "Mile", "Inch"],
    "Weight": ["Gram", "Kilogram", "Pound", "Ounce"],
    "Volume": ["Milliliter", "Liter", "Gallon"],
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"]
}

# Inputs for value and unit selection
st.markdown("### 📝 Enter your values and units:")
value = st.number_input("Enter value to convert", min_value=0.0, format="%.4f")
from_unit = st.selectbox("From 🛑", unit_options[selected_category])
to_unit = st.selectbox("To 🚀", unit_options[selected_category])

# Conversion button with visual feedback
if st.button("Convert 🔄"):
    if value:
        result = convert_units(selected_category, value, from_unit, to_unit)
        if result is not None:
            st.success(f"✅ **Conversion Result**: {value} {from_unit} = {round(result, 4)} {to_unit}")
    else:
        st.error("❌ Please enter a valid value to convert!")

# Additional Features: Adding some fun with emojis and interactive feedback
st.markdown("---")
st.markdown("### 🌟 Tips for better use:")
st.markdown("""
- **Length**: Convert meters to miles or kilometers to inches with ease! 🌍
- **Weight**: Convert grams to pounds or ounces to kilograms! ⚖️
- **Temperature**: Switch between Celsius, Fahrenheit, and Kelvin with a breeze! 🌡️
- **Volume**: Convert milliliters to liters or gallons! 🏺
""")
