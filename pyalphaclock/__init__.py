import calendar
import datetime
import serial
import time

def pad_string(s, length=5, align='right'):
    s = s[:length]
    while len(s) < length:
        if align == 'left':
            s += ' '
        else:
            s = ' ' + s
    return str(s).upper()

def substr(s, start, end):
    spaces_before = ' ' * (0-start)
    spaces_after = ' ' * (end-len(s))
    return spaces_before + s[max(0,start):end] + spaces_after

class AlphaClock(object):
    def __init__(self, path='/dev/tty.usbserial-AE015K9Z'):
        self.serial = serial.Serial(path, 19200)
    
    def clear_screen(self):
        """
        Clears the clock screen.
        """
        self.serial.write('\xffA0' + " "*5 + "0"*5)

    def display_text(self, s, align='right'):
        """
        Display the provided string in the clock.
        Only the first 5 characters of the provided string are considered.
        
        If the string has length less than 5, then the 'align' keyword argument
        determines whether it will be aligned to the left or to the right when displayed.
        """
        to_display = pad_string(s, align=align)
        self.serial.write('\xffA0' + to_display + "0"*5)
        
    def display_scrolling_text(self, s, delay=0.5):
        """
        Display text that's longer than 5 characters by scrolling through it.
        You can specify the delay between every subsequent character with the 'delay' keyword argument. 
        """
        for i in range(-4, len(s)):
            self.display_text(substr(s, i, i+5))
            time.sleep(delay)

    def display_date(self, d):
        """
        Display the month and day from a datetime object provided (e.g. 'FEB23')"
        """
        to_display = d.strftime("%b%d").upper()
        self.serial.write('\xffA0' + to_display + "00100")

    def display_time(self, d):
        """
        Display the hour and minute from a datetime object provided (e.g. '12:52')"
        """
        unixtime = time.mktime(d.timetuple())
        unixtime = calendar.timegm(d.utctimetuple())
        self.serial.write('\xffMT' + " "*10)
        self.serial.write('\xffST' + str(int(unixtime)))
