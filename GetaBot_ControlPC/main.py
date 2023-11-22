import discord
import os
import json
import pyautogui
import os
import psutil
import GPUtil
from discord.ext import commands
from datetime import *
from dhooks import Webhook, Embed, File

def isExist(path):
    if os.path.exists(path):
        return True
    else:
        return False
def json_loaddata(filename):
    with open(filename, 'r') as file:
        return json.load(file)
def json_writedata(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file)
def gettime():
    current_time = datetime.now().strftime("%H:%M:%S")
    return current_time
def getdate():
    current_date = date.today().strftime("%Y-%m-%d")
    return current_date
def gettimedate():
    current_timedate = str(getdate()) + ' ' + str(gettime())
    return current_timedate

data_chars = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3',
    '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
    'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
    'Y', 'Z'
]
chars = []

localpath = os.path.abspath(os.getcwd())
configspath = (localpath+"\configs.json").replace("\\",'/')
if isExist(configspath):
    loaddata = json_loaddata(configspath)
else:
    newdata = {
        "token": "",
        "prefix": ""
    }
    json_writedata(configspath,newdata)
os.system('cls')
print('''┌─────────────────────────────────────────────────────────────────────────────────┐
│  ▄████ ▓█████ ▄▄▄█████▓ ▄▄▄         ▄▄▄█████▓ ▒█████   ▒█████   ██▓      ██████ │
│ ██▒ ▀█▒▓█   ▀ ▓  ██▒ ▓▒▒████▄       ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    ▒██    ▒ │
│▒██░▄▄▄░▒███   ▒ ▓██░ ▒░▒██  ▀█▄     ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    ░ ▓██▄   │
│░▓█  ██▓▒▓█  ▄ ░ ▓██▓ ░ ░██▄▄▄▄██    ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░      ▒   ██▒│
│░▒▓███▀▒░▒████▒  ▒██▒ ░  ▓█   ▓██▒     ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒▒██████▒▒│
│ ░▒   ▒ ░░ ▒░ ░  ▒ ░░    ▒▒   ▓▒█░     ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░▒ ▒▓▒ ▒ ░│
│  ░   ░  ░ ░  ░    ░      ▒   ▒▒ ░       ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░░ ░▒  ░ ░│
│░ ░   ░    ░     ░        ░   ▒        ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   ░  ░  ░  │
│      ░    ░  ░               ░  ░                ░ ░      ░ ░      ░  ░      ░  │
└─────────────────────────────────────────────────────────────────────────────────┘ ''')
print("GetaBot - ControlPC by Geta (geta1005)\n")
token = loaddata['token'] or input("BOT TOKEN: ")
prefix = loaddata['prefix'] or input("PREFIX: ")
length = 0
status = ['online', 'GetaBot - ControlPC']
newdata = {
    "token": token,
    "prefix": prefix
}
json_writedata(configspath,newdata)
PROCNAME = "RobloxPlayerBeta.exe"

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=prefix,intents=intents)

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online,activity=discord.Game(status[1]))
    os.system('cls')
    print('''┌─────────────────────────────────────────────────────────────────────────────────┐
│  ▄████ ▓█████ ▄▄▄█████▓ ▄▄▄         ▄▄▄█████▓ ▒█████   ▒█████   ██▓      ██████ │
│ ██▒ ▀█▒▓█   ▀ ▓  ██▒ ▓▒▒████▄       ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    ▒██    ▒ │
│▒██░▄▄▄░▒███   ▒ ▓██░ ▒░▒██  ▀█▄     ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    ░ ▓██▄   │
│░▓█  ██▓▒▓█  ▄ ░ ▓██▓ ░ ░██▄▄▄▄██    ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░      ▒   ██▒│
│░▒▓███▀▒░▒████▒  ▒██▒ ░  ▓█   ▓██▒     ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒▒██████▒▒│
│ ░▒   ▒ ░░ ▒░ ░  ▒ ░░    ▒▒   ▓▒█░     ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░▒ ▒▓▒ ▒ ░│
│  ░   ░  ░ ░  ░    ░      ▒   ▒▒ ░       ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░░ ░▒  ░ ░│
│░ ░   ░    ░     ░        ░   ▒        ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   ░  ░  ░  │
│      ░    ░  ░               ░  ░                ░ ░      ░ ░      ░  ░      ░  │
└─────────────────────────────────────────────────────────────────────────────────┘ ''')
    print("GetaBot - ControlPC by Geta (geta1005)\n")
    print('----------------------------------------------------')
    print(str(gettimedate()) + ' | ' + 'Set status: ' + str(status[0]))
    print(str(gettimedate()) + ' | ' + 'Set game: ' + str(status[1]))
    print(str(gettimedate()) + ' | ' + 'Set prefix: ' + prefix)
    print(str(gettimedate()) + ' | ' + 'Logged as {0.user}'.format(bot))
    print(str(gettimedate()) + ' | ' + 'Bot is ready!')
    print('----------------------------------------------------')

