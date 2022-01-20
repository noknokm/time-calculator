def add_time(start, duration, day= None):
    S = start.split(" ")
    startTime = S[0].split(":")
    sHour = int(startTime[0])
    x = sHour
    sMin = int(startTime[1])
    
    timeOfDay = S[1]
    
    D = duration.split(":")
    dHour = int(D[0])
    dMin = int(D[1])
    
    #convert to 24 hour format
    if timeOfDay == "PM":
        sHour += 12
    elif timeOfDay =="AM":
        sHour += 0
    
    n = 0    
    #convert duration into minutes and add to start minutes
    dMins = dMin + (dHour * 60)
    mins = sMin + dMins
    
    #convert minutes into final minutes
    finalMins = mins % 60
    h = mins // 60
    
    #convert hours into final hours

    add = sHour + h
    remainder = h % 24
    finalHours = remainder + sHour

    if finalHours > 24:
        finalHours -= 24
    else:
        finalHours = remainder + sHour
            
    if add > 24:
        n += (add // 24)
            

    
    minutes = ""
    #convert back to 12 hour format
    
    if finalMins < 10:
        minutes += "0" + str(finalMins)
        
    else:
        minutes = str(finalMins)
        
    finalTime = ""   
    if finalHours == 24:
        finalHours -= 12
        timeOfDay = "AM"
        finalTime += str(finalHours) + ":" + minutes + " " + timeOfDay
    
        
    elif finalHours == 12:
        timeOfDay = "PM"
        finalTime += str(finalHours) + ":" + minutes + " " + timeOfDay
        
    elif finalHours > 12:
        if finalHours < 24:
            finalHours -= 12
            timeOfDay = "PM"
            finalTime += str(finalHours) + ":" + minutes + " " + timeOfDay
            
    elif finalHours < 12:
        timeOfDay = "AM"
        finalTime += str(finalHours) + ":" + minutes + " " + timeOfDay  
    
       
    if day == None:
        if n == 0:
            return finalTime
        if n == 1:
            days = "(next day)"
            finalTime += " " + days
            return finalTime
        if n > 1:
            days = "(" + str(n) + " days later)"
            finalTime += " " + days
            return finalTime
   
    if not day == None:
        weekDays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        i = 0
        while not day == None:
            if day.lower() == weekDays[i].lower():
                break
            i += 1
        index = i + (n % 7)
        index %= 7
        newDay = weekDays[index]
        finalTime += ", " + newDay
        if n == 0:
            return finalTime
        if n == 1:
            daysLater = "(next day)"
            finalTime = finalTime + " " + daysLater
            return finalTime
        if n > 1:
            daysLater = "(" + str(n) + " days later)"
            finalTime = finalTime + " " + daysLater
            return finalTime