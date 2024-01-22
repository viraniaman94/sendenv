import json
from twisted.internet import reactor, defer
from wormhole import create
from wormhole.cli.public_relay import MAILBOX_RELAY

@defer.inlineCallbacks
def send_vault():
    # Create a wormhole
    w = yield create("magicenv.dev", MAILBOX_RELAY, reactor)
    w.allocate_code()

    code = yield w.get_code()
    print(f"code: {code}")

    data = {
        "vault": "test",
        "variables": ["test1", "test2"]
    }

    yield w.send_message(json.dumps(data).encode('utf-8'))

    # Wait for an acknowledgement from the receiver
    ack = yield w.get_message()
    print(f"Acknowledgement received: {ack}")

    yield w.close()

reactor.callWhenRunning(send_vault)
reactor.run()