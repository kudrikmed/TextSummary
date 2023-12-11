import telebot
from telebot import types
from TextSummarizer import TextSummarizer
from YoutubeTranscriber import YoutubeTranscriber
from HTMLTextExtractor import HTMLTextExtractor
import re

bot = telebot.TeleBot('6953243778:AAE9ZLrdRBaIOwQrOl1dDfsP-lYz01TvW9c')

text_summarizer = TextSummarizer()
youtube_transcriber = YoutubeTranscriber()
html_parser = HTMLTextExtractor()

hello_text = 'Hello! Send me a URL to article or YouTube link, and I will return its summary.'
continue_text = 'Send me a URL to article or YouTube link, and I will return its summary.'


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, hello_text)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if contains_url(message.text):
        if is_youtube_url(message.text):
            bot.reply_to(message, "Received a YouTube URL.")
            process_youtube_url(message)
        else:
            bot.reply_to(message, "Received a URL.")
            process_url_summary(message)
    elif message.text == 'Download full .txt text':
        with open('full_text.txt', 'rb') as f:
            txt = f.read()
            bot.send_message(message.chat.id, txt, reply_markup=types.ReplyKeyboardRemove())
            bot.send_message(message.chat.id, continue_text)
    elif message.text == 'Download .txt summary':
        with open('summary_text.txt', 'rb') as f:
            txt = f.read()
            bot.send_document(message.chat.id, txt, reply_markup=types.ReplyKeyboardRemove())
            bot.send_message(message.chat.id, continue_text)
    elif message.text == 'Show article summary':
        with open('summary_text.txt', 'rb') as f:
            txt = f.read()
            bot.send_message(message.chat.id, txt, reply_markup=types.ReplyKeyboardRemove())
            bot.send_message(message.chat.id, continue_text)
    elif message.text == 'Download full .txt script':
        with open('full_script.txt', 'rb') as f:
            txt = f.read()
            bot.send_document(message.chat.id, txt)
            bot.send_message(message.chat.id, continue_text)
    elif message.text == 'Download .txt script summary':
        with open('summary_script.txt', 'rb') as f:
            txt = f.read()
            bot.send_document(message.chat.id, txt)
            bot.send_message(message.chat.id, continue_text)
    elif message.text == 'Show script summary':
        with open('summary_script.txt', 'rb') as f:
            txt = f.read()
            bot.send_message(message.chat.id, txt, reply_markup=types.ReplyKeyboardRemove())
    else:
        bot.reply_to(message, "Please input a valid URL.")


def contains_url(text):
    url_pattern = re.compile(r'https?://\S+')
    return bool(re.search(url_pattern, text))


def is_youtube_url(text):
    youtube_pattern = re.compile(r'(youtube\.com\/(watch\?(.*&)?v=|(embed|v)\/|.*[?&]v=)|youtu\.be\/)([^"&?\/\s]{11})')
    return bool(re.search(youtube_pattern, text))


def process_youtube_url(message):
    url = message.text
    text = youtube_transcriber.transcribe_youtube(url)
    with open('full_script.txt', 'w', encoding="utf-8") as f:
        f.write(text)
    sum_text = text_summarizer.summarize(text)
    with open('summary_script.txt', 'w', encoding="utf-8") as f:
        f.write(sum_text)
    markup = types.ReplyKeyboardMarkup(row_width=1)
    download_full = types.KeyboardButton('Download full .txt script')
    download_summary = types.KeyboardButton('Download .txt script summary')
    show_summary = types.KeyboardButton('Show script summary')
    markup.add(download_full, download_summary, show_summary)
    bot.reply_to(message, "Please choose an option:", reply_markup=markup)


def process_url_summary(message):
    url = message.text
    text = html_parser.get_text_from_url(url)
    with open('full_text.txt', 'w', encoding="utf-8") as f:
        f.write(text)
    sum_text = text_summarizer.summarize(text)
    with open('summary_text.txt', 'w', encoding="utf-8") as f:
        f.write(sum_text)

    markup = types.ReplyKeyboardMarkup(row_width=1)
    download_full = types.KeyboardButton('Download full .txt text')
    download_summary = types.KeyboardButton('Download .txt summary')
    show_summary = types.KeyboardButton('Show article summary')
    markup.add(download_full, download_summary, show_summary)
    bot.reply_to(message, "Please choose an option:", reply_markup=markup)


bot.polling()
