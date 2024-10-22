# property decorators

class Product:
    def __init__(self, price):
        self.__price = price  # Private attribute

    # Getter method with @property decorator
    @property
    def price(self):
        return self.__price

    # Setter method for price with validation
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        else:
            self.__price = value

# Example usage
try:
    price = float(input("Enter the value of the item: "))
    product = Product(price)

    # Getting the price using the property
    print(f"Initial Price: ${product.price}")

    # Setting a new price
    new_price = float(input("Enter the new price: "))
    product.price = new_price  # This will trigger the setter
    print(f"Updated Price: ${product.price}")

except ValueError as e:
    print(e)

        