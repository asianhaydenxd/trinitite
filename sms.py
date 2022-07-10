from ipaddress import IPv4Address
from pyairmore.request import AirmoreSession
from pyairmore.services.messaging import MessagingService

class Trinitite:
    def __init__(self, phone: str, ip: str):
        self.phone = phone
        self.ip = ip
        self.session = AirmoreSession(self.ip)
        self.service = MessagingService(self.session)
    
    def fetch_msgs(self):
        all_history = self.service.fetch_message_history()
        history = self.service.fetch_chat_history([message for message in all_history if message.phone == self.phone][0])
        return history
    
    def send_msg(self, msg: str):
        self.service.send_message(self.phone, msg)
