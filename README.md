# 🛒 Facebook Marketplace Auto Poster Bot (Python + Pyppeteer)

## 🧠 Overview
The **Facebook Marketplace Auto Poster Bot** is a **powerful Python automation system** built to automatically list your products on **Facebook Marketplace** — including **images, titles, prices, and descriptions** — all in just a few clicks.

It automates every single step of the Marketplace posting process using **Pyppeteer** (a headless Chrome automation library). It interacts with Facebook the same way a human would: clicking, scrolling, typing, and uploading — making it appear completely natural.

This tool is built for:
- Entrepreneurs
- E-commerce sellers
- Dropshippers
- Social media marketers
- Developers testing Facebook automation  

The project was developed by **Ezee Kits** and works perfectly on **Windows**, **Linux**, and even **Android (Termux)**.

---

## ⚡ Features

- ✅ Full automation for **Facebook Marketplace listings**
- 🖼️ Auto upload multiple **product images**
- 🏷️ Auto fill **product name, price, and description**
- 💬 Automatically select **condition** (New, Used, etc.)
- 🧾 Reads data directly from a **CSV file**
- 👤 Uses your **existing Chrome profile** for persistent login (no repeated logins)
- 🔄 Scrolls and interacts like a real human user
- 🧠 Built-in retry and safety delays using `asyncio`
- 📱 Works across **Windows / Linux / Android (Termux)**
- 🧩 Modular design with clean, reusable helper functions

---

## 📂 Folder Structure
Facebook-Marketplace-Poster/
│
├── FB_MarketPlace.py # Main bot logic (posts product listings)
├── posting.py # Launch script for Chrome and the bot
├── func.py # Utility helper functions
├── products.csv # Product data file
└── README.md # Project documentation


---

## 🧩 How It Works

1. Launches Chrome using your saved **profile folder**  
2. Navigates to **Facebook Marketplace**
3. Clicks **Sell Something → Item for Sale**
4. Uploads multiple **product images**
5. Fills in the **product name, price, and condition**
6. Adds your **product description**
7. Selects **Marketplace audience** (checklists)
8. Clicks **Post** automatically 🎯

---

## 📄 Example CSV Format

Store all your product info in a CSV file (e.g., `products.csv`):

| NAME | PRODUCT_PRICE | PRODUCT_PIC_URLS |
|------|----------------|------------------|
| PS5 PRO | 500000 | ['C:\\Users\\HP\\Pictures\\ps5_1.jpg', 'C:\\Users\\HP\\Pictures\\ps5_2.jpg'] |
| iPhone 14 | 800000 | ['C:\\Users\\HP\\Pictures\\iphone1.png', 'C:\\Users\\HP\\Pictures\\iphone2.png'] |

Each row represents one item to be posted on Facebook Marketplace.  
The bot automatically picks data from each column and fills it into the corresponding field.

---

## 🧠 Step-by-Step Setup

### 🪟 Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/Facebook-Marketplace-Bot.git
cd Facebook-Marketplace-Bot

⚙️ Step 2: Install Dependencies

Make sure you have Python 3.9+ installed.
Then run:

pip install pyppeteer pandas bs4 lxml pyperclip asyncio

🌐 Step 3: Chrome Setup (Persistent Login)

You’ll need your existing Chrome profile folder to stay logged in automatically.

Example path (on Windows):

C:\Users\HP\AppData\Local\Google\Chrome\User Data\Profile 1


Paste this inside posting.py:

'userDataDir': r"C:\Users\HP\Desktop\ChromeProfileClone"


This ensures your bot runs as if you’re the real user — no login prompts.

🧩 Step 4: Edit the Target Link

In posting.py, replace the sample link with your Marketplace or Group URL:

await page.goto("https://web.facebook.com/marketplace", {"timeout": 0, "waitUntil": "networkidle2"})

▶️ Step 5: Run the Bot
python posting.py


The bot will open Chrome, go to Facebook, and start posting products automatically — filling all product details and images just like a human seller.

🧱 Code Architecture Breakdown
🔹 FB_MarketPlace.py

Handles the main automation logic:

Uploads product images

Fills title, price, and condition

Adds detailed description

Scrolls to the "Next" and "Marketplace" sections

Selects audience checkboxes

Clicks the final Post button

🔹 posting.py

Launches Chrome with your custom settings

Loads your profile and Facebook page

Starts the Marketplace bot (Facebook_MarketPlace_Bot)

🔹 func.py

A collection of helper functions:

css_click_center() → Click using CSS selector

xpath_click_center() → Click using XPath

click_checkboxes() → Select multiple checkboxes automatically

css_scroll_center() / xpath_scroll_center() → Smooth scrolling

create_dir(), drop_duplicate(), etc. → File utilities



🧩 Key Automation Actions Explained
| Step | Action                 | Description                             |
| ---- | ---------------------- | --------------------------------------- |
| 1️⃣  | Click "Sell Something" | Opens the Facebook selling menu         |
| 2️⃣  | Click "Item for Sale"  | Starts a new product listing            |
| 3️⃣  | Upload Photos          | Finds the file input and uploads images |
| 4️⃣  | Enter Title            | Fills the product name                  |
| 5️⃣  | Set Price              | Fills the product price                 |
| 6️⃣  | Select Condition       | Chooses "New", "Used", etc.             |
| 7️⃣  | Add Description        | Pastes text content from clipboard      |
| 8️⃣  | Click "Next"           | Moves to next posting stage             |
| 9️⃣  | Click "Marketplace"    | Selects Marketplace audience            |
| 🔟   | Click "Post"           | Submits the listing ✅                   |


📱 Android (Termux) Support
You can also run this bot on Android using Termux.

pkg update && pkg upgrade -y
pkg install python git chromium -y
pip install pyppeteer pandas bs4 lxml pyperclip
git clone https://github.com/yourusername/Facebook-Marketplace-Bot.git
cd Facebook-Marketplace-Bot
python posting.py


Use a Chromium-compatible data folder for persistent sessions.

💾 Logging and Debugging

Console logs track every action and step

Failed clicks or uploads are printed clearly

Extend with CSV logging using saving_files()

Example log snippet:

✅ Picked file input #1 (multiple upload enabled)
✅ Uploaded product images successfully
✅ Waited for and clicked on 'New'
✅ Clicked 'Marketplace' button successfully
✅ Product posted!

🚀 Expandable Features

Auto-post multiple products from CSV (loop)

Schedule posting intervals (daily/hourly)

Add support for Groups and Pages

Dynamic pricing adjustments

AI-based description generation

🧠 Real-Life Example

Let’s say you run a small gadget store and need to upload 20 products daily.
Instead of spending hours manually adding each one:

You prepare your product CSV

Run python posting.py

The bot uploads all items, one after another
This saves time, prevents repetition, and makes scaling effortless.

🎥 Video Tutorial

You can find the complete video guide on:
👉 Ezee Kits YouTube Channel

Learn how to configure, run, and expand this bot for your business automation projects.

👨‍💻 Author

Ezee Kits (Peter)
🎓 Electrical & Electronics Engineer | 🇳🇬 Nigeria
💡 Automation Developer | AI & Python Enthusiast
📧 Email: ezeekits@gmail.com

📺 YouTube: Ezee Kits

📜 License

MIT License

This project is open-source and free for educational and business automation purposes.
You can use, modify, and distribute it — but please give credit to the author.



Automate Facebook Marketplace posting using Python and Pyppeteer. Upload product images, set prices, add descriptions, and post listings automatically. Works on Windows, Linux, and Android.
