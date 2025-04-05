# ComfyUI-BS-Textchop

A custom node for ComfyUI that extracts text segments found between specified start and end marker strings. You can define multiple pairs of markers to extract different segments from the same input text.

![Example Node](placeholder_image.png) <!-- Optional: Replace with a screenshot -->

## Features

*   **Multiple Extractions:** Define up to 10 pairs of start/end markers.
*   **Configurable Count:** Use the `pair_count` input to specify how many marker pairs to actively use.
*   **Simple Extraction Logic:** For each pair, it finds the *first* occurrence of the start marker, and then the *first* occurrence of the end marker *after* that start marker.
*   **Individual Outputs:** Each marker pair corresponds to a unique output string (`extracted_text_1`, `extracted_text_2`, etc.).

## Installation

1.  **Navigate** to your ComfyUI `custom_nodes` directory:
    *   Example: `ComfyUI/custom_nodes/`
2.  **Clone this repository:**
    ```bash
    git clone https://github.com/YOUR_GITHUB_USERNAME/ComfyUI-BS-Textchop.git
    ```
    (Replace `YOUR_GITHUB_USERNAME` with your actual GitHub username if you host it there)
    *   Alternatively, download the repository ZIP file and extract its contents into the `custom_nodes` directory. Make sure the folder name is `ComfyUI-BS-Textchop`.
3.  **Restart ComfyUI:** Ensure ComfyUI is fully restarted to recognize the new node.

## Usage

1.  **Add Node:** Right-click on the ComfyUI canvas, go to `Add Node` -> `BS-Nodes` -> `Text`, and select `BS Textchop`.
2.  **Connect Inputs:**
    *   `text`: Connect the main string from which you want to extract text.
    *   `pair_count`: Set this integer to the number of marker pairs you intend to use (from 1 to 10).
    *   `start_marker_1`, `end_marker_1`: Define the first pair of text markers.
    *   `start_marker_2`, `end_marker_2` (and so on, up to `pair_count`): Define subsequent pairs if needed. Inputs beyond `pair_count` are ignored.
3.  **Connect Outputs:**
    *   `extracted_text_1`: This output will contain the text found between `start_marker_1` and `end_marker_1`.
    *   `extracted_text_2`: Corresponds to the second marker pair.
    *   ...and so on, up to `extracted_text_10`. Outputs corresponding to pairs beyond `pair_count` or where the text wasn't found will be empty strings.

### Example

Suppose you have the following input `text`: