import pyautogui
import time
import os
import psutil
import sys
import json
from tkinter import *
from multiprocessing import Process
from win10toast import ToastNotifier
from dhooks import Webhook

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
def sendwebhook(webhookurl,content):
    Webhook(webhookurl).send(str(content))

localpath = os.path.abspath(os.getcwd())
PROCNAME = "RobloxPlayerBeta.exe"
configspath = (localpath+'\settings.json').replace("\\","/")
icon = (localpath+'\icon.ico').replace("\\","/")
pathrobloxfolder = (os.getenv('LOCALAPPDATA')).replace('\\','/')+"/Roblox"+'/Versions'
toast = ToastNotifier()
try:
    for i in os.listdir(pathrobloxfolder):
        if isExist(pathrobloxfolder+'/'+str(i)+'/'+PROCNAME):
            pathrobloxfolder = pathrobloxfolder+'/'+str(i)+'/'+PROCNAME
except Exception as e:
    toast.show_toast(
        "Notification",
        "Oops! Something went wrong.\nOUTPUT: "+e,
        duration = 3,
        icon_path = icon,
        threaded = True,
    )
    sys.exit(0)
try:
    if not isExist(configspath):
        newdata = {
            "action": "Do Nothing",
            "webhook": {
                "enabled": False,
                "mention": False,
                "url": "",
                "tag": "",
            }
        }
        json_writedata(configspath,newdata)
except Exception as e:
    toast.show_toast(
        "Notification",
        "Oops! Something went wrong.\nOUTPUT: "+e,
        duration = 3,
        icon_path = icon,
        threaded = True,
    )
    sys.exit(0)


root = Tk()
root.title("Geta's Tool")
root.geometry("400x340")
root.iconbitmap(icon)

label_1 = Label(root, text="Need help? Contact me through Discord: geta1005")
label_1.pack()
label_2 = Label(root, text="Select action after disconnection")
label_2.pack()

dropdownselect = StringVar()
loaddata = json_loaddata(configspath)
dropdownselect.set(loaddata['action'])

options = [ 
    "Close Roblox",
    "Shutdown",
    "Do Nothing"
] 

dropdown = OptionMenu(root, dropdownselect, *options)
dropdown.pack()

# Tạo textbox
label_3 = Label(root, text="WEBHOOK URL:")
label_3.pack()
textbox = Text(root, height=3, width=48)
textbox.tag_configure("center", justify='center')
textbox.tag_add("center", "1.0", "end")
textbox.pack()

toggle_webhook = BooleanVar()
checkbutton_webhook = Checkbutton(root, text="Send WEBHOOK", variable=toggle_webhook)
checkbutton_webhook.pack()
toggle_mention = BooleanVar()
checkbutton_mention = Checkbutton(root, text="Mention", variable=toggle_mention)
checkbutton_mention.pack()

if loaddata['webhook']['enabled']:
    toggle_webhook.set(True)
if loaddata['webhook']['mention']:
    toggle_mention.set(True)

label_4 = Label(root, text="DISCORD TAG: [ YOUR-ID | everyone | here ]")
label_4.pack()
textbox2 = Text(root, height=1, width=25)
textbox2.tag_configure("center", justify='center')
textbox2.tag_add("center", "1.0", "end")
textbox2.pack()

textbox.delete("1.0", 'end')
textbox.insert('end', loaddata['webhook']['url'])
textbox2.delete("1.0", 'end')
textbox2.insert('end', loaddata['webhook']['tag'])

label_0 = Label(root, text="Always remember to update DATA.")
label_0.pack()

button_updatedata = Button(root, text="Update DATA")
button_updatedata.pack()
button_check_webhook = Button(root, text="Check webhook")
button_check_webhook.pack()
button_confirm = Button(root, text="---- [ CONFIRM ] ----")
button_confirm.pack()

def on_toggle_webhook():
    loaddata = json_loaddata(configspath)
    if toggle_webhook.get():
        loaddata['webhook']['enabled'] = True
    else:
        loaddata['webhook']['enabled'] = False
    json_writedata(configspath,loaddata)

def on_toggle_mention():
    loaddata = json_loaddata(configspath)
    if toggle_mention.get():
        loaddata['webhook']['mention'] = True
    else:
        loaddata['webhook']['mention'] = False
    json_writedata(configspath,loaddata)

checkbutton_webhook.config(command=on_toggle_webhook)
checkbutton_mention.config(command=on_toggle_mention)

def on_button_confirm():
    root.destroy()
def on_button_updatedata():
    try:
        loaddata = json_loaddata(configspath)
        selection = dropdownselect.get()
        loaddata = json_loaddata(configspath)
        loaddata['action'] = str(selection)
        loaddata['webhook']['url'] = str(textbox.get('1.0', 'end')).replace('\n','')
        loaddata['webhook']['tag'] = str(textbox2.get('1.0', 'end')).replace('\n','')
        json_writedata(configspath,loaddata)
        toast.show_toast(
            "Notification",
            "DATA updated successfully!",
            duration = 3,
            icon_path = icon,
            threaded = True,
        )
    except Exception as e:
        toast.show_toast(
            "Notification",
            "DATA update failed!\n"+"OUTPUT: "+str(e),
            duration = 3,
            icon_path = icon,
            threaded = True,
        )
