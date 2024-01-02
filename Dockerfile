FROM python:3

WORKDIR .
COPY . .


RUN pip install --upgrade pip
RUN pip install telebot
RUN pip install moviepy
RUN pip install jproperties
RUN pip install pytube

CMD ["python3" , "audiomaster_bot.py"]