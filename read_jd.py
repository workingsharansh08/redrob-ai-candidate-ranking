from docx import Document

doc = Document("job_description.docx")

for para in doc.paragraphs:
    print(para.text)