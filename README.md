# Apache Kafka and Apache Spark - A Distributed Streaming Project



## Running the project

You can try out this project running all components in your local setup

You need kafka and spark to run this project

Docker setup will be soon

Make sure following are available 

- Python 3.6 and above
- Java 8 or 11
- Kafka
- Spark

Install the python packages

```
pip install -r requirements.txt
```

Run the all the kafka command to start the kafka
 
- Zookeeper
- Kafka
- Kafka Topic

After initiated above command, Run the producer.py to generate the data and send to kafka cluster

```
python producer.py
```
Then, run the streaming_earth.py for curated data
```
python streaming_earth.py
```