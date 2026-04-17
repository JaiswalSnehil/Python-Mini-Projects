import time
from datetime import datetime

# User input
alarm_time = input("Set alarm time (HH:MM in 24-hour format): ")

print(f"Alarm set for {alarm_time}")

while True:
    current_time = datetime.now().strftime("%H:%M")
    
    print(f"\rCurrent Time: {current_time}", end="")
    
    if current_time == alarm_time:
        print("\n⏰ Wake up! Alarm ringing!")
        
        # Beep sound (works in terminal)
        for _ in range(5):
            print("\a")  # system beep
            time.sleep(1)
        
        break

    time.sleep(1)