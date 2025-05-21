# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "8087950004")

API_HASH = os.environ.get("API_HASH", "461969be0f5af13fc50a55f6e783d6c8")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7488436463:AAGIHMc2F79zr_lQcDXscxqN2IPtNhxjiM8") 

FORCE_SUB = os.environ.get("FORCE_SUB", "amit_movies") 

             # Don't Remove Credit @VJ_Botz
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @KingVJ01

DB_NAME = os.environ.get("DB_NAME", "卂爪丨ㄒ")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://mahataamit54:mahataamit143>@tgrenameclst.0nunqj5.mongodb.net/?retryWrites=true&w=majority&appName=tgrenameclst")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5606411877').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
