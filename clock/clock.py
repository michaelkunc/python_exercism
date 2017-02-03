class Clock(object):

    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def __str__(self):
        hours = self.hours + self.minutes / 60
        minutes = self.minutes % 60
        return self.format_hours(hours) + ':' + self.format_minutes(minutes)

    def format_hours(self, hour):
        if hour > 23:
            return '0' + str(hour % 24)
        else:
            return self.less_than_10(hour)

    def format_minutes(self, minutes):
        if minutes > 59:
            return '00'
        else:
            return self.less_than_10(minutes)

    def less_than_10(self, unit_of_time):
        if unit_of_time < 10:
            return '0' + str(unit_of_time)
        else:
            return str(unit_of_time)
