# checkin.py

class CheckIn(name, pokeball, location, time):
    """A check-in of a Team Rocket Delivery agent at a specific
    location/time.

    -Represents a row of the check-ins spreadsheet.

    :param str name: Stores the name of the Team Rocket Delivery Agent
    :param Pokeball pokeball: Reflects the type of Pokeball carried by agent
    :param str location: Stores the name of location where agent checked in
    :param datetime.datetime time: Stores time at which agent checked in
    """

    def __init__(self, name, pokeball, location, time):
        """Constructor

        :param str name: The name of the agent who's checking in
        :param Pokeball pokeball: represents type of Pokeball carried
        :param str location: The location where the agent checked in
        :param str time: The time that the agent checked in.

        :raises ValueError: If a datetime.datetime could not be created
        using the time parameter. Note that datetime.strptime throws
        this error.
        """
        self.name = name
        self.pokeball = pokeball
        self.location = location
        self.time = time

    def __lt__(self, other):
        """Overloaded < operator.
        
        -Returns True if this object's time member variable is less than
        other's time. 

        :param CheckIn other: The check-in we're comparing against. 

        :returns: True if this object's time is less than the other's time. 
        :rtype: bool
        """
        return self.time < other.time

    def __le__(self, other):
        """Overloaded <= operator. 

        -Returns True if this object's time member variable is less than or
        equal to the other's time.

        :param CheckIn other: The check-in we're comparing against. 

        :returns: True if this object's time is less than or equal to 
        the other's time. 

        :rtype: bool
        """
        return self.time <= other.time

    def __gt__(self, other):
        """Overloaded > operator. 

        -Returns True if this object's time member variable is greater than
        the other's time.

        :param CheckIn other: The check-in we're comparing against. 

        :returns: True if this object's time is greater than the other's time.

        :rtype: bool
        """
        return self.time > other.time

    def __ge__(self, other):
        """Overloaded >= operator. 

        -Returns True if this object's time member variable is greater than
        or equal to the other's time.

        :param CheckIn other: The check-in we're comparing against. 

        :returns: True if this object's time is greater than or equal to 
        the other's time. 

        :rtype: bool
        """
        return self.time >= other.time 

    def __str__(self):
        """ 
        -Called by str() to turn a CheckIn into a str. 

        :returns: This CheckIn as a str.

        :rtype: str
        """
        output = ("{1} at {2} with a/an {3} ({4})")
            .format(self.name, self.location, self.pokeball, self.time)

        return output
