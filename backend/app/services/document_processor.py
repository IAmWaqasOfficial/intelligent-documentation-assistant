import fitz
from app.services.text_splitter import split_text


def extract_pdf_text(file_path: str):

    document = fitz.open(file_path)

    all_text = ""

    for page in document:
        text = page.get_text()

        if text.strip():
            all_text += text + "\n"

    document.close()

    return all_text


def extract_and_chunk_pdf(file_path: str):

    all_text = extract_pdf_text(file_path)

    chunks = split_text(all_text)

    return {
        "text": all_text,
        "chunks": chunks
    }