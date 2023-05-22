from json import JSONDecodeError

from broker import Producer
from protocol import decoder


class BridgeController:

    def __init__(
        self,
        request: 'dict',
        host: 'str', 
        port: 'int', 
        queue: 'str'
    ):
        self._request = request
        self._host = host
        self._port = port
        self._queue = queue 

    def send(self):
        res = None

        try:
            assert decoder.check_message_format(self._request)
            
            Producer(
                host=self._host, 
                port=self._port, 
                queue=self._queue
            ).publish(self._request)

            res = (200, 'OK')

        except (AssertionError, JSONDecodeError):
            res = (400, 'request body outside protocol definition.')

        return res
