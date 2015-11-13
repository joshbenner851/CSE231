class Time(object):
    pass

    def __init__(self,hours=0,minutes=0,seconds=0):
        '''initializes an instance of clock with sent or default values'''
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    def __repr__(self):
        '''return string in that says "Clock Time hh:mm:ss"      '''
        str1 = "Clock Time " + "{:02d}:{:02d}:{:02d}".format(self.hours,self.minutes,self.seconds)
        return str1
    def __str__(self):
        '''return string of time in format hh:mm:ss'''
        str1 = "{:02d}:{:02d}:{:02d}".format(self.hours,self.minutes,self.seconds)
        return str1
    def from_str(self,str1):
        '''update time obj after created'''
        time = str1.split()
        self.hours += time[0]
        self.minutes += time[1]
        self.seconds += time[2]
        
