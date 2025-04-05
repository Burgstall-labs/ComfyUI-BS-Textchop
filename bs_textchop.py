# --- START OF FILE bs_textchop.py ---

import re

class TextExtractBetween:
    # Define a maximum number of pairs the node can handle
    MAX_PAIRS = 15

    @classmethod
    def INPUT_TYPES(s):
        inputs = {
            "required": {
                "text": ("STRING", {"default": "", "multiline": True, "forceInput": True}),
                "pair_count": ("INT", {"default": 1, "min": 1, "max": s.MAX_PAIRS, "step": 1}),
                # First pair is always required
                "start_marker_1": ("STRING", {"default": ""}),
                "end_marker_1": ("STRING", {"default": ""}),
            },
            "optional": {}
        }
        # Add subsequent pairs as optional inputs up to MAX_PAIRS
        for i in range(2, s.MAX_PAIRS + 1):
            inputs["optional"][f"start_marker_{i}"] = ("STRING", {"default": ""})
            inputs["optional"][f"end_marker_{i}"] = ("STRING", {"default": ""})

        return inputs

    # Define return types and names dynamically based on MAX_PAIRS
    RETURN_TYPES = tuple(["STRING"] * MAX_PAIRS)
    RETURN_NAMES = tuple([f"extracted_text_{i}" for i in range(1, MAX_PAIRS + 1)])

    FUNCTION = "extract"
    # Updated Category
    CATEGORY = "BS-Nodes/Text"
    OUTPUT_NODE = True

    def extract(self, text, pair_count, **kwargs):
        """
        Extracts text segments based on start and end markers.

        Args:
            text (str): The main input text.
            pair_count (int): The number of marker pairs to process.
            **kwargs: Contains start_marker_i and end_marker_i values.

        Returns:
            tuple: A tuple containing the extracted text for each pair,
                   padded with empty strings up to MAX_PAIRS.
        """
        results = []

        for i in range(1, pair_count + 1):
            start_key = f"start_marker_{i}"
            end_key = f"end_marker_{i}"

            # Retrieve markers for the current pair using kwargs.get for safety
            start_marker = kwargs.get(start_key, "")
            end_marker = kwargs.get(end_key, "")

            extracted_text = "" # Default value if not found or markers are empty

            # Only proceed if both markers are non-empty and text exists
            if text and start_marker:
                # Find the first occurrence of the start marker
                start_pos = text.find(start_marker)

                if start_pos != -1:
                    # Define the position to start searching for the end marker
                    search_start_pos = start_pos + len(start_marker)

                    # Find the first occurrence of the end marker *after* the start marker
                    # Only proceed if end_marker is also non-empty
                    if end_marker:
                        end_pos = text.find(end_marker, search_start_pos)

                        if end_pos != -1:
                            # Extract the text between the markers
                            extracted_text = text[search_start_pos:end_pos]
                    # Handle case where end_marker is empty: returns ""

            results.append(extracted_text)

        # Pad the results list with empty strings if pair_count < MAX_PAIRS
        while len(results) < self.MAX_PAIRS:
            results.append("")

        # Return the results as a tuple
        return tuple(results)

# --- END OF FILE bs_textchop.py ---
