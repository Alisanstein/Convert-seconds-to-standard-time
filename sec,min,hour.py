def make_readable(seconds):     #this function get seconds and give "HH:MM:SS" time for you
    if seconds <60:             #For example make_readable(3599)--> "23:59:59"
        sec = seconds
        if sec<10:
            return "00:00:0"+str(sec)
        elif sec>=10:
            return "00:00:"+str(sec)

    elif seconds >= 60 and seconds < 3600:
        min = seconds // 60
        sec = seconds % 60
        if min < 10:
            if sec<10:
                return "00:0"+str(min)+":0"+str(sec)
            elif sec>=10:
                return "00:0"+str(min)+":"+str(sec)
            
            
        elif min >= 10:
            if sec<10:
                return "00:"+str(min)+":0"+str(sec)
            elif sec>=10:
                return "00:"+str(min)+":"+str(sec)
    else:

        hour = seconds // 3600
        seconds = seconds % 3600
        min = seconds // 60
        sec = seconds % 60

        if hour<10:

            if min<10:

                if sec<10:
                    return "0"+str(hour)+":0"+str(min)+":0"+str(sec)

                elif sec>=10:
                    return "0"+str(hour)+":0"+str(min)+":"+str(sec)

            elif min>=10:

                if sec<10:
                    return "0"+str(hour)+":"+str(min)+":0"+str(sec)

                elif sec>=10:
                    return "0"+str(hour)+":"+str(min)+":"+str(sec)
        elif hour>=10:
            if min<10:

                if sec<10:
                    return ""+str(hour)+":0"+str(min)+":0"+str(sec)

                elif sec>=10:
                    return ""+str(hour)+":0"+str(min)+":"+str(sec)

            elif min>=10:

                if sec<10:
                    return ""+str(hour)+":"+str(min)+":0"+str(sec)

                elif sec>=10:
                    return ""+str(hour)+":"+str(min)+":"+str(sec)