def on_button_check_webhook():
    loaddata = json_loaddata(configspath)
    tagid = loaddata['webhook']['tag']
    tagcheck = False
    try:
        if int(tagid):
            tagcheck = True
    except:
        tagcheck = False
    try:
        if loaddata['webhook']['mention']:
            if loaddata['webhook']['tag'] != "" and loaddata['webhook']['url'] != "":
                if loaddata['webhook']['tag'] == 'everyone':
                    sendwebhook(loaddata['webhook']['url'],"@everyone check webhook from geta's tool")
                    toast.show_toast(
                        "Check webhook",
                        "The webhook was sent successfully!",
                        duration = 3,
                        icon_path = icon,
                        threaded = True,
                    )
                elif loaddata['webhook']['tag'] == 'here':
                    sendwebhook(loaddata['webhook']['url'],"@here check webhook from geta's tool")
                    toast.show_toast(
                        "Check webhook",
                        "The webhook was sent successfully!",
                        duration = 3,
                        icon_path = icon,
                        threaded = True,
                    )
                elif tagcheck:
                    sendwebhook(loaddata['webhook']['url'],f"<@{loaddata['webhook']['tag']}> check webhook from geta's tool")
                    toast.show_toast(
                        "Check webhook",
                        "The webhook was sent successfully!",
                        duration = 3,
                        icon_path = icon,
                        threaded = True,
                    )
                else:
                    sendwebhook(loaddata['webhook']['url'],"check webhook from geta's tool")
                    toast.show_toast(
                        "Check webhook",
                        "The webhook was sent successfully!",
                        duration = 3,
                        icon_path = icon,
                        threaded = True,
                    )
            else:
                toast.show_toast(
                        "Check webhook",
                        "Webhook URL and Discord TAG cannot be empty.",
                        duration = 3,
                        icon_path = icon,
                        threaded = True,
                    )
        else:
            sendwebhook(loaddata['webhook']['url'],"check webhook from geta's tool")
            toast.show_toast(
                "Check webhook",
                "The webhook was sent successfully!",
                duration = 3,
                icon_path = icon,
                threaded = True,
            )
    except Exception as e:
        toast.show_toast(
                "Check webhook",
                "OUTPUT: "+str(e),
                duration = 3,
                icon_path = icon,
                threaded = True,
            )

button_check_webhook.config(command=on_button_check_webhook)
button_updatedata.config(command=on_button_updatedata)
button_confirm.config(command=on_button_confirm)
root.mainloop()
location = pyautogui.locateOnScreen(localpath+'\disconnected.PNG')
print("RUNNING...")
while location is None:
    try:
        location = pyautogui.locateOnScreen(localpath+'\disconnected.PNG')
    except Exception as e:
        location = None
if location:
    print("Found: "+localpath+'\disconnected.PNG')
    toast.show_toast(
        "Notification",
        "Roblox has disconnected!",
        duration = 3,
        icon_path = icon,
        threaded = True,
    )
    loaddata = json_loaddata(configspath)
    if loaddata['webhook']['enabled']:
        print("Start sending webhook...")
        loaddata = json_loaddata(configspath)
        tagid = loaddata['webhook']['tag']
        tagcheck = False
        try:
            if int(tagid):
                tagcheck = True
        except:
            tagcheck = False
        try:
            if loaddata['webhook']['mention']:
                if loaddata['webhook']['tag'] != "" and loaddata['webhook']['url'] != "":
                    if loaddata['webhook']['tag'] == 'everyone':
                        sendwebhook(loaddata['webhook']['url'],"@everyone Roblox has disconnected!")
                        toast.show_toast(
                            "Check webhook",
                            "The webhook was sent successfully!",
                            duration = 3,
                            icon_path = icon,
                            threaded = True)
                    elif loaddata['webhook']['tag'] == 'here':
                        sendwebhook(loaddata['webhook']['url'],"@here Roblox has disconnected!")
                        toast.show_toast(
                            "Check webhook",
                            "The webhook was sent successfully!",
                            duration = 3,
                            icon_path = icon,
                            threaded = True)
                    elif tagcheck:
                        sendwebhook(loaddata['webhook']['url'],f"<@{loaddata['webhook']['tag']}> Roblox has disconnected!")
                        toast.show_toast(
                            "Check webhook",
                            "The webhook was sent successfully!",
                            duration = 3,
                            icon_path = icon,
                            threaded = True)
                    else:
                        sendwebhook(loaddata['webhook']['url'],"Roblox has disconnected!")
                        toast.show_toast(
                            "Check webhook",
                            "The webhook was sent successfully!",
                            duration = 3,
                            icon_path = icon,
                            threaded = True)
                else:
                    toast.show_toast(
                            "Check webhook",
                            "Webhook URL and Discord TAG cannot be empty.",
                            duration = 3,
                            icon_path = icon,
                            threaded = True)
            else:
                sendwebhook(loaddata['webhook']['url'],"Roblox has disconnected!")
                toast.show_toast(
                    "Check webhook",
                    "The webhook was sent successfully!",
                    duration = 3,
                    icon_path = icon,
                    threaded = True)
        except Exception as e:
            toast.show_toast(
                    "Check webhook",
                    "OUTPUT: "+str(e),
                    duration = 3,
                    icon_path = icon,
                    threaded = True)
        print("DONE")
print("Start doing action...")
time.sleep(1)
if loaddata['action'] == 'Shutdown':
    os.system("shutdown /s /t 0")
elif loaddata['action'] == 'Close Roblox':
    for proc in psutil.process_iter():
        if proc.name() == PROCNAME:
            proc.kill()
    print("DONE")
else: 
    pass
sys.exit(0)