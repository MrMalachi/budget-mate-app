from core.budget_allocator import BudgetAllocator
from pathlib import Path
import json

class BudgetTracker(BudgetAllocator):
    """
    A child class used to track the user's cash flow based on:
    Debt, Needs, Wants.
    """

    def __init__(self):
        """Define and assign instance attributes to their initial values."""
        super().__init__()
        self.expenses = 0
        self.last_added_expense = 0

    def display_main_menu(self):
        """Print the menu options for the user."""
        print(
                "\n--- BUDGET-MATE MENU ---"
                "\n1. Add earnings"
                "\n2. Track expenses"
                "\n3. View Budget-Mate summary"
                "\n4. Exit"
        )

    def get_main_menu_choice(self):
        """Prompt user to select a menu option based on 'display_main_menu'."""
        while True:
            try:
                menu_choice = int(input("Select an option: "))
            except ValueError:
                print("\nInvalid input! Enter 1, 2, 3, or 4.")
                continue

            if menu_choice in (1, 2, 3, 4):
                return menu_choice
            else:
                print("\nInvalid option! Enter 1, 2, 3, or 4.")

    def display_expense_categories(self):
        """Print the category options for the user."""
        print(
            "\n--- EXPENSE CATEGORIES ---"
            "\n1. Debt"
            "\n2. Needs"
            "\n3. Wants"
        )

    def get_expense_category_choice(self):
        """Prompt user to select an expense category option."""
        while True:
            try:
                category_choice = int(input("Select an option: "))
            except ValueError:
                print("\nInvalid input! Enter 1, 2, or 3.")
                continue

            if category_choice in (1, 2, 3):
                return category_choice
            else:
                print("\nInvalid option! Enter 1, 2, or 3.")

    def get_expense_amount(self):
        """Prompt user to enter an expense amount & return an integer."""
        total_expenses_added = 0

        while True:
            try:
                amount = int(input("\nEnter an expense amount you'd like to add: $"))
                if amount < 0:
                    raise ValueError
            except ValueError:
                print("\nInvalid input! Income must be a positive whole number.")
                continue

            total_expenses_added += amount

            while True:
                response = input(
                    "Would you like to enter any more expenses for this month? "
                    "[y/n] "
                ).strip().lower()

                if response == "n":
                    return total_expenses_added
                elif response == "y":
                    break
                else:
                    print("\nInvalid input! Please enter 'y' or 'n'.")
                    continue

    def add_expenses(self, expense_category_choice, amount):
        """Menu option2: track expenses for this session & save to JSON."""
        category_map = {
            1: "debt",
            2: "needs",
            3: "wants",
        }

        category = category_map[expense_category_choice]

        data = self.load_monthly_budget()

        if self.month not in data:
            print("\nNo budget exists for this month yet. PLease add earnings first.")
            return

        if "expenses" not in data[self.month]:
            data[self.month]["expenses"] = {
                "debt": 0,
                "needs": 0,
                "wants": 0,
            }

        data[self.month]["expenses"][category] += amount

        self.last_added_expense = amount
        self.expenses += amount
        self.data = data

        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        print(f"\nAdded ${amount} to the {category.title()} expense category for {self.month}.")

    def run_budget_tracker(self):
        self.display_expense_categories()
        expense_category_choice = self.get_expense_category_choice()
        amount = self.get_expense_amount()
        self.add_expenses(expense_category_choice, amount)

    def run_budget_mate(self):
        """Menu loop orchestrator."""
        self.greet_user()

        while True:
            # Always refresh from disk so self.data does not go stale.
            self.data = self.load_monthly_budget()

            self.display_main_menu()
            menu_choice = self.get_main_menu_choice()
            if menu_choice is None:
                continue

            if menu_choice == 1:
                self.add_earnings()
                self.display_budget_summary()
            elif menu_choice == 2:
                self.run_budget_tracker()
            elif menu_choice == 3:
                self.display_budget_summary()
            elif menu_choice == 4:
                self.exit_budget_mate()
            else:
                print("\nInvalid option! Enter 1, 2, 3, or 4.")

