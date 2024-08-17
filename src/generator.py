import PyPDF2 as pdf2
# function to create a new invoice from a template
def generate_invoice():
    # create pdf reader object
    reader = pdf2.PdfReader("template.pdf")
    template = reader.pages[0]
    text = template.extract_text()
    pdf2.addText()
    # print the text in the template as confirmation
    print(text) 

