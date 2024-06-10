import time
import datetime
import playsound

def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        actual_time = datetime.datetime.now()
        now = actual_time.strftime("%H:%M:%S")
        date = actual_time.strftime("%d/%m/%Y")
        print("The set date is:", date)
        print(now)
        if now == set_alarm_timer:
            print("Time to Wake up")
            playsound.playsound('audio.mp3')
            break

def actual_time():
    set_alarm_timer = input("Set the time of alarm: HH:MM:SS\n")
    alarm(set_alarm_timer)

actual_time()

