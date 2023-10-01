# streaming-with-UM-Warszawa-Kafka
Otwarte dane - czyli dane po warszawsku
# Warunki korzystania z danych.
Żródło danych: Miasto Stołeczne Warszawa - serwis https://api.um.warszawa.pl/#

Dane użyte w tym rezpozytorium, które są przesyłane strumieniowo w czasie rzeczywistym i są danymi publicznymi - materiałami urzędowymi.

Data wytworzenia oraz pozyskania informacji publicznej z serwisu https://api.um.warszawa.pl/# 30.09.2023.

To repozytorium buduje aplikację do przesyłania strumieniowego w języku Python (użyte narzędzia Apache Kafka, silnik bazy danych Cassandra).
Przesyłane strumieniowo dane są przetwarzane i ładowane  do  silnika bazy danych Cassandra. 

Wszystkie aplikacje uruchamiane są w kontenerach Docker. Przesyłane są strumieniowo dane -	lokalizacje	pojazdów	komunikacji	miejskiej m.st. Warszawy na żywo z interfejsu API (https://api.um.warszawa.pl/api/action/busestrams_get/).

Warunki użycia repozytorium

1) Instalacja Docker Desktop (jeśli nie posiadasz)
2) Sklonowanie repozytorium:
    https://github.com/StaszekKon/streaming-with-UM-Warszawa-Kafka.git

3) Sciągnij obrazy docker i uruchom kontenery tych obrazów
   a) przejdź  do folderu streaming-with-UM-Warszawa-Kafka (folder gdzie jest ściągnięte repozytorium)
   np. cd streaming-with-UM-Warszawa-Kafka (możesz użyć narzędzia cmd)
   b) wpisz w cmd polecenie: docker-compose up -d (pobranie obrazów Kafki, Cassandry, Zookeeper i uruchomienie w tle kontenerów)
4) 
