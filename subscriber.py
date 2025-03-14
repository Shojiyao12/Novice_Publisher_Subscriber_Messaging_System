import socket
import threading
import sys

def receive_messages(sock):
    try:
        while True:
            data = sock.recv(1024).decode('utf-8')
            if not data:
                break
            for line in data.strip().split('\n'):
                print(f">> {line}")
    except:
        pass

def main():
    if len(sys.argv) != 2:
        print("Usage: python subscriber.py <SUBSCRIBER_ID>")
        return
    sub_id = sys.argv[1]
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', 9000))
    print(f"Subscriber {sub_id} connected. Commands: subscribe <TOPIC>, unsubscribe <TOPIC>")
    threading.Thread(target=receive_messages, args=(sock,), daemon=True).start()
    try:
        while True:
            cmd = input().strip()
            if not cmd:
                continue
            action, *rest = cmd.split()
            if action.lower() == 'subscribe' and len(rest) == 1:
                topic = rest[0]
                sock.send(f"SUBSCRIBE {topic} {sub_id}\n".encode('utf-8'))
            elif action.lower() == 'unsubscribe' and len(rest) == 1:
                topic = rest[0]
                sock.send(f"UNSUBSCRIBE {topic} {sub_id}\n".encode('utf-8'))
            else:
                print("Invalid command. Use: subscribe <TOPIC> or unsubscribe <TOPIC>")
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        sock.close()

if __name__ == "__main__":
    main()