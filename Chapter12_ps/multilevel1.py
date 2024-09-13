
class Message:

    def send(self):
        print("Sending message...")

class Email(Message):

    def sendmail(self):
        print("Sending email...")

class SMS(Message):
    def send_sms(self):
        super().send()
        print("Sending SMS...")


m1 = SMS()
m1.send_sms()