from datetime import datetime
def date_time():
    # datetime object containing current date and time
    now = datetime.now()

    # month date,Year Hour:Minutes:Second
    dt_string = now.strftime("%B %d,%Y %H:%M:%S")
    return(dt_string)

