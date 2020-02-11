class Telegram:
    def __init__(self, sender, receiver, message_type, extra_info=None):
        self.sender = sender,
        self.receiver = receiver
        self.message_type = message_type
        self.step_delay = 0
        self.extra_info = extra_info