# NexusCore Backend

NexusCore Backend is a Python-based RESTful API built with **FastAPI**. It handles complex optimization algorithms, AI-powered analysis, and PDF report generation for the NexusCore application suite.

## Features

- **Server Load Optimization**: Implements gradient ascent to maximize resource allocation and performance across server clusters.
- **Network Routing**: Uses Dynamic Programming on graphs to determine optimal paths for network traffic.
- **Marketing Optimization**: Employs the 0/1 Knapsack algorithm via Dynamic Programming to maximize ROI for marketing campaigns under a fixed budget.
- **AI Analysis**: Integrates the Gemini API to provide intelligent insights based on the optimization outcomes.
- **Report Generation**: Automatically generates comprehensive PDF reports detailing algorithm results and metrics.

## Technology Stack

- **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **Language**: Python 3.13+
- **Package Management**: [uv](https://docs.astral.sh/uv/)
- **AI Integration**: Google GenAI (`google-genai`)
- **PDF Generation**: `fpdf2`
- **Validation**: Pydantic
- **Environment Management**: `python-dotenv`

## Project Structure

- `app/main.py`: Entry point for the FastAPI application. Includes middleware and mounts routers.
- `app/algorithms/`: Core logic for optimization algorithms (`gradient_ascent.py`, `dp_graph.py`, `dp_knapsack.py`).
- `app/ai_analysis/`: Module for interacting with Google GenAI to analyze results.
- `app/marketing/`: Module handling marketing budget optimizations.
- `app/network_routing/`: Module handling network route optimizations.
- `app/server_load/`: Module handling server load distributions.
- `app/report/`: Module responsible for PDF generation.
- `app/core/`: Application settings and configuration.

## Setup and Installation

1. **Install `uv`**:
   Ensure you have [uv](https://docs.astral.sh/uv/) installed on your machine.

2. **Sync Dependencies**:
   ```bash
   uv sync
   ```

3. **Environment Variables**:
   Copy the example environment file and update variables appropriately:
   ```bash
   cp .env.example .env
   ```
   Add your `GEMINI_API_KEY` to the `.env` file to enable AI Analysis.

4. **Run the Server**:
   ```bash
   uv run fastapi dev app/main.py
   ```

The API documentation will be available at `http://127.0.0.1:8000/docs`.
