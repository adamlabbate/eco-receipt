import random
import time

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
    
    print(f"\n--- 🧾 ECO-RECEIPT ANALYSIS (DEMO) ---\n")
    print(f"SUMMARY")
    print(f"Total Carbon Footprint: {scenario['total']} kg CO2e")
    print(f"Confidence Level:       {scenario['confidence']}")
    print(f"\nITEM BREAKDOWN")
    print(f"{'Item':<30} | {'Category':<15} | {'CO2e (kg)':<10}")
    print("-" * 65)
    
    for item in scenario['items']:
        print(f"{item[0]:<30} | {item[1]:<15} | {item[2]:<10}")

    print(f"\nINSIGHTS")
    for insight in scenario['insights']:
        print(f"- {insight.replace('**', '')}")
        
    print(f"\n---------------------------------------")

if __name__ == "__main__":
    print("Initializing Demo Mode...")
    time.sleep(1)
    get_mock_response()
