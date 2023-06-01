import random


class Time:
    """A class that represents time in the format HH:MM"""

    def __init__(self, hour, minute):
        self.hour = int(hour)
        self.minute = int(minute)

    def __lt__(self, other):
        """Compare two times based on their hour and minute"""
        """ return True if self < other, and False otherwise"""
        if self.hour < other.hour:
            return True
        elif self.hour == other.hour and self.minute < other.minute:
            return True
        else:
            return False

    def __eq__(self, other):
        """Compare two times based on their hour and minute"""
        """ return True if self == other, and False otherwise"""
        if self.hour == other.hour and self.minute == other.minute:
            return True
        else:
            return False

    def __repr__(self):
        """Return the string representation of the time"""
        return f"{self.hour:02d}:{self.minute:02d}"


class Entry:
    """A class that represents a customer in the waitlist"""

    def __init__(self, name, time):
        self.name = name
        self.time = time

    def __lt__(self, other):
        """Compare two customers based on their time, if equal then compare based on the customer name"""
        if self.time == other.time:
            return self.name < other.name
        return self.time < other.time


class Waitlist:
    def __init__(self):
        self._entries = []

    def add_customer(self, name, reservation_time):
        if not self._entries:
            self._entries.append(
                Entry(name, Time(reservation_time[:2], reservation_time[3:])))
        else:
            self._entries.append(
                Entry(name, Time(reservation_time[:2], reservation_time[3:])))
            self._entries.sort()

    def peek(self):
        if not self._entries:
            return (None, None)
        else:
            return (str(self._entries[0].name), str(self._entries[0].time))

    def seat_customer(self):
        customer = self.peek()
        if customer[0] is None:
            return None
        else:
            self._entries.pop(0)
            return customer

    def print_reservation_list(self):
        lst = []
        if not self._entries:
            return 'No reservations currently.'
        else:
            for i in self._entries:
                lst.append((i.name, repr(i.time)))
            return lst

    def change_reservation(self, name, new_reservation_time):
        if not self._entries:
            return 'No reservations currently.'
        for reservation in self._entries:
            if reservation.name == name:
                reservation.time = Time(
                    new_reservation_time[:2], new_reservation_time[3:])
                self._entries.sort()
                return f"{reservation.name}'s reservation time has been changed to {repr(reservation.time)}"
        return "No reservations made under that name."
