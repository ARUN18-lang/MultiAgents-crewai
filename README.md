# Content Planning and Review Tool

This project is a Streamlit-based web application for content planning and review. It uses Groq models and HuggingFace models to generate and review content based on user input.

## Features

- **Content Planning**: Generate a comprehensive content plan based on a given topic.
- **Content Writing**: Write insightful and factually accurate content.
- **Content Editing**: Proofread and edit content for grammatical errors and alignment with the brand's voice.

## Installation
1. clone this repo

3. Create a virtual environment and activate it:

python -m venv .venv
.venv\Scripts\activate  # On Windows
source .venv/bin/activate  # On macOS/Linux

3. Install the required packages:

pip install -r requirements.txt

4.Create a .env file in the project root directory and add your API keys:
GROQ_API_KEY=your-groq-api-key

Usage
1. Run the Streamlit app:

streamlit run main.py

2. Open your web browser and go to http://localhost:8501 to access the application.

Example
1.Enter a topic for content planning in the input field.
2.Click the "Generate Content Plan" button to generate a content plan.
3.Click the "Review Content" button to display the backstory for content review.
