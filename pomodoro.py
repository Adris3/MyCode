from win10toast import ToastNotifier
import time
import os

#Setting up notification messages
endOfWork = ToastNotifier()
endOfRest = ToastNotifier()
endOfSession = ToastNotifier()




def min_sec(minutes):
    return minutes * 60


def countdown(t, label):
    while t:
        min, sec = divmod(t, 60)
        #t//60 -> minutes
        #t%60 -> seconds
        print(f"{label}: {min:02d}:{sec:02d}", end="\r")
        time.sleep(1)
        t -= 1


def pomodoro(work, rest, cycle):

    w = min_sec(work)
    r = min_sec(rest)

    for i in range(cycle):
        print("CYCLE ", i+1)
        countdown(w, "Work")
        endWork = endOfWork.show_toast("Work Done", "Your working time is up, rest", duration= 5)
        os.system("clear||cls")
        print("CYCLE ", i+1)
        countdown(r, "Rest")
        endOfRest.show_toast("Get To Work", f"Work for {work} minutes", duration= 5)

    #after the for loop, the following notification should show up
    
    endMessage = f"Cycles completed: {cycle} \nminutes worked: {work * cycle}"

    endOfSession.show_toast("Session Done", endMessage, duration= 3)



work = int(input("Enter working time(min): "))
rest = int(input("Enter resting time(min): "))
cycle = int(input("Enter number of cycles: "))
# print(work)
# print(rest)

pomodoro(work, rest, cycle)

