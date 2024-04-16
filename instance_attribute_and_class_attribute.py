class Shop:
    #cart=[] #class attribute

    def __init__(self,buyer) -> None:
        self.buyer=buyer
        self.cart=[] #instance atribute

    def add_to_cart(self,product):
        self.cart.append(product)

Mehjabeen=Shop('Mehjabeen')
Mehjabeen.add_to_cart('mobile')
Mehjabeen.add_to_cart('shoe')

print(Mehjabeen.cart)

Nisho=Shop('Nisho')
Nisho.add_to_cart('Sunglass')
Nisho.add_to_cart('Wallet')

print(Nisho.cart)