#from functions import *
from tkinter import *
from subprocess import Popen,PIPE
import subprocess
import os
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import ttk
import pandas as  pd
import numpy as np
from PIL import ImageTk, Image
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

nice_data= pd.DataFrame()
def password():
    passwd = simpledialog.askstring("Password","Enter your password",show="*",parent=window)
    return passwd

def changefile():
    user=user_type.get()
    operator=operation_type.get()
    permisson=permissons_type.get()
    path=path_type.get()
    print(permisson)
    if(user=='' and operator=='' and permision=='' and path==''):
            messagebox.showinfo("WARNING: ", "enter valid details")
    else:
        password1=password()
        command="echo "+password1+" | sudo -S chmod "+user+""+operator+""+permisson+" "+path+""
        subprocess.call(command,shell=True)
        messagebox.showinfo("sucess", "permissions updated")
        fileframe()

def changedir():
    user=user_type1.get()
    operator=operation_type1.get()
    permisson=permissons_type1.get()
    path=path_type1.get()
    if(user=='' and operator=='' and permision=='' and path==''):
            messagebox.showinfo("WARNING: ", "enter valid details")
    else:
        password1=password()
        command="echo "+password1+" | sudo -S chmod "+user+""+operator+""+permisson+" "+path+""
        subprocess.call(command,shell=True)
        messagebox.showinfo("sucess", "permissions updated")
        dirframe()


def umask_file():
    umask=umask_type.get()
    default="-rw-rw-rw-"
    file=[]
    if(len(umask)<10):
            messagebox.showinfo("warning", "Enter the valid permissions")
    else:
        for i in range(len(umask)):
            if(i==0):
                file.append(default[0])
            else:
                if(default[i]==umask[i]):
                    file.append(default[i])
                else:
                    file.append("-")

        file_permission=''.join(file)
        print(file_permission)
        value_file(file_permission)


def umask_dir():
    umask=umask_type.get()
    default="-rwxrwxrwx"
    file=[]
    if(len(umask)<10):
            messagebox.showinfo("warning", "Enter the correct permissions")
    else:
        for i in range(len(umask)):
            if(i==0):
                file.append(default[0])
            else:
                if(default[i]==umask[i]):
                    file.append(default[i])
                else:
                    file.append("-")

        file_permission=''.join(file)
        print(file_permission)
        value_dir(file_permission)

def add():
    user=username.get()
    group=groupname.get()
    file_path=add_file.get()
    permision=add_perm.get()
    option=add_option.get()
    command=''
    if(option==''):
        messagebox.showinfo("WARNING", "please select user or group")

    if (option=='u'):
        if(file_path=='' and user=='' and permision==''):
            messagebox.showinfo("WARNING", "please enter details correctly")
        else:
            password1=password()
            command="echo "+password1+" | sudo -S setfacl -m u:"+user+":"+permision+" "+file_path+""
            subprocess.call(command,shell=True)
            messagebox.showinfo("SUCESS", "permissions changed")
            acess_frame()

    if (option=='g'):
        if(file_path=='' and group=='' and permision==''):
            messagebox.showinfo("WARNING", "please enter details correctly")
        else:
            password1=password()
            command="echo "+password1+" | sudo -S setfacl -m g:"+group+":"+permision+" "+file_path+""
            subprocess.call(command,shell=True)
            messagebox.showinfo("SUCESS", "permissions changed")
            acess_frame()
    #print(command)



def remove():
    user=username.get()
    group=groupname.get()
    file_path=remove_file.get()
    permision=remove_perm.get()
    option=remove_option.get()

    if(option==''):
        messagebox.showinfo("WARNING", "please select user or group")

    if (option=='u'):
        if(file_path=='' and user==''):
            messagebox.showinfo("WARNING", "please enter details correctly")
        else:
            password1=password()
            command="echo "+password1+" | sudo -S setfacl -x "+user+" "+file_path+""
            subprocess.call(command,shell=True)
            messagebox.showinfo("SUCESS", "permissions changed")
            acess_frame2()
    if (option=='g'):
        if(file_path=='' and group=='' and permision==''):
            messagebox.showinfo("WARNING", "please enter details correctly")
        else:
            password1=password()
            command="echo "+password1+" | sudo -S setfacl -x "+group+" "+file_path+""
            subprocess.call(command,shell=True)
            messagebox.showinfo("SUCESS", "permissions changed")
            acess_frame2()




window = Tk()
window.configure(background='lavender')

