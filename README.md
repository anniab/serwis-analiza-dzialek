# serwis-analiza-dzialek

Głównym celem serwisu jest wizualizacja efektów analizy potencjału budowalnego w miejscowości Kijany, która została oparta o algorytmy  nachylenia i ekspozycji. Serwis interentowy powstał za pomocą frameworka Django, a dane przechowywane są w bazie danych Postgres z rozszerzeniem postgis odpowiadającym za możliwości zapisywania danych geograficznych (przestrzennych). Więcej informacji o samym serwisie i analizie można znaleźć w samej aplikacji.

####  Wdrożoną aplikację można znaleźć pod adresem: https://app-mgr.herokuapp.com
(Czasami jej pierwsze załadowanie trwa trochę czasu)

##### Obecne funkcjonalności serwisu pozwalają użytkownikowi na:
- odczytywanie działek spełniających dane kryteria, 
- wyświetlanie informacji o numerze, obwodzie i polu danej działki, 
- wyszukiwanie działek po numerze działki, 
- tworzenie pomiarów na mapie, 
- zmiany map podkładowych, 
- włączenie planu zagospodorowania przestrzennego dla tej gminy, 

##### Technologie
- Django
- Python
- JavaScript
- HTML
- CSS
- SCSS
- PostgreSQL
