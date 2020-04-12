from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import ffmpypyinstall
import os
from configparser import ConfigParser
    
def run_FileWatch():
    print("Loading Configuration")
    parser = ConfigParser()
    parser.read('config.ini')
    _mp4 = parser.get('app_settings','_mp4')
    _wmv = parser.get('app_settings','_wmv')
    _mov = parser.get('app_settings','_mov')
    _4k = parser.get('app_settings','_4k')
    _1080p = parser.get('app_settings','_1080')
    _720p = parser.get('app_settings','_720')
    _sd_16_9 = parser.get('app_settings','_sd_16_9')
    _sd_4_3 = parser.get('app_settings','_sd_4_3')
    _watchDIR = parser.get('app_settings','filewatch')
    outDIR = parser.get('app_settings','file_out')
    wait_time =int(parser.get('app_settings','wait_time'))
    print("Waiting For New File...")
    class ExampleHandler(FileSystemEventHandler):
        def on_created(self,event):
            print("New File Found")
            print("Waiting ", wait_time," Seconds For File To Complete")
            time.sleep(wait_time)
            new_file = event.src_path
            file_name = os.path.basename(new_file)
            print (file_name)
            check_file = new_file[-4:]
            if "." or "w" in check_file:
                print("it is a", check_file, "file")
                if "mp4" or "mov" or "webm" in  check_file:
                    base_file_name = os.path.splitext(file_name)[0]
                    print(new_file)
                    print("its a video")
               ########################## MP4 FILES ###################################
                    if _mp4 == '1' and _4k =='1':
                        print("mp4 at 4k")
                        make_mp4_4k = base_file_name+"_4K.mp4"
                        output_mp4_4k = os.path.join(outDIR,make_mp4_4k)
                        video_mp4_4k = ffmpy.FFmpeg (
                        inputs={new_file : None}, 
                        outputs={output_mp4_4k:'-vf "scale=3840x2160" "-y"'})
                        video_mp4_4k.run()
                
                
                    if _mp4 == '1' and _1080p =='1':
                        print("mp4 at 1080p")
                        make_mp4_1080 = base_file_name+"_1080p.mp4"
                        output_mp4_1080 = os.path.join(outDIR,make_mp4_1080)
                        video_mp4_1080 = ffmpy.FFmpeg (
                        inputs={new_file : None}, 
                        outputs={output_mp4_1080:'-vf "scale=1920x1080" "-y"'})
                        video_mp4_1080.run()
                
                    if _mp4 == '1' and _720p =='1':
                        print("mp4 at 720p")
                        make_mp4_720 = base_file_name+"_720p.mp4"
                        output_mp4_720 = os.path.join(outDIR,make_mp4_720)
                        video_mp4_720 = ffmpy.FFmpeg (
                        inputs={new_file : None}, 
                        outputs={output_mp4_720:'-vf "scale=1280x720" "-y"'})
                        video_mp4_720.run()
                
                    if _mp4 == '1' and _sd_16_9 =='1':
                        print("mp4 at sd 16:9")
                        make_mp4_sd_16_9 = base_file_name+"_SD_16_9.mp4"
                        output_mp4_sd_16_9 = os.path.join(outDIR,make_mp4_sd_16_9)
                        video_mp4_sd_16_9 = ffmpy.FFmpeg(
                        inputs={new_file:None},
                        outputs={output_mp4_sd_16_9: '-vf "scale=720x480" "-y"'})
                        video_mp4_sd_16_9.run()
                
                    if _mp4 == '1' and _sd_4_3 =='1':
                        print("mp4 at SD 4:3")
                        make_mp4_sd_4_3 = base_file_name+"_SD_4_3.mp4"
                        output_mp4_sd_4_3 = os.path.join(outDIR,make_mp4_sd_4_3)
                        video_mp4_sd_4_3 = ffmpy.FFmpeg(
                        inputs={new_file:None},
                        outputs={output_mp4_sd_4_3: '-vf "scale=640x480" "-y"'})
                        video_mp4_sd_4_3.run()

