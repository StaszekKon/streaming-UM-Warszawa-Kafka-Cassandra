import json
from kafka import KafkaConsumer
from cassandra.cluster import Cluster
from uuid import uuid1
#https://docs.datastax.com/en/cql-oss/3.3/cql/cql_reference/cqlDropTable.html
if __name__ == '__main__':
    consumer = KafkaConsumer(
       'bus-input-api',
        bootstrap_servers='localhost:29092',
        auto_offset_reset='earliest'
    )

    cluster = Cluster(['127.0.0.1'], port = 9042)
    session = cluster.connect('keyspaces')

    for message in consumer:
        um_Warsaw_api_data = json.loads(message.value)
        
        try:
            
            for i in um_Warsaw_api_data:
                
                session.execute(
                """
                INSERT INTO keyspaces.um_Warsaw_bus_tram (uuiid, Lines, Lon, VehicleNumber, Time, Lat, Brigade)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """,(uuid1(), um_Warsaw_api_data["Lines"], um_Warsaw_api_data["Lon"],
                     um_Warsaw_api_data["VehicleNumber"], um_Warsaw_api_data["Time"],
                     um_Warsaw_api_data["Lat"], um_Warsaw_api_data["Brigade"],
                )
                )
                print("Sending : ", um_Warsaw_api_data)
        except:
            print("API Rate Limit Reached")
            pass