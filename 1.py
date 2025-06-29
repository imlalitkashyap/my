
import os
import zipfile
from datetime import datetime

# Create main project directory
project_name = "telegram-file-organizer-bot"
os.makedirs(project_name, exist_ok=True)
os.makedirs(f"{project_name}/templates", exist_ok=True)
os.makedirs(f"{project_name}/static/css", exist_ok=True)
os.makedirs(f"{project_name}/static/js", exist_ok=True)
os.makedirs(f"{project_name}/static/images", exist_ok=True)
os.makedirs(f"{project_name}/uploads", exist_ok=True)

print("Project structure created successfully!")
