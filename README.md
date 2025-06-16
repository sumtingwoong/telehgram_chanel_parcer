# Parcer for Telegram Channels

## Installation
Install dependencies
```
pip install telethon
```

## API
Get your ```api_id``` and ```api_hash from``` https://core.telegram.org/api#getting-started
1. Log in with your Telegram account
2. Go to API Development Tools
3. Create a new application and get your ```api_id``` and ```api_hash```

## Edit script

```
api_id = your_api_id
api_hash = 'your_api_hash_here'
phone = 'ypur_phone_number' # with international code (f.e.: +1xxxxxx)
```

## Usage
Run the script

The script will:
1. Connect to Telegram
2. Ask for login code (only on first run)
3. If 2FA is enabled, it will also ask for your password
4. Fetch and display the last 5 messages from the specified channel

## Changing the channel
```
channel = await client.get_entity('channel_id')
```

## TODO
- [ ] Save mesages to a file
- [ ] Support multiple channels
- [ ] Donwload media and extract links
