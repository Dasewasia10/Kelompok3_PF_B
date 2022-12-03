class State:
    def receive_payment(self):
        raise NotImplementedError()
        
    def ship(self):
        raise NotImplementedError()

    def mark_delivered(self):
        raise NotImplementedError()

class Order:
    def __init__(self) -> None:
        self.unpaid_state = UnpaidState()
        self.paid_state = PaidState()
        self.shipped_state = ShippedState()
        self.delivered_state = DeliveredState()

        self.state = self.unpaid_state
    
    def set_state(self, state: State):
        self.state = state

    def ship(self):
        self.state.ship()

    def receive_payment(self):
        self.state.receive_payment()

    def mark_delivered(self):
        self.state.mark_delivered()

class UnpaidState(State):
    def __init__(self, context: Order):
        self.context = context

    def receive_payment(self):
        self.context.set_state(self.context.paid_state)
        print("Your payment was accepted")
    
    def ship(self):
        print("Can't ship unpaid orders")

    def mark_delivered(self):
        print("Can't delivered unshipped orders")

class PaidState(State):
    def __init__(self, context: Order):
        self.context = context

    def receive_payment(self):
        print("The order has been already paid for!")
    
    def ship(self):
        self.context.set_state(self.context.shipped_state)
        print("The order has been shipped!")

    def mark_delivered(self):
        print("Only shipped orders can be delivered")

class ShippedState(State):
    def __init__(self, context: Order):
        self.context = context

    def receive_payment(self):
        print("The order has been already paid for!")
    
    def ship(self):
        print("The order has been already shipped!")

    def mark_delivered(self):
        self.context.set_state(self.context.delivered_state)
        print("Only orders has been delivered!")

class DeliveredState(State):
    def __init__(self, context: Order):
        self.context = context

    def receive_payment(self):
        print("The order has been already paid for!")
    
    def ship(self):
        print("The order has been already delivered! Check the front door")

    def mark_delivered(self):
        print("The order has been already delivered! Check the front door")

if __name__ == "__main__":
    order = Order()
    print(order.state)
    order.receive_payment()
    print(order.state)
    order.ship()
    print(order.state)
    order.mark_delivered()
    print(order.state)