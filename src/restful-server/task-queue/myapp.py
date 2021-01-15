from mytask import *
print("[myapp] call add()")
result = add.delay(4, 5)

print("myapp is sending the file..")
# send_file.delay('myfile', '1234567890')