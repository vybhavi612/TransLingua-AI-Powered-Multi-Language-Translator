"""
Run script for TransLingua application
"""

import streamlit.web.cli as stcli
import sys
import os

def main():
    """Main function to run the Streamlit app"""
    # Set the current directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # Run the Streamlit app
    sys.argv = ["streamlit", "run", "app.py"]
    sys.exit(stcli.main())

if __name__ == "__main__":
    main()
