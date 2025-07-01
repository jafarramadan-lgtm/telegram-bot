import telebot
import sqlite3
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN ='7895273932:AAHifk7HF3LOdJsld3GVXKMo78HqhGHmCIY'
bot = telebot.TeleBot(TOKEN)










# لوحة الزر الرئيسي
main_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
main_keyboard.add(KeyboardButton("ثقافة"),KeyboardButton("رياضيات"),KeyboardButton("تحليل"),KeyboardButton("لغة"),KeyboardButton("مبادئ"),KeyboardButton("دارات"),KeyboardButton("برمجة"))


#########################################################################

m_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
m_keyboard.add(
    KeyboardButton("عملي برمجة"),
    KeyboardButton("نظري برمجة"),
    KeyboardButton("🔙 رجوع")
)
##########################################################################
n_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
n_keyboard.add(
    KeyboardButton("عملي مبادئ" ),
    KeyboardButton("نظري مبادئ"),
    KeyboardButton("🔙 رجوع")
)
##########################################################################
a_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
a_keyboard.add(
     KeyboardButton("1محاضرة رياضيات" ),
     KeyboardButton("2محاضرة رياضيات" ),
     KeyboardButton("3محاضرة رياضيات" ),
     KeyboardButton("4محاضرة رياضيات" ),
     KeyboardButton("5محاضرة رياضيات" ),
     KeyboardButton("6محاضرة رياضيات" ),
          KeyboardButton("7محاضرة رياضيات" ),
          KeyboardButton("8محاضرة رياضيات" ),

     KeyboardButton("🔙 رجوع")
)
#########################################################################
b_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
b_keyboard.add(
     KeyboardButton("1محاضرة تحليل"),
     KeyboardButton("2محاضرة تحليل"),
     KeyboardButton("3محاضرة تحليل"),
     KeyboardButton("4محاضرة تحليل"),
     KeyboardButton("5محاضرة تحليل"),
     KeyboardButton("6محاضرة تحليل"),
     KeyboardButton("7محاضرة تحليل"),
     KeyboardButton("🔙 رجوع")
)
#########################################################################
c_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
c_keyboard.add(
    KeyboardButton("1 محاضرة برمجةعملي"),
    KeyboardButton("2 محاضرة برمجةعملي"),
    KeyboardButton("3 محاضرة برمجةعملي"),
    KeyboardButton("4 محاضرة برمجةعملي"),
    KeyboardButton("5 محاضرة برمجةعملي"),
    KeyboardButton("6 محاضرة برمجةعملي"),
    KeyboardButton("7 محاضرة برمجةعملي"),
     KeyboardButton("🔙 رجوع")
)
#########################################################################
d_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
d_keyboard.add(
    KeyboardButton("1 محاضرة برمجة نظري"),
    KeyboardButton("2 محاضرة برمجة نظري"),
    KeyboardButton("3 محاضرة برمجة نظري"),
    KeyboardButton("4 محاضرة برمجة نظري"),
    KeyboardButton("5 محاضرة برمجة نظري"),
    KeyboardButton("6 محاضرة برمجة نظري"),
    KeyboardButton("7 محاضرة برمجة نظري"),
     KeyboardButton("🔙 رجوع")
)
#########################################################################
e_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
e_keyboard.add(

    KeyboardButton("1 محاضرة مبادئ نظري"),
    KeyboardButton("2 محاضرة مبادئ نظري"),
    KeyboardButton("3 محاضرة مبادئ نظري"),
    KeyboardButton("4 محاضرة مبادئ نظري"),
    KeyboardButton("5 محاضرة مبادئ نظري"),
    KeyboardButton("7+6 محاضرة مبادئ نظري"),
    KeyboardButton("8 محاضرة مبادئ نظري"),
    KeyboardButton("9 محاضرة مبادئ نظري"),
     KeyboardButton("10+11 محاضرة مبادئ نظري"),     
        KeyboardButton("12 محاضرة مبادئ نظري"),
    
     
     
     KeyboardButton("🔙 رجوع")
)
#########################################################################
f_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
f_keyboard.add(
    KeyboardButton("1 محاضرة مبادئ عملي"),
    KeyboardButton("2 محاضرة مبادئ عملي"),
    KeyboardButton("3 محاضرة مبادئ عملي"),
    KeyboardButton("4 محاضرة مبادئ عملي"),
    KeyboardButton("5 محاضرة مبادئ عملي"),
    KeyboardButton("6 محاضرة مبادئ عملي"),

     KeyboardButton("🔙 رجوع")
)
#########################################################################

