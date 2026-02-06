# Eco-Receipt Analyzer

An AI-powered tool that analyzes retail receipts to estimate the carbon footprint of purchased items.

## Features
- **Receipt Parsing**: Extracts items, prices, and dates from receipt images.
- **Categorization**: Automatically categorizes items (e.g., Meat, Produce, Household).
- **Carbon Estimation**: Estimates CO₂e emissions for each item.
- **Insights**: Provides actionable tips to reduce your footprint.

## Setup

1. **Install Python**: Ensure you have Python installed.
2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **API Key**:
   - Get a free Google Gemini API key from [Google AI Studio](https://aistudio.google.com/app/apikey).
   - You can enter it in the app sidebar or create a `.env` file:
     ```bash
     cp .env.example .env
     # Edit .env and add your key
     ```

## Running the App

```bash
streamlit run app.py
```

## How it Works
This application uses Google's Gemini Multimodal model to process receipt images and apply environmental impact data logic to generate estimates.
