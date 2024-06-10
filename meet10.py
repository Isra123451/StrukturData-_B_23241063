#belajar perbandingan lanjutan, ELIF

nama = input("masukan nama :")

if nama=="isra": # kondisi 1
    print("mahasiswa ganteng") # aksi true 2
elif nama=="ko": # kondisi 2
    print("mahasiswa ganteng") # aksi true 2
elif nama=="ko": # kondisi 3
    print("anda kn mahasiswa") # aksi true3
else:
    print("bukan dosen ganteng") # aksi false
 print("program selesai")

class Product:
    def _init_(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def update_stock(self, quantity):
        if self.stock >= quantity:
            self.stock -= quantity
            return True
        else:
            return False

    def _str_(self):
        return f"Product(name={self.name}, price={self.price}, stock={self.stock})"


class Sale:
    def _init_(self, product, quantity):
        self.product = product
        self.quantity = quantity
        self.total_price = product.price * quantity

    def process_sale(self):
        if self.product.update_stock(self.quantity):
            return self.total_price
        else:
            return None

    def _str_(self):
        return f"Sale(product={self.product.name}, quantity={self.quantity}, total_price={self.total_price})"


class Store:
    def _init_(self):
        self.products = []
        self.sales = []

    def add_product(self, product):
        self.products.append(product)

    def make_sale(self, product_name, quantity):
        for product in self.products:
            if product.name == product_name:
                sale = Sale(product, quantity)
                total = sale.process_sale()
                if total is not None:
                    self.sales.append(sale)
                    return f"Sale successful! Total price: {total}"
                else:
                    return "Sale failed! Not enough stock."
        return "Product not found!"

    def sales_report(self):
        report = "Sales Report:\n"
        for sale in self.sales:
            report += f"{sale}\n"
        return report

    def inventory_report(self):
        report = "Inventory Report:\n"
        for product in self.products:
            report += f"{product}\n"
        return report


# Example usage
if _name_ == "_main_":
    store = Store()

    product1 = Product("Laptop", 10000000, 10)
    product2 = Product("Smartphone", 5000000, 20)

    store.add_product(product1)
    store.add_product(product2)

    print(store.inventory_report())

    print(store.make_sale("Laptop", 2))
    print(store.make_sale("Smartphone", 1))
    print(store.make_sale("Tablet", 1))  # Should return "Product not found!"

    print(store.sales_report())
    print(store.inventory_report())

