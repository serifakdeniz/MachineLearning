#Initialize the cart list
cart=[]
#Define the "add_to_cart" function
def add_to_cart(item,quantity):
  cart.append((item,quantity))
 # item_list.remove(item)
  
  #Define the "create_invoice" function
def create_invoice():
  total_amount_inc_tax=0
  for item,quantity in cart:
    price=price_sheet[item]
    tax=0.18*price
    total=(tax+price)*quantity
    total_amount_inc_tax+=total
    print('Item : ',item,'\t','price',price,'\t','quantity',quantity,'\t','tax ',tax,'\t','total',total,'\n')
    print("after applied total amoutnt:",'\t',total_amount_inc_tax)
    return total_amount_inc_tax
#Define the "checkout" function
def checkout():
  global limit
  total_amount=create_invoice()
  if limit==0:
    print("you dont have any budget")
  elif total_amount > limit:
    print("limiti geçtiniz")
  else:
    limit-=total_amount
    print(f"total amount is (incl. taxes) you have paid is {total_amount} you have {limit} dollars left")

#Add first item to cart
add_to_cart('Laptop',1)
add_to_cart('Headset',8)
add_to_cart('second monitor',5)
add_to_cart('mousepad',5)
add_to_cart('usb drive',4)
add_to_cart('external drive',2)

checkout()
#Add second item to cart
