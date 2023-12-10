from flask import Flask, request, jsonify
import requests
import os
import xml.etree.ElementTree as ET
import PyPDF2
from io import BytesIO

app = Flask(__name__)

ARXIV_API_URL = os.getenv('ARXIV_API_URL', 'http://export.arxiv.org/api/query?search_query=')

@app.route('/')
def index():
    return "Welcome to the API!"

@app.route('/fetchFromArxiv', methods=['GET'])
def fetch_from_arxiv():
    query = request.args.get('query', '')
    max_results = request.args.get('max_results', 5, type=int)  # Default to 5 if not specified

    if not query:
        return jsonify({"error": "Query parameter is required"}), 400

    # Modify the URL to include max_results and processed query
    url = f'{ARXIV_API_URL}{query}&max_results={max_results}&sortBy=submittedDate&sortOrder=descending'
    
    try:
        response = requests.get(url)
        response.raise_for_status()

        root = ET.fromstring(response.content)
        entries = []
        for entry in root.findall('{http://www.w3.org/2005/Atom}entry'):
            entry_data = {
                'id': entry.find('{http://www.w3.org/2005/Atom}id').text,
                'title': entry.find('{http://www.w3.org/2005/Atom}title').text,
                'summary': entry.find('{http://www.w3.org/2005/Atom}summary').text,
                'publication_date': entry.find('{http://www.w3.org/2005/Atom}published').text,
                'pdf_url': entry.find('{http://www.w3.org/2005/Atom}id').text.replace('/abs/', '/pdf/') + '.pdf'
            }
            entries.append(entry_data)

        if len(entries) < max_results:
            return jsonify({"message": "Fewer papers available than requested", "entries": entries})
        else:
            return jsonify(entries)
    except requests.exceptions.RequestException as e:
        app.logger.error(f"Error fetching data from ArXiv: {e}")
        return jsonify({"error": "Failed to fetch data from ArXiv", "details": str(e)}), 500
    except ET.ParseError as xml_err:
        app.logger.error(f"XML parsing error: {xml_err}")
        return jsonify({"error": "XML parsing error", "details": str(xml_err)}), 500

@app.route('/extractTextFromPdf', methods=['GET'])
def extract_text_from_pdf():
    pdf_url = request.args.get('pdf_url', '')
    if not pdf_url:
        return jsonify({"error": "PDF URL parameter is required"}), 400

    try:
        # Download PDF from URL
        response = requests.get(pdf_url)
        response.raise_for_status()

        # Use BytesIO as a buffer for the PDF file
        f = BytesIO(response.content)

        # Initialize PyPDF2 reader
        pdf_reader = PyPDF2.PdfReader(f)
        extracted_text = ""

        # Extract text from each page
        for page in pdf_reader.pages:
            extracted_text += page.extract_text() + "\n"

        return jsonify({"extracted_text": extracted_text})
    except requests.RequestException as e:
        return jsonify({"error": "Error downloading PDF", "details": str(e)}), 500
    except Exception as e:
        return jsonify({"error": "Failed to extract text from PDF", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=False)