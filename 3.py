
CONFIG_CODE = '''import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    """Configuration class for the bot"""
    
    # Bot Configuration
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    
    # File Configuration
    MAX_FILE_SIZE = 50 * 1024 * 1024  # 50MB
    ALLOWED_EXTENSIONS = {
        'videos': ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm', '.m4v'],
        'pdfs': ['.pdf'],
        'documents': ['.doc', '.docx', '.txt', '.rtf', '.odt'],
        'images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp'],
        'audio': ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma'],
        'archives': ['.zip', '.rar', '.7z', '.tar', '.gz']
    }
    
    # Directory Configuration
    UPLOAD_FOLDER = 'uploads'
    TEMPLATE_FOLDER = 'templates'
    STATIC_FOLDER = 'static'
    
    # Bot Settings
    WEBHOOK_URL = os.getenv("WEBHOOK_URL")
    PORT = int(os.getenv("PORT", 8000))
    
    # Feature Flags
    ENABLE_SEARCH = True
    ENABLE_DOWNLOAD = True
    ENABLE_SHARING = True
    
    @classmethod
    def validate_config(cls):
        """Validate required configuration"""
        if not cls.BOT_TOKEN:
            raise ValueError("BOT_TOKEN is required!")
        
        # Create directories if they don't exist
        os.makedirs(cls.UPLOAD_FOLDER, exist_ok=True)
        os.makedirs(cls.TEMPLATE_FOLDER, exist_ok=True)
        os.makedirs(cls.STATIC_FOLDER, exist_ok=True)
        
        return True

# Development Configuration
class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = False

# Production Configuration  
class ProductionConfig(Config):
    DEBUG = False
    TESTING = False

# Configuration mapping
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
'''

create_file(f"{project_name}/config.py", CONFIG_CODE)

