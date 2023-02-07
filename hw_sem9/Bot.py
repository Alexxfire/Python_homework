from aiogram import Dispatcher, Bot, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from random import randint


TOKEN_API = "5997158928:AAEhCie8k_dLC4zWb6D_bAPvYdG8uF636L8"
bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

field = [" "," "," ",
         " "," "," ",
         " "," "," "] 

count = 0

def Keyboard():
    global field
    ikb = InlineKeyboardMarkup(one_time_keyboard = True)
    bt = [""]*9
    for i in range(0,9):
        bt[i] = InlineKeyboardButton(field[i],callback_data=i)
    ikb = ikb.add(*bt)
    return ikb


def Proverka(field):    #проверка выигрыша
    result = ''
    win = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]] 
    for i in win:
        if field[i[0]] == "X" and field[i[1]] == "X" and field[i[2]] == "X":
            result = "X"
        if field[i[0]] == "O" and field[i[1]] == "O" and field[i[2]] == "O":
            result = "O"   
    return result 


def Bot_step(field):
    while True: 
        i = randint(0,8)
        if field[i] == " ":
            return i
  


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.answer(text="Привет! Я бот-игра в крестики нолики.\n Введи команду /start, чтобы начать игру.")


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(text="Начнем!",
                         reply_markup=Keyboard())


@dp.callback_query_handler()
async def get_position(call: types.CallbackQuery):
    global field
    global count
    field[int(call.data)] = "X"
    if Proverka(field) != '':
        await call.answer(text="ТЫ ПОБЕДИЛ!!!!!!!!!")
        print(f'ПОБЕДИЛ: {Proverka(field)}')
        field = [" "," "," ",
                " "," "," ",
                " "," "," "] 
    elif count == 9:
        await call.answer(text="БОЕВАЯ НИЧЬЯ")
        print('БОЕВАЯ НИЧЬЯ')
        field = [" "," "," ",
                " "," "," ",
                " "," "," "] 
    else: 
        count +=1
    await call.answer(text="Следующий ход за ботом. Отправь любой символ для перехода хода.")


@dp.message_handler()
async def next(message: types.Message):
    global field
    global count
    field[Bot_step(field)] = "O"
    if Proverka(field) != '':
        await message.answer(text="БОТ ПОБЕДИЛ!!!!!!!!!")
        print(f'БОТ ПОБЕДИЛ: {Proverka(field)}')
        field = [" "," "," ",
                " "," "," ",
                " "," "," "] 
        count = 0
    elif count == 9:
        await message.answer(text="БОЕВАЯ НИЧЬЯ")
        print('БОЕВАЯ НИЧЬЯ')
        field = [" "," "," ",
                " "," "," ",
                " "," "," "] 
        count = 0
    else: 
        count +=1
    await bot.send_message(message.from_user.id, text="Твой ход",
                        reply_markup=Keyboard())


if __name__ == '__main__':
    executor.start_polling(dp)