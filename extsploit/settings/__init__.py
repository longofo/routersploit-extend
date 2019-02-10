import os

# extsploit dir
EXT_DIR = os.path.dirname(os.path.dirname(__file__))

# routersploit root dir
PROJECT_DIR = os.path.dirname(os.path.dirname(EXT_DIR))

# exploit common config path
CONF_PATH = os.path.join(EXT_DIR, 'exploit/config/config.conf')
CONF_PATH = CONF_PATH.replace('/', os.sep)

# routersploit extend search engine dir
ENGINE_DIR = os.path.join(EXT_DIR, 'exploit/search')

# routersploit extent save module dir
SAVE_DIR = os.path.join(EXT_DIR, 'exploit/save')

# routersploit extent Output
OUTPUT_DIR = os.path.join(PROJECT_DIR, 'output')
if not os.path.exists(OUTPUT_DIR):
    os.mkdir(OUTPUT_DIR)

# Exploit execute command
EXPLOIT_COMMAND = ['run', 'check']
