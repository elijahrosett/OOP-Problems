from hashlib import new


class Alarm:
    def __init__(self):
        self.current_time = 1200
        self.on_or_off = ""
        self.alarm_set_time = 1200

    def change_current_time(self, new_time):
        self.current_time = new_time
        print(f"The new time is {new_time}.")

    def change_on_or_off(self, on_or_off):
        self.on_or_off = on_or_off
        print(f"The alarm is now {on_or_off}.")

    def set_alarm_time(self, time):
        self.alarm_set_time = time
        print(f"The alarm is set to go off at {time}.")
