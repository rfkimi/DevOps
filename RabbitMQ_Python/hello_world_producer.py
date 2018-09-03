import pika
import sys

# build connection to server
credentials = pika.PlainCredentials("guest", "guest")
conn_params = pika.ConnectionParameters("localhost",
                                        credentials=credentials)
conn_broker = pika.BlockingConnection(conn_params)

channel = conn_broker.channel()

channel.confirm_delivery()
# create text message
msg = sys.argv[1]
msg_props = pika.BasicProperties()
msg_props.content_type = "text/plain"
msg_ids = []
# publish message
ack = channel.basic_publish(body=msg,
                            exchange="hello-exchange",
                            properties=msg_props,
                            routing_key="hola")
if ack:
    print "put message to rabbitmq successed!"
else:
    print "put message to rabbitmq failed"


msg_ids.append(len(msg_ids)+1)
channel.close()
