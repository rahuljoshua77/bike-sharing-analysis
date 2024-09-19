# Bike Sharing Data Analysis Dashboard

## Overview
This Streamlit application provides an interactive dashboard for analyzing bike sharing data. It offers visualizations and analyses based on daily and hourly rental data.

## Features
- **Data Selection**: Choose between daily and hourly datasets.
- **Temperature Impact Visualization**: Analyze how temperature affects bike rentals.
- **Hourly Rental Patterns**: View rental patterns by hour (hourly data only).
- **RFM Analysis**: A simple analysis of recency, frequency, and monetary value of rentals.

## Structure Directory

bike-sharing-analysis/
│
├── app.py
├── day.csv
├── hour.csv
├── bike_sharing_analysis_rfm.ipynb
├── requirements.txt
└── README.md

## Setup and Installation

1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd <repository-folder>
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

5. Open a web browser and go to `http://localhost:8501` to view the dashboard.

## Data Files
- `day.csv`: Daily bike sharing data.
- `hour.csv`: Hourly bike sharing data.

Make sure these files are in the same directory as `app.py` for the app to work correctly.

## License
This project is licensed under the MIT License.


