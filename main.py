from datetime import datetime
invoices = []

def newInvoice():
    amount =  input("Amount:")
    try:
        amount=int(amount)
    except:
        return print("This is not number")
    date = datetime.now()
    currency = input("Curremcy(PLN,USD,EUR,GBP):")
    if(currency !="PLN" and currency !="USD" and currency !="GBP" and currency !="EUR"):
        return print("Unvalid currency (PLN,USD,GBP,EUR)")
    formatted_date = date.strftime("%d-%m-%Y")
    currentInvoice = {
        "amount": amount,
        "date": formatted_date,
        "currency": currency
    }
    print (currentInvoice)
    invoices.append(currentInvoice)
    nextInvoice = input("Do you want to add next invoice, type 'more' ")
    if(nextInvoice =="more"):
        newInvoice()
    

newInvoice()
print(invoices)