g_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
g_keyboard.add(
    KeyboardButton("1 محاضرة دارات"),
    KeyboardButton("2 محاضرة دارات"),
    KeyboardButton("3 محاضرة دارات"),
    KeyboardButton("4 محاضرة دارات"),
    KeyboardButton("5 محاضرة دارات"),
    KeyboardButton("6 محاضرة دارات"),

     KeyboardButton("🔙 رجوع")
)
#########################################################################

x_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
x_keyboard.add(
    KeyboardButton(" المقرر ثقافة"),
    
    KeyboardButton("🔙 رجوع")
)
#############################################################################

x_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
x_keyboard.add(
    KeyboardButton(" المقرر لغة"),
    
    KeyboardButton("🔙 رجوع")
)
#############################################################################



@bot.message_handler(commands=['start'])
def send_welcome(message):
    
    user=message.from_user
    id_user=user.id
    name=user.username 
    f_name=user.full_name
####################################################33




    db=sqlite3.connect("informayion_user.db")
    cr=db.cursor()
    cr.execute("create table if not exists infor(id integer ,user_name text,full_name text)")
    cr.execute(f"insert into infor(id,user_name,full_name) values(?,?,?)",(id_user,name,f_name))
    cr.execute("select * from infor where (id,user_name,full_name)=(?,?,?)",(id_user,name,f_name))
    db.commit()
    db.close()
    bot.send_message(message.chat.id, "أهلاً وسهلا:", reply_markup=main_keyboard)

@bot.message_handler(func=lambda msg: msg.text == "برمجة")
def show_second_buttons(message):
    bot.send_message(message.chat.id, "اختر نوع المادة:", reply_markup=m_keyboard)

@bot.message_handler(func=lambda msg: msg.text == "نظري")
def show_second_buttons(message):
    bot.send_message(message.chat.id, "اختر المحاضرة:", reply_markup=d_keyboard)
@bot.message_handler(func=lambda msg: msg.text == "6 محاضرة برمجة نظري")
def send_file_by_id(message):
    bot.send_document(message.chat.id, "BQACAgQAAxkBAAIBTGhR0UlYGztEFBQ7j2fmGLV9MW7xAAKyFQACe8CJUk3n62wfsEqnNgQ")

@bot.message_handler(func=lambda msg: msg.text == "5 محاضرة برمجة نظري")
def send_file_by_id(message):
    bot.send_document(message.chat.id, "BQACAgQAAxkBAAIBamhR0t02ltUPuNJhGPaeVvt95Z42AAK0FQACe8CJUk9GqKbGWxPWNgQ")

@bot.message_handler(func=lambda msg: msg.text == "1 محاضرة برمجة نظري")
def send_file_by_id(message):
    bot.send_document(message.chat.id, "BQACAgQAAxkBAAIBhWhR2iNNB4OmERuDXMGDgpc3l6dxAALHFQACe8CJUilS2iqqA2DzNgQ")


@bot.message_handler(func=lambda msg: msg.text =="3 محاضرة برمجة نظري" )
def send_file_by_id(message):
    bot.send_document(message.chat.id, "BQACAgQAAxkBAAIBh2hR2n25iVHPLGWvvNs2br3MIGVRAALIFQACe8CJUmsNvgOFSwdCNgQ")
@bot.message_handler(func=lambda msg: msg.text =="4 محاضرة برمجة نظري" )
def send_file_by_id(message):
    bot.send_document(message.chat.id, "BQACAgQAAxkBAAIBiWhR2t0T255JF9zR2tuwe56-inekAALJFQACe8CJUk1zDURAx6qBNgQ")
@bot.message_handler(func=lambda msg: msg.text == "2 محاضرة برمجة نظري")
def send_file_by_id(message):
    bot.send_document(message.chat.id, "BQACAgQAAxkBAAIBi2hR20RaWL7zrh3edBd6WlP6UWIQAALLFQACe8CJUtHLFJfSQ1xdNgQ")

@bot.message_handler(func=lambda msg: msg.text == "7 محاضرة برمجة نظري")
def send_file_by_id(message):
    bot.send_document(message.chat.id, "BQACAgQAAxkBAAIGrGhkFBST7713FF35F_yW669TvLa2AAImFwACSHPJUnmUK-op2qFzNgQ")



