#Author: Anastasia Van Natta
#Date: 09/29/2024
#Short description of program: 
import root as tk

class PurchaseRequest:
    def __init__(self, asset, price, name, date):
        self.asset = asset
        self.price = price
        self.name = name
        self.date = date
        self.approved = False
        self.rejected = False

    def __str__(self):
        return (f"Purchase Request\n"
                f"------------------\n"
                f"Asset: {self.asset}\n"
                f"Price: ${self.price:.2f}\n"
                f"Requester: {self.name}\n"
                f"Date: {self.date}\n"
                f"Status: {'Approved' if self.approved else 'Rejected' if self.rejected else 'Pending Approval'}")

class Approver:
    def __init__(self, name):
        self.name = name

    def review_request(self, purchase_request):
        if purchase_request.price > 100.00:
            decision = input(f"{self.name}, the purchase request exceeds $100.00. Do you approve it? (yes/no): ").lower()
            if decision == "yes":
                purchase_request.approved = True
                print(f"{self.name} approved the purchase request.")
            else:
                purchase_request.rejected = True
                print(f"{self.name} rejected the purchase request.")
        else:
            print("Purchase request does not require approval.")

def create_purchase_request():
    asset = input("Enter the asset name: ")
    price = float(input("Enter the price of the asset: "))
    name = input("Enter your name: ")
    date = input("Enter the date (YYYY-MM-DD): ")
    
    return PurchaseRequest(asset, price, name, date)

def main():
    print("Create a Purchase Request")
    purchase_request = create_purchase_request()

    approver = Approver("Manager")  # This can be changed to the actual approver's name

    if purchase_request.price > 100.00:
        approver.review_request(purchase_request)
    else:
        print("Purchase request does not require approval and is automatically approved.")
        purchase_request.approved = True

    print(purchase_request)

if __name__ == "__main__":
    main()
