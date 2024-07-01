import redis

# Especifica los detalles de la conexión
hostname = 'redis-18722.c74.us-east-1-4.ec2.redns.redis-cloud.com'
port = 18722
password = 'r8iZjmnGFfOZldE6gREBcjtaRoJ4ofx4'

# Conectar a Redis
r = redis.Redis(host=hostname, port=port, password=password)

def publish_messages():
    while True:
        message = input("Enter message to publish: ")
        r.publish('my-channel', message)
        print(f"Published: {message}")

if __name__ == "__main__":
    publish_messages()
