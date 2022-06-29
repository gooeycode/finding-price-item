#declerations
MSG_YES = "This item is in the database, getting the price for you..."
MSG_NO = "This item is not in the database."
itemNoList = [234, 813, 629, 887, 1423, 35]
itemPrices = [3.00, 14.34, 2.20, 34.8, 28.9, 7.34]
foundIt = ""
SIZE = 6
QUIT = 999

#functions
def findItems():
    global itemInput
    foundIt = "N"
    x = 0
    while (x < SIZE) and (foundIt != "Y"):
        if int(itemInput) == int(itemNoList[x]):
            foundIt = "Y"
            price = itemPrices[x]
        x = x + 1
    if foundIt == "Y":
        print(MSG_YES)
        print("Item number is", itemInput)
        print("Item price is £", price)
    else:
        print(MSG_NO)
    print("enter your item number and I'll return the price for you, or 999 to quit program")
    itemInput = input()

#program start
print("Hello, welcome to my program")
print("this program will find your item price")
print("enter your item number and I'll return the price for you, or 999 to quit program")

itemInput = input()
while itemInput != QUIT:
    findItems()
    
print("thank you for using this program. Goodbye")