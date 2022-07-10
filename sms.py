from ipaddress import IPv4Address
from pyairmore.request import AirmoreSession
from pyairmore.services.messaging import MessagingService

class Trinitite:
    def __init__(self, phone: str, ip: str):
        self.phone = phone
        self.ip = ip
        self.session = AirmoreSession(self.ip)
        self.service = MessagingService(self.session)
        self.fetched = []
        self.fetch_msgs()
    
    def fetch_msgs(self):
        all_history = self.service.fetch_message_history()
        history = self.service.fetch_chat_history([message for message in all_history if message.phone in (self.phone, "+1" + self.phone)][0])
        new_messages = []
        for message in reversed(history):
            if message not in self.fetched:
                new_messages.append(message)
        self.fetched = new_messages + self.fetched
        return new_messages
    
    def send_msg(self, msg: str):
        self.service.send_message(self.phone, msg)
