class Interval(object):

    def __init__(self, start, end):
        
        self.start = start
        self.end = end


class MeetingRooms2 (object):

    def minMeetingRooms(self, intervals):

        # Save the start times to a list and sort it
        start = sorted([i.start for i in intervals])
        # Save the end times to a list and sort it
        end = sorted([i.end for i in intervals])

        # Initialize variable to keep track of the max required rooms
        rooms = 0
        # Initialize variable to keep track of the current required rooms
        count = 0
        # Initialize pointers to iterate through the start and end lists
        sPointer = 0
        ePointer = 0

        # Iterate while the start pointer is less than the length of the intervals
        while sPointer < len(intervals):
            # If the start time is less than the end time, increment the count and the start-pointer
            if start[sPointer] < end[ePointer]:
                sPointer += 1
                count += 1
            # If the start time is greater than the end time, decrement the count and the end-pointer
            else:
                ePointer += 1
                count -= 1    

            # Update the max rooms required if needed
            rooms = max(rooms, count)

        # Return the max rooms required
        return rooms
