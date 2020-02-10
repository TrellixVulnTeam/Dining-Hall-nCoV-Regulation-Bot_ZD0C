from telegram import InlineKeyboardMarkup, InlineKeyboardButton

#  █████╗ ██╗      █████╗ ██████╗ ███╗   ███╗███████╗
# ██╔══██╗██║     ██╔══██╗██╔══██╗████╗ ████║██╔════╝
# ███████║██║     ███████║██████╔╝██╔████╔██║███████╗
# ██╔══██║██║     ██╔══██║██╔══██╗██║╚██╔╝██║╚════██║
# ██║  ██║███████╗██║  ██║██║  ██║██║ ╚═╝ ██║███████║
# ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝
#                                                                       
def alarmEatin(context):
    EATIN_MESSAGE = "EH HELLO! YOU HAVE BEEN EATING IN THE DINING HALL FOR 20 MINUTES ALREADY LEH. PLEASE LEAVE NOW."

    job = context.job
    button_list = [InlineKeyboardButton(text='Leave Dining hall', callback_data = 'EXIT')]
    menu = build_menu(button_list, n_cols = 1, header_buttons = None, footer_buttons = None)
    
    context.bot.send_message(job.context, text = EATIN_MESSAGE,
                            reply_markup = InlineKeyboardMarkup(menu))

def alarmTakeAway(context):
    TAKEAWAY_MESSAGE = "EH HELLO! YOU HAVE BEEN IN THE DINING HALL FOR 10 MINUTES. YOU NEED 10 MINUTES TO TAKEAWAY MEH? PLEASE LEAVE NOW."

    job = context.job
    button_list = [InlineKeyboardButton(text='Leave Dining Hall', callback_data = 'EXIT')]
    menu = build_menu(button_list, n_cols = 1, header_buttons = None, footer_buttons = None)

    context.bot.send_message(job.context, text = TAKEAWAY_MESSAGE,
                            reply_markup = InlineKeyboardMarkup(menu))

# A function to build menu of buttons for every occasion 
def build_menu(buttons, n_cols, header_buttons, footer_buttons):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, header_buttons)
    if footer_buttons:
        menu.append(footer_buttons)
    return menu

# ██╗   ██╗███╗   ██╗██╗   ██╗███████╗███████╗██████╗ 
# ██║   ██║████╗  ██║██║   ██║██╔════╝██╔════╝██╔══██╗
# ██║   ██║██╔██╗ ██║██║   ██║███████╗█████╗  ██║  ██║
# ██║   ██║██║╚██╗██║██║   ██║╚════██║██╔══╝  ██║  ██║
# ╚██████╔╝██║ ╚████║╚██████╔╝███████║███████╗██████╔╝
#  ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚══════╝╚═════╝ 
#                                                                            

def setEatinTimer(update, context):
    chat_id = update.message.chat_id
    new_job = context.job_queue.run_once(alarmEatin, 1200, context = chat_id)

def setTakeawayTimer(update, context):
    chat_id = update.message.chat_id
    new_job = context.job_queue.run_once(alarmTakeAway, 5, context = chat_id)