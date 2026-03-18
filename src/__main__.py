"""CLI for pujaguide."""
import sys, json, argparse
from .core import Pujaguide

def main():
    parser = argparse.ArgumentParser(description="PujaGuide — AI Ritual Guide. Step-by-step Hindu puja guidance with mantra audio and timing.")
    parser.add_argument("command", nargs="?", default="status", choices=["status", "run", "info"])
    parser.add_argument("--input", "-i", default="")
    args = parser.parse_args()
    instance = Pujaguide()
    if args.command == "status":
        print(json.dumps(instance.get_stats(), indent=2))
    elif args.command == "run":
        print(json.dumps(instance.process(input=args.input or "test"), indent=2, default=str))
    elif args.command == "info":
        print(f"pujaguide v0.1.0 — PujaGuide — AI Ritual Guide. Step-by-step Hindu puja guidance with mantra audio and timing.")

if __name__ == "__main__":
    main()
