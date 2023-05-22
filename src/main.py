#!/usr/bin/env python3

from flask import Flask, request

from controller import BridgeController
from utils.config import configure_from_file


CONFIG_FILE = "../config.ini"


conf = configure_from_file(CONFIG_FILE)

app = Flask(__name__)


@app.get('/control')
def send_to_control_bridge():
    req = request.json
    
    res = BridgeController(
        request=req,
        host=conf['baddr'],
        port=conf['bport'],
        queue=conf['bqueue']
    ).send()

    return res


app.run(
    host=conf['addr'],
    port=conf['port']
)
