# checkin_timeline.py

class DataError(Exception):
    """An Exception class raised by CheckInTimeline.

    Bases: Exception

    -This exception is raised whenever a CheckInTimeline detects 
    a semantic error with its CheckIns.
    """
    pass

class CheckInTimeline:
    """A timeline of check-ins.

    -Represents a timeline of recorded check-ins: ordered chronologically
    from least recent to most recent. 

    -Instances have one member variable:
        checkins: a list that stores the sequence of CheckIn instances.
        Note that this list will always be sorted by check-in time,
        provided that the CheckInTimeline.add() method is used to add
        new CheckIns.
    """

    def __init__(self):
        """Constructor

        Initializes a CheckInTimeline.
        """
        pass

    def add(self, checkin):
        """

        Adds a CheckIn to the timeline of check-ins.

        -When the check-in is added, the timeline of check-ins is sorted
        by time stamp to ensure that they remain in order: from least recent
        to most recent.

        :param CheckIn checkin: The CheckIn to add.

        :returns: None
        """
        pass

    def windows(self, window_size=datetime.timedelta(0,3600))
        """A generator for iterating over windows of a given size.

        -Iterates over the timeline's collection of CheckIns, yielding
        tuples of CheckIns that occurred within a timedelta of window_size
        after the first check-in in the window.

        :param datetime.timedelta window_size: The size of the window
        for looking into the future. Defaults to one hour (3600 seconds).

        :returns: An iterable that yields tuples of CheckIns that occurred
        within time delta of window_size from teh first Check-In in the
        tuple. The size of the tuple will vary depending on the size of
        the window.

        :rtype: iterable
        """
        pass

    def rendezvous(self, window_size=datetime.timedelta(0, 3600))
        """A generator for chronologically iterating over rendezvous.
        
        -Iterates over windows (of duration window_size) to determine
        which of those windows contain a rendezvous. We dect a rendezvous
        for a window by checking whether the first check-in in the window
        shares a location with any other check-ins in the window.

        :param datetime.timedelta window_size: -The size of the window for
        looking into the future. Defaults to one hour (3600 seconds).

        :returns: An iterable that yields pairs of CheckIn. Each pair
        corresponds to two agents who met at the same location within
        window_size of one antother. Pairs are tuples, and each will
        have exactly two items.
        
        :rtype: iterable
        
        :raises DataError: If we detect a rendezvous has more than two 
        members, a DataError is raised. Something must be wrong with the
        input data. 
        """
        pass