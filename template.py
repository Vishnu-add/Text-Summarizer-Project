import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

project_name = "textSummarizer"

list_of_files =[
    ".github/workflows/.gitkeep",   # (if we commit into github, it will take from this and deploy in the cloud)useful in CI/CD  deployment, we'll write ci/cd related yml file automatic file, which will help in Cicd deploy
    f"src/{project_name}/__init__.py",  # to insall the local package this constructor file is used
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",  # in this common file we'll write utility
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"   # all notebook experiments
    
]


for filepath in list_of_files:
    filepath = Path(filepath)
    # first creating folders then files
    filedir, filename = os.path.split(filepath)
    
    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):  # getsize - gives length of chars inside the file
        with open(filepath, 'w') as f:
            pass
            logging.info(f"Creating Empty file: {filepath}")
            
    else:
        logging.info(f"{filename} already exists.")