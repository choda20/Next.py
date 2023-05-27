import file1


class BirthdayCard(file1.GreetingCard):
    def __init__(self, recipient="Dana Ev", sender="Eyal Ch", sender_age=0):
        self._sender_age = sender_age
        super().__init__(recipient, sender)

    def greeting_msg(self):
        print("Happy Birthday " + self._recipient + " from " + str(self._sender_age) + " year old " + self._sender)


if __name__ == "__main__":
    pass