from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from sqlite3 import *
import requests
import socket
import bs4
import lxml
import textwrap
from googletrans import Translator


try:
	google = ("www.google.com", 80)
	socket.create_connection(google)
	res = requests.get("https://ipinfo.io/")
	data = res.json()
	city = "Thane"

	a1 = "http://api.openweathermap.org/data/2.5/weather?units=metric"
	a2 = "&appid=c6e315d09197cec231495138183954bd"
	a3 = "&q="+city
	web_address = a1 + a2 + a3
	res = requests.get(web_address)
	data = res.json()

# write code to get temp

	main = data['main']
	temp1 = main['temp']
	v = "Temperature ", temp1
	p = "City: "+city
	
except OSError as e:
	print("issue ", e)
except KeyError as e:
	showerror("issue ", e)

try:
	google = ("www.google.com", 80)
	socket.create_connection(google)
	print("Connected")

	res = requests.get("https://www.brainyquote.com/quote_of_the_day")
	#print(res)

	s = bs4.BeautifulSoup(res.text, 'lxml')
	#print(s)

	data = s.find('img', {"class":"p-qotd"})
	#print("data ",data)

	quote = data['alt']
	
except OSError as e:
	print("issue ",e)	

#-----------------------------------------------------------------------------------------------

def f1():
	adst.deiconify()
	root.withdraw()

def f2():
	root.deiconify()
	adst.withdraw()

def f3():
	vist_stData.delete(1.0, END)
	vist.deiconify()
	root.withdraw()
	root.withdraw()
	con = None
	try:
		con = connect("student_database.db")
		cur = con.cursor()
		sql = "select * from student"
		cur.execute(sql)
		data = cur.fetchall()
		msg = ""
		for d in data:
			msg = msg + "rno: " + str(d[0]) + " name: " + str(d[1]) + " marks: " + str(d[2]) + "\n"
		vist_stData.insert(INSERT, msg)
	except Exception as e:
		showerror("Issue", e)
	finally:
		if con is not None:
			con.close()
def f4():
	root.deiconify()
	vist.withdraw()

def f5():
	con = None
	try:
		con = connect("student_database.db")
		cur = con.cursor()
		sql = "create table if not exists student(rno int primary key, name text, marks float)"
		cur.execute(sql)

		sql = "insert into student values('%d', '%s', '%f')"

#Validation for add student -----

		srno = adst_entRno.get()
		if srno.isdigit() and int(srno)>0:
			rno = int(srno)
		else:
			showerror("Mistake", "rno should all be integers")
			adst_entRno.delete(0, END)
			adst_entRno.focus()
			return
		rno = int(srno)
		name = adst_entName.get()
		if not name.isalpha():
			showerror("Mistake", "name should contain alphabets only")
		elif len(name) <= 1:
			showerror("Mistake","Minimum length of Name is 2")
			adst_entName.delete(0, END)
			adst_entName.focus()
			return
		
		smarks = adst_entMarks.get()
		if not smarks.isdigit or (int(smarks)<= 0 or int(smarks)>=100):
			showerror("Mistake", "Marks out of range")
			adst_entMarks.delete(0, END)
			adst_entMarks.focus()
			return
		marks = int(smarks)

#validation ends -----
		
		cur.execute(sql % (rno, name, marks))
		con.commit()
		showinfo("Success", "row inserted")

	except Exception as e:
		con.rollback()
		showerror("Issue", e)
	finally:
		if con is not None:
			con.close()
	adst_entRno.delete(0, END)
	adst_entName.delete(0, END)
	adst_entMarks.delete(0, END)
	adst_entRno.focus()


def f6():
	root.withdraw()
	upst.deiconify()

def f7():
	root.deiconify()
	upst.withdraw()

def f8():
	root.withdraw()
	dest.deiconify()
		
def f9():
	root.deiconify()
	dest.withdraw()

def f10():
	con = None
	try:
		con = connect("student_database.db")
		cur = con.cursor()
		sql = "update student set name = '%s', marks = '%f' where rno = '%d'"
		
#Validation for update student -----
		
		urno = upst_entRno.get()
		if urno.isdigit() and int(urno) > 0:
			rno = int(urno)		
		else:
			showerror("Mistake", "Incorrect Rno")
			upst_entRno.delete(0, END)
			upst_entRno.focus()
			return
		
		uname = upst_entName.get()
		if not uname.isalpha():
			showerror("Mistake", "Incorrect Name")
			upst_entName.delete(0, END)
			upst_entName.focus()
			return
		elif  len(uname) <= 1:
			showerror("Mistake","Minimum length of Name is 2")
			adst_entName.delete(0, END)
			adst_entName.focus()
			return
		name = uname		
	
		umarks = upst_entMarks.get()
		if umarks.isdigit() and (int(umarks)>= 0 or int(umarks)<=100):
			marks = int(umarks)
		else:
			showerror("Mistake", "Marks out of range")
			#upst_entMarks.delete(0, END)
			upst_entMarks.focus()
			return
		
