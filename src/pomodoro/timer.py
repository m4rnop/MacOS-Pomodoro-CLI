import time
import math

from pomodoro.state import save_state

def countdown(seconds):
    save_state({
        "status": "running",
        "duration": seconds
    })

    deadline = time.monotonic() + seconds

    while True:
        remaining = max(0, math.ceil(deadline - time.monotonic()))

        minutes, secs = divmod(remaining, 60)

        print(f"\rFocus: {minutes:02d}:{secs:02d}", end="", flush=True)

        if remaining == 0:
            break

        time.sleep(min(0.1, remaining))

    save_state({
            "status": "completed",
            "duration": seconds
        })
    
    print("\nSession completed!")

            
        
