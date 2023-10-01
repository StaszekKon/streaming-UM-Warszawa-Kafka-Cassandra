import json
import time
from datetime import datetime
from kafka import KafkaProducer
from rest_api_Warsaw import data_from_um_Warsaw_api

sleep_time = 10

def serializer(message):
    return json.dumps(message).encode('utf-8')

producer = KafkaProducer(
    bootstrap_servers=['localhost:29092'],
    value_serializer=serializer
)

if __name__ == '__main__':
    while True:
        try:
            
            api_data = data_from_um_Warsaw_api()               
            print('Sending data...')
            for record in api_data['result']:
                 prod = producer.send('bus-input-api', record)
                 result = prod.get(timeout=40)
        except:
            print("blad")
        time.sleep(sleep_time)