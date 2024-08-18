from calculator import calculate
from generator import generate_invoice, send_email

# main function
def main():
    # calculate expenses
    var_dict = calculate()
    # change these variables to own info
    var_dict["phone_number"] = "0"
    var_dict["address"] = "My House,\nExample Street"
    var_dict["sender"] = "My Name"
    var_dict["sender_email"] = "my@gmail.com"
    var_dict["recipient"] = "Mr. Recipient"
    var_dict["recipient_email"] = "recipient@example.com"
    var_dict["iban"] = "IBAN NUMBER"

    # create new invoice
    generate_invoice(var_dict)

    # send invoice
    # send_email(var_dict)

# run program
if __name__ == "__main__":
    main()
