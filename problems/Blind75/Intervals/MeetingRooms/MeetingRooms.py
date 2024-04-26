class Interval(object):

    def __init__(self, start, end):

        self.start = start
        self.end = end


class MeetingRooms (object):

    def canAttendMeetings(self, intervals):

        # Sort the intervals by start time
        intervals.sort(key = lambda i : i.start)

        # Iterate through the intervals starting from the second one
        for i in range(1, len(intervals)):
            # If the start time of the current interval is less than the end time of the previous interval, return False
            if intervals[i].start < intervals[i-1].end:
                return False

        # If no overlapping intervals are found, return True
        return True
