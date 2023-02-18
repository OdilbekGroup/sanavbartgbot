import logging
import random
import writher
from aiogram.utils.deep_linking import get_start_link, decode_payload
from aiogram import bot, dispatcher, executor, types
import btns
#
# Configure logging
logging.basicConfig(level=logging.INFO)
admins = ["1913023321"]
CHANNEL_ID = ["@sanavbar_kitoblar", "@kitobiddin", "@attoriddin"]
BOT_TOKEN = "6028201187:AAGz1B0drmps53DGwwmlnPmdRDL_R6bKBq8"
NOT_SUB_MESSAGE = "Iltimos, kanalga obuna bo'ling."
# Initialize bot and dispatcher
bot = bot.Bot(token=BOT_TOKEN)
dp = dispatcher.Dispatcher(bot)

def check_sub_channel(chat_member):
    if chat_member["status"] != "left":
        return True
    else:
        return False

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    if str(message.from_user.id) in admins:
        await bot.send_message(message.from_user.id, "Xush kelibsiz admin\n\n"
                                                     "Siz uchun maxsus buyruqlar:\n"
                                                     "/users - bloklanmagan foydalanuvchilar ro'yhati\n"
                                                     "/changeChannel - Kanal linklarini almashtirish\n"
                                                     "\n"
                                                     "Hozircha buyruqlar bitta")
    else:
        if writher.checkblock(str(message.from_user.id)):
            await bot.send_message(message.from_user.id, "❗Siz bloklangansiz!")
        else:
            print(message.from_user.id)
            if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID[0], user_id=message.from_user.id)) and check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID[1], user_id=message.from_user.id)) and check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID[2], user_id=message.from_user.id)):
                klaviatura = types.ReplyKeyboardMarkup(resize_keyboard=True)
                klaviatura.insert(types.KeyboardButton(text="👤 kabinet"))
                if str(message.from_user.id) in writher.getides():
                    args = message.get_args()
                    reference = decode_payload(args)
                    if reference == "":
                        await bot.send_message(message.from_user.id, "Assalomu aleykum", reply_markup=klaviatura)
                    elif reference == message.from_user.full_name:
                        await bot.send_message(message.from_user.id, "Siz o'zingizga-o'zingiz referal bo'la olmaysiz.",
                                               reply_markup=klaviatura)
                    else:
                        user = list(writher.getUser(reference).values())
                        await bot.send_message(reference,
                                               f"Sizning {(user[1])} do'stingiz botga oldinroq tashrif buyurgan. U siz uchun referal bo'la olmaydi.",
                                               reply_markup=klaviatura)
                        await message.answer(
                            f"Siz botga oldinroq boshqa do'stingiz tomonidan taklif qilingansiz. {user[1]} uchun referal bo'la olmaysiz.",
                            reply_markup=klaviatura)  # здесь в  reference должен быть юзернейм, того кто создал ссылку
                else:
                    writher.create_user(str(message.from_user.id), message.from_user.full_name, "no", str(0))
                    args = message.get_args()
                    reference = decode_payload(args)
                    if reference == "":
                        await bot.send_message(message.from_user.id, "Assalomu aleykum", reply_markup=klaviatura)
                    elif reference == message.from_user.full_name:
                        await bot.send_message(message.from_user.id, "Siz o'zingizga-o'zingiz referal bo'la olmaysiz.",
                                               reply_markup=klaviatura)
                    elif reference == message.from_user.full_name:
                        await bot.send_message(message.from_user.id, "Siz o'zingizga-o'zingiz referal bo'la olmaysiz.",
                                               reply_markup=klaviatura)
                    else:
                        user = list(writher.getUser(reference).values())
                        writher.changecountandsum(reference, user[1], user[2], int(user[3]) + 1, int(user[4]) + 500)
                        await bot.send_message(reference,
                                               f"Sizning {int(user[3]) + 1}-do'stingiz {message.from_user.full_name} botga tashrif buyurdi.",
                                               reply_markup=klaviatura)
                        await message.answer(
                            f"{user[1]} do'stingiz sizni bu botga taklif qildi.",
                            reply_markup=klaviatura)  # здесь в  reference должен быть юзернейм, того кто создал ссылку
            else:
                await bot.send_message(message.from_user.id, text=NOT_SUB_MESSAGE, reply_markup=btns.checkSubMenu)

