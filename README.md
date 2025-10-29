# 🤖 OLXparser

A Python Telegram bot that scrapes listings from **OLX** by user query and sends the results directly as a document.  
Designed for fast, simple automation and clean code structure.

---

## 🚀 Features

- 🔍 Search for listings on OLX directly through Telegram  
- ⚙️ Uses **Selenium** and **BeautifulSoup4** to collect item data  
- 📄 Exports results (name, price, description, link) to a text file  
- 💬 Sends the report file to the user via Telegram automatically  
- 🧵 Runs scraping in a separate thread to avoid freezing the bot  
- 🧱 Lightweight, easy to modify or extend  

---

## 🛠 Tech Stack

| Component | Technology |
|:-----------|:------------|
| **Language** | Python |
| **Libraries** | Selenium, BeautifulSoup4, Telebot (pyTelegramBotAPI), threading |
| **Automation** | Chrome WebDriver |
| **Platform** | Local / server deployment ready |

---

## 📂 Project Structure

```
OLXparser/
│
├── bot.py               # Telegram bot logic and scraping process
├── logi.txt             # Output file containing collected listings
├── requirements.txt     # Dependencies list
└── README.md            # Project documentation
```

---

## ⚙️ Installation & Run

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Oleg-git-cketch/OLXparser.git
cd OLXparser
```

### 2️⃣ Create and activate a virtual environment
```bash
python -m venv venv
venv\Scripts\activate      # Windows
# or
source venv/bin/activate   # Linux / macOS
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Set up your bot token
Open the script and replace:
```python
bot = telebot.TeleBot('YOUR BOT TOKEN')
```
with your actual **Telegram Bot Token**.

### 5️⃣ Make sure ChromeDriver is installed
You can download it from:
👉 https://chromedriver.chromium.org/downloads  
Make sure it matches your Chrome version.

### 6️⃣ Run the bot
```bash
python bot.py
```

---

## 💡 Usage

1. Open your bot in Telegram.  
2. Type the command `/analiz`.  
3. Enter the product name (for example, *iPhone 13*).  
4. Wait while the bot scrapes OLX.  
5. Receive a `.txt` file with all collected listings, including names, prices, descriptions, and links.

---

## 🧠 Author

**Oleg** — Python Developer  
💼 Project created for my **portfolio**, demonstrating skills in automation, scraping, and Telegram bot integration.

📬 *Available on Upwork / Freelancer for projects involving Python, bots, automation, and data parsing.*

---

## 🏷️ License

This project is intended for **educational and portfolio** use.  
You are free to clone, modify, and experiment with it for learning or demonstration purposes.

---
