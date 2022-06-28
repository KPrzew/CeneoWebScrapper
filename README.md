# CeneoWebScraperS11

## Struktura opinii w serwisie Ceneo [Ceneo.pl](https://www.ceneo.pl/)

|Składowa|Selektor|Nazwa zmiennej|Typ zmiennej|
|--------|--------|--------------|------------|
|opinia|div.js_product-review|opinion|obj|
|indentyfikator opinii|div.js_product-review["data-entry-id"\]|opinion_id|int|
|autor opinii|span.user-post__author-name|author|str|
|rekomendacja|span.user-post__author-recomendation > em|recommendation|str|
|liczba gwiazdek|span.user-post__score_count|score|str|
|treść opinii|div.user-post__text|content|str|
|lista zalet|div.review-feature__title--positives ~ div.review-feature__item|pros|list|
|lista wad|div.review-feature__title--negatives ~ div.review-feature__item|cons|list|
|dla ilu osób przydatna|buttton.vote-yes > span|useful|int|
|dla ilu osób nieprzydatna|buttton.vote-no > span|useless|int|
|data wystawienie opinii|span.user-post__published > time:nth-child(1)["datetime"]|publish_date|list|
|data zakupu|span.user-post__published > time:nth-child(2)["datetime"]|purchase_date|list|


## Biblioteki wykorzystane w projekcie
|Biblioteka|Do czego była wykorzystywana|
|----------|------------------|
|Beautiful Soup|Analiza plikow html|
|requests|Żądania HTTP|
|Jinja|Szablony|
|pandas|Analiza i manipulacja danych|
|numpy|Tabele|
|matplotlib|Wykresy|
|Flask|Framework|
|Markdown|Konwersja .md na html|

## Etapy pracy nad projektem
1. Pobranie do pojedynczych zmiennych składowych pojedynczej opinii
2. Zapisanie wszystkich składowych pojedynczej opinii do słownika
3. Pobranie wszystkich opinii z pojedynczej strony do słowników i zapisanie ich na liście
4. Zapisanie wszystkich opinii z listy do pliku .json
5. Pobranie wszystkich opinii o produkcie i zapisanie ich na liście w postaci słowników
6. Dodanie możliwości podania kodu produktu przez użytkownika
7. Optymalizacja kodu 
    a. utworzenie funkcji do ekstrakcji elementów strony 
    b. utworzenie słownika selektorów 
    c. użycie dictionary comprehension do pobrania składowych pojedynczej opinii na podstawie słownika selektorów
8. Analiza pobranych opinii dla konkretnego produktu 
    a. wyliczenie podstawowych statystyk: 
        - liczba wszystkich opinii 
        - liczba opinii dla których podano zalety 
        - liczba opinii dla których podano wady 
        - średnia ocena produktu 
    b. przygotowanie wykresów: 
        - udział poszczególnych rekomendacji w ogólnej liczbie opinii 
        - histogram występowania poszczególnych ocen
9. Zapisanie statystyk w rozszerzeniu .json
10. Utworzenie wykresów
11. Wyświetlenie danych i wykresów
12. Umożliwienie dostępu do stron przez sekcję "products"

