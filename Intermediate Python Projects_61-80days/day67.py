# **67.** Countdown Timer CLI


import time

def countdown_timer(minutes: int, seconds: int):
    total_seconds = minutes * 60 + seconds

    try:
        while total_seconds:
            mins, secs = divmod(total_seconds, 60)
            timer_display = f"{mins:02d}:{secs:02d}"
            print(f"\r⏳ Time Remaining: {timer_display}", end="")
            time.sleep(1)
            total_seconds -= 1

        print("\r⏰ Time's up!                       ")
    except KeyboardInterrupt:
        print("\n⛔ Countdown cancelled by user.")

def main():
    print("🔢 Countdown Timer")
    try:
        minutes = int(input("Enter minutes: "))
        seconds = int(input("Enter seconds: "))
        if minutes < 0 or seconds < 0 or seconds >= 60:
            print("❌ Invalid input. Minutes ≥ 0 and 0 ≤ Seconds < 60.")
            return
        countdown_timer(minutes, seconds)
    except ValueError:
        print("❌ Please enter valid integers for minutes and seconds.")

if __name__ == "__main__":
    main()
