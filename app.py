import streamlit as st
import google.generativeai as genai
from PIL import Image
import os
from dotenv import load_dotenv
import random
import time

# Load environment variables
load_dotenv()

# Configure page
st.set_page_config(
    page_title="Eco-Receipt Analyzer",
    page_icon="🌱",
    layout="wide"
)

# System Prompt
SYSTEM_PROMPT = """
Role 
You are an environmental impact analysis assistant. You analyze a user-uploaded image of a retail receipt and estimate the carbon footprint of the purchased items. 
... (rest of prompt implied by context, but for mock we don't need it sent)
"""

def get_mock_response():
    """Generates a realistic mock response for demo purposes."""
    scenarios = [
        {
            "total": 14.2,
            "confidence": "Medium",
            "items": [
                ("Organic Bananas (1 bunch)", "Produce", 0.8, "0.6-1.0", "High", "Imported fruit transport emissions"),
                ("Grass-Fed Ground Beef (1lb)", "Meat & seafood", 12.5, "10.0-15.0", "High", "High methane production from cattle"),
                ("Almond Milk (1L)", "Dairy & eggs", 0.9, "0.7-1.1", "Medium", "Water usage high, but lower CO2 than dairy"),
            ],
            "insights": [
                "**Beef is the biggest contributor**: Red meat has a very high carbon footprint compared to other proteins.",
                "**Choose local fruit**: Imported bananas have higher transport emissions than local seasonal fruit.",
                "**Alternative**: Consider swapping beef for chicken or plant-based meat to reduce emissions by up to 80%."
            ]
        },
        {
            "total": 8.5,
            "confidence": "High",
            "items": [
                ("Chicken Breast (500g)", "Meat & seafood", 3.5, "3.0-4.0", "High", "Poultry has lower emissions than red meat"),
                ("Cheddar Cheese (200g)", "Dairy & eggs", 2.8, "2.2-3.4", "Medium", "Dairy processing and cattle emissions"),
                ("Soda Can (12 pack)", "Beverages", 2.2, "1.8-2.6", "High", "Aluminum packaging and processing"),
            ],
            "insights": [
                "**Dairy impact**: Cheese production is resource-intensive.",
                "**Packaging matters**: Aluminum is recyclable, but production is energy-heavy.",
                "**Tip**: Buying in bulk or larger containers can sometimes reduce packaging waste per unit."
            ]
        }
    ]
    
    scenario = random.choice(scenarios)
    
    markdown_output = f"""
### Summary 
- **Total estimated carbon footprint**: {scenario['total']} kg CO₂e 
- **Overall confidence level**: {scenario['confidence']}

### Item Breakdown 
| Item Name | Category | Est. CO₂e (kg) | Range | Confidence | Assumptions |
| :--- | :--- | :--- | :--- | :--- | :--- |
"""
    
    for item in scenario['items']:
        markdown_output += f"| {item[0]} | {item[1]} | {item[2]} | {item[3]} | {item[4]} | {item[5]} |\n"

    markdown_output += "\n### Insights\n"
    for insight in scenario['insights']:
        markdown_output += f"- {insight}\n"
        
    markdown_output += "\n\n*(Note: This is a simulated result for demonstration purposes)*"
    
    return markdown_output

def analyze_receipt(image, api_key):
    # Simulation Mode (No Key)
    if not api_key:
        time.sleep(2) # Simulate processing time
        return get_mock_response()

    # Real Analysis Mode
    try:
        genai.configure(api_key=api_key)
        # Use Gemini 1.5 Flash for speed and cost, or Pro for better reasoning
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        with st.spinner("Analyzing receipt..."):
            response = model.generate_content([SYSTEM_PROMPT, image])
            return response.text
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    st.title("🌱 Eco-Receipt Analyzer")
    st.markdown("Upload a receipt to estimate the carbon footprint of your purchases.")

    # Sidebar for API Key
    with st.sidebar:
        st.header("Settings")
        api_key = st.text_input("Google Gemini API Key", type="password", value=os.getenv("GOOGLE_API_KEY") or "")
        st.markdown("[Get an API Key](https://aistudio.google.com/app/apikey)")
        
        if not api_key:
            st.warning("⚠️ No API Key detected. App will run in **Demo Mode** with simulated data.")
        else:
            st.success("✅ API Key loaded. Ready for real analysis.")
        
        st.info("This tool uses AI to estimate carbon emissions. Results are estimates only.")

    # Main Content
    uploaded_file = st.file_uploader("Choose a receipt image", type=['png', 'jpg', 'jpeg', 'webp'])

    if uploaded_file is not None:
        col1, col2 = st.columns([1, 2])
        
        with col1:
            image = Image.open(uploaded_file)
            st.image(image, caption='Uploaded Receipt', use_container_width=True)
            
        with col2:
            if st.button("Analyze Carbon Footprint", type="primary"):
                if not api_key:
                    st.info("Running in **Demo Mode** (Simulated Analysis)...")
                
                result = analyze_receipt(image, api_key)
                st.markdown(result)

if __name__ == "__main__":
    main()
