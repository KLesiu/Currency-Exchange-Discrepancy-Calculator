# Dokumentacja programu

## Nazwa programu
Program do zarządzania fakturami i płatnościami oraz do obliczania różnic kursowych między nimi

## Autorzy
- Jakub Leśkiewicz
- Antoni Krawczyk

## Język programowania
Python

## Opis ogólny
Program umożliwia zarządzanie fakturami i płatnościami. Pozwala użytkownikowi dodawać nowe faktury, dokonywać płatności, sprawdzać stan faktur, importować dane z plików oraz obliczać różnice kursowe w walutach na fakturze.

# Funkcjonalności

## 1. `newInvoice()`
Dodaje nową fakturę do listy faktur.

## 2. `newPayment(invoice)`
Dodaje nową płatność do listy płatności na podstawie wybranej faktury.

- `invoice`: Faktura, do której dodawana jest płatność.

## 3. `paymentSummary(invoice)`
Wyświetla podsumowanie stanu faktury.

- `invoice`: Faktura, której stan jest sprawdzany.

## 4. `openFileInvoices(filePath)`
Dodaje nowe faktury na podstawie danych z pliku.

- `filePath`: Ścieżka do pliku zawierającego dane faktur.

## 5. `openFilePayments(filePath)`
Dodaje nowe płatności na podstawie danych z pliku.

- `filePath`: Ścieżka do pliku zawierającego dane płatności.

## 6. `calculateExchangeRateDifferences(invoice, paymentsForInvoice)`
Oblicza różnice kursowe w walutach na fakturze.

- `invoice`: Faktura, dla której obliczane są różnice kursowe.
- `paymentsForInvoice`: Lista płatności powiązanych z fakturą.

## 7. `saveToTheFile(fileName, data)`
Zapisuje dane do pliku.

- `fileName`: Nazwa pliku, do którego dane są zapisywane.
- `data`: Dane do zapisania.

## 8. `saveInvoiceToTheFIle(invoice, paymentsForInvoice)`
Zapisuje dane faktury i powiązanych płatności do pliku.

- `invoice`: Faktura do zapisania.
- `paymentsForInvoice`: Lista płatności powiązanych z fakturą.

## 9. `isValidDate(date_str, date_format='%d-%m-%Y')`
Sprawdza poprawność formatu daty.

- `date_str`: Data w formie tekstowej.
- `date_format`: Opcjonalny format daty (domyślnie `%d-%m-%Y`).

## 10. `getExchangeRateFromToday(currency)`
Pobiera aktualny kurs wymiany dla danej waluty.

- `currency`: Kod waluty.

## 11. `getExchangeRateFromDate(currency, date)`
Pobiera kurs wymiany dla danej waluty na określoną datę.

- `currency`: Kod waluty.
- `date`: Data w formie tekstowej (`%d-%m-%Y`).

# Instrukcja uruchomienia programu

Aby uruchomić program, wykonaj poniższe kroki:

## 1. Sklonuj repozytorium za pomocą Git

Użyj poniższej komendy w terminalu, aby sklonować repozytorium:

```bash
git clone [link_do_repozytorium]
```

## 2. Przejdz do folderu z repozytorium na swoim komputerze za pomocą

```bash
cd [link_do_repozytorium]
```

## 3. Mając zainstalowanego pythona uruchom
```bash
python main.py
```

## 4. Program działa w pętli posługując się instrukcjami od 1 do 7, nr 10 kończy program

# Zabezpieczenia
Program zawiera mechanizmy zabezpieczające przed błędnym wprowadzeniem danych, na przykład sprawdzanie poprawności daty, waluty


# Pliki wsadowe
## Dla faktur
 - File must have a structure: (Kwota: 400 Waluta: EUR Data: 22-01-2004)
## Dla płatności
 - File must have a structure: (Kwota: 400 Waluta: EUR  FakturaId: iodjaio76f12osfiosholfjnoilh )



