# Kafka

First, Install Kafka and set environment variable
```
KAFKA_HOME=/path/to/kafka
```
you can get the command inside kafka_script folder.

The first line for windows user
The second line for Mac/Linux User

Start Zookeeper:

```
$ %KAFKA_HOME%\bin\windows\zookeeper-server-start.bat %KAFKA_HOME%\config\zookeeper.properties
```

Start Kafka:

```
$ %KAFKA_HOME%\bin\windows\kafka-server-start.bat %KAFKA_HOME%\config\server.properties
```

Kafka topics

```
$ kafka-topics --list --bootstrap-server localhost:9092
$ %KAFKA_HOME%\bin\windows\kafka-topics.bat --create --topic earth --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1
```

Kafka Producer
```
$ %KAFKA_HOME%\bin\windows\kafka-console-producer.bat --topic invoices --broker-list localhost:9092
```

Kafka Consumer
```
$ %KAFKA_HOME%\bin\windows\kafka-console-consumer.bat --topic earth --bootstrap-server localhost:9092
```

<!-- # Dockerization of Kafka

* https://github.com/wurstmeister/kafka-docker
* Difficulties with networking

## Problem with docker-composer network on macOS

Solution:
* Setting up priorities and dependencies, with `depends_on` property in `docker-compose.yml`

**Testing**

* Launch a separate docker container inside the network
* Connect to this container with command line, so we can 


Check the name of the kafka instance for the console.

```
$ docker ps
```

Use that name to run a terminal on it.

```
$ docker exec -it kafka-console /bin/bash
```

Commands for producers and consumers

```
$ /opt/kafka/bin/kafka-console-producer.sh --broker-list kafka-1:9092 --topic boerse.dev
$ /opt/kafka/bin/kafka-console-consumer.sh --bootstrap-server kafka-1:9092 --topic boerse.dev --from-beginning
```

** Development

```
$ docker run wurstmeister/zookeeper
$ docker run wurstmeister/kafka
``` -->