@bot.event
async def on_message(message):
    content = message.content
    author = message.author
    channel = message.channel
    if author == bot.user:
        return
    def cmd(syntax):
        try:
            checkcontent = content.lower()
            if checkcontent.startswith(prefix+(syntax)):
                return True
            else:
                return False
        except:
            return False
    if cmd("help"):
        try:
            await message.reply(f'```Need help? Contact me through Discord: geta1005\nPREFIX: {prefix}\nCommands:\n{prefix}help\n{prefix}screenshot [ss]\n{prefix}shutdown [sd]\n{prefix}status [st]\n{prefix}exitroblox [er]```')
        except Exception as e:
            print("\nSomething went wrong!\nOUTPUT:"+str(e))
    elif cmd("screenshot") or cmd("ss"):
        imgpath = localpath+"\screenshot.png"
        try:
            try:
                pyautogui.screenshot(imgpath)
                print(f"Saved image at: {imgpath}")
            except Exception as e:
                print("\nFailed to take screenshot\nOUTPUT:"+str(e))
                await message.reply("Failed to take screenshot\nOUTPUT:"+str(e))
            await message.reply(file=discord.File(imgpath))
        except Exception as e:
            print("\nFailed to take screenshot\nOUTPUT:"+str(e))
            await message.reply("Failed to take screenshot\nOUTPUT:"+str(e))
    elif cmd("status") or cmd("st"):
        try:
            textstatus = ''
            gpus = GPUtil.getGPUs()
            cpu_usage = psutil.cpu_percent()
            memory = psutil.virtual_memory()
            textstatus = textstatus+(f"**CPU:** {cpu_usage}%\n")
            for gpu in gpus:
                textstatus = textstatus+(f"**GPU:** {round(gpu.memoryUtil*100,1)}%\n")
            textstatus = textstatus+(f"**Memory:** {round((memory.used/memory.total)*100,1)}% *[{round(memory.used/1024/1024)}/{round(memory.total/1024/1024)}MB]*")
            print(textstatus)
            await message.reply(textstatus)
        except Exception as e:
            print("\nFailed to get status\nOUTPUT:"+str(e))
            await message.reply("Failed to get status\nOUTPUT:"+str(e))
    elif cmd("shutdown") or cmd("sd"):
        try:
            timesd = message.split(' ')[1]
        except:
            timesd = ''
        try:
            if timesd != '':
                os.system(("shutdown /s /t "+timesd))
            else:
                os.system("shutdown /s /t 0")
            await message.reply("Successfully shutdown the computer")
        except Exception as e:
            print("\nFailed to shutdown\nOUTPUT:"+str(e))
            await message.reply("Failed to shutdown\nOUTPUT:"+str(e))
    elif cmd("exitroblox") or cmd('er'):
        try:
            totalproc = 0
            count = 0
            for proc in psutil.process_iter():
                totalproc += 1
                if proc.name() == PROCNAME:
                    proc.kill()
                    print("\nExited Roblox")
                    await message.reply("Exited Roblox")
                else:
                    count += 1
            if totalproc == count:
                print("\nRoblox was not found")
                await message.reply("Roblox was not found")
        except Exception as e:
            print("\nFailed to exit Roblox\nOUTPUT:"+str(e))
            await message.reply("Failed to exit Roblox\nOUTPUT:"+str(e))
bot.run(token)