#validation ends -----

		cur.execute(sql % (name, marks, rno))
		con.commit()
		if cur.rowcount > 0:
			showinfo("Sucsess", "Row Updated ")
		else:
			showerror("Failure", "Record does not exists")
		
	except Exception as e:
		con.rollback()
		showerror("Issue", e)
	finally:
		if con is not None:
			con.close()
	upst_entRno.delete(0, END)
	upst_entName.delete(0, END)
	upst_entMarks.delete(0, END)
	upst_entRno.focus()


def f11():
	con = None
	try:
		con = connect("student_database.db")
		cur = con.cursor()
		sql = "DELETE FROM student WHERE rno = '%d'"

#validation for delete student -----

		drno = dest_entRno.get()
		
		if drno.isdigit() and int(drno)> 0 :
			rno = int(drno)
		else:
			showerror("Error", "Incorrect Rno")
			dest_entRno.focus()
			return
#Validation ends -----
	
		cur.execute(sql % (rno))
		con.commit()
		if cur.rowcount > 0:
			msg = str(cur.rowcount) + " record deleted"
			showinfo("Success", msg)
		else:
			showerror("Error", "Oops...! Rno doesn't Exists")
		dest_entRno.delete(0, END)
		dest_entRno.focus()
		
		
	except Exception as e:
		con.rollback()
		showerror("Issue", e)
	finally:
		if con is not None:
			con.close()
	dest_entRno.delete(0, END)
	dest_entRno.focus()

def f12():
	import matplotlib.pyplot as plt
	import pandas as pd
	import numpy as np
	
	con = None
	try:
		con = connect("student_database.db")
		cur = con.cursor()
		sql = "select name, marks from student"
		cur.execute(sql)
		value = cur.fetchall()
		name = []
		marks = []
		for d in value:
			name.append(d[0])
			marks.append(d[1])		
		plt.bar(name, marks, linewidth = 1.5, color = ('green')) 				
		plt.xlabel("Names")
		plt.ylabel("Marks")
		plt.title("Student Database")
		plt.grid()
	
		plt.show()
	
	except Exception as e:
		con.rollback()
		showerror("Issue", e)
	finally:
		if con is not None:
			con.close()

#-----------------------------------------------------------------------------------------------
#Student Mgmt System

root=Tk()
root.title("S.M.S")
root.geometry("600x600+430+100")
root.resizable(True,True)
root.configure(background = 'spring green')

btnAdd = Button(root, text= 'Add', width =10, background = 'RosyBrown3', font=('arial', 15, 'bold'), command = f1)
btnView = Button(root, text= 'View', width =10, background = 'navajo white', font=('arial', 15, 'bold'), command = f3)
btnUpdate = Button(root, text= 'Update', width =10, background = 'RosyBrown3', font=('arial', 15, 'bold'), command = f6)
btnDelete = Button(root, text= 'Delete', width =10, background = 'navajo white', font=('arial', 15, 'bold'), command = f8)
btnChart = Button(root, text= 'Charts', width =10, background = 'RosyBrown3', font=('arial', 15, 'bold'), command = f12)

btnAdd.pack(pady = 10)
btnView.pack(pady = 10)
btnUpdate.pack(pady = 10)
btnDelete.pack(pady = 10)
btnChart.pack(pady = 10)

# Location -----------------------------------------------------------------------------------

c = Label(root, text = p, width = 15, height = 2,background = 'black', foreground = 'white', font=('arial', 15, 'bold'))
c.pack(pady = 10)

# Temperature ---------------------------------------------------------------------------------

w = Label(root, text=v , width = 20, height = 2, background = 'black', foreground = 'white', font=('arial',15,'bold'))
w.pack(pady=2)

# QOTD ---------------------------------------------------------------------------------------

wrapper = textwrap.TextWrapper(width=45)
word_list = wrapper.fill(text=quote)
quotes = "Quote: " + word_list
q = Label(root, text =quotes, height = 7, background = 'black', foreground = 'cyan', font=('arial',15,'bold'))
q.pack(pady=10, padx=30) 

#-----------------------------------------------------------------------------------------------


def on_close():
	if askokcancel("Quit", "Do you want to leave..?"):
		root.destroy()
root.protocol("WM_DELETE_WINDOW", on_close)


#-----------------------------------------------------------------------------------------------
#Add St.

