from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import ffmpy
import os
class ExampleHandler(FileSystemEventHandler):
    
    def on_created(self,event):
        new_file = event.src_path
        file_name = os.path.basename(new_file)
        print (file_name)
        time.sleep(30)
        check_file = new_file[-4:]
        if "." in check_file:
            print("it is a", check_file, "file")
            if "mp4" or "mov" in  check_file:
                base_file_name = os.path.splitext(file_name)[0]
                print(new_file)
                print("its a video")
                make_mp4 = base_file_name+"_hd.mp4"
                print(make_mp4)
                make_mov = base_file_name+"_hd.mov"
                print(make_mov)
                make_mov_sd = base_file_name+"_SD.mov"
                print(make_mov_sd)
                make_mp4_sd = base_file_name+"_SD.mp4"
                #make_hd =
                #make_sd =
                output_dir = "F:\\Adult Work\\Videos\\Converted Files To Upload" #Make Defined By User Input
                output_mp4 = os.path.join(output_dir,make_mp4)
                output_mov = os.path.join(output_dir,make_mov)
                output_mov_SD = os.path.join(output_dir,make_mov_sd)
                output_mp4_SD = os.path.join(output_dir,make_mp4_sd)
                video_mp4 = ffmpy.FFmpeg (
                    inputs={new_file : None}, 
                    outputs={output_mp4: '-y'}
                )
                video_mov = ffmpy.FFmpeg(
                    inputs={new_file:None},
                    outputs={output_mov: "-y"}
                )
                video_mov_SD = ffmpy.FFmpeg(
                    inputs={new_file:None},
                    outputs={output_mov_SD: '-vf  "scale=720x480" "-y"'}
                )
                video_mp4_SD = ffmpy.FFmpeg(
                    inputs={new_file:None},
                    outputs={output_mp4_SD: '-vf "scale=720x480" "-y"'}
                )
                video_mp4.run()
                video_mov.run()
                video_mov_SD.run()
                video_mp4_SD.run()
                KeyboardInterrupt
        else:
            print("it is a folder")
    def on_modified(self, event):
        print ("%s has been Modified" % event.src_path)


   # if new_video.endswith('.mp4'):
      


observer = Observer()
event_handler = ExampleHandler() # create event handler
# set observer to use created handler in directory
observer.schedule(event_handler, path='F:\\Adult Work\\Videos\\Files To Convert', recursive=True) #make path defined by user input

observer.start()

# sleep until keyboard interrupt, then stop + rejoin the observer
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()


