import html
import random, re
import requests as r

from telegram import Update, ParseMode, TelegramError, MAX_MESSAGE_LENGTH
from telegram.ext import Filters, CallbackContext, CommandHandler, run_async
from telegram.error import BadRequest
from telegram.utils.helpers import escape_markdown

from Funny.modules.helper_funcs.extraction import extract_user
from Funny.modules.helper_funcs.filters import CustomFilters
from Funny.modules.helper_funcs.alternate import typing_action
from Funny import dispatcher, DRAGONS, DEMONS, LOGGER, DEV_USERS
from Funny.modules.disable import DisableAbleCommandHandler, DisableAbleMessageHandler

import Funny.modules.helper_funcs.fun_strings as fun


@run_async
@typing_action
def truth(update, context):
    update.effective_message.reply_text(random.choice(fun.TRUTH))

@run_async
@typing_action
def dare(update, context):
    update.effective_message.reply_text(random.choice(fun.DARE))


#run
@run_async
@typing_action
def runs(update, context):
    update.effective_message.reply_text(random.choice(fun.RUN_STRINGS))


@run_async
@typing_action
def pat(update: Update, context: CallbackContext):
    bot = context.bot
    args = context.args
    message = update.effective_message

    reply_to = message.reply_to_message if message.reply_to_message else message

    curr_user = html.escape(message.from_user.first_name)
    user_id = extract_user(message, args)

    if user_id:
        patted_user = bot.get_chat(user_id)
        user1 = curr_user
        user2 = html.escape(patted_user.first_name)

    else:
        user1 = bot.first_name
        user2 = curr_user

    pat_type = random.choice(("Text", "Gif", "Sticker"))
    if pat_type == "Gif":
        try:
            temp = random.choice(fun.PAT_GIFS)
            reply_to.reply_animation(temp)
        except BadRequest:
            pat_type = "Text"

    if pat_type == "Sticker":
        try:
            temp = random.choice(fun.PAT_STICKERS)
            reply_to.reply_sticker(temp)
        except BadRequest:
            pat_type = "Text"

    if pat_type == "Text":
        temp = random.choice(fun.PAT_TEMPLATES)
        reply = temp.format(user1=user1, user2=user2)
        reply_to.reply_text(reply, parse_mode=ParseMode.HTML)


@run_async
@typing_action
def judge(update: Update, context: CallbackContext):
    judger = ["<b>is lying!</b>", "<b>is telling the truth!</b>"]
    rep = update.effective_message
    msg = ""
    msg = update.effective_message.reply_to_message
    if not msg:
        rep.reply_text("Reply to someone's message to judge them!")
    else:
        user = msg.from_user.first_name
    res = random.choice(judger)
    reply = msg.reply_text(f"{user} {res}", parse_mode=ParseMode.HTML)

@run_async
@typing_action
def slap(update, context):
    args = context.args
    msg = update.effective_message

    # reply to correct message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )

    # get user who sent message
    if msg.from_user.username:
        curr_user = "@" + escape_markdown(msg.from_user.username)
    else:
        curr_user = "[{}](tg://user?id={})".format(
            msg.from_user.first_name, msg.from_user.id)
        

    user_id = extract_user(update.effective_message, args)
    if user_id:
        slapped_user = context.bot.get_chat(user_id)
        user1 = curr_user
        if slapped_user.username:
            user2 = "@" + escape_markdown(slapped_user.username)
        else:
            user2 = "[{}](tg://user?id={})".format(
                slapped_user.first_name, slapped_user.id
            )

    # if no target found, bot targets the sender
    else:
        user1 = "[{}](tg://user?id={})".format(context.bot.first_name, context.bot.id)
        user2 = curr_user

    temp = random.choice(fun.SLAP_TEMPLATES)
    item = random.choice(fun.ITEMS)
    hit = random.choice(fun.HIT)
    throw = random.choice(fun.THROW)

    repl = temp.format(user1=user1, user2=user2, item=item, hits=hit, throws=throw)

    reply_text(repl, parse_mode=ParseMode.MARKDOWN)


