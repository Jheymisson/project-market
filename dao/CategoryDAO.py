from models import *
from models.Models import Category


class CategoryDAO:
    @classmethod
    def saveCategory(cls, category):
        with open('categoria.txt', 'a') as arq:
            arq.writelines(category)
            arq.writelines('\n')

    @classmethod
    def readSales(cls):
        with open('categoria.txt', 'r') as arq:
            cls.category = arq.readlines()
        cls.category = list(map(lambda x: x.replace('\n', ''), cls.category))
        cat = []
        for i in cls.category:
            cat.append(Category(i))
        return cat

CategoryDAO.readSales()