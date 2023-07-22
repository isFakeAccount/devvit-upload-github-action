import json
import sys
from pathlib import Path

if __name__ == "__main__":
    refresh_token = sys.argv[1]
    devvit_token = {"token": refresh_token, "copyPaste": False}

    devvit_dir = Path.home() / ".devvit"
    devvit_dir.mkdir(exist_ok=True)
    token_file = Path(devvit_dir.absolute(), "token")
    token_file.write_text(json.dumps(devvit_token))
