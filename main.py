def add_time(starts, durations, day=None):
#   new_time =""
  # tach phan tu
  start = starts.split() 
  print(start)
  print(start[0])
  print(start[1])

  h = start[0].split(":") 
  print(h)
  duration = durations.split(":") 
  print(duration)
  #kieemr tra so
  try: 
    h[0]=int(h[0]) 
    h[1]=int(h[1]) 
    duration[0]=int(duration[0]) 
    duration[1]=int(duration[1]) 
  except: return("Error: must be number") 
  
# kieemr tra phut <60
  if h[1]>=60: 
    return("Error: munite must be smaller than 60") 
#tinh tong phut, gio
  a=h[0]+ duration[0] 
  b=h[1]+duration[1] 
# neeus phuts nho hown 60

  if b<60: 
      phut = b 
      #xacdinh gio
      if a>24: 
        gio = a%24 
        day= (a-a%24)/24 
        #xac dinh am/pm
        if gio >12: 
          start[1]="PM" 
        elif gio<12: 
          start[1]="AM" 
      elif a<24: 
        gio= a 
        if gio > 12: 
            start[1]="PM" 
      elif gio < 12: 
        start[1]="AM" 
    # phut >60
  elif b>60: 
        phut = b%60 
        a=a+(b-b%60)/60 
        # xacdinhgio
        if a<24: 
          gio = a
          if a>12: 
            start[1]= "PM" 
          elif a<12: 
            start[1]="AM" 
        elif a>24: 
            gio = a%24 
            day= (a-a%24)/24 
            if gio >12: 
              start[1]="PM" 
            elif gio <12: 
              start[1]="AM" 
        new_time= gio+":"+ phut
        day = int(day)
  if not day == None:
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    pos = 0
    while True:
      if day.lower() == days[pos].lower():
        break
      pos= pos + 1
    newDay = days[((pos + (days % 7)) % 7)]
    new_time = new_time + ", " + newDay

  #Final output
  if day == 1:
    new_time = new_time + " (next day)"
  elif day > 1:
    days = str(days)
    new_time = new_time + " (" + days + " days later)"

  return new_time
add_time("2:30 AM","3:30")
         




