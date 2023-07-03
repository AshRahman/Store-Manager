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
        return f"Item('{self.name}',{self.price},{self.quantity})"  # Best Practice for using __repr__


print(Item.is_integer(7.5))

# Item.instantiate_from_csv()
# print(Item.all)

""" 
item2.has_numpad = False
print(Item.__dict__)  # dict is a magic attribute for printing out all the instances
print(item1.__dict__)
item1.apply_discount()
print(item1.price)

item2.pay_rate = 0.7
item2.apply_discount()
print(item2.price) """
