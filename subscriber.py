import redis

# Especifica los detalles de la conexión
hostname = 'redis-18722.c74.us-east-1-4.ec2.redns.redis-cloud.com'
port = 18722
password = 'r8iZjmnGFfOZldE6gREBcjtaRoJ4ofx4'

# Conectar a Redis
r = redis.Redis(host=hostname, port=port, password=password)

def message_handler(message):
    print(f"Received: {message['data'].decode('utf-8')}")

def subscribe_to_channel():
    pubsub = r.pubsub()
    pubsub.subscribe(**{'my-channel': message_handler})
    print("Subscribed to 'my-channel'. Waiting for messages...")
    pubsub.run_in_thread(sleep_time=1)

if __name__ == "__main__":
    subscribe_to_channel()
