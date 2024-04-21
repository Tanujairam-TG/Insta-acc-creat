from Bot import app
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

user_vault = {}

@app.on_message(filters.command("start") & filters.private)
async def start_command(client, message):
    await message.reply_photo(
        photo="http://telegra.ph/file/4beb984109631f88704b8.jpg",
        caption="Welcome To The World of Solo Leveling. What are you in The World Of Solo Leveling?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Hunter", callback_data="start_hun"),
                    InlineKeyboardButton("Healer", callback_data="start_heal")
                ]
            ]
        )
    )

@app.on_callback_query(filters.regex(r'^start_'))
async def start_callbacks(client, query):
    data = query.data
    user_id = query.from_user.id
    if data == "start_hun":
        await query.message.reply_photo(
            photo="http://telegra.ph/file/9471582944eb83307d974.jpg",
            caption="You Have Choosen Hunter Section. Which Starter Hunter You Choose?",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Cho Kyuhwan", callback_data="cho_hun"),
                        InlineKeyboardButton("Yoo Jino", callback_data="yoo_hun"),
                        InlineKeyboardButton("Kim Sangshik", callback_data="kim_hun")
                    ]
                ]
            )
        )
    elif data == "start_heal":
        await query.message.reply_photo(
            photo="http://telegra.ph/file/0d4be1568394286e2e946.jpg",
            caption="You Have Chosen the Healer Section. Which Healer Would You Like to Be?",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Lee Joohee", callback_data="lee_heal"),
                        InlineKeyboardButton("Jun Yerim", callback_data="jun_heal"),
                        InlineKeyboardButton("Park Minseok", callback_data="park_heal")
                    ]
                ]
            )
        )

@app.on_callback_query(filters.regex(r'^(cho_hun|yoo_hun|kim_hun|lee_heal|jun_heal|park_heal)'))
async def character_selection_callback(client, query):
    data = query.data
    user_id = query.from_user.id
    character_name = {
        "cho_hun": "Cho Kyuhwan",
        "yoo_hun": "Yoo Jino",
        "kim_hun": "Kim Sangshik",
        "lee_heal": "Lee Joohee",
        "jun_heal": "Jun Yerim",
        "park_heal": "Park Minseok"
    }[data]
    category = "hunters" if "hun" in data else "healers"
    
    user_data = user_vault.setdefault(user_id, {"hunters": [], "healers": []})
    if character_name in user_data["hunters"] or character_name in user_data["healers"]:
        await query.message.reply_text("You have already selected a character.")
    else:
        user_data[category].append(character_name)
        await query.message.reply_text(f"{character_name} has been added to your vault.")

@app.on_message(filters.command("vault"))
async def vault_command(client, message):
    user_id = message.from_user.id
    user_data = user_vault.get(user_id)
    if user_data:
        hunters = "\n".join(user_data.get("hunters", []))
        healers = "\n".join(user_data.get("healers", []))
        response_text = (
            f"Total Hunters: {len(user_data.get('hunters', []))}\n"
            f"Total Healers: {len(user_data.get('healers', []))}\n\n"
            f"Hunters:\n{hunters}\n\n"
            f"Healers:\n{healers}"
        )
    else:
        response_text = "Your vault is empty. Choose your characters using /start."
    
    await message.reply_text(response_text)
