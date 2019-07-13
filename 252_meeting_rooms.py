def canAttendMeetings(self, intervals):
    def get_1(time):
        return int(time.start)
    intervals.sort(key=get_1)
    for i in range(len(intervals)-1):
        if intervals[i].end > intervals[i+1].start:
            return False
    return True