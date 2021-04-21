from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube

Folder_Name = ""

#file location
def openLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if(len(Folder_Name) > 1):
        locationError.config(text=Folder_Name,fg="green")

    else:
        locationError.config(text="Please Choose Folder!!",fg="red")

#donwload video
def DownloadVideo():
    choice = ytdchoices.get()
    url = ytdEntry.get()

    if(len(url)>1):
        ytdError.config(text="")
        yt = YouTube(url)

        if(choice == choices[0]):
            select = yt.streams.filter(progressive=True).first()

        elif(choice == choices[1]):
            select = yt.streams.filter(progressive=True,file_extension='mp4').last()

        elif(choice == choices[2]):
            select = yt.streams.filter(only_audio=True).first()

        else:
            ytdError.config(text="Paste Link again!!",fg="red")


    #download function
    select.download(Folder_Name)
    ytdError.config(text="Download Completed!!")



root = Tk()
root.title("Youtube Downloader")
root.geometry("350x400") 
root.columnconfigure(0,weight=1)

ytdLabel = Label(root,text="Enter the URL of the Video",font=("jost",15)).grid()

ytdEntryVar = StringVar()
ytdEntry = Entry(root,width=50,textvariable=ytdEntryVar).grid()

ytdError = Label(root,text="Error Msg",fg="red",font=("jost",10)).grid()

saveLabel = Label(root,text="Save the Video File",font=("jost",15,"bold")).grid()

saveEntry = Button(root,width=10,bg="red",fg="white",text="Choose Path",command=openLocation).grid()

locationError = Label(root,text="Error Msg of Path",fg="red",font=("jost",10)).grid()

ytdQuality = Label(root,text="Select Quality",font=("jost",15)).grid()

choices = ["720p","144p","Only Audio"]
ytdchoices = ttk.Combobox(root,values=choices).grid()


downloadbtn = Button(root,text="Donwload",width=10,bg="red",fg="white",command=DownloadVideo).grid()

developerlabel = Label(root,text="---AMBUSH---",font=("jost",15))
developerlabel.grid()
root.mainloop()