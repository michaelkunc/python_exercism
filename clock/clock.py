class Clock(object):

    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def __str__(self):
        return self.format_hours() + ':' + self.format_minutes()

    def format_hours(self):
        if self.hours >= 24:
            return '0' + str(self.hours - 24)
        elif self.hours < 10:
            return '0' + str(self.hours)
        else:
            return str(self.hours)

    def format_minutes(self):
        if self.minutes < 10:
            return '0' + str(self.minutes)
        else:
            return (str.self.minutes)
