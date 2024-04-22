import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from problems.MeetingRooms2.MeetingRooms2 import Interval, MeetingRooms2

def test_meeting_rooms():
    meeting_rooms_instance = MeetingRooms2()

    # Test case 1
    interval1 = Interval(0,40)
    interval2 = Interval(5,10)
    interval3 = Interval(15,20)
    expected = 2
    assert meeting_rooms_instance.minMeetingRooms([interval1, interval2, interval3]) == expected

    # Test case 2
    interval1 = Interval(4,9)
    expected = 1
    assert meeting_rooms_instance.minMeetingRooms([interval1]) == expected

    # Test case 3
    interval1 = Interval(1,5)
    interval2 = Interval(2,6)
    interval3 = Interval(3,7)
    interval4 = Interval(4,8)
    interval5 = Interval(5,9)
    expected = 4
    assert meeting_rooms_instance.minMeetingRooms([interval1, interval2, interval3, interval4, interval5]) == expected
