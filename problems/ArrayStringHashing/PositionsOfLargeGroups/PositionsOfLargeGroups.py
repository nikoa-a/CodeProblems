class PositionOfLargeGroups:

    def largeGroupPositions(self, s):

        start, end = 0, 0
        groups = []

        for i in range(len(s) - 1):
            if s[i] == s[i+1]:
                end = i+1
            else:
                if end - start >= 2:
                    groups.append([start, end])
                start = i+1

        # Edge case when list ends with a group
        if end - start >= 2:
            groups.append([start, end])

        return groups