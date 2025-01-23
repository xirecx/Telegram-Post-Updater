import asyncio
from telethon import TelegramClient

api_id = 'your_api_id'  
api_hash = 'your_api_hash'  
phone_number = 'your_phone_number'

client = TelegramClient('chenge', api_id, api_hash)
async def update_all_posts(chat, new_description):
    async for message in client.iter_messages(chat):  
        if message.text: 
            try:
                await client.edit_message(chat, message.id, new_description)
                print(f"Message updated successfully {message.id}")
            except Exception as e:
                print(f"Error updating message {message.id}: {e}")

async def periodic_update(chat, new_description, interval):
    while True:
        print("I'm starting to update all posts...")
        await update_all_posts(chat, new_description)
        print(f"Completed. Next update in {interval} seconds.")
        await asyncio.sleep(interval)  

async def main():
    await client.start(phone_number)
    chat = '@username'  
    new_description = "Description"  
    interval = 15 

    await periodic_update(chat, new_description, interval)
with client:
    client.loop.run_until_complete(main())
