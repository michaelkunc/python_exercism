class Clock(object):
    HOURS = 24
    MINUTES = 60

    def __init__(self, hours, minutes):
        self.minutes = (hours * Clock.MINUTES) + minutes

    def __repr__(self):
        hours, minutes = self.hours_minutes(self.minutes)
        return '{:02}:{:02}'.format(hours, minutes)

    def hours_minutes(self, minutes):
        hours, minutes = divmod(minutes, Clock.MINUTES)
        hours = hours % Clock.HOURS
        return hours, minutes

    def add(self, additional_minutes):
        self.minutes = self.minutes + additional_minutes
        return self

    def __eq__(self, other):
        return str(self) == str(other)
