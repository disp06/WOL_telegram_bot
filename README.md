# Wake-on-LAN Telegram Bot  

Telegram-bot for remotely waking up computers in a server's local network using Wake-on-LAN (WOL).  

---

## 📋 Requirements  
- Python 3.10+  
- Libraries: `python-telegram-bot` (v20.x), `wakeonlan`  

---

## 🚀 Installation  
1. Download release or clone the repository:
   ```bash
   git clone https://github.com/your-username/wol-telegram-bot.git
3. RUN
   ```bash  
   pip install -r requirements.txt
4. In the Telegram app. Create a bot via @BotFather and get bot token.

5. Send a simple random message to your bot.

6. Replace BOT_TOKEN to your actual token in URL below and visit:
   https://api.telegram.org/botBOT_TOKEN/getUpdates
   Find your chat_id: Look for the "id" field in the JSON response.
   
8. Open wol_bot.py in a text editor to replace BOT_TOKEN and your_chat_id with your actual token and actual your_chat_id

9. Run the bot:
   ```bash
   python wol_bot.py

10. Send the command to your bot:
"/wol AA:BB:CC:DD:EE:FF"
The MAC address must be specified for the computer you want to wake up from sleep.
