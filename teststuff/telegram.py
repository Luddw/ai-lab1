class Telegram:
    def __init__(self, sender, receiver, message_type, step_delay, extra_info):
        self.sender = sender,
        self.receiver = receiver
        self.message_type = message_type
        self.step_delay = step_delay
        self.extra_info = extra_info