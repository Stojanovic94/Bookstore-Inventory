class Customer:
    def __init__(self, customer_id, name, phone, address, email):
        self.customer_id = customer_id
        self.name = name
        self.phone = phone
        self.address = address
        self.email = email
        self.orders = []

    def place_order(self, order):
        self.orders.append(order)

    def get_order_history(self):
        return self.orders
