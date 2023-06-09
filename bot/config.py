#    This file is part of the AutoAnime distribution.
#    Copyright (c) 2023 Kaif_00z
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
# License can be found in <
# https://github.com/kaif-00z/AutoAnimeBOt/blob/main/LICENSE > .

from decouple import config


class Var:
    REDIS_URI = config("redis://admin:7518@Sidd@redis://default:Pn2F48emzKB7TE1nDuUAVDG8yLSmTZuK@redis-17361.c305.ap-south-1-1.ec2.cloud.redislabs.com:17361/Disha-free-db", default=None)
    REDIS_PASS = config("7518@Sidd", default=None)
    API_ID = config("26019444", default=6, cast=int)
    API_HASH = config("a308fac723905cdbd836414b18f3b3d6", default="")
    BOT_TOKEN = config("6100344970:AAGrq-OnnEwz9KBahxtCcdo68pXG7kV6Z1I", default=None)
    BACKUP = config("BACKUP", default=0, cast=int)
    FFMPEG = config("FFMPEG", default="ffmpeg")
    CHAT = config("", default=None)
    THUMB = config(
        "https://te.legra.ph/file/7489c3a0ff4002c01253b.jpg", default="https://te.legra.ph/file/7489c3a0ff4002c01253b.jpg"
    )
    LOG_CHANNEL = config("-1001970622682", default=0, cast=int)
    CLOUD = config("1001802196143", default=None)
    GDRIVE_FOLDER_ID = config("GDRIVE_FOLDER_ID", default=None)
    TOKEN_FILE_LINK = config("TOKEN_FILE_LINK", default=None)
    INDEX_LINK = config("INDEX_LINK", default="https://github.com/")
    OWNERS = config("6046532356", default="")
    GDRIVE_UPLOAD = config("GDRIVE_UPLOAD", default=False, cast=bool)
