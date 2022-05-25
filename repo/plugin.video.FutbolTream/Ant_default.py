# -*- coding: utf-8 -*-
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Gracias a la librería plugintools de Jesús (www.mimediacenter.info), PlatformCode y Core del Grupo Balandro (https://linktr.ee/balandro)

import os, sys, urllib, re, shutil, zipfile, base64
#import xbmc, xbmcgui, xbmcaddon, xbmcplugin, requests
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
import locale, time, random, plugintools
import resolvers

if sys.version_info[0] < 3:
    import urllib2
else:
    import urllib.error as urllib2

from core import httptools
from core.item import Item
from platformcode.config import WebErrorException


addonName           = xbmcaddon.Addon().getAddonInfo("name")
addonVersion        = xbmcaddon.Addon().getAddonInfo("version")
addonId             = xbmcaddon.Addon().getAddonInfo("id")
addonPath           = xbmcaddon.Addon().getAddonInfo("path")

version="(v0.0.5)"

addonPath           = xbmcaddon.Addon().getAddonInfo("path")
mi_data = xbmc.translatePath(os.path.join('special://home/userdata/addon_data/plugin.video.FutbolTream/'))
mi_addon = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.FutbolTream'))

fondo = xbmc.translatePath(os.path.join(mi_addon,'fanart.jpg'))
logoprin = xbmc.translatePath(os.path.join(mi_addon,'icon.png'))

mislogos = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.FutbolTream/jpg/'))

logo_transparente = xbmc.translatePath(os.path.join(mislogos , 'transparente.png'))

web = "https://futbolgratis0.webnode.es/"
headers = {'Referer': web}

dataWeb = httptools.downloadpage(web, headers=headers).data

guia_eventos = plugintools.find_multiple_matches(dataWeb,'<tr>(.*?)</tr>')

horusTorrent = "eydhY3Rpb24nOiAncGxheScsICdmYW5hcnQnOiAnJywgJ2ljb24nOiAnTUktSUNPTk8nLCAndXJsJzogJ01JLVRPUlJFTlQnLCAnbGFiZWwnOiAnTUktVElUVUxPJ30="  ## Para Torrents
horusAce = "eydhY3Rpb24nOiAncGxheScsICdmYW5hcnQnOiAnTUktRkFOQVJUJywgJ2ljb24nOiAnTUktSUNPTk8nLCAnaWQnOiAnTUktSUQtQUNFJywgJ2xhYmVsJzogJ01JLVRJVFVMTyd9"  ##Para id-Aces

if not os.path.exists(mi_data):
	os.makedirs(mi_data)  # Si no existe el directorio, lo creo


cabecera = "[COLOR mediumslateblue][B]      FutbolTream  "+version+" [COLOR red]        ····[COLOR yellowgreen]by AceTorr[COLOR red]····[/B][/COLOR]"
	

# Punto de Entrada
def run():
	plugintools.log('[%s %s] Running %s... ' % (addonName, addonVersion, addonName))

	# Obteniendo parámetros...
	params = plugintools.get_params()
    
	
	if params.get("action") is None:
		main_list(params)
	else:
		action = params.get("action")
		exec(action+"(params)")
        

	plugintools.close_item_list()            



# Principal
def main_list(params):
    
    plugintools.add_item(action="",url="",title=cabecera,thumbnail=logoprin,fanart=fondo,folder=False,isPlayable=False)

    if len(guia_eventos) > 0:
        plugintools.add_item(action="guiaEventos",url=web,title='[COLOR lime]>>>  Guía de Eventos  (entrar)  <<<[/COLOR]', thumbnail=logoprin, fanart=fondo, folder=True, isPlayable=False)
    else:
        plugintools.add_item(action="",url="",title="[COLOR red]····Guia de Eventos temporalmente Inactiva en la Web····[/COLOR]",thumbnail=logoprin,fanart=fondo,folder=False,isPlayable=False)
    
    if ("Canales HD" in dataWeb) and ("Lucas_m_" in dataWeb) and ("@MANUK0S" in dataWeb):  ##Si están tituladas las 3 Listas del Centro de la página
        plugintools.add_item(action="bylucas",url=web,title='[COLOR white]By @Lucas_m_o_o_m[/COLOR]', thumbnail=logoprin, fanart=fondo, folder=True, isPlayable=False)
        plugintools.add_item(action="manukos",url=web,title='[COLOR white]By @MANUK0S[/COLOR]', thumbnail=logoprin, fanart=fondo, folder=True, isPlayable=False)
        plugintools.add_item(action="canalesHD",url=web,title='[COLOR white]Canales HD[/COLOR]', thumbnail=logoprin, fanart=fondo, folder=True, isPlayable=False)
    else:  ##Intentamos coger todos los links en una única lista
        plugintools.add_item(action="listaCentral",url=web,title='[COLOR white]Recopilación Temporal de Listas [COLOR coral](Faltan datos de creadores en la Web)[/COLOR]', thumbnail=logoprin, fanart=fondo, folder=True, isPlayable=False)
    
    plugintools.add_item(action="canales365",url="",title='[COLOR white]Canales 365[/COLOR]', thumbnail=logoprin, fanart=fondo, folder=True, isPlayable=False)
    plugintools.add_item(action="zapping",url="",title='[COLOR white]Zapping Arena[/COLOR]', thumbnail=logoprin, fanart=fondo, folder=True, isPlayable=False)
    
    plugintools.add_item(action="", url="", title="", genre="NOGESTIONAR", thumbnail=logo_transparente, fanart=fondo, folder=False, isPlayable=False)
    mensaje = "[COLOR firebrick]**Este addon se suministra gratuitamente desde [COLOR yellow][B]Kelebek[/B][COLOR firebrick]. Si está en algún otro paquete, es sin la AUTORIZACIÓN de sus creadores.[/COLOR]"
    plugintools.add_item(action="", url="", title=mensaje, genre="NOGESTIONAR", thumbnail=logoprin, fanart=fondo, folder=False, isPlayable=False)





def guiaEventos(params):

    acotacion = 'class="title">'
    elTitulo = plugintools.find_single_match(dataWeb,acotacion+'(.*?)</h1')
    plugintools.add_item(action="", url="", title="[COLOR red][B]····"+elTitulo+"····[/B][/COLOR]", genre="NOGESTIONAR", thumbnail=logoprin, fanart=fondo, folder=False, isPlayable=False)
    plugintools.add_item(action="", url="", title="[COLOR greenyellow]***Los canales pueden no estar activos hasta minutos antes del Evento***[/COLOR]", genre="NOGESTIONAR", thumbnail=logoprin, fanart=fondo, folder=False, isPlayable=False)

    primeraLin = True
    for item in guia_eventos:
        if primeraLin:  ##Si es la 1ª línea la salto pues es la cabecera en la web
            primeraLin = False
        else:
            evento = plugintools.find_multiple_matches(item,'<td(.*?)/td>')
            
            dia = plugintools.find_single_match(evento[0],'>(.*?)<').replace("td&gt;" , "").replace("\n" , "")
            hora = plugintools.find_single_match(evento[1],'>(.*?)<').replace("td&gt;" , "").replace("\n" , "")
            deporte = plugintools.find_single_match(evento[2],'>(.*?)<').replace("td&gt;" , "").replace("\n" , "")
            competicion = plugintools.find_single_match(evento[3],'>(.*?)<').replace("td&gt;" , "").replace("\n" , "")
            partido = plugintools.find_single_match(evento[4],'>(.*?)<').replace("td&gt;" , "").replace("\n" , "")
            #canales = plugintools.find_single_match(evento[5],'>(.*?)<').replace("td&gt;" , "").replace("\n" , "")
            aCanal = ["",""]
            if "<br>" in evento[5]:  ## Hay mas de 1 canal para el evento
                #class="auto-style3">9-10 [SPA]<br> 17-18 [SPA]
                can2 = evento[5].replace("td&gt;" , "").replace("\n" , "") + "<"
                aCanal[0] = plugintools.find_single_match(can2,'>(.*?)<br')
                aCanal[1] = plugintools.find_single_match(can2,'br>(.*?)<')
            else:
                aCanal[0] =  plugintools.find_single_match(evento[5],'>(.*?)<').replace("td&gt;" , "").replace("\n" , "")
            
            for canales in aCanal:
                if len(canales) > 0:
                    ##Vamos a localizar el link del partido
                    can2 = ">" + canales.replace("[" , "<")
                    elCanal = plugintools.find_single_match(can2,'>(.*?)<').strip()
                    #plugintools.log("*****************Canales: "+canales+"********************")
                    
                    #Lo busco en el grupo "a visionar"
                    acotacion = "a visionar<"
                    grupo = plugintools.find_single_match(dataWeb,acotacion+'(.*?)</strong')
                    lineas = plugintools.find_multiple_matches(grupo,'<a(.*?)/a>')
                    link = ""
                    for item in lineas:
                        titulo = plugintools.find_single_match(item,'follow">(.*?)<').strip()
                        if titulo == elCanal:
                            link = plugintools.find_single_match(item,'href="(.*?)"')
                    
                    titu = ""
                    if len(link) > 0:  ## Tenemos Link, podemos poner el evento en Pantalla
                        titu = "[COLOR white]-" + dia + " [COLOR lime](" + hora + ") [COLOR orange] " + deporte.title()
                        titu = titu + ": " + competicion.title() + "-> [COLOR blue] " + partido + " [COLOR red]" + canales + "[/COLOR]"
         
                        if "acestream" in link:
                            horus = horusAce
                            link = link.replace("acestream://" , "")
                            reemplaza = base64.b64decode(horus.encode('utf-8')).decode('utf-8').replace("MI-ID-ACE" , link)
                        else:
                            horus = horusTorrent
                            reemplaza = base64.b64decode(horus.encode('utf-8')).decode('utf-8').replace("MI-TORRENT" , link)
                            
                        reemplaza = reemplaza.replace("MI-FANART" , "")
                        reemplaza = reemplaza.replace("MI-ICONO" , logoprin)
                        reemplaza = reemplaza.replace("MI-TITULO" , partido)
                        #plugintools.log("*****************Remplaza: "+reemplaza+"********************")
                        
                        mivideo = "plugin://script.module.horus/?" + base64.b64encode(reemplaza.encode('utf-8')).decode('utf-8')
                        
                        plugintools.add_item(action="lanza", url=mivideo, title=titu, genre="NOGESTIONAR", thumbnail=logoprin, fanart=fondo, folder=False, isPlayable=False)
 





def listaCentral(params):
    
    acotacion = "/a></h1"
    acotaFin = '<hr class="line-style'
    grupo = plugintools.find_single_match(dataWeb,acotacion+'(.*?)'+acotaFin)  
    canales = plugintools.find_multiple_matches(grupo,'<a(.*?)/a>')
    for item in canales:
        link = plugintools.find_single_match(item,'href="(.*?)"')
        titulo = plugintools.find_single_match(item,'follow">(.*?)<')
        titu = "[COLOR white]" + titulo + "[/COLOR]"
        #plugintools.log("*****************Titu: "+titulo+"********************")
        #plugintools.log("*****************Link: "+link+"********************")
        if len(titulo) > 0:
            if "acestream" in link:
                horus = horusAce
                link = link.replace("acestream://" , "")
                reemplaza = base64.b64decode(horus.encode('utf-8')).decode('utf-8').replace("MI-ID-ACE" , link)
            else:
                horus = horusTorrent
                reemplaza = base64.b64decode(horus.encode('utf-8')).decode('utf-8').replace("MI-TORRENT" , link)
                
            reemplaza = reemplaza.replace("MI-FANART" , "")
            reemplaza = reemplaza.replace("MI-ICONO" , logoprin)
            reemplaza = reemplaza.replace("MI-TITULO" , titulo)
            #plugintools.log("*****************Reemplaza: "+reemplaza+"********************")
            
            mivideo = "plugin://script.module.horus/?" + base64.b64encode(reemplaza.encode('utf-8')).decode('utf-8')
            
            plugintools.add_item(action="lanza", url=mivideo, title=titu, genre="NOGESTIONAR", thumbnail=logoprin, fanart=fondo, folder=False, isPlayable=False)


def canalesHD(params):
    
    acotacion = "Canales HD"
    grupo = plugintools.find_single_match(dataWeb,acotacion+'(.*?)<div')  
    canales = plugintools.find_multiple_matches(grupo,'<a(.*?)/a>')
    for item in canales:
        link = plugintools.find_single_match(item,'href="(.*?)"')
        titulo = plugintools.find_single_match(item,'follow">(.*?)<')
        titu = "[COLOR white]" + titulo + "[/COLOR]"
        #plugintools.log("*****************Titu: "+titulo+"********************")
        #plugintools.log("*****************Link: "+link+"********************")
        if len(titulo) > 0:
            if "acestream" in link:
                horus = horusAce
                link = link.replace("acestream://" , "")
                reemplaza = base64.b64decode(horus.encode('utf-8')).decode('utf-8').replace("MI-ID-ACE" , link)
            else:
                horus = horusTorrent
                reemplaza = base64.b64decode(horus.encode('utf-8')).decode('utf-8').replace("MI-TORRENT" , link)
                
            reemplaza = reemplaza.replace("MI-FANART" , "")
            reemplaza = reemplaza.replace("MI-ICONO" , logoprin)
            reemplaza = reemplaza.replace("MI-TITULO" , titulo)
            #plugintools.log("*****************Reemplaza: "+reemplaza+"********************")
            
            mivideo = "plugin://script.module.horus/?" + base64.b64encode(reemplaza.encode('utf-8')).decode('utf-8')
            
            plugintools.add_item(action="lanza", url=mivideo, title=titu, genre="NOGESTIONAR", thumbnail=logoprin, fanart=fondo, folder=False, isPlayable=False)


def bylucas(params):
    
    acotacion = "Lucas_m_"
    grupo = plugintools.find_single_match(dataWeb,acotacion+'(.*?)<div')  
    canales = plugintools.find_multiple_matches(grupo,'<a(.*?)/a>')
    for item in canales:
        link = plugintools.find_single_match(item,'href="(.*?)"')
        titulo = plugintools.find_single_match(item,'follow">(.*?)<')
        titu = "[COLOR white]" + titulo + "[/COLOR]"
        if len(titulo) > 0:
            if "acestream" in link:
                link = link.replace("acestream://" , "")
                horus = horusAce
                reemplaza = base64.b64decode(horus.encode('utf-8')).decode('utf-8').replace("MI-ID-ACE" , link)
            else:
                horus = horusTorrent
                reemplaza = base64.b64decode(horus.encode('utf-8')).decode('utf-8').replace("MI-TORRENT" , link)
                
            reemplaza = reemplaza.replace("MI-FANART" , "")
            reemplaza = reemplaza.replace("MI-ICONO" , logoprin)
            reemplaza = reemplaza.replace("MI-TITULO" , titulo)
            
            mivideo = "plugin://script.module.horus/?" + base64.b64encode(reemplaza.encode('utf-8')).decode('utf-8')
            
            plugintools.add_item(action="lanza", url=mivideo, title=titu, genre="NOGESTIONAR", thumbnail=logoprin, fanart=fondo, folder=False, isPlayable=False)



def manukos(params):
    
    acotacion = "@MANUK0S"
    grupo = plugintools.find_single_match(dataWeb,acotacion+'(.*?)<div')  
    canales = plugintools.find_multiple_matches(grupo,'<a(.*?)/a>')
    for item in canales:
        link = plugintools.find_single_match(item,'href="(.*?)"')
        titulo = plugintools.find_single_match(item,'follow">(.*?)<')
        titu = "[COLOR white]" + titulo + "[/COLOR]"
        if len(titulo) > 0:
            if "acestream" in link:
                link = link.replace("acestream://" , "")
                horus = horusAce
                reemplaza = base64.b64decode(horus.encode('utf-8')).decode('utf-8').replace("MI-ID-ACE" , link)
            else:
                horus = horusTorrent
                reemplaza = base64.b64decode(horus.encode('utf-8')).decode('utf-8').replace("MI-TORRENT" , link)
                
            reemplaza = reemplaza.replace("MI-FANART" , "")
            reemplaza = reemplaza.replace("MI-ICONO" , logoprin)
            reemplaza = reemplaza.replace("MI-TITULO" , titulo)
            
            mivideo = "plugin://script.module.horus/?" + base64.b64encode(reemplaza.encode('utf-8')).decode('utf-8')
            
            plugintools.add_item(action="lanza", url=mivideo, title=titu, genre="NOGESTIONAR", thumbnail=logoprin, fanart=fondo, folder=False, isPlayable=False)



def canales365(params):
    
    acotacion = "Canales 365"
    grupo = plugintools.find_single_match(dataWeb,acotacion+'(.*?)<hr')
    canales = plugintools.find_multiple_matches(grupo,'<a(.*?)/a>')
    for item in canales:
        link = plugintools.find_single_match(item,'href="(.*?)"')
        titulo = plugintools.find_single_match(item,'follow">(.*?)<')
        titu = "[COLOR white]" + titulo + "[/COLOR]"
        if len(titulo) > 0:
            if "acestream" in link:
                link = link.replace("acestream://" , "")
                horus = horusAce
                reemplaza = base64.b64decode(horus.encode('utf-8')).decode('utf-8').replace("MI-ID-ACE" , link)
            else:
                horus = horusTorrent
                reemplaza = base64.b64decode(horus.encode('utf-8')).decode('utf-8').replace("MI-TORRENT" , link)
                
            reemplaza = reemplaza.replace("MI-FANART" , "")
            reemplaza = reemplaza.replace("MI-ICONO" , logoprin)
            reemplaza = reemplaza.replace("MI-TITULO" , titulo)
            plugintools.log("*****************Reemplaza: "+reemplaza+"********************")
            
            mivideo = "plugin://script.module.horus/?" + base64.b64encode(reemplaza.encode('utf-8')).decode('utf-8')
            
            plugintools.add_item(action="lanza", url=mivideo, title=titu, genre="NOGESTIONAR", thumbnail=logoprin, fanart=fondo, folder=False, isPlayable=False)



def zapping(params):
    
    acotacion = "a visionar<"
    grupo = plugintools.find_single_match(dataWeb,acotacion+'(.*?)</strong')
    canales = plugintools.find_multiple_matches(grupo,'<a(.*?)/a>')
    for item in canales:
        link = plugintools.find_single_match(item,'href="(.*?)"')
        titulo = plugintools.find_single_match(item,'follow">(.*?)<')
        if len(titulo) > 0:
            titu = "[COLOR white]Canal " + titulo + "[/COLOR]"
            #plugintools.log("*****************Titu: "+titu+"********************")
            if "acestream" in link:
                link = link.replace("acestream://" , "")
                horus = horusAce
                reemplaza = base64.b64decode(horus.encode('utf-8')).decode('utf-8').replace("MI-ID-ACE" , link)
            else:
                horus = horusTorrent
                reemplaza = base64.b64decode(horus.encode('utf-8')).decode('utf-8').replace("MI-TORRENT" , link)
                
            reemplaza = reemplaza.replace("MI-FANART" , "")
            reemplaza = reemplaza.replace("MI-ICONO" , logoprin)
            reemplaza = reemplaza.replace("MI-TITULO" , titulo)
            #plugintools.log("*****************Reemplaza: "+reemplaza+"********************")
            
            mivideo = "plugin://script.module.horus/?" + base64.b64encode(reemplaza.encode('utf-8')).decode('utf-8')
            
            plugintools.add_item(action="lanza", url=mivideo, title=titu, genre="NOGESTIONAR", thumbnail=logoprin, fanart=fondo, folder=False, isPlayable=False)





def lanza(params):
    mivideo = params.get("url")
    logo = params.get("thumbnail")
    titu = params.get("title")
    titulo = params.get("extra")
    
    xbmc.Player().play(mivideo)





def salida(params):

	xbmc.executebuiltin('ActivateWindow(10000,return)')
	



	


	


		
run()

		




	

