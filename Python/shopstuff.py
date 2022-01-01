stuff={'tape':1,'torch':6,'gold':56,'arrow':12}
#productname:quatity
def displayInventory(inventory):
    print("Inventory...!")
    item_total=0
    for k,v in inventory.items():
        print(str(v)+" "+k)
        item_total+=v
        print("Total number of items: "+str(item_total))
displayInventory(stuff)