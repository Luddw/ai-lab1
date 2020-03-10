from telegram import Telegram

class EntityManager:
    def __init__(self, tick_size):
        self.entities = {}
        self.current_ticks = 0
        self.message_q = []
        
    def add_entity(self, entity):
        self.entities[entity.ID] = entity
        entity.manager = self
    
    def add_entity_dict(self, entities):
        for ent in entities:
            self.entities[ent.ID] = ent
            ent.manager = self
        
    def update(self, tick_size):
        for i in self.entities:
            self.current_ticks += tick_size
            self.discharge_delayed()
            self.entities[i].update(tick_size)
    
    def get_agent_from_id(self, agent_id):
        return self.entities.get(agent_id, None)
    
    def discharge(self, telegram):
        receiver = self.get_agent_from_id(telegram.receiver)
        receiver.handle_message(telegram)

    def discharge_delayed(self):
        for msg in self.message_q:
            if self.current_ticks >= msg.tick_delay:
                self.discharge(msg)
                self.message_q.remove(msg)

    def dispatch_message(self, telegram, tick_delay=0):
        if telegram.receiver is None:
            for agent in self.entities.values():
                if agent == telegram.sender:
                    continue
                unicast = Telegram(telegram.sender, agent.ID, telegram.message_type, telegram.extra_info)
                self.dispatch_message(unicast, tick_delay)
            return
        # check if message has delay
        if tick_delay > 0:
            telegram.tick_delay = self.current_ticks + tick_delay
            self.message_q.append(telegram)
        else:
            self.discharge(telegram)


