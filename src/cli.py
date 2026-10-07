import argparse

from .analyzer import parse_ticket, build_report


def main() -> None:
    parser = argparse.ArgumentParser(description="Ticket Analyzer")
    parser.add_argument("tickets", nargs="+", help="Ticket texts")

    args = parser.parse_args()

    tickets = [parse_ticket(text) for text in args.tickets]

    report = build_report(tickets)

    print(report)


if __name__ == "__main__":
    main()