#sanitize a user - by @saitamarobot
@run_async
@typing_action
def sanitize(update: Update, context: CallbackContext):
    message = update.effective_message
    name = message.reply_to_message.from_user.first_name if message.reply_to_message else message.from_user.first_name
    reply_animation = message.reply_to_message.reply_animation if message.reply_to_message else message.reply_animation
    reply_animation(
        random.choice(fun.GIFS), caption=f'*Sanitizes {name}*')


@run_async
@typing_action
def hug(update, context):
    args = context.args
    msg = update.effective_message  # type: Optional[Message]

    # reply to correct message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )

    # get user who sent message
    if msg.from_user.username:
        curr_user = "@" + escape_markdown(msg.from_user.username)
    else:
        curr_user = "[{}](tg://user?id={})".format(
            msg.from_user.first_name, msg.from_user.id
        )

    user_id = extract_user(update.effective_message, args)
    if user_id:
        hugged_user = context.bot.get_chat(user_id)
        user1 = curr_user
        if hugged_user.username:
            user2 = "@" + escape_markdown(hugged_user.username)
        else:
            user2 = "[{}](tg://user?id={})".format(
                hugged_user.first_name, hugged_user.id
            )

    # if no target found, bot targets the sender
    else:
        user1 = "Awwh! [{}](tg://user?id={})".format(
            context.bot.first_name, context.bot.id
        )
        user2 = curr_user

    temp = random.choice(fun.HUG_TEMPLATES)
    hug = random.choice(fun.HUG)

    repl = temp.format(user1=user1, user2=user2, hug=hug)

    reply_text(repl, parse_mode=ParseMode.MARKDOWN)







@run_async
@typing_action
def decide(update, context):
    args = update.effective_message.text.split(None, 1)
    if len(args) >= 2:  # Don't reply if no args
        reply_text = (
            update.effective_message.reply_to_message.reply_text
            if update.effective_message.reply_to_message
            else update.effective_message.reply_text
        )
        reply_text(random.choice(fun.DECIDE))




@run_async
@typing_action
def table(update, context):
    reply_text = (
        update.effective_message.reply_to_message.reply_text
        if update.effective_message.reply_to_message
        else update.effective_message.reply_text
    )
    reply_text(random.choice(fun.TABLE))





@run_async
def gbun(update, context):
    user = update.effective_user
    chat = update.effective_chat

    if update.effective_message.chat.type == "private":
        return
    if int(user.id) in DRAGONS or int(user.id) in DEMONS:
        context.bot.sendMessage(chat.id, (random.choice(fun.GBUN)))


@run_async
def gbam(update, context):
    user = update.effective_user
    chat = update.effective_chat
    bot, args = context.bot, context.args
    message = update.effective_message

    curr_user = html.escape(message.from_user.first_name)
    user_id = extract_user(message, args)
    

    if user_id:
        gbam_user = bot.get_chat(user_id)
        user1 = curr_user
        user2 = html.escape(gbam_user.first_name)

    else:
        user1 = curr_user
        user2 = bot.first_name


    if update.effective_message.chat.type == "private":
        return
    if int(user.id) in DRAGONS or int(user.id) in DEMONS:
        gbamm = fun.GBAM
        reason = random.choice(fun.GBAM_REASON)
        gbam = gbamm.format(user1=user1, user2=user2, chatid=chat.id, reason=reason)
        context.bot.sendMessage(chat.id, gbam, parse_mode=ParseMode.HTML)