adst = Toplevel(root)
adst.title("Add St.")
adst.geometry("600x600+430+100")
adst.configure(background = 'deep sky blue')

adst_lblRno = Label(adst, text="Enter Rno", background = 'dark slate gray', foreground = 'white', font=('arial', 15, 'bold'))
adst_lblName = Label(adst, text="Enter Name", background = 'dark slate gray', foreground = 'white', font=('arial', 15, 'bold'))
adst_lblMarks = Label(adst, text="Enter Marks", background = 'dark slate gray', foreground = 'white', font=('arial', 15, 'bold'))
adst_entRno = Entry(adst, bd=5, font=('arial', 15, 'bold'))
adst_entName = Entry(adst, bd=5, font=('arial', 15, 'bold'))
adst_entMarks = Entry(adst, bd=5, font=('arial', 15, 'bold'))
adst_btnSave = Button(adst, text="Save", background = 'black', foreground = 'white', font=('arial', 15, 'bold'), command = f5)
adst_btnBack = Button(adst, text="Back", background = 'black', foreground = 'white', font=('arial', 15, 'bold'), command = f2)

adst_lblRno.pack(pady = 10)
adst_entRno.pack(pady = 10)
adst_lblName.pack(pady = 10)
adst_entName.pack(pady = 10)
adst_lblMarks.pack(pady = 10)
adst_entMarks.pack(pady = 10)
adst_btnSave.pack(pady = 40)
adst_btnBack.pack(pady = 10)

adst.withdraw()

#-----------------------------------------------------------------------------------------------
# View St.

vist = Toplevel(root)
vist.title("View St.")
vist.geometry("600x600+430+100")
vist.configure(background = 'DeepPink4')

vist_stData = ScrolledText(vist, width = 50, height = 15, background = 'snow', font=('Times new roman', 14, 'bold'))
vist_btnBack = Button(vist, text="Back", background = 'snow', font = ('arial', 15, 'bold'), command = f4)

vist_stData.pack(pady=30)
vist_btnBack.pack(pady = 10)

vist.withdraw()

#-----------------------------------------------------------------------------------------------
#Update St.

upst = Toplevel(root)
upst.title("Update St.")
upst.geometry("600x600+430+100")
upst.resizable(False,False)
upst.configure(background = 'dark slate grey')

upst_lblRno = Label(upst, text="Enter Rno", background = 'thistle', font=('arial', 15, 'bold'))
upst_lblName = Label(upst, text="Enter Name", background = 'thistle', font=('arial', 15, 'bold'))
upst_lblMarks = Label(upst, text="Enter Marks", background = 'thistle', font=('arial', 15, 'bold'))
upst_entRno = Entry(upst, bd=5, font=('arial', 15, 'bold'))
upst_entName = Entry(upst, bd=5, font=('arial', 15, 'bold'))
upst_entMarks = Entry(upst, bd=5, font=('arial', 15, 'bold'))
upst_btnSave = Button(upst, text="Save", font=('arial', 15, 'bold'), command = f10)
upst_btnBack = Button(upst, text="Back", font=('arial', 15, 'bold'), command = f7)

upst_lblRno.pack(pady = 10)
upst_entRno.pack(pady = 10)
upst_lblName.pack(pady = 10)
upst_entName.pack(pady = 10)
upst_lblMarks.pack(pady = 10)
upst_entMarks.pack(pady = 10)
upst_btnSave.pack(pady = 40)
upst_btnBack.pack(pady = 10)

upst.withdraw()

#-----------------------------------------------------------------------------------------------
#Delete St.

dest = Toplevel(root)
dest.title("Delete St.")
dest.geometry("600x600+430+100")
dest.resizable(False,False)
dest.configure(background = 'OliveDrab2')

dest_lblRno = Label(dest, text="Enter Rno", background = 'black', foreground = 'white', font=('arial', 15, 'bold'))
dest_entRno = Entry(dest, bd=5, font=('arial', 15, 'bold'))
dest_btnSave = Button(dest, text="Save",background = 'black', foreground = 'white', font=('arial', 15, 'bold'), command = f11)
dest_btnBack = Button(dest, text="Back", background = 'black', foreground = 'white', font=('arial', 15, 'bold'), command = f9)
dest_btnView = Button(dest, text="View", background = 'black', foreground = 'white', font=('arial', 15, 'bold'), command = f3)

dest_lblRno.pack(pady = 15)
dest_entRno.pack(pady = 15)
dest_btnSave.pack(pady = 40)
dest_btnBack.pack(pady = 10)
dest_btnView.pack(pady = 10)

dest.withdraw()

root.mainloop()
