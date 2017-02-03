class Clock(object):
    HOURS = 24
    MINUTES = 60

    def __init__(self, hours, minutes):
        self.hours = hours + minutes / Clock.MINUTES
        self.minutes = minutes % Clock.MINUTES

    def __str__(self):
        return self.format(Clock.HOURS, self.hours) + ':' + self.format(Clock.MINUTES, self.minutes)

    def format(self, unit_of_time, number_of_units):
        if (number_of_units % unit_of_time) < 10:
            return '0' + str(number_of_units % unit_of_time)
        else:
            return str(number_of_units % unit_of_time)
