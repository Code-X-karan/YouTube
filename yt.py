from tkinter import *
from tkinter import messagebox
import yt_dlp
window=Tk()
window.config(bg="#edebeb")
window.title("YT Downloader")
window.geometry("425x550")
window.minsize(425,550)
window.maxsize(425,550)
## defined input var
url=StringVar()
default_format=StringVar()
Format=['Audio .mp3','Video .mp4']
default_format.set("Choose format")


def download(): ## defined downlaod function
    fetched_url=url.get()

    if(fetched_url==""): ## check input is blank or not
        messagebox.showerror("YT Downloader","Input can't be blank")

    elif(default_format.get()=="Choose format"): ## check user select format or not
        messagebox.showerror("YT Downloader","Select any format")

    elif(default_format.get()=="Video .mp4"): ## downlaod file in video format
        yt_dlp.YoutubeDL({'format':'best','outtmpl':'%(title)s.%(ext)s'}).download([fetched_url])
        messagebox.showinfo("YT Downloader","Download completed ! Enjoy ")


    elif(default_format.get()=="Audio .mp3"): ##download file in audio
        yt_dlp.YoutubeDL({'format':'bestaudio','outtmpl':'%(title)s.%(ext)s'}).download([fetched_url])
        messagebox.showinfo("YT Downloader","Download completed ! Enjoy ")

Label(window,text="").pack(pady=10) ##blank space at top
Label(window,text="📺 You Tube ",font=("calibri",21,"bold"),foreground="#FFFFFF",background="#FF0000").pack(fill=X)
Label(window,text="  video downloader ⬇",font=("calibri",13,""),foreground="#FFFFFF",background="#FF0000").pack(fill=X)
Label(window,text="Enter a Valid You Tube URL: ",font=("Calibri",13," ")).pack(pady=15)
Entry(window,textvariable=url,width=50).pack()
OptionMenu(window,default_format,*Format).pack(pady=5) ##drop down menu
Button(window,text="Download",font=("calibri","12","bold"),bg="#1568bf",fg="#FFFFFF",command=download).pack(pady=10)
Label(window,text="Made by Code-X-Karan",font=("calibri",9,"")).pack(side="bottom")

window.mainloop()