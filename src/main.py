from calculator import calculate
from generator import generate_invoice
from send_invoice import send_email

# main function
def main():
    # calculate expenses
    var_dict = calculate()
    # change these variables to own info
    var_dict["phone_number"] = "0"
    var_dict["address"] = "My House,\nExample Street"
    var_dict["sender"] = "My Name"
    var_dict["from_email"] = "my@gmail.com"
    var_dict["service"] = "Service provided"
    var_dict["app_password"] = "APP PASSWORD"
    var_dict["recipient"] = "Mr. Recipient"
    var_dict["to_email"] = "recipient@gmail.com"
    var_dict["iban"] = "IBAN NUMBER"
    

    # create new invoice
    generate_invoice(var_dict)

    # send invoice
    send_email(var_dict)

# run program
if __name__ == "__main__":
    main()
