from tkinter import *
from tkinter import filedialog, Text
import time
import pathlib
import os
from configparser import ConfigParser
import filewatch

root = Tk() #outer body of window
root.title("KingMarti's File Prep Bot")
#global Variables
file_in = ""
file_out = ""
_mp4 = IntVar()
_mov =IntVar()
_wmv =IntVar()
_4k = IntVar()
_1080p =IntVar()
_720p = IntVar()
_sd_16_9=IntVar()
_sd_4_3=IntVar()
error_format = ""
error_res =""
config = ConfigParser()

#file Input Selection
def in_select():
    input_file=filedialog.askdirectory(initialdir="/")
    global file_in
    file_in = input_file
    file_in_label= Label(frame,text=file_in)
    file_in_label.grid(row=1,column=1)  
    
#File output Selection
def out_select():
    output_file=filedialog.askdirectory(initialdir="/")
    global file_out
    file_out = output_file
    file_out_label=Label(frame,text=file_out)
    file_out_label.grid(row=2,column=1)
#Error Popup
def error():
    popup = Tk()
    popup.wm_title("! ERROR !")
    if error_res == 1 or error_format ==1:
        error_message="Required Options Were Not Selected \n Please Check that you have selected a minimum of 1 resolution and 1 file format"
    label = Label(popup, text=error_message)
    label.pack()
    b1 = Button(popup, text="Okay",command=popup.destroy)
    b1.pack()
    print("it's kind of working")
#Run Script
def run_FileWatch():
    config['app_settings'] = {
    'fileWatch' : file_in,
    'file_out' : file_out,
    '_mp4' : _mp4.get(),
    '_wmv': _wmv.get(),
    '_mov' : _mov.get(),
    '_1080' : _1080p.get(),
    '_720' : _720p.get(),
    '_4k' : _4k.get(),
    '_sd_16_9' : _sd_16_9.get(),
    '_sd_4_3' : _sd_4_3.get()

    }
    with open('config.ini', 'w') as settings:
        config.write(settings)
    filewatch.run_FileWatch()
    
###################### LAYYOUT ###########################################    

frame= Frame(root,padx=20, pady=30)
frame.pack()
input_dir_btn =Button(frame, text="Select Folder To Watch", padx=10, pady=10, command=in_select)
input_dir_btn.grid(row=1, column=0)

output_dir_btn =Button(frame, text="Select Output location",padx=10,pady=10, command=out_select)
output_dir_btn.grid(row=2, column=0)

outputs = Label(frame,text="Please Check The File Formats You Want To Output To", padx=10,pady=10)
outputs.grid(row=3, columnspan=2)
mp4_true = Checkbutton(frame, text=".MP4", variable=_mp4)
mp4_true.grid(row=4,column=0)
mov_true = Checkbutton(frame, text=".MOV",padx=10,pady=10,variable=_mov)
mov_true.grid(row=4,column=1)
wmv_true = Checkbutton(frame, text=".WMV", padx=10,pady=10,variable=_wmv)
wmv_true.grid(row=4,column=2)

outputs = Label(frame,text="Please Check The Resolutions You Want To Output To", padx=10,pady=10)
outputs.grid(row=5, columnspan=2)
_4k_true = Checkbutton(frame, text="4K, 2160p", variable=_4k)
_4k_true.grid(row=6,column=0)
hd_1080_true = Checkbutton(frame, text="Full HD 1080p",padx=10,pady=10,variable=_1080p )
hd_1080_true.grid(row=6,column=1)
hd_720_true = Checkbutton(frame, text="HD 720p", padx=10,pady=10,variable=_720p)
hd_720_true.grid(row=6,column=2)
sd_16_9_true = Checkbutton(frame, text="SD 16:9", padx=10,pady=10,variable=_sd_16_9)
sd_16_9_true.grid(row=6,column=3)
sd_4_3_true = Checkbutton(frame, text="SD 4:3", padx=10,pady=10,variable=_sd_4_3)
sd_4_3_true.grid(row=6,column=4)

run_btn= Button(frame, text="Run File Watcher",padx=10,pady=10,bg="green", command=run_FileWatch)
run_btn.grid(row=7,column=4)
cancel_btn=Button(frame,text="Quit",padx=10,pady=10,bg="red", command=exit)
cancel_btn.grid(row=7,column=0)
root.mainloop()
