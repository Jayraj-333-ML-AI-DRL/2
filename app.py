# Importing necessary libraries
from dotenv import load_dotenv  # For loading environment variables from .env file
import os
import streamlit as st

import google.generativeai as Genai
import pypdf2 as pdf 

# Load environment variables from .env file
load_dotenv()

# Configure GenAI API with the API key from environment variables
Genai.configure(api_key=os.getenv("GENAI_APIKEY"))

# Load the Gemini Vision model
model = Genai.GenerativeModel('gemini-pro-vision')

# Function to get the model response based on input
def get_model_response(input):
    response = model.generate_content(input)
    return response.text

# Function to set up image data from the uploaded file
def input_pdf_text(uploaded_file):
    reader = pdf.PdfFileReader(uploaded_file)
    
    text = ""
    
    for page in range (reader.numPages):
        pageObj = reader.pages[page]
        text += str(pageObj.extract_text())
        
        
    return text 


# Input prompt for the model
input_prompt="""
Hey Act Like a skilled or very experience ATS(Application Tracking System)
with a deep understanding of tech field,software engineering,data science ,data analyst
and big data engineer. Your task is to evaluate the resume based on the given job description.
You must consider the job market is very competitive and you should provide 
best assistance for improving thr resumes. Assign the percentage Matching based 
on Jd and
the missing keywords with high accuracy
resume:{text}
description:{jd}

I want the response in one single string having the structure
{{"JD Match":"%","MissingKeywords:[]","Profile Summary":""}}
"""

# Set page configuration
st.set_page_config(
    page_title="My ATS tracker",
)

# Streamlit UI elements
st.header("ATS Tracker")

jd=st.text_area("Paste the Job Description")

# File uploader for CV
uploaded_file = st.file_uploader("Choose your CV ", type=[".pdf"],help= "Please make sure that the file is PDF format.")



# Button 
submit = st.button("submit")



if submit:
    text = input_pdf_text(uploaded_file)
    
    # Get the model response
    response = get_model_response(input_prompt)
    
    # Display the response
    st.subheader("The response is")
    st.write(response)
