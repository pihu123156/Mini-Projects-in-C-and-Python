import csv
from datetime import datetime, timedelta
from collections import defaultdict

FILENAME = "expenses.csv"

def add_expense():
    date = input("Enter date (YYYY-MM-DD) or leave blank for today: ").strip()
    if not date:
        date = datetime.now().strftime("%Y-%m-%d")
    category = input("Enter category (e.g. Food, Transport): ").strip()
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("❌ Invalid amount.")
        return

    with open(FILENAME, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([date, category, amount])
        print("✅ Expense added.")

def load_expenses():
    expenses = []
    try:
        with open(FILENAME, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                date, category, amount = row
                expenses.append({
                    "date": datetime.strptime(date, "%Y-%m-%d"),
                    "category": category,
                    "amount": float(amount)
                })
    except FileNotFoundError:
        pass
    return expenses

def show_summary(period="monthly"):
    expenses = load_expenses()
    now = datetime.now()
    summary = defaultdict(float)

    for e in expenses:
        if period == "daily" and e["date"].date() == now.date():
            summary[e["category"]] += e["amount"]
        elif period == "weekly" and (now - e["date"]).days < 7:
            summary[e["category"]] += e["amount"]
        elif period == "monthly" and e["date"].month == now.month and e["date"].year == now.year:
            summary[e["category"]] += e["amount"]

    print(f"\n📊 {period.capitalize()} Summary:")
    if not summary:
        print("No data found.")
    else:
        total = sum(summary.values())
        for cat, amt in summary.items():
            print(f"{cat}: ${amt:.2f}")
        print(f"Total: ${total:.2f}")

def main():
    while True:
        print("\n📒 Personal Expense Tracker")
        print("1. Add Expense")
        print("2. Daily Summary")
        print("3. Weekly Summary")
        print("4. Monthly Summary")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()
        if choice == '1':
            add_expense()
        elif choice == '2':
            show_summary("daily")
        elif choice == '3':
            show_summary("weekly")
        elif choice == '4':
            show_summary("monthly")
        elif choice == '5':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid option. Try again.")


if __name__ == "__main__":
    main()
