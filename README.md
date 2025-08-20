# Currency Converter Telegram Bot (USD ↔ UZS)

A simple Telegram bot that converts Uzbek so'm and US dollar using a live exchange rate.

## Features
- Main menu with two buttons: 
  - "So'm → Dollar"
  - "Dollar → So'm"
- Always-available "Back" button to return to the main menu
- Live USD/UZS rate from open.er-api.com
- Secure token handling with `.env` (never checked into git)

## Quick Start

1. **Create and activate a virtual environment (recommended):**
   ```bash
   python -m venv .venv
   # Windows:
   .venv\Scripts\activate
   # macOS/Linux:
   source .venv/bin/activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure your token:**
   - Copy `.env.example` to `.env`
   - Put your real BotFather token in `BOT_TOKEN=`

4. **Run the bot:**
   ```bash
   python -m app.main
   ```

## Prevent Token Leaks (GitHub-safe)
- `.gitignore` excludes `.env` by default
- Never hardcode your token in the source code
- If you accidentally commit a token, **revoke it** in @BotFather immediately

## Python Version
Tested on Python 3.10 with `python-telegram-bot==13.15`.
