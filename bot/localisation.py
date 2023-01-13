#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AbirHasan2005

from bot.get_cfg import get_config


class Localisation:
    START_TEXT = "Hello, \n\nThis is a Telegram <b>Video Compress Bot</b>. \n\n<b>Please send me any Telegram big video file I will compress it as s small video file!</b> \n\n/help for more details. \n\nSupport Group: @danisooper"
   
    ABS_TEXT = " Please don't be selfish."
    
    FORMAT_SELECTION = "Select the desired format: <a href='{}'>file size might be approximate</a> \nIf you want to set custom thumbnail, send photo before or quickly after tapping on any of the below buttons.\nYou can use /deletethumbnail to delete the auto-generated thumbnail."
    
    
    DOWNLOAD_START = "📥 ᗪOᗯᑎᒪOᗩᗪIᑎG ... 📥 \n"
    
    UPLOAD_START = "📤 ᑌᑭᏞᝪᗩᗞᏆᑎᏀ ... 📤 \n"
    
    COMPRESS_START = "📀 ᎢᖇᎩᏆᑎᏀ Ꭲᝪ ᑕᝪᗰᑭᖇᗴᔑᔑ ... 📀"
    
    RCHD_BOT_API_LIMIT = "sᎥᏃᎬ ᎶᏒᎬᎪᏆᎬᏒ ᏆhᎪᏁ mᎪxᎥmum ᎪᏞᏞᎾᎳᎬᎠ sᎥᏃᎬ (50mb). ᏁᎬᏉᎬᏒᏆhᏞᎬss, ᏆᏒᎽᎥᏁᎶ ᏆᎾ uᏢᏞᎾᎪᎠ."
    
    RCHD_TG_API_LIMIT = "ᎠᎾᎳᏁᏞᎾᎪᎠᎬᎠ ᎥᏁ {} sᎬᏟᎾᏁᎠs.\nᎠᎬᏆᎬᏟᏆᎬᎠ fᎥᏞᎬ sᎥᏃᎬ: {}\nsᎾᏒᏒᎽ. buᏆ, Ꭵ ᏟᎪᏁᏁᎾᏆ uᏢᏞᎾᎪᎠ fᎥᏞᎬs ᎶᏒᎬᎪᏆᎬᏒ ᏆhᎪᏁ 1.95Ꮆb ᎠuᎬ ᏆᎾ ᏆᎬᏞᎬᎶᏒᎪm ᎪᏢᎥ ᏞᎥmᎥᏆᎪᏆᎥᎾᏁs."
    
    COMPRESS_SUCCESS = "📥 ᎠᎾᎳᏁᏞᎾᎪᎠᎬᎠ ᎥᏁ {}\n\n📀 ᏟᎾmᏢᏒᎬssᎬᎠ ᎥᏁ {}\n\n📤 uᏢᏞᎾᎪᎠᎬᎠ ᎥᏁ {}\n\nbᎽ @Savior_128"

    COMPRESS_PROGRESS = "⏳ ᎬᏆᎪ: {}\n🚀 ᏢᏒᎾᎶᏒᎬss: {}%"
    SAVED_CUSTOM_THUMB_NAIL = "ᏟusᏆᎾm ᏉᎥᎠᎬᎾ / fᎥᏞᎬ ᏆhumbᏁᎪᎥᏞ sᎪᏉᎬᎠ. ᏆhᎥs ᎥmᎪᎶᎬ ᎳᎥᏞᏞ bᎬ usᎬᎠ ᎥᏁ ᏆhᎬ ᏉᎥᎠᎬᎾ / fᎥᏞᎬ."
    
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ ᏟusᏆᎾm ᏆhumbᏁᎪᎥᏞ ᏟᏞᎬᎪᏒᎬᎠ suᏟᏟᎬsfuᏞᏞᎽ."
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "✅ mᎬᎠᎥᎪ ᏟᏞᎬᎪᏒᎬᎠ suᏟᏟᎬsfuᏞᏞᎽ."
    
    SAVED_RECVD_DOC_FILE = "✅ ᎠᎾᎳᏁᏞᎾᎪᎠᎬᎠ suᏟᏟᎬssfuᏞᏞᎽ."
    
    CUSTOM_CAPTION_UL_FILE = " "
    
    NO_CUSTOM_THUMB_NAIL_FOUND = "ᑎO ᑕᑌՏTOᗰ TᕼᑌᗰᗷᑎᗩIᒪ ᖴOᑌᑎᗪ."
    
    NO_VOID_FORMAT_FOUND = "no-one gonna help you\n{}"
    
    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> added to {} till {}."
    
    FF_MPEG_RO_BOT_STOR_AGE_ALREADY_EXISTS = "⚠️ ᎪᏞᏒᎬᎪᎠᎽ ᎾᏁᎬ ᏢᏒᎾᏟᎬss ᎶᎾᎥᏁᎶ ᎾᏁ! ⚠️ \n\nᏟhᎬᏟᏦ ᏞᎥᏉᎬ sᏆᎪᏆus ᎾᏁ uᏢᎠᎪᏆᎬs ᏟhᎪᏁᏁᎬᏞ."
    
    HELP_MESSAGE = get_config(
        "sᏆᏒᎥᏁᎶs_hᎬᏞᏢ_mᎬssᎪᎶᎬ",
        "hᎥ, Ꭵ Ꭺm ᏉᎥᎠᎬᎾ ᏟᎾmᏢᏒᎬssᎾᏒ bᎾᏆ \n\n. sᎬᏁᎠ mᎬ ᎽᎾuᏒ ᏆᎬᏞᎬᎶᏒᎪm bᎥᎶ ᏉᎥᎠᎬᎾ fᎥᏞᎬ \n2. ᏒᎬᏢᏞᎽ ᏆᎾ ᏆhᎬ fᎥᏞᎬ ᎳᎥᏆh: /ᏟᎾmᏢᏒᎬss 50 \n\nsuᏢᏢᎾᏒᏆ ᎶᏒᎾuᏢ: @danisooper"
    )
    WRONG_MESSAGE = get_config(
        "STRINGS_WRONG_MESSAGE",
        "current CHAT ID: <code>{CHAT_ID}</code>"
    )

    
