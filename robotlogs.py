import os
from datetime import datetime
from re import X
import time
import json

og_path=r'/home/meditab/Documents/robot9-docker/logs'

# path_in=input("Enter the path from where do you want to copy: ")
# og_path=og_path+path_in

copy_path=r'/home/meditab/Documents/robot9-docker/getpackdetails'

# path_out=input("Enter the path from where you want to place your copied file: ")
# copy_path=copy_path+path_out
og_file_name='extra_data_manager_pack_processing.log'
copy_file_name='extra_data_manager.log'

with open(os.path.join(og_path,og_file_name),'r') as ogfile, open(os.path.join(copy_path,copy_file_name),'a') as copyfile:
    string1="Return from call webservice: Status : True, response data : {'data': {'id"
    ogfile_r=ogfile.readlines()
    for i in ogfile_r:
        if string1 in i:    
            print(type(i))
            copyfile.write(i)

        
# with open('og.log','r') as ogfile, open('copy.log','a') as copyfile:
#     string1='getpack'
#     ogfile_r=(ogfile.readlines())
#     print(ogfile_r)
#     for i in range(len(ogfile_r)):
#         ogfile_r[i]
#         if string1 in ogfile_r[i]:    
#             copyfile.write(ogfile_r[i])

        


        
# print("logs is copying....")
# time.sleep(2)
# print("Your logs data is copied")
