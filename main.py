import csv


class Item:
    pay_rate = 0.8  # Class attribute
    all = []

    def __init__(
        self,
        name: str,  # //? specifying the datatypes makes it more precise on what it should take as input
        price: float,
        quantity=0,
    ):  # * * magic method. This will be called first when initializing an object
        # Run validation to the received arguments
        assert (
            price >= 0
        ), f"Price {price} is not greater than or equal to 0"  ## Making custom assert exception error message
        assert quantity >= 0, f"Price {quantity} is not greater than or equal to 0"

        # TODO: Assigned to self objects
        self.name = name
        self.price = price
        self.quantity = quantity

        # TODO: Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity  # receives the data from init class

    def apply_discount(self):
        self.price = (
            self.price * self.pay_rate
        )  # Class name is needed for using class attributes, but for custom pay rate self is used here instead of Item.pay_rate

    @classmethod  # *? decorator used for changing behavior of methods
    def instantiate_from_csv(cls):  # *? class method used for reading csv files
        with open("items.csv", "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:  # * * Used for instantiating objects
            Item(
                name=item.get("name"),
                price=float(item.get("price")),
                quantity=int(item.get("quantity")),
            )

    @staticmethod
    def is_integer(num):
        # We will count out the float that are point zero
        # for 5.0, 10.0
        if isinstance(num, float):
            # count out the float that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}',{self.price},{self.quantity})"  # Best Practice for using __repr__


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


phone1 = Phone("IPhone10", 500, 4)
print(phone1.calculate_total_price())

print(Item.all)
print(Phone.all)