window.title('SYSTEM ADMIN TOOL TO MAINATAIN FILESYSTEM')
note = ttk.Notebook(window)

tab1 = ttk.Frame(note)
tab2 = ttk.Frame(note)
tab3 = ttk.Frame(note)
#tab4 = ttk.Frame(note)

note.add(tab1, text = "PERMISSIONS")
note.add(tab2, text = "UMASK")
note.add(tab3, text = "ACESS CONTROL")
#note.add(tab4, text = "CONTROL")

note.pack(expand=1,fill="both")

#-----------------------------tab1 content---------------------------------------
users = ['u', 'g', 'o', 'ug','go', 'ou','a']
operation=['+','=','-']
permissons=['x','w','wx','r','rx','rw','rwx']


user_type=StringVar()
operation_type=StringVar()
permissons_type=StringVar()
path_type=StringVar()

user_type1=StringVar()
operation_type1=StringVar()
permissons_type1=StringVar()
path_type1=StringVar()

def fileframe():

    tab1_frame1 =LabelFrame(tab1,text="CHANGING DEFAULT PERMISSIONS OF FILE:",fg="brown",font="15",bg="lavender",bd=5,width=500, height=80)
    tab1_frame1.grid(row=1, column=1,padx=50,pady=15)

    label1=Label(tab1_frame1,text="ENTER YOUR PATH FOR FILE: ")
    label1.grid(row=2,column=1,padx=10,pady=5)
    #path_type=StringVar()
    entry1 =Entry(tab1_frame1,textvariable=path_type)
    entry1.grid(row=2,column=3,padx=10,pady=5)

    label1=Label(tab1_frame1,text="SELECTING YOUR USER TYPE ")
    label1.grid(row=3,column=1,padx=10,pady=5)
    label1=Label(tab1_frame1,text="SELECTING YOUR OPERATION ")
    label1.grid(row=4,column=1,padx=10,pady=5)
    label1=Label(tab1_frame1,text="SELECTING YOUR PERMISSIONS ")
    label1.grid(row=5,column=1,padx=10,pady=5)

    option1 = OptionMenu(tab1_frame1, user_type, *users)
    option1.grid(row=3,column=2,columnspan=2,padx=8, pady=5)
    option2 = OptionMenu(tab1_frame1, operation_type, *operation)
    option2.grid(row=4,column=2,columnspan=2,padx=8, pady=5)
    option3 = OptionMenu(tab1_frame1, permissons_type, *permissons)
    option3.grid(row=5,column=2,columnspan=2,padx=8, pady=5)

    button1 =Button (tab1_frame1, text='submit',bg="orange", command=changefile)
    button1.grid(row=6,column=2,padx=10,pady=5)



#-------------------------FRAME2------------IN TAB1-----------------------

def dirframe():

    tab1_frame2 =LabelFrame(tab1,text="CHANGING DEFAULT PERMISSIONS OF DIRECTORY:",fg="brown",font="15",bg="lavender",bd=5,width=500, height=80)
    tab1_frame2.grid(row=2, column=1,padx=50,pady=15)


    label1=Label(tab1_frame2,text="ENTER YOUR PATH FOR FILE: ")
    label1.grid(row=2,column=1,padx=10,pady=5)
    #path_type=StringVar()
    entry1 =Entry(tab1_frame2,textvariable=path_type1)
    entry1.grid(row=2,column=3,padx=10,pady=5)
    #user_type=StringVar()
    #operation_type=StringVar()
    #permissons_type=StringVar()
    label1=Label(tab1_frame2,text="SELECTING YOUR USER TYPE ")
    label1.grid(row=3,column=1,padx=10,pady=5)
    label1=Label(tab1_frame2,text="SELECTING YOUR OPERATION ")
    label1.grid(row=4,column=1,padx=10,pady=5)
    label1=Label(tab1_frame2,text="SELECTING YOUR PERMISSIONS ")
    label1.grid(row=5,column=1,padx=10,pady=5)

    option1 = OptionMenu(tab1_frame2, user_type1, *users)
    option1.grid(row=3,column=2,columnspan=2,padx=8, pady=5)
    option2 = OptionMenu(tab1_frame2, operation_type1, *operation)
    option2.grid(row=4,column=2,columnspan=2,padx=8, pady=5)
    option3 = OptionMenu(tab1_frame2, permissons_type1, *permissons)
    option3.grid(row=5,column=2,columnspan=2,padx=8, pady=5)

    button1 =Button (tab1_frame2, text='submit',bg="orange", command=changedir)
    button1.grid(row=6,column=2,padx=10,pady=5)

