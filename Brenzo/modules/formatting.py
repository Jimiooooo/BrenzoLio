from Brenzo.modules.helper_funcs.decorators import kigcallback
from telegram import (
    ParseMode,
    Update,
    Bot,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from telegram.ext import CommandHandler, Filters, MessageHandler, CallbackQueryHandler
from Brenzo.modules.tr_engine.strings import tld

def fmt_md_help(bot: Bot, update: Update):
    chat = update.effective_chat
    update.effective_message.reply_text(
        tld(chat.id, 'md_help'),
        parse_mode=ParseMode.HTML,
    )


def fmt_filling_help(bot: Bot, update: Update):
    chat = update.effective_chat
    update.effective_message.reply_text(
        tld(chat.id, 'filling_help'),
        parse_mode=ParseMode.HTML,
    )



@kigcallback(pattern=r"fmt_help_")
def fmt_help(bot: Bot, update: Update):
    query = update.callback_query
    bot = context.bot
    help_info = query.data.split("fmt_help_")[1]
    if help_info == "md":
        help_text = tld(chat.id, 'md_help')
    elif help_info == "filling":
        help_text = tld(chat.id, 'filling_help')
    query.message.edit_text(
        text=help_text,
        parse_mode=ParseMode.HTML,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(text="Back", callback_data=f"help_module({__mod_name__.lower()})"),
            InlineKeyboardButton(text='Report Error', url='https://t.me/YorkTownEagleUnion')]]
        ),
    )
    bot.answer_callback_query(query.id)

__mod_name__ = 'Formatting'

def get_help(chat):
    return [tld(chat, "formt_help_bse"),
    [
        InlineKeyboardButton(text="Markdown", callback_data="fmt_help_md"),
        InlineKeyboardButton(text="Filling", callback_data="fmt_help_filling")
    ]
]
