from db import DB
import sqlite3
import logging
import os
import re
from telegram import User, TelegramObject
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler, DictPersistence, BasePersistence, Dispatcher)
from dotenv import load_dotenv
load_dotenv()

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


START, NAME, COLLEGE, SIDEPROJECT, LANGUAGE, FRAMEWORK,CONFIDENT,GITHUB,CONFIRM= range(9)


SOCIAL = ['Facebook','Whatsapp', 'LinkedIn']
LANGUAGE = ['C', 'C++','c#', 'Java','Javascript','Python','HTML5','PHP','SQL','Ruby']

CONFIDENT = ['Very Confident',' Confident Enough','Still Learning']
CONFIRM=tuple(['Yes','No'])




def start(update, context):
    """Send a message when the command /start is issued."""
    user = update.message.from_user
    update.message.reply_text(
        f'''
	Hey! Enter your Name
        ''')
    return NAME

def name(update, context):
    context.user_data['Name'] = update.message.text
    user = update.message.from_user
    regex = r"^[a-z A-Z]+$"

    if(re.search(regex, context.user_data['Name'])):
        logger.info("Name: %s", update.message.text)
        update.message.reply_text(
            ''' Enter your college name''',
            reply_markup=ReplyKeyboardRemove())

    return COLLEGE

def college(update, context):

    context.user_data['College'] = update.message.text
    user = update.message.from_user
    regex = r"^[a-z A-Z]+$"

    if(re.search(regex, context.user_data['College'])):
        logger.info("College: %s", update.message.text)
        update.message.reply_text(
            'How do you get to know about sideproject',
            reply_markup=ReplyKeyboardMarkup([SOCIAL], one_time_keyboard=True))

    return SOCIAL

def social(update, context):
   
    context.user_data['Social'] = update.message.text
    user = update.message.from_user

    if(context.user_data['Social'] in SOCIAL):
        logger.info("Social: %s", update.message.text)

        update.message.reply_text(
            '''
		Which programming language do you know ?''',
            reply_markup=ReplyKeyboardMarkup([LANGUAGE], one_time_keyboard=True))
        return LANGUAGE


def language(update, context):
    context.user_data['Language'] = update.message.text
    user = update.message.from_user
    if(context.user_data['Language']in LANGUAGE):
        logger.info("Language: %s",update.message.text)
        update.message.reply_text(
            '''Do you know any framework ? Please list them''',
            reply_markup=ReplyKeyboardRemove())
    return FRAMEWORK


def framework(update, context):
    context.user_data['Framework'] = update.message.text
    user = update.message.from_user
    regex = r"^[a-z,-:A-Z 0-9]+$"

    if(re.search(regex, context.user_data['Framework'])):
        logger.info("Framework: %s", update.message.text)
        update.message.reply_text(
            'How confident are you about your programming skills',
            reply_markup=ReplyKeyboardMarkup([CONFIDENT], one_time_keyboard=True))

    return  CONFIDENT


    
def confident(update, context):
    context.user_data['Confident'] = update.message.text
    user = update.message.from_user
    if(context.user_data['Confident']in CONFIDENT):
        logger.info("Confident: %s",update.message.text)
        update.message.reply_text(
            '''Please share your github repository for us to keep a track of your work.''',
            reply_markup=ReplyKeyboardRemove())
    return GITHUB

def github(update, context):
    context.user_data['Github'] = update.message.text
    user = update.message.from_user
    regex = r"^[a-z,-:A-Z 0-9]+$"

    if(re.search(regex, context.user_data['Github'])):
        logger.info("Github: %s", update.message.text)
        update.message.reply_text(
            'Have you done any project before ? ',
            reply_markup=ReplyKeyboardMarkup([CONFIRM], one_time_keyboard=True))

    return CONFIRM 

def confirm(update, context):
    context.user_data['Confirm'] = update.message.text
    user = update.message.from_user
    if update.message.text == "Yes":
        logger.info("Confirmation of%s: %s",
                    user.first_name, update.message.text)
        update.message.reply_text(
            'Based on your skills and experience, we feel you should join the SideProjects Level 2', reply_markup=ReplyKeyboardRemove())
        return ConversationHandler.END
    else:
        logger.info("Confirmation of%s: %s",
                    user.first_name, update.message.text)
        update.message.reply_text(
            'Based on your skills and experience, we feel you should join the SideProjects Level 1', reply_markup=ReplyKeyboardRemove())
        return ConversationHandler.END
    #if(context.user_data['Confirm']in CONFIRM_OPTIONS):
        #logger.info("Confirm: %s",update.message.text)
        #update.message.reply_text(
            #'Based on your skills and experience, we feel you should join the SideProjects',
            #reply_markup=ReplyKeyboardREmove())
    #return ConversationHandler.END
    
'''def confident(update, context):
    context.user_data['Confident'] = update.message.text
    user = update.message.from_user
    if(context.user_data['Confident']in CONFIDENT):
        logger.info("Confident: %s",update.message.text)
        update.message.reply_text(
            33333333333333,
            reply_markup=ReplyKeyboardRemove())
    return NAME'''

    #return NAME
'''def reply(update,context):
    context.user_data['Reply']=update.message.text
    user=update.messsage.from_user
    regrex=r"^[a-z,-:A-Z 0-9]+$"
    #user = update.message.from_user
    #update.message.reply_text(
        #f'''
	#Hello!Please enter your Name
        #''')
'''if(re.search(regrex,context.user_data['Reply'])):
        logger.info("Reply: %s",update.message.text)
        update.message.reply_text(
            'Thankyou...According to your information your in Level 1',
            reply_markup=ReplyKeyboardRemove())
    return NAME'''




def main():
  
 # will Create the Updater and pass it our bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    updater = Updater(
        os.getenv("TELEGRAM_TOKEN", ""), use_context=True)


    dp = updater.dispatcher


    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={
            START: [MessageHandler(Filters.text, start)],

            COLLEGE: [MessageHandler(Filters.text, college)],

            NAME: [MessageHandler(Filters.text, name)],

            SOCIAL: [MessageHandler(Filters.text, social)],

            LANGUAGE: [MessageHandler(Filters.text, language)],

            FRAMEWORK: [MessageHandler(Filters.text, framework)],


            CONFIDENT: [MessageHandler(Filters.text, confident)],

             GITHUB: [MessageHandler(Filters.text, github)],

             CONFIRM: [MessageHandler(Filters.text, confirm)]

        },
        
        #fallbacks=[CommandHandler('confident', confident)],)
        fallbacks=[CommandHandler('confirm', confirm)], )

    dp.add_handler(conv_handler)


    updater.start_polling()

   
    updater.idle()
    

if __name__ == '__main__':
    main()

