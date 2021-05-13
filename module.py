

import datetime 
daysOftheWeek = ("ISO Week days start from 1",

                "Monday",

                "Tuesday",

                "Wednesday",

                "Thursday",

                "Friday",

                "Saturday",

                "Sunday"

                )
a = datetime.date(2021,12,24)
ti = a.isoweekday()
print("Christmas Eve this year falls on  {}" .format(daysOftheWeek[ti]))

 