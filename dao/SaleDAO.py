from models.Models import *

class SaleDAO:

    @classmethod
    def saveSale(cls, sale: Sale):
        with open('venda.txt', 'a') as arq:
            arq.writelines(sale.soldItems.name + " | " +
                           sale.soldItems.price + " | " +
                           sale.soldItems.category + " | " +
                           sale.seller + " | " +
                           sale.buyer + " | " +
                           str(sale.quantitySold) + " | " +
                           sale.date)
            arq.writelines('\n')


    @classmethod
    def readSales(cls):
        with open('venda.txt', 'r') as arq:
            cls.sale = arq.readlines()
        cls.sale = list(map(lambda x: x.replace('\n', ''), cls.sale))
        cls.sale = list(map(lambda x: x.split('|'), cls.sale))

        print(cls.sale)

SaleDAO.readSales()