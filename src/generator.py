import docx
from email.message import EmailMessage
import smtplib

# function to create a new invoice from a docx template
def generate_invoice(var_dict):
    print("opening template... ")
    template = docx.Document("template.docx")
    print("Replacing placeholders... ")
    invoice = find_and_replace(template.pages[0], var_dict)
    print(f"Saving Invoice {var_dict["invoice_number"]}... ")
    invoice.save(f"invoices/Invoice {var_dict['invoice_number']}")
    print("Done!")
    

def find_and_replace(text, var_dict):
    for word in text:
        if word.startswith("placeholder"):
            print(word "is replaced with "end="")
            var = word.replace("placeholder_", "")
            word = var_dict[var]
            print(word)
    return text

def send_email(var_dict):
    # create email
    print("creating email... ")
    msg = EmailMessage()
    subject = f"Invoice for {var_dict['location']}"
    print(f"Setting subject to: {subject}")
    msg["Subject"] = subject
    msg["From"] = var_dict["sender_email"]
    msg["To"] = var_dict["recipient_email"]
    msg.set_content(f"Hi,\n\nPlease find invoice attached.\n\nAll the best,\n{var_dict['sender']}")
    msg.add_attachment(f"invoices/Invoice {var_dict['invoice_number']}")
    print(msg.items())
    # send
    print("Sending email ... ")
    s = smtplib.SMTP('localhost')
    s.send_message(msg)
    s.quit()
    print("Sent!")

def main():
    generate_invoice()
    send_email()

if __name__ == "__main__":
   main()