@run_async
def gboom(update, context):
    user = update.effective_user
    chat = update.effective_chat
    bot, args = context.bot, context.args
    message = update.effective_message

    curr_user = html.escape(message.from_user.first_name)
    user_id = extract_user(message, args)

    if user_id:
        gbam_user = bot.get_chat(user_id)
        user1 = curr_user
        user2 = html.escape(gbam_user.first_name)

    else:
        user1 = curr_user
        user2 = bot.first_name


    if update.effective_message.chat.type == "private":
        return
    if int(user.id) in DRAGONS or int(user.id) in DEMONS:
        gbamm = fun.GBOOM
        reason = random.choice(fun.GBAM_REASON)
        gbam = gbamm.format(user1=user1, user2=user2, chatid=chat.id, reason=reason)
        context.bot.sendMessage(chat.id, gbam, parse_mode=ParseMode.HTML)

@run_async
@typing_action
def shout(update, context):
    args = context.args
    message = update.effective_message

    if message.reply_to_message:
        data = message.reply_to_message.text
    elif args:
        data = " ".join(args)
    else:
        data = ("I need a message to meme")

    msg = "```"
    result = []
    result.append(' '.join([s for s in data]))
    for pos, symbol in enumerate(data[1:]):
        result.append(symbol + ' ' + '  ' * pos + symbol)
    result = list("\n".join(result))
    result[0] = data[0]
    result = "".join(result)
    msg = "```\n" + result + "```"
    return update.effective_message.reply_text(msg, parse_mode="MARKDOWN")






@run_async
@typing_action
def owo(update, context):
    message = update.effective_message
    if not message.reply_to_message:
        message.reply_text("I need a message to meme.")
    else:
        faces = [
            "(・`ω´・)",
            ";;w;;",
            "owo",
            "UwU",
            ">w<",
            "^w^",
            "\(^o\) (/o^)/",
            "( ^ _ ^)∠☆",
            "(ô_ô)",
            "~:o",
            ";____;",
            "(*^*)",
            "(>_",
            "(♥_♥)",
            "*(^O^)*",
            "((+_+))",
        ]
        reply_text = re.sub(r"[rl]", "w", message.reply_to_message.text)
        reply_text = re.sub(r"[ｒｌ]", "ｗ", message.reply_to_message.text)
        reply_text = re.sub(r"[RL]", "W", reply_text)
        reply_text = re.sub(r"[ＲＬ]", "Ｗ", reply_text)
        reply_text = re.sub(r"n([aeiouａｅｉｏｕ])", r"ny\1", reply_text)
        reply_text = re.sub(r"ｎ([ａｅｉｏｕ])", r"ｎｙ\1", reply_text)
        reply_text = re.sub(r"N([aeiouAEIOU])", r"Ny\1", reply_text)
        reply_text = re.sub(r"Ｎ([ａｅｉｏｕＡＥＩＯＵ])", r"Ｎｙ\1", reply_text)
        reply_text = re.sub(r"\!+", " " + random.choice(faces), reply_text)
        reply_text = re.sub(r"！+", " " + random.choice(faces), reply_text)
        reply_text = reply_text.replace("ove", "uv")
        reply_text = reply_text.replace("ｏｖｅ", "ｕｖ")
        reply_text += " " + random.choice(faces)
        message.reply_to_message.reply_text(reply_text)


@run_async
@typing_action
def stretch(update, context):
    message = update.effective_message
    if not message.reply_to_message:
        message.reply_text("I need a message to streeeeeeeeetch.")
    else:
        count = random.randint(3, 10)
        reply_text = re.sub(
            r"([aeiouAEIOUａｅｉｏｕＡＥＩＯＵ])", (r"\1" * count), message.reply_to_message.text
        )
        if len(reply_text) >= MAX_MESSAGE_LENGTH:
            return message.reply_text(
                "Result of this message was too long for telegram!"
            )

        message.reply_to_message.reply_text(reply_text)


@run_async
@typing_action
def goodnight(update, context):
    message = update.effective_message
    first_name = update.effective_user.first_name
    reply = f"Good Night! {escape_markdown(first_name)}" 
    message.reply_text(reply, parse_mode=ParseMode.MARKDOWN)


@run_async
@typing_action
def goodmorning(update, context):
    message = update.effective_message
    first_name = update.effective_user.first_name
    reply = f"Good Morning! {escape_markdown(first_name)}"
    message.reply_text(reply, parse_mode=ParseMode.MARKDOWN)