fileframe()

dirframe()


button1 =Button (tab1, text='Exit',bg="red", command=window.destroy)
button1.grid(row=10,column=4,padx=10,pady=5)


#-----------------------------tab2 content---------------------------------------

tab2_frame1 =LabelFrame(tab2,text="CHANGING DEFAULT FILE PERMISSIONS:",fg="saddle brown",bg="lavender",font='15',bd=4,width=500, height=80)
tab2_frame1.grid(row=1, column=1,padx=80,pady=15)
tab2_frame2 =LabelFrame(tab2,text="CHANGING DEFAULT FILE PERMISSIONS:",fg="saddle brown",bd=4,bg="lavender",font='15',width=500, height=80)
tab2_frame2.grid(row=3, column=1,padx=80,pady=15)

label1=Label(tab2_frame1,text="ENTER UMASK VALUE: ")
label1.grid(row=2,column=1,padx=10,pady=5)
umask_type=StringVar()
entry1 =Entry(tab2_frame1,textvariable=umask_type)
entry1.grid(row=2,column=3,padx=10,pady=5)

file_permission=StringVar()


button1 =Button (tab2_frame1, text='submit',bg="orange", command=umask_file)
button1.grid(row=4,column=3,padx=10,pady=5)

def value_file(file_permission):
    label1=Label(tab2_frame1,text="DEFAULT PERMISSIONS OF FILE IS:")
    label1.grid(row=5,column=1,padx=10,pady=5)
    label1=Label(tab2_frame1,text=file_permission,width=15,borderwidth=2,relief="raised",bg="pink",font=("Helvetica", 16))
    label1.grid(row=6,column=2,padx=10,pady=5)

#-------------------------------directory permissions----------------
label1=Label(tab2_frame2,text="ENTER UMASK VALUE: ")
label1.grid(row=2,column=1,padx=10,pady=5)
umask_type=StringVar()
entry1 =Entry(tab2_frame2,textvariable=umask_type)
entry1.grid(row=2,column=3,padx=10,pady=5)

file_permission=StringVar()


button1 =Button (tab2_frame2, text='submit',bg="orange", command=umask_dir)
button1.grid(row=4,column=3,padx=10,pady=5)

def value_dir(file_permission):
    label1=Label(tab2_frame2,text="DEFAULT PERMISSIONS OF DIRECTORY IS:")
    label1.grid(row=5,column=1,padx=10,pady=5)
    label1=Label(tab2_frame2,text=file_permission,width=15,borderwidth=2,relief="raised",bg="pink",font=("Helvetica", 16))
    label1.grid(row=6,column=2,padx=10,pady=5)


button1 =Button (tab2, text='Exit',bg="red", command=window.destroy)
button1.grid(row=7,column=5,padx=10,pady=5)

#--------------------------------------TAB3-------------------------------------------------------
permision=['--x','-w-','r--','-wx','r-x','rw-','rwx']

username=StringVar()
groupname=StringVar()
add_file=StringVar()
remove_file=StringVar()
add_perm=StringVar()
remove_perm=StringVar()
add_option=StringVar()
remove_option=StringVar()

tab3_frame1 =LabelFrame(tab3,text="ADD PERMISSIONS:",fg="saddle brown",bg="lavender",font='15',bd=4,width=500, height=80)
tab3_frame1.grid(row=1, column=1,padx=80,pady=15)

tab3_frame2 =LabelFrame(tab3,text="REMOVE PERMISSIONS:",fg="saddle brown",bd=4,bg="lavender",font='15',width=500, height=80)
tab3_frame2.grid(row=3, column=1,padx=80,pady=15)

def acess_frame():
    label1=Label(tab3_frame1,text="ENTER YOUR PATH FOR FILE: ")
    label1.grid(row=2,column=1, padx=10,pady=5)
    #path_type=StringVar()
    entry1 =Entry(tab3_frame1,textvariable=add_file)
    entry1.grid(row=2,column=2,columnspan=2,padx=10,pady=5)

    label1=Label(tab3_frame1,text="SELECTING USER TYPE :")
    label1.grid(row=3,column=1,padx=5,pady=5)
    radio1=Radiobutton(tab3_frame1,text="GROUP",padx =10,variable=add_option,command=group_detail,value='g')
    radio1.grid(row=3,column=2,padx=5,pady=5)
    radio1=Radiobutton(tab3_frame1,text="USER",padx =10,variable=add_option,command=user_detail,value='u')
    radio1.grid(row=3,column=3,padx=10,pady=5)

