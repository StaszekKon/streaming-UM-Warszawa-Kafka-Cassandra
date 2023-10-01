CREATE KEYSPACE keyspaces WITH REPLICATION={'class': 'SimpleStrategy', 'replication_factor': 1};


CREATE TABLE IF NOT EXISTS keyspaces.um_Warsaw_bus_tram (
uuiid UUID,
Lines TEXT,
Lon float,
VehicleNumber TEXT,
Time TEXT,
Lat float, 
Brigade TEXT, 
PRIMARY KEY(uuiid));