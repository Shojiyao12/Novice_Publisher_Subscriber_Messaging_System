import socket
import threading
from datetime import datetime

topics = {}  # {topic_name: set(subscriber_ids)}
subscriber_sockets = {}  # {subscriber_id: socket}
topics_lock = threading.Lock()
subscriber_sockets_lock = threading.Lock()

def handle_client(client_socket):
    try:
        while True:
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break
            commands = data.strip().split('\n')
            for cmd in commands:
                parts = cmd.strip().split()
                if not parts:
                    continue
                command = parts[0]
                if command == 'SUBSCRIBE':
                    if len(parts) != 3:
                        continue
                    topic = parts[1]
                    subscriber_id = parts[2]
                    with topics_lock:
                        if topic not in topics:
                            topics[topic] = set()
                        topics[topic].add(subscriber_id)
                    with subscriber_sockets_lock:
                        subscriber_sockets[subscriber_id] = client_socket
                    print(f"{subscriber_id} subscribed to {topic}")
                elif command == 'UNSUBSCRIBE':
                    if len(parts) != 3:
                        continue
                    topic = parts[1]
                    subscriber_id = parts[2]
                    with topics_lock:
                        if topic in topics:
                            topics[topic].discard(subscriber_id)
                            if not topics[topic]:
                                del topics[topic]
                    print(f"{subscriber_id} unsubscribed from {topic}")
                elif command == 'PUBLISH':
                    if len(parts) < 4:
                        continue
                    topic = parts[1]
                    publisher_id = parts[-1]
                    message = ' '.join(parts[2:-1])
                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    deliver_msg = f"DELIVER {topic} {message} {publisher_id} {timestamp}\n"
                    with topics_lock:
                        subscribers = topics.get(topic, set()).copy()
                    for sub_id in subscribers:
                        with subscriber_sockets_lock:
                            sub_socket = subscriber_sockets.get(sub_id)
                        if sub_socket:
                            try:
                                sub_socket.send(deliver_msg.encode('utf-8'))
                            except:
                                pass
                    print(f"Message published to {topic} by {publisher_id}")
    except:
        pass
    finally:
        client_socket.close()

def main():
    broker = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    broker.bind(('localhost', 9000))
    broker.listen(5)
    print("Broker running on port 9000...")
    while True:
        client_socket, addr = broker.accept()
        print(f"Connected: {addr}")
        threading.Thread(target=handle_client, args=(client_socket,)).start()

if __name__ == "__main__":
    main()