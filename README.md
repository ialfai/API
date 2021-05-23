# API

Aplikacja umożliwia zapisywanie i pobieranie danych z bazy danych w formie json. Możliwa jest także edycja danych oraz ich usuwanie. 


Dostępne linki:

http://127.0.0.1:8000/messages - na tej stronie można zobaczyć wszystkie wiadomości oraz dodać nową. 
Strona powinna być dostępna tylko dla uwierzytelnionego użytkownika, ale tej funkcjonalności jeszcze nie ma.

http://127.0.0.1:8000/messages/1 - na tej stronie można edytować lub usunąć wiadomość o numerze id równym jeden.
Strona powinna być dostępna tylko dla uwierzytelnionego użytkownika, ale tej funkcjonalności jeszcze nie ma.

http://127.0.0.1:8000/messages-view - na tej stronie nieuwierzytelniony użytkownik może zobaczyć listę wszystkich wiadomości, bez możliwości edycji lub usuwania.

http://127.0.0.1:8000/messages-view/1 - na tej stronie nieuwierzytelniony użytkownik może zobaczyć wiadomość o numerze id równym jeden. Każde wywołanie widoku
powoduje podniesienie o jeden wartość licznika wyświetleń wiadomości.


