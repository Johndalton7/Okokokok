#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.errors import UserNotParticipant
from bot import Translation # pylint: disable=import-error
from bot.database import Database # pylint: disable=import-error

db = Database()

@Client.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot, update):
    update_channel = "@MF_MOVIES1"
    if update_channel:
        try:
            user = await bot.get_chat_member(update_channel, update.chat.id)
            if user.status == "kicked out":
               await update.reply_text("??五 Sorry Dude, You are B A N N E D ??不??不??不")
               return
        except UserNotParticipant:
            #await update.reply_text(f"Join @{update_channel} To Use Me")
            await update.reply_text(
                text="<b>??五 ???????滕??塔??? ???ｈ??????? ???????氣??塔??? ???埠??蛤??氣??鳶??鳶??莞??? ??五\n\n鉥兒曾鉥?鉞?鉥?鉞擒??鉞? 鉥詮曾鉥兒曾鉥桌??鉞? 鉥菽??鉥?鉞?? 鉥?鉥戈曾鉥兒晷鉥能曾 鉥?鉥舟??鉥能?? 鉥兒曾鉥?鉞?鉥?鉞? 鉥?鉞?鉥能??鉥能??鉥?鉞?鉥?鉥戈?? 鉥?鉥?鉞?鉥?鉥喪??鉥?鉞? 鉥桌??鉥能曾鉞? 鉥?鉥擒捶鉥耜曾鉞? 鉥?鉞?鉥能曾鉞? 鉥?鉥菽??鉥? 鉥?鉥兒??鉥兒握鉥擒提鉞???五... ????\n\nJoin 鉥?鉞?鉥能握鉥戈??鉥戈曾鉥兒?? 鉥嗣??鉥獅?? 鉥菽??鉥?鉞?鉥?鉞?鉥? 鉥眇??鉥?鉞?鉥?鉞? /start 鉥?鉥?鉞?鉥?鉞? AND FEEL THE MAGIC.????</b>",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text=" ??五JOIN OUR CHANNEL??五 ", url=f"https://t.me/MF_MOVIES1")]
              ])
            )
            return
        except Exception:
            await update.reply_text("Something Wrong. Contact my Support Group")
            return
    
    try:
        file_uid = update.command[1]
    except IndexError:
        file_uid = False
    
    if file_uid:
        file_id, file_name, file_caption, file_type = await db.get_file(file_uid)
        
        if (file_id or file_type) == None:
            return
        
        caption = file_caption if file_caption != ("" or None) else ("<code>" + file_name + "</code>")
        try:
            await update.reply_cached_media(
                file_id,
                quote=True,
                caption = "???埠??? 鉥?鉞?鉥?鉞?鉥戈善 鉥詮曾鉥兒曾鉥桌??鉞擒??鉞?鉥?鉞?鉥? 鉥桌敢鉞?鉥晤?? 鉥菽曾鉥菽敦鉥?鉞?鉥?鉞擒??鉞?鉥?鉞?鉥桌晷鉥能曾 鉥?鉥?鉞?鉥?鉥喪??鉥?鉞? Group 鉞? 鉥?鉞?鉥能曾鉞? 鉥?鉞?鉥能??鉥能??????\n\n鉏? ????????Ｔ????Ｔ?? ?????Ｔ????Ｔ?????鉏? \nChannel??????? @MF_MOVIES1Group   \n???乒?? @MF_CHATGROUP",
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    'CHANNEL??云', url="https://t.me/MF_MOVIES1"
                                )
                        ]
                    ]
                )
            )
        except Exception as e:
            await update.reply_text(f"<b>Error:</b>\n<code>{e}</code>", True, parse_mode="html")
            LOGGER(__name__).error(e)
        return

    buttons = [[
        InlineKeyboardButton('???儭? JOIN', url='https://t.me/MF_MOVIES1'),
        InlineKeyboardButton('SOURCE CODE', url ='https://github.com/CrazyBotsz/Adv-Auto-Filter-Bot-V2')
    ],[
        InlineKeyboardButton('??鳴?? GROUP', url='https://t.me/MF_CHATGROUP')
    ],[
        InlineKeyboardButton('???？ELP', callback_data="help")
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT.format(
                update.from_user.first_name),
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["help"]) & filters.private, group=1)
async def help(bot, update):
    buttons = [[
        InlineKeyboardButton('Home ???', callback_data='start'),
        InlineKeyboardButton('About ????', callback_data='about')
    ],[
        InlineKeyboardButton('Close ????', callback_data='close')
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_TEXT,
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["about"]) & filters.private, group=1)
async def about(bot, update):
    
    buttons = [[
        InlineKeyboardButton('Home ???', callback_data='start'),
        InlineKeyboardButton('Close ????', callback_data='close')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_TEXT,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )
