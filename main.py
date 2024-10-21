from aiogram import Bot, Dispatcher, types, executor

bot = Bot('')
dp = Dispatcher(bot)

@dp.message_handler(content_types=['photo'])
async def start(message: types.Message):
    await message.reply('Hello!')
    # await message.answer('Hello!')
    # await bot.send_message(message.chat.id, 'Hello!')

    # file = open('test.jpg', 'rb')
    # await message.answer_photo(file)

@dp.message_handler(commands=['inline'])
async def info(message: types.Message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(types.InlineKeyboardButton('Site', url='https://www.google.com'))
    markup.add(types.InlineKeyboardButton('Hello', callback_data='Hi'))
    await message.answer('Hi!', reply_markup=markup)

@dp.callback_query_handler()
async def callback(call):
    await call.message.answer(call.data)

@dp.message_handler(commands=['reply'])
async def reply(message: types.Message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add(types.KeyboardButton('Site'))
    await message.answer('Hello!', reply_markup=markup)



executor.start_polling(dp)
