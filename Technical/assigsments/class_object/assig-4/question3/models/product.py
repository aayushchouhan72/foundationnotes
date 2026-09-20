class  Product:
    def __init__(self,pid,pname,pprice,pqua):
         self.product_id=pid
         self.product_name=pname
         self.price=pprice
         self.quantity=pqua
    @classmethod
    def display_products(cls,product_list):
         for product in product_list:
             print(f"{ product.product_id,product.product_name ,product.price,product.quantity}")
    @classmethod
    def display_product_with_cost(cls,product_list):
         for product in product_list:
               print(f"{ product.product_id,product.product_name ,"Total cost :- ",product.price*product.quantity}")
    @classmethod
    def display_product_it_dep(cls,product_list):
         for product in product_list:
             if product.quantity<10:
                       print(f"{ product.product_id,product.product_name ,product.price,product.quantity}")
    @classmethod
    def highest_price_product(cls,product_list):
         maxmark=product_list[0].price
         st=0
         for product in product_list:
             if product.price>maxmark:
                    st=product
         product=st
         print(f"{ product.product_id,product.product_name ,product.price,product.quantity}")
    @classmethod
    def sum_of_product_quantity(cls,product_list):
         sum=0
         for product in product_list:
             sum+=product.quantity
         return sum
    @classmethod
    def product_find_by_key(cls,product_list,key):
         for product in product_list:
             if product.product_id==key:
                  return product
         else:
               return "Product not found"
         

  
 
         
         
         
