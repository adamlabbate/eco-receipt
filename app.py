import streamlit as st
import google.generativeai as genai
from PIL import Image
import os
from dotenv import load_dotenv

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

Core Tasks 
1. Parse the Receipt 
   - Extract store name, purchase date, line items (item name, quantity, price).
   - If text is ambiguous, make a reasonable inference and flag it.
   - If unreadable, explicitly say so.

2. Normalize & Categorize Items 
   - Convert abbreviated names to human-readable names.
   - Categories: Meat & seafood, Dairy & eggs, Produce, Packaged foods, Beverages, Household goods, Personal care, Unknown.

3. Estimate Carbon Footprint 
   - Estimate emissions in kg CO2e using average lifecycle data.
   - Include Production, Processing, Packaging, Transportation.
   - Use typical consumer averages if weight/quantity is missing.

4. Handle Uncertainty 
   - Provide Estimated CO2e (single value), Range (low-high), Confidence level (High/Medium/Low).

Output Format (Strict) 
Summary 
- Total estimated carbon footprint: X kg CO2e 
- Overall confidence level: High / Medium / Low 

Item Breakdown 
For each item: 
- Item name 
- Category 
- Estimated CO2e (kg) 
- Estimated range (kg CO2e) 
- Confidence level 
- Assumptions 

Insights 
- Identify highest-impact items. 
- Suggest up to 3 realistic alternatives/behavior changes.

Tone & Constraints 
- Neutral, informative, non-judgmental. 
- Do not claim exact accuracy. 
- Treat outputs as estimates.
"""

def analyze_receipt(image, api_key):
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
                    st.error("Please enter a Google Gemini API Key in the sidebar.")
                else:
                    result = analyze_receipt(image, api_key)
                    st.markdown(result)

if __name__ == "__main__":
    main()
