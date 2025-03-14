# Publish-Subscribe Messaging System

This project implements a **Publish-Subscribe (Pub-Sub) messaging system** using Python sockets. The system consists of three main components:
- **Broker**: Manages subscriptions and forwards published messages to subscribers.
- **Publisher**: Sends messages to a specific topic.
- **Subscriber**: Receives messages for topics it has subscribed to.

## Quickstart Guide

### Running the Broker
1. Copy all the contents from this repository.
2. Open a terminal and navigate to the folder containing `broker.py`.
3. Start the broker by running:
   ```bash
   python broker.py
   ```
4. The broker will listen on **port 9000** for connections from publishers and subscribers.

### Running a Publisher
1. Open another terminal and navigate to the same folder.
2. Start a publisher instance by running:
   ```bash
   python publisher.py <PUBLISHER_ID>
   ```
3. The publisher can send messages using the format:
   ```
   <TOPIC> <MESSAGE>
   ```

### Running a Subscriber
1. Open another terminal and navigate to the same folder.
2. Start a subscriber instance by running:
   ```bash
   python subscriber.py <SUBSCRIBER_ID>
   ```
3. The subscriber can use the following commands:
   ```
   subscribe <TOPIC>
   unsubscribe <TOPIC>
   ```

## Core Concepts
- **Message Routing**: The broker delivers published messages to all subscribed clients.
- **Topic-Based Filtering**: Messages are categorized by topics, allowing targeted delivery.
- **Real-Time Communication**: Messages are sent instantly between publishers and subscribers.

## Preview of Pub-Sub System

### **Example Usage**
```bash
# Terminal 1 - Start the broker
python broker.py

# Terminal 2 - Start a subscriber
python subscriber.py sub1
> subscribe weather

# Terminal 3 - Start a publisher
python publisher.py pub1
> weather Rainy day ahead!
```

### **Example Output**
```bash
# Subscriber Output
>> DELIVER weather Rainy day ahead! pub1 2025-03-14 10:30:00
```

## Notes:
- Multiple subscribers and publishers can run simultaneously.
- The system is **event-driven**, meaning messages are forwarded as soon as they arrive.
- The broker ensures **message delivery to all active subscribers** of a given topic.

## Future Enhancements
- Implement **message persistence** for disconnected subscribers.
- Add **QoS levels** for guaranteed message delivery.
- Support **distributed brokers** for scalability.

---

