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
        print(f"Invoice closed {invoice['id']} ")

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

def paymentSummary(invoice):
    invoiceState = invoice["toPay"]
    invoiceState = round(invoiceState,2)
    if(invoiceState > 0):
        print(f"You have to pay {invoiceState}")
    else:
        print(f"You have {-invoiceState} excess payment")

def openFileInvoices(filePath):
    try:
        with open(filePath, 'r') as file:
            for line in file:
                data = line.strip().split(' ')
                try:
                    int(data[1])
                except:
                    return print(f"This is not number in line {line}")
                if(data[3] !="PLN" and data[3] !="USD" and data[3] !="GBP" and data[3] !="EUR"):
                    return print(f"Unvalid currency (PLN,USD,GBP,EUR) in line {line}")
                isDateCorrect = isValidDate(data[5])
                if(isDateCorrect == False):
                    return print(f"Unvalid date type. Enter date with (%d-%m-%Y) type in line {line}")
                transactionData = {
                    'amount': int(data[1]),
                    'currency': data[3],
                    'date': data[5],
                    'toPay': int(data[1]),
                    'id': str(uuid.uuid4())
                }
                invoices.append(transactionData)
                
    except:
        print('Incorrect file path')
    print(invoices)

def openFilePayments(filePath):
    try:
        with open(filePath, 'r') as file:
                for line in file:
                    data = line.strip().split(' ')
                    try:
                        int(data[1])
                    except:
                        return print(f"This is not number in line {line}")
                    if(data[3] !="PLN" and data[3] !="USD" and data[3] !="GBP" and data[3] !="EUR"):
                        return print(f"Unvalid currency (PLN,USD,GBP,EUR) in line {line}")
                    findedInvoice = next((invoice for invoice in invoices if invoice['id']  == data[5]), None)
                    if(findedInvoice == None):
                        print("We dont have invoice with given id")
                    else: 
                        if(data[3] != findedInvoice["currency"]):
                            exchangeRate = getExchangeRateFromToday(findedInvoice["currency"])
                            amount = int(data[1])
                            if(data[3] == 'PLN'):
                                amount /= exchangeRate
                            elif(data[3] == "EUR"):
                                exchangeRateEURPLN = getExchangeRateFromToday('eur')
                                amount *= exchangeRateEURPLN
                                amount /= exchangeRate
                            elif(data[3] == "USD"):
                                exchangeRateUSDPLN = getExchangeRateFromToday('usd')
                                amount *= exchangeRateUSDPLN
                                amount /= exchangeRate
                            else:
                                exchangeRateGPBPLN = getExchangeRateFromToday('gbp')
                                amount *= exchangeRateGPBPLN
                                amount /= exchangeRate
                            amount = round(amount,2)
                        transactionData = {
                            'amount': amount,
                            'currency': data[3],
                            'id': str(uuid.uuid4())
                        }
                        payments.append(transactionData)
                        findedInvoice["toPay"] -= transactionData["amount"]
                        findedInvoice["toPay"] = round(findedInvoice["toPay",2])
                        if(findedInvoice["toPay"] == 0):
                            invoices.remove(findedInvoice)
                            print(f"Invoice closed {findedInvoice['id']}")
    except:
        print('Incorrect file path')

startProgram = True
while (startProgram==True):
    print('What do you want to do?:')
    print('- Add new invoice (Enter number 1)')
    print('- Add new payment (Enter number 2)')
    print('- Check invoice (Enter number 3)')
    print('- Add new invoice from file (Enter number 4)')
    print('- Add new payment from file (Enter number 5)')
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
                newPayment(findedInvoice)
                print(payments)
    if(choice == '3'):
        if(len(invoices)==0):
            print("You dont have invoices!")
        else:
            print("Which invoice do you want to check?" )
            print(invoices)
            invoiceChoice = input("Choice (enter id): ")
            findedInvoice = next((invoice for invoice in invoices if invoice["id"] == invoiceChoice), None)
            if(findedInvoice == None):
                print("We dont have invoice with given id")
            else:
                paymentSummary(findedInvoice)
    if(choice == '4'):
        print('File must have a structure: (Kwota: 400 Waluta: EUR Data: 22-01-2004) if you want to add more invoices, enter next in new line')
        invoicePath = input("Enter invoice path: ")
        openFileInvoices(invoicePath)
    if(choice == '5'):
        print('File must have a structure: (Kwota: 400 Waluta: EUR  FakturaId: iodjaio76f12osfiosholfjnoilh )')
        paymentPath = input("Enter payment path: ")
        openFilePayments(paymentPath)





















