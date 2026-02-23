from datetime import datetime
from os.path import exists
from pathlib import Path
import json

class BudgetCalculator:
    """Template for calculating my personal 50/30/20 rule budget plan."""

    def __init__(self):
        """Define and assign instance attributes to their initial values."""
        self.earnings = 0
        self.debt_funds = 0
        self.needs_funds = 0
        self.wants_funds = 0
        self.budget_allocation = {}
        self.month = datetime.now().strftime("%B %Y")
        self.file_path = "monthly_budget.json"

    def get_monthly_income(self):
        """Prompt user for their monthly income & return an integer."""
        while True:
            try:
                self.earnings = int(input("Enter you earnings for this month: $"))
                if self.earnings < 0:
                    raise ValueError
            except ValueError:
                print("\nInvalid input! Income must be positive whole number.")
            else:
                return self.earnings

    def calculate_budget_allocation(self):
        """
        Calculates how much money to allocate to all categories based on income.
        """
        self.debt_funds = int(self.earnings * 0.50)
        self.needs_funds = int(self.earnings * 0.30)
        self.wants_funds = int(self.earnings * 0.20)

    def convert_budget_allocation_to_dict(self):
        """Build a nested dictionary representing the budget allocation."""
        self.budget_allocation = {
            "month": self.month,
            "income": self.earnings,
            "allocations": {
                "debt": self.debt_funds,
                "needs": self.needs_funds,
                "wants": self.wants_funds,
            },
            "percentages": {
                "debt": 0.50,
                "needs": 0.30,
                "wants": 0.20,
            },
        }

    def load_monthly_budget(self):
        """
        Read JSON file, return dictionary, and if file does not exist,
        return empty structure.
        """
        if exists(self.file_path):
            with open(self.file_path, "r") as file:
                data = json.load(file)
                return data
        else:
            return {}

    def save_to_monthly_budget(self):
        """Write the user's input & calculations to JSON file."""
        path = Path("monthly_budget.json")
        path.write_text(json.dumps(self.budget_allocation, indent=4), encoding="utf-8")

    def update_monthly_budget(self):
        """"""
        pass

    def display_budget_summary(self):
        """A summarized view of money distribution based on 50/30/20 rule."""
        print(f"\n---Budget Mate Summary Results---"
              f"\nDebt Allocation (50%) - ${self.debt_funds}"
              f"\nNeeds Allocation (30%) - ${self.needs_funds}"
              f"\nWants Allocation (20%) - ${self.wants_funds}")

    def run_budget_mate(self):
        """Orchestrator method runs based on order of operations."""
        self.get_monthly_income()
        self.calculate_budget_allocation()
        self.convert_budget_allocation_to_dict()
        self.save_to_monthly_budget()
        self.display_budget_summary()

budget = BudgetCalculator()
budget.run_budget_mate()





