import docx
# function to create a new invoice from a docx template
def generate_invoice():
    template = docx.Document("template.docx")
    template.save("test.docx")

if __name__ == "__main__":
    generate_invoice()