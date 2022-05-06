import xbmc, xbmcaddon, xbmcgui, xbmcplugin, xbmcvfs,os,sys
import urllib
import re
import time
import requests
from resources.lib.modules import control, tools
from resources.lib.modules.backtothefuture import unicode, PY2

if PY2:
    quote_plus = urllib.quote_plus
else:
    quote_plus = urllib.parse.quote_plus

AddonID ='script.ezlimpiador'
USER_AGENT = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
selfAddon    = xbmcaddon.Addon(id=AddonID)

# Code to map the old translatePath
try:
    translatePath = xbmcvfs.translatePath
except AttributeError:
    translatePath = xbmc.translatePath

# ADDON SETTINGS
wizard1      =  control.setting('enable_wiz1')
wizard2      =  control.setting('enable_wiz2')
wizard3      =  control.setting('enable_wiz3')
wizard4      =  control.setting('enable_wiz4')
wizard5      =  control.setting('enable_wiz5')
backupfull   =  control.setting('backup_database')
backupaddons =  control.setting('backup_addon_data')
backupzip    =  control.setting("remote_backup")
USB          =  translatePath(os.path.join(backupzip))

# ICONS FANARTS
ADDON_FANART  = control.addonFanart()
ADDON_ICON    = control.addonIcon()

# DIRECTORIES
backupdir        =  translatePath(os.path.join('special://home/backupdir',''))
packagesdir      =  translatePath(os.path.join('special://home/addons/packages',''))
USERDATA         =  translatePath(os.path.join('special://home/userdata',''))
ADDON_DATA       =  translatePath(os.path.join(USERDATA,'addon_data'))
HOME             =  translatePath('special://home/')
HOME_ADDONS      =  translatePath('special://home/addons')
backup_zip       =  translatePath(os.path.join(backupdir,'backup_addon_data.zip'))

# DIALOGS
dialog = xbmcgui.Dialog()
progressDialog = xbmcgui.DialogProgress()

AddonTitle = "EZ Limpiador+"
EXCLUDES         = [AddonID, 'backupdir','backup.zip','script.module.requests','script.module.urllib3','script.module.chardet','script.module.idna','script.module.certifi']
EXCLUDES_ADDONS  = ['notification','packages']


# ######################### CATEGORIES ################################
def MAINTENANCE():
    CreateDir('Limpiar Cache','url','clear_cache',ADDON_ICON,ADDON_FANART,'')
    CreateDir('Borrar Paquetes','url','clear_packages',ADDON_ICON,ADDON_FANART,'')
    CreateDir('Limpiar Imagenes','url','clear_thumbs',ADDON_ICON,ADDON_FANART,'')


# ###########################################################################################
# ###########################################################################################





def CreateDir(name, url, action, icon, fanart, description, isFolder=False):
        if icon == None or icon == '': icon = ADDON_ICON
        u=sys.argv[0]+"?url="+quote_plus(url)+"&action="+str(action)+"&name="+quote_plus(name)+"&icon="+quote_plus(icon)+"&fanart="+quote_plus(fanart)+"&description="+quote_plus(description)
        ok=True
        if PY2:
            liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=icon)
        else:
            liz=xbmcgui.ListItem(name)
            liz.setArt({'icon':"DefaultFolder.png"})
            liz.setArt({'thumbnailImage': icon})
        liz.setInfo(type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=isFolder)
        return ok


if PY2:
    from urlparse import parse_qsl
else:
    from urllib.parse import parse_qsl

params = dict(parse_qsl(sys.argv[2].replace('?','')))
action = params.get('action')

icon = params.get('icon')

name = params.get('name')

title = params.get('title')

year = params.get('year')

fanart = params.get('fanart')

tvdb = params.get('tvdb')

tmdb = params.get('tmdb')

season = params.get('season')

episode = params.get('episode')

tvshowtitle = params.get('tvshowtitle')

premiered = params.get('premiered')

url = params.get('url')

image = params.get('image')

meta = params.get('meta')

select = params.get('select')

query = params.get('query')

description = params.get('description')

content = params.get('content')



if action   == None: MAINTENANCE()
elif action == 'maintenance': MAINTENANCE()

elif action == 'clear_cache':
    from resources.lib.modules import maintenance
    maintenance.clearCache()

elif action == 'clear_packages':
    from resources.lib.modules import maintenance
    maintenance.purgePackages()
elif action == 'clear_thumbs':
    from resources.lib.modules import maintenance
    maintenance.deleteThumbnails()


xbmcplugin.endOfDirectory(int(sys.argv[1]))

