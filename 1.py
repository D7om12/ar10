# -*- coding: utf-8 -*-
import ARIFISTIFIK
from ARIFISTIFIK.lib.curve.ttypes import *	
from datetime import datetime	
import io,os,re,ast,six,sys,glob,json,time,timeit,codecs,random,shutil,urllib,urllib2,urllib3,goslate,html5lib,requests,threading,wikipedia,subprocess,googletrans	,pytz
from gtts import gTTS	
from random import randint	
from time import sleep	
from urllib import urlopen, urlretrieve, urlencode	
from io import StringIO	
from bs4 import BeautifulSoup	
from threading import Thread	
from googletrans import Translator	

if (six.PY2):
    import urllib2
    import urllib
else:
    import urllib.request
    import urllib.parse

owner = ARIFISTIFIK.LINE() #Akun Utama
owner.login(token="EubxjkxLIQFbhUvO8ngc.YiNb/pDcDpex4kdwNmXvNa.wkjNiD8g+2OP80zEj4iY/WEXJK+CIuJkWU4bNahYbT4=")
owner.loginResult()
    
arif = ARIFISTIFIK.LINE()
arif.login(token="EuWtbbgTsDwOiomPd24d.shyzkohN5EqZUaaBNnCr+q.r7EWDIwlWmkWgOfMCZ+jx/f/pVRk3u+9GKcT9juztHY=")
arif.loginResult()

ki = ARIFISTIFIK.LINE()
ki.login(token="EuUS6Rp3TUv2egstvMfc.TYh/o16sR2Z4TjSCupGM7a.S9hjz+Vi/D6D+5tcvT5ha5pdcHu2sS6BSJ8jcoZcy8U=")
ki.loginResult()

ghost = ARIFISTIFIK.LINE() #Ghost
ghost.login(token="EuVRdnUfILHSghJRenBc.erKfmq0Nh//3sESdk37gRa.Wri4CkucfhrfLE5dISf8wqOToEeWK4iKlvTkRy5+KcY=")
ghost.loginResult()
print "━━━「arif login success」━━━"
reload(sys)
sys.setdefaultencoding('utf-8')
helpMenu="""┏━━━「 ǞЯiբisƮiբiκ」━━━┓
┣☬┳━━━━━━━━━━━━━━━
┃☬┃ Me
┃☬┃ Add
┃☬┃ Gift
┃☬┃ Spam gift️
┃☬┃ Cn 「 text」
┃☬┃ Clockname 「 text」
┃☬┃ TL:「 text」
┃☬┃ Ban:「 mid」
┃☬┃ Unban:「 mid」
┃☬┃ Bl:on
┃☬┃ Unbl:on
┃☬┃ Mcheck
┃☬┃ Mybio:
┃☬┃ Mybots
┃☬┃ Mymid
┃☬┃ Mygroups
┃☬┃ Group id 
┃☬┃ Message set:「 text」
┃☬┃ Message confirm
┃☬┃ Msg add:「 text」
┃☬┃ Com set:「 text」
┃☬┃ Comment
┃☬┃ Comban/del/cek
┃☬┃ Help set:「 text」
┃☬┃ Change
┃☬┃ Gn 「 text」
┃☬┃ Clink/Curl
┃☬┃ Kick:「 mid」
┃☬┃ Invite:「 mid」
┃☬┃ Creator
┃☬┃ Gcancel:「 jumlah」
┃☬┃ Gcancelall
┃☬┃ Ginfo
┃☬┃ Cctv/Ciduk
┃☬┃ Glink
┃☬┃ Spam on/off
┃☬┃ Gurl
┃☬┃ Clink
┃☬┃ Blocklist
┃☬┃ Banlist
┃☬┃ Update
┃☬┃ Creator
┃☬┃ Sc:「 mid」
┃☬┃ Ban "@"
┃☬┃ Unban "@"
┃☬┃ Sc @
┃☬┃ Nuke
┃☬┃ Backup
┃☬┃ Tagall
┃☬┃ Kick@mbl 
┃☬┃ Reinvite
┃☬┃ Conban
┃☬┃ Clearban
┃☬┃ Gid
┃☬┃ Grupname
┃☬┃ Lurk on/off
┃☬┃ Lurkers
┃☬┃ Wc️
┃☬┃ Sp
┃☬┃ stafflist
┃☬┃ Reboot
┃☬┃ Leaveallgroup
┃☬┃ Pmfavorite
┃☬┃ Broken
┣☬┻━━━━━━━━━━━━━━━
┗━━━「 ǞЯiբisƮiբiκ」━━━╯
  """
helpMessage="""┏━━━「 ǞЯiբisƮiբiκ」━━━┓
┣┳━━━━━━━━━━━━━━━
┃┃♠ 「Menu」
┃┃♠ 「Media」
┃┃♠ 「Translate」
┃┃♠ 「Self」
┃┃♠ 「Settings」
┃┃♠ 「Set」
┣┻━━━━━━━━━━━━━━━
┗━━━「 ǞЯiբisƮiբiκ」━━━╯
"""  
helpMedia="""┏━━━「 ǞЯiբisƮiբiκ」━━━┓
┣┳━━━━━━━━━━━━━━━
┃┃⎈ Youtube 「 text」
┃┃⎈ Youtubesearch 「 user」
┃┃⎈ Ig 「 name」
┃┃⎈ Gimage 
┃┃⎈ Image 「 text」
┃┃⎈ Google 「 text」
┃┃⎈ Micadd @
┃┃⎈ Micdel @
┃┃⎈ Miclist
┃┃⎈ Picturl @
┃┃⎈ Coverurl @
┃┃⎈ Copy @
┃┃⎈ Getname @
┃┃⎈ Getinfo @
┃┃⎈ pict @️
┃┃⎈ Getcontact @
┃┃⎈ Getvid @
┃┃⎈ Getmid @
┃┃⎈ Copy @     
┃┃⎈ Recopy
┃┃⎈ Getcover @    
┃┃⎈ Getbio @
┃┃⎈ Getinfo @
┃┃⎈ youinfo @
┃┃⎈ info 「 mid」
┃┃⎈ Contact 「 mid」
┃┃⎈ Id 「 id line」
┃┃⎈ Memlist
┃┃⎈ Setimage:
┃┃⎈ Papimage
┃┃⎈ Setvideo:
┃┃⎈ Papvideo
┃┃⎈ Checkdate
┃┃⎈ Myname
┃┃⎈ Mybio
┃┃⎈ Mypict
┃┃⎈ Myvid
┃┃⎈ Urlpict
┃┃⎈ Mycover
┃┃⎈ Urlcover
┃┃⎈ Smule 「 id smule」
┃┃⎈ Time
┃┃⎈ Imagetxt 「 text」
┃┃⎈ Playstore 「 text」
┃┃⎈ Twitter 「 text」
┃┃⎈ Github 「 text」
┃┃⎈ Facebook 「 text」
┃┃⎈ Wikipedia 「 text」
┃┃⎈ Checkdate 「 ttl」
┣┻━━━━━━━━━━━━━━━
┗━━━「 ǞЯiբisƮiբiκ」━━━╯
"""
helpFun = """┏━━━「 ǞЯiբisƮiբiκ」━━━┓
┣☬┳━━━━━━━━━━━━━━━
┃☬┃ sider:「 text」
┃☬┃ tagme:「 text」
┃☬┃ welcome:「 text」
┃☬┃ left:「 text」
┃☬┃ message set:「 text」
┃☬┃ cekresponse
┣☬┻━━━━━━━━━━━━━━━
┗━━━「 ǞЯiբisƮiբiκ」━━━╯
"""
helpself="""
┏━━━「 ǞЯiբisƮiբiκ」━━━┓
┣┳━━━━━━━━━━━━━━━
┃┃♅ Fuck1 "@"
┃┃♅ Kick1 "@"
┃┃♅ All mid
┃┃♅ Reinvite
┃┃♅ B1-9 mid
┃┃♅ B1-9name 「 text」
┃┃♅ B1-9
┃┃♅ B1-9 gift
┃┃♅ B1-9 in
┃┃♅ B1-9 bye
┃┃♅ Allgift
┃┃♅ Spam gift️
┃┃♅ Botcopy
┃┃♅ Botbackup
┃┃♅ Botpict
┃┃♅ Botcover
┃┃♅ Allname 「 nama」
┃┃♅ Allbio 「 status」
┃┃♅ Botbyeall  
┣┻━━━━━━━━━━━━━━━
┗━━━「 ǞЯiբisƮiբiκ」━━━╯
  """
helpset="""┏━━━「 ǞЯiբisƮiբiκ」━━━┓
┣┳━━━━━━━━━━━━━━━
┃┃✪ Ban:on/Unbl:on
┃┃✪ Contact:on/off
┃┃✪ Add:on/off
┃┃✪ Join:on/off
┃┃✪ Leave:on/off
┃┃✪ Share:on/off
┃┃✪ Com:on/off
┃┃✪ Clock:on/off
┃┃✪ Respon:on/off
┃┃✪ Stickertag:on/off
┃┃✪ Welcome:on/off
┃┃✪ Left:on/off
┃┃✪ Sider:on/off
┃┃✪ Notag:on/off
┃┃✪ Mimic on/off
┃┃✪ Simsimi:on/off
┃┃✪ Read:0n/off
┃┃✪ Like:on/off
┃┃✪ Runtime
┃┣━「sᴇᴛᴛɪɴɢ ɢʀᴏᴜᴘ」━
┃┃✪ Pro:on/off
┃┃✪ Prolink:on/off
┃┃✪ Proinvite:on/off
┃┃✪ Procancel:on/off
┃┃✪ Namelock:on/off
┃┃✪ Projoin:on/off
┃┃✪ Ghost:on/off
┃┃✪ Allprotect:on/off
┣┻━━━━━━━━━━━━━━━
┗━━━「 ǞЯiբisƮiբiκ」━━━╯
"""
translateMessage ="""
┏━━━「 ǞЯiբisƮiբiκ」━━━┓
┣┳━━━━━━━━━━━━━━━
┃┃🌎 Afrika/
┃┃🌎 Albanian/
┃┃🌎 Arab/
┃┃🌎 Armenian/
┃┃🌎 Bengali/
┃┃🌎 Catalan/
┃┃🌎 Chinese/
┃┃🌎 Croatian/
┃┃🌎 Czech/
┃┃🌎 Danish/
┃┃🌎 Dutch/
┃┃🌎 English/
┃┃🌎 Australia/
┃┃🌎 Uk/
┃┃🌎 Us/
┃┃🌎 Esperanto/
┃┃🌎 Finnish/
┃┃🌎 French/
┃┃🌎 German/
┃┃🌎 Greek/
┃┃🌎 Hindi/
┃┃🌎 Hungarian/
┃┃🌎 Icelandic/
┃┃🌎 Indonesia/
┃┃🌎 Italia/
┃┃🌎 Japanese/
┃┃🌎 Khmer/
┃┃🌎 Korean/
┃┃🌎 Latin/
┃┃🌎 Latvian/
┃┃🌎 Macedonian/
┃┃🌎 Malaysia/
┃┃🌎 Norwegian/
┃┃🌎 Polish/
┃┃🌎 Portuguese/
┃┃🌎 Romanian/
┃┃🌎 Russian/
┃┃🌎 Sarbian/
┃┃🌎 Sinhala/
┃┃🌎 Slovak/
┃┃🌎 Spanish/
┃┃🌎 Spain/
┃┃🌎 Swadhili/
┃┃🌎 Swedish/
┃┃🌎 Tamil/
┃┃🌎 Thai/
┃┃🌎 Turki/
┃┃🌎 Ukrainian/
┃┃🌎 Vietnam/
┃┃🌎 Welsh/
┣┻━━━━━━━━━━━━━━━
┗━━━「 ǞЯiբisƮiբiκ」━━━╯
"""
KAC=[arif,ki,ghost]
DEF=[arif,ki,ghost]
mid = arif.getProfile().mid
kimid = ki.getProfile().mid
ghostmid = ghost.getProfile().mid
Smid = owner.getProfile().mid
Bots=[mid,kimid,ghostmid,Smid,"u65224f4e8812136f01b25275a54b5aef","u48761928e1e7e5e433b8001b9cd711fd","ub721fe3b5e92af6cf8b49b1c50f826ec","u111905310d271fefb749eb032b7ec6ac"]
admin=[mid,kimid,Smid,"u65224f4e8812136f01b25275a54b5aef","u48761928e1e7e5e433b8001b9cd711fd","ub721fe3b5e92af6cf8b49b1c50f826ec","u111905310d271fefb749eb032b7ec6ac"]
creator=["u65224f4e8812136f01b25275a54b5aef"]
admsa=["u65224f4e8812136f01b25275a54b5aef"]

readOpen = codecs.open("st2__b.json","r","utf-8")
read = json.load(readOpen)

contact = arif.getProfile()
restoreprofile = arif.getProfile()
restoreprofile.displayName = contact.displayName
restoreprofile.statusMessage = contact.statusMessage                        
restoreprofile.pictureStatus = contact.pictureStatus

contact = arif.getProfile()
backup = arif.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = ki.getProfile()
backup = ki.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

wait = {
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':False,
    'autoAdd':True,
    'tagme':"message tag belum di set",
    'sider1':"CCTV Jones 😂😂😂",
    'joingc':"WELCOME",
    'leftgc':"Papay... 😢😢😢",
    "stickerMention":False,
    'message':"THANKS FOR ADD ME",
    "lang":"JP",
    "comment":"Thanks For Add Me",
    "comment1":"ᴀᴜᴛᴏ ʟɪᴋᴇ ⓑⓨ「 ∆Яⅰﾓⅰㄅtⅰﾓⅰкᵃʳᶤᶠ ᵐʰ 」\n\n\n\nline.me/ti/p/~arif-qu",
    "commentOn":True,
    "likeOn":{},
    "wcOn":True,
    "leftOn":True,
    "alwayRead":False,
    "Removechat":True,
    "detectMention":False,    
    "kickMention":False,
    "cpp":True,
    "steal":False,
    "Ghost":False,
    'pap':{},
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cName":"",
    "cNames":"",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "protect":False,
    "cancelprotect":False,
    "inviteprotect":False,
    "linkprotect":False,
    "atjointicket":True,
    "potoMention":{},
    "prankName":True,
    "Sider":{},
    "checkSticker":{},
    "cyduk":{},
    "pname":{},
    "pro_name":{},
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
    }
wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }
mimic = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
    }
settings = {
    "simiSimi":{}
    }
res = {
    'num':{},
    'us':{},
    'au':{},
    }
cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}
setTime = {}
setTime = wait2['setTime']
mulai = time.time() 
def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     #If the Current Version of Python is 3.0 or above
        import urllib,request    #urllib library for Extracting web pages
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read)
            return respData
        except Exception as e:
            print(str(e))
    else:                        #If the Current Version of Python is 2.x
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"
#Finding 'Next Image' from the given raw page
def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:    #If no links are found then give an error!
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_meta"')
        start_content = s.find('"ou"',start_line+90)
        end_content = s.find(',"ow"',start_content-90)
        content_raw = str(s[start_content+6:end_content-1])
        return content_raw, end_content
#Getting all links with the help of '_images_get_next_image'
def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      #Append all the links in the list named 'Links'
            time.sleep(0.1)        #Timer could be used to slow down the request for image downloads
            page = page[end_content:]
    return items
    
