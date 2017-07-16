import csv
import shutil
from collections import defaultdict
Bill=["ProName","Quantity","Rate"]
class SuperMarket:
	ProName=""
	Quantity=0
	Rate=0
	
	def search(self,randomp):
		count=0
		with open("contents.csv","r") as csv_f:
			reader=csv.DictReader(csv_f,fieldnames=Bill)
			for row in reader:
				if row["ProName"]==randomp:
					count=1
					break
			if count==1:
				print("Found")
				
			else:
				randomp=raw_input("Enter another Product")
				self.search(randomp)
	def calculate(self):
		total=0
		boole='Y'
		while boole is not 'N' :
			name=raw_input("Enter the product name")
			qty=int(input("Enter the quantity of the product u want"))
			
			with open("contents.csv","r") as csv_f:
				reader=csv.DictReader(csv_f,fieldnames=Bill)
				for row in reader:
					if row["ProName"]==name:
						if(qty>int(row["Quantity"])):
							print("Sorry!!Enter same/another product within the given quantity")
							self.calculate()
						else:
							print("Calculating...Pls Wait")
							total=total+int(row["Rate"])*qty
						
				
				
				
					
		
			print("The total amount is")
			print total
			boole=raw_input("PressY to go ahead and N to quit??")
	def add(self):
		with open("contents.csv",'a') as csv_f:
			writer=csv.writer(csv_f) 
			name=raw_input("Enter the Name of the product to be added\n")
			quantity=input("Enter the quantity of the new product\n")
			cost=input("Enter the cost of the product\n")
			data=[name,quantity,cost]
			writer.writerow(data)
		self.display()
	
	def display(self):
		with open("contents.csv","r") as csv_f:
			reader=csv.DictReader(csv_f)
			for row in reader:
				print(row)
	def delete(self):
		name=raw_input("Enter the name of the product to be deleted")
		with open("contents.csv","r") as csv_f,open('File.csv','w') as outputf:
			reader=csv.DictReader(csv_f,fieldnames=Bill)
			writer=csv.DictWriter(outputf,fieldnames=Bill)
			for row in reader:
				if not name==row["ProName"]:
					writer.writerow({'ProName':row["ProName"],"Quantity":row["Quantity"],"Rate":row["Rate"]})
		shutil.move('File.csv',"contents.csv")
		self.display()
	
	def update_cost(self):
		name=raw_input("Enter the name of the product to be updated")
		new_cost=input("Enter the new rate")
		with open("contents.csv","r") as csv_f,open('File.csv','w') as outputf:
			reader=csv.DictReader(csv_f,fieldnames=Bill)
			writer=csv.DictWriter(outputf,fieldnames=Bill)
			for row in reader:
				if name==row["ProName"]:
					writer.writerow({'ProName':row["ProName"],"Quantity":row["Quantity"],"Rate":new_cost})
				else:
					writer.writerow({'ProName':row["ProName"],"Quantity":row["Quantity"],"Rate":row["Rate"]})
		shutil.move('File.csv',"contents.csv")
		self.display()
	def update_quantity(self):
		name=raw_input("Enter the name of the product to be updated")
		new_quantity=input("Enter the new quantity")
		with open("contents.csv","r") as csv_f,open('File.csv','w') as outputf:
			reader=csv.DictReader(csv_f,fieldnames=Bill)
			writer=csv.DictWriter(outputf,fieldnames=Bill)
			for row in reader:
				if name==row["ProName"]:
					writer.writerow({'ProName':row["ProName"],"Quantity":new_quantity,"Rate":row["Rate"]})
				else:
					writer.writerow({'ProName':row["ProName"],"Quantity":row["Quantity"],"Rate":row["Rate"]})
		shutil.move('File.csv',"contents.csv")
		self.display()
					
					
suma=SuperMarket();
option=-1
while(option is not 0): 
	print("Welcome to Keeru's Program!!!Select any one of the following options")
	print("1.ADD\n2.SEARCH\n3.UPDATE_COST\n4.DISPLAY\n5.CALCULATE\n6.DELETE\n7.UPDATE_QUANTITY\n")
	option=input("Enter the number")
	if(option==1):
		suma.add()
	if(option==2):
		ranp=raw_input("\nenter the Product u want to search\n")
		suma.search(ranp)
	if(option==3):
		suma.update_cost()
	if(option==4):
		suma.display()
	if(option==5):
		suma.calculate()
	if(option==6):
		suma.delete()
	if(option==7):
		suma.update_quantity()
	if(option==0):
		print("Your Processing ends here!TATA")



