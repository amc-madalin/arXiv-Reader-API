# arXiv-Reader
An API for reading text from arXiv PDFs.

## API Overview

- **Purpose**: Facilitate the summary and querying of academic papers.
- **Functionality**:
  - Fetch paper details from **arXiv**.
  - Extract text from the papers' PDFs.
- **Integration with GPT-4**: 
  - Use the extracted text for summarization or queries via GPT-4 or a custom GPT model.
- **Hosting**: Designed for **Azure** hosting.
- **Unique Feature**: Bridges GPT models with multiple APIs, addressing the limitation in custom GPTs for accessing various APIs directly.


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

### Integration with GPT-4 for Summarization and Querying:
Once you fetch and extract text, use GPT-4 or a custom LLM model to summarize the content.

For a custom GPT use the custom action from the [openapi.json](https://github.com/amc-madalin/arXiv-Reader-API/blob/main/openapi.json) file.

And optional the custom instructions from the [instructions.txt](https://github.com/amc-madalin/arXiv-Reader-API/blob/main/instructions.txt) file.

Take into consideration that you need a hosting service like Azure.

Example:

```
https://arxivreader.azurewebsites.net/
```

## License
[Apache License 2.0](https://github.com/amc-madalin/arXiv-Reader-API/tree/main?tab=Apache-2.0-1-ov-file)
