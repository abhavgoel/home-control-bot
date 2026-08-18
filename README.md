# 🏠 Home Control Bot

A personal Telegram-powered home automation bot that lets you control your PC and smart lighting remotely.

Built with **Python + Raspberry Pi + Telegram + Wake-on-LAN + Philips WiZ**. You can also use a secondary laptop/device which can be the server. In my case its the Rasberry Pi.

> **One Telegram message → PC wakes up + room lights turn on.**

## ✨ Features

* 🖥️ **Wake your PC remotely** using Wake-on-LAN
* 💡 **Control Philips WiZ smart lights** over your local network
* 🤖 **Telegram bot interface**
* 🏠 Run continuously on a Raspberry Pi
* ⚡ Trigger multiple devices with a single command

## 🧠 How It Works

```text
                 Telegram
                    │
                    │ /home
                    ▼
            ┌─────────────────┐
            │  Telegram Bot   │
            │   Raspberry Pi  │
            └────────┬────────┘
                     │
              ┌──────┴──────┐
              │             │
              ▼             ▼
        Wake-on-LAN      Philips WiZ
              │             │
              ▼             ▼
          🖥️ PC         💡 Smart Light
```

The Raspberry Pi acts as the always-on controller.

When you send a command through Telegram, the bot processes it and sends the appropriate commands to your devices on the local network.

## 🛠️ Tech Stack

* **Python 3**
* **python-telegram-bot**
* **Wake-on-LAN**
* **pywizlight**
* **Raspberry Pi**
* **Philips WiZ**
* **Telegram Bot API**

## 📋 Commands

| Command   | Action                                    |
| --------- | ----------------------------------------- |
| `/wake_pc`      | Start the bot and show available commands |
| `/im_home`      | Wake the PC and turn on the room light    |


> Commands may change as the project evolves.

## 🤖 Create a Telegram Bot

Before running the project, you need to create your own Telegram bot and get its bot token.

1. Open Telegram and search for **[@BotFather](https://t.me/BotFather)**.
2. Send the `/newbot` command.
3. Enter a **name** for your bot, for example `Geol Home`.
4. Choose a unique **username** ending in `bot`, for example `geol_home_bot`.
5. BotFather will provide you with a **Bot Token**. It will look similar to:

```text
1234567890:AAExampleBotTokenxxxxxxxxxxxxxxxxxxx
```

6. Copy the token and add it to your `.env` file:

```env
TELEGRAM_BOT_TOKEN=your_bot_token_here
```

> ⚠️ **Keep your bot token private.** Anyone with access to it can control your Telegram bot. Never commit your `.env` file or expose the token publicly on GitHub.

You can then open your bot in Telegram and send `/start` to test it.


## 🚀 Setup

### 1. Clone the repository

```bash
git clone https://github.com/abhavgoel/home-control-bot.git
cd home-control-bot
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows:**

```powershell
venv\Scripts\activate
```

**Linux / Raspberry Pi:**

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create your `.env`

Create a file named `.env` in the project root:

```env
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
PC_MAC_ADDRESS=XX:XX:XX:XX:XX:XX
LIGHT_IP=192.168.1.100
```

### 5. Configure Wake-on-LAN

Enable **Wake-on-LAN** in your PC's BIOS/UEFI and network adapter settings.

The PC should preferably be connected through Ethernet.

Find your PC's MAC address with:

```powershell
ipconfig /all
```

Then add it to `.env`:

```env
PC_MAC_ADDRESS=XX:XX:XX:XX:XX:XX
```

### 6. Configure the WiZ light

Make sure your Philips WiZ bulb and Raspberry Pi are connected to the same local network.

Find the bulb's local IP address and add it to:

```env
LIGHT_IP=192.168.1.100
```

For reliable operation, consider assigning the bulb a DHCP reservation in your router so its IP doesn't change.

## ▶️ Run the Bot

```bash
python bot.py
```

The bot will start polling Telegram for new messages.

You can then send:

```text
/home
```

to activate your room.

## 🔐 Security

**Never commit your `.env` file.**

The repository uses `.gitignore` to prevent sensitive credentials from being uploaded.

Your `.env` should contain:

```env
TELEGRAM_BOT_TOKEN=...
PC_MAC_ADDRESS=...
LIGHT_IP=...
```

while `.env` should remain local.

If you're publishing your own version of this project, make sure you never expose your Telegram bot token.

## 🍓 Raspberry Pi

The intended deployment is a Raspberry Pi that stays powered on.

```text
Raspberry Pi
     │
     ├── Telegram Bot
     ├── Wake-on-LAN
     └── WiZ Controller
```

Because the bot runs on the Pi rather than your main PC, the PC can be completely powered off while the bot remains available.

For permanent deployment, the bot can be configured as a `systemd` service so it starts automatically whenever the Raspberry Pi boots.

## 🔮 Future Ideas

* [ ] PC online/offline status
* [ ] PC shutdown/restart commands
* [ ] Light brightness control
* [ ] Light scene selection
* [ ] Multiple smart lights
* [ ] Telegram inline buttons
* [ ] Automated `Good Morning` / `Good Night` modes
* [ ] More Raspberry Pi-based home automation
* [ ] Voice control
* [ ] Home Assistant integration

## 📄 License

This project is open source. Feel free to fork it, modify it, and build your own setup.

---

### Built by Abhav

Made as a personal home automation project using a Raspberry Pi, Telegram, Wake-on-LAN and Philips WiZ.
