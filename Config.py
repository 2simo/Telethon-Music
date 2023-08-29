import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "1403456233"))
    API_HASH = os.environ.get("API_HASH", "8ce3522bd21cc937eee4c68813d501d5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", 6494033471:AAGSc_QwGnMnzw3HPWj0bPz98Rb1iRQRwgE)
    STRING_SESSION = os.environ.get("STRING_SESSION", 1BJWap1wBu7q3_dz_xCJba1gCzgrWcVfz9RsdjpaEZ728jXhbpS6z2wPRTOvxzmmpiC7-WxH9hRHZ6cvrXqvH7am_nGi5gKsPvNbfXBS3IoxHxSMYZVYFzT3bPWpBwbOVxZyvXE7RbT5DuE54HkmSXJvgGB4dRe3mW7SeEIpqG7Be-kaXFhddnDtONe0BP1LPEcx_-XF36gc87pIqfat6rlPav-nvqqYf5X7tAlWcu-bZGQF8RrDmgiwArj4bnNCwVQDPIecA3lYj1xKyfvqbnPRYZ1gZB-i2pS4dBGY0XWuh8jiVsMVxPbuuv1Fzww1e5OHJhTS0CeMr4fSfHP-Ewzhq4Q0NM7Q=)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Music_PANGWAN_BOT")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "76817c4b94c0660d48a563e4632a2f5e")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