@bot.message_handler(func=lambda msg: msg.text == "1محاضرة رياضيات")
def send_file_by_id(message):
    bot.send_document(message.chat.id, "BQACAgQAAxkBAAIBm2hR3EN-W0OpaC-3nNX9MlXjo2M4AALPFQACe8CJUoyB1AGB6n6PNgQ")
@bot.message_handler(func=lambda msg: msg.text == "2محاضرة رياضيات")
def send_file_by_id(message):
    bot.send_document(message.chat.id, "BQACAgQAAxkBAAIBnWhR3F4aHF0WGQgFq_FsLDCFNbmnAALQFQACe8CJUl4echab6k1ONgQ")
@bot.message_handler(func=lambda msg: msg.text == "3محاضرة رياضيات")
def send_file_by_id(message):
    bot.send_document(message.chat.id, "BQACAgQAAxkBAAIBn2hR3G_Wg6MpnvjXjU8E8y-NRRrmAALRFQACe8CJUh7THhHHMQ53NgQ")

@bot.message_handler(func=lambda msg: msg.text == "4محاضرة رياضيات")
def send_file_by_id(message):
    bot.send_document(message.chat.id, "BQACAgQAAxkBAAIBoWhR3IGu1hZFIhaNvFNUmmL2Y57oAALTFQACe8CJUjgyTY2n0NagNgQ")

@bot.message_handler(func=lambda msg: msg.text == "8محاضرة رياضيات")
def send_file_by_id(message):
    bot.send_document(message.chat.id, "BQACAgQAAxkBAAIFs2hj6xhT5xmuto-T2DVpagH4pJ6NAALfGQACpoHYUoCrE3FZAAHLnzYE")
    
    
@bot.message_handler(func=lambda msg: msg.text == "7محاضرة رياضيات")
def send_file_by_id(message):
    bot.send_document(message.chat.id, "BQACAgQAAxkBAAIFt2hj64rAsOT0Hkude2R1RYI91qd8AAKkGgADTKFSLRnv9Myd2vw2BA")
    
@bot.message_handler(func=lambda msg: msg.text == "5محاضرة رياضيات")
def send_file_by_id(message):
    bot.send_document(message.chat.id, "BQACAgQAAxkBAAIBo2hR3J2kvTOOveUR3hqBW2Bb11oAA9QVAAJ7wIlSWMcl1OKB3Ww2BA")

@bot.message_handler(func=lambda msg: msg.text == "6محاضرة رياضيات")
def send_file_by_id(message):
    bot.send_document(message.chat.id, "BQACAgQAAxkBAAIBpWhR3Lum9sV1gstXMBfsunsDJOf_AALVFQACe8CJUtSuIOEw15jPNgQ")


@bot.message_handler(func=lambda msg: msg.text == "ثقافة")
def send_file_by_id(message):
    bot.send_document(message.chat.id, "BQACAgQAAxkBAAIB5WhR3_G0-BKmyMRPQWytMptKqq_BAALWFQACe8CJUunG7ZTAw2gRNgQ")

@bot.message_handler(func=lambda msg: msg.text == "1محاضرة تحليل")
def send_file_by_id(message):
    bot.send_document(message.chat.id, "BQACAgQAAxkBAAIB6WhR4WEzLJpkEsRbBlrovCSMfSdXAAKAFgACe8CRUoZnUwn8Bp-1NgQ")
@bot.message_handler(func=lambda msg: msg.text == "2محاضرة تحليل")
def send_file_by_id(message):
    bot.send_document(message.chat.id, "BQACAgQAAxkBAAIB9WhR4qs0RwmrMYYbRTuePDy_r4lAAAKIFgACe8CRUrojy8oUzl6ZNgQ")
@bot.message_handler(func=lambda msg: msg.text == "3محاضرة تحليل")
def send_file_by_id(message):
    bot.send_document(message.chat.id, "BQACAgQAAxkBAAIB82hR4mjBHEnh_GSasAVEhhNZUnhKAAKHFgACe8CRUj4ZwEe5I90HNgQ")

@bot.message_handler(func=lambda msg: msg.text == "4محاضرة تحليل")
def send_file_by_id(message):
    bot.send_document(message.chat.id, "BQACAgQAAxkBAAIB62hR4X5_kuqPOrwjguQw0zSvikzNAAKCFgACe8CRUhkUC9ydFRLpNgQ")
