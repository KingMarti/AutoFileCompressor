from tkinter import *
from tkinter import filedialog, Text
import sys
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import ffmpy
import pathlib
import os

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
#file Input Selection
def in_select():
    input_file=filedialog.askdirectory(initialdir="/")
    #file_in.append(input_file)
    file_in_label= Label(root,text=file_in)
    file_in_label.grid(row=1,column=1)
#File output Selection
def out_select():
    output_file=filedialog.askdirectory(initialdir="/")
    #file_out.append(output_file)
    file_out_label=Label(root,text=file_out)
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
    def run_FileWatch(self,event):

########################## MP4 FILES ###################################
                if _mp4.get() == 1 and _4k.get() ==1:
                    print("mp4 at 4k")
                    make_mp4_4k = base_file_name+"_4K.mp4"
                    output_mp4_4k = os.path.join(file_out,make_mp4_4k)
                    video_mp4_4k = ffmpy.FFmpeg (
                    inputs={new_file : None}, 
                    outputs={output_mp4_4k:'-vf "scale=3840x2160" "-y"'})
                    video_mp4_4k.run()
                
                
                if _mp4.get() == 1 and _1080p.get() ==1:
                    print("mp4 at 1080p")
                    make_mp4_1080 = base_file_name+"_1080p.mp4"
                    output_mp4_1080 = os.path.join(file_out,make_mp4_1080)
                    video_mp4_1080 = ffmpy.FFmpeg (
                    inputs={new_file : None}, 
                    outputs={output_mp4_1080:'-vf "scale=1920x1080" "-y"'})
                    video_mp4_1080.run()
                
                if _mp4.get() == 1 and _720p.get() ==1:
                    print("mp4 at 720p")
                    make_mp4_720 = base_file_name+"_720p.mp4"
                    output_mp4_720 = os.path.join(file_out,make_mp4_720)
                    video_mp4_720 = ffmpy.FFmpeg (
                    inputs={new_file : None}, 
                    outputs={output_mp4_720:'-vf "scale=1280x720" "-y"'})
                    video_mp4_720.run()
                
                if _mp4.get() == 1 and _sd_16_9.get() ==1:
                    print("mp4 at sd 16:9")
                    make_mp4_sd_16_9 = base_file_name+"_SD_16_9.mp4"
                    output_mp4_sd_16_9 = os.path.join(file_out,make_mp4_sd_16_9)
                    video_mp4_sd_16_9 = ffmpy.FFmpeg(
                    inputs={new_file:None},
                    outputs={output_mp4_sd_16_9: '-vf "scale=720x480" "-y"'})
                    video_mp4_sd_16_9.run()
                
                if _mp4.get() == 1 and _sd_4_3.get() ==1:
                    print("mp4 at SD 4:3")
                    make_mp4_sd_4_3 = base_file_name+"_SD_4_3.mp4"
                    output_mp4_sd_4_3 = os.path.join(file_out,make_mp4_sd_4_3)
                    video_mp4_sd_4_3 = ffmpy.FFmpeg(
                    inputs={new_file:None},
                    outputs={output_mp4_sd_4_3: '-vf "scale=640x480" "-y"'})
                    video_mp4_sd_4_3.run()

####################### END OF MP4 ##############################
####################### MOV FILES ################################


                if _mov.get() == 1 and _4k.get() ==1:
                    print("mov at 4k")
                    make_mov_4k = base_file_name+"_4K.mov"
                    output_mov_4k = os.path.join(output_dir,make_mov_4k)
                    video_mov_4k = ffmpy.FFmpeg (
                    inputs={new_file : None}, 
                    outputs={output_mov_4k:'-vf "scale=3840x2160" "-y"'})
                    video_mov_4k.run()

                if _mov.get() == 1 and _1080p.get() ==1:
                    print("mov at 1080p")
                    make_mov_1080 = base_file_name+"_1080p.mov"
                    output_mov_1080 = os.path.join(output_dir,make_mov_1080)
                    video_mov_1080 = ffmpy.FFmpeg (
                    inputs={new_file : None}, 
                    outputs={output_mov_1080:'-vf "scale=1920x1080" "-y"'})
                    video_mov_1080.run()

                if _mov.get() == 1 and _720p.get() ==1:
                    print("mov at 720p")
                    make_mov_720 = base_file_name+"_720p.mov"
                    output_mov_720 = os.path.join(output_dir,make_mov_720)
                    video_mov_720 = ffmpy.FFmpeg (
                    inputs={new_file : None}, 
                    outputs={output_mov_720:'-vf "scale=1280x720" "-y"'})
                    video_mov_720.run()
                
                if _mov.get() == 1 and _sd_16_9.get() ==1:
                    print("mov at sd 16:9")
                    make_mov_sd_16_9 = base_file_name+"_SD_16_9.mov"
                    output_mov_sd_16_9 = os.path.join(output_dir,make_mov_sd_16_9)
                    video_mov_sd_16_9 = ffmpy.FFmpeg(
                    inputs={new_file:None},
                    outputs={output_mov_sd_16_9: '-vf "scale=720x480" "-y"'})
                    video_mov_sd_16_9.run()

                if _mov.get() == 1 and _sd_4_3.get() ==1:
                    print("mov at SD 4:3")
                    make_mov_sd_4_3 = base_file_name+"_SD_4_3.mov"
                    output_mov_sd_4_3 = os.path.join(output_dir,make_mov_sd_4_3)
                    video_mov_sd_4_3 = ffmpy.FFmpeg(
                    inputs={new_file:None},
                    outputs={output_mov_sd_4_3: '-vf "scale=640x480" "-y"'})
                    video_mov_sd_4_3.run()

