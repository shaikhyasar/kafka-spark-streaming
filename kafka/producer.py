from confluent_kafka import Producer
import socket
import requests
import json
conf = {'bootstrap.servers': "localhost:9092",
        'client.id': socket.gethostname()}

API_KEY = 'WdZdiLhMQMRhl4iGNidcHaIqWPKLcfwao0vl10NB'
url = 'https://api.nasa.gov/EPIC/api/natural'

res = requests.get(url,params={'api_key':API_KEY})
# print(type(list(res.text)))

producer = Producer(conf)

for i in json.loads(res.text):
    i = json.dumps(i).encode('utf-8')
    producer.produce("earth",value=i)
    producer.flush()