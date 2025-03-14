import socket
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python publisher.py <PUBLISHER_ID>")
        return
    pub_id = sys.argv[1]
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', 9000))
    print(f"Publisher {pub_id} connected. Enter messages as <TOPIC> <MESSAGE>")
    try:
        while True:
            inp = input().strip()
            if not inp:
                continue
            parts = inp.split(maxsplit=1)
            if len(parts) < 2:
                print("Format: <TOPIC> <MESSAGE>")
                continue
            topic, message = parts
            sock.send(f"PUBLISH {topic} {message} {pub_id}\n".encode('utf-8'))
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        sock.close()

if __name__ == "__main__":
    main()