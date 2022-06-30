import os

class config:
    # Go to the Secrets tab, in "key" write TOKEN and in "value" write your  token, and then click add new secret
    global token; token = os.getenv("TOKEN")
    # If to run a server to keep it alive 24/7. (Use UptimeRobot to do so)
    global run_server; run_server = True
  
    global prefix; prefix = 'v.'
    global nitro_sniper; nitro_sniper = False
    
    # Go to the Secrets tab, in "key" write WEB_URL and in "value" write your  webhook url, and then click add new secret. To disable it, just simply write '' or anything that isnt your webhook url
    global nitro_sniper_url; nitro_sniper_url = os.getenv("WEB_URL")