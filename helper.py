import sys
from datetime import datetime, timedelta
from pathlib import Path
import json

class BudgetCalculator:
    """Template for calculating my personal 50/30/20 rule budget plan."""

    # Stored class attributes.
    file_path = "monthly_budget.json"
    debt_percent = 0.50
    needs_percent = 0.30
    wants_percent = 0.20

    def __init__(self):
        """Define and assign instance attributes to their initial values."""
        self.earnings = 0
        self.last_added = 0
        self.debt_funds = 0
        self.needs_funds = 0
        self.wants_funds = 0
        self.budget_allocation = {}
        self.pay_day = datetime.now()
        self.month = (self.pay_day + timedelta(days=3)).strftime("%B %Y")
        self.data = self.load_monthly_budget()

    def greet_user(self):
        """Print a neat greeting message to the user."""
        print(
                "\nWelcome to Budget-Mate: "
                "A Program Designed Around Money Management™"
        )

    def display_menu(self):
        """Print the menu options for the user."""
        print(
                "\n--- BUDGET-MATE MENU ---"
                "\n1. Add earnings"
                "\n2. View Budget Mate summary"
                "\n3. Exit"
        )

    def get_menu_choice(self):
        """Prompt the user to select a menu option based on 'display_menu'."""
        while True:
            try:
                menu_choice = int(input("Select an option: "))
            except ValueError:
                print("\nInvalid input! Enter 1, 2, or 3.")
                continue

            if menu_choice in (1, 2, 3):
                return menu_choice
            else:
                print("\nInvalid option! Enter 1, 2, or 3.")

    def get_monthly_income(self):
        """Prompt user for their monthly income & return an integer."""
        total_earnings_added = 0

        while True:
            try:
                amount = int(input("\nEnter an income amount you'd like to add: $"))
                if amount < 0:
                    raise ValueError
            except ValueError:
                print("\nInvalid input! Income must be positive whole number.")
                continue

            total_earnings_added += amount

            while True:
                response = input(
                    "Would you like to enter more earnings for this month? "
                    "[y/n] "
                ).strip().lower()

                if response == "n":
                    return total_earnings_added
                elif response == "y":
                    break
                else:
                    print("\nInvalid input! Please enter 'y' or 'n'.")
                    continue

    def load_monthly_budget(self):
        """
        Read JSON file, return dictionary, and if file does not exist,
        return empty structure.
        """
        if Path(self.file_path).exists():
            with open(self.file_path, "r", encoding="utf-8") as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    return {}
        else:
            return {}

    def update_monthly_budget(self, amount):
        """Load existing data, modify/update it, and write it back to .json."""
        if self.month in self.data:
            # Add to existing earnings.
            self.data[self.month]["earnings"] += amount
            total = self.data[self.month]["earnings"]

            # Recompute allocations to match new total.
            self.data[self.month]["allocations"] = {
                "debt": int(total * self.debt_percent),
                "needs": int(total * self.needs_percent),
                "wants": int(total * self.wants_percent),
            }
            # Percentages stay consistent (or ensure they exist).
            self.data[self.month]["percentages"] = {
                "debt": self.debt_percent,
                "needs": self.needs_percent,
                "wants": self.wants_percent,
            }
        else:
            self.data[self.month] = {
                "earnings": amount,
                "allocations": {
                    "debt": int(amount * self.debt_percent),
                    "needs": int(amount * self.needs_percent),
                    "wants": int(amount * self.wants_percent),
                },
                "percentages": {
                    "debt": self.debt_percent,
                    "needs": self.needs_percent,
                    "wants": self.wants_percent,
                },
            }

        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(self.data, file, indent=4)
        # Reload after saving (dumping) JSON  and write it to disk.
        self.data = self.load_monthly_budget()

    def add_earnings(self):
        """Menu option1: add earnings for this session & save to JSON."""
        amount = self.get_monthly_income()
        self.last_added = amount
        self.earnings += amount
        self.update_monthly_budget(amount)  # Persist ONLY the new amount.

    def display_budget_summary(self):
        """A summarized view of money distribution based on 50/30/20 rule."""
        self.data = self.load_monthly_budget()

        month_data = self.data.get(self.month)
        if not month_data:
            print(
                f"\nNo saved budget found for {self.month} yet."
                "\nChoose option 1 to add earnings first."
            )
            return

        updated_earnings = self.data[self.month]["earnings"]
        updated_debt_allocation = self.data[self.month]["allocations"]["debt"]
        updated_needs_allocation = self.data[self.month]["allocations"]["needs"]
        updated_wants_allocation = self.data[self.month]["allocations"]["wants"]

        print(f"\n---Budget-Mate Summary Results---"
              f"\nAdded Earnings Amount - ${self.last_added}"
              f"\nUpdated Earnings Total Amount for {self.month} - ${updated_earnings}"
              f"\nDebt Allocation (50%) - ${updated_debt_allocation}"
              f"\nNeeds Allocation (30%) - ${updated_needs_allocation}"
              f"\nWants Allocation (20%) - ${updated_wants_allocation}")

    def exit_budget_mate(self):
        """Save data and exit the program intentionally."""
        sys.exit("\nExiting Budget-Mate...")

    def run_budget_mate(self):
        """Menu loop orchestrator."""
        self.greet_user()

        while True:
            # Always refresh from disk so self.data does not go stale.
            self.data = self.load_monthly_budget()

            self.display_menu()
            menu_choice = self.get_menu_choice()
            if menu_choice is None:
                continue

            if menu_choice == 1:
                self.add_earnings()
                self.display_budget_summary()
            elif menu_choice == 2:
                self.display_budget_summary()
            elif menu_choice == 3:
                self.exit_budget_mate()
            else:
                print("\nInvalid option! Enter 1, 2, or 3.")





