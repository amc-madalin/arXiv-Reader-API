# arXiv-Reader
An API for reading text from arXiv PDFs.

## Overview
This API is designed to fetch scientific papers from the ArXiv database and extract text from their PDFs. It's particularly useful in combination with GPT-4's summarization capabilities, allowing for quick and efficient summaries of academic papers. The API can be hosted on Azure and integrated with custom GPT models.

## Features
Fetch Papers from ArXiv: Retrieve a list of papers based on a user-defined query. Metadata including the title, summary, publication date, and PDF URL is returned.
Extract Text from PDF: Download a paper in PDF format from a provided URL and extract its text.
## How to Use

### Setup: 

Ensure you have Python and necessary packages installed. Use requirements.txt to install dependencies.

### Running the API:

Host the API on an Azure server or locally.

Start the API using python app.py.

### Endpoints:
- /: A simple welcome message.

- /fetchFromArxiv: Fetch papers from ArXiv. Use query parameters query for the search term and max_results for the number of results.

- /extractTextFromPdf: Extract text from a PDF. Use the pdf_url query parameter to specify the PDF's URL.
