import argparse

from pomodoro.timer import countdown
from pomodoro.state import load_state,save_state

def main():
    parser = argparse.ArgumentParser(
        prog="pomodoro",
        description="A Pomodoro CLI for macOS"   
    )

    parser.add_argument(
        "command", 
        choices=["hello", "start", "status"]
    )

    parser.add_argument(
        "--seconds",
        type=int,
        default=1500
    )

    args = parser.parse_args()

    if args.command == "hello":
        print("Hello from Pomodoro")

    elif args.command == "start":
        if args.seconds <= 0:
            parser.error("--seconds must be greater than zero")

        try:
            countdown(args.seconds)
            
        except KeyboardInterrupt:
            save_state({
                "status": "idle",
                "duration": args.seconds
            })
            
            print("\nSession cancelled")

    elif args.command == "status":
        state = load_state()
        print(f"Pomodoro status: {state['status']}")