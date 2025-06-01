Vehicle Routing Problem

Vehicle Routing Problem (VRP)
Projekt rozwiązujący problem VRP (Vehicle Routing Problem) algorytmem genetycznym. Celem jest znalezienie możliwie najkrótszych tras dla kilku pojazdów, które muszą odwiedzić daną grupę klientów i wrócić do magazynu.

Każde rozwiązanie (chromosom) to permutacja wszystkich klientów – czyli lista kolejności, w jakiej są odwiedzani. Ta lista dzielona jest na tyle części, ile mamy pojazdów – i każda część to trasa jednego pojazdu.

Algorytm genetyczny działa w kilku krokach:
- najpierw tworzy losową populację takich rozwiązań,
- potem wybiera lepsze rozwiązania (im krótsza trasa, tym lepiej),
- krzyżuje je i mutuje (zamienia miejscami klientów), żeby stworzyć nowe rozwiązania,
- i powtarza ten proces przez wiele pokoleń (generacji),
- na końcu zwraca najlepszy wynik – najkrótsze znalezione trasy.

Parametry: liczba pojazdów, klientów, rozmiar populacji, liczbę generacji, szanse na krzyżowanie i mutację. Warto poeksperymentować.