class InsertInterval (object):

    def insert(self, intervals, newInterval):

        # Initialize the result list
        result = []

        # Iterate through the intervals
        for i in range(len(intervals)):
            # If the end time of the new interval is less than the start time of the current interval
            if newInterval[1] < intervals[i][0]:
                # Append the new interval to the result list
                result.append(newInterval)
                # Return the result list with the current interval and the remaining intervals
                return result + intervals[i:]
            # If the start time of the new interval is greater than the end time of the current interval
            elif newInterval[0] > intervals[i][1]:
                # Append the current interval to the result list
                result.append(intervals[i])
            # If the new interval overlaps with the current interval
            else:
                # Update the new interval with the minimum start time and the maximum end time
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]

        # Append the new interval to the result list
        result.append(newInterval)

        # Return the result list
        return result
