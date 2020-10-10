from cryptography.fernet import Fernet
from tkinter import *
from tkinter import messagebox
from onLogin import onLoginf
import os

keyE= b'WC6G-mXyKNWcd-DVAaeQ9I3Q_yUP4bqhKcObnL8t2bg='

def delete():
	print("yo")


def delete1():
	screen1.destroy()

def login_success():
	global screen3
	screen3 = Toplevel(screen)
	screen3.title("Login Successful")
	screen3.geometry("250x100+300+300")
	Label(screen3, text="Login Successful").pack()
	Button(screen3, text="OK", padx="20", command=delete3).pack()

def delete3():
	screen3.destroy()
	screen.destroy()
	# onLoginf()

def password_error():
	global screen4
	screen4 = Toplevel(screen)
	screen4.title("Login Error")
	screen4.geometry("250x100+300+300")
	Label(screen4, text="Password not recongnized. Please try again.").pack()
	Button(screen4, text="OK", padx="20", command=delete4).pack()


def delete4():
	screen4.destroy()

def user_not_found():
	global screen5
	screen5 = Toplevel(screen)
	screen5.title("User not found")
	screen5.geometry("250x100+300+300")
	Label(screen5, text="User not found").pack()
	Button(screen5, text="OK", padx="20",command=delete5).pack()

def delete5():
	screen5.destroy()



def Submit():
	usernamesub = usernamemain.get()
	passwordsub = passwordmain.get()
	x= passwordsub.encode()

	# userEntryMain.delete(0, END)
	passEntryMain.delete(0, END)

	listfiles = os.listdir()
	if usernamesub in listfiles:
		f=Fernet(keyE)
		file1 =open(usernamesub, "rb")
		verify =file1.read().splitlines()
		y=verify[1]
		# print(verify.decode())
		decryptUP=f.decrypt(y)
		# print(decryptUP)

		if x in decryptUP:
			login_success()
		else:
			password_error()
	else:
		user_not_found()

# def alrdelete():
	# ALR.destroy()

def passwordMatch():
	username_info=username.get()
	password1_info=password1.get()
	password2_info=password2.get()
	global userE
	global passE
	global encryptU
	global encryptP

	listfiles1 = os.listdir()
	
	if username_info=="" or password1_info=="" or password2_info=="":
		messagebox.showinfo('Error', 'All fields required')
	elif username_info in listfiles1:
		Label(screen1, text="Username already exists." ,font=("Calibri", 10), fg="red").pack()
		userEntry.delete(0, END)
	elif password1_info==password2_info:
		Label(screen1, text="Registration Successful! You may now login.", font=("Calibri", 10), fg="green").pack()

		file=open(username_info, "wb")
		userE = username_info.encode()
		passE = password1_info.encode()
		f=Fernet(keyE)
		encryptU= f.encrypt(userE)
		encryptP = f.encrypt(passE)

		file.write(encryptU+b"\n")
		file.write(encryptP)
		file.close()
		Button(screen1, text="OK", padx="20", command=delete1).pack()
	else:	
		Label(screen1, text="Password does not match. Please try again.", font=("Calibri", 10), fg="red").pack()

	
	pass1Entry.delete(0, END)
	pass2Entry.delete(0, END)

def Register():
	global screen1
	screen1=Toplevel (screen)
	screen1.title("Register")
	screen1.geometry("300x350+300+150")

	global username
	global password1
	global password2
	global userEntry
	global pass1Entry
	global pass2Entry

	username=StringVar()
	password1=StringVar()
	password2=StringVar()

	Label(screen1, text="Enter Username").pack()
	userEntry= Entry(screen1, textvariable=username, width=40)
	# listfiles1 = os.listdir()
	# print(listfiles1)
	# if userEntry in listfiles1:
	# 	print("user already exists")
	# else:
	userEntry.pack()
	Label(screen1, text=" ").pack()
	Label(screen1, text="Enter Password").pack()
	pass1Entry =Entry(screen1, textvariable=password1, show="*", width=40)
	pass1Entry.pack()
	Label(screen1, text=" ").pack()
	Label(screen1, text="Confirm Password").pack()
	pass2Entry= Entry(screen1, textvariable=password2, show="*", width=40)
	pass2Entry.pack()
	Label(screen1, text=" ").pack()
	Button(screen1, text="Confirm", height=2, width=30, command=passwordMatch).pack()
	

def Main():
	global screen
	screen = Tk()
	screen.geometry("380x450+350+150")
	screen.title("Encrypted Login System 1.10")
	# screen.configure(background="white")
	Label(screen, text="Encrypted Login System 1.10", bg="grey", width="300", height="2", font=("Calibri", 14)).pack()
	Label(screen, text="").pack()

	global usernamemain
	global passwordmain
	global userEntryMain
	global passEntryMain

	usernamemain = StringVar()
	passwordmain = StringVar()

	Label(screen, text="Username:").pack()
	userEntryMain=Entry(screen,width=40, textvariable=usernamemain)
	userEntryMain.pack()
	Label(screen, text=" ").pack()
	Label(screen, text="Password").pack()
	passEntryMain=Entry(screen, width=40, textvariable=passwordmain, show="*")
	passEntryMain.pack()
	Label(screen, text=" ").pack()
	Button(screen, text="Submit", height=2, width=30, command=Submit).pack()
	Label(screen, text=" ").pack()
	Label(screen, text="First time? Register your password").pack()
	Label(screen, text=" ").pack()
	Button(screen, text="Register", height=2, width=30, command=Register).pack()
	Label(screen, text=" ").pack()
	Label(screen, text=" ").pack()
	Label(screen, text=" ").pack()
	Label(screen, text=" ").pack()
	Label(screen, text="Created by Shridhar Kamma",font=("Calibri", 10), fg="black" ).pack()



	screen.mainloop()

Main()

