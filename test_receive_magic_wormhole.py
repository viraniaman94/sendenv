import json
from twisted.internet import reactor, defer
from wormhole import create
from wormhole.cli.public_relay import MAILBOX_RELAY

@defer.inlineCallbacks
def receive_vault():
    # Create a wormhole
    w = yield create("magicenv.dev", MAILBOX_RELAY, reactor)

    # Set the code for the wormhole
    print("Enter the code: ")
    code = input()
    yield w.set_code(code)

    # Receive the message
    message = yield w.get_message()
    data = json.loads(message.decode('utf-8'))
    print(f"Received data: {data}")

    # Send an acknowledgement back to the sender
    yield w.send_message(b"Received")

    # Close the wormhole
    yield w.close()

# Run the function
reactor.callWhenRunning(receive_vault)
reactor.run()
