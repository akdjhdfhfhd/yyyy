from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def botplaylist_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="ᴩᴇʀsᴏɴᴀʟ",
                callback_data="get_playlist_playmode",
            ),
            InlineKeyboardButton(
                text="ɢʟᴏʙᴀʟ", callback_data="get_top_playlists"
            ),
        ],
        [
            InlineKeyboardButton(
                text="✯ اغلاق ✯", callback_data="close"
            ),
        ],
    ]
    return buttons


def top_play_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="ᴛᴏᴘ 10 ᴘʟᴀʏʟɪsᴛs", callback_data="SERVERTOP"
            )
        ],
        [
            InlineKeyboardButton(
                text="ᴘᴇʀsᴏɴᴀʟ", callback_data="SERVERTOP user"
            )
        ],
        [
            InlineKeyboardButton(
                text="ɢʟᴏʙᴀʟ", callback_data="SERVERTOP global"
            ),
            InlineKeyboardButton(
                text="ɢʀᴏᴜᴘ's", callback_data="SERVERTOP chat"
            )
        ],
        [
            InlineKeyboardButton(
                text="♡ رجوع ♡", callback_data="get_playmarkup"
            ),
            InlineKeyboardButton(
                text="☆ اغلاق ☆", callback_data="close"
            ),
        ],
    ]
    return buttons


def get_playlist_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="ᴀᴜᴅɪᴏ", callback_data="play_playlist a"
            ),
            InlineKeyboardButton(
                text="ᴠɪᴅᴇᴏ", callback_data="play_playlist v"
            ),
        ],
        [
            InlineKeyboardButton(
                text="♡ رجوع ♡", callback_data="home_play"
            ),
            InlineKeyboardButton(
                text="☆ اغلاق ☆", callback_data="close"
            ),
        ],
    ]
    return buttons


def top_play_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="ᴛᴏᴘ 10 ᴘʟᴀʏʟɪsᴛs", callback_data="SERVERTOP"
            )
        ],
        [
            InlineKeyboardButton(
                text="ᴘᴇʀsᴏɴᴀʟ", callback_data="SERVERTOP Personal"
            )
        ],
        [
            InlineKeyboardButton(
                text="ɢʟᴏʙᴀʟ", callback_data="SERVERTOP Global"
            ),
            InlineKeyboardButton(
                text="ɢʀᴏᴜᴘ's", callback_data="SERVERTOP Group"
            )
        ],
        [
            InlineKeyboardButton(
                text="♡ رجوع ♡", callback_data="get_playmarkup"
            ),
            InlineKeyboardButton(
                text="☆ اغلاق ☆", callback_data="close"
            ),
        ],
    ]
    return buttons


def failed_top_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="♡ رجوع ♡",
                callback_data="get_top_playlists",
            ),
            InlineKeyboardButton(
                text="☆ اغلاق ☆", callback_data="close"
            ),
        ],
    ]
    return buttons


def warning_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="ᴅᴇʟᴇᴛᴇ",
                    callback_data="delete_whole_playlist",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="♡ رجوع ♡",
                    callback_data="del_back_playlist",
                ),
                InlineKeyboardButton(
                    text="☆ اغلاق ☆",
                    callback_data="close",
                ),
            ],
        ]
    )
    return upl


def close_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="✯ اغلاق ✯",
                    callback_data="close",
                ),
            ]
        ]
    )
    return upl


function targma(msg)
text = nil
if msg and msg.content and msg.content.text then
text = msg.content.text.text
end
msg_chat_id = msg.chat_id
msg_id = msg.id
if tonumber(msg.sender_id.user_id) == tonumber(Fast) then
return false
end
if text then
local neww = Redis:get(Fast.."Get:Reides:Commands:Group"..msg.chat_id..":"..text)
if neww then
text = neww or text
end
end
if text == 'ترجمه' or text == 'ترجمة' or text == 'ترجم' or text == 'translat' then 
local reply_markup = bot.replyMarkup{
type = 'inline',
data = {
{{text = 'ترجمه الي العربية', data = msg.sender_id.user_id..'toar'},{text = 'ترجمه الي الانجليزية', data = msg.sender_id.user_id..'toen'}},
{{text = '𝑆𝑂𝑈𝑅𝐶𝐸 𝐻𝐴𝑀𝐷', url = "https://t.me/ah05v"}},
}
}
return send(msg_chat_id,msg_id, [[*
• Hey Send Text translate
• ارسل النص لترجمته
*]],"md",false, false, false, false, reply_markup)
end

end
return {Fast = targma}
        ),
            ]
        ]
    )
    return upl
