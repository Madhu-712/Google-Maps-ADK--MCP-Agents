# Google-Maps-ADK--MCP-Agents

# MapsAgent and MapsMCPAgent

## Project Overview

This project implements two intelligent agents, `MapsAgent`, designed to assist users with mapping, directions, and finding places using various Google Maps Platform APIs  and 'MapsMCPAgent' leverages the **Model Context Protocol (MCP)** framework to integrate with the `@modelcontextprotocol/server-google-maps` toolset, allowing the agent to dynamically interact with numerous Google Maps services.

The primary goal of this agent is to provide a natural language interface for accessing Google Maps functionalities, making it easier to retrieve geographical information without needing direct API calls.

## Features

*   **Natural Language Understanding:** Interprets user queries related to maps, locations, and routes.
*   **Google Maps Platform Integration:** Utilizes a comprehensive set of Google Maps APIs through the MCP toolset, including:
    *   Directions API
    *   Distance Matrix API
    *   Maps Elevation API
    *   Geocoding API
    *   Geolocation API
    *   Maps JavaScript API (data provision, not direct execution)
    *   Roads API
    *   Time Zone API
    *   Places API (including new versions)
    *   Maps Static API / Street View Static API (for image generation, if implemented)
    *   Air Quality API, Solar API, Aerial View API, Pollen API (if enabled and used)
    *   Route Optimization API
*   **Extensible Architecture:** Built on the `LlmAgent` and `MCPToolset` framework, allowing for easy expansion with more tools or different LLMs.
*   **Cloud-Native:** Designed to run effectively within Google Cloud environments, leveraging environment variables for secure API key management.

## Project Structure

*   `agent.py`: Contains the core `LlmAgent` definition, instructions for the agent, and the configuration for the `MCPToolset` to connect to the Google Maps server.
*   `customfunctions.py` :  A helper module that contain Python functions for directly interacting with Google Maps Platform APIs using the `googlemaps` library.
*   `requirements.txt`: Lists all Python dependencies.

## Getting Started

Follow these instructions to set up and run the `MapsAgent` locally or deploy it.

### Prerequisites

*   **Google Cloud Project:** An active Google Cloud Project (e.g., `mcp-map-agent`).
*   **Billing Enabled:** Ensure billing is enabled for your Google Cloud Project.
*   **Google Maps Platform APIs:** Enable the necessary Google Maps Platform APIs in your Google Cloud Project. At a minimum, you'll need:
    *   **Directions API**
    *   **Geocoding API**
    *   **Places API**
    *   **Vertex AI API** (for the underlying LLM services)
*   **Google Maps Platform API Key:** A valid API key with access to the enabled Google Maps Platform APIs.
    *   For secure management, it is highly recommended to restrict this key to only the necessary APIs and, if applicable, to specific IP addresses or HTTP referrers.
    *   link reference to set up Java script API : https://developers.google.com/maps/documentation/javascript/get-api-key#create-api-keys
*   **Node.js and npm:** Required for the `@modelcontextprotocol/server-google-maps` toolset.
*   **Python 3.8+:** The Python environment for running `agent.py`.
*   **`gcloud` CLI:** Authenticated to your Google Cloud account and with the correct project set.

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```
    (Replace `your-username` and `your-repo-name` with your actual repository details.)

2.  **Install Python dependencies:**
    ```bash
    pip install requirements.txt
    ```
    (You'll need `google-cloud-aiplatform` and `model-context-protocol` at least.)

3.  **Install the MCP Google Maps Server (via npm):**
    The `MCPToolset` will manage running this, but `npm` needs to be able to find it. This step is usually handled dynamically by `npx` when the tool is first invoked.

    pip install mcp
    pip install googlemaps

### Configuration

1.  **Set your Google Maps Platform API Key:**
    The `MapsAgent` expects your API key to be provided via an environment variable.
    ```bash
    # For Linux/macOS
    export GOOGLE_MAPS_API_KEY="YOUR_ACTUAL_GOOGLE_MAPS_API_KEY"

    # For Windows Command Prompt
    set GOOGLE_MAPS_API_KEY="YOUR_ACTUAL_GOOGLE_MAPS_API_KEY"

    # For Windows PowerShell
    $env:GOOGLE_MAPS_API_KEY="YOUR_ACTUAL_GOOGLE_MAPS_API_KEY"
    ```
    **Replace `YOUR_ACTUAL_GOOGLE_MAPS_API_KEY` with your valid API key.**

2.  **Ensure `gcloud` is authenticated:**
    If you haven't already, authenticate your `gcloud` CLI and set your project:
    ```bash
    gcloud auth login
    gcloud config set project mcp-flight-agent
    gcloud auth application-default login # For local dev with client libraries
    ```

## Usage

To interact with the `MapsAgent`, you will typically run `agent.py` and provide it with user queries.

1.  **Run the agent:**
    ```bash
    python agent.py
    ```

2.  **Interact with the agent:**
    Once `agent.py` is running, it will listen for input. You can type your queries related to maps, directions, or places.

    **Example Queries:**
    *   "What's the route from Paris, France to Berlin, Germany?"
    *   "Find coffee shops near Times Square."
    *   "What is the elevation of Mount Everest?"
    *   "Tell me the time zone of Tokyo, Japan."
    *   "What's the address of the Eiffel Tower?"
    *   "Travelling from Bangalore to Pune .Give directions info, weather info, airquality info,elevation info,driving navigation map details ,important hotspots and cafes.
    *   I am currently in Satara and want to navigate shirdi. Give me directions and plan.

## Contributing

Contributions are welcome! Please follow these steps:
1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/your-feature-name`).
3.  Make your changes and commit them (`git commit -m 'Add new feature'`).
4.  Push to the branch (`git push origin feature/your-feature-name`).
5.  Open a Pull Request.

## License

This project is licensed under the [Your Chosen License, e.g., MIT License] - see the `LICENSE` file for details.

## Contact

For questions or issues, please open an issue in the GitHub repository or contact [Your Name/Email/Link].