@dp.message_handler(commands="users")
async def get_users(message: types.Message):
    if str(message.from_user.id) in admins:
        users = writher.getUsersL()
        await bot.send_message(message.from_user.id, text=users)
    else:
        if check_sub_channel(
                await bot.get_chat_member(chat_id=CHANNEL_ID[0], user_id=message.from_user.id)) and check_sub_channel(
                await bot.get_chat_member(chat_id=CHANNEL_ID[1], user_id=message.from_user.id)):

            if message.text == "konkurs825":
                await bot.send_message(message.from_user.id, text="Parol kiriting: ")
            else:
                await bot.send_message(message.from_user.id, text="Men bu buyruqqa javob bera olmayman.")
        else:
            if writher.checkblock(str(message.from_user.id)):
                await bot.send_message(message.from_user.id,
                                       text="❌ Afsuski, kanaldan chiqib ketibgansiz. Siz bloklangansiz.!")
            else:
                writher.create_user(str(message.from_user.id), f"{message.from_user.full_name}", "yes", str(0))
                await bot.send_message(message.from_user.id,
                                       text="❌ Afsuski, kanaldan chiqib ketibgansiz. Siz bloklangansiz.!")



@dp.message_handler(text="👤 kabinet")
async def change(message: types.Message):
    if check_sub_channel(
        await bot.get_chat_member(chat_id=CHANNEL_ID[0], user_id=message.from_user.id)) and check_sub_channel(
        await bot.get_chat_member(chat_id=CHANNEL_ID[1], user_id=message.from_user.id)) and check_sub_channel(
        await bot.get_chat_member(chat_id=CHANNEL_ID[2], user_id=message.from_user.id)):

        link = await get_start_link(str(message.from_user.id), encode=True)
        await bot.send_message(message.from_user.id, f"👤 kabinet:\n🔹 Ism-familya: {message.from_user.full_name}"
                                                     f"\n🔹 ID: {message.from_user.id}"
                                                     f"\n🔹 referal link: {link} ")
    else:
        writher.create_user(str(message.from_user.id), f"{message.from_user.full_name}", "yes", str(0))
        await bot.send_message(message.from_user.id,
                               text="❌ Afsuski, kanaldan chiqib ketibgansiz. Siz bloklangansiz.!")


@dp.message_handler()
async def bot_message(message: types.Message):
    if str(message.from_user.id) in admins:
        await bot.send_message(message.from_user.id, "Men bu buyruqni tushinmayman.")
    else:
        if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID[0], user_id=message.from_user.id)) and check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID[1], user_id=message.from_user.id)) and check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID[2], user_id=message.from_user.id)):
            if message.text == "konkurs825":
                await bot.send_message(message.from_user.id, text="Parol kiriting: ")
            else:
                await bot.send_message(message.from_user.id, text="Men bu buyruqqa javob bera olmayman.")
        else:
            if writher.checkblock(str(message.from_user.id)):
                await bot.send_message(message.from_user.id,
                                       text="❌ Afsuski, kanaldan chiqib ketibgansiz. Siz bloklangansiz.!")
            else:
                writher.create_user(str(message.from_user.id), f"{message.from_user.first_name}", "yes", str(0))
                await bot.send_message(message.from_user.id,
                                       text="❌ Afsuski, kanaldan chiqib ketibgansiz. Siz bloklangansiz.!")

















