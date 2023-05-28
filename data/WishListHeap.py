from data.HeapMin import HeapMin
import pandas as pd
import os
import csv
from data.Product import Product

class WishListHeap:

    def __init__(self) -> None:
        self.list = HeapMin()
        self.indices_csv :dict = {}
        if os.path.exists("src/wishList.csv"):
            self.lector = pd.read_csv("src/wishList.csv")
            row_count = len(self.lector)
            for i in range(row_count):
                print(i)
                print(self.lector.iloc[i])
                curProduct : Product = Product(title=self.lector['title'][i], price=self.lector['price'][i],
                                     link=self.lector['link'][i], seller=self.lector['seller'][i])
                self.list.insert(curProduct)
                self.indices_csv[str(curProduct)] = i
                print(self.indices_csv[str(curProduct)])
        else:
            with open("src/wishList.csv", 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['title', 'price', 'link','seller'])

    def __str__(self):
        return str(self.list.array)
    
    def insert(self, prod: Product):
        self.list.insert(prod)
        df = pd.read_csv("src/wishList.csv")
        rows = df.shape[0]
        data = pd.DataFrame({"title": prod.title, "price": prod.price, "link": prod.link, "seller": prod.seller}, index=[rows])
        df = pd.concat([df, data])
        df.to_csv("src/wishList.csv", index=False)

    def delete_min(self):
        prod : Product = self.list.get_min()
        index_prod = self.indices_csv[str(prod)]
        prod : Product = self.list.extract_min()
        df = pd.read_csv("src/wishList.csv")

        if index_prod == 0:
            df = df.iloc[1:]
        elif index_prod == (len(df)-1):
            df = df.iloc[0:index_prod]
        else:
            df = pd.concat([df.iloc[0:index_prod], df.iloc[index_prod+1:]]) #Elimina la fila del indice
        df.to_csv("src/wishList.csv", index=False)
        print("Deleted from wish list: "+str(prod))

    
    def delete(self, prod:Product):
        index_list = self.list.array.findPosition(prod)
        index_csv = self.indices_csv[str(prod)]
        self.list.remove_product(index_list)

        df = pd.read_csv("src/wishList.csv")

        if index_csv == 0:
            df = df.iloc[1:]
        elif index_csv == (len(df)-1):
            df = df.iloc[0:index_csv]
        else:
            df = pd.concat([df.iloc[0:index_csv], df.iloc[index_csv+1:]]) #Elimina la fila del indice
        df.to_csv("src/wishList.csv", index=False)
        print("Deleted from wish list: "+str(prod))