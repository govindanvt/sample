from pyexcel_xls import save_data
data={"sheet1":[[1,2,3],[4,5,6]]}
save_data("d:\\t1.xls",data)
print("Successfully created")