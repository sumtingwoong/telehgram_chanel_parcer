from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
import asyncio

api_id = your_api_id
api_hash = 'your_ip_hash'
phone = '+1xxxx' # ypur phone number

client = TelegramClient('new_session', api_id, api_hash)

async def main():
    await client.connect()

    if not await client.is_user_authorized():
        print('Code is sent')
        await client.send_code_request(phone)
        code = input('Please enter ypur code from Telegram ')
        try:
            print('Signing in')
            await client.sign_in(phone, code)
        except SessionPasswordNeededError:
            print('2FA is required')
            password = input('Please enter your password ')
            await client.sign_in(password=password)

    print('Authorization is complete')

    channel = await client.get_entity('channel_id')
    print('Chanel is found', channel.title)

    print('\nLast 5 messages:\n')
    async for message in client.iter_messages(channel, limit=5):
        print('📅', message.date)
        print('📝', message.text[:300] if message.text else '[Without text]')
        print('🔗', f'https://t.me/channel_id/{message.id}')
        print('---')


asyncio.run(main())
