from core.budget_allocator import BudgetAllocator

class BudgetTracker(BudgetAllocator):
    """
    A child class used to track the user's cash flow based on:
    Debt, Needs, Wants.
    """

    def __init__(self):
        """Define and assign instance attributes to their initial values."""
        super().__init__()

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
                amount = int(input("\n Enter an expense amount you'd like to add: $"))
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
                elif reponse == "y":
                    break
                else:
                    print("\nInvalid input! Please enter 'y' or 'n'.")
                    continue

    def run_budget_tracker(self):
        self.display_expense_categories()
        self.get_expense_category_choice()
        self.get_expense_amount()

