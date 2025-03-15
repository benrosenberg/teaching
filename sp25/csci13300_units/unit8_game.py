import random
from tkinter import *

numberShares = 0
account = 10000
sharePrice = 97


def update():
    shares["text"] = "You own {0} shares".format(numberShares)
    cash["text"] = "Cash balance: ${0:.0f}".format(account)
    totalWorth = account + numberShares * sharePrice
    worth["text"] = "Total worth: ${0:.0f}".format(totalWorth)
    price["text"] = "${0:.2f}/share".format(sharePrice)


def doBuy():
    global account, numberShares
    if account >= 10 * sharePrice:
        numberShares += 10
        account -= 10 * sharePrice
        update()


def doSell():
    global account, numberShares
    if numberShares >= 10:
        numberShares -= 10
        account += 10 * sharePrice
        update()


def changePrice():
    global sharePrice
    sharePrice += random.random() * 4 - 2
    update()
    root.after(2000, changePrice)


root = Tk()

status = Frame(root)

shares = Label(status)
shares.pack(anchor=W)

cash = Label(status)
cash.pack(anchor=W)

worth = Label(status)
worth.pack(side=BOTTOM, anchor=W)

action = Frame(root)

price = Label(action)
price.pack(anchor=E)

sell = Button(action)
sell["text"] = "sell"
sell["command"] = doSell
sell.pack(side=BOTTOM, fill=X)

buy = Button(action)
buy["text"] = "buy"
buy["command"] = doBuy
buy.pack(side=BOTTOM, fill=X)

status.pack(side=LEFT, expand=YES, fill=BOTH)
action.pack(side=RIGHT, expand=YES, fill=BOTH)

changePrice()

mainloop()
