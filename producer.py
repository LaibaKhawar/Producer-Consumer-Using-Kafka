import time
import numpy as np
from kafka import KafkaProducer

# Set up Kafka producer
producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

# Set up the items
products = ['no1', 'no2', 'no3', 'no4', 'no5', 'no6', 'no7', 'no8', 'no9', 'no10']

# Initialize data for sales
data = np.zeros((60*60*10, len(products)))

# Generate the data stream 
for i in range(60*60*10):
    userdata = np.random.binomial(1, 0.2, size=(100, len(products)))
    data[i,:] = np.sum(userdata, axis=0)
    unsold_items = {}
    for j, item in enumerate(products):
        if data[i,j] < 10:
            unsold_items[item] = data[i,j]
    #send kafka values in form of key and value pairs
    producer.send('unsold-items', key=str(i).encode('utf-8'), value=str(unsold_items).encode('utf-8'))
    time.sleep(1)
#close producer
producer.close()


























            #result1 from chatgpt
from kafka import KafkaProducer
import numpy as np

# Define the items and chance of buying
items = ['item1', 'item2', 'item3', 'item4', 'item5', 'item6', 'item7', 'item8', 'item9', 'item10']
chance = 0.2

# Create a Kafka producer instance
producer = KafkaProducer(bootstrap_servers=['localhost:9092'], value_serializer=lambda x: str(x).encode('utf-8'))

# Set the topic
topic = 'shop_items'

# Simulate the visits to the shops for each minute
for minute in range(10*60):

    # Generate the matrix of user-item interactions using numpy
    interactions = np.random.binomial(1, chance, size=(100, len(items)))

    # Calculate the number of items sold and unsold
    unsold = np.sum(interactions == 0, axis=0)
    sold = len(interactions) - unsold

    # Send the unsold items to the Kafka topic as key-value pairs
    for i, item in enumerate(items):
        if unsold[i] > 0:
            producer.send(topic, key=item, value=unsold[i])

# Close the producer
producer.close()
