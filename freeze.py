from flask_frozen import Freezer
from app import app
import os

# Configure Freezer
app.config['FREEZER_RELATIVE_URLS'] = True
app.config['FREEZER_DESTINATION'] = '.'  # Output to current directory to overwrite root index.html
app.config['FREEZER_REMOVE_EXTRA_FILES'] = False 

freezer = Freezer(app)

if __name__ == '__main__':
    try:
        freezer.freeze()
        print("Static site generated successfully.")
    except Exception as e:
        print(f"Error freezing: {e}")