@dp.callback_query_handler(text="subchanneldone")
async def subchanneldone(query: types.Message):
    if writher.getUser(str(query.from_user.id)):
        await bot.send_message(query.from_user.id, "❗Siz bloklangansiz!")
    else:
        if check_sub_channel(
                await bot.get_chat_member(chat_id=CHANNEL_ID[0], user_id=query.from_user.id)) and check_sub_channel(
                await bot.get_chat_member(chat_id=CHANNEL_ID[1], user_id=query.from_user.id)) and check_sub_channel(
                await bot.get_chat_member(chat_id=CHANNEL_ID[2], user_id=query.from_user.id)):

            if str(query.from_user.id) in writher.getides():
                user = writher.getUser(str(query.from_user.id))
                print(query.from_user.id)
                if len(user["cheklov"]) == "yes":
                    await bot.send_message(query.from_user.id,
                                               text="Afsuski, siz bot kanaldan chiqib ketgansiz. Bot uchun siz bloklandingiz. Siz konkursda qatnasha olmaysiz.")
                else:
                    print(query.from_user.id)
                    if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID[0],
                                                                   user_id=query.from_user.id)) and check_sub_channel(
                            await bot.get_chat_member(chat_id=CHANNEL_ID[1],
                                                      user_id=message.from_user.id)) and check_sub_channel(
                            await bot.get_chat_member(chat_id=CHANNEL_ID[2], user_id=message.from_user.id)):
                        klaviatura = types.ReplyKeyboardMarkup(resize_keyboard=True)
                        klaviatura.insert(types.KeyboardButton(text="👤 kabinet"))
                        if str(query.from_user.id) in writher.getides():
                            args = query.get_args()
                            reference = decode_payload(args)
                            if reference == "":
                                await bot.send_message(query.from_user.id, "Assalomu aleykum", reply_markup=klaviatura)
                            elif reference == query.from_user.full_name:
                                await bot.send_message(query.from_user.id,
                                                       "Siz o'zingizga-o'zingiz referal bo'la olmaysiz.",
                                                       reply_markup=klaviatura)
                            else:
                                user = list(writher.getUser(reference).values())
                                await bot.send_message(reference,
                                                       f"Sizning {(user[1])} do'stingiz botga oldinroq tashrif buyurgan. U siz uchun referal bo'la olmaydi.",
                                                       reply_markup=klaviatura)
                                await query.answer(
                                    f"Siz botga oldinroq boshqa do'stingiz tomonidan taklif qilingansiz. {user[1]} uchun referal bo'la olmaysiz.",
                                    reply_markup=klaviatura)  # здесь в  reference должен быть юзернейм, того кто создал ссылку
                        else:
                            writher.create_user(str(query.from_user.id), query.from_user.full_name, "no", str(0))
                            args = query.get_args()
                            reference = decode_payload(args)
                            if reference == "":
                                await bot.send_message(query.from_user.id, "Assalomu aleykum", reply_markup=klaviatura)
                            elif reference == query.from_user.full_name:
                                await bot.send_message(message.from_user.id,
                                                       "Siz o'zingizga-o'zingiz referal bo'la olmaysiz.",
                                                       reply_markup=klaviatura)
                            elif reference == query.from_user.full_name:
                                await bot.send_message(query.from_user.id,
                                                       "Siz o'zingizga-o'zingiz referal bo'la olmaysiz.",
                                                       reply_markup=klaviatura)
                            else:
                                user = list(writher.getUser(reference).values())
                                writher.changecountandsum(reference, user[1], user[2], int(user[3]) + 1)
                                await bot.send_message(reference,
                                                       f"Sizning {int(user[3]) + 1}-do'stingiz {query.from_user.full_name} botga tashrif buyurdi.",
                                                       reply_markup=klaviatura)
                                await message.answer(
                                    f"{user[1]} do'stingiz sizni bu botga taklif qildi.",
                                    reply_markup=klaviatura)  # здесь в  reference должен быть юзернейм, того кто создал ссылку

        else:
            await bot.send_message(query.from_user.id, text=NOT_SUB_MESSAGE, reply_markup=btns.checkSubMenu)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
