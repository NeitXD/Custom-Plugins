""" Chat info, Join and leave chat, tagall and tag admins """

# by @Krishna_Singhal

import html
import os
import asyncio

from pyrogram.errors.exceptions.bad_request_400 import (
    BadRequest,
    UsernameOccupied,
    UsernameInvalid,
    UsernameNotOccupied,
    PeerIdInvalid)

from userge import userge, Config, Message

LOG = userge.getLogger(__name__)

def mention_html(user_id, name):
    return u'<a href="tg://user?id={}">{}</a>'.format(user_id, html.escape(name))
    
    @userge.on_cmd("users", about={
    'header': "get userid of 100 recent members",
    'usage': "{tr}.users [Chat Id]"},
    allow_via_bot=False, allow_private=False, only_admins=False)
async def users_(message: Message):
    """ Tag recent members """
    c_title = message.chat.title
    c_id = message.chat.id
    await message.edit(f"`Checking recent users`")
    text = f"**{text}**\n" if text else ""
    message_id = replied.message_id if replied else None
    try:
        async for members in message.client.iter_chat_members(c_id, filter="recent"):
            if not members.user.is_bot:
                u_id = members.user.id
                f_name = (await message.client.get_user_dict(u_id))['fname']
                if u_name:
                    text += f"`{u_id}` "
                else:
                    text += f"`{u_id}` "
    except Exception as e:
        text += " " + str(e)
    await message.client.send_message(c_id, text, reply_to_message_id=message_id)
    await message.edit("```Tagged recent Members Successfully...```", del_in=3)
