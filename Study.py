Study_time= float (input("Enter Study Time:(In Hours)"))

if Study_time== 0:
    print("No study today? Discipline builds destiny. Start now.")
elif Study_time < 2:
    print("Good start. But success requires more pressure. Push harder.")
elif Study_time < 4: 
    print("You are warming up. Increase focus. You have more in you.")
elif Study_time <6:
    print("Solid effort. This is how toppers are built.")
elif 6.1>= Study_time <8:
    print("Future Doctor energy detected 🔥 Keep grinding.")
else :
    print("Legendary focus mode activated. Just avoid burnout and rest properly.")
