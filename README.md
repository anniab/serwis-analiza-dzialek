# serwis-analiza-dzialek

Głównym celem serwisu jest wizualizacja efektów analizy potencjału budowalnego w miejscowości Kijany, która została oparta o algorytmy  nachylenia i ekspozycji. Serwis interentowy powstał za pomocą frameworka Django, a dane przechowywane są w bazie danych Postgres z rozszerzeniem postgis odpowiadającym za możliwości zapisywania danych geograficznych (przestrzennych). Więcej informacji o samym serwisie i analizie można znaleźć w zakładkach aplikacji.

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


##### Uruchomienie aplikacji
Opisana instrukcja dotyczy systemu komputerowego Windows
1. Najpierw należy rozpakować plik .
2. Następnie należy uruchomić konsole.
3. Następnie należy utworzyć w konsoli wirtualne środowisko i je aktywować:
```
            python -m venv nazwa_srodowiska 
```
```
            activate nazwa_srodowiska
```
4. Następnie należy w konsoli przejść do lokalizacji folderu  aplikacja\webgis
5. Zainstalować wszystkie biblioteki i pakiety z pliku requirements.txt, w pliku znajdują się  nazwy wszystkich zainstalowanych pakietów i bibliotek wraz z ich dokładną wersją
```
            pip install -r requirements.txt
```
6. Po poprawnej instalacji wszystkich bibliotek należy  wpisać polecenie uruchamiające serwer deweloperski
```
            python manage.py runserver
```
7. Efektem tego powinno być
```
          Starting development server at http://127.0.0.1:8000/
```
8. Wtedy należy http://127.0.0.1:8000/ przekopiować do pasku przeglądarki internetowej
9. Serwis powinien już być załadowany i widoczny
