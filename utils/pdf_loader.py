from pypdf import PdfReader

class PDFLoader: 

    def __init__(self):

        pass

    def load_pdf_text(self,path):
        reader = PdfReader(path)
        return "\n".join(page.extract_text() for page in reader.pages)
