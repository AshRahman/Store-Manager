from item import Item


class Phone(Item):
    def __init__(
        self,
        name: str,  # //? specifying the datatypes makes it more precise on what it should take as input
        price: float,
        quantity=0,
        broken_phones=0,
    ):  # * * magic method. This will be called first when initializing an object
        # TODO: call to super function to have access to all attributes/methods
        super().__init__(name, price, quantity)

        # TODO: Run validation to the received arguments
        assert (
            broken_phones >= 0
        ), f"Broken phones {broken_phones} is not greater than or equal to 0"

        # TODO: Assigned to self objects
        self.broken_phones = broken_phones

        # TODO: Actions to execute
        # Phone.all.append(self) inherits the all from parent class
