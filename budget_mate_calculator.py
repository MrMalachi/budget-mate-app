import sys
from datetime import datetime
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
        self.debt_funds = 0
        self.needs_funds = 0
        self.wants_funds = 0
        self.budget_allocation = {}
        self.month = datetime.now().strftime("%B %Y")
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
        menu_choice = int(input("Select an option: "))
        if menu_choice == 1:
            self.get_monthly_income()
        elif menu_choice == 2:
            self.display_budget_summary()
        elif menu_choice == 3:
            self.save_and_exit()

    def login_or_signup(self):
        """To be included in the future when using a database..."""
        pass

    def get_monthly_income(self):
        """Prompt user for their monthly income & return an integer."""
        while True:
            try:
                amount = int(input("\nEnter an income amount you'd like to add: $"))
                if amount < 0:
                    raise ValueError
            except ValueError:
                print("\nInvalid input! Income must be positive whole number.")
                continue

            # Add to 'self.earnings' attribute
            self.earnings += amount

            while True:
                response = input(
                    "Would you like to enter more earnings for this month? "
                    "[y/n] "
                ).strip().lower()

                if response == "n":
                    return self.earnings
                elif response == "y":
                    break
                else:
                    print("\nInvalid input! Please enter 'y' or 'n'.")
                    continue

    def calculate_budget_allocation(self):
        """
        Calculates how much money to allocate to all categories based on income.
        """
        self.debt_funds = int(self.earnings * self.debt_percent)
        self.needs_funds = int(self.earnings * self.needs_percent)
        self.wants_funds = int(self.earnings * self.wants_percent)

    def convert_budget_allocation_to_dict(self):
        """Build a nested dictionary representing the budget allocation."""
        self.budget_allocation = {
            "earnings": self.earnings,
            "allocations": {
                "debt": self.debt_funds,
                "needs": self.needs_funds,
                "wants": self.wants_funds,
            },
            "percentages": {
                "debt": self.debt_percent,
                "needs": self.needs_percent,
                "wants": self.wants_percent,
            },
        }
        return self.budget_allocation

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

    def update_monthly_budget(self):
        """Load existing data, modify/update it, and write it back to .json."""
        if self.month in self.data:
            # Add to existing earnings.
            self.data[self.month]["earnings"] += self.earnings
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
            self.data[self.month] = self.budget_allocation   # Update dict. with month.

        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(self.data, file, indent=4)
        # Reload after saving (dumping) JSON  and write it to disk.
        self.data = self.load_monthly_budget()

    def display_budget_summary(self):
        """A summarized view of money distribution based on 50/30/20 rule."""
        updated_earnings = self.data[self.month]["earnings"]
        updated_debt_allocation = self.data[self.month]["allocations"]["debt"]
        updated_needs_allocation = self.data[self.month]["allocations"]["needs"]
        updated_wants_allocation = self.data[self.month]["allocations"]["wants"]

        print(f"\n---Budget-Mate Summary Results---"
              f"\nAdded Earnings Amount - ${self.earnings}"
              f"\nUpdated Earnings Total Amount for {self.month} - ${updated_earnings}"
              f"\nDebt Allocation (50%) - ${updated_debt_allocation}"
              f"\nNeeds Allocation (30%) - ${updated_needs_allocation}"
              f"\nWants Allocation (20%) - ${updated_wants_allocation}")

    def save_and_exit(self):
        """Save data and exit the program intentionally."""
        self.update_monthly_budget()
        sys.exit("\nBudget-Mate data saved. Exiting program...")

    def run_budget_mate(self):
        """Orchestrator method runs based on order of operations."""
        self.greet_user()
        self.display_menu()
        self.get_menu_choice()
        self.calculate_budget_allocation()
        self.convert_budget_allocation_to_dict()
        self.update_monthly_budget()
        self.display_budget_summary()

budget = BudgetCalculator()
budget.run_budget_mate()





