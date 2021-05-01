# Taken from USERGE_X and modifications done by NeitXD

"""Spammy Animations Module 2☠️"""
import asyncio

from userge import Message, userge


@userge.on_cmd("call$", about={"header": "Call TG headquarters"})
async def call_(message: Message):
    """call"""
    animation_interval = 3
    animation_ttl = range(0, 18)
    await message.edit("Calling")
    animation_chars = [
        "`Connecting To Telegram Headquarters...`",
        "`Call Connected.`",
        "`Telegram: Hello This is Telegram HQ. Who is this?`",
        f"`Me: Yo this is` {mention} ,`Please Connect me to my big bro, Rahul `",
        "`Rahul sir is busy , doing Chutiyappa.`",
        "`Calling Asmo `  `At +916969696969`",
        "`Private  Call Connected...`",
        "`Me: Hello Sir, Please Ban This Telegram Account.`",
        "`Asmo : May I Know Who Is This?`",
        "`Me: Yo Brah, I Am` @NeitXD ",
        "`Asmo : OMG!!! Long time no see, Wassup cat...\nI'll Make Sure That Guy Account Will Get Blocked Within 24Hrs.`",
        "`Me: Thanks, See You Later Brah.`",
        "`Asmo : Please Don't Thank Brah, Telegram Is Our's. Just Gimme A Call When You Become Free.`",
        "`Me: Is There Any Issue/Emergency???`",
        "`Asmo : Yes Sur, There Is A Bug In Telegram v69.6.9.\nI Am Not Able To Fix It. If Possible, Please Help Fix The Bug.`",
        "`Me: Send Me The App On My Telegram Account, I Will Fix The Bug & Send You.`",
        "`Asmo : Sure Sur \nTC Bye Bye :)`",
        "`Private Call Disconnected.`",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await message.edit(animation_chars[i % 18])


@userge.on_cmd("deploy$", about={"header": "Deploy UB on Heroku"})
async def deploy_(message: Message):
    """deploy"""
    animation_interval = 3
    animation_ttl = range(0, 12)
    await message.edit("Deploying")
    animation_chars = [
        "**Heroku Connecting To Latest Github Build **",
        "**Build started by user** @NeitXD",
        "**Deploy** `535a74f0` **by user** @NeitXD",
        "**Restarting Heroku Server...**",
        "**State changed from up to starting**",
        "**Stopping all processes with SIGTERM**",
        "**Process exited with** `status 143`",
        "**Starting process with command** `python3 -m stdborg`",
        "**State changed from starting to up**",
        "__INFO:Userbot:Logged in as 557667062__",
        "__INFO:Userbot:Successfully loaded all plugins__",
        "**Build Succeeded**",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await message.edit(animation_chars[i % 12])
