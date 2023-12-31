# Streaming danych lokalizacji on-line pojazdów komunikacji miejskiej Urzędu miasta Warszawa za pomocą ekosystemu Kafka i załadowanie danych do bazy danych Cassandra
Otwarte dane - czyli dane po warszawsku

### DataFlow

Publiczny interfejs API (https://api.um.warszawa.pl/#) udostępnia dane  w czasie rzeczywistym (pobranie danych warszawskich przez skrypt Pythona) ---> wrzucenie danych (publikowanie danych do danego tematu) strumieniowo do  Kafka ----> załadowanie danych przez konsumenta do bazy danych Cassandra   



### Warunki korzystania z danych.
Żródło danych: Miasto Stołeczne Warszawa - serwis https://api.um.warszawa.pl/#

Dane użyte w tym rezpozytorium, które są przesyłane strumieniowo w czasie rzeczywistym i są danymi publicznymi - materiałami urzędowymi.

Data wytworzenia oraz pozyskania informacji publicznej z serwisu https://api.um.warszawa.pl/# 30.09.2023.

Wszystkie aplikacje uruchamiane są w kontenerach Docker. Dane przesyłane są na  żywo strumieniowo - lokalizacje on-line	pojazdów	komunikacji	miejskiej m.st. Warszawy  z interfejsu API (https://api.um.warszawa.pl/api/action/busestrams_get/).

+ Lat - współrzędna szerokości geograficznej w układzie WGS84(EPSG:4326)
+ Lon - współrzędna długości geograficznej w układzie WGS84(EPSG:4326)
+ Time - czas wysłania sygnału GPS
+ Lines - numer linii autobusowej lub tramwajowej
+ Brigade - numer brygady pojazdu
+ resource_id	=	f2e5503e-927d-4ad3-9500-4ab9e55deb59 (identyfikator zasobu)

**Warunki użycia repozytorium**

1) Instalacja Docker Desktop (jeśli nie posiadasz)
   
2) Sklonowanie repozytorium:
    https://github.com/StaszekKon/streaming-UM-Warszawa-Kafka-Cassandra.git

3) Sciągnięcie obrazów docker i uruchomienie kontenerów tych obrazów

     + przejdź  do folderu streaming-UM-Warszawa-Kafka-Cassandra (folder gdzie jest ściągnięte repozytorium)
   	  np. <br/>**cd streaming-UM-Warszawa-Kafka-Cassandra** (możesz użyć narzędzia cmd)
   
     + wpisz w cmd polecenie: **docker-compose up -d** (pobranie obrazów Kafki, Cassandry, Zookeeper i uruchomienie w tle kontenerów)
   
4) Utworzonie przestrzeni kluczy i tabeli bazy danych Cassandra.
   
   	+ docker exec -it <container_name> cqlsh (po uruchomieniu polecenia docker ps zobaczymy uruchomione kontenery - ich nazwy)
   
   	+ CREATE KEYSPACE keyspaces WITH REPLICATION={'class': 'SimpleStrategy', 'replication_factor': 1};

   	+  CREATE TABLE IF NOT EXISTS keyspaces.um_Warsaw_bus_tram (
        uuiid UUID,
        Lines TEXT,
        Lon float,
        VehicleNumber TEXT,
        Time TEXT,
        Lat float, 
        Brigade TEXT, 
        PRIMARY KEY(uuiid)); 
        
5)  Uruchomienie aplikacji do przesyłania strumieniowego w języku Python - interfejs API, który udostępnia w czasie rzeczywistym lokalizacje on-line pojazdów komunikacji miejskiej m. st. Warszawy
   
      + uruchom w kolejnym terminalu np. wierszu poleceń cmd interfejs API producenta (skrypt w Pythonie ściąga dane z API i wrzuca na platformę Kafka):

    	**python producent.py**
    
      + uruchom w następnym oknie cmd interfejs API dla konsumenta:

        **python consumer.py**
    
6) Sprawdzenie w bazie danych Cassandra czy zostały załadowane dane - lokalizacje on-line pojazdów komunikacji miejskiej m.st. Warszawa:
   
      +	 w oknie terminala cmd wchodzimy interaktywnie do  kontenera Cassandry poprzez polecenie:

      	 **docker exec -it <container_name> cqlsh**
 
      + wykonujemy polecenie: **select * from keyspaces.um_Warsaw_bus_tram;**
      