@bot.message_handler(func=lambda msg: msg.text == "5محاضرة تحليل")
def send_file_by_id(message):
    bot.send_document(message.chat.id, "BQACAgQAAxkBAAIB72hR4eky2jxwP0Wzy4bluy2XvQw-AAKDFgACe8CRUo7Hr7y_JpOCNgQ")

@bot.message_handler(func=lambda msg: msg.text == "6محاضرة تحليل")
def send_file_by_id(message):
    bot.send_document(message.chat.id, "BQACAgQAAxkBAAIB8WhR4f3CWdOzRKAGTm6vI3ns3bWEAAKEFgACe8CRUhe83nbHCG3kNgQ")
@bot.message_handler(func=lambda msg: msg.text == "7محاضرة تحليل")
def send_file_by_id(message):
    bot.send_document(message.chat.id, "BQACAgQAAxkBAAIFzGhj7EJB4o1e7QaPll7gRXB9319xAALVFQACXXShUrJ-qnUfUXsTNgQ")


@bot.message_handler(func=lambda msg: msg.text == "1 محاضرة دارات")
def send_file_by_id(message):
    bot.send_document(message.chat.id, "BQACAgQAAxkBAAICLmhR5H3IW7uHtJuArzrKiTcela79AAIWGgAC9lbAUOvDPYz2BWrUNgQ")
@bot.message_handler(func=lambda msg: msg.text == "2 محاضرة دارات")
def send_file_by_id(message):
    bot.send_document(message.chat.id, "BQACAgQAAxkBAAICKGhR5AkJwWY35MFLEyzV1zx7bIgLAAKKFgACe8CRUmr6Ker6Lg57NgQ")
@bot.message_handler(func=lambda msg: msg.text == "3 محاضرة دارات")
def send_file_by_id(message):
    bot.send_document(message.chat.id, "BQACAgQAAxkBAAICLGhR5EVFVc3Om6hx4mKQpDVohAkfAAJnFAACjSeIUoNdWol18b7UNgQ")
@bot.message_handler(func=lambda msg: msg.text == "4 محاضرة دارات")
def send_file_by_id(message):
    bot.send_document(message.chat.id, "BQACAgQAAxkBAAICKmhR5CCs2AcWeuzM_yjrBqTLPJShAAJrFAACjSeIUm7-CMtccQVPNgQ")
@bot.message_handler(func=lambda msg: msg.text == "5 محاضرة دارات")
def send_file_by_id(message):
    bot.send_document(message.chat.id, "")
@bot.message_handler(func=lambda msg: msg.text =="6 محاضرة دارات")
def send_file_by_id(message):
    bot.send_document(message.chat.id, "")

############
@bot.message_handler(func=lambda msg: msg.text =="1 محاضرة برمجةعملي")
def send_file_by_id(message):
    bot.send_document(message.chat.id, "BQACAgQAAxkBAAICUWhR5quvk8LiUl80pPgrZPxLLcwyAAJnFwACFTOoUDp7fdsVRhGSNgQ")
@bot.message_handler(func=lambda msg: msg.text =="2 محاضرة برمجةعملي")
def send_file_by_id(message):
    bot.send_document(message.chat.id, "BQACAgQAAxkBAAICUmhR5qvQWypKzzzS66n-Suj6kVgxAAJoFwACFTOoUAyhQgadzmLZNgQ")
@bot.message_handler(func=lambda msg: msg.text =="3 محاضرة برمجةعملي")
def send_file_by_id(message):
    bot.send_document(message.chat.id, "BQACAgQAAxkBAAICT2hR5nlGuSJKeYh4dBGo30UxzbUAA2wfAAJT9-BQhxR15vOXzo02BA")
@bot.message_handler(func=lambda msg: msg.text =="4 محاضرة برمجةعملي")
def send_file_by_id(message):
    bot.send_document(message.chat.id, "BQACAgQAAxkBAAICTWhR5lnDckcra-JuUtcy0jlvnrVoAAJoKAADgChRC86QMlryg602BA")
@bot.message_handler(func=lambda msg: msg.text =="5 محاضرة برمجةعملي")
def send_file_by_id(message):
    bot.send_document(message.chat.id, "BQACAgQAAxkBAAICS2hR5jrQ3MuV0xWiyx6eJkqfCQ-KAAIJHAACusFwUQABGjksf9_grDYE")
