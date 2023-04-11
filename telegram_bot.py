import asyncio, telegram ,db,data 

job_data = data.allinf
lastquery = db.lastresult

title = job_data[0]
link = job_data[1]
description = job_data[2]
budget = job_data[3]


async def main():   
    if (db.new_record):
        fullMessage = title + '\n' + link + '\n' +description +'\n' + budget
        bot = telegram.Bot("6006940271:AAFalBsk0FzQnfM6Z1mXlMF2p31xjzDnkW4")
        async with bot:
            await bot.send_message(text=fullMessage, chat_id='-900290781')
        print('job has been sent successfully')
    else : 
        print('there is no jobs available')


if __name__ == '__main__':
    asyncio.run(main())
