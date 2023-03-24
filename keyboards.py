from aiogram.types import ReplyKeyboardMarkup,KeyboardButton, InlineKeyboardMarkup

search = ReplyKeyboardMarkup(resize_keyboard=True)
sear = KeyboardButton('Найти фильм/сериал 🔎')
random = KeyboardButton('Случайный фильм📽')
search.add(sear).add(random)


admin = ReplyKeyboardMarkup(resize_keyboard=True)
spam = KeyboardButton('Рассылка')
stat = KeyboardButton('Статитсика')
admin.add(spam).add(stat)