def acess_frame2():

    label1=Label(tab3_frame2,text="ENTER YOUR PATH FOR FILE: ")
    label1.grid(row=2,column=1, padx=10,pady=5)
    #path_type=StringVar()
    entry1 =Entry(tab3_frame2,textvariable=remove_file)
    entry1.grid(row=2,column=2,columnspan=2,padx=10,pady=5)

    label1=Label(tab3_frame2,text="SELECTING USER TYPE :")
    label1.grid(row=3,column=1,padx=5,pady=5)
    radio1=Radiobutton(tab3_frame2,text="GROUP",padx =10,variable=remove_option,command=group_detail1,value='g')
    radio1.grid(row=3,column=2,padx=5,pady=5)
    radio1=Radiobutton(tab3_frame2,text="USER",padx =10,variable=remove_option,command=user_detail1,value='u')
    radio1.grid(row=3,column=3,padx=10,pady=5)


def group_detail():
    #print(add_option.get())
    label1=Label(tab3_frame1,text="ENTER YOUR GROUPNAME: ")
    label1.grid(row=4,column=1, padx=10,pady=5)
    #path_type=StringVar()
    entry1 =Entry(tab3_frame1,textvariable=groupname)
    entry1.grid(row=4,column=2,columnspan=2,padx=10,pady=5)

    label1=Label(tab3_frame1,text="SELECTING YOUR PERMISSIONS ")
    label1.grid(row=5,column=1,padx=10,pady=5)

    option1 = OptionMenu(tab3_frame1,add_perm, *permision)
    option1.grid(row=5,column=2,columnspan=2,padx=8, pady=5)

    button1 =Button (tab3_frame1, text='submit',bg="orange",command=add)
    button1.grid(row=6,column=1,columnspan=3,padx=10,pady=5)

def user_detail():
    print(add_option.get())

    label1=Label(tab3_frame1,text="ENTER YOUR USERNAME: ")
    label1.grid(row=4,column=1, padx=10,pady=5)
    #path_type=StringVar()
    entry1 =Entry(tab3_frame1,textvariable=username)
    entry1.grid(row=4,column=2,columnspan=2,padx=10,pady=5)

    label1=Label(tab3_frame1,text="SELECTING YOUR PERMISSIONS ")
    label1.grid(row=5,column=1,padx=10,pady=5)

    option1 = OptionMenu(tab3_frame1,add_perm, *permision)
    option1.grid(row=5,column=2,columnspan=2,padx=8, pady=5)

    button1 =Button (tab3_frame1, text='submit',bg="orange",command=add)
    button1.grid(row=6,column=1,columnspan=3,padx=10,pady=5)

def group_detail1():
    print(remove_option.get())

    label1=Label(tab3_frame2,text="ENTER YOUR GROUPNAME: ")
    label1.grid(row=4,column=1, padx=10,pady=5)
    #path_type=StringVar()
    entry1 =Entry(tab3_frame2,textvariable=groupname)
    entry1.grid(row=4,column=2,columnspan=2,padx=10,pady=5)

    #label1=Label(tab3_frame2,text="SELECTING YOUR PERMISSIONS")
    #label1.grid(row=5,column=1,padx=10,pady=5)

    #option1 = OptionMenu(tab3_frame2,remove_perm, *permision)
    #option1.grid(row=5,column=2,columnspan=2,padx=8, pady=5)

    button1 =Button (tab3_frame2, text='submit',bg="orange",command=remove)
    button1.grid(row=6,column=1,columnspan=3,padx=10,pady=5)

def user_detail1():

    print(remove_option.get())

    label1=Label(tab3_frame2,text="ENTER YOUR USERNAME: ")
    label1.grid(row=4,column=1, padx=10,pady=5)
    #path_type=StringVar()
    entry1 =Entry(tab3_frame2,textvariable=username)
    entry1.grid(row=4,column=2,columnspan=2,padx=10,pady=5)

    #label1=Label(tab3_frame2,text="SELECTING YOUR PERMISSIONS")
    #label1.grid(row=5,column=1,padx=10,pady=5)

    #option1 = OptionMenu(tab3_frame2,remove_perm, *permision)
    #option1.grid(row=5,column=2,columnspan=2,padx=8, pady=5)


    button1 =Button (tab3_frame2, text='submit',bg="orange",command=remove)
    button1.grid(row=6,column=1,columnspan=3,padx=10,pady=5)

acess_frame()
acess_frame2()


window.mainloop()
exit()
