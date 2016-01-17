import os

file_list = os.listdir('/home/merlo/Desktop/prank/')
print file_list
os.chdir('/home/merlo/Desktop/prank/')
for file_name in file_list:
    os.rename(file_name, file_name.translate(None, "1234567890"))
file_list = os.listdir('/home/merlo/Desktop/prank/')
print file_list