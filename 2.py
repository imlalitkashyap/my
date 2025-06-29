
MAIN_BOT_CODE = '''import os
import logging
import re
from datetime import datetime
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler
from jinja2 import Environment, FileSystemLoader
import asyncio
from urllib.parse import urlparse
import mimetypes

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

class FileOrganizerBot:
    def __init__(self, token):
        self.token = token
        self.app = Application.builder().token(token).build()
        
        # Setup Jinja2 template environment
        self.template_env = Environment(loader=FileSystemLoader('templates'))
        
        # File categories
        self.categories = {
            'videos': {
                'extensions': ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm', '.m4v'],
                'keywords': ['video', 'lecture', 'tutorial', 'class', 'session'],
                'icon': '🎥'
            },
            'pdfs': {
                'extensions': ['.pdf'],
                'keywords': ['pdf', 'document', 'book', 'notes', 'material'],
                'icon': '📄'
            },
            'documents': {
                'extensions': ['.doc', '.docx', '.txt', '.rtf', '.odt'],
                'keywords': ['document', 'text', 'notes', 'assignment'],
                'icon': '📝'
            },
            'images': {
                'extensions': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp'],
                'keywords': ['image', 'photo', 'picture', 'screenshot'],
                'icon': '🖼️'
            },
            'audio': {
                'extensions': ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma'],
                'keywords': ['audio', 'music', 'sound', 'recording'],
                'icon': '🎵'
            },
            'archives': {
                'extensions': ['.zip', '.rar', '.7z', '.tar', '.gz'],
                'keywords': ['archive', 'compressed', 'zip', 'backup'],
                'icon': '📦'
            },
            'others': {
                'extensions': [],
                'keywords': [],
                'icon': '📁'
            }
        }
        
        self.setup_handlers()
    
    def setup_handlers(self):
        """Setup bot command and message handlers"""
        self.app.add_handler(CommandHandler("start", self.start_command))
        self.app.add_handler(CommandHandler("help", self.help_command))
        self.app.add_handler(CommandHandler("organize", self.organize_command))
        self.app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_text))
        self.app.add_handler(CallbackQueryHandler(self.handle_callback))
    
    async def start_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /start command"""
        welcome_message = """
🎯 **Professional File Organizer Bot**

मैं आपकी files को professional तरीके से organize करूंगा!

**Features:**
🎥 Videos - Lectures, tutorials
📄 PDFs - Documents, books  
📝 Documents - Notes, assignments
🖼️ Images - Photos, screenshots
🎵 Audio - Music, recordings
📦 Archives - Zip files, backups

**Commands:**
/start - Start the bot
/help - Show help
/organize - Organize your files

बस मुझे अपनी file list भेजें, मैं उन्हें beautifully organize कर दूंगा! 🚀
        """
        
        keyboard = [
            [InlineKeyboardButton("📚 Help", callback_data="help")],
            [InlineKeyboardButton("🎯 Start Organizing", callback_data="organize")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await update.message.reply_text(welcome_message, reply_markup=reply_markup, parse_mode='Markdown')
    
    async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /help command"""
        help_text = """
📚 **How to Use:**

1. **Send File List**: मुझे अपनी files की list भेजें
2. **Auto Organization**: मैं automatically categorize करूंगा
3. **Professional HTML**: Beautiful organized HTML file मिलेगा
4. **Interactive UI**: Click करके navigate करें

**Supported Formats:**
🎥 Videos: MP4, AVI, MKV, MOV
📄 PDFs: PDF documents
📝 Documents: DOC, DOCX, TXT
🖼️ Images: JPG, PNG, GIF
🎵 Audio: MP3, WAV, FLAC
📦 Archives: ZIP, RAR, 7Z

**Example Input:**
\`\`\`
Lecture 1 - Introduction.mp4
Notes Chapter 1.pdf
Assignment 1.docx
Tutorial Video.mp4
Reference Book.pdf
\`\`\`

बस text भेजें, बाकी मैं handle करूंगा! 🎯
        """
        await update.message.reply_text(help_text, parse_mode='Markdown')
    
    async def organize_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /organize command"""
        organize_text = """
🎯 **Ready to Organize!**

अब मुझे अपनी files की list भेजें:

**Format Example:**
\`\`\`
Video Lecture 1.mp4
Chapter 1 Notes.pdf
Assignment.docx
Tutorial Part 2.mp4
Reference Material.pdf
Images folder/screenshot.png
\`\`\`

मैं automatically detect करूंगा कि कौन सी file किस category में जाएगी और एक beautiful HTML page बनाऊंगा! 🚀
        """
        await update.message.reply_text(organize_text, parse_mode='Markdown')
    
    def categorize_file(self, filename):
        """Categorize file based on extension and keywords"""
        filename_lower = filename.lower()
        file_ext = os.path.splitext(filename_lower)[1]
        
        for category, config in self.categories.items():
            if category == 'others':
                continue
                
            # Check extension
            if file_ext in config['extensions']:
                return category
            
            # Check keywords
            for keyword in config['keywords']:
                if keyword in filename_lower:
                    return category
        
        return 'others'
    
    def parse_file_list(self, text):
        """Parse text and extract file information"""
        lines = text.strip().split('\\n')
        organized_files = {category: [] for category in self.categories.keys()}
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
            
            # Extract file info
            file_info = {
                'name': line,
                'size': 'Unknown',
                'path': line,
                'category': self.categorize_file(line)
            }
            
            # Try to extract size if mentioned
            size_match = re.search(r'\\((\\d+(?:\\.\\d+)?\\s*(?:KB|MB|GB))\\)', line)
            if size_match:
                file_info['size'] = size_match.group(1)
                file_info['name'] = line.replace(size_match.group(0), '').strip()
            
            organized_files[file_info['category']].append(file_info)
        
        return organized_files
    
    def generate_html(self, organized_files, user_name="User"):
        """Generate professional HTML from organized files"""
        template = self.template_env.get_template('file_organizer.html')
        
        # Calculate statistics
        total_files = sum(len(files) for files in organized_files.values())
        category_stats = {
            category: {
                'count': len(files),
                'icon': self.categories[category]['icon']
            }
            for category, files in organized_files.items()
            if len(files) > 0
        }
        
        html_content = template.render(
            organized_files=organized_files,
            categories=self.categories,
            total_files=total_files,
            category_stats=category_stats,
            user_name=user_name,
            generated_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
        
        return html_content
    
    async def handle_text(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle text messages containing file lists"""
        user_text = update.message.text
        user_name = update.effective_user.first_name or "User"
        
        # Show processing message
        processing_msg = await update.message.reply_text("🔄 Processing your files... Please wait!")
        
        try:
            # Parse and organize files
            organized_files = self.parse_file_list(user_text)
            
            # Generate HTML
            html_content = self.generate_html(organized_files, user_name)
            
            # Save HTML file
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"organized_files_{timestamp}.html"
            filepath = os.path.join("uploads", filename)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(html_content)
            
            # Update processing message
            await processing_msg.edit_text("✅ Files organized successfully!")
            
            # Send the HTML file
            with open(filepath, 'rb') as f:
                await update.message.reply_document(
                    document=f,
                    filename=filename,
                    caption=f"🎯 **Your Organized Files**\\n\\n"
                           f"📊 Total Files: {sum(len(files) for files in organized_files.values())}\\n"
                           f"📁 Categories: {len([cat for cat, files in organized_files.items() if len(files) > 0])}\\n"
                           f"⏰ Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\\n\\n"
                           f"Open this HTML file in your browser for the best experience! 🚀",
                    parse_mode='Markdown'
                )
            
            # Clean up
            os.remove(filepath)
            
        except Exception as e:
            logger.error(f"Error processing files: {e}")
            await processing_msg.edit_text("❌ Error processing files. Please try again!")
    
    async def handle_callback(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle inline keyboard callbacks"""
        query = update.callback_query
        await query.answer()
        
        if query.data == "help":
            await self.help_command(update, context)
        elif query.data == "organize":
            await self.organize_command(update, context)
    
    def run(self):
        """Start the bot"""
        logger.info("Starting File Organizer Bot...")
        self.app.run_polling()

if __name__ == "__main__":
    # Get bot token from environment variable
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    
    if not BOT_TOKEN:
        print("❌ Error: BOT_TOKEN environment variable not set!")
        print("Please set your Telegram bot token in the environment variables.")
        exit(1)
    
    # Create and run bot
    bot = FileOrganizerBot(BOT_TOKEN)
    bot.run()
'''

create_file(f"{project_name}/main.py", MAIN_BOT_CODE)
