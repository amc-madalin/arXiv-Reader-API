# arXiv-Reader
An API for reading text from arXiv PDFs.

## Introduction
This API is designed for integrating with GPT-4 to summarize academic papers from the arXiv database. It provides endpoints to fetch paper details from arXiv and extract text from PDFs. The extracted text can then be summarized using GPT-4 or a custom GPT model. The API is suitable for hosting on Azure and can be easily integrated into AI-driven applications.

## Features
- **Fetch Papers from ArXiv**: Retrieve paper details such as title, summary, publication date, and PDF URL based on search queries.
- **Extract Text from PDF**: Download and extract text from PDFs hosted on arXiv.

## Prerequisites
- Python 3.x
- Flask
- Requests
- PyPDF2
- An Azure account for hosting (optional)

## Installation and Setup

**Clone the Repository**:
   ```bash
   git clone https://github.com/amc-madalin/arXiv-Reader-API.git
   ```

### Install Dependencies:
Navigate to the project directory and install dependencies using:

```bash
pip install -r requirements.txt
```

### Environment Variables:
Set `ARXIV_API_URL` in your environment or directly in the code.

### Running the API Locally:
Run the Flask application:

## Using the API

### Fetch Papers from ArXiv:
Send a GET request to `/fetchFromArxiv` with parameters `query` (search term) and `max_results` (optional, default 5).

```http
GET /fetchFromArxiv?query=[search_term]&max_results=[number]
```

### Extract Text from PDF:
Send a GET request to `/extractTextFromPdf` with the parameter `pdf_url`.

```http
GET /extractTextFromPdf?pdf_url=[pdf_url]
```

### Integration with GPT-4 for Summarization:
Once you fetch and extract text, use GPT-4 or a custom LLM model to summarize the content.

## License
[Specify License Here]
