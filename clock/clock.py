class Clock(object):

    def __init__(self, hours, minutes):
        self.hours = hours + self.minutes_roll_over(minutes)[0]
        self.minutes = minutes

    def __str__(self):
        return self.format_hours() + ':' + self.format_minutes()

    def format_hours(self):
        if self.hours > 23:
            return '0' + str(divmod(self.hours, 24)[1])
        elif self.hours < 10:
            return '0' + str(self.hours)
        else:
            return str(self.hours)

    def format_minutes(self):
        if self.minutes > 59:
            return '00'
        elif self.minutes < 10:
            return '0' + str(self.minutes)
        else:
            return str(self.minutes)

    def minutes_roll_over(self, minutes):
        return divmod(minutes, 60)
