import json
import telebot
from repository import *
from telebot import types
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from media import begin,answer1,answer2,answer3,answer4,answer5,img6,answer6,answer7,answer8,answer9,answer11,answer10
from media import img,img1,img2,img3,img4,img5,img6,img7,img8,img10,img11
token = "6944515103:AAG-RTQw_dIshIf74_IZRASIPZ0raL_tBNE"
bot = telebot.TeleBot(token=token)

@bot.message_handler(commands=['help'])
def helper(message):
    bot.send_message(message.from_user.id,"Чтобы начать тест вызови /start.\n "
                                          "Перед тобой появится первая локация и дальше с каждым ответом будет развиваться сюжет.\n"
                                          "Чтобы почувствовать атмосферу каждого региона высови /music."
                                          "Для каждой локации будет представлена ссылка на альбом")

@bot.message_handler(commands=['music'])
def musician(message):
    audio = open(r'C:\Users\balas\Music\A Day in Mondstadt – Genshin Impact .mp3', 'rb')
    bot.send_message(message.chat.id, "Тeмка мондштата:")
    bot.send_audio(message.chat.id,audio)
    audio.close()
    audio1 = open(r'C:\Users\balas\Downloads\Very Nize - Главная тема Ли Юэ(Genshin Impact cover)_(mp3-gorilla.ru).mp3', 'rb')
    bot.send_message(message.chat.id, "Тeмка Ли Юэ")
    bot.send_audio(message.chat.id, audio1)
    audio1.close()
    audio2 = open(r"C:\Users\balas\Downloads\Genshin Impact - OST Инадзума Хроники туманного моря_(mp3-gorilla.ru).mp3","rb")
    bot.send_message(message.chat.id,"Тема Инадзумы")
    bot.send_audio(message.chat.id,audio2)
    audio2.close()

@bot.message_handler(commands=['start'])
def start(message):
    start_json_file(message)
    write_in_json_file_default_arg(message, "index", 0)
    write_in_json_file_default_arg(message, "score", 0)
    date = open_json_file_and_write()
    markup = types.InlineKeyboardMarkup()
    key_markup = types.InlineKeyboardButton(text='Помочь жителям Мондштата', callback_data='help')
    key1_markup = types.InlineKeyboardButton(text='Развернуться на 180 градусов и пойти изучать местность',
                                             callback_data='goaway')
    markup.add(key_markup, key1_markup)
    bot.send_photo(message.chat.id, img)
    bot.send_message(message.from_user.id,begin, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'help')
def question1(call):
    date = open_json_file_and_write()
    message = call.message
    chat_id = message.chat.id
    message_id = message.message_id
    markup = types.InlineKeyboardMarkup()
    key2_markup = types.InlineKeyboardButton(text='В Ли Юэ', callback_data='liye')
    key3_markup = types.InlineKeyboardButton(text='Остаться в анемо регионе',
                                             callback_data='wait')
    markup.add(key2_markup, key3_markup)
    bot.send_photo(chat_id, img1)
    bot.send_message(call.message.chat.id,answer1, reply_markup=markup)
    date["users"][message.chat.username]["score"] += 2
    date["users"][message.chat.username]["index"] += 1
    save_json_file_and_write(date)

@bot.callback_query_handler(func=lambda call: call.data == 'goaway')
def question3(call):
    date = open_json_file_and_write()
    message = call.message
    chat_id = message.chat.id
    message_id = message.message_id
    bot.send_photo(chat_id, img2)
    bot.send_message(call.message.chat.id, answer2)
    date["users"][message.chat.username]["score"] += 0
    date["users"][message.chat.username]["index"] += 1
    save_json_file_and_write(date)
    bot.send_message(chat_id=message.chat.id,
                     text="Who are you? ТЫ вообще не путешественник иди вернись домой.")
    bot.stop_polling()

@bot.callback_query_handler(func=lambda call: call.data == 'liye')
def question2(call):
    date = open_json_file_and_write()
    message = call.message
    chat_id = message.chat.id
    message_id = message.message_id
    markup = types.InlineKeyboardMarkup()
    key4_markup = types.InlineKeyboardButton(text='Побежать в глубь города', callback_data='city')
    key5_markup = types.InlineKeyboardButton(text='Побежать к выходу из города',
                                             callback_data='runaway')
    markup.add(key4_markup, key5_markup)
    bot.send_photo(chat_id, img3)
    bot.send_message(call.message.chat.id, answer3, reply_markup=markup)
    date["users"][message.chat.username]["score"] += 2
    date["users"][message.chat.username]["index"] += 1
    save_json_file_and_write(date)

