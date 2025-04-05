# --- START OF FILE __init__.py ---

# Import the node class
from .bs_textchop import TextExtractBetween

# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "BSTextChop": TextExtractBetween
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "BSTextChop": "BS Textchop"
}

# Optional: Add a version string
__version__ = '1.0.0'

# Optional: A web directory mapping if the node needs to serve web files
# WEB_DIRECTORY = "./js" # Example if you had javascript files

print("------------------------------------------")
print("ComfyUI-BS-Textchop: Loaded")
print("------------------------------------------")


# --- END OF FILE __init__.py ---