__help__ = """
*Some dank memes for fun or whatever!*
 ✪ /sanitize*:* Sanitize Your Self
 ✪ /judge : Judges the user.
 ✪ /decide*:* Randomly answer yes no etc.
 ✪ /table*:* Flips a table...
 ✪ runs*:* Reply a random string from an array of replies.
 ✪ /slap*:* Slap a user, or get slapped if not a reply.
 ✪ /owo*:* UwU-fy whole text XD.	
 ✪ /stretch*:*  streeeeeeetch iiiiiiit.
 ✪ /hug*:* Hug a user warmly, or get hugged if not a reply.
 ✪ /pat*:* pats a user, or get patted
 ✪ /shout*:* write anything you want to give loud shoute
 
 ✪ /truth or /dare*:* Send random truth or dare.

*Regex based memes:*

✪ /decide can be also used with regex like: `sukuna? <question>: randomly answer "Yes, No" etc.`

Some other regex filters are:
`goodmorning`, `good morning` or `goodnight`, `good night`.

Sukuna will reply random strings accordingly when these words are used!
All regex filters can be disabled incase u don't want... like: `/disable goodnight`.

"""

__mod_name__ = "Memes"


JUDGE_HANDLER = DisableAbleCommandHandler("judge", judge)
PAT_HANDLER = DisableAbleCommandHandler("pat", pat)
SHOUT_HANDLER = DisableAbleCommandHandler("shout", shout)
DARE_HANDLER = DisableAbleCommandHandler("dare", dare)
TRUTH_HANDLER = DisableAbleCommandHandler("truth", truth)
SANITIZE_HANDLER = DisableAbleCommandHandler("sanitize", sanitize)
DECIDE_HANDLER = DisableAbleMessageHandler(
    Filters.regex(r"(?i)^Suzuya\?"), decide, friendly="decide"
)
RUNS_HANDLER = DisableAbleCommandHandler("runs", runs ,pass_args=True)
SLAP_HANDLER = DisableAbleCommandHandler("slap", slap)
HUG_HANDLER = DisableAbleCommandHandler("hug", hug)
GBUN_HANDLER = CommandHandler("gbun", gbun)
GBAM_HANDLER = CommandHandler("gbam", gbam)
GBOOM_HANDLER = CommandHandler("gboom", gboom)
TABLE_HANDLER = DisableAbleCommandHandler("table", table)
OWO_HANDLER = DisableAbleCommandHandler("owo", owo)
STRECH_HANDLER = DisableAbleCommandHandler("stretch", stretch)
GDMORNING_HANDLER = DisableAbleMessageHandler(
    Filters.regex(r"(?i)(goodmorning|good morning)"), goodmorning, friendly="goodmorning"
)
GDNIGHT_HANDLER = DisableAbleMessageHandler(
    Filters.regex(r"(?i)(goodnight|good night)"), goodnight, friendly="goodnight"
)



dispatcher.add_handler(GBOOM_HANDLER)
dispatcher.add_handler(JUDGE_HANDLER)
dispatcher.add_handler(PAT_HANDLER)
dispatcher.add_handler(SHOUT_HANDLER)
dispatcher.add_handler(DARE_HANDLER)
dispatcher.add_handler(TRUTH_HANDLER)
dispatcher.add_handler(DECIDE_HANDLER)
dispatcher.add_handler(RUNS_HANDLER)
dispatcher.add_handler(SLAP_HANDLER)
dispatcher.add_handler(GBAM_HANDLER)
dispatcher.add_handler(HUG_HANDLER)
dispatcher.add_handler(GBUN_HANDLER)
dispatcher.add_handler(TABLE_HANDLER)
dispatcher.add_handler(OWO_HANDLER)
dispatcher.add_handler(STRECH_HANDLER)
dispatcher.add_handler(GDMORNING_HANDLER)
dispatcher.add_handler(GDNIGHT_HANDLER)
