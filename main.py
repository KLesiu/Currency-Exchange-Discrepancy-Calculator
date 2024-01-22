from datetime import datetime
import uuid
import requests
invoices = []
payments = []

def newInvoice():
    print("Invoice")
    amount =  input("Amount:")
    try:
        amount=int(amount)
    except:
        return print("This is not number")
    date = input("Enter date (%d-%m-%Y): ")
    isDateCorrect = isValidDate(date)
    if(isDateCorrect == False):
        return print("Unvalid date type. Enter date with (%d-%m-%Y) type")
    currency = input("Currency(PLN,USD,EUR,GBP):")
    if(currency !="PLN" and currency !="USD" and currency !="GBP" and currency !="EUR"):
        return print("Unvalid currency (PLN,USD,GBP,EUR)")
    currentInvoice = {
        "amount": amount,
        "date": date,
        "currency": currency,
        "toPay": amount,
        "id": str(uuid.uuid4())
    }
    print (currentInvoice)
    invoices.append(currentInvoice)
    nextInvoice = input("Do you want to add next invoice, type 'more' ")
    if(nextInvoice =="more"):
        newInvoice()

def newPayment(invoice):
    print("Payment")
    print("Choosen invoice: " + invoice["id"] )
    amount = input("Amount:")
    basicAmount = amount
    try:
        amount = int(amount)
    except:
        return print("This is not number")
    date = datetime.now()
    currency = input("Currency(PLN,USD,EUR,GBP):")

    if(currency !="PLN" and currency != "GBP" and currency !="EUR" and currency !="USD"):
        return print("Unvalid currency (PLN,USD,GBP,EUR)")
    formattedDate = date.strftime("%d-%m-%Y")
    invoiceCurrency = invoice['currency']
    exchangeRate = getExchangeRateFromToday(invoiceCurrency)
    if(currency != invoiceCurrency):
        if(currency == 'PLN'):
            amount /= exchangeRate
        elif(currency == "EUR"):
            exchangeRateEURPLN = getExchangeRateFromToday('eur')
            amount *= exchangeRateEURPLN
            amount /= exchangeRate
        elif(currency == "USD"):
            exchangeRateUSDPLN = getExchangeRateFromToday('usd')
            amount *= exchangeRateUSDPLN
            amount /= exchangeRate
        else:
            exchangeRateGPBPLN = getExchangeRateFromToday('gbp')
            amount *= exchangeRateGPBPLN
            amount /= exchangeRate
        amount = round(amount,2)
    curremtPayment = {
        "amount": basicAmount,
        "date": formattedDate,
        "currency": currency,
        "id": str(uuid.uuid4())
    }
    print(curremtPayment)
    payments.append(curremtPayment)
    invoice["toPay"] -= amount
    if(invoice["toPay"] == 0):
        invoices.remove(invoice) 

def getExchangeRateFromToday(currency):
    url = f"http://api.nbp.pl/api/exchangerates/rates/a/{currency}/"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        exchangeRate = data["rates"][0]["mid"]
        return exchangeRate
    else:
        print(f"Request failed with status code: {response.status_code}")

def getExchangeRateFromDate(currency,date):
    url = f"http://api.nbp.pl/api/exchangerates/rates/a/{currency}/{date}/"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        exchangeRate = data["rates"][0]["mid"]
        return exchangeRate
    else:
        print(f"Request failed with status code: {response.status_code}")    

def isValidDate(date_str, date_format='%d-%m-%Y'):
    try:
        datetime.strptime(date_str, date_format)
        return True
    except ValueError:
        return False

startProgram = True
while (startProgram==True):
    print('What do you want to do?:')
    print('- Add new invoice (Enter number 1)')
    print('- Add new payment (Enter number 2)')
    print('If you want to close program (Enter number 10)')
    choice = input("Your choice:")
    if(choice == '10'):
        startProgram = False
    if(choice == '1'):
        newInvoice()
    if(choice == '2'):
        if(len(invoices)==0):
            print("You dont have invoices!")
        else:
            print("Which invoice do you want to pay?" )
            print(invoices)
            invoiceChoice = input("Choice (enter id): ")
            findedInvoice = next((invoice for invoice in invoices if invoice["id"] == invoiceChoice), None)
            if(findedInvoice == None):
                print("We dont have invoice with given id")
            else:
                print(findedInvoice)
                newPayment(findedInvoice)
                print(payments)



















