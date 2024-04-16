class Shopping:
    def __init__(self,buyer) -> None:
        self.buyer=buyer
        self.cart=[]
    def add_to_cart(self,item,price,quantity):
        product={'item':item,'price':price,'quantity':quantity}
        self.cart.append(product)

    def checkout(self,amount):
        total=0
        for item in self.cart:
            total+=item['price']*item['quantity']
        print('total price=',total)
        if amount<total:
            print(f'please provide {total-amount} more')
        else:
            print(f'Here is your item and your change {amount-total}')

Badsha=Shopping('Badsha')
Badsha.add_to_cart('Alu',50,5)
Badsha.add_to_cart('Kola',5,12)
Badsha.add_to_cart('Chal',50,10)

Badsha.checkout(100000)


        
