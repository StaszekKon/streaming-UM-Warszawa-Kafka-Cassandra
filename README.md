# streaming-with-UM-Warszawa-Kafka
Otwarte dane - czyli dane po warszawsku
# Warunki korzystania z danych.
Żródło danych: Miasto Stołeczne Warszawa - serwis https://api.um.warszawa.pl/#

Dane użyte w tym rezpozytorium, które są przesyłane strumieniowo w czasie rzeczywistym i są danymi publicznymi - materiałami urzędowymi.

Data wytworzenia oraz pozyskania informacji publicznej z serwisu https://api.um.warszawa.pl/# 30.09.2023.

To repozytorium buduje aplikację do przesyłania strumieniowego w języku Python (użyte narzędzia Apache Kafka, silnik bazy danych Cassandra).
Przesyłane strumieniowo dane są przetwarzane i ładowane  do  silnika bazy danych Cassandra. 

Wszystkie aplikacje uruchamiane są w kontenerach Docker. Dane przesyłane są na  żywo strumieniowo - lokalizacje	pojazdów	komunikacji	miejskiej m.st. Warszawy  z interfejsu API (https://api.um.warszawa.pl/api/action/busestrams_get/).

Warunki użycia repozytorium

1) Instalacja Docker Desktop (jeśli nie posiadasz)
2) Sklonowanie repozytorium:
    https://github.com/StaszekKon/streaming-with-UM-Warszawa-Kafka.git

3) Sciągnięcie obrazów docker i uruchomienie kontenerów tych obrazów
   a) przejdź  do folderu streaming-with-UM-Warszawa-Kafka (folder gdzie jest ściągnięte repozytorium)
   np. cd streaming-with-UM-Warszawa-Kafka (możesz użyć narzędzia cmd)
   b) wpisz w cmd polecenie: docker-compose up -d (pobranie obrazów Kafki, Cassandry, Zookeeper i uruchomienie w tle kontenerów)
4)  Utworzonie przestrzeni kluczy i tabeli bazy danych Cassandra.
   a) docker exec -it <container_name> cqlsh (po uruchomieniu polecenia docker ps zobaczymy uruchomione kontenery - ich nazwy)
   b) CREATE KEYSPACE keyspaces WITH REPLICATION={'class': 'SimpleStrategy', 'replication_factor': 1};
   c)   CREATE TABLE IF NOT EXISTS keyspaces.um_Warsaw_bus_tram (
        uuiid UUID,
        Lines TEXT,
        Lon float,
        VehicleNumber TEXT,
        Time TEXT,
        Lat float, 
        Brigade TEXT, 
        PRIMARY KEY(uuiid)); 
5)  Uruchomienie aplikacji do przesyłania strumieniowego w języku Python - interfejs API, który udostępnia w czasie rzeczywistym lokalizacje pojazdów komunikacji miejskiej m. st. Warszawy
