import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="99$inmedi",
  database="testing"
)

mycursor = mydb.cursor()


# mycursor.execute("CREATE TABLE final_canister(id INT not null, batch_no INT(25), rfid VARCHAR(50), drug_name VARCHAR(50), NDC INT(15), size VARCHAR(10), primary key(id))")
# mycursor.execute("Create table raw_material(batch_no int(25),big_stick_size int(25), big_stick_qty int(25), small_stick_size int(15), small_stick_qty int (10), drum_qty int(10), main_body_qty int(10), brush_size int(10), brush_qty int(10), primary key(batch_no))")
# mycursor.execute("show tables;")
# for x in mycursor:
#     print(x)


while True:
  print("Press 1 to view or Enter data of Raw Materials ")    
  print("Press 2 to view or Enter data of Final Canister ")
  print("")
  x=int(input("Enter a no to proceed further :- "))
  print("")
  if x==1:
    print("Press 1 to view the Raw Materials")
    print("Press 2 to enter data of recent batch in Raw Materials")
    print("")
    y=int(input("Enter a keyword to proceed further :- "))
    print("")
  # elif :
  #   print("Please Enter a valid No.")
    
    if y==1:
      print("The batchwise data of all the raw Materials are shown below :- ")
      mycursor.execute("Select * from raw_material;")
      for i in mycursor:
        print(i)
    elif y==2:
      batch = int(input("Enter the batch no : "))
      big_Stick = int(input("Enter the big_Stick : "))
      big_qty = int(input("Enter the big qty : "))
      small_size = int(input("Enter the small size : "))
      small_qty = int(input("Enter the small qty : "))
      drum = int(input("Enter the drum : "))
      body = int(input("Enter the body : "))
      brush_size = int(input("Enter the brush size : "))
      brush_qty = int(input("Enter the brush qty : "))
      q = ("""Insert into raw_material values(%s, %s, %s, %s, %s, %s, %s, %s, %s)""")
      data = (batch,big_Stick,big_qty,small_size,small_qty,drum,body,brush_size,brush_qty)
      mycursor.execute(q, data)
      mydb.commit()
      print("Values inserted into table...")
  elif x==2:
    print("Press 1 to view the Raw Materials")
    print("Press 2 to enter data of recent batch in Raw Materials")
    print("")
    y=int(input("Enter a keyword to proceed further :- "))
    print("")
    if y==1:
      print("The batchwise data of all the raw Materials are shown below :- ")
      mycursor.execute("Select * from final_canister;")
      for q in mycursor:
        print(q)
    elif y==2:
      print("Entery done")
    else:
      print("Wrong choice")
  else:
    print("Wrong choice, Please enter from given numbers\nPress 'y/Y' to continue")
    con = input()
    if con not in ['y', 'Y']:
      break
      # print("The value of x is" ,x)
      