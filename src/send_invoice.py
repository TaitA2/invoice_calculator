from email.message import EmailMessage
import smtplib

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
    attachment_path = f"invoices/Invoice {var_dict['invoice_number']}.docx"
    print("Adding attachment...")
    with open(attachment_path, 'rb') as f:
        file_data = f.read()
        file_name = f.name
    msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)
    print(msg.items())
    # send
    print("Sending email ... ")
    # create connection
    s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    # login to email
    s.login(var_dict["sender_email"], var_dict["app_password"])
    # send email
    s.send_message(msg)
    s.quit()
    print("Sent!")

def main():
    send_email()

if __name__ == "__main__":
    send_email()