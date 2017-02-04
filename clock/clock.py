class Clock(object):
    HOURS = 24
    MINUTES = 60

    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def __str__(self):
        self.roll_over()
        return self.format(Clock.HOURS, self.hours) + ':' + self.format(Clock.MINUTES, self.minutes)

    def format(self, unit_of_time, number_of_units):
        if (number_of_units % unit_of_time) < 10:
            return '0' + str(number_of_units % unit_of_time)
        else:
            return str(number_of_units % unit_of_time)

    def roll_over(self):
        self.hours = self.hours + self.minutes / Clock.MINUTES
        self.minutes = self.minutes % Clock.MINUTES
        return self

    def add(self, additional_minutes):
        self.minutes = self.minutes + additional_minutes
        return self
