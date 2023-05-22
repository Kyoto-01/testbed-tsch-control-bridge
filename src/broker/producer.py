import pika
import json


class Producer:

    def __init__(
        self,
        host: 'str',
        port: 'int', 
        queue: 'str'
    ):
        self._parameters = pika.ConnectionParameters(
            host=host,
            port=port
        )

        self._connection = pika.BlockingConnection(self._parameters)

        self._channel = self._connection.channel()
        self._queue = queue

        self._setup()

    def _setup(self):
        self._channel.queue_declare(
            queue=self._queue, 
            auto_delete=True
        )

    def publish(self, msg):
        msg = json.dumps(msg)

        self._channel.basic_publish(
            exchange='',
            routing_key=self._queue,
            body=msg
        )

    def close(self):
        self._channel.close()