def summon(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
        akh = akh + 2
        aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
        strt = strt + 6
        akh = akh + 4
        bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    try:
        arif.sendMessage(msg)
    except Exception as error:
        print (error)    
    
def upload_tempimage(client):
     '''
         Upload a picture of a kitten. We don't ship one, so get creative!
     '''
     config = {
         'album': album,
         'name':  'bot auto upload',
         'title': 'bot auto upload',
         'description': 'bot auto upload'
     }
     print("Uploading image... ")
     image = client.upload_from_path(image_path, config=config, anon=False)
     print("Done")
     print()
     return image
def updateProfilePicture(self, path):
        file=open(path, 'rb')
        files = {
            'file': file
        }
        params = {
            'name': 'media',
            'type': 'image',
            'oid': self.profile.mid,
            'ver': '1.0',
        }
        data={
            'params': json.dumps(params)
        }
        r = self.server.postContent(self.server.LINE_OBS_DOMAIN + '/talk/p/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Update profile picture failure.')
        return True
def sendVideo(self, to_, path):
        M = Message(to=to_, text=None, contentType = 2)
        M.contentMetadata = None
        M.contentPreview = None
        M2 = self.Talk.client.sendMessage(0,M)
        M_id = M2.id
        files = {
            'file': open(path, 'rb'),
        }
        params = {
            'name': 'media',
            'oid': M_id,
            'size': len(open(path, 'rb').read()),
            'type': 'video',
            'ver': '1.0',
        }
        data = {
            'params': json.dumps(params)
        }
        r = self.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
        #print r
        if r.status_code != 201:
            raise Exception('Upload video failure.')
        return True
def sendVideoWithURL(self, to_, url):
        path = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
        r = requests.get(url, stream=True)
        if r.status_code == 200:
            with open(path, 'w') as f:
                shutil.copyfileobj(r.raw, f)
        else:
            raise Exception('Download video failure.')
        try:
            self.sendVideo(to_, path)
        except Exception as e:
            raise (e)
def sendAudioWithURL(self, to_, url):
        path = '%s/pythonLine-%1.data' % (tempfile.gettempdir(), randint(0, 9))
        r = requests.get(url, stream=True)
        if r.status_code == 200:
            with open(path, 'w') as f:
                shutil.copyfileobj(r.raw, f)
        else:
            raise Exception('Download audio failure.')
def sendAudio(self, to_, path):
        M = Message(to=to_, text=None, contentType = 3)
        M.contentMetadata = None
        M.contentPreview = None
        M2 = self.Talk.client.sendMessage(0,M)
        M_id = M2.id
        files = {
            'file': open(path, 'rb'),
        }
        params = {
            'name': 'media',
            'oid': M_id,
            'size': len(open(path, 'rb').read()),
            'type': 'audio',
            'ver': '1.0',
        }
        data = {
            'params': json.dumps(params)
        }
        r = self.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Upload audio failure.')
        return True
        try:
            self.sendAudio(to_, path)
        except Exception as e:
            raise (e)
def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
def fullwidth(text):
    '''converts a regular string to Unicode Fullwidth
    Preconditions: text, a string'''
    translator = ''
    translator = translator.maketrans('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&()*+,-./:;<=>?@[]^_`{|}~' , '０１２３４５６７８９ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ！゛＃＄％＆（）＊＋、ー。／：；〈＝〉？＠［］＾＿‘｛｜｝～')
    return text.translate(translator)
def sendImage(self, to_, path):
      M = Message(to=to_, text=None, contentType = 1)
      M.contentMetadata = None
      M.contentPreview = None
      M2 = self._client.sendMessage(0,M)
      M_id = M2.id
      files = {
         'file': open(path, 'rb'),
      }
      params = {
         'name': 'media',
         'oid': M_id,
         'size': len(open(path, 'rb').read()),
         'type': 'image',
         'ver': '1.0',
      }
      data = {
         'params': json.dumps(params)
      }
      r = self.post_content('https://obs-sg.line-apps.com/talk/m/upload.nhn', data=data, files=files)
      if r.status_code != 201:
         raise Exception('Upload image failure.')
      return True
def sendImageWithURL(self, to_, url):
      path = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
      r = requests.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download image failure.')
      try:
         self.sendImage(to_, path)
      except:
         try:
            self.sendImage(to_, path)
         except Exception as e:
            raise e
def NOTIFIED_READ_MESSAGE(op):
    try:
        if op.param1 in wait2['readPoint']:
            Name = arif.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n・" + Name
                wait2['ROM'][op.param1][op.param2] = "・" + Name
        else:
            pass
    except:
        pass
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d Jam %02d Menit %02d Detik' % (hours, mins, secs)
def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 13:
            if mid in op.param3:
                G = arif.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            arif.rejectGroupInvitation(op.param1)
                        else:
                            arif.acceptGroupInvitation(op.param1)
			    G.preventJoinByTicket = False
			    arif.updateGroup(G)
			    Ticket = arif.reissueGroupTicket(op.param1)
			    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
			    arif.acceptGroupInvitationByTicket(op.param1,Ticket)
			    G.preventJoinByTicket = True
			    arif.updateGroup(G)
                    else:
                        arif.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        arif.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace(" ",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    random.choice(KAC).kickoutFromGroup(op.param1, matched_list)
                    
        if op.type == 32:
            if not op.param2 in Bots and admin:
              if not op.param2 in admsa and creator:
                if wait["protect"] == True: 
                    try:
                        klist=[ki,arif,arif,arif,arif,arif,arif,arif,arif]
                        kicker = random.choice(klist) 
                        G = kicker.getGroup(op.param1)
                        kicker.kickoutFromGroup(op.param1,[op.param2])
                        arif.inviteIntoGroup(op.param1,[op.param3])
                    except Exception, e:
                       print e                                       
                    
        if op.type == 13:
            if op.param3 in mid:
                if op.param2 in kimid:
                    G = kimid.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    kimid.updateGroup(G)
                    Ticket = kimid.reissueGroupTicket(op.param1)
                    arif.acceptGroupInvitationByTicket(op.param1,Ticket)
                    G.preventJoinByTicket = True
                    kimid.updateGroup(G)
                    Ticket = kimid.reissueGroupTicket(op.param1)

            if op.param3 in kimid:
                if op.param2 in mid:
                    X = arif.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    arif.updateGroup(X)
                    Ti = arif.reissueGroupTicket(op.param1)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    ki.updateGroup(X)
                    Ti = ki.reissueGroupTicket(op.param1)

            if op.param3 in mid:
                if op.param2 in kimid:
                    X = ki.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki.updateGroup(X)
                    Ti = ki.reissueGroupTicket(op.param1)
                    arif.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    arif.updateGroup(X)
                    Ti = arif.reissueGroupTicket(op.param1)

            if op.param3 in mid:
                if op.param2 in mid:
                    X = arif.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    arif.updateGroup(X)
                    Ti = arif.reissueGroupTicket(op.param1)
                    arif.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    arif.updateGroup(X)
                    Ti = arif.reissueGroupTicket(op.param1)
                
            if op.param3 in mid:
                if op.param2 in mid:
                    X = arif.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    arif.updateGroup(X)
                    Ti = arif.reissueGroupTicket(op.param1)
                    arif.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    arif.updateGroup(X)
                    Ti = arif.reissueGroupTicket(op.param1)
                
            if op.param3 in mid:
                if op.param2 in mid:
                    X = arif.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    arif.updateGroup(X)
                    Ti = arif.reissueGroupTicket(op.param1)
                    arif.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    arif.updateGroup(X)
                    Ti = arif.reissueGroupTicket(op.param1)
                
            if op.param3 in mid:
                if op.param2 in mid:
                    X = arif.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    arif.updateGroup(X)
                    Ti = arif.reissueGroupTicket(op.param1)
                    arif.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    arif.updateGroup(X)
                    Ti = arif.reissueGroupTicket(op.param1)
                
            if op.param3 in mid:
                if op.param2 in mid:
                    X = arif.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    arif.updateGroup(X)
                    Ti = arif.reissueGroupTicket(op.param1)
                    arif.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    arif.updateGroup(X)
                    Ti = arif.reissueGroupTicket(op.param1)
                
            if op.param3 in mid:
                if op.param2 in mid:
                    X = arif.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    arif.updateGroup(X)
                    Ti = arif.reissueGroupTicket(op.param1)
                    arif.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    arif.updateGroup(X)
                    Ti = arif.reissueGroupTicket(op.param1)
                    
            if op.param3 in mid:
                if op.param2 in mid:
                    X = arif.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    arif.updateGroup(X)
                    Ti = arif.reissueGroupTicket(op.param1)
                    arif.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    arif.updateGroup(X)
                    Ti = arif.reissueGroupTicket(op.param1)
                                  
        if op.type == 55:
	    try:
	      group_id = op.param1
	      user_id=op.param2
	      subprocess.Popen('echo "'+ user_id+'|'+str(op.createdTime)+'" >> dataSeen/%s.txt' % group_id, shell=True, stdout=subprocess.PIPE, )
	    except Exception as e:
	      print e            
        if op.type == 19:
            if mid in op.param3:
                wait["blacklist"][op.param2] = True
            #if op.param2 not in Bots + admin + creator:
             #     if wait["Ghost"] == True:  
              #     try:
               #        klist=[arif,ki,arif,arif,arif,arif]
                #       kicker = random.choice(klist)
                 #      G = kicker.getGroup(op.param1)
                  #     G.preventJoinByTicket = False
                  #     kicker.updateGroup(G)
                  #     Ticket = kicker.reissueGroupTicket(op.param1)
                  #     ghostacceptGroupInvitationByTicket(op.param1,Ticket)
                  #     time.sleep(0.0002)
                  #     X = kicker.getGroup(op.param1)             
                  #     X.preventJoinByTicket = True
                 #      ghost.kickoutFromGroup(op.param1,[op.param2])
                 #      kicker.kickoutFromGroup(op.param1,[op.param2])
                 #      ghost.leaveGroup(op.param1)
                  #     kicker.updateGroup(X)
                  # except Exception, e:
                   #         print e
           # if op.param2 not in Bots:
            #  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
             # arif.inviteIntoGroup(op.param1,[op.param3])
            if op.param2 not in Bots + admin + creator:
                    try:
                    	gs = arif.getGroup(op.param1)
                        targets = [op.param2]
                        for target in targets:
                           try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                           except:
                            pass
                                
                    except Exception, e:
                        print e
            if op.param3 in admin: #Kalo Admin ke Kick
              if op.param2 in Bots:
                pass
              if op.param2 in admin:
                pass
              else:
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  arif.inviteIntoGroup(op.param1,[op.param3])                
            if op.param3 in Smid: #Akun Utama Ke Kick
                G = random.choice(KAC).getGroup(op.param1)
                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                G.preventJoinByTicket = False
                random.choice(KAC).updateGroup(G)
                Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                owner.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                G.preventJoinByTicket = True
                random.choice(KAC).updateGroup(G)
                owner.updateGroup(G)
                wait["blacklist"][op.param2] = True
        if op.type == 22:
            if wait["leaveRoom"] == True:
                arif.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                arif.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == mid:
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            arif.acceptGroupInvitationByTicket(list_[1],list_[2])
                            G = arif.getGroup(list_[1])
                            G.preventJoinByTicket = True
                            arif.updateGroup(G)
                        except:
                            arif.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    arif.leaveRoom(msg.to)
            if msg.contentType == 7:
                if wait["checkSticker"] == True:
                    stk_id = msg.contentMetadata["STKID"]
                    stk_ver = msg.contentMetadata["STKVER"]
                    pkg_id = msg.contentMetadata["STKPKGID"]
                    ret_ = "┏━━[ Sticker Info ]"
                    ret_ += "\n┣ STICKER ID : {}"(stk_id)
                    ret_ += "\n┣ STICKER PACKAGES ID : {}"(pkg_id)
                    ret_ += "\n┣ STICKER VERSION : {}"(stk_ver)
                    ret_ += "\n┣ STICKER URL : line://shop/detail/{}"(pkg_id)
                    ret_ += "\n┗━━[ Finish ]"
                    arif.sendMessage(msg)
                    arif.sendText(msg.to,ret_)
            if msg.contentType == 16:
              if wait["likeOn"] == True:
                url = msg.contentMetadata["postEndUrl"]
                arif.like(url[25:58], url[66:], likeType=1001)
                ki.like(url[25:58], url[66:], likeType=1002)
                #ghost.like(url[25:58], url[66:], likeType=1001)
                arif.comment(url[25:58], url[66:], wait["comment1"])
                ki.comment(url[25:58], url[66:], wait["comment1"])
                arif.comment(url[25:58], url[66:], wait["comment1"])
                arif.comment(url[25:58], url[66:], wait["comment1"])
                arif.comment(url[25:58], url[66:], wait["comment1"])
                arif.comment(url[25:58], url[66:], wait["comment1"])
                arif.comment(url[25:58], url[66:], wait["comment1"])
                arif.comment(url[25:58], url[66:], wait["comment1"])
                arif.comment(url[25:58], url[66:], wait["comment1"])
                arif.comment(url[25:58], url[66:], wait["comment1"])
                #ghost.comment(url[25:58], url[66:], wait["comment1"])
                wait["likeOn"] = False
#-----------------------------------------------
        if op.type == 11:
            if op.param3 == '1':
                if op.param1 in wait['pname']:
                    try:
                        G = arif.getGroup(op.param1)
                    except:
                        try:
                            G = ki.getGroup(op.param1)
                        except:
                            try:
                                G = arif.getGroup(op.param1)
                            except:
                                try:
                                    G = arif.getGroup(op.param1)
                                except:
                                    try:
                                        G = arif.getGroup(op.param1)
				    except:
					try:
                                            G = arif.getGroup(op.param1)
                                        except:
                                            pass
                    G.name = wait['pro_name'][op.param1]
                    try:
                        arif.updateGroup(G)
                    except:
                        try:
                            ki.updateGroup(G)
                        except:
                            try:
                                arif.updateGroup(G)
                            except:
                                try:
                                    arif.updateGroup(G)
                                except:
                                    try:
                                        arif.updateGroup(G)
                                    except:
                                        try:
                                            arif.updateGroup(G)
                                        except:
                                            pass
                    if op.param2 in Bots:
                        pass
                    else:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                arif.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    arif.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        arif.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            arif.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass
        if op.type == 26:
            msg = op.message
            if msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
                    text = msg.text
                    if text is not None:
                        ki.sendText(msg.to,text)
        if op.type == 26:
            msg = op.message
            if msg.to in settings["simiSimi"]:
                if settings["simiSimi"][msg.to] == True:
                    if msg.text is not None:
                        text = msg.text
                        r = requests.get("http://api.ntcorp.us/chatbot/v1/?text=" + text.replace(" ","+") + "&key=beta1.nt")
                        data = r.text
                        data = json.loads(data)
                        if data['status'] == 200:
                            if data['result']['result'] == 100:
                                arif.sendText(msg.to, "🤠" + data['result']['response'].encode('utf-8'))
            if "MENTION" in msg.contentMetadata.keys() != None:
                 if wait['detectMention'] == True:
                     contact = arif.getContact(msg.from_)
                     cName = contact.pictureStatus
                     balas = ["http://dl.profile.line-cdn.net/" + cName]
                     ret_ = random.choice(balas)
                     mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                     mentionees = mention["MENTIONEES"]
                     for mention in mentionees:
                           if mention["M"] in mid:
                                  arif.sendImageWithURL(msg.to,ret_)
                                  msg.contentType = 13
                                  msg.contentMetadata = {'mid': msg.from_}
                                  arif.sendMessage(msg)
                                  arif.sendText(msg.to, wait["tagme"])
                                  break
            if "MENTION" in msg.contentMetadata.keys() != None:
            	if wait['stickerMention'] == True:
                     mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                     mentionees = mention["MENTIONEES"]
                     for mention in mentionees:
                           if mention["M"] in mid:
                           	msg.contentType = 7
                           	msg.text = ''
                           	msg.contentMetadata = {
                                                  	   'STKPKGID': 1,
                                                  	   'STKTXT': '[]',
                                                  	   'STKVER': 100,
                                                  	   'STKID':110 
                                              		 }
                           	arif.sendText(msg.to, wait["tagme"])
                           	arif.sendMessage(msg)
                           	break
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["kickMention"] == True:
                     contact = arif.getContact(msg.from_)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in mid:
                                  arif.sendText(msg.to,"don't tag me")
                                  arif.kickoutFromGroup(msg.to,[msg.from_])
                                  break
            if msg.contentType == 13:
                if wait['invite'] == True:
                     _name = msg.contentMetadata["displayName"]
                     invite = msg.contentMetadata["mid"]
                     groups = arif.getGroup(msg.to)
                     pending = groups.invitee
                     targets = []
                     for s in groups.members:
                         if _name in s.displayName:
                             arif.sendText(msg.to, _name + " Berada DiGrup Ini")
                         else:
                             targets.append(invite)
                     if targets == []:
                         pass
                     else:
                         for target in targets:
                             try:
                                 arif.findAndAddContactsByMid(target)
                                 arif.inviteIntoGroup(msg.to,[target])
                                 arif.sendText(msg.to,"Invite " + _name)
                                 wait['invite'] = False
                                 break                              
                             except:             
                                      arif.sendText(msg.to,"Error")
                                      wait['invite'] = False
                                      break
            if wait["alwayRead"] == True:
                if msg.toType == 0:
                    arif.sendChatChecked(msg.from_,msg.id)
                else:
                    arif.sendChatChecked(msg.to,msg.id)
            if wait["Removechat"] == True:
                if msg.toType == 0:
                    arif.removeAllMessages(op.param2)
                    ki.removeAllMessages(op.param2)
                    owner.removeAllMessages(op.param2)
                else:
                    arif.removeAllMessages(op.param2)
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
                if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        arif.sendText(msg.to,"sudah masuk daftar hitam👈")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        arif.sendText(msg.to,"Itu tidak berkomentar👈")
                elif wait["dblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        arif.sendText(msg.to,"Done")
                        wait["dblack"] = False
                    else:
                        wait["dblack"] = False
                        arif.sendText(msg.to,"Tidak ada dalam daftar hitam👈")
                elif wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        arif.sendText(msg.to,"sudah masuk daftar hitam")
                        wait["wblacklist"] = False
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        arif.sendText(msg.to,"Done👈")
                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        arif.sendText(msg.to,"Done👈")
                        wait["dblacklist"] = False
                    else:
                        wait["dblacklist"] = False
                        arif.sendText(msg.to,"Done👈")
                elif wait["contact"] == True:
                    msg.contentType = 0
                    arif.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = arif.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = arif.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        arif.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = arif.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = arif.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        try:
                            arif.sendImageWithURL(msg.to, "http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        except:
                            cu = ""
                        arif.sendText(msg.to,"🎀━displayName━🎀\n✤[" + contact.displayName + "]✤\n🎀━MIDs━🎀\n✤[" + msg.contentMetadata["mid"] + "]✤\n🎀━StatusContact━🎀\n✤" + contact.statusMessage + "✤")
                        arif.sendText(msg.to,"LINKPROFILE\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\nLINKBERANDA\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "menempatkan URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    arif.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text in ["Botallbye"]: 
              if msg.from_ in creator:    
                gid = ki.getGroupIdsJoined()
                gid = arif.getGroupIdsJoined()
                for i in gid:
                  ki.leaveGroup(i)
                  arif.leaveGroup(i)
                if wait["lang"] == "JP":
                  random.choice(KAC).sendText(msg.to,"Bye~Bye " + str(ginfo.name) + "\n\nBots Dipaksa Keluar oleh selfbot...!!!\nMakasih...!!!")
                else:
                  arif.sendText(msg.to,"He declined all invitations")
#--------------------------
            elif msg.text in ["Leaveallgroup"]: 
              if msg.from_ in creator:
                gid = arif.getGroupIdsJoined()
                for i in gid:
                  arif.leaveGroup(i)
                if wait["lang"] == "JP":
                  arif.sendText(msg.to,"Bye~Bye " + str(ginfo.name) + "\n\nBots Dipaksa Keluar oleh selfbot...!!!\nMakasih...!!!")
                else:
                  arif.sendText(msg.to,"He declined all invitations")
#----------------------------------------------
            elif "/Sendgrup " in msg.text:
              if msg.from_ in creator + admin:
                    bctxt = msg.text.replace("/Sendgrup ", "")
                    n = arif.getGroupIdsJoined()
                    for manusia in n:
                        arif.sendText(manusia, (bctxt))
            elif "/Sendcontact " in msg.text:
              if msg.from_ in creator + admin:
					bctxt = msg.text.replace("/Sendcontact ", "")
					t = arif.getAllContactIds()
					t = ki.getAllContactIds()
					for manusia in t:
						arif.sendText(manusia,(bctxt))
						ki.sendText(manusia,(bctxt))
            elif "/Sendpm " in msg.text:
                    bctxt = msg.text.replace("/Sendpm ", "")
                    t = arif.getAllContactIds()
                    for manusia in t:
                        arif.sendText(manusia, (bctxt))
            elif "Virus" in msg.text:
              if msg.from_ in creator:
                msg.contentType = 13
                msg.contentMetadata = {'mid': "BEBAS,'"}
                arif.sendMessage(msg)
            elif msg.text in ["Stafflist"]:
              if Bots == []:
                  arif.sendText(msg.to,"The Friends is empty")
              else:
                  arif.sendText(msg.to,"Tunggu...")
                  mc = "||===FRIENDLIST===||\n=====================\n"
                  for mi_d in Bots:
                      mc += "★" +arif.getContact(mi_d).displayName + "\n"
                  arif.sendText(msg.to,mc)
                  print "[Command]Friendlist executed"                    
            elif "Youinfo" in msg.text:
              if msg.from_ in creator + admin:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = arif.getContact(key1)
                cu = arif.channel.getCover(key1)
                path = str(cu)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                try:
                    arif.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nBio :\n" + contact.statusMessage)
                    arif.sendText(msg.to,"Profile Picture " + contact.displayName)
                    arif.sendImageWithURL(msg.to,image)
                    arif.sendText(msg.to,"Cover " + contact.displayName)
                    arif.sendImageWithURL(msg.to,path)
                except:
                    pass
            elif "Botak" in msg.text:
              if msg.from_ in creator + admin:
                group = arif.getGroup(msg.to)
                k = len(group.members)//100
                for j in xrange(k+1):
                    msg = Message(to=msg.to)
                    txt = u''
                    s=0
                    d=[]
                    for i in group.members[j*200 : (j+1)*200]:
                        d.append({"S":str(s), "E" :str(s+8), "M":i.mid})
                        s += 9
                        txt += u'@Krampus\n'
                    msg.text = txt
                    msg.contentMetadata = {u'MENTION':json.dumps({"MENTIONEES":d})}
                    ki.sendMessage(msg) 
                    

            elif "Github " in msg.text:
                    a = msg.text.replace("Github ","")
                    b = urllib.quote(a)
                    arif.sendText(msg.to,"「 Searching 」\n" "Type: GitHub Search\nStatus: Processing...")
                    arif.sendText(msg.to, "Title: " + a + "\nLink: https://github.com/search?utf8=✓&q="+b)
            elif 'playstore ' in msg.text.lower():
                    tob = msg.text.lower().replace('playstore ',"")
                    arif.sendText(msg.to,"Please wait...")
                    arif.sendText(msg.to,"Title : "+tob+"\nSource : Google Play\nLinknya : https://play.google.com/store/search?q=" + tob)
                    arif.sendText(msg.to,"This is link aplication")     
            elif "Wikipedia " in msg.text:
                  try:
                      wiki = msg.text.lower().replace("Wikipedia ","")
                      wikipedia.set_lang("id")
                      pesan="Title ("
                      pesan+=wikipedia.page(wiki).title
                      pesan+=")\n\n"
                      pesan+=wikipedia.summary(wiki, sentences=1)
                      pesan+="\n"
                      pesan+=wikipedia.page(wiki).url
                      arif.sendText(msg.to, pesan)
                  except:
                          try:
                              pesan="Over Text Limit! Please Click link\n"
                              pesan+=wikipedia.page(wiki).url
                              arif.sendText(msg.to, pesan)
                          except Exception as e:
                              arif.sendText(msg.to, str(e))
            elif "Twitter " in msg.text:
                    a = msg.text.replace("Twitter ","")
                    b = urllib.quote(a)
                    arif.sendText(msg.to,"「 Searching 」\n" "Type:Search Info\nStatus: Processing")
                    arif.sendText(msg.to, "https://www.twitter.com" + b)
                    arif.sendText(msg.to,"「 Searching 」\n" "Type:Search Info\nStatus: Success") 
            elif "Smule " in msg.text:
                    a = msg.text.replace("Smule ","")
                    b = urllib.quote(a)
                    arif.sendText(msg.to,"Searching to id smule..")
                    arif.sendText(msg.to, "Nama: "+b+"\nId smule: http://smule.com/" +b)
            elif "Google " in msg.text:
                    a = msg.text.replace("Google ","")
                    b = urllib.quote(a)
                    arif.sendText(msg.to,"Searching google..")
                    arif.sendText(msg.to, "Search: "+b+"\nsuccess: http://google.com/" +b)
	    elif "Xvideos " in msg.text:
		    a = msg.text.replace("Xvideos ","")
                    b = urllib.quote(a)
                    arif.sendText(msg.to,"Searching ....\n" "Type:Search Xvideos\nStatus: Processing")
                    arif.sendText(msg.to, "{ Xvideos search page }\n\nTitle: "+b+"\nSource : Xvideos\nhttp://xvideos.com/?k=" +b)
            elif "Picturl @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Picturl @","")
                _nametarget = _name.rstrip(' ')
                gs = arif.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    arif.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = arif.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            arif.sendText(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]dp executed"
            elif "Coverurl @" in msg.text:
              if msg.from_ in creator + admin:
                print "[Command]cover executing"
                _name = msg.text.replace("Coverurl @","")
                _nametarget = _name.rstrip(' ')
                gs = arif.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    arif.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = arif.getContact(target)
                            cu = arif.channel.getCover(target)
                            path = str(cu)
                            arif.sendText(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]cover executed"         
            elif msg.text in ["Pmfavorite"]:
              if msg.from_ in creator + admin:
                dj = arif.getFavoriteMids()
                kontak = arif.getContacts(dj)
                num = 1
                family = str(len(dj))
                msgs = "[List Favorite Friends Guys]"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\nTotal Friend : %i" % len(kontak)
                arif.sendText(msg.to, msgs)
            elif msg.text.lower()  == 'setauto':
              if msg.from_ in creator + admin:
                   arif.sendText(msg.to,helpFun)
            elif msg.text.lower() == 'help':
              if msg.from_ in creator + admin:
                if wait["lang"] == "JP":
                    arif.sendText(msg.to,helpMessage)
                else:
                    arif.sendText(msg.to,helpMessage)
            elif msg.text.lower() == 'menu':
              if msg.from_ in creator + admin:
                if wait["lang"] == "JP":
                    arif.sendText(msg.to,helpMenu)
                else:
                    arif.sendText(msg.to,helpMenu)
            elif msg.text.lower() == 'media':
              if msg.from_ in creator + admin:
                if wait["lang"] == "JP":
                    arif.sendText(msg.to,helpMedia)
                else:
                    arif.sendText(msg.to,helpMedia)
            elif msg.text.lower() == 'self':
              if msg.from_ in creator + admin:
                if wait["lang"] == "JP":
                    arif.sendText(msg.to,helpself)
                else:
                    arif.sendText(msg.to,helpself)
            elif msg.text.lower() == 'settings':
              if msg.from_ in creator + admin:
                if wait["lang"] == "JP":
                    arif.sendText(msg.to,helpset)
                else:
                    arif.sendText(msg.to,helpset)
            elif ("Gn:" in msg.text):
              if msg.from_ in creator + admin:
                if msg.toType == 2:
                    group = arif.getGroup(msg.to)
                    group.name = msg.text.replace("Gn:","")
                    arif.updateGroup(group)
                else:
                    arif.sendText(msg.to,"Hal ini tidak dapat digunakan di luar kelompok👈")
            elif ("Gn " in msg.text):
              if msg.from_ in creator + admin:
                if msg.toType == 2:
                    group = arif.getGroup(msg.to)
                    group.name = msg.text.replace("Gn ","")
                    arif.updateGroup(group)
                else:
                    arif.sendText(msg.to,"Can not be used for groups other than")
            elif "Kick:" in msg.text:
              if msg.from_ in creator + admin:
                midd = msg.text.replace("Kick:","")
                arif.kickoutFromGroup(msg.to,[midd])
            elif "Invite:" in msg.text:
              if msg.from_ in creator + admin:
                midd = msg.text.replace("Invite:","")
                arif.findAndAddContactsByMid(midd)
                arif.inviteIntoGroup(msg.to,[midd])
            elif "Me" == msg.text:
                       msg.contentType = 13
                       msg.contentMetadata = {'mid': msg.from_}
                       arif.sendMessage(msg)
                       eltime = time.time() - mulai
                       van = "Bot has been active "+waktu(eltime)
                       arif.sendText(msg.to,van) 
            elif "Mybots" == msg.text:
              if msg.from_ in creator + admin:
                msg.contentType = 13
                msg.contentMetadata = {'mid': kimid}
                arif.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                arif.sendMessage(msg)
            elif "Respon" == msg.text:
              if msg.from_ in creator + admin:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                arif.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': kimid}
                ki.sendMessage(msg)
                ki.sendText(msg.to,"AMAN TERKENDALI ")
            elif "B1" == msg.text:
              if msg.from_ in creator + admin:
                msg.contentType = 13
                msg.contentMetadata = {'mid': kimid}
                ki.sendMessage(msg)
            elif "Creator" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': 'u65224f4e8812136f01b25275a54b5aef'}
                arif.sendMessage(msg)
            elif msg.text in ["B1 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '8fe8cdab-96f3-4f84-95f1-6d731f0e273e',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '7'}
                msg.text = None
                ki.sendMessage(msg)
            elif msg.text in ["Gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '696d7046-843b-4ed0-8aac-3113ed6c0733',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '6'}
                msg.text = None
                arif.sendMessage(msg)

            elif msg.text in ["B1 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                arif.sendMessage(msg)

            elif msg.text in ["B1 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '4'}
                msg.text = None
                arif.sendMessage(msg)
            elif msg.text in ["B1 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                arif.sendMessage(msg)
            elif msg.text in ["B1 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '6'}
                msg.text = None
                arif.sendMessage(msg)
            elif msg.text in ["B1 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '7'}
                msg.text = None
                arif.sendMessage(msg)
            elif msg.text in ["B1 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '8'}
                msg.text = None
                arif.sendMessage(msg)
            elif msg.text in ["B1 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '13'}
                msg.text = None
                arif.sendMessage(msg)
            elif msg.text in ["B1 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '11'}
                msg.text = None
                arif.sendMessage(msg)
            elif msg.text in ["Spam gift"]:
				if msg.from_ in admin:
					msg.contentType = 9
					msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
										'PRDTYPE': 'THEME',
										'MSGTPL': '12'}
					msg.text = None
					ki.sendMessage(msg)
					arif.sendMessage(msg)
            elif msg.text in ["Clink"]:
              if msg.from_ in creator + admin:
                if msg.toType == 2:
                    group = arif.getGroup(msg.to)
                    group.preventJoinByTicket = False
                    arif.updateGroup(group)
                    if wait["lang"] == "JP":
                        arif.sendText(msg.to,"URL open ô€¨ô€„Œ")
                    else:
                        arif.sendText(msg.to,"URL open ô€¨ô€„Œ")
                else:
                    if wait["lang"] == "JP":
                        arif.sendText(msg.to,"It can not be used outside the group👈")
                    else:
                        arif.sendText(msg.to,"Can not be used for groups other than")
            elif msg.text in ["Curl"]:
                if msg.toType == 2:
                    group = arif.getGroup(msg.to)
                    group.preventJoinByTicket = True
                    arif.updateGroup(group)
                    if wait["lang"] == "JP":
                        arif.sendText(msg.to,"URL close 👈")
                    else:
                        arif.sendText(msg.to,"URL close 👈")
                else:
                    if wait["lang"] == "JP":
                        arif.sendText(msg.to,"It can not be used outside the group  👈")
                    else:
                        arif.sendText(msg.to,"Can not be used for groups other than ")
            elif msg.text.lower() == 'ginfo':        
                    group = arif.getGroup(msg.to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "Error"
                    md ="✥GROUP NAME✥\n" + group.name + "\n\n✥GROUP ID✥\n✿" + group.id +"✿" "\n\n[Pembuat Grup :]\n" + gCreator + "\n\n[Gambar Grup : ]\nhttp://dl.profile.line-cdn.net/" + group.pictureStatus
                    if group.preventJoinByTicket is False: md += "\n\nKode Url : Diizinkan"
                    else: md += "\n\nKode Url : Diblokir"
                    if group.invitee is None: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : 0 Orang"
                    else: md += "\n✥TOTAL MEMBER✥\n" + str(len(group.members)) + " Orang" + "\n✥PENDINGAN✥\n" + str(len(group.invitee)) + " Orang"
                    arif.sendText(msg.to,md)
            elif "Mymid" == msg.text:
                arif.sendText(msg.to,msg.from_)
            elif "B mid" == msg.text:
              if msg.from_ in creator + admin:
                arif.sendText(msg.to,mid)
            elif "B1 mid" == msg.text:
              if msg.from_ in creator + admin:
                ki.sendText(msg.to,kimid)
            elif "All mid" == msg.text:
              if msg.from_ in creator + admin:
                arif.sendText(msg.to,mid)
                ki.sendText(msg.to,kimid)
                ghost.sendText(msg.to,ghostmid)
            elif "TL:" in msg.text:
              if msg.from_ in creator + admin:
                tl_text = msg.text.replace("TL:","")
                arif.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+arif.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif "Allname " in msg.text:
              if msg.from_ in creator + admin:
                string = msg.text.replace("Allname ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = arif.getProfile()
                    profile.displayName = string
                    arif.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = arif.getProfile()
                    profile.displayName = string
                    arif.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = arif.getProfile()
                    profile.displayName = string
                    arif.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = arif.getProfile()
                    profile.displayName = string
                    arif.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = arif.getProfile()
                    profile.displayName = string
                    arif.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = arif.getProfile()
                    profile.displayName = string
                    arif.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = arif.getProfile()
                    profile.displayName = string
                    arif.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = arif.getProfile()
                    profile.displayName = string
                    arif.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = arif.getProfile()
                    profile.displayName = string
                    arif.updateProfile(profile)
                    arif.sendText(msg.to,"􀜁􀇔􏿿NAMA BOT BERHASIL DI UBAH MENJADI\n👉" + string + "👈")
            elif "Allbio " in msg.text:
              if msg.from_ in creator + admin:
                string = msg.text.replace("Allbio ","")
                if len(string.decode('utf-8')) <= 500:
                    profile = arif.getProfile()
                    profile.statusMessage = string
                    arif.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki.getProfile()
                    profile.statusMessage = string
                    ki.updateProfile(profile)
                    arif.sendText(msg.to,"􀜁􀇔􏿿SEMUA TELAH  UPDATE BIO PROFILE\n👉" + string + "👈")
            elif "Mybio " in msg.text:
              if msg.from_ in creator + admin:
                string = msg.text.replace("Mybio ","")
                if len(string.decode('utf-8')) <= 500:
                    profile = arif.getProfile()
                    profile.statusMessage = string
                    arif.updateProfile(profile)
                    arif.sendText(msg.to,"􀜁􀇔􏿿Update Bio\n👉" + string + "👈")
#------------------------------------------------------------------------------------------#
            elif "Bname " in msg.text:
              if msg.from_ in creator + admin:
                string = msg.text.replace("Bname ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = arif.getProfile()
                    profile.displayName = string
                    arif.updateProfile(profile)
                    arif.sendText(msg.to,"􀜁􀇔􏿿Update Names👉 " + string + "👈")
#---------------------------------------------------------
            elif "B1name " in msg.text:
              if msg.from_ in creator + admin:
                string = msg.text.replace("B1name ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                    ki.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "B1name " in msg.text:
              if msg.from_ in creator + admin:
                string = msg.text.replace("B1name ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = arif.getProfile()
                    profile.displayName = string
                    arif.updateProfile(profile)
                    arif.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "B1name " in msg.text:
              if msg.from_ in creator + admin:
                string = msg.text.replace("B1name ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = arif.getProfile()
                    profile.displayName = string
                    arif.updateProfile(profile)
                    arif.sendText(msg.to,"??􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "B1name " in msg.text:
              if msg.from_ in creator + admin:
                string = msg.text.replace("B1name ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = arif.getProfile()
                    profile.displayName = string
                    arif.updateProfile(profile)
                    arif.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
#--------------------------------------------------------
            elif "B1name " in msg.text:
              if msg.from_ in creator + admin:
                string = msg.text.replace("B1name ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = arif.getProfile()
                    profile.displayName = string
                    arif.updateProfile(profile)
                    arif.sendText(msg.to,"􀇔 􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "B1name " in msg.text:
              if msg.from_ in creator + admin:
                string = msg.text.replace("B1name ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = arif.getProfile()
                    profile.displayName = string
                    arif.updateProfile(profile)
                    arif.sendText(msg.to,"􀜁􀇔􏿿Update Names��" + string + "👈")
#---------------------------------------------------------
            elif "B1name " in msg.text:
              if msg.from_ in creator + admin:
                string = msg.text.replace("B1name ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = arif.getProfile()
                    profile.displayName = string
                    arif.updateProfile(profile)
                    arif.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#---------------------------------------------------------
            elif "B1name " in msg.text:
              if msg.from_ in creator + admin:
                string = msg.text.replace("B1name ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = arif.getProfile()
                    profile.displayName = string
                    arif.updateProfile(profile)
                    arif.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#---------------------------------------------------------
            elif "B1name " in msg.text:
              if msg.from_ in creator + admin:
                string = msg.text.replace("B1name ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = arif.getProfile()
                    profile.displayName = string
                    arif.updateProfile(profile)
                    arif.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#---------------------------------------------------------
#--------------------------------------------------------
            elif "wkwkwk" in msg.text.lower():
                    msg.contentType = 7
                    msg.text = "Yg Ketawa Gak Waras"
                    arif.sendText(msg.to, "Yg Ketawa Gak Waras")
                    msg.contentMetadata={'STKID': '100',
                                        'STKPKGID': '1',
                                        'STKVER': '100'}                    
                    arif.sendMessage(msg)
                    
            elif "tidur" in msg.text.lower():
                    msg.contentType = 7
                    msg.text = "Yuk Bot Temenin Tidur"
                    arif.sendText(msg.to, "Yuk Bot Temenin Tidur")
                    msg.contentMetadata={'STKID': '1',
                                        'STKPKGID': '1',
                                        'STKVER': '100'}                  
                    arif.sendMessage(msg)
                    
            elif "hahaha" in msg.text.lower():
                    msg.contentType = 7
                    msg.text = "Jones ketawa"
                    arif.sendText(msg.to, "Jones ketawa")
                    msg.contentMetadata={'STKID': '21831483',
                                        'STKPKGID': '9674',
                                        'STKVER': '100'}                
                    arif.sendMessage(msg)
                    
            elif "hoax" in msg.text.lower():
                    msg.contentType = 7
                    msg.contentMetadata={'STKID': '20332852',
                                        'STKPKGID': '9472',
                                        'STKVER': '100'}
                    msg.text = None
                    arif.sendMessage(msg)
                    
            elif "tet" in msg.text.lower():
                    msg.contentType = 7
                    msg.text = "Nah kan"
                    arif.sendText(msg.to, "Nah kan")
                    msg.contentMetadata={'STKID': '20332855',
                                        'STKPKGID': '9472',
                                        'STKVER': '100'}          
                    arif.sendMessage(msg)
                    
            elif "dugem" in msg.text.lower():
                    msg.contentType = 7
                    msg.text = "Yuk dugem"
                    arif.sendText(msg.to, "Yuk dugem")
                    msg.contentMetadata={'STKID': '21831481',
                                        'STKPKGID': '9674',
                                        'STKVER': '100'}                    
                    arif.sendMessage(msg)
                    
            elif "peluk" in msg.text.lower():
                    msg.contentType = 7
                    msg.text = "Sini peluk"
                    arif.sendText(msg.to, "Sini peluk")
                    msg.contentMetadata={'STKID': '156',
                                        'STKPKGID': '2',
                                        'STKVER': '100'}                    
                    arif.sendMessage(msg)
                    
            elif "bot" in msg.text.lower():
                    msg.contentType = 7
                    msg.text = "Hadir mblo"
                    arif.sendText(msg.to, "Hadir mblo")
                    msg.contentMetadata={'STKID': '27695298',
                                        'STKPKGID': '1900619',
                                        'STKVER': '100'}                    
                    arif.sendMessage(msg)
                    
            elif "peak" in msg.text.lower():
                    msg.contentType = 7
                    msg.text = "Kamu peak"
                    arif.sendText(msg.to, "Kamu peak")
                    msg.contentMetadata={'STKID': '27695296',
                                        'STKPKGID': '1900619',
                                        'STKVER': '100'}                    
                    arif.sendMessage(msg)
                    
            elif "hbd" in msg.text.lower():
                    msg.contentType = 7
                    msg.text = "Selamat ulang tahun"
                    arif.sendText(msg.to, "Selamat ulang tahun")
                    msg.contentMetadata={'STKID': '257',
                                        'STKPKGID': '3',
                                        'STKVER': '100'}                    
                    arif.sendMessage(msg)
                    
            elif "sepi" in msg.text.lower():
                  if msg.from_ in creator + admin:
                     group = arif.getGroup(msg.to)
                     nama = [contact.mid for contact in group.members]
                     nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                     if jml <= 100:
                        summon(msg.to, nama)
                     if jml > 100 and jml < 200:
                        for i in range(0, 99):
                            nm1 += [nama[i]]
                        summon(msg.to, nm1)
                        for j in range(100, len(nama)-1):
                            nm2 += [nama[j]]
                        summon(msg.to, nm2)
                     if jml > 200  and jml < 500:
                        for i in range(0, 99):
                            nm1 += [nama[i]]
                        summon(msg.to, nm1)
                        for j in range(100, 199):
                            nm2 += [nama[j]]
                        summon(msg.to, nm2)
                        for k in range(200, 299):
                            nm3 += [nama[k]]
                        summon(msg.to, nm3)
                        for l in range(300, 399):
                            nm4 += [nama[l]]
                        summon(msg.to, nm4)
                        for m in range(400, len(nama)-1):
                            nm5 += [nama[m]]
                        summon(msg.to, nm5)
                     if jml > 500:
                         print ("Terlalu Banyak Men 500+") 
                     cnt = Message()
                     cnt.text = "Jumlah:\n" + str(jml) +  " Members"
                     cnt.to = msg.to
                     arif.sendMessage(cnt)        
#--------------------------------------------------------
            elif "Contact " in msg.text:
              if msg.from_ in creator + admin:
                mmid = msg.text.replace("Contact ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                arif.sendMessage(msg)
            elif msg.text in ["Allprotect:on"]:
              if msg.from_ in creator + admin:
                if wait["protect"] == True:
                    if wait["lang"] == "JP":
                        arif.sendText(msg.to,"Protection Enable 􀜁􀇔􏿿✔")
                    else:
                        arif.sendText(msg.to,"Hal ini sudah terbuka ✔")
                else:
                    wait["protect"] = True
                    if wait["lang"] == "JP":
                        arif.sendText(msg.to,"Protection Enable􀜁✔􀇔􏿿")
                    else:
                        arif.sendText(msg.to,"It is already On ✔")
                if wait["linkprotect"] == True:
                    if wait["lang"] == "JP":
                        arif.sendText(msg.to,"Link Protection Enable 􀜁􀇔􏿿✔")
                    else:
                        arif.sendText(msg.to,"Hal ini sudah terbuka ✔")
                else:
                    wait["linkprotect"] = True
                    if wait["lang"] == "JP":
                        arif.sendText(msg.to,"Link Protect Enable􀜁􏿿")
                    else:
                        arif.sendText(msg.to,"It is already On ô€¨")
                if wait["inviteprotect"] == True:
                    if wait["lang"] == "JP":
                        arif.sendText(msg.to,"Invite Protect Enable 􀜁􀇔􏿿✔")
                    else:
                        arif.sendText(msg.to,"Hal ini sudah terbuka ✔")
                else:
                    wait["inviteprotect"] = True
                    if wait["lang"] == "JP":
                        arif.sendText(msg.to,"Invite Protect Enable􀜁􀇔􏿿")
                    else:
                        arif.sendText(msg.to,"It is already On ¨")
                    if msg.to in wait['pname']:
                        arif.sendText(msg.to,"TURN ON")
                    else:
                        arif.sendText(msg.to,"ALREADY ON")
                        wait['pname'][msg.to] = True
                        wait['pro_name'][msg.to] = arif.getGroup(msg.to).name
                if wait["cancelprotect"] == True:
                    if wait["lang"] == "JP":
                        arif.sendText(msg.to,"Cancel Protection Enable 􀜁􀇔􏿿✔")
                    else:
                        arif.sendText(msg.to,"Hal ini sudah terbuka ✔")
                else:
                    wait["cancelprotect"] = True
                    if wait["lang"] == "JP":
                        arif.sendText(msg.to,"already ON􀜁􀇔􏿿✔")
                    else:
                        arif.sendText(msg.to,"It is already On ✔")
#=====================================================================================
            elif msg.text in ["Allprotect:off"]:
              if msg.from_ in creator + admin:
                if wait["protect"] == False:
                    if wait["lang"] == "JP":
                        arif.sendText(msg.to,"Protection Disable ✔")
                    else:
                        arif.sendText(msg.to,"sudah dimatikan ✔")
                else:
                    wait["protect"] = False
                    if wait["lang"] == "JP":
                        arif.sendText(msg.to,"already close")
                    else:
                        arif.sendText(msg.to,"It is already open ✔")
                if wait["linkprotect"] == False:
                    if wait["lang"] == "JP":
                        arif.sendText(msg.to,"Link Protection Disable ✖")
                    else:
                        arif.sendText(msg.to,"sudah dimatikan ✖")
                else:
                    wait["linkprotect"] = False
                    if wait["lang"] == "JP":
                        arif.sendText(msg.to,"already close✖")
                    else:
                        arif.sendText(msg.to,"It is already open ✔")
                if wait["inviteprotect"] == False:
                    if wait["lang"] == "JP":
                        arif.sendText(msg.to,"Invite Protection Disable ✖")
                    else:
                        arif.sendText(msg.to,"sudah dimatikan ✖")
                else:
                    wait["inviteprotect"] = False
                    if wait["lang"] == "JP":
                        arif.sendText(msg.to,"already close✖")
                    else:
                        arif.sendText(msg.to,"It is already open ✔")
                    if msg.to in wait['pname']:
                        arif.sendText(msg.to,"TURN OFF")
                        del wait['pname'][msg.to]
                    else:
                        arif.sendText(msg.to,"ALREADY OFF")
                if wait["cancelprotect"] == False:
                    if wait["lang"] == "JP":
                        arif.sendText(msg.to,"Cancel Protection Disable ✖")
                    else:
                        arif.sendText(msg.to,"sudah dimatikan ✖")
                else:
                    wait["cancelprotect"] = False
                    if wait["lang"] == "JP":
                        arif.sendText(msg.to,"already close✖")
                    else:
                        arif.sendText(msg.to,"It is already open ✔")  

#=====================================================================================   
            elif msg.text.lower() == 'contact:on':
              if msg.from_ in creator + admin:
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        arif.sendText(msg.to,"Sudah On")
                    else:
                        arif.sendText(msg.to,"It is already open")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        arif.sendText(msg.to,"already open ✔")
                    else:
                        arif.sendText(msg.to,"It is already open 􀜁􀇔􏿿")
            elif msg.text.lower() == 'contact:off':
              if msg.from_ in creator + admin:
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        arif.sendText(msg.to,"sudah off ✖")
                    else:
                        arif.sendText(msg.to,"It is already off ✖")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        arif.sendText(msg.to,"off already")
                    else:
                        arif.sendText(msg.to,"already Close ✔")
            elif msg.text in ["Pro:on"]:
              if msg.from_ in creator + admin:
                if wait["protect"] == True:
                    if wait["lang"] == "JP":
                        arif.sendText(msg.to,"Protection Enable 􀜁??􏿿✔")
                    else:
                        arif.sendText(msg.to,"Hal ini sudah terbuka ✔")
                else:
                    wait["protect"] = True
                    if wait["lang"] == "JP":
                        arif.sendText(msg.to,"Protection Enable􀜁✔􀇔􏿿")
                    else:
                        arif.sendText(msg.to,"It is already On ✔")
            elif msg.text in ['Prolink:on']:
              if msg.from_ in creator + admin:
                if wait["linkprotect"] == True:
                    if wait["lang"] == "JP":
                        arif.sendText(msg.to,"Link Protection Enable 􀜁􀇔􏿿✔")
                    else:
                        arif.sendText(msg.to,"Hal ini sudah terbuka ✔")
                else:
                    wait["linkprotect"] = True
                    if wait["lang"] == "JP":
                        arif.sendText(msg.to,"Link Protect Enable􀜁􏿿")
                    else:
                        arif.sendText(msg.to,"It is already On ô€¨")
            elif msg.text in ['Proinvite:on']:
              if msg.from_ in creator + admin:
                if wait["inviteprotect"] == True:
                    if wait["lang"] == "JP":
                        arif.sendText(msg.to,"Invite Protect Enable 􀜁􀇔􏿿✔")
                    else:
                        arif.sendText(msg.to,"Hal ini sudah terbuka ✔")
                else:
                    wait["inviteprotect"] = True
                    if wait["lang"] == "JP":
                        arif.sendText(msg.to,"Invite Protect Enable􀜁􀇔􏿿")
                    else:
                        arif.sendText(msg.to,"It is already On ¨")
            elif msg.text in ['Procancel:on']:
              if msg.from_ in creator + admin:
                if wait["cancelprotect"] == True:
                    if wait["lang"] == "JP":
                        arif.sendText(msg.to,"Cancel Protection Enable 􀜁􀇔􏿿✔")
                    else:
                        arif.sendText(msg.to,"Hal ini sudah terbuka ✔")
                else:
                    wait["cancelprotect"] = True
                    if wait["lang"] == "JP":
                        arif.sendText(msg.to,"already ON􀜁􀇔􏿿✔")
                    else:
                        arif.sendText(msg.to,"It is already On ✔")
            elif msg.text.lower() == 'join:on':
              if msg.from_ in creator + admin:
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        arif.sendText(msg.to,"Ini sudah on􀜁􀇔􏿿✔")
                    else:
                        arif.sendText(msg.to,"Hal ini sudah terbuka ✔")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        arif.sendText(msg.to,"already ON􀜁􀇔􏿿✔")
                    else:
                        arif.sendText(msg.to,"It is already On ✔")
            elif msg.text.lower() == 'blocklist':
              if msg.from_ in creator + admin:
                blockedlist = arif.getBlockedContactIds()
                arif.sendText(msg.to, "Please wait...")
                kontak = arif.getContacts(blockedlist)
                num=1
                msgs="✖User Blocked List✖\n"
                for ids in kontak:
                    msgs+="\n%i. %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n\nTotal %i blocked user(s)" % len(kontak)
                arif.sendText(msg.to, msgs)
            elif msg.text.lower() == 'join:off':
              if msg.from_ in creator + admin:
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        arif.sendText(msg.to,"Auto Join Already Off✔")
                    else:
                        arif.sendText(msg.to,"Auto Join set off✔")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        arif.sendText(msg.to,"already close✔")
                    else:
                        arif.sendText(msg.to,"It is already open ✔")
            elif msg.text in ["Pro:off"]:
              if msg.from_ in creator + admin:
                if wait["protect"] == False:
                    if wait["lang"] == "JP":
                        arif.sendText(msg.to,"Protection Disable ✔")
                    else:
                        arif.sendText(msg.to,"sudah dimatikan ✔")
                else:
                    wait["protect"] = False
                    if wait["lang"] == "JP":
                        arif.sendText(msg.to,"already close")
                    else:
                        arif.sendText(msg.to,"It is already open ✔")
            elif msg.text in ["Prolink:off"]:
              if msg.from_ in creator + admin:
                if wait["linkprotect"] == False:
                    if wait["lang"] == "JP":
                        arif.sendText(msg.to,"Link Protection Disable ✖")
                    else:
                        arif.sendText(msg.to,"sudah dimatikan ✖")
                else:
                    wait["linkprotect"] = False
                    if wait["lang"] == "JP":
                        arif.sendText(msg.to,"already close✖")
                    else:
                        arif.sendText(msg.to,"It is already open ✔")
            elif msg.text in ["Proinvite:off"]:
              if msg.from_ in creator + admin:
                if wait["inviteprotect"] == False:
                    if wait["lang"] == "JP":
                        arif.sendText(msg.to,"Invite Protection Disable ✖")
                    else:
                        arif.sendText(msg.to,"sudah dimatikan ✖")
                else:
                    wait["inviteprotect"] = False
                    if wait["lang"] == "JP":
                        arif.sendText(msg.to,"already close✖")
                    else:
                        arif.sendText(msg.to,"It is already open ✔")
            elif msg.text in ["Procancel:off"]:
              if msg.from_ in creator + admin:
                if wait["cancelprotect"] == False:
                    if wait["lang"] == "JP":
                        arif.sendText(msg.to,"Cancel Protection Disable ✖")
                    else:
                        arif.sendText(msg.to,"sudah dimatikan ✖")
                else:
                    wait["cancelprotect"] = False
                    if wait["lang"] == "JP":
                        arif.sendText(msg.to,"already close✖")
                    else:
                        arif.sendText(msg.to,"It is already open ✔")
            elif "Join:" in msg.text:
              if msg.from_ in creator + admin:
                try:
                    strnum = msg.text.replace("Join:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            arif.sendText(msg.to,"Itu off undangan ditolak✖\nSilakan kirim dengan menentukan jumlah orang ketika Anda menghidupkan✖")
                        else:
                            arif.sendText(msg.to,"Off undangan ditolak✖Sebutkan jumlah terbuka ketika Anda ingin mengirim")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            arif.sendText(msg.to,strnum + "Kelompok berikut yang diundang akan ditolak secara otomatis✔")
                        else:
                            arif.sendText(msg.to,strnum + "The team declined to create the following automatic invitation")
                except:
                    if wait["lang"] == "JP":
                        arif.sendText(msg.to,"")
                    else:
                        arif.sendText(msg.to,"Weird value✖")
            elif msg.text in ["Leave:on"]:
              if msg.from_ in creator + admin:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        arif.sendText(msg.to,"on􀇔􏿿✔")
                    else:
                        arif.sendText(msg.to,"Sudah terbuka 􀜁􀇔✔􏿿")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        arif.sendText(msg.to,"Done􀜁􀇔􏿿✔")
                    else:
                        arif.sendText(msg.to,"Is already open􀇔􏿿✔")
            elif msg.text in ["Leave:off"]:
              if msg.from_ in creator + admin:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        arif.sendText(msg.to,"off􀜁􀇔􏿿✖")
                    else:
                        arif.sendText(msg.to,"Sudah off??􀇔􏿿✖")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        arif.sendText(msg.to,"Done􀇔??✔")
                    else:
                        arif.sendText(msg.to,"Is already close􀇔􏿿✔")
            elif msg.text in ["Share:on"]:
              if msg.from_ in creator + admin:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        arif.sendText(msg.to,"Done ??􀇔􏿿✔")
                    else:
                        arif.sendText(msg.to,"Hal ini sudah terbuka ✖")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        arif.sendText(msg.to,"on ✔")
                    else:
                        arif.sendText(msg.to,"on ✔")
            elif msg.text in ["Share:off"]:
              if msg.from_ in creator + admin:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        arif.sendText(msg.to,"Done􀇔􏿿✔")
                    else:
                        arif.sendText(msg.to,"It is already turned off 􀜁??􏿿✔")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        arif.sendText(msg.to,"Off ✖")
                    else:
                        arif.sendText(msg.to,"Off ✖")
            elif msg.text.lower() == 'set':
              if msg.from_ in creator + admin:
                md = "┏━━「 ǞЯiբisƮiբiκ」━━┓\n┃━━━━━━━━━━━━━┃\n"
                if wait["likeOn"] == True: md+="┃☆┃Like:ON⏩📳\n"
                else: md+="┃☆┃Like:OFF⏩📴\n"
                if wait["wcOn"] == True: md+="┃☆┃Welcome:ON⏩📳\n"
                else: md+="┃☆┃Welcome:OFF⏩📴\n"
                if wait["leftOn"] == True: md+="┃☆┃Left:ON⏩📳\n"
                else: md+="┃☆┃Left:OFF⏩📴\n"
                if wait["detectMention"] == True: md+="┃☆┃Respon:ON⏩📳\n"
                else: md +="┃☆┃Respon:OFF⏩📴\n"
                if wait["stickerMention"] == True: md+="┃☆┃Stickertag:ON⏩📳\n"
                else: md +="┃☆┃Stickertag:OFF⏩📴\n"
                if settings["simiSimi"] == True: md+="┃☆┃Simisimi:ON⏩📳\n"
                else: md+="┃☆┃Simisimi:OFF⏩📴\n"
                if wait["alwayRead"] == True: md+="┃☆┃Auto read:ON⏩📳\n"
                else: md+="┃☆┃Auto read:OFF⏩📴\n"
                if wait["Sider"] == True: md+="┃☆┃Sider:ON⏩📳\n"
                else: md+="┃☆┃Sider:OFF⏩📴\n"
                if wait["kickMention"] == True: md+="┃☆┃Notag:ON⏩📳\n"
                else:md+="┃☆┃Notag:OFF⏩📴\n"
                if wait["contact"] == True: md+="┃☆┃Contact:ON⏩📳\n"
                else: md+="┃☆┃Contact:OFF⏩📴\n"
                if wait["autoJoin"] == True: md+="┃☆┃Join:ON⏩📳\n"
                else: md +="┃☆┃Join:OFF⏩📴\n"
                if wait["autoCancel"]["on"] == True:md+="┃☆┃Cancel:" + str(wait["autoCancel"]["members"]) + "⏩📳\n"
                else: md+= "┃☆┃Cancel:OFF⏩📴\n"
                if wait["leaveRoom"] == True: md+="┃☆┃Leave:ON⏩📳\n"
                else: md+="┃☆┃Leave:OFF⏩📴\n"
                if wait["timeline"] == True: md+="┃☆┃Share:ON⏩📳\n"
                else:md+="┃☆┃Share:OFF⏩📴\n"
                if wait["autoAdd"] == True: md+="┃☆┃Add:ON⏩📳\n"
                else:md+="┃☆┃Add:OFF⏩📴\n"
                if wait["commentOn"] == True: md+="┃☆┃Com:ON⏩📳\n"
                else:md+="┃☆┃Com:OFF⏩📴\n┃━┃❨◄━━━►❩\n┃☆┃◄━PROTECTION━►\n┃━┃━ARIFISTIFIK━╣\n"
                if wait["protect"] == True: md+="┃☆┃Pro:ON⏩📳\n"
                else:md+="┃☆┃Pro:OFF⏩📴\n"
                if wait["linkprotect"] == True: md+="┃☆┃ProtectQr:ON⏩📳\n"
                else:md+="┃☆┃ProtectQr:OFF⏩📴\n"
                if wait["inviteprotect"] == True: md+="┃☆┃Proinvite:ON⏩📳\n"
                else:md+="┃☆┃Proinvite:OFF⏩📴\n"
                if wait["cancelprotect"] == True: md+"┃☆┃Procancel:ON⏩📳\n"
                else:md+="┃☆┃Procancel:OFF⏩📴\n"
                if wait["pname"] == True: md+="┃☆┃Namelock:ON⏩📳\n"
                else: md+="┃☆┃Namelock:OFF⏩📴\n"   
                if wait["Ghost"] == True: md+="┃☆┃Ghost:ON⏩📳\n"
                else: md+="┃☆┃Ghost:OFF⏩📴\n"
                arif.sendText(msg.to,md + "┃━━━━━━━━━━━━┃\n┗━━「 ǞЯiբisƮiբiκ」━━╯")
            elif "Creatorgrup" == msg.text:
                try:
                    group = arif.getGroup(msg.to)
                    GS = group.creator.mid
                    M = Message()
                    M.to = msg.to
                    M.contentType = 13
                    M.contentMetadata = {'mid': GS}
                    GS = arif.getContact(msg.to)
                    arif.sendMessage(M)
                except:
                    W = group.members[0].mid
                    M = Message()
                    M.to = msg.to
                    M.contentType = 13
                    M.contentMetadata = {'mid': W}
                    arif.sendMessage(M)
                    W = arif.getContact(msg.to)
                    arif.sendText(msg.to,"old user")
            elif cms(msg.text,["Add"]):
                msg.contentType = 13
                msg.contentMetadata = {'mid': 'u65224f4e8812136f01b25275a54b5aef'}
                arif.sendText(msg.to,"❂•••••••••✧••••••••••❂")
                arif.sendMessage(msg)
            elif "Tagme: " in msg.text:
              if msg.from_ in creator + admin:
                c = msg.text.replace("Tagme: ","")
                if c in [""," ","\n",None]:
                    arif.sendText(msg.to,"Is a string that can not be changed✔")
                else:
                    wait["tagme"] = c
                    arif.sendText(msg.to,"✨This has been changed✨\n\n" + c)
            elif "Welcome " in msg.text:
                c = msg.text.replace("Welcome ","")
                if c in [""," ","\n",None]:
                    arif.sendText(msg.to,"Is a string that can not be changed✔")
                else:
                    wait["joingc"] = c
                    arif.sendText(msg.to,"✨This has been changed✨\n\n" + c)
            elif "Left " in msg.text:
                c = msg.text.replace("Left ","")
                if c in [""," ","\n",None]:
                    arif.sendText(msg.to,"Is a string that can not be changed✔")
                else:
                    wait["leftgc"] = c
                    arif.sendText(msg.to,"✨This has been changed✨\n\n" + c)
            elif "Sider: " in msg.text:
                c = msg.text.replace("Sider: ","")
                if c in [""," ","\n",None]:
                    arif.sendText(msg.to,"Is a string that can not be changed✔")
                else:
                    wait["sider1"] = c
                    arif.sendText(msg.to,"✨This has been changed✨\n\n" + c)
            elif "Setrespon: " in msg.text:
              if msg.from_ in creator + admin:
                c = msg.text.replace("Setrespon: ","")
                if c in [""," ","\n",None]:
                    arif.sendText(msg.to,"Is a string that can not be changed✔")
                else:
                    wait["responName"] = c
                    arif.sendText(msg.to,"✨This has been changed✨\n\n" + c)
            elif "Cekresponse" in msg.text:
              if msg.from_ in creator + admin:
            	arif.sendText(msg.to,"👇Respon saat di tag👇\n" + wait["tagme"])
            	arif.sendText(msg.to,"👇Respon saat di add👇\n" + wait["comment"])
            	arif.sendText(msg.to,"👇Respon saat member join👇\n" + wait["joingc"])
            	arif.sendText(msg.to,"👇Respon saat member left👇\n" + wait["leftgc"])
            	arif.sendText(msg.to,"👇Respon saat member readchat👇\n" + wait["sider1"])
            	arif.sendText(msg.to,"👇Respon saat member memanggil👇\n" + wait["responName"])
            	arif.sendText(msg.to,"👇Respon di autolike👇\n" + wait["comment1"] + "\n\nHAL INI TIDAK DAPAT DI UBAH SESUAI HAK CIPTA\nCREATOR::ARIFISTIFIK")
            elif msg.text in ["Left:on"]:
              if msg.from_ in creator + admin:
                if wait["leftOn"] == True:
                    if wait["lang"] == "JP":
                        arif.sendText(msg.to,"Done")
                else:
                    wait["leftOn"] = True
                    if wait["lang"] == "JP":
                        arif.sendText(msg.to,"Already")
            elif msg.text in ["Left:off"]:
              if msg.from_ in creator + admin:
                if wait["leftOn"] == False:
                    if wait["lang"] == "JP":
                        arif.sendText(msg.to,"Done")
                else:
                    wait["leftOn"] = False
                    if wait["lang"] == "JP":
                        arif.sendText(msg.to,"Already") 
            elif msg.text in ["Welcome:on"]:
              if msg.from_ in creator + admin:
                if wait['wcOn'] == True:
                    if wait["lang"] == "JP": 
                        arif.sendText(msg.to,"sudah ON")
                else:
                    wait["wcOn"] = True
                    if wait["lang"] == "JP":
                        arif.sendText(msg.to,"already ON")
            elif msg.text in ["Welcome:off"]:
              if msg.from_ in creator + admin:
                if wait['wcOn'] == False:
                    if wait["lang"] == "JP":
                        arif.sendText(msg.to,"Sudah off")
                else:
                    wait['wcOn'] = False
                    if wait["lang"] == "JP":
                        arif.sendText(msg.to,"already OFF")
            elif msg.text.lower() == 'group id':
              if msg.from_ in creator + admin:
                gid = arif.getGroupIdsJoined()
                h = "❂•••••••••L I S T  I D  G R O U P••••••••••❂\n "
                for i in gid:
                    h += "[%s]:%s\n" % (arif.getGroup(i).name,i)
                arif.sendText(msg.to,h)
            elif msg.text in ["Gcancelall"]:
              if msg.from_ in creator + admin:
                gid = arif.getGroupIdsInvited()
                for i in gid:
                    arif.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    arif.sendText(msg.to,"Success menolak semua undangan")
                else:
                    arif.sendText(msg.to,"He declined all invitations")
            elif msg.text in ["Add:on","Add auto on"]:
              if msg.from_ in creator + admin:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        arif.sendText(msg.to,"Already On✔")
                    else:
                        arif.sendText(msg.to,"Already On✔")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        arif.sendText(msg.to,"Already On✔")
                    else:
                        arif.sendText(msg.to,"Already On✔")
            elif msg.text in ["Add:off","Add auto off"]:
              if msg.from_ in creator + admin:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        arif.sendText(msg.to,"Hal ini sudah off✖")
                    else:
                        arif.sendText(msg.to,"Hal ini sudah dimatikan✖")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        arif.sendText(msg.to,"Already Off✖")
                    else:
                        arif.sendText(msg.to,"Untuk mengaktifkan-off✖")
            elif "Message set:" in msg.text:
              if msg.from_ in creator + admin:
                wait["message"] = msg.text.replace("Message set:","")
                arif.sendText(msg.to,"✨We changed the message✨")
            elif "Help set:" in msg.text:
              if msg.from_ in creator + admin:
                wait["help"] = msg.text.replace("Help set:","")
                arif.sendText(msg.to,"✨We changed the Help✨")
            elif "Msg add-" in msg.text:
              if msg.from_ in creator + admin:
                wait["message"] = msg.text.replace("Pesan add-","")
                if wait["lang"] == "JP":
                    arif.sendText(msg.to,"✨Kami mengubah pesan✨")
                else:
                    arif.sendText(msg.to,"Change information")
            elif msg.text in ["Pesan add cek","Message confirm"]:
              if msg.from_ in creator + admin:
                if wait["lang"] == "JP":
                    arif.sendText(msg.to,"Additional information is automatically set to the following \n\n" + wait["message"])
                else:
                    arif.sendText(msg.to,"Pesan tambahan otomatis telah ditetapkan sebagai berikut \n\n" + wait["message"])
            elif msg.text in ["Change","change"]:
              if msg.from_ in creator + admin:
                if wait["lang"] =="JP":
                    wait["lang"] = "TW"
                    arif.sendText(msg.to,"I changed the language to engglis✔")
                else:
                    wait["lang"] = "JP"
                    arif.sendText(msg.to,"I changed the language to indonesia✔")
            elif "Message set: " in msg.text:
              if msg.from_ in creator + admin:
                c = msg.text.replace("Message set: ","")
                if c in [""," ","\n",None]:
                    arif.sendText(msg.to,"Is a string that can not be changed✔")
                else:
                    wait["comment"] = c
                    arif.sendText(msg.to,"✨This has been changed✨\n\n" + c)
            elif msg.text in ["Comment:on","Com:on","Comment on"]:
              if msg.from_ in creator + admin:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        arif.sendText(msg.to,"Aku berada di✔")
                    else:
                        arif.sendText(msg.to,"To open✔")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        arif.sendText(msg.to,"✔")
                    else:
                        arif.sendText(msg.to,"✔")
            elif msg.text in ["Com:off"]:
              if msg.from_ in creator + admin:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        arif.sendText(msg.to,"Hal ini sudah off ✖")
                    else:
                        arif.sendText(msg.to,"It is already turned off ✖")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        arif.sendText(msg.to,"Off✖")
                    else:
                        arif.sendText(msg.to,"To turn off✖")
            elif msg.text in ["Com","Comment"]:
              if msg.from_ in creator + admin:
                arif.sendText(msg.to,"✨Auto komentar saat ini telah ditetapkan sebagai berikut✨\n\n" + str(wait["comment"]))
            elif msg.text in ["Glink","Url"]:
              if msg.from_ in creator + admin:
                if msg.toType == 2:
                    g = arif.getGroup(msg.to)
                    if g.preventJoinByTicket == True:
                        g.preventJoinByTicket = False
                        arif.updateGroup(g)
                    gurl = arif.reissueGroupTicket(msg.to)
                    arif.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        arif.sendText(msg.to,"Hal ini tidak dapat digunakan di luar kelompok")
                    else:
                        arif.sendText(msg.to,"Tidak dapat digunakan untuk kelompok selain")
            elif "gurl+" in msg.text:
              if msg.from_ in creator + admin:
                if msg.toType == 2:
                    gid = msg.text.replace("gurl+","")
                    gurl = arif.reissueGroupTicket(gid)
                    arif.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    arif.sendText(msg.to,"ã‚°ãƒ«ãƒ¼ãƒ—ä»¥å¤–ã§ã¯ä½¿ç”¨ã§ãã¾ã›ã‚“👈")

            elif "gurl" in msg.text:
              if msg.from_ in creator + admin:
                if msg.toType == 1:
                    tid = msg.text.replace("gurl","")
                    turl = ki.getUserTicket(tid)
                    ki.sendText(msg.to,"line://ti/p" + turl)
                else:
                    ki.sendText(msg.to,"error")

            elif msg.text in ["Gurl"]:
              if msg.from_ in creator + admin:
                if msg.toType == 2:
                    x = arif.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        arif.updateGroup(x)
                    gurl = arif.reissueGroupTicket(msg.to)
                    arif.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        arif.sendText(msg.to,"Can't be used outside the group")
                    else:
                        arif.sendText(msg.to,"Not for use less than group")
#                else:
#                    arif.sendText(msg.to,"Tidak dapat digunakan untuk kelompok selain")
            elif msg.text in ["Comban"]:
              if msg.from_ in creator + admin:
                wait["wblack"] = True
                arif.sendText(msg.to,"Please send contacts from the person you want to add to the blacklist…”✚")
            elif msg.text in ["Comban del"]:
              if msg.from_ in creator + admin:
                wait["dblack"] = True
                arif.sendText(msg.to,"Please send contacts from the person you want to add from the blacklist…”✚")
            elif msg.text in ["Comban cek"]:
              if msg.from_ in creator + admin:
                if wait["commentBlack"] == {}:
                    arif.sendText(msg.to,"Nothing in the blacklist✖")
                else:
                    arif.sendText(msg.to,"The following is a blacklist✔")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "ãƒ»" +arif.getContact(mi_d).displayName + "\n"
                    arif.sendText(msg.to,mc)
            elif msg.text in ["Like:on","Like on"]:
              if msg.from_ in creator + admin:
                if wait["likeOn"] == True:
                    if wait["lang"] == "JP":
                        arif.sendText(msg.to,"Done")
                else:
                    wait["likeOn"] = True
                    if wait["lang"] == "JP":
                        arif.sendText(msg.to,"Already")
                        
            elif msg.text in ["Like off","Like:off"]:
              if msg.from_ in creator + admin:
                if wait["likeOn"] == False:
                    if wait["lang"] == "JP":
                        arif.sendText(msg.to,"Done")
                else:
                    wait["likeOn"] = False
                    if wait["lang"] == "JP":
                        arif.sendText(msg.to,"Already")
            elif "Namelock:on" in msg.text:
              if msg.from_ in admin + creator:
                    if msg.to in wait['pname']:
                        arif.sendText(msg.to,"TURN ON")
                    else:
                        arif.sendText(msg.to,"ALREADY ON")
                        wait['pname'][msg.to] = True
                        wait['pro_name'][msg.to] = arif.getGroup(msg.to).name
            elif "Namelock:off" in msg.text:
              if msg.from_ in admin or creator:
                    if msg.to in wait['pname']:
                        arif.sendText(msg.to,"TURN OFF")
                        del wait['pname'][msg.to]
                    else:
                        arif.sendText(msg.to,"ALREADY OFF")                        
            elif msg.text in ["Simisimi on","Simisimi:on"]:
                settings["simiSimi"][msg.to] = True
                arif.sendText(msg.to,"BOT SIMISIMI TURN ON")
                ki.sendText(msg.to,"already turn active")
            elif msg.text in ["Simisimi off","Simisimi:off"]:
                settings["simiSimi"][msg.to] = False
                arif.sendText(msg.to,"BOT SIMISIMI TURN OFF")
                ki.sendText(msg.to,"already non active")
            elif msg.text in ["Read on","Read:on"]:
              if msg.from_ in creator + admin:
                if wait['alwayRead'] == True:
                    if wait["alwayRead"] == "JP": 
                        arif.sendText(msg.to,"Auto Sider ON")
                else:
                    wait["alwayRead"] = True
                    if wait["lang"] == "JP":
                        arif.sendText(msg.to,"already ON")
            elif msg.text in ["Read off","Read:off"]:
              if msg.from_ in creator + admin:
                if wait['alwayRead'] == False:
                    if wait["lang"] == "JP":
                        arif.sendText(msg.to,"Auto Sider OFF")
                else:
                    wait['alwayRead'] = False
                    if wait["lang"] == "JP":
                        arif.sendText(msg.to,"already OFF auto read")
            elif msg.text in ["Deletechat"]:
              if msg.from_ in creator + admin:
                if wait['Removechat'] == True:
                    if wait["Removechat"] == "JP": 
                        arif.sendText(msg.to,"Success!!!")
                if wait['Removechat'] == False:
                    if wait["lang"] == "JP":
                        pass
            elif "Sider on" in msg.text:
	#      if msg.toType == 2:
                try:
                    del cctv['point'][msg.to]
                    del cctv['sidermem'][msg.to]
                    del cctv['cyduk'][msg.to]
                except:
                    pass
                cctv['point'][msg.to] = msg.id
                cctv['sidermem'][msg.to] = ""
                cctv['cyduk'][msg.to]=True
                wait["Sider"] = True
                arif.sendText(msg.to,"Siap On Cek Sider")
            elif "Sider off" in msg.text:
	#      if msg.toType == 2:
                if msg.to in cctv['point']:
                    cctv['cyduk'][msg.to]=False
                    wait["Sider"] = False
                    arif.sendText(msg.to, "Cek Sider Off")
                else:
                    arif.sendText(msg.to, "Heh Belom Di Set")
            elif msg.text in ["Autorespon on","Autorespon:on","Respon on","Respon:on"]:
              if msg.from_ in creator + admin:
                if wait["detectMention"] == True:
                    if wait["lang"] == "JP":
                        arif.sendText(msg.to,"Auto Respon ON")
                else:
                    wait["detectMention"] = True
                    if wait["lang"] == "JP":
                        arif.sendText(msg.to,"already ON")
            elif msg.text in ["Autorespon off","Autorespon:off","Respon off","Respon:off"]:
              if msg.from_ in creator + admin:
                if wait["detectMention"] == False:
                    if wait["lang"] == "JP":
                        arif.sendText(msg.to,"Auto Respon OFF")
                else:
                    wait["detectMention"] = False
                    if wait["lang"] == "JP":
                        arif.sendText(msg.to,"already OFF")
            elif msg.text in ["Notag:on"]:
              if msg.from_ in creator + admin:
                if wait["kickMention"] == True:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"☠️DANGER TAG KICK ON☠️")
                else:
                    wait["kickMention"] = True
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"already ON")
            elif msg.text in ["Notag:off"]:
              if msg.from_ in creator + admin:
                if wait["kickMention"] == False:
                   if wait["lang"] == "JP":
                        ki.sendText(msg.to,"SELF PROTECT TAG OFF ✔")
                else:
                    wait["kickMention"] = False
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"already turn OF")
            elif msg.text.lower() == 'Clock:on':
              if msg.from_ in creator + admin:
                if wait["clock"] == True:
                    arif.sendText(msg.to,"Sudah On")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = arif.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    arif.updateProfile(profile)
                    arif.sendText(msg.to,"Jam on✔")
            elif msg.text in ["Stickertag:on"]:
              if msg.from_ in creator + admin:
                if wait["stickerMention"] == True:
                    if wait["lang"] == "JP":
                        arif.sendText(msg.to,"sudah on")
                else:
                    wait["stickerMention"] = True
                    if wait["lang"] == "JP":
                        arif.sendText(msg.to,"already ON")
            elif msg.text in ["Stickertag:off"]:
              if msg.from_ in creator + admin:
                if wait["stickerMention"] == False:
                    if wait["lang"] == "JP":
                        arif.sendText(msg.to,"sudah off")
                else:
                    wait["stickerMention"] = False
                    if wait["lang"] == "JP":
                        arif.sendText(msg.to,"already OFF")
            elif msg.text.lower() == 'Clock:off':
              if msg.from_ in creator + admin:
                if wait["clock"] == False:
                    arif.sendText(msg.to,"Hal ini sudah off✖")
                else:
                    wait["clock"] = False
                    arif.sendText(msg.to," Dimatikan ✔")
            elif "Clockname " in msg.text:
              if msg.from_ in creator + admin:
                n = msg.text.replace("Jam say ","")
                if len(n.decode("utf-8")) > 30:
                    arif.sendText(msg.to,"terlalu lama")
                else:
                    wait["cName"] = n
                    arif.sendText(msg.to,"Ini telah diubah✔\n\n" + n)
            elif msg.text in ["Translate"]:
					if wait["lang"] == "JP":
						arif.sendText(msg.to,translateMessage)
					else:
						arif.sendText(msg.to,helpt)
            elif msg.text.lower() == 'update':
              if msg.from_ in creator + admin:
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = arif.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    arif.updateProfile(profile)
                    arif.sendText(msg.to,"Diperbarui✔")
                else:
                    arif.sendText(msg.to,"✨Silahkan Aktifkan Nama✨")
            elif ("Fuck " in msg.text):
              if msg.from_ in creator + admin:
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           arif.kickoutFromGroup(msg.to,[target])
                       except:
                           arif.sendText(msg.to,"Error")
            elif ("Kick1 " in msg.text):
                if msg.from_ in creator + admin:
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           ki.kickoutFromGroup(msg.to,[target])
                       except:
                           ki.sendText(msg.to,"Error")
            elif ("Kick2 " in msg.text):
                if msg.from_ in creator + admin:
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           arif.kickoutFromGroup(msg.to,[target])
                       except:
                           arif.sendText(msg.to,"Error")
            elif ("Kick3 " in msg.text):
                if msg.from_ in creator + admin:
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           arif.kickoutFromGroup(msg.to,[target])
                       except:
                           arif.sendText(msg.to,"Error")
            elif ("Kick4 " in msg.text):
                if msg.from_ in creator + admin:
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           arif.kickoutFromGroup(msg.to,[target])
                       except:
                           arif.sendText(msg.to,"Error")
            elif ("Kick5 " in msg.text):
                if msg.from_ in creator + admin:
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           arif.kickoutFromGroup(msg.to,[target])
                       except:
                           arif.sendText(msg.to,"Error")
            elif ("Kick6 " in msg.text):
                if msg.from_ in creator + admin:
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           arif.kickoutFromGroup(msg.to,[target])
                       except:
                           arif.sendText(msg.to,"Error")
            elif ("Kick7 " in msg.text):
                if msg.from_ in creator + admin:
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           arif.kickoutFromGroup(msg.to,[target])
                       except:
                           arif.sendText(msg.to,"Error")
            elif ("Kick8 " in msg.text):
                if msg.from_ in creator + admin:
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           arif.kickoutFromGroup(msg.to,[target])
                       except:
                           arif.sendText(msg.to,"Error")
            elif ("Kick9 " in msg.text):
                if msg.from_ in creator + admin:
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           arif.kickoutFromGroup(msg.to,[target])
                       except:
                           arif.sendText(msg.to,"Error")
            elif ("Sc " in msg.text):
                if msg.from_ in creator + admin:
                   key = eval(msg.contentMetadata["MENTION"])
                   key1 = key["MENTIONEES"][0]["M"]
                   key = arif.getContact(key1)
                   arif.sendText(msg.to,"" +  key1)

            elif "Bro " in msg.text:
                if msg.from_ in creator + admin:
                       nk0 = msg.text.replace("Bro ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = arif.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    random.choice(KAC).kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    arif.sendText(msg.to,"Good Bye")
#-----------------------------------------------------------
            elif ("Bye " in msg.text):
              if msg.from_ in creator + admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      random.choice(KAC).kickoutFromGroup(msg.to,[target])
                   except:
                      pass


            elif ("Ban " in msg.text):
              if msg.from_ in creator + admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      wait["blacklist"][target] = True
                      f=codecs.open('st2__b.json','w','utf-8')
                      json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                      arif.sendText(msg.to,"Succes Banned")
                   except:
                      pass

            elif msg.text in ["Mygroups"]:
              if msg.from_ in creator + admin:
                 gid = arif.getGroupIdsJoined()
                 h = ""
                 for i in gid:
                  h += "[⛓️] %s \n" % (arif.getGroup(i).name + " | 🗜️Members : " + str(len (arif.getGroup(i).members)))
                 arif.sendText(msg.to, "☆「Group List」☆\n"+ h +"🗜️Total Group : " +str(len(gid)))

#----------------------------------------------------------
            elif "Unban @" in msg.text:
              if msg.from_ in creator + admin:
                if msg.toType == 2:
                    print "[Unban]ok"
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip()
                    gs = arif.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        arif.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                arif.sendText(msg.to,"Target Unlocked")
                            except:
                                arif.sendText(msg.to,"Error")

            elif "Ban:" in msg.text:
                if msg.from_ in creator + admin:
                       nk0 = msg.text.replace("Ban:","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = arif.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
									wait["blacklist"][target] = True
									f=codecs.open('st2__b.json','w','utf-8')
									json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
									arif.sendText(msg.to,"Target Locked")
                                except:
                                    arif.sendText(msg.to,"Error")

            elif "Unban:" in msg.text:
                if msg.from_ in creator + admin:
                       nk0 = msg.text.replace("Unban:","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = arif.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
									del wait["blacklist"][target]
									f=codecs.open('st2__b.json','w','utf-8')
									json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
									arif.sendText(msg.to,"Target Unlocked")
                                except:
                                    arif.sendText(msg.to,"Error")
            elif "Papay " in msg.text:
              if msg.from_ in creator:
                ulti0 = msg.text.replace("Papay ","")
                ulti1 = ulti0.rstrip()
                ulti2 = ulti1.replace("@","")
                ulti3 = ulti2.rstrip()
                _name = ulti3
                gs = arif.getGroup(msg.to)
                ginfo = arif.getGroup(msg.to)
                gs.preventJoinByTicket = False
                arif.updateGroup(gs)
                invsend = 0
                Ticket = arif.reissueGroupTicket(msg.to)
                ghost.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.2)
                targets = []
                for s in gs.members:
                        if _name in s.displayName:
                                targets.append(s.mid)
                if targets ==[]:
                        sendMessage(msg.to,"user does not exist")
                        pass
                else:
                        for target in targets:
                                try:
                                        ghost.kickoutFromGroup(msg.to,[target])
                                        ghost.leaveGroup(msg.to)
                                        print (msg.to,[g.mid])
                                except:
                                        ghost.sendText(msg.t,"Ter ELIMINASI....")
                                        ghost.sendText(msg.to,"WOLES brooo....!!!")
                                        ghost.leaveGroup(msg.to)
                                        gs = arif.getGroup(msg.to)
                                        gs.preventJoinByTicket = True
                                        arif.updateGroup(gs)
                                        gs.preventJoinByTicket(gs)
                                        arif.updateGroup(gs)
            elif "Cleanse" in msg.text:
	      if msg.from_ in creator:
                if msg.toType == 2:
                    print "ok cleanse"
                    _name = msg.text.replace("Cleanse","")
                    gs = ki.getGroup(msg.to)
                    gs = arif.getGroup(msg.to)
                    arif.sendText(msg.to,"Maaf group kami sita (^_^) ")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        arif.sendText(msg.to,"you are not admin")
                    else:
                        for target in targets:
                          if not target in Bots:
                            if not target in admin:
                              if not target in admsa:
                                if not target in creator:
                                    try:
                                     klist=[ki,arif]
                                     kicker=random.choice(klist)
                                     kicker.kickoutFromGroup(msg.to,[target])
                                     print (msg.to,[g.mid])
                                    except:
                                     arif.sendText(msg.to,"Group cleanse")
            elif "Id " in msg.text:
                msgg = msg.text.replace("Id ",'')
                conn = arif.findContactsByUserid(msgg)
                if True:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': conn.mid}
                    arif.sendText(msg.to,"http://line.me/ti/p/~" + msgg)
                    arif.sendMessage(msg)
#_________________________________________________________________________
            elif 'ig ' in msg.text.lower():
              #if msg.from_ in admin:
                try:
                    instagram = msg.text.lower().replace("ig ","")
                    html = requests.get('https://www.instagram.com/' + instagram + '/?')
                    soup = BeautifulSoup(html.text, 'html5lib')
                    data = soup.find_all('meta', attrs={'property':'og:description'})
                    text = data[0].get('content').split()
                    data1 = soup.find_all('meta', attrs={'property':'og:image'})
                    text1 = data1[0].get('content').split()
                    user = "Name: " + text[-2] + "\n"
                    user1 = "Username: " + text[-1] + "\n"
                    followers = "Followers: " + text[0] + "\n"
                    following = "Following: " + text[2] + "\n"
                    post = "Post: " + text[4] + "\n"
                    link = "Link: " + "https://www.instagram.com/" + instagram
                    detail = "======INSTAGRAM INFO USER======\n"
                    details = "\n======INSTAGRAM INFO USER======"
                    arif.sendText(msg.to, detail + user + user1 + followers + following + post + link + details)
                    arif.sendImageWithURL(msg.to, text1[0])
                except Exception as njer:
                	arif.sendText(msg.to, str(njer))
            elif "Image " in msg.text:
                search = msg.text.replace("Image ","")
                url = 'https://www.google.com/search?espv=2&biw=1366&bih=667&tbm=isch&oq=kuc&aqs=mobile-gws-lite.0.0l5&q=' + search
                raw_html = (download_page(url))
                items = []
                items = items + (_images_get_all_items(raw_html))
                path = random.choice(items)
                print path
                try:
                    arif.sendImageWithURL(msg.to,path)
                except:
                    pass
            elif msg.text in ["Kalender","Time","Waktu"]:
                       tz = pytz.timezone("Asia/Jakarta")
                       timeNow = datetime.now(tz=tz)
                       day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                       hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                       bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                       hr = timeNow.strftime("%A")
                       bln = timeNow.strftime("%m")
                       for i in range(len(day)):
                           if hr == day[i]: hasil = hari[i]
                       for k in range(0, len(bulan)):
                           if bln == str(k): bln = bulan[k-1]
                       rst = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                       arif.sendText(msg.to, rst)
#==============================================================================#

                
            elif msg.text.lower() == 'runtime':
                eltime = time.time() - mulai
                van = "Bot has been active "+waktu(eltime)
                arif.sendText(msg.to,van) 
                
            elif "Getvid @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Getvid @","")
                _nametarget = _name.rstrip('  ')
                gs = arif.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    arif.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = arif.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            arif.sendVideoWithURL(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]dp executed"
            elif "Getcontact" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]                
                mmid = arif.getContact(key1)
                msg.contentType = 13
                msg.contentMetadata = {"mid": key1}
                arif.sendMessage(msg)
            elif "Getname" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = arif.getContact(key1)
                cu = arif.channel.getCover(key1)
                try:
                    arif.sendText(msg.to, "===[DisplayName]===\n" + contact.displayName)
                except:
                    arif.sendText(msg.to, "===[DisplayName]===\n" + contact.displayName)
            elif msg.text in ["Myname"]:
                    h = arif.getContact(msg.from_)
                    arif.sendText(msg.to,"===[DisplayName]===\n" + h.displayName)
            elif msg.text in ["Mybio"]:
                    h = arif.getContact(msg.from_)
                    arif.sendText(msg.to,"===[StatusMessage]===\n" + h.statusMessage)
            elif msg.text in ["Mypict"]:
                    h = arif.getContact(msg.from_)
                    arif.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
            elif msg.text in ["Myvid"]:
                    h = arif.getContact(msg.from_)
                    arif.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
            elif msg.text in ["Urlpict"]:
                    h = arif.getContact(msg.from_)
                    arif.sendText(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
            elif msg.text in ["Mycover"]:
                    h = arif.getContact(msg.from_)
                    cu = arif.channel.getCover(msg.from_)          
                    path = str(cu)
                    arif.sendImageWithURL(msg.to, path)
            elif msg.text in ["Urlcover"]:
                    h = arif.getContact(msg.from_)
                    cu = arif.channel.getCover(msg.from_)          
                    path = str(cu)
                    arif.sendText(msg.to, path)
            elif "Getmid @" in msg.text:
                _name = msg.text.replace("Getmid @","")
                _nametarget = _name.rstrip(' ')
                gs = arif.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        arif.sendText(msg.to, g.mid)
                    else:
                        pass
            elif "Setimage: " in msg.text:
              if msg.from_ in creator + admin:
                wait["pap"] = msg.text.replace("Setimage: ","")
                arif.sendText(msg.to, "Pap telah di Set")
            elif msg.text in ["Papimage","Papim","Pap"]:
              if msg.from_ in creator + admin:
                arif.sendImageWithURL(msg.to,wait["pap"])
            elif "Setvideo: " in msg.text:
              if msg.from_ in creator + admin:
                wait["pap"] = msg.text.replace("Setvideo: ","")
                arif.sendText(msg.to,"Video Has Ben Set To")
            elif msg.text in ["Papvideo","Papvid"]:
              if msg.from_ in creator + admin:
                arif.sendVideoWithURL(msg.to,wait["pap"])
#=========================
#-----------------------------------------------------------
            elif msg.text == "Check":
                    arif.sendText(msg.to, "Check Yang nyimak")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    now2 = datetime.now()
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.strftime(now2,"%H:%M")
                    wait2['ROM'][msg.to] = {}
                    print wait2
                    
            elif "Cctv" in msg.text:
                subprocess.Popen("echo '' > dataSeen/"+msg.to+".txt", shell=True, stdout=subprocess.PIPE)
                #arif.sendText(msg.to, "Checkpoint checked!")
                arif.sendText(msg.to, "Set the lastseens' point(｀・ω・´)\n\n" + datetime.now().strftime('%H:%M:%S'))
                print "Setlastpoint"

            elif "Ciduk" in msg.text:
	        lurkGroup = ""
	        dataResult, timeSeen, contacts, userList, timelist, recheckData = [], [], [], [], [], []
                with open('dataSeen/'+msg.to+'.txt','r') as rr:
                    contactArr = rr.readlines()
                    for v in xrange(len(contactArr) -1,0,-1):
                        num = re.sub(r'\n', "", contactArr[v])
                        contacts.append(num)
                        pass
                    contacts = list(set(contacts))
                    for z in range(len(contacts)):
                        arg = contacts[z].split('|')
                        userList.append(arg[0])
                        timelist.append(arg[1])
                    uL = list(set(userList))
                    for ll in range(len(uL)):
                        try:
                            getIndexUser = userList.index(uL[ll])
                            timeSeen.append(time.strftime("%H:%M:%S", time.localtime(int(timelist[getIndexUser]) / 1000)))
                            recheckData.append(userList[getIndexUser])
                        except IndexError:
                            conName.append('nones')
                            pass
                    contactId = arif.getContacts(recheckData)
                    for v in range(len(recheckData)):
                        dataResult.append(contactId[v].displayName + ' ('+timeSeen[v]+')')
                        pass
                    if len(dataResult) > 0:
                        tukang = "┏━━━━━━━━━━━━━━━━━━━━━━━━━\n┃         ☆☞ LIST JONES ☜☆\n┣━━━━━━━━━━━━━━━━━━━━━━━━━\n┣♦"
                        grp = '\n┣♦ '.join(str(f) for f in dataResult)
                        total = '\n┣━━━━━━━━━━━━━━━━━━━━━━━━━\n┣♦ Total %i Jones (%s)' % (len(dataResult), datetime.now().strftime('%H:%M:%S')) + "\n┗━━━━━━━━━━━━━━━━━━━━━━━━━"
                        msg.contentType = 7
                        msg.text = ""
                        msg.contentMetadata={'STKID': '27695301',
                                            'STKPKGID': '1900619',
                                            'STKVER': '100'}                                        
                        arif.sendText(msg.to, "%s %s %s" % (tukang, grp, total))
                        subprocess.Popen("echo '' > dataSeen/"+msg.to+".txt", shell=True, stdout=subprocess.PIPE)
                        arif.sendText(msg.to, "☆Jones Nongol☆")  
                        arif.sendMessage(msg)
                    else:
                        arif.sendText(msg.to, "☆Belum Ada Jones☆")
                    print "Viewseen"

            elif 'copy ' in msg.text.lower():
              if msg.from_ in creator + admin:
                if msg.toType == 2:
                    red = re.compile(re.escape('copy '),re.IGNORECASE)
                    tname = red.sub('',msg.text)
                    tname = tname.lstrip()
                    tname = tname.replace(" @","$spliter$")
                    tname = tname.rstrip()
                    tname = tname.split("$spliter$")
                    tname = tname[0]
                    tname = tname[1:]
                    clist = {
                        "Founded":False,
                        "displayName":"",
                        "statusMessage":"",
                        "pictureStatus":""
                    }
                    mems = arif.getGroup(msg.to).members
                    for targ in mems:
                        if targ.displayName == tname:
                            clist["displayName"] = targ.displayName
                            clist["statusMessage"] = targ.statusMessage
                            clist["pictureStatus"] = targ.pictureStatus
                            clist["Founded"] = True
                    if clist["Founded"]:
                        wait["selfStatus"] = False
                        me = arif.getProfile()
                        me.displayName = clist["displayName"]
                        me.statusMessage = clist["statusMessage"]
                        me.pictureStatus = clist["pictureStatus"]
                        arif.updateDisplayPicture(me.pictureStatus)
                        arif.updateProfile(me)
                        arif.sendText(msg.to,"Done")
                    else:
                        arif.sendText(msg.to,"Done")

            elif "Urlpict @" in msg.text:
              if msg.from_ in creator + admin:
                print "[Command]dp executing"
                _name = msg.text.replace("Urlpict @","")
                _nametarget = _name.rstrip(' ')
                gs = arif.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    arif.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = arif.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            arif.sendText(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]dp executed"
            elif "Urlcover @" in msg.text:
              if msg.from_ in creator + admin:
                print "[Command]cover executing"
                _name = msg.text.replace("Urlcover @","")
                _nametarget = _name.rstrip(' ')
                gs = arif.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    arif.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = arif.getContact(target)
                            cu = arif.channel.getCover(target)
                            path = str(cu)
                            arif.sendText(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]cover executed"
            elif msg.text in ["Conban","Contactban","Contact ban"]:
              if msg.from_ in creator + admin:
                if wait["blacklist"] == {}:
                    arif.sendText(msg.to,"Tidak Ada kontak blacklist")
                else:
                    arif.sendText(msg.to,"━━━━━━━━━List Blacklist━━━━━━━━")
                    h = ""
                    for i in wait["blacklist"]:
                        h = arif.getContact(i)
                        M = Message()
                        M.to = msg.to
                        M.contentType = 13
                        M.contentMetadata = {'mid': i}
                        arif.sendMessage(M)

#-------------------------------------------------
	    elif "Spam @" in msg.text:
	      if msg.from_ in creator:
                _name = msg.text.replace("Spam @","")
                _nametarget = _name.rstrip(' ')
                gs = arif.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
		       arif.sendText(msg.to,"Wating in progres...")
                       arif.sendText(g.mid,"Your Account Has Been Spammed !")
                       arif.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       arif.sendText(g.mid,"Your Account Has Been Spammed !")
		       arif.sendText(g.mid,"Your Account Has Been Spammed !")
                       arif.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       arif.sendText(g.mid,"Your Account Has Been Spammed !")
		       arif.sendText(g.mid,"Your Account Has Been Spammed !")
                       arif.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       arif.sendText(g.mid,"Your Account Has Been Spammed !")
	  	       arif.sendText(g.mid,"Your Account Has Been Spammed !")
                       arif.sendText(g.mid,"Your Account Has Been Spammed !")
                       arif.sendText(g.mid,"Your Account Has Been Spammed !")
                       arif.sendText(g.mid,"Your Account Has Been Spammed !")
		       arif.sendText(g.mid,"Your Account Has Been Spammed !")
                       arif.sendText(g.mid,"Your Account Has Been Spammed !")
                       arif.sendText(g.mid,"Your Account Has Been Spammed !")
                       arif.sendText(g.mid,"Your Account Has Been Spammed !")
		       arif.sendText(g.mid,"Your Account Has Been Spammed !")
		       arif.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
		       arif.sendText(g.mid,"Your Account Has Been Spammed !")
                       arif.sendText(g.mid,"Your Account Has Been Spammed !")
                       arif.sendText(g.mid,"Your Account Has Been Spammed !")
                       arif.sendText(g.mid,"Your Account Has Been Spammed !")
		       arif.sendText(g.mid,"Your Account Has Been Spammed !")
                       arif.sendText(g.mid,"Your Account Has Been Spammed !")
		       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
		       arif.sendText(g.mid,"Your Account Has Been Spammed !")
                       arif.sendText(g.mid,"Your Account Has Been Spammed !")
                       arif.sendText(g.mid,"Your Account Has Been Spammed !")
                       arif.sendText(g.mid,"Your Account Has Been Spammed !")
		       arif.sendText(g.mid,"Your Account Has Been Spammed !")
		       arif.sendText(g.mid,"Your Account Has Been Spammed !")
                       arif.sendText(g.mid,"Your Account Has Been Spammed !")
		       arif.sendText(g.mid,"Your Account Has Been Spammed !")
		       arif.sendText(g.mid,"Your Account Has Been Spammed !")
                       arif.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
		       arif.sendText(g.mid,"Your Account Has Been Spammed !")
                       arif.sendText(g.mid,"Your Account Has Been Spammed !")
                       arif.sendText(g.mid,"Your Account Has Been Spammed !")
		       arif.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       arif.sendText(g.mid,"Your Account Has Been Spammed !")
                       arif.sendText(g.mid,"Your Account Has Been Spammed !")
                       arif.sendText(g.mid,"Your Account Has Been Spammed !")
                       arif.sendText(g.mid,"Your Account Has Been Spammed !")
                       arif.sendText(g.mid,"Your Account Has Been Spammed !")
                       arif.sendText(g.mid,"Your Account Has Been Spammed !")
                       arif.sendText(g.mid,"Your Account Has Been Spammed !")
                       arif.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       arif.sendText(g.mid,"Your Account Has Been Spammed !")
                       arif.sendText(g.mid,"Your Account Has Been Spammed !")
                       arif.sendText(g.mid,"Your Account Has Been Spammed !")
                       arif.sendText(g.mid,"Your Account Has Been Spammed !")
                       arif.sendText(g.mid,"Your Account Has Been Spammed !")
                       arif.sendText(g.mid,"Your Account Has Been Spammed !")
                       arif.sendText(g.mid,"Your Account Has Been Spammed !")
                       arif.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       arif.sendText(g.mid,"Your Account Has Been Spammed !")
                       arif.sendText(g.mid,"Your Account Has Been Spammed !")
                       arif.sendText(g.mid,"Your Account Has Been Spammed !")
                       arif.sendText(g.mid,"Your Account Has Been Spammed !")
                       arif.sendText(g.mid,"Your Account Has Been Spammed !")
                       arif.sendText(g.mid,"Your Account Has Been Spammed !")
                       arif.sendText(g.mid,"Your Account Has Been Spammed !")
                       arif.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       arif.sendText(g.mid,"Your Account Has Been Spammed !")
                       arif.sendText(g.mid,"Your Account Has Been Spammed !")
                       arif.sendText(g.mid,"Your Account Has Been Spammed !")
                       arif.sendText(g.mid,"Your Account Has Been Spammed !")
                       arif.sendText(g.mid,"Your Account Has Been Spammed !")
                       arif.sendText(g.mid,"Your Account Has Been Spammed !")
                       arif.sendText(g.mid,"Your Account Has Been Spammed !")
                       arif.sendText(g.mid,"Your Account Has Been Spammed !")
		       arif.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       arif.sendText(g.mid,"Your Account Has Been Spammed !")
                       arif.sendText(g.mid,"Your Account Has Been Spammed !")
                       arif.sendText(g.mid,"Your Account Has Been Spammed !")
                       arif.sendText(g.mid,"Your Account Has Been Spammed !")
                       arif.sendText(g.mid,"Your Account Has Been Spammed !")
                       arif.sendText(g.mid,"Your Account Has Been Spammed !")
                       arif.sendText(g.mid,"Your Account Has Been Spammed !")
                       arif.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       arif.sendText(g.mid,"Your Account Has Been Spammed !")
                       arif.sendText(g.mid,"Your Account Has Been Spammed !")
                       arif.sendText(g.mid,"Your Account Has Been Spammed !")
                       arif.sendText(g.mid,"Your Account Has Been Spammed !")
                       arif.sendText(g.mid,"Your Account Has Been Spammed !")
                       arif.sendText(g.mid,"Your Account Has Been Spammed !")
                       arif.sendText(g.mid,"Your Account Has Been Spammed !")
                       arif.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       arif.sendText(g.mid,"Your Account Has Been Spammed !")
                       arif.sendText(g.mid,"Your Account Has Been Spammed !")
                       arif.sendText(g.mid,"Your Account Has Been Spammed !")
                       arif.sendText(g.mid,"Your Account Has Been Spammed !")
                       arif.sendText(g.mid,"Your Account Has Been Spammed !")
                       arif.sendText(g.mid,"Your Account Has Been Spammed !")
                       arif.sendText(g.mid,"Your Account Has Been Spammed !")
                       arif.sendText(g.mid,"Your Account Has Been Spammed !")
                       arif.sendText(msg.to, "Succes")
                       print " Spammed !"
#--------------------------------------------------------------------------
#-----------------------------------------------------------
            elif "Mban:" in msg.text:
              if msg.from_ in creator + admin:
                midd = msg.text.replace("Mban:","")
                wait["blacklist"][midd] = True
		arif.sendText(msg.to,"Target Lock")
#-----------------------------------------------------------
            elif "#leave" in msg.text:
                try:
                    import sys
                    sys.exit()
                except:
                    pass
#-----------------------------------------------------------
            elif "/Spam " in msg.text:
              if msg.from_ in creator + admin:
                txt = msg.text.split(" ")
                jmlh = int(txt[2])
                text = msg.text.replace("/Spam "+str(txt[1])+" "+str(jmlh)+" ","")
                tulisan = jmlh * (text+"\n")
                if txt[1] == "on":
                    if jmlh <= 10000:
                        for x in range(jmlh):
                            ki.sendText(msg.to, text)
                    else:
                        arif.sendText(msg.to, "Out Of Range!")
                elif txt[1] == "off":
                    if jmlh <= 10000:
                        ki.sendText(msg.to, tulisan)
                    else:
                        arif.sendText(msg.to, "Out Of Range!")
            elif ("Micadd " in msg.text):
              if msg.from_ in creator + admin:
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        mimic["target"][target] = True
                        arif.sendText(msg.to,"Target ditambahkan!")
                        break
                    except:
                        arif.sendText(msg.to,"Fail !")
                        break
                    
            elif ("Micdel " in msg.text):
              if msg.from_ in creator + admin:
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        del mimic["target"][target]
                        arif.sendText(msg.to,"Target dihapuskan!")
                        break
                    except:
                        arif.sendText(msg.to,"Fail !")
                        break
                    
            elif msg.text in ["Miclist"]:
              if msg.from_ in creator + admin:
                        if mimic["target"] == {}:
                            arif.sendText(msg.to,"nothing")
                        else:
                            mc = "Target mimic user\n"
                            for mi_d in mimic["target"]:
                                mc += "?? "+arif.getContact(mi_d).displayName + "\n"
                            arif.sendText(msg.to,mc)

            elif "Mimic target " in msg.text:
              if msg.from_ in creator + admin:
                        if mimic["copy"] == True:
                            siapa = msg.text.replace("Mimic target ","")
                            if siapa.rstrip(' ') == "me":
                                mimic["copy2"] = "me"
                                arif.sendText(msg.to,"Mimic change to me")
                            elif siapa.rstrip(' ') == "target":
                                mimic["copy2"] = "target"
                                arif.sendText(msg.to,"Mimic change to target")
                            else:
                                arif.sendText(msg.to,"I dont know")
            
            elif "Mimic " in msg.text:
              if msg.from_ in creator + admin:
                cmd = msg.text.replace("Mimic ","")
                if cmd == "on":
                    if mimic["status"] == False:
                        mimic["status"] = True
                        arif.sendText(msg.to,"Reply Message on")
                    else:
                        arif.sendText(msg.to,"Sudah on")
                elif cmd == "off":
                    if mimic["status"] == True:
                        mimic["status"] = False
                        arif.sendText(msg.to,"Reply Message off")
                    else:
                        arif.sendText(msg.to,"Sudah off")
            elif "Grupname" in msg.text:
              if msg.from_ in creator + admin:
                saya = msg.text.replace('Grupname','')
                gid = arif.getGroup(msg.to)
                arif.sendText(msg.to, "[Nama Grup : ]\n" + gid.name)
            
            elif "Gid" in msg.text:
                saya = msg.text.replace('Gid','')
                gid = arif.getGroup(msg.to)
                arif.sendText(msg.to, "[ID Grup : ]\n" + gid.id)
            elif msg.text in ["Friendlist"]:  
              if msg.from_ in creator:
                contactlist = arif.getAllContactIds()
                kontak = arif.getContacts(contactlist)
                num=1
                msgs="━━━━━━━━━List Friend━━━━━━━━━"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n━━━━━━━━━List Friend━━━━━━━━━\n\nTotal Friend : %i" % len(kontak)
                arif.sendText(msg.to, msgs)
                
            elif msg.text in ["Memlist"]:   
              if msg.from_ in creator + admin:
                kontak = arif.getGroup(msg.to)
                group = kontak.members
                num=1
                msgs="━━━━━━━━━List Member━━━━━━━━━-"
                for ids in group:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n━━━━━━━━━List Member━━━━━━━━━\n\nTotal Members : %i" % len(group)
                arif.sendText(msg.to, msgs)
               
                
            elif msg.text in ["Friendlistmid"]: 
              if msg.from_ in creator + admin:
                gruplist = arif.getAllContactIds()
                kontak = arif.getContacts(gruplist)
                num=1
                msgs="━━━━━━━━━List FriendMid━━━━━━━━━"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.mid)
                    num=(num+1)
                msgs+="\n━━━━━━━━━List FriendMid━━━━━━━━━\n\nTotal Friend : %i" % len(kontak)
                arif.sendText(msg.to, msgs)
                    
#-----------------------------------------------
            elif "lurk on" == msg.text.lower():
                if msg.to in wait2['readPoint']:
                        try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                        except:
                            pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        with open('sider.json', 'w') as fp:
                         json.dump(wait2, fp, sort_keys=True, indent=4)
                         arif.sendText(msg.to,"Lurking already on")
                else:
                    try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                    except:
                          pass
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                    wait2['ROM'][msg.to] = {}
                    with open('sider.json', 'w') as fp:
                     json.dump(wait2, fp, sort_keys=True, indent=4)
                     arif.sendText(msg.to, "Set reading point:\n" + datetime.now().strftime('%H:%M:%S'))
                     print wait2

                    
            elif "lurk off" == msg.text.lower():
                if msg.to not in wait2['readPoint']:
                    arif.sendText(msg.to,"Lurking already off")
                else:
                    try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                    except:
                          pass
                    arif.sendText(msg.to, "Delete reading point:\n" + datetime.now().strftime('%H:%M:%S'))


                    
            elif "lurkers" == msg.text.lower():
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                             arif.sendText(msg.to, "Lurkers:\nNone")
                        else:
                            chiya = []
                            for rom in wait2["ROM"][msg.to].items():
                                chiya.append(rom[1])
                               
                            cmem = arif.getContacts(chiya)
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = 'Lurkers:\n'
                        for x in range(len(cmem)):
                                xname = str(cmem[x].displayName)
                                pesan = ''
                                pesan2 = pesan+"@a\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                zx2.append(zx)
                                zxc += pesan2
                                msg.contentType = 0
           
                        print zxc
                        msg.text = xpesan+ zxc + "\nLurking time: %s\nCurrent time: %s"%(wait2['setTime'][msg.to],datetime.now().strftime('%H:%M:%S'))
                        lol ={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                        print lol
                        msg.contentMetadata = lol
                        try:
                          arif.sendMessage(msg)
                        except Exception as error:
                              print error
                        pass
               
                    else:
                        arif.sendText(msg.to, "Lurking has not been set.")           

            elif msg.text in ["Bl:on"]:
              if msg.from_ in creator + admin:
                wait["wblacklist"] = True
                arif.sendText(msg.to,"Send Contact")
            elif msg.text in ["Unbl:on"]:
              if msg.from_ in creator + admin:
                wait["dblacklist"] = True
                arif.sendText(msg.to,"Send Contact")
            elif msg.text.lower() == 'mcheck':
              if msg.from_ in creator + admin:
                if wait["blacklist"] == {}:
                    arif.sendText(msg.to,"􀜁􀇔􏿿 Nothing in the blacklist")
                else:
                    arif.sendText(msg.to,"􀜁􀇔􏿿 following is a blacklist")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "�" +arif.getContact(mi_d).displayName + "\n"
                    arif.sendText(msg.to,mc)
 #---------Fungsi Banlist With Tag--------#
            elif msg.text in ["Banlist","ip banlist"]:
              if msg.from_ in creator + admin:
                if wait["blacklist"] == {}:
                    arif.sendText(msg.to,"No user is Blacklisted")
                else:
                    ki.sendText(msg.to,"Blacklisted user")
                    mc = " 🛡️====||B L A C K L I S T||====🛡️\n"
                    for mi_d in wait["blacklist"]:
                        mc += "🗜️" +arif.getContact(mi_d).displayName + "\n"
                    arif.sendText(msg.to,mc)
                    
                    print "[Command]Banlist executed"
            elif msg.text in ["Clearban"]:
              if msg.from_ in creator + admin:
                if msg.toType == 2:
                   wait["blacklist"] = {}
                   arif.sendText(msg.to,"clear all blacklist")
                   ki.sendText(msg.to,"done ✔")
                   arif.sendText(msg.to,"done ✔")
                   ki.sendText(msg.to,"blacklist done all removed 👮")
            elif msg.text.lower() == 'kick@mbl':
              if msg.from_ in creator + admin:
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        ki.sendText(msg.to,"Daftar hitam pengguna tidak memiliki")
                        return
                    for jj in matched_list:
                        try:
                            arif.kickoutFromGroup(msg.to,[jj])
                            ki.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass
#-----------------------------------------------

#---------------------------------------------------
            elif "Pict @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Pict @","")
                _nametarget = _name.rstrip(' ')
                gs = arif.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    arif.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = arif.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            arif.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"
#---------------------------------------------------
#---------------------------------------------------
            elif msg.text in ["Recopy"]:
              if msg.from_ in creator + admin:
                try:
                    arif.updateDisplayPicture(mybackup.pictureStatus)
                    arif.updateProfile(mybackup)
                    arif.sendText(msg.to, "Success")
                except Exception as e:
                    arif.sendText(msg.to, str (e))
#-----------------------------------------------------------------------
            elif "Youtube " in msg.text:
                try:
                    textToSearch = (msg.text).replace("Youtube ", "").strip()
                    query = urllib.quote(textToSearch)
                    url = "https://www.youtube.com/results?search_query=" + query
                    response = urllib2.urlopen(url)
                    html = response.read()
                    soup = BeautifulSoup(html, "html.parser")
                    results = soup.find(attrs={'class':'yt-uix-tile-link'})
                    arif.sendText(msg.to,'https://www.youtube.com' + results['href'])
                except:
                    arif.sendText(msg.to,"Could not find it")
            elif "Youtubesearch " in msg.text:
                    query = msg.text.replace("Youtubesearch ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        url = 'http://www.youtube.com/results'
                        params = {'search_query': query}
                        r = s.get(url, params=params)
                        soup = BeautifulSoup(r.content, 'html5lib')
                        hasil = ""
                        for a in soup.select('.yt-lockup-title > a[title]'):
                            if '&list=' not in a['href']:
                                hasil += ''.join((a['title'],'\nUrl : http://www.youtube.com' + a['href'],'\n\n'))
                        arif.sendText(msg.to,hasil)
                        print '[Command] Youtube Search'
                        
#------------------------------------------------
            elif "Getinfo" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = arif.getContact(key1)
                cu = arif.channel.getCover(key1)
                try:
                    arif.sendText(msg.to,"~Nama\n" + contact.displayName + "\n~Mid\n" + contact.mid + "\n~Bio\n" + contact.statusMessage + "\n~Profile Picture\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n~Header\n" + str(cu))
                except:
                    arif.sendText(msg.to,"~Nama\n" + contact.displayName + "\n~Mid\n" + contact.mid + "\n~Bio\n" + contact.statusMessage + "\n~Profile Picture\n" + str(cu))
            
            elif "Getbio" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = arif.getContact(key1)
                cu = arif.channel.getCover(key1)
                try:
                    arif.sendText(msg.to,contact.statusMessage)
                except:
                    arif.sendText(msg.to,contact.statusMessage)
            elif "Gimage" in msg.text:
					group = arif.getGroup(msg.to)
					path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
					arif.sendImageWithURL(msg.to,path)
            
            elif "Getprofile @" in msg.text:            
                print "[Command]dp executing"
                _name = msg.text.replace("Getprofile @","")
                _nametarget = _name.rstrip('  ')
                gs = arif.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    arif.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = arif.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            arif.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"
                
            elif "Dosa " in msg.text:
                tanya = msg.text.replace("Dosa ","")
                jawab = ("60%","70%","80%","90%","100%","Tak terhingga")
                jawaban = random.choice(jawab)
                arif.sendText(msg.to,"Dosanya " + tanya + " adalah " + jawaban + "\nBanyak banyak tobat Nak")
                
            elif "Pahala " in msg.text:
                tanya = msg.text.replace("Pahala ","")
                jawab = ("0%","20%","40%","50%","60%","Tak ada")
                jawaban = random.choice(jawab)
                arif.sendText(msg.to,"Pahalanya " + tanya + " adalah " + jawaban + "\nTobatlah nak")
                
            elif "Apakah " in msg.text:
                apk = msg.text.replace("Apakah ","")
                rnd = ["Iya","Tidak","Bisa Jadi","Mungkin","Pikir Sendiri Coy","Meneketehe","Iya Kayaknya","Maebi Yes Maebi No"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                arif.sendAudio(msg.to,"hasil.mp3")
                
            elif "Kapan " in msg.text:
                apk = msg.text.replace("Kapan ","")
                rnd = ["kapan kapan","besok","satu abad lagi","Hari ini","Tahun depan","Minggu depan","Bulan depan","Sebentar lagi","Tidak Akan Pernah"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                arif.sendAudio(msg.to,"hasil.mp3")
                
            elif "Hari " in msg.text:
                apk = msg.text.replace("Hari ","")
                rnd = ["Senin","Selasa","Rabu","Kamis","Jumat","Sabtu","Minggu"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                arif.sendAudio(msg.to,"hasil.mp3")
                
            elif msg.text in ["Auto like"]:
                wait["likeOn"] = True
                arif.sendText(msg.to,"Share Post Kamu Yang Mau Di Like!")
                
            elif "Say " in msg.text:
                say = msg.text.replace("Say ","")
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                arif.sendAudio(msg.to,"hasil.mp3")
                
            elif msg.text.lower() in ["hi","hai","halo","hallo"]:
                    beb = "Hai Beb 😘 " +arif.getContact(msg.from_).displayName + " 􀸂􀆇starry heart􏿿"
                    arif.sendText(msg.to,beb)    
#------------------------------------------------------------
            elif msg.text in ["Invite"]:
              if msg.from_ in creator + admin:
                wait["invite"] = True
                random.choice(KAC).sendText(msg.to,"send contact 😉")
#------------------------------------------------------------
            elif msg.text in ["Admin","admin"]:
                msg.contentType = 13
                admin1 = "u65224f4e8812136f01b25275a54b5aef"
                admin2 = "ub21eb3d440e0dfd640eef9f2fb5ce02d"
                admin3 = "u782cdf7a9fd2545c84a0cd86f418e9f7"
                admin4 = "ue4e13b0a41d848845489374e671c6861"
                admin5 = "u799da4e06d50e1775cfcff1f3e59df03"
                admin6 = "u00d73ba3e810e651e8c5690723e1b5bf"
                msg.contentMetadata = {'mid': admin1}
                arif.sendMessage(msg)
                msg.contentMetadata = {'mid': admin2}
                arif.sendMessage(msg)
                msg.contentMetadata = {'mid': admin3}
                arif.sendMessage(msg)
                msg.contentMetadata = {'mid': admin4}
                arif.sendMessage(msg)
                msg.contentMetadata = {'mid': admin5}
                arif.sendMessage(msg)
                msg.contentMetadata = {'mid': admin6}
                arif.sendMessage(msg)
                
            elif "Musik " in msg.text:
				songname = msg.text.replace("Musik ","")
				params = {"songname": songname}
				r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
				data = r.text
				data = json.loads(data)
				for song in data:
					abc = song[3].replace('https://','http://')
					arif.sendText(msg.to, "Title : " + song[0] + "\nLength : " + song[1] + "\nLink download : " + song[4])
					arif.sendText(msg.to, "Lagu " + song[0] + "\nSedang Di Prosses... Tunggu Sebentar ^_^ ")
					arif.sendAudioWithURL(msg.to,abc)
					arif.sendText(msg.to, "Selamat Mendengarkan Lagu " + song[0])
						
            elif "Getcover @" in msg.text:
                print "[Command]cover executing"
                _name = msg.text.replace("Getcover @","")    
                _nametarget = _name.rstrip('  ')
                gs = arif.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    arif.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = arif.getContact(target)
                            cu = arif.channel.getCover(target)          
                            path = str(cu)
                            arif.sendImageWithURL(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]cover executed"
            elif msg.text.lower() == 'reboot':
                if msg.from_ in creator + admin:
                    print "[Command]Like executed"
                    try:
                        arif.sendText(msg.to,"Restarting...")
                        restart_program()
                    except:
                        arif.sendText(msg.to,"Please wait")
                        restart_program()
                        pass
            elif "Hay " in msg.text:
                say = msg.text.replace("Hay ","")
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                arif.sendAudio(msg.to,"hasil.mp3")
            elif "Nuke" in msg.text:
              if msg.from_ in creator:
                if msg.toType == 2:
                    print "Nuke ok"
                    _name = msg.text.replace("Nuke","")
                    gs = arif.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        arif.sendText(msg.to,"Limit gw njir..")
                    else:
                        for target in targets:
                          if not target in Bots:
                            try:
                                klist=[arif,ki]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                pass
            elif msg.text in ["Tag","Tagall","Mencret"]:
              if msg.from_ in creator + admin:
                group = arif.getGroup(msg.to)
                k = len(group.members)//500
                for j in xrange(k+1):
                    msg = Message(to=msg.to)
                    txt = u''
                    s=0
                    d=[]
                    for i in group.members[j*500 : (j+1)*500]:
                        d.append({"S":str(s), "E" :str(s+8), "M":i.mid})
                        s += 9
                        txt += u'@Krampus\n'
                    msg.text = txt
                    msg.contentMetadata = {u'MENTION':json.dumps({"MENTIONEES":d})}
                    arif.sendMessage(msg) 
            elif msg.text.lower() == 'in':
                if msg.from_ in creator:
                        G = arif.getGroup(msg.to)
                        ginfo = arif.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        arif.updateGroup(G)
                        invsend = 0
                        Ticket = arif.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        arif.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        G = arif.getGroup(msg.to)
                        ginfo = arif.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        random.choice(KAC).updateGroup(G)

#-----------------------------------------------
            elif msg.text.lower() == 'reinvite':
              if msg.from_ in creator + admin:
                if msg.toType == 2:
                        G = arif.getGroup(msg.to)
                        ginfo = arif.getGroup(msg.to)
                        arif.sendText(msg.to,"waitting...")
                        ki.leaveGroup(msg.to)
                        G.preventJoinByTicket = False
                        arif.updateGroup(G)
                        invsend = 0
                        Ticket = arif.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        arif.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = arif.getGroup(msg.to)
                        ginfo = arif.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)
#-----------------------------------------------
            elif "B1 in" in msg.text:
                if msg.from_ in creator + admin:
                        G = arif.getGroup(msg.to)
                        ginfo = arif.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        arif.updateGroup(G)
                        invsend = 0
                        Ticket = arif.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = arif.getGroup(msg.to)
                        ginfo = arif.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)
#-----------------------------------------------
            elif "B1 in" in msg.text:
                if msg.from_ in creator + admin:
                        G = arif.getGroup(msg.to)
                        ginfo = arif.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        arif.updateGroup(G)
                        invsend = 0
                        Ticket = arif.reissueGroupTicket(msg.to)
                        arif.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = arif.getGroup(msg.to)
                        ginfo = arif.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        arif.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        arif.updateGroup(G)
#------------------------------------------------------------------

            elif msg.text.lower() == 'out':
              if msg.from_ in creator + admin:
                if msg.toType == 2:
                    ginfo = arif.getGroup(msg.to)
                    try:
                        arif.sendText(msg.to,"􀜁􀇔􏿿Bye Bye😘 "  +  str(ginfo.name)  + "")
                        ki.leaveGroup(msg.to)
                        arif.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Bye" in msg.text:
              if msg.from_ in creator + admin:
                if msg.toType == 2:
                    ginfo = arif.getGroup(msg.to)
                    try:
                    	ki.leaveGroup(msg.to)
                        arif.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "B1 bye" in msg.text:
              if msg.from_ in creator + admin:
                if msg.toType == 2:
                    ginfo = arif.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
#-----------------------------------------------
            elif msg.text in ["Welcome","wc","welcome","Wc"]:
                ginfo = arif.getGroup(msg.to)
                msg.contentType = 7
                msg.text = ""
                msg.contentMetadata={'STKID': '247',
                                    'STKPKGID': '3',
                                    'STKVER': '100'}
                arif.sendText(msg.to,"Selamat Datang Di Grup " + str(ginfo.name))
                arif.sendText(msg.to,"Owner Grup " + str(ginfo.name) + " :\n" + ginfo.creator.displayName )
                arif.sendMessage(msg)
            elif msg.text in ["Ghost on"]:
             if msg.from_ in admin:
                wait["Ghost"] = True
                arif.sendText(msg.to,"Ghost Sudah Aktif")
            elif msg.text in ["Ghost off"]:
             if msg.from_ in admin:
                wait["Ghost"] = False
                arif.sendText(msg.to,"Ghost Sudah Di Nonaktifkan")
            elif msg.text in ["Ghost join"]:
		if msg.from_ in admin:
                    G = arif.getGroup(msg.to)
                    ginfo = arif.getGroup(msg.to)
                    G.preventJoinByTicket = False
                    arif.updateGroup(G)
                    invsend = 0
                    Ticket = arif.reissueGroupTicket(msg.to)
                    ghost.acceptGroupInvitationByTicket(msg.to,Ticket)
                    G.preventJoinByTicket = True
                    ghost.updateGroup(G)
            elif "Bc " in msg.text:
              if msg.from_ in creator + admin:
				bctxt = msg.text.replace("Bc ","")
				ki.sendText(msg.to,(bctxt))            

            elif msg.text.lower() == 'ping':
              if msg.from_ in creator + admin:
                arif.sendText(msg.to,"Ping ")
                ki.sendText(msg.to,"Ping 􀜁􀇔􏿿")
                arif.sendText(msg.to,"Ping 􀜁􀇔􏿿")
                
            elif msg.text.lower() == 'ifconfig':
              if msg.from_ in admin + creator:
                    botKernel = subprocess.Popen(["ifconfig"], stdout=subprocess.PIPE).communicate()[0]
                    arif.sendText(msg.to, botKernel + "\n\n===SERVER INFO NetStat===")
            elif msg.text.lower() == 'system':
              if msg.from_ in admin + creator:
                    botKernel = subprocess.Popen(["df","-h"], stdout=subprocess.PIPE).communicate()[0]
                    arif.sendText(msg.to, botKernel + "\n\n===SERVER INFO SYSTEM===")
            elif msg.text.lower() == 'kernel':
              if msg.from_ in admin + creator:
                    botKernel = subprocess.Popen(["uname","-srvmpio"], stdout=subprocess.PIPE).communicate()[0]
                    arif.sendText(msg.to, botKernel + "\n\n===SERVER INFO KERNEL===")
            elif msg.text.lower() == 'cpu':
              if msg.from_ in admin + creator:
                    botKernel = subprocess.Popen(["cat","/proc/cpuinfo"], stdout=subprocess.PIPE).communicate()[0]
                    arif.sendText(msg.to, botKernel + "\n\n===SERVER INFO CPU===")
            elif "ftext " in msg.text.lower():
                txt = msg.text.replace("ftext ", "")
                t1 = "\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xa0\x81\xf4\x80\xa0\x81\xf4\x80\xa0\x81"
                t2 = "\xf4\x80\x82\xb3\xf4\x8f\xbf\xbf"
                arif.sendText(msg.to, t1 + txt + t2)

            elif msg.text.lower() == 'restore':
                    try:
                        arif.updateDisplayPicture(restoreprofile.pictureStatus)
                        arif.updateProfile(restoreprofile)
                        arif.sendText(msg.to, "Success Restore Profile")
                    except Exception as e:
                        arif.sendText(msg.to, str(e))
                    
            elif msg.text.lower() == 'ceksticker on':
                    wait["checkSticker"] = True
                    arif.sendText(msg.to, "Berhasil mengaktifkan Check Details Sticker")
                    
            elif text.lower() == 'ceksticker off':
                    wait["checkSticker"] = False
                    arif.sendText(msg.to, "Berhasil nonaktifkan Check Details Sticker")                    
            
            elif "Video " in msg.text:
                    try:
                        textToSearch = (msg.text).replace("Video ", "").strip()
                        query = urllib.quote(textToSearch)
                        url = "https://www.youtube.com/results?search_query=" + query
                        response = urllib2.urlopen(url)
                        html = response.read()
                        soup = BeautifulSoup(html, "html.parser")
                        results = soup.find(attrs={'class': 'yt-uix-tile-link'})
                        arif.sendVideoWithURL(msg.to,'https://www.youtube.com' + results['href'])
                    except:
                        arif.sendText(msg.to, "Could not find it")                                        

#-----------------------------------------------        
        if op.type == 19:
	 if wait["Ghost"] == True:
          if op.param2 not in admin + creator:
           if op.param2 not in Bots:
               pass
          else:
            try:
              G = arif.getGroup(op.param1)
              G.preventJoinByTicket = False
              arif.updateGroup(G)
              Ticket = arif.reissueGroupTicket(op.param1)
              ghost.acceptGroupInvitationByTicket(op.param1,Ticket)
              time.sleep(0.01)
              ghost.kickoutFromGroup(op.param1,[op.param2])
              c = Message(to=op.param1, from_=None, text=None, contentType=13)
              c.contentMetadata={'mid':op.param2}
              ghost.sendMessage(c)
              ghost.leaveGroup(op.param1)
              G.preventJoinByTicket = True
              arif.updateGroup(G)
              wait["blacklist"][op.param2] = True
            except:
              G = arif.getGroup(op.param1)
              G.preventJoinByTicket = False
              arif.updateGroup(G)
              Ticket = arif.reissueGroupTicket(op.param1)
              ghost.acceptGroupInvitationByTicket(op.param1,Ticket)
              time.sleep(0.01)
              ghost.kickoutFromGroup(op.param1,[op.param2])
              c = Message(to=op.param1, from_=None, text=None, contentType=13)
              c.contentMetadata={'mid':op.param2}
              ghost.sendMessage(c)
              ghost.leaveGroup(op.param1)
              G.preventJoinByTicket = True
              arif.updateGroup(G)
              wait["blacklist"][op.param2] = True
#-----------------------------------------------        
        if op.type == 19:
            try:
                if op.param3 in mid:
                    if op.param2 in kimid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        arif.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        arif.updateGroup(G)
                    else:
                        G = ki.getGroup(op.param1)
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        arif.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        arif.updateGroup(G)
                        ki.updateGroup(G)
                        wait["blacklist"][op.param2] = True
                elif op.param3 in kimid:
                    if op.param2 in mid:
                        G = arif.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        arif.updateGroup(G)
                        Ticket = arif.reissueGroupTicket(op.param1)
                        arif.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        arif.updateGroup(G)
                    else:
                        G = arif.getGroup(op.param1)
                        arif.kickoutFromGroup(op.param1,[op.param2])
                        G.preventJoinByTicket = False
                        arif.updateGroup(G)
                        Ticket = arif.reissueGroupTicket(op.param1)
                        arif.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        arif.updateGroup(G)
                        wait["blacklist"][op.param2] = True
                elif op.param3 in mid:
                    if op.param2 in mid:
                        G = arif.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        arif.updateGroup(G)
                        Ticket = arif.reissueGroupTicket(op.param1)
                        arif.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        arif.updateGroup(G)
                    else:
                        G = arif.getGroup(op.param1)
                        arif.kickoutFromGroup(op.param1,[op.param2])
                        G.preventJoinByTicket = False
                        arif.updateGroup(G)
                        Ticket = arif.reissueGroupTicket(op.param1)
                        arif.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        arif.updateGroup(G)
                        wait["blacklist"][op.param2] = True
                elif op.param3 in mid:
                    if op.param2 in mid:
                        G = arif.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        arif.updateGroup(G)
                        Ticket = arif.reissueGroupTicket(op.param1)
                        arif.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        arif.updateGroup(G)
                    else:
                        G = arif.getGroup(op.param1)
                        arif.kickoutFromGroup(op.param1,[op.param2])
                        G.preventJoinByTicket = False
                        arif.updateGroup(G)
                        Ticket = arif.reissueGroupTicket(op.param1)
                        arif.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        arif.updateGroup(G)
                        wait["blacklist"][op.param2] = True
                elif op.param3 in mid:
                    if op.param2 in mid:
                        G = arif.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        arif.updateGroup(G)
                        Ticket = arif.reissueGroupTicket(op.param1)
                        arif.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        arif.updateGroup(G)
                    else:
                        G = arif.getGroup(op.param1)
                        arif.kickoutFromGroup(op.param1,[op.param2])
                        G.preventJoinByTicket = False
                        arif.updateGroup(G)
                        Ticket = arif.reissueGroupTicket(op.param1)
                        arif.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        arif.updateGroup(G)
                        arif.updateGroup(G)
                        wait["blacklist"][op.param2] = True
                elif op.param3 in mid:
                    if op.param2 in mid:
                        G = arif.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        arif.updateGroup(G)
                        Ticket = arif.reissueGroupTicket(op.param1)
                        arif.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        arif.updateGroup(G)
                    else:
                        G = arif.getGroup(op.param1)
                        arif.kickoutFromGroup(op.param1,[op.param2])
                        G.preventJoinByTicket = False
                        arif.updateGroup(G)
                        Ticket = arif.reissueGroupTicket(op.param1)
                        arif.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        arif.updateGroup(G)
                        arif.updateGroup(G)
                        wait["blacklist"][op.param2] = True
                elif op.param3 in mid:
                    if op.param2 in mid:
                        G = arif.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        arif.updateGroup(G)
                        Ticket = arif.reissueGroupTicket(op.param1)
                        arif.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        arif.updateGroup(G)
                    else:
                        G = arif.getGroup(op.param1)
                        arif.kickoutFromGroup(op.param1,[op.param2])
                        G.preventJoinByTicket = False
                        arif.updateGroup(G)
                        Ticket = arif.reissueGroupTicket(op.param1)
                        arif.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        arif.updateGroup(G)
                        arif.updateGroup(G)
                        wait["blacklist"][op.param2] = True
                elif op.param3 in mid:
                    if op.param2 in mid:
                        G = arif.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        arif.updateGroup(G)
                        Ticket = arif.reissueGroupTicket(op.param1)
                        arif.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        arif.updateGroup(G)
                    else:
                        G = arif.getGroup(op.param1)
                        arif.kickoutFromGroup(op.param1,[op.param2])
                        G.preventJoinByTicket = False
                        arif.updateGroup(G)
                        Ticket = arif.reissueGroupTicket(op.param1)
                        arif.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        arif.updateGroup(G)
                        arif.updateGroup(G)
                        wait["blacklist"][op.param2] = True
                elif op.param3 in kimid:
                    if op.param2 in mid:
                        G = arif.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        arif.updateGroup(G)
                        Ticket = arif.reissueGroupTicket(op.param1)
                        arif.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        arif.updateGroup(G)
                    else:
                        G = arif.getGroup(op.param1)
                        arif.kickoutFromGroup(op.param1,[op.param2])
                        G.preventJoinByTicket = False
                        arif.updateGroup(G)
                        Ticket = arif.reissueGroupTicket(op.param1)
                        arif.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        arif.updateGroup(G)
                        arif.updateGroup(G)
                        wait["blacklist"][op.param2] = True
                elif op.param3 in kimid:
                    if op.param2 in mid:
                        G = arif.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        arif.updateGroup(G)
                        Ticket = arif.reissueGroupTicket(op.param1)
                        arif.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        arif.updateGroup(G)
                    else:
                        G = arif.getGroup(op.param1)
                        arif.kickoutFromGroup(op.param1,[op.param2])
                        G.preventJoinByTicket = False
                        arif.updateGroup(G)
                        Ticket = arif.reissueGroupTicket(op.param1)
                        arif.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        arif.updateGroup(G)
                        arif.updateGroup(G)
                        wait["blacklist"][op.param2] = True
                elif op.param3 in mid:
                    if op.param2 in mid:
                        G = arif.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        arif.updateGroup(G)
                        Ticket = arif.reissueGroupTicket(op.param1)
                        arif.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        arif.updateGroup(G)
                    else:
                        G = arif.getGroup(op.param1)
                        arif.kickoutFromGroup(op.param1,[op.param2])
                        G.preventJoinByTicket = False
                        arif.updateGroup(G)
                        Ticket = arif.reissueGroupTicket(op.param1)
                        arif.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        arif.updateGroup(G)
                        arif.updateGroup(G)
                        wait["blacklist"][op.param2] = True
            except:
                pass
	if op.type == 17:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
	    if wait["protect"] == True:
		if wait["blacklist"][op.param2] == True:
		   try:
			random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			G = random.choice(KAC).getGroup(op.param1)
			G.preventJoinByTicket = True
			arif.updateGroup(G)
			random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		   except:
			pass
			try:
			    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			    G = random.choice(KAC).getGroup(op.param1)
			    G.preventJoinByTicket = True
			    random.choice(KAC).updateGroup(G)
			    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			except:
			    pass
		elif op.param2 not in Bots:
		    random.choice(KAC).sendText(op.param1,"Welcome. Don't Play Bots. I can kick you!")
	    else:
		pass
	if op.type == 19:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["protect"] == True:
		    wait ["blacklist"][op.param2] = True
		    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		else:
		    arif.sendText(op.param1,"")
	    else:
		arif.sendText(op.param1,"")
	if op.type == 13:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["inviteprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		else:
		    arif.sendText(op.param1,"")
	    else:
		arif.sendText(op.param1,"")
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["inviteprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    arif.cancelGroupInvitation(op.param1,[contact.mid for contact in arif.getGroup(op.param1).invitee])
		else:
		    arif.sendText(op.param1,"")
	    else:
		arif.sendText(op.param1,"")
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["cancelprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    arif.cancelGroupInvitation(op.param1,[contact.mid for contact in arif.getGroup(op.param1).invitee])
		else:
		    arif.sendText(op.param1,"JANGAN INVITE TANPA SEIJIN ADMIN.!")
	    else:
		arif.sendText(op.param1,"")
	if op.type == 11:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["linkprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    G = ki.getGroup(op.param1)
		    G.preventJoinByTicket = True
		    ki.updateGroup(G)
		    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		else:
		    arif.sendText(op.param1,"")
	    else:
		arif.sendText(op.param1,"")
        if op.type == 5:
            if wait["autoAdd"] == True:
            	c = Message(to=op.param1, from_=None, text=None, contentType=13)
                c.contentMetadata={'mid':'u65224f4e8812136f01b25275a54b5aef'}
                arif.sendImageWithURL(op.param1,"http://dl.profile.line-cdn.net/0h9lRSzNuMZkNvKkqg8-AZFFNvaC4YBGALF0t9dhh9OHZBTihABk0hcU55bCdEE3UcVhh6dx4jOXdD")
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    arif.sendText(op.param1,str(wait["message"]))
                    arif.sendMessage(c)
                    ki.sendText(op.param1,str(wait["message"]))
                    ki.sendMessage(c)
                    
#------Open QR Kick start------#
        if op.type == 11:
            if wait["linkprotect"] == True:
                if op.param2 not in Bots:
                    G = random.choice(KAC).getGroup(op.param1)
                    G.preventJoinByTicket = True
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param3])
                    random.choice(KAC).updateGroup(G)
        #------Open Kick finish-----#
#------invite Kick start------#
        if op.type == 13:
            if wait["inviteprotect"] == True:
                if op.param2 not in Bots:
                    G = random.choice(KAC).getGroup(op.param1)
                    G.preventJoinByTicket = True
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param3])
                    random.choice(KAC).updateGroup(G)
        #------invite Kick finish-----#
        if op.type == 55:
            try:
                if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                            Name = arif.getContact(op.param2).displayName
                            Np = arif.getContact(op.param2).pictureStatus
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n� " + Name
                                if " " in Name:
                                    nick = Name.split(' ')
                                    if len(nick) == 2:
                                        arif.sendText(op.param1,"━━━━━━━━━[SIDER]━━━━━━━━━\n" + nick[0] + "\n" +  wait["sider1"])
                                        arif.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net/" + Np)
                                    else:
                                        arif.sendText(op.param1,"━━━━━━━━━[SIDER]━━━━━━━━━\n" + nick[0] + "\n" +  wait["sider1"])
                                        arif.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net/" + Np)
                                else:
                                    arif.sendText(op.param1,"━━━━━━━━━[SIDER]━━━━━━━━━\n" + nick[0] + "\n" +  wait["sider1"])
                                    arif.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net/" + Np)
                        else:
                            pass
                else:
                    pass
            except:
                pass
        else:
            pass
        
        if op.type == 55:
            if op.param1 in wait2['readPoint']:
                Name = arif.getContact(op.param2).displayName
                if Name in wait2['readMember'][op.param1]:
                    pass
                else:
                    wait2['readMember'][op.param1] += "\n・" + Name
                    wait2['ROM'][op.param1][op.param2] = "・" + Name
            else:
                arif.sendText
        if op.type == 17:
          if wait["wcOn"] == True:
            	ginfo = arif.getGroup(op.param1)
            	contact = arif.getContact(op.param2)
            	c = Message(to=op.param1, from_=None, text=None, contentType=13)
            	c.contentMetadata={'mid':op.param2}
            	arif.sendText(op.param1,wait["joingc"] + "\n" + arif.getContact(op.param2).displayName + "\nDi grup " + str(ginfo.name) + "\nCreator grup " + ginfo.creator.displayName + "\n\nBudayakan Cek Note\nDan Semoga Betah Disini ^_^")
            	arif.sendMessage(c)
            	arif.sendImageWithURL(op.param1,"http://dl.profile.line-cdn.net/" + contact.pictureStatus)
            	print ("MEMBER JOIN TO GROUP")
        if op.type == 15:
          if wait["leftOn"] == True:
            	c = Message(to=op.param1, from_=None, text=None, contentType=13)
            	c.contentMetadata={'mid':op.param2}
            	arif.sendMessage(c)
            	arif.sendText(op.param1,arif.getContact(op.param2).displayName + "\n" + wait["leftgc"])
            	print ("MEMBER HAS LEFT THE GROUP")
        if op.type == 55:
            try:
                if op.param1 in wait2['readPoint']:
           
                    if op.param2 in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += op.param2
                    wait2['ROM'][op.param1][op.param2] = op.param2
                    with open('sider.json', 'w') as fp:
                     json.dump(wait2, fp, sort_keys=True, indent=4)
                else:
                    pass
            except:
                pass           
        if op.type == 59:
            print op
    except Exception as error:
        print error
def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True
def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = arif.getProfile()
                profile.displayName = wait["cName"] + nowT
                arif.updateProfile(profile)
            time.sleep(0.30)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()
while True:
    try:
        Ops = arif.fetchOps(arif.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(arif.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            arif.Poll.rev = max(arif.Poll.rev, Op.revision)
            bot(Op)

