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
2. RUN
   ```bash  
   pip install -r requirements.txt

3. In the Telegram app. Create a bot via @BotFather and get bot token.

4. Send a simple random message to your bot.

5. replace BOT_TOKEN in URL below and visit, find your chat_id: Look for the "id" field in the JSON response in URL:
   https://api.telegram.org/botBOT_TOKEN/getUpdates

   Open wol_bot.py in a text editor to replace BOT_TOKEN and your_chat_id with your actual token and actual your_chat_id and run:
   ```bash
   python wol_bot.py

OR
   
6. Run the bot with arguments:
   ```bash
   python wol_bot.py --token "YOUR_TOKEN" --chat-ids "123456789"

7. Send the command to your bot:
"/wol AA:BB:CC:DD:EE:FF"
The MAC address must be specified for the computer you want to wake up from sleep.

🛠️NOTE: Remotely waking-up-computers MUST BE in a server local network use only!

⚡⚡⚡VERY IMPORTANT FOR USE: Remotely waking-up-computers MUST BE config for Wake-on-LAN, that allows a computer to be turned on or awakened from sleep mode by a network message!
