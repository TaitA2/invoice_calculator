# Invoice Generator

A CLI based program for generating invoices. Created to solve my own real world problem of creating and sending invoices.

## Usage
* Edit the variables in main.py to meet your own needs (e.g replace "My Name" with your own name etc.)
    - I recommend setting the recipient email to your own for the first time you run the program to confirm the invoice gets delivered correctly
* Run main.py from the root of the program
* Answer all the CLI prompts as needed for your invoice
    - Invoice number is created in the format of YYMMXXX where Y is the year, M is the month, and X is the invoice suffix 
    - e.g the first invoice of September 2024 would be 2409001 
* Once the program is finished running, check the 'sent' section of your email to confirm the invoice was sent

## Template
This program should work with any placeholder template you want to use but there are a few requirements.
* Replace any fields you want the program to fill out with "placeholder_FIELDNAME" 
    - e.g The "Invoice Number" field on your template should look like "Invoice number: placeholder_invoice_number (see provided template for more examples)
* The template must be a .docx file format
