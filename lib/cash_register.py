#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.total = 0.0
        self.discount = discount
        self.items = []
        self.last_transaction = 0.0

    def add_item(self, title, price, quantity=1):
        # Add price * quantity to total
        self.last_transaction = price * quantity
        self.total += self.last_transaction

        # Add items to the items list
        for _ in range(quantity):
            self.items.append(title)

    def apply_discount(self):
        if self.discount > 0:
            self.total = self.total * (100 - self.discount) / 100
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        # Subtract last transaction from total
        self.total -= self.last_transaction
        # Remove last transaction items from the items list
        if self.last_transaction > 0 and self.items:
            # Calculate how many items were in the last transaction
            quantity = int(self.last_transaction / (self.last_transaction / len(self.items)))  # safer to just remove one if needed
            # For simplicity, remove last 'quantity' items
            self.items = self.items[:-1] if len(self.items) >= 1 else []
        # Reset total to 0.0 if empty
        if self.total < 0:
            self.total = 0.0
