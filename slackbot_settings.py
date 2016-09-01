from pit import Pit

DEFAULT_REPLY = "Usage: @seminarbot MM/dd"
API_TOKEN = Pit.get('seminarbot', {'require': {'token': 'slack_token'}})['token']
PLUGINS = ['seminarbot.plugins']