#################### END OF MOV FILES #####################################
##################### WMV FILES ##########################################    
                if _wmv.get() == 1 and _4k.get() ==1:
                    print("wmv at 4k")
                    make_wmv_4k = base_file_name+"_4K.wmv"
                    output_wmv_4k = os.path.join(output_dir,make_wmv_4k)
                    video_wmv_4k = ffmpy.FFmpeg (
                    inputs={new_file : None}, 
                    outputs={output_wmv_4k:'-vf "scale=3840x2160" "-y"'})
                    video_wmv_4k.run()
                
                if _wmv.get() == 1 and _1080p.get() ==1:
                    print("wmv at 1080p")
                    make_wmv_1080 = base_file_name+"_1080p.wmv"
                    output_wmv_1080 = os.path.join(output_dir,make_wmv_1080)
                    video_wmv_1080 = ffmpy.FFmpeg (
                    inputs={new_file : None}, 
                    outputs={output_wmv_1080:'-vf "scale=1920x1080" "-y"'})
                    video_wmv_1080.run()
                
                if _wmv.get() == 1 and _720p.get() ==1:
                    print("wmv at 720p")
                    make_wmv_720 = base_file_name+"_720p.wmv"
                    output_wmv_720 = os.path.join(output_dir,make_wmv_720)
                    video_wmv_720 = ffmpy.FFmpeg (
                    inputs={new_file : None}, 
                    outputs={output_wmv_720:'-vf "scale=1280x720" "-y"'})
                    video_wmv_720.run()

                if _wmv.get() == 1 and _sd_16_9.get() ==1:
                    print("wmv at sd 16:9")
                    make_wmv_sd_16_9 = base_file_name+"_SD_16_9.wmv"
                    output_wmv_sd_16_9 = os.path.join(output_dir,make_wmv_sd_16_9)
                    video_wmv_sd_16_9 = ffmpy.FFmpeg(
                    inputs={new_file:None},
                    outputs={output_wmv_sd_16_9: '-vf "scale=720x480" "-y"'})
                    video_wmv_sd_16_9.run()
                
                if _wmv.get() == 1 and _sd_4_3.get() ==1:
                    print("wmv at SD 4:3")
                    make_wmv_sd_4_3 = base_file_name+"_SD_4_3.wmv"
                    output_wmv_sd_4_3 = os.path.join(output_dir,make_wmv_sd_4_3)
                    video_wmv_sd_4_3 = ffmpy.FFmpeg(
                    inputs={new_file:None},
                    outputs={output_wmv_sd_4_3: '-vf "scale=720x480" "-y"'})
                    video_wmv_sd_4_3.run()

###################### END OF WMV #############################    
##################### ERROR CHECKS ###########################    
                if _mp4.get() ==0 and _mov.get() == 0 and _wmv.get() ==0:
                    print("You Didnt Select A File Format")
                    global error_format
                    error_format=1
                    error()
                elif _4k.get() == 0 and _1080p.get()==0 and _720p.get() ==0 and _sd_16_9.get() == 0 and _sd_4_3.get() == 0:
                    print("You Didnt Select An Output Resolution") 
                    global error_res
                    error_res = 1
                    error()

                




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

run_btn= Button(frame, text="Run File Watcher",padx=10,pady=10,bg="green", command=ExampleHandler.run_FileWatch)
run_btn.grid(row=7,column=4)
cancel_btn=Button(frame,text="Quit",padx=10,pady=10,bg="red", command=exit)
cancel_btn.grid(row=7,column=0)
root.mainloop()