@bot.message_handler(func=lambda msg: msg.text =="6 محاضرة برمجةعملي")
def send_file_by_id(message):
    bot.send_document(message.chat.id, "BQACAgQAAxkBAAICR2hR5d_NN6jLE6HO0-99ohtsThfFAAKuGgACbH8AAVLA7MGOwypXYDYE")
@bot.message_handler(func=lambda msg: msg.text =="7 محاضرة برمجةعملي")
def send_file_by_id(message):
    bot.send_document(message.chat.id, "BQACAgQAAxkBAAIF5Ghj7QoJlw-bA-k4vl_ZLbCLPRWcAAINGQAC3rDgUneuUQVMicnoNgQ")



@bot.message_handler(func=lambda msg: msg.text =="1 محاضرة مبادئ عملي")
def send_file_by_id(message):
    bot.send_document(message.chat.id, "BQACAgQAAxkBAAIGJGhj7nKhyv58mG3g9Jrof-tRD0KcAAKgHAACK3qYUIHkDIp4ing-NgQ")

@bot.message_handler(func=lambda msg: msg.text =="2 محاضرة مبادئ عملي")
def send_file_by_id(message):
    bot.send_document(message.chat.id, "BQACAgQAAxkBAAIGKGhj7szKsjy1bLo9AqbbUOv4aWBKAAKhHAACK3qYUPwGBsFsdX-eNgQ")
@bot.message_handler(func=lambda msg: msg.text =="3 محاضرة مبادئ عملي")
def send_file_by_id(message):
    bot.send_document(message.chat.id, "BQACAgQAAxkBAAIGLGhj7vWIiFd1EWKg_rSl0Z6CiT8pAAKkHAACK3qYUJUCl6Glv20FNgQ")
@bot.message_handler(func=lambda msg: msg.text =="4 محاضرة مبادئ عملي")
def send_file_by_id(message):
    bot.send_document(message.chat.id, "BQACAgQAAxkBAAICu2hR6dl5GzOGwMf4WuxdeDy45Ts3AAKrHAACK3qYUFJrqYB-f6rvNgQ")
@bot.message_handler(func=lambda msg: msg.text =="5 محاضرة مبادئ عملي")
def send_file_by_id(message):
    bot.send_document(message.chat.id, "BQACAgQAAxkBAAICt2hR6T3SVFBXklVcdz5j33zb-N6jAAKxHAACK3qYUPQrzcRKSc6_NgQ")
@bot.message_handler(func=lambda msg: msg.text =="6 محاضرة مبادئ عملي")
def send_file_by_id(message):
    bot.send_document(message.chat.id, "BQACAgQAAxkBAAICuWhR6aFcNDVLHiPLi9OaTCDRcg4SAAKyHAACK3qYUJRqY39aSvATNgQ")



@bot.message_handler(func=lambda msg: msg.text =="1 محاضرة مبادئ نظري")
def send_file_by_id(message):
    bot.send_document(message.chat.id,  "BQACAgQAAxkBAAIDIWhR7TyrPOPu1gABEeHTNURWk-Y_ggACCxkAAofw4VNMVoOolSA2XDYE")


@bot.message_handler(func=lambda msg: msg.text =="2 محاضرة مبادئ نظري")
def send_file_by_id(message):
    bot.send_document(message.chat.id,"BQACAgQAAxkBAAIDNGhR7ovHPURFkNEW3WdY01APgA_7AAJxGgACqK5BUN20sRwCMm28NgQ")



@bot.message_handler(func=lambda msg: msg.text =="3 محاضرة مبادئ نظري")
def send_file_by_id(message):
    bot.send_document(message.chat.id, "BQACAgQAAxkBAAIDNmhR7r1PnyOpjoA4GTrO54Jz3aEsAAKeGQAC_ViRUG7n0s9liekmNgQ")



@bot.message_handler(func=lambda msg: msg.text =="4 محاضرة مبادئ نظري")
def send_file_by_id(message):
    bot.send_document(message.chat.id, "BQACAgQAAxkBAAIDOWhR7vKx302uXpwd6dVbHf9OmUM4AAKmFwACWffBUEiyUcGTRg4GNgQ")




