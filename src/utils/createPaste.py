from src import config
import os
from ..modules import pastebin

def createPaste(name, content, format, expire_date='N'):
  key = pastebin.api_user_key(os.getenv("pasteToken"), os.getenv("pasteUsername"), os.getenv("pastePassword"))
  link = pastebin.paste(os.getenv("pasteToken"), code=content, user_key=key, name=name, format=format, private='private', expire_date='N')

  return link