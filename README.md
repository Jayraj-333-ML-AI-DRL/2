# ATS Tracker

This project is an Application Tracking System (ATS) that evaluates resumes based on a given job description.

## Introduction

The ATS Tracker is designed to simulate a skilled or experienced ATS with a deep understanding of the tech field, including software engineering, data science, data analysis, and big data engineering. Its primary task is to evaluate resumes based on a provided job description, assigning a percentage match and identifying missing keywords with high accuracy.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)

- [License](#license)

## Installation

To install and set up the ATS Tracker, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ATS-Tracker.git
   
   
2. Navigate to the project directory:
    ```bash
    cd ATS-Tracker 

3. Install the required dependencies:
    ````bash
    pip install -r requirements.txt

4. Create a .env file in the project directory and add your GenAI API key:
    ```
    GENAI_APIKEY=your_api_key_here



## Usage

To use the ATS Tracker, follow these steps:

1. Run the application:
   ```bash
   streamlit run ats_tracker.py

2. Paste the job description into the provided text area.

3.    Choose a PDF resume file and upload it.

4.   Click the "Submit" button to initiate the evaluation process.
