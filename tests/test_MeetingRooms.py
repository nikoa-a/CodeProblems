import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from problems.MeetingRooms.MeetingRooms import Interval, MeetingRooms

def test_meeting_rooms():
    meeting_rooms_instance = MeetingRooms()

    # Test case 1
    interval1 = Interval(0,30)
    interval2 = Interval(5,10)
    interval3 = Interval(15,20)
    expected = False
    assert meeting_rooms_instance.canAttendMeetings([interval1, interval2, interval3]) == expected

    # Test case 2
    interval1 = Interval(5,8)
    interval2 = Interval(9,15)
    expected = True
    assert meeting_rooms_instance.canAttendMeetings([interval1, interval2]) == expected
