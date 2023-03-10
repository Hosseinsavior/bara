#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AbirHasan2005

from bot.get_cfg import get_config


class Localisation:
    START_TEXT = "Hello, \n\nThis is a Telegram <b>Video Compress Bot</b>. \n\n<b>Please send me any Telegram big video file I will compress it as s small video file!</b> \n\n/help for more details. \n\nSupport Group: @danisooper"
   
    ABS_TEXT = " Please don't be selfish."
    
    FORMAT_SELECTION = "Select the desired format: <a href='{}'>file size might be approximate</a> \nIf you want to set custom thumbnail, send photo before or quickly after tapping on any of the below buttons.\nYou can use /deletethumbnail to delete the auto-generated thumbnail."
    
    
    DOWNLOAD_START = "ð¥ áªOá¯ááªOá©áªIáG ... ð¥ \n"
    
    UPLOAD_START = "ð¤ áá­ááªá©áááá ... ð¤ \n"
    
    COMPRESS_START = "ð á¢áá©ááá á¢áª ááªá°á­áá´áá ... ð"
    
    RCHD_BOT_API_LIMIT = "sá¥áá¬ á¶áá¬áªáá¬á áháªá máªxá¥mum áªááá¾á³á¬á  sá¥áá¬ (50mb). áá¬áá¬ááháá¬ss, ááá½á¥áá¶ áá¾ uá¢áá¾áªá ."
    
    RCHD_TG_API_LIMIT = "á á¾á³ááá¾áªá á¬á  á¥á {} sá¬áá¾áá s.\ná á¬áá¬ááá¬á  fá¥áá¬ sá¥áá¬: {}\nsá¾ááá½. buá, á¥ ááªááá¾á uá¢áá¾áªá  fá¥áá¬s á¶áá¬áªáá¬á áháªá 1.95á¶b á uá¬ áá¾ áá¬áá¬á¶ááªm áªá¢á¥ áá¥má¥ááªáá¥á¾ás."
    
    COMPRESS_SUCCESS = "ð¥ á á¾á³ááá¾áªá á¬á  á¥á {}\n\nð áá¾má¢áá¬ssá¬á  á¥á {}\n\nð¤ uá¢áá¾áªá á¬á  á¥á {}\n\nbá½ @Savior_128"

    COMPRESS_PROGRESS = "â³ á¬ááª: {}\nð á¢áá¾á¶áá¬ss: {}%"
    SAVED_CUSTOM_THUMB_NAIL = "áusáá¾m áá¥á á¬á¾ / fá¥áá¬ áhumbááªá¥á sáªáá¬á . áhá¥s á¥máªá¶á¬ á³á¥áá bá¬ usá¬á  á¥á áhá¬ áá¥á á¬á¾ / fá¥áá¬."
    
    DEL_ETED_CUSTOM_THUMB_NAIL = "â áusáá¾m áhumbááªá¥á ááá¬áªáá¬á  suááá¬sfuááá½."
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "â má¬á á¥áª ááá¬áªáá¬á  suááá¬sfuááá½."
    
    SAVED_RECVD_DOC_FILE = "â á á¾á³ááá¾áªá á¬á  suááá¬ssfuááá½."
    
    CUSTOM_CAPTION_UL_FILE = " "
    
    NO_CUSTOM_THUMB_NAIL_FOUND = "áO ááÕTOá° Tá¼áá°á·áá©Iáª á´Oáááª."
    
    NO_VOID_FORMAT_FOUND = "no-one gonna help you\n{}"
    
    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> added to {} till {}."
    
    FF_MPEG_RO_BOT_STOR_AGE_ALREADY_EXISTS = "â ï¸ áªááá¬áªá á½ á¾áá¬ á¢áá¾áá¬ss á¶á¾á¥áá¶ á¾á! â ï¸ \n\náhá¬áá¦ áá¥áá¬ sááªáus á¾á uá¢á áªáá¬s áháªááá¬á."
    
    HELP_MESSAGE = get_config(
        "sááá¥áá¶s_há¬áá¢_má¬ssáªá¶á¬",
        "há¥, á¥ áªm áá¥á á¬á¾ áá¾má¢áá¬ssá¾á bá¾á \n\n. sá¬áá  má¬ á½á¾uá áá¬áá¬á¶ááªm bá¥á¶ áá¥á á¬á¾ fá¥áá¬ \n2. áá¬á¢áá½ áá¾ áhá¬ fá¥áá¬ á³á¥áh: /áá¾má¢áá¬ss 50 \n\nsuá¢á¢á¾áá á¶áá¾uá¢: @danisooper"
    )
    WRONG_MESSAGE = get_config(
        "STRINGS_WRONG_MESSAGE",
        "current CHAT ID: <code>{CHAT_ID}</code>"
    )

    