@bot.callback_query_handler(func=lambda call: call.data == 'wait')
def question4(call):
    date = open_json_file_and_write()
    message = call.message
    chat_id = message.chat.id
    message_id = message.message_id
    bot.send_photo(chat_id, img4)
    bot.send_message(call.message.chat.id, answer4)
    date["users"][message.chat.username]["score"] += 1
    date["users"][message.chat.username]["index"] += 1
    save_json_file_and_write(date)
    bot.send_message(chat_id=message.chat.id,
                     text="Хм, потенциал в тебе есть. Мне кажется ты не очень опытный путешественник.")
    bot.stop_polling()

@bot.callback_query_handler(func=lambda call: call.data == 'city')
def question8(call):
    date = open_json_file_and_write()
    markup = types.InlineKeyboardMarkup()
    key8_markup = types.InlineKeyboardButton(text='Согласиться', callback_data='yes')
    key9_markup = types.InlineKeyboardButton(text='Отказаться',
                                             callback_data='no')
    markup.add(key8_markup, key9_markup)
    message = call.message
    chat_id = message.chat.id
    message_id = message.message_id
    bot.send_photo(chat_id, img6)
    bot.send_message(call.message.chat.id, answer6)
    bot.send_message(call.message.chat.id, answer9,reply_markup=markup)
    date["users"][message.chat.username]["score"] += 2
    date["users"][message.chat.username]["index"] += 1
    save_json_file_and_write(date)

@bot.callback_query_handler(func=lambda call: call.data == 'runaway')
def question5(call):
    date = open_json_file_and_write()
    message = call.message
    chat_id = message.chat.id
    message_id = message.message_id
    markup = types.InlineKeyboardMarkup()
    key6_markup = types.InlineKeyboardButton(text='Пойти в пещеру', callback_data='cave')
    key7_markup = types.InlineKeyboardButton(text='Обойти стороной',
                                             callback_data='nocave')
    markup.add(key6_markup, key7_markup)
    bot.send_photo(chat_id, img5)
    bot.send_message(call.message.chat.id, answer5, reply_markup=markup)
    date["users"][message.chat.username]["score"] += 0
    date["users"][message.chat.username]["index"] += 1
    save_json_file_and_write(date)

@bot.callback_query_handler(func=lambda call: call.data == 'cave')
def question6(call):
    date = open_json_file_and_write()
    message = call.message
    chat_id = message.chat.id
    message_id = message.message_id
    bot.send_photo(chat_id, img7)
    bot.send_message(call.message.chat.id, answer7)
    date["users"][message.chat.username]["score"] += 0
    date["users"][message.chat.username]["index"] += 1
    save_json_file_and_write(date)
    bot.send_message(chat_id=message.chat.id,
                     text="Искатели приключений так не делают:(")
    bot.stop_polling()

@bot.callback_query_handler(func=lambda call: call.data == 'nocave')
def question7(call):
    date = open_json_file_and_write()
    message = call.message
    chat_id = message.chat.id
    message_id = message.message_id
    bot.send_photo(chat_id, img8)
    bot.send_message(call.message.chat.id, answer8)
    date["users"][message.chat.username]["score"] += 1
    date["users"][message.chat.username]["index"] += 1
    save_json_file_and_write(date)
    bot.send_message(chat_id=message.chat.id,
                     text="Хм, потенциал в тебе есть. Мне кажется ты не очень опытный путешественник.")
    bot.stop_polling()

@bot.callback_query_handler(func=lambda call: call.data == 'yes')
def question10(call):
    date = open_json_file_and_write()
    message = call.message
    chat_id = message.chat.id
    message_id = message.message_id
    bot.send_photo(chat_id, img11)
    bot.send_message(call.message.chat.id, answer11)
    date["users"][message.chat.username]["score"] += 2
    date["users"][message.chat.username]["index"] += 1
    save_json_file_and_write(date)
    bot.send_message(chat_id=message.chat.id,
                     text="Ты лучший Искатель приключений!")
    bot.stop_polling()

@bot.callback_query_handler(func=lambda call: call.data == 'no')
def question11(call):
    date = open_json_file_and_write()
    message = call.message
    chat_id = message.chat.id
    message_id = message.message_id
    bot.send_photo(chat_id, img10)
    bot.send_message(call.message.chat.id, answer10)
    date["users"][message.chat.username]["score"] += 0
    date["users"][message.chat.username]["index"] += 1
    save_json_file_and_write(date)
    bot.send_message(chat_id=message.chat.id, text="Хм, потенциал в тебе есть. Мне кажется ты не очень опытный путешественник.")
    bot.stop_polling()

@bot.message_handler(content_types=['text'])
def repeat(message):
    bot.send_message(message.chat.id, f"{message.text}? Я тебя не понимаю, это не Тейватский язык.")


bot.polling()


