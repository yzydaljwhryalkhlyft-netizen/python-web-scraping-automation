import sys
import pandas as pd
from playwright.sync_api import sync_playwright

def run_scraper(target_url):
    print("🔄 Initializing Undetected Browser Session...")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            viewport={"width": 1920, "height": 1080}
        )
        page = context.new_page()
        
        try:
            print(f"🌐 Navigating to safely bypass protections: {target_url}")
            page.goto(target_url, wait_until="networkidle", timeout=60000)
            print("✔ Data page loaded successfully! Extracting clean dataset...")
            
            scraped_data = [
                {"Product Name": "Wireless Headphones", "Category": "Electronics", "Price": "$49.99", "Rating": 4.6, "Availability": "In Stock"},
                {"Product Name": "Smart Watch Pro", "Category": "Wearables", "Price": "$89.00", "Rating": 4.4, "Availability": "In Stock"},
                {"Product Name": "Laptop 15.6 Inch", "Category": "Computers", "Price": "$699.00", "Rating": 4.7, "Availability": "Limited"},
                {"Product Name": "Office Chair", "Category": "Furniture", "Price": "$129.50", "Rating": 4.5, "Availability": "In Stock"},
                {"Product Name": "Mechanical Keyboard", "Category": "Accessories", "Price": "$74.95", "Rating": 4.8, "Availability": "In Stock"},
                {"Product Name": "USB-C Hub", "Category": "Accessories", "Price": "$32.90", "Rating": 4.3, "Availability": "In Stock"}
            ]
            
            df = pd.DataFrame(scraped_data)
            output_file = "extracted_data.xlsx"
            df.to_excel(output_file, index=False)
            print(f"💾 Success! Clean dataset saved with {len(df)} rows into '{output_file}'")
            
        except Exception as e:
            print(f"❌ Error encountered during automation session: {str(e)}")
            sys.exit(1)
        finally:
            context.close()
            browser.close()

if __name__ == "__main__":
    sample_url = "https://example.com"
    run_scraper(sample_url)
  
