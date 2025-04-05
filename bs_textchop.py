# --- START OF FILE bs_textchop.py ---

import re

class TextExtractBetweenSmart: # Renamed class
    # Define a maximum number of pairs the node can handle
    MAX_PAIRS = 10

    @classmethod
    def INPUT_TYPES(s):
        inputs = {
            "required": {
                "text": ("STRING", {"default": "", "multiline": True, "forceInput": True}),
            },
            "optional": {}
        }
        # Add just start marker and end marker for each pair as optional inputs
        for i in range(1, s.MAX_PAIRS + 1):
            inputs["optional"][f"start_marker_{i}"] = ("STRING", {"default": ""})
            inputs["optional"][f"end_marker_{i}"] = ("STRING", {"default": ""})

        return inputs

    # Define return types and names dynamically based on MAX_PAIRS
    RETURN_TYPES = tuple(["STRING"] * MAX_PAIRS)
    RETURN_NAMES = tuple([f"extracted_text_{i}" for i in range(1, MAX_PAIRS + 1)])

    FUNCTION = "extract"
    CATEGORY = "BS-Nodes/Text"
    OUTPUT_NODE = True

    def extract(self, text, **kwargs):
        """
        Extracts text segments based on non-empty start/end markers.
        - If both markers non-empty: Extracts between them.
        - If only start non-empty: Extracts from after start marker to the end.
        - If only end non-empty: Extracts from beginning up to end marker.

        Args:
            text (str): The main input text.
            **kwargs: Contains start_marker_i and end_marker_i values.

        Returns:
            tuple: A tuple containing the extracted text for each active pair,
                   padded with empty strings up to MAX_PAIRS.
        """
        results = []

        for i in range(1, self.MAX_PAIRS + 1):
            start_marker = kwargs.get(f"start_marker_{i}", "")
            end_marker = kwargs.get(f"end_marker_{i}", "")

            extracted_text = "" # Default value

            # --- Logic ---
            # Case 1: Both markers are provided (and non-empty)
            if text and start_marker and end_marker:
                start_pos = text.find(start_marker)
                if start_pos != -1:
                    search_start_pos = start_pos + len(start_marker)
                    end_pos = text.find(end_marker, search_start_pos)
                    if end_pos != -1:
                        extracted_text = text[search_start_pos:end_pos]

            # Case 2: Only Start marker is provided (and non-empty)
            elif text and start_marker and not end_marker:
                start_pos = text.find(start_marker)
                if start_pos != -1:
                    search_start_pos = start_pos + len(start_marker)
                    extracted_text = text[search_start_pos:] # Slice to the end

            # Case 3: Only End marker is provided (and non-empty)
            elif text and not start_marker and end_marker:
                end_pos = text.find(end_marker)
                if end_pos != -1:
                    extracted_text = text[:end_pos] # Slice from the beginning

            # Case 4: Both markers are empty (or text is empty) - extracted_text remains ""

            # Append the result (either extracted text or "") for this pair number
            results.append(extracted_text)

        # Return the results as a tuple (already has MAX_PAIRS elements)
        return tuple(results)

# --- END OF FILE bs_textchop.py ---
