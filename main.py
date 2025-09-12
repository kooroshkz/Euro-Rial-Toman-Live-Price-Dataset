#!/usr/bin/env python3
"""
Euro Scraper - Main Entry Point

A professional tool for scraping EUR to IRR exchange rate historical data
from tgju.org with automatic pagination and incremental updates.

Author: Koorosh Komeili Zadeh
"""

import sys
import os

# Add src directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.scraper import EuroScraper
from src.utils import setup_logging


def main():
    """Main entry point for the euro scraper."""
    print("=" * 60)
    print("EUR/IRR Exchange Rate Scraper")
    print("=" * 60)
    print("Target: https://www.tgju.org/profile/price_eur/history")
    print("Output: data/Euro_Rial_Price_Dataset.csv")
    print("=" * 60)
    
    logger = setup_logging()
    
    try:
        # Initialize scraper
        scraper = EuroScraper()
        
        # Run the scraper
        print("\nStarting scraper...")
        success = scraper.run()
        
        if success:
            print("\nScraping completed successfully!")
            print("Check the 'data' folder for your CSV file.")
        else:
            print("\nScraping failed. Check the log file for details.")
            return 1
            
    except KeyboardInterrupt:
        print("\nScraping interrupted by user.")
        return 1
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        print(f"\nUnexpected error: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
