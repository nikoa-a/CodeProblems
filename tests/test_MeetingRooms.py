import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from problems.MeetingRooms.MeetingRooms import MeetingRooms

def test_meeting_rooms():
    meeting_rooms_instance = MeetingRooms()

    # Test case 1
    intervals = [(0,30),(5,10),(15,20)]
    expected = False
    assert meeting_rooms_instance.canAttendMeetings(intervals) == expected

    # Test case 2
    intervals = [(5,8),(9,15)]
    expected = True
    assert meeting_rooms_instance.canAttendMeetings(intervals) == expected