@bot.message_handler(func=lambda msg: msg.text =="5 محاضرة مبادئ نظري")
def send_file_by_id(message):
    bot.send_document(message.chat.id, "BQACAgQAAxkBAAIDPGhR7yk1hV-6S-aKlZECFMqYsf6CAAMWAAJbChlRwnLqF5COgYg2BA")



@bot.message_handler(func=lambda msg: msg.text =="7+6 محاضرة مبادئ نظري")
def send_file_by_id(message):
    bot.send_document(message.chat.id, "BQACAgQAAxkBAAIDPmhR71CGWE_94JXC7reKktBRSc9GAALfGAACHIMQUTRDRDkPxzivNgQ")
    
    
@bot.message_handler(func=lambda msg: msg.text =="8 محاضرة مبادئ نظري")
def send_file_by_id(message):
    bot.send_document(message.chat.id, "BQACAgQAAxkBAAIGV2hj79TiCKOJVGLMf_0j6cEeiRsCAAIXGgACcMlIUUdg-24DEn1QNgQ")
    
@bot.message_handler(func=lambda msg: msg.text =="9 محاضرة مبادئ نظري")
def send_file_by_id(message):
    bot.send_document(message.chat.id, "BQACAgQAAxkBAAIGgWhkEkePfAJjk3xJMxdDtLEL12l9AAKHFwACARlgUb7onYTx7ibLNgQ")

@bot.message_handler(func=lambda msg: msg.text =="10+11 محاضرة مبادئ نظري")
def send_file_by_id(message):
    bot.send_document(message.chat.id, "BQACAgQAAxkBAAIGhmhkEuyDAj_fOjWEGNZ0VN4qmWI6AAK2GwAC9TABUoCCJQr09BA2NgQ")


@bot.message_handler(func=lambda msg: msg.text =="12 محاضرة مبادئ نظري")
def send_file_by_id(message):
    bot.send_document(message.chat.id, "BQACAgQAAxkBAAIGiGhkEyTxK8VdlMXvrqUUQg2TrMVAAAKPIQACN0F5UtviKsIAAXDWAAE2BA")
#######################################################################################################
@bot.message_handler(func=lambda msg: msg.text == "رياضيات")
def show_second_buttons(message):
    bot.send_message(message.chat.id, "اختر:", reply_markup=a_keyboard)

@bot.message_handler(func=lambda msg: msg.text == "دارات")
def show_second_buttons(message):
    bot.send_message(message.chat.id, "اختر:", reply_markup=g_keyboard)


@bot.message_handler(func=lambda msg: msg.text =="تحليل" )
def show_second_buttons(message):
    bot.send_message(message.chat.id, "اختر:", reply_markup=b_keyboard)

@bot.message_handler(func=lambda msg: msg.text == "برمجة")
def show_second_buttons(message):
    bot.send_message(message.chat.id, "اختر نوع المادة:", reply_markup=m_keyboard)
@bot.message_handler(func=lambda msg: msg.text == "نظري برمجة")
def show_second_buttons(message):
    bot.send_message(message.chat.id, "اختر :", reply_markup=d_keyboard)

@bot.message_handler(func=lambda msg: msg.text =="عملي برمجة" )
def show_second_buttons(message):
    bot.send_message(message.chat.id, "اختر :", reply_markup=c_keyboard)



@bot.message_handler(func=lambda msg: msg.text == "مبادئ")
def show_second_buttons(message):
    bot.send_message(message.chat.id, "اختر نوع المادة:", reply_markup=n_keyboard)


@bot.message_handler(func=lambda msg: msg.text =="نظري مبادئ" )
def show_second_buttons(message):
    bot.send_message(message.chat.id, "اختر :", reply_markup=e_keyboard)

@bot.message_handler(func=lambda msg: msg.text =="عملي مبادئ")
def show_second_buttons(message):
    bot.send_message(message.chat.id, "اختر :", reply_markup=f_keyboard)

##########################################################################################################
@bot.message_handler(func=lambda msg: msg.text == "🔙 رجوع")
def go_back(message):
    bot.send_message(message.chat.id, "القائمة الرئيسية", reply_markup=main_keyboard)
###########################################################################################################

@bot.message_handler(content_types=['document'])
def get_file_id(message):





    file_id = message.document.file_id
    bot.send_message(message.chat.id, f"📎 File ID: {file_id}")
    print(f"[DEBUG] File ID: {file_id}")
 








bot.infinity_polling() 