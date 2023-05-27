class GreetingCard:
    def __init__(self, recipient="Dana Ev", sender="Eyal Ch"):
        self._sender = sender
        self._recipient = recipient

    def greeting_msg(self):
        print("This card was sent by " + self._sender + " to " + self._recipient)


if __name__ == "__main__":
    pass
