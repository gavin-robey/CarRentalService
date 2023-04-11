from datetime import datetime, timedelta
from calendar import HTMLCalendar
from reservation.models import Reservation

class Calendar(HTMLCalendar):
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(Calendar, self).__init__()
    

    def formatday(self, day, events):
        events_per_day = events.filter(startDate__month__lt=self.month, endDate__day__gte=day)
        events_per_day_x = events.filter(endDate__month__gt=self.month, startDate__day__lte=day)
        events_per_day_y = events.filter(startDate__month=self.month, endDate__month=self.month, startDate__day__lte=day, endDate__day__gte=day)
        d = ''
        color = "#2A2D3E"
        textColor = "#C6C6CA"
        for event in events_per_day:
            color = "#2b2332"
            textColor = "#632032"
        
        for event in events_per_day_x:
            color = '#2b2332'
            textColor = "#632032"

        for event in events_per_day_y:
            color = '#2b2332'
            textColor = "#632032"
        
        if day != 0:
            return f"<td><span class='date' style='background-color: {color}; color: {textColor}'>{day}</td>"
        
        return '<td></td>'
    
    def formatweek(self, theweek, events):
        week = ''
        for d, weekday in theweek:
            week += self.formatday(d, events)
        return f'<tr> {week} </tr>'
    
    def formatmonth(self, vehicle_id, addMonths, withyear=True):
        self.month = correct_month(addMonths)
        events = Reservation.objects.filter(carId=vehicle_id)
        events = events.filter(startDate__year__lte=self.year, startDate__month__lte=self.month)
        events = events.filter(endDate__year__gte=self.year, endDate__month__gte=self.month)
        
        cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar" id="{self.month}" style="display: none;">\n'
        cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        cal += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.formatweek(week, events)}\n'
        return cal
    
def correct_month(month):
    while month > 12:
        month -= 12
    return month