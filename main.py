from datetime import datetime
import uuid
invoices = []
payments = []

def newInvoice():
    print("Invoice")
    amount =  input("Amount:")
    try:
        amount=int(amount)
    except:
        return print("This is not number")
    date = datetime.now()
    currency = input("Currency(PLN,USD,EUR,GBP):")
    if(currency !="PLN" and currency !="USD" and currency !="GBP" and currency !="EUR"):
        return print("Unvalid currency (PLN,USD,GBP,EUR)")
    formattedDate = date.strftime("%d-%m-%Y")
    currentInvoice = {
        "amount": amount,
        "date": formattedDate,
        "currency": currency,
        "toPay": currency,
        "id": uuid.uuid4()
    }
    print (currentInvoice)
    invoices.append(currentInvoice)
    nextInvoice = input("Do you want to add next invoice, type 'more' ")
    if(nextInvoice =="more"):
        newInvoice()



def newPayment(invoice):
    print("Payment")
    print("Choosen invoice: " + invoice )
    amount = input("Amount:")
    try:
        amount = int(amount)
    except:
        return print("This is not number")
    date = datetime.now()
    currency = input("Currency(PLN,USD,EUR,GBP):")
    if(currency !="PLN" and currency != "GBP" and currency !="EUR" and currency !="USD"):
        return print("Unvalid currency (PLN,USD,GBP,EUR)")
    formattedDate = date.strftime("%d-%m-%Y")
    curremtPayment = {
        "amount": amount,
        "date": formattedDate,
        "currency": currency,
        "id": uuid.uuid4()
    }
    print(curremtPayment)
    payments.append(curremtPayment)
    

newInvoice()
print(invoices)
print("Which invoice do you want to pay?" )
print(invoices)
invoiceChoice = input("Choice: ")
findedInvoice = next((invoice for invoice in invoices if invoice["id"] == invoiceChoice), None)
if(findedInvoice == None):
    print("We dont have invoice with given id")
else:
    newPayment(findedInvoice)
print(payments)




