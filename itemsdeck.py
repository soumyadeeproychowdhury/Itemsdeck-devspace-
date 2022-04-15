import mysql.connector

mydb = mysql.connector.connect(host = "localhost", user="root",passwd="student")
cur=mydb.cursor()
cur.execute("use Itemsdeck")
def search_input():
  a = input("Enter Product Name to be searched\n")
  return a

def add_values():
  print("Please enter the following information for the product you're selling : ")
  b=input("Enter Brand Name")
  cost_price=float(input("Enter Cost Price"))
  selling_price=float(input("Enter Selling Price"))
  ins="insert into groceries (name,brand,cost_price,selling_price) values (%s,%s,%s,%s)"
  values=(search_name,b,cost_price,selling_price)
  cur.execute(ins,values)
  mydb.commit()
  print("Thank You for your valuable feedback!")
search_name = search_input()  

def high(rec):
  l=list()
  for r in rec:
    l.append(r[3])
  return max(l)

def low(rec):
  l=list()
  for r in rec:
    l.append(r[3])
  return min(l)
    
def sp_average(rec,ctr):
  sum = 0
  for r in rec:
    sum += r[3]
  sp_average = sum / ctr
  return sp_average

def cp_average(rec,ctr):
  sum = 0
  for r in rec: 
      sum += r[2]
  cpaverage = sum / ctr
  return cpaverage

def ideal1(average_val,cp_average):
  x = average_val - average_val * 0.05
  if x<cp_average:
    x=average_val
  return x
def ideal2(average_val,cp_average):
  y = average_val + average_val * 0.06
  return y
while True:
  st = "select * from groceries where name = '"+search_name+"'"
  cur.execute(st)
  rec = cur.fetchall()
  ctr = cur.rowcount
  if ctr == -1:
    print("Item Not Available In Database")
    ch = input("Do you want to add item to Database y/n")
    if ch.lower() in ("y","yes"):
      add_values()
      break
    else:
      feedback = input("Do you have any feedback about how we can improve our software : ")
      print("Thank You for your valuable feedback !")
      break
  else:
      high_val = high(rec)
      low_val = low(rec)
      average_val = sp_average(rec,ctr)
      cp_average = cp_average(rec,ctr)
      ideal_value_1 = ideal1(average_val,cp_average)
      ideal_value_2 = ideal2(average_val,cp_average)
      print("The highest price for ",search_name,"is : ", high_val)
      print("The lowest price for ",search_name,"is : ", low_val)
      print("The average price for ",search_name,"is : ", average_val)
      print("The ideal price range for ",search_name,"is : ", ideal_value_1, "to ", ideal_value_2)
      add_values()
      break
      
  
  