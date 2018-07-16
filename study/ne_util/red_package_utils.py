# -*- coding:utf-8 -*-
import math
import random

class LeftMoneyPackage:
    remainSize = 0
    remainMoney = 0
    def __init__(self, remainSize, remainMoney):
        self.remainSize = remainSize
        self.remainMoney = remainMoney

    def reduce_size(self):
        self.remainSize = self.remainSize-1
        return self.remainSize

    def reduce_money(self, money):
        self.remainMoney-=money
        return round(self.remainMoney, 2)

def getRandomMoney(leftMoneyPackage):
    # remainSize 剩余的红包数量
    # remainMoney 剩余的钱
    if (leftMoneyPackage.remainSize == 1):
        return round((leftMoneyPackage.remainMoney * 100)/100, 2)
    min_money = 0.01
    max_money = round(leftMoneyPackage.remainMoney / leftMoneyPackage.remainSize * 2, 2)
    print("max", max_money)

    rand_num = random.random() # 0-1随机数
    print("随机数: ", rand_num)
    money = (rand_num * max_money)
    if money <= min_money:
        money=0.01
    money = math.floor(money * 100) / 100
    return money

if __name__ == '__main__':
    leftMoneyPackage = LeftMoneyPackage(5, 10)

    while(leftMoneyPackage.remainSize >= 1):
        money = getRandomMoney(leftMoneyPackage)
        print("抢到:", money)
        print("剩余次数: ", leftMoneyPackage.reduce_size())
        print("剩余金额: ", leftMoneyPackage.reduce_money(money))
        print("="*5)
