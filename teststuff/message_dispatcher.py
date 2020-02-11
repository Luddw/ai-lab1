import datetime
from entity_manager import EntityManager
from telegram import Telegram
from message_types import message_type_to_string


class MessageDispatcher:

    def discharge(self, receiver, telegram):
        receiver.handle_message(telegram)

    def dispatch_message(self, telegram, tick_delay=0):
        agent = EntityManager.g
        if telegram.receiver is None:
            print('No receipient')
            return
        # check if message has delay
        if tick_delay <= 0:
            print('Instant telegram dispatched at time: {} by {} for {} and message is: {}'.format(
                    datetime.datetime.now(),
                    telegram.sender.id,
                    telegram.receiver.id,
                    message_type_to_string(telegram.message_type))
                )

            self.discharge(telegram.receiver, telegram)
