class Invoice:
    amount = 0

    def __init__(self, number, description, quantity, price):
        self.__number = number
        self.__description = description
        self.__quantity = quantity
        self.__price = price  # double underscore"__" used to change public to private

    def display_details(self):
        print("Part Number = ", self.__number)
        print("Part description = ", self.__description)
        print("Quantity of the item being purchased = ", self.__quantity)
        print("Price per item = ", self.__price)
    def get_number(self):
        print(self.__number)
    def get_description(self):
        print(self.__description)
    def get_quantity(self):
        print(self.__quantity)
    def get_price(self):
        print(self.__price)
    
    def set_number(self,new_number):
        self.__number=new_number
    def set_description(self,new_description):
        self.__description=new_description
    def set_quantity(self,new_quantity):
        self.__quantity=new_quantity
    def set_price(self,new_price):
        self.__price=new_price

    def get_invoice(self):
        if self.__quantity < 0:
            self.__quantity = 0
        if self.__price < 0:
            self.__price = 0
        print("Amount : ", self.__quantity*self.__price)
       
invoice = Invoice(1, "classmate note", 20, -30)
invoice.display_details()
invoice.get_invoice()