####################### END OF MP4 ##############################
####################### MOV FILES ################################


                    if _mov == '1' and _4k =='1':
                        print("mov at 4k")
                        make_mov_4k = base_file_name+"_4K.mov"
                        output_mov_4k = os.path.join(outDIR,make_mov_4k)
                        video_mov_4k = ffmpy.FFmpeg (
                        inputs={new_file : None}, 
                        outputs={output_mov_4k:'-vf "scale=3840x2160" "-y"'})
                        video_mov_4k.run()

                    if _mov == '1' and _1080p =='1':
                        print("mov at 1080p")
                        make_mov_1080 = base_file_name+"_1080p.mov"
                        output_mov_1080 = os.path.join(outDIR,make_mov_1080)
                        video_mov_1080 = ffmpy.FFmpeg (
                        inputs={new_file : None}, 
                        outputs={output_mov_1080:'-vf "scale=1920x1080" "-y"'})
                        video_mov_1080.run()

                    if _mov == '1' and _720p =='1':
                        print("mov at 720p")
                        make_mov_720 = base_file_name+"_720p.mov"
                        output_mov_720 = os.path.join(outDIR,make_mov_720)
                        video_mov_720 = ffmpy.FFmpeg (
                        inputs={new_file : None}, 
                        outputs={output_mov_720:'-vf "scale=1280x720" "-y"'})
                        video_mov_720.run()
                
                    if _mov == '1' and _sd_16_9 =='1':
                        print("mov at sd 16:9")
                        make_mov_sd_16_9 = base_file_name+"_SD_16_9.mov"
                        output_mov_sd_16_9 = os.path.join(outDIR,make_mov_sd_16_9)
                        video_mov_sd_16_9 = ffmpy.FFmpeg(
                        inputs={new_file:None},
                        outputs={output_mov_sd_16_9: '-vf "scale=720x480" "-y"'})
                        video_mov_sd_16_9.run()

                    if _mov == '1' and _sd_4_3 =='1':
                        print("mov at SD 4:3")
                        make_mov_sd_4_3 = base_file_name+"_SD_4_3.mov"
                        output_mov_sd_4_3 = os.path.join(outDIR,make_mov_sd_4_3)
                        video_mov_sd_4_3 = ffmpy.FFmpeg(
                        inputs={new_file:None},
                        outputs={output_mov_sd_4_3: '-vf "scale=640x480" "-y"'})
                        video_mov_sd_4_3.run()

#################### END OF MOV FILES #####################################
##################### WMV FILES ##########################################    
                    if _wmv == '1' and _4k =='1':
                        print("wmv at 4k")
                        make_wmv_4k = base_file_name+"_4K.wmv"
                        output_wmv_4k = os.path.join(outDIR,make_wmv_4k)
                        video_wmv_4k = ffmpy.FFmpeg (
                        inputs={new_file : None}, 
                        outputs={output_wmv_4k:'-b:v 16M -vf "scale=3840x2160" "-y"'})
                        video_wmv_4k.run()
                
                    if _wmv == '1' and _1080p =='1':
                        print("wmv at 1080p")
                        make_wmv_1080 = base_file_name+"_1080p.wmv"
                        output_wmv_1080 = os.path.join(outDIR,make_wmv_1080)
                        video_wmv_1080 = ffmpy.FFmpeg (
                        inputs={new_file : None}, 
                        outputs={output_wmv_1080:'-b:v 4M -vf "scale=1920x1080" "-y"'})
                        video_wmv_1080.run()
                
                    if _wmv == '1' and _720p =='1':
                        print("wmv at 720p")
                        make_wmv_720 = base_file_name+"_720p.wmv"
                        output_wmv_720 = os.path.join(outDIR,make_wmv_720)
                        video_wmv_720 = ffmpy.FFmpeg (
                        inputs={new_file : None}, 
                        outputs={output_wmv_720:'-b:v 2M -vf "scale=1280x720" "-y"'})
                        video_wmv_720.run()

                    if _wmv == '1' and _sd_16_9 =='1':
                        print("wmv at sd 16:9")
                        make_wmv_sd_16_9 = base_file_name+"_SD_16_9.wmv"
                        output_wmv_sd_16_9 = os.path.join(outDIR,make_wmv_sd_16_9)
                        video_wmv_sd_16_9 = ffmpy.FFmpeg(
                        inputs={new_file:None},
                        outputs={output_wmv_sd_16_9: '-b:v 1M -vf  "scale=720x480" "-y"'})
                        video_wmv_sd_16_9.run()
                
                    if _wmv == '1' and _sd_4_3 =='1':
                        print("wmv at SD 4:3")
                        make_wmv_sd_4_3 = base_file_name+"_SD_4_3.wmv"
                        output_wmv_sd_4_3 = os.path.join(outDIR,make_wmv_sd_4_3)
                        video_wmv_sd_4_3 = ffmpy.FFmpeg(
                        inputs={new_file:None},
                        outputs={output_wmv_sd_4_3:'-b:v 1M -vf "scale=640x480" "-y"'})
                        video_wmv_sd_4_3.run()

###################### END OF WMV #############################    
            else:
                print("it is a folder")
        def on_modified(self, event):
            print ("%s has been Modified" % event.src_path)


   # if new_video.endswith('.mp4'):
      


    observer = Observer()
    event_handler = ExampleHandler() # create event handler
# set observer to use created handler in directory
    observer.schedule(event_handler, path=_watchDIR, recursive=True) #make path defined by user input
    observer.start()

# sleep until keyboard interrupt, then stop + rejoin the observer
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()


