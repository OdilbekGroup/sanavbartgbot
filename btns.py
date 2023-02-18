from main import types

btnurlChannel1 = types.InlineKeyboardButton(text="Obuna bo'lish", url="https://T.me/sanavbar_kitoblar")
btnurlChannel2 = types.InlineKeyboardButton(text="Obuna bo'lish", url="https://T.me/kitobiddin")
btnurlChannel3 = types.InlineKeyboardButton(text="Obuna bo'lish", url="https://T.me/attoriddin")
btndonSubChannel = types.InlineKeyboardButton(text="✅ Obuna bo'ldim", callback_data="subchanneldone")

checkSubMenu = types.InlineKeyboardMarkup(row_width=1)
checkSubMenu.add(btnurlChannel1, btnurlChannel2, btndonSubChannel)