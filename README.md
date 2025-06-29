
README_CONTENT = '''# 🤖 Professional File Organizer Telegram Bot

एक professional Telegram bot जो आपकी files को beautifully organize करता है और interactive HTML pages बनाता है!

## ✨ Features

- 🎥 **Video Files** - Lectures, tutorials को organize करें
- 📄 **PDF Documents** - Books, notes को categorize करें  
- 📝 **Documents** - Text files, assignments को manage करें
- 🖼️ **Images** - Photos, screenshots को arrange करें
- 🎵 **Audio Files** - Music, recordings को sort करें
- 📦 **Archives** - Zip files, backups को organize करें
- 🔍 **Smart Search** - Files को easily find करें
- 📱 **Responsive Design** - Mobile और desktop friendly
- 🎨 **Professional UI** - Modern और clean interface

## 🚀 Quick Start

### 1. Telegram Bot बनाएं

1. Telegram पर [@BotFather](https://t.me/botfather) को message करें
2. \`/newbot\` command भेजें
3. Bot का name और username set करें
4. Bot token को save करें

### 2. Local Setup

\`\`\`bash
# Repository clone करें
git clone <your-repo-url>
cd telegram-file-organizer-bot

# Dependencies install करें
pip install -r requirements.txt

# Environment variables set करें
cp .env.example .env
# .env file में अपना BOT_TOKEN add करें

# Bot run करें
python main.py
\`\`\`

### 3. Render पर Deploy करें

#### Step 1: GitHub Repository बनाएं
\`\`\`bash
git init
git add .
git commit -m "Initial commit"
git remote add origin <your-github-repo-url>
git push -u origin main
\`\`\`

#### Step 2: Render पर Deploy करें
1. [Render.com](https://render.com) पर account बनाएं
2. "New Web Service" click करें
3. अपनी GitHub repository connect करें
4. Settings configure करें:
   - **Name**: \`your-bot-name\`
   - **Environment**: \`Python 3\`
   - **Build Command**: \`pip install -r requirements.txt\`
   - **Start Command**: \`python main.py\`

#### Step 3: Environment Variables Add करें
Render dashboard में Environment Variables section में:
\`\`\`
BOT_TOKEN = your_telegram_bot_token
PORT = 8000
ENVIRONMENT = production
\`\`\`

## 📱 Bot Usage

### Commands:
- \`/start\` - Bot को start करें
- \`/help\` - Help information देखें
- \`/organize\` - Files organize करने के लिए

### File List भेजने का तरीका:
\`\`\`
Video Lecture 1.mp4
Chapter 1 Notes.pdf
Assignment 1.docx
Tutorial Part 2.mp4
Reference Book.pdf
Screenshot.png
Music File.mp3
\`\`\`

Bot automatically detect करेगा कि कौन सी file किस category में जाएगी!

## 🎯 Example Output

Bot एक beautiful HTML file generate करेगा जिसमें:

- **Professional Header** with user info
- **Statistics Dashboard** with file counts
- **Search Functionality** for easy navigation
- **Category-wise Organization**:
  - 🎥 Videos section with play buttons
  - 📄 PDFs section with view buttons
  - 📝 Documents with download options
  - 🖼️ Images with preview options
- **Interactive Navigation** between categories
- **Responsive Design** for all devices

## 🛠️ Project Structure

\`\`\`
telegram-file-organizer-bot/
├── main.py                 # Main bot logic
├── config.py              # Configuration settings
├── requirements.txt       # Python dependencies
├── Procfile              # Render deployment config
├── .env.example          # Environment variables template
├── README.md             # Documentation
├── templates/
│   └── file_organizer.html # HTML template
├── static/
│   ├── css/              # Stylesheets
│   ├── js/               # JavaScript files
│   └── images/           # Static images
└── uploads/              # Temporary file storage
\`\`\`

## 🔧 Configuration

### Environment Variables:
- \`BOT_TOKEN\` - Your Telegram bot token (required)
- \`PORT\` - Server port (default: 8000)
- \`ENVIRONMENT\` - production/development
- \`WEBHOOK_URL\` - Your Render app URL (for webhooks)

### Customization:
आप \`config.py\` में file categories और settings को modify कर सकते हैं।

## 📋 Supported File Types

| Category | Extensions | Keywords |
|----------|------------|----------|
| Videos | .mp4, .avi, .mkv, .mov | video, lecture, tutorial |
| PDFs | .pdf | pdf, document, book, notes |
| Documents | .doc, .docx, .txt | document, text, assignment |
| Images | .jpg, .png, .gif | image, photo, screenshot |
| Audio | .mp3, .wav, .flac | audio, music, recording |
| Archives | .zip, .rar, .7z | archive, compressed, backup |

## 🎨 Features Showcase

### Professional UI:
- Modern gradient backgrounds
- Smooth animations और transitions
- Card-based layout with hover effects
- Mobile-responsive design
- Professional typography

### Interactive Elements:
- Category filtering buttons
- Real-time search functionality
- Collapsible file sections
- Action buttons (Play, View, Download)
- Print और download options

### Smart Organization:
- Automatic file categorization
- Extension-based detection
- Keyword-based classification
- File size display
- Path information

## 🚀 Deployment Tips

### Render Deployment:
1. Repository को public रखें
2. Environment variables properly set करें
3. Build logs check करें for errors
4. Health check endpoint add करें (optional)

### Bot Testing:
1. Local environment में पहले test करें
2. Sample file lists के साथ try करें
3. Different file types test करें
4. Mobile responsiveness check करें

## 🔍 Troubleshooting

### Common Issues:

**Bot not responding:**
- BOT_TOKEN check करें
- Internet connection verify करें
- Render logs check करें

**HTML not generating:**
- Template file path check करें
- Jinja2 syntax verify करें
- File permissions check करें

**Deployment failing:**
- requirements.txt में all dependencies हैं
- Python version compatibility check करें
- Build logs में errors देखें

## 📞 Support

Issues या questions के लिए:
1. GitHub issues create करें
2. Documentation carefully पढ़ें
3. Error logs share करें

## 🎉 Contributing

Contributions welcome हैं! Please:
1. Fork the repository
2. Create feature branch
3. Make changes
4. Submit pull request

## 📄 License

This project is open source और free to use है।

---

**Happy Organizing! 🎯**

Made with ❤️ for better file management
'''

create_file(f"{project_name}/README.md", README_CONTENT)

