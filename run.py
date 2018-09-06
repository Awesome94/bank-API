from os import environ, write

from app import app

RED   = "\033[1;31m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD  = "\033[;1m"

if environ.get('ENV') == 'PROD': print(f'{BOLD}{RED}USING PROD{RESET}')
elif environ.get('ENV') == 'LOCAL': print(f'{GREEN}using local{RESET}')
elif environ.get('ENV') == 'TESTING': print(f'{GREEN}Using Testing{RESET}')
else: print(f'{CYAN}using staging{RESET}')

app.run(debug=True, threaded=True)
