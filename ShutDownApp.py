from tkinter import *
import os
def restart():
    os.system("shutdown /r /t 1")
def restart_time():
    os.system("shutdown /r /t 20")
def logout():
    os.system("shutdown -l")
def shutdown():
    os.system("shutdown /s /t 1")

st=Tk()
st.title("Shutdown App")
st.geometry("300x400")
r_button = Button(st,text="Restart",font=("Time New Roman",18,"bold"),relief=RAISED, cursor="plus",command=restart)
r_button.place(x=100,y=50-30,height=50,width=100)
Sh_button = Button(st,text="ShutDown",font=("Time New Roman",13,"bold"),relief=RAISED, cursor="plus",command=shutdown)
Sh_button.place(x=100,y=150-30,height=50,width=100)
Sl_button = Button(st,text="Restart With Time",font=("Time New Roman",7,"bold"),relief=RAISED, cursor="plus",command=restart_time)
Sl_button.place(x=100,y=250-30,height=50,width=100)
Lg_button = Button(st,text="Logout",font=("Time New Roman",18,"bold"),relief=RAISED, cursor="plus",command=logout)
Lg_button.place(x=100,y=350-30,height=50,width=100)




st.mainloop()

print("Succes")