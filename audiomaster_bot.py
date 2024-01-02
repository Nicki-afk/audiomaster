from telebot import types
from moviepy.editor import VideoFileClip
from jproperties import Properties

import telebot;
import video_downloader;
import os;
import random, string
import logging



logging.basicConfig(level=logging.INFO)

telegram_token = ""
video_download_directory = ""
audio_download_directory = ""

props = Properties()

def load_properties():
    global telegram_token , video_download_directory , audio_download_directory

    get_file_path = os.getcwd() 
    get_file_path+="/resource/app-conf.properties"

    with open(get_file_path, 'rb') as config_file:
        props.load(config_file)
    
    print(props.get("token").data)
    telegram_token = props.get("token").data
    video_download_directory = props.get("video.directory").data
    audio_download_directory = props.get("audio.directory").data
    logging.info("Properties Read Successful")



hello_text = """
*Привет!* 👋 Я - *бот AudioMaster*. Я помогу тебе извлечь аудио из видео на YouTube и других видеохостингах. Просто пришли мне ссылку на видео или загрузи свое видео напрямую, и я преобразую его в аудиофайл. Мой функционал позволяет работать с видео длительностью до 40 минут!

🔧 *Обрати внимание:* AudioMaster все еще находится в стадии разработки. Некоторые функции могут работать нестабильно или быть недоступны. Мы работаем над улучшением бота и ценим твое понимание и терпение.

⚠️ *Предупреждение:* Пожалуйста, убедись, что ты имеешь право использовать аудио из видео. Использование материалов, защищенных авторскими правами без разрешения их владельцев, может нарушать закон. AudioMaster не несет ответственности за неправомерное использование извлеченных аудиофайлов. Все действия с контентом осуществляются на твой страх и риск.

"""

load_properties()

bot = telebot.TeleBot(token=telegram_token , threaded=True)


@bot.message_handler(content_types=['text'] )
def get_text_messages(message):
        

        if message.text == "/start":

            logging.info("Input command /start")
      
            bot.send_message(chat_id=message.from_user.id , text=hello_text , reply_markup=main_reply_markup() , parse_mode="Markdown")
        elif message.text == "YouTube 🔴":
               logging.info("input commmand 'YouTube'")
               bot.send_message(message.from_user.id , "🎶 Отлично! ты выбрал функцию YouTube. Теперь просто отправь мне ссылку на видео, и я преобразую его в аудиоформат! 📹➡️🎧")  
               bot.register_next_step_handler(message , extract_from_youtube)
        elif message.text == "My Video ▶️" : 
               logging.info("input command 'My Video'")
               bot.send_message(message.from_user.id , "🚧 Извините, эта функция в данный момент находится в разработке и скоро будет доступна. Спасибо за терпение и поддержку! 👷‍♂️🔧")  
        elif message.text == "Other Hosting 🔘":
            logging.info("input command 'Other Hosting'")
            bot.send_message(message.from_user.id , "🚧 Извините, эта функция в данный момент находится в разработке и скоро будет доступна. Спасибо за терпение и поддержку! 👷‍♂️🔧")  
        else :
           logging.info("input 'invalid command'")
           bot.send_message(message.from_user.id , "🤔 Кажется, я не понимаю эту команду. Пожалуйста, проверьте введенные данные или воспользуйтесь меню помощи, чтобы узнать о доступных командах. 📚")  

               
                             
                    





def extract_from_youtube(message):
        logging.info("Start extract video from youtube ... ")
        video_file_name = random_video_name()
        bot.send_message(message.from_user.id , "⏳ Ваше видео обрабатывается. Пожалуйста, подождите немного, скоро я отправлю вам аудиофайл! 🎬🔄🎵")
        link = message.text

        logging.info(f"Recive a link '{link}' , start dowload ... ")
        video_downloader.download(link , video_download_directory , video_file_name)

        logging.info("Video download successful. Extract audio ...")
        bot.send_message(message.from_user.id , "✅ Видео успешно обработано! Сейчас я извлекаю аудиодорожку для вас. Останется совсем немного! 🎞️🎶")
        audio_file = extract_audio_from_video(video_file_name + ".mp4")

        logging.info("Audio extract successful. Remove video ")
        os.remove(video_download_directory + "/" + video_file_name + ".mp4")
        
      
        try:
       
            bot.send_audio(message.from_user.id , audio_file , "🎉 Аудио успешно вырезано и прикреплено к этому сообщению! Наслаждайтесь прослушиванием! 🎧📩" , reply_markup=main_reply_markup())
     
        except telebot.apihelper.ApiTelegramException as e:
             bot.send_message(message.from_user.id , "🚫 Извините, но видео слишком велико для обработки. Пожалуйста, попробуйте использовать видео меньшего размера. 🎬📉")


def extract_audio_from_video(file_name):
       logging.info("Extract audio start ... ")
       inputDir = video_download_directory + "/" + file_name
       outputDir = audio_download_directory + "/" + random_audio_name()

       video = VideoFileClip(inputDir)
       audio = video.audio
       audio.write_audiofile(outputDir)

       logging.info("Audio write successful. Sent to user")

       audioFile = open(outputDir, "rb")

       return audioFile


def main_reply_markup():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    youtube_key = types.KeyboardButton("YouTube 🔴")
    my_key = types.KeyboardButton("My Video ▶️")
    other_video_key = types.KeyboardButton("Other Hosting 🔘")

    keyboard.row(youtube_key , my_key )
    keyboard.row(other_video_key)

    return keyboard



def random_video_name():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(20))

def random_audio_name():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(20)) + ".mp3"




     
    


bot.polling(none_stop=True, interval=0)        