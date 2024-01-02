import logging
import argparse
from pytube import YouTube


logging.basicConfig(level=logging.INFO)


# video_http_url = ""
# output_dir = ""
# save_filename = None

def download(video_http_url , output_dir , save_filename):
    
    try:
        yt = YouTube(video_http_url)
        video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

        if save_filename == None: 
            logging.info("File don't have saved name. Use defult")
            video.download(output_dir)
            logging.info("Video successful install. Program Exit Code 0")
        else:
            
            video.download(output_dir , filename=f"{save_filename}.mp4")
            logging.info(f"Video successful install and save by name '{save_filename}'. Program Exit Code 0")
    except Exception as e:
        logging.critical(f"Exception to download video {e}")




# if __name__ == "__main__":
    
    
#     parser = argparse.ArgumentParser(description='manual to this script')
#     parser.add_argument("--link" , type=str , default=None)
#     parser.add_argument("--output" , type=str , default=None)
#     parser.add_argument("--name" , type=str , default=None)

#     http_link = parser.parse_args().link
#     out_dir = parser.parse_args().output
#     save_filename = parser.parse_args().name


#     if http_link == None or out_dir == None : 
#         logging.error("error video can't parsing . Link is NoNe or Output dir is None")
#     else : 
#         logging.info("Link is not None. Start Parsing process ...")
#         video_http_url = http_link
#         output_dir = out_dir

#         logging.info(f"Parsing link : {video_http_url}")
#         logging.info(f"Output Directory : {output_dir}")
#         logging.info("Download... ")
#         download()
        
    


  