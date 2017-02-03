class Clock(object):

    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def __str__(self):
        return self.format_hours() + ':' + self.format_minutes()

    def format_hours(self):
        if self.hours > 23:
            return '0' + str(divmod(self.hours, 24)[1])
        else:
            return self.greater_than_10(self.hours)

    def format_minutes(self):
        if self.minutes > 59:
            return '00'
        else:
            return self.greater_than_10(self.minutes)

    def greater_than_10(self, unit_of_time):
        if unit_of_time < 10:
            return '0' + str(unit_of_time)
        else:
            return str(unit_of_time)
