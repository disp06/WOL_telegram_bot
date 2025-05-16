# Wake-on-LAN Telegram Bot  

Telegram bot for remotely waking up computers in a server's local network using Wake-on-LAN (WOL).  

---

## 📋 Requirements  
- Python 3.10+  
- Libraries: `python-telegram-bot` (v20.x), `wakeonlan`  

---

## 🚀 Installation  
1. Download release or clone the repository:
   ```bash
   git clone https://github.com/your-username/wol-telegram-bot.git
3. 
   ```bash  
   Run pip install -r requirements.txt

4. Config and save wol_bot.py with BOT_TOKEN and chat_id

3. Run the bot:
   ```bash
   python wol_bot.py

4. Send the command to your bot:
/wol AA:BB:CC:DD:EE:FF
MAC-adress must be config PC's MAC
