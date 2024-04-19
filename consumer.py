from kafka import KafkaConsumer
import matplotlib.pyplot as plt

# Set up Kafka consumer
consumer = KafkaConsumer('unsold-items', bootstrap_servers=['localhost:9092'])

# Set up the items
products = ['no1', 'no2', 'no3', 'no4', 'no5', 'no6', 'no7', 'no8', 'no9', 'no10']

# Initialize the least sold data
least_sold = {item: 0 for item in products}

# Receive and process the unsold items
for message in consumer:
    items_unsold = eval(message.value.decode('utf-8'))
    for item, count in items_unsold.items():
        if count > least_sold[item]:
            least_sold[item] = count

consumer.close()

# Plot the seasonality of the least sold item
least_sold_item = min(least_sold, key=least_sold.get)
least_sold_data = data[:,products.index(least_sold_item)]
plt.plot(least_sold_data)
plt.xlabel('Time (secs)')
plt.ylabel('sales')
plt.title('Seasonality of Least Sold Item')
plt.show()