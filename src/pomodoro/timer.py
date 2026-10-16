import time
import math

def countdown(seconds):
    deadline = time.monotonic() + seconds

    while True:
        remaining = max(0, math.ceil(deadline - time.monotonic()))

        minutes, secs = divmod(remaining, 60)

        print(f"\rFocus: {minutes:02d}:{secs:02d}", end="", flush=True)

        if remaining == 0:
            break

        time.sleep(min(0.1, remaining))

    print("\nSession completed!")

            
        
