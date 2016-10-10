# -*- coding: utf-8 -*-
#------------------------------------------------------------
# PalcoTV Parser de TuMarcador.xyz by DarioMO
# Version 0.0.1 (10-09-2016)
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Gracias a la librería plugintools de Jesús (www.mimediacenter.info)
# Gracias a las librerías resolvers y media_analyzer de JuarroX (Grupo PalcoTV http://arena.pe.hu/forums/index.php y http://palcotv.blogspot.com.es/)

import os
import xbmcplugin
import xbmc, xbmcgui
import urllib

import sys
import urllib
import urllib2
import re

import xbmcaddon

import plugintools
import requests

from resources.tools.resolvers import *
from resources.tools.media_analyzer import *

playlists = xbmc.translatePath(os.path.join('special://userdata/playlists', ''))
temp = xbmc.translatePath(os.path.join('special://userdata/playlists/tmp', ''))

addonName           = xbmcaddon.Addon().getAddonInfo("name")
addonVersion        = xbmcaddon.Addon().getAddonInfo("version")
addonId             = xbmcaddon.Addon().getAddonInfo("id")
addonPath           = xbmcaddon.Addon().getAddonInfo("path")



parser="[COLOR skyblue][B]TuMarcador  [COLOR orange]Alegre  [COLOR skyblue]v0.0.6[/B][/COLOR]"
autor="[COLOR yellow][B][I]      **** by DarioMO ****[/I][/B][/COLOR]"
url_ref = "http://tumarcador.xyz/"
#url_montada = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=MI_CANAL%26referer='+url_ref
url_montada = 'plugin://plugin.video.live.streamspro/?url=%24doregex%5Bget-m3u8%5D&mode=17&regexs=%7Bu%27get-m3u8%27%3A%20%7B%27expres%27%3A%20u%27%23%24pyFunction%5Cndef%20GetLSProData%28page_data%2CCookie_Jar%2Cm%29%3A%5Cn%5Cn%20import%20requests%5Cn%20import%20re%5Cn%5Cn%20headers%20%3D%20%7B%5C%27User-Agent%5C%27%3A%20%5C%27Mozilla/5.0%20%28X11%3B%20Linux%20i686%3B%20rv%3A44.0%29%20Gecko/20100101%20Firefox/44.0%20Iceweasel/44.0%5C%27%2C%20%5C%27Referer%5C%27%3A%20%5C%27%5C%27%7D%5Cn%5Cn%20source%20%3D%20requests.get%28%5C%27MI_CANAL%5C%27%2C%20headers%3Dheaders%29%5Cn%20streamfn%20%3D%20re.findall%28%5C%27source%3A%20%28.%2A%3F%29%5C%5C%28%5C%27%2C%20source.text%29%5B0%5D%5Cn%20formula1%20%3D%20re.search%28r%5C%27function%20%5C%27%20%2B%20streamfn%20%2B%20%5C%27.%2A%5C%5Cn.%2A%5C%5C%5B%28.%2A%3F%29%5C%5C%5D.join.%2A%3F%5C%5C%2B%20%28.%2A%3F%29.join.%2A%3FById%5C%5C%28%22%28.%2A%3F%29%22%5C%27%2C%20source.text%29%5Cn%20par1%20%3D%20formula1.group%281%29.replace%28%5C%27%5C%5C%22%5C%27%2C%20%5C%27%5C%27%29.replace%28%5C%27%2C%5C%27%2C%20%5C%27%5C%27%29.replace%28%5C%27%5C%5C%5C%5C/%5C%27%2C%20%5C%27/%5C%27%29%5Cn%20prepar2%20%3D%20re.findall%28%5C%27var%20%5C%27%20%2B%20formula1.group%282%29%20%2B%20%5C%27.%2A%3F%5C%5C%5B%28%22.%2A%3F%29%5C%5C%5D%5C%27%2C%20source.text%29%5B0%5D%5Cn%20par2%20%3D%20prepar2.replace%28%5C%27%5C%5C%22%5C%27%2C%20%5C%27%5C%27%29.replace%28%5C%27%2C%5C%27%2C%20%5C%27%5C%27%29.replace%28%5C%27%5C%5C%5C%5C/%5C%27%2C%20%5C%27/%5C%27%29%5Cn%20par3%20%3D%20re.findall%28%5C%27id%3D%5C%27%20%2B%20formula1.group%283%29%20%2B%20%5C%27%3E%28.%2A%3F%29%3C%5C%27%2C%20source.text%29%5B0%5D%5Cn%5Cn%20finalm3u8%3D%20par1%20%2B%20par2%20%2Bpar3%5Cn%20return%20finalm3u8%5Cn%5Cn%27%2C%20%27name%27%3A%20u%27get-m3u8%27%2C%20%27page%27%3A%20None%7D%7D'
#url_montada = 'plugin://plugin.video.live.streamspro/?url=%24doregex%5Bget-m3u8%5D&amp;mode=17&amp;regexs=%7Bu%27get-m3u8%27%3A%20%7B%27expres%27%3A%20u%27%23%24pyFunction%5Cndef%20GetLSProData%28page_data%2CCookie_Jar%2Cm%29%3A%5Cn%5Cn%20import%20requests%5Cn%20import%20re%5Cn%5Cn%20headers%20%3D%20%7B%5C%27User-Agent%5C%27%3A%20%5C%27Mozilla/5.0%20%28X11%3B%20Linux%20i686%3B%20rv%3A44.0%29%20Gecko/20100101%20Firefox/44.0%20Iceweasel/44.0%5C%27%2C%20%5C%27Referer%5C%27%3A%20%5C%27%5C%27%7D%5Cn%5Cn%20source%20%3D%20requests.get%28%5C%27MI_CANAL%5C%27%2C%20headers%3Dheaders%29%5Cn%20streamfn%20%3D%20re.findall%28%5C%27source%3A%20%28.%2A%3F%29%5C%5C%28%5C%27%2C%20source.text%29%5B0%5D%5Cn%20formula1%20%3D%20re.search%28r%5C%27function%20%5C%27%20%2B%20streamfn%20%2B%20%5C%27.%2A%5C%5Cn.%2A%5C%5C%5B%28.%2A%3F%29%5C%5C%5D.join.%2A%3F%5C%5C%2B%20%28.%2A%3F%29.join.%2A%3FById%5C%5C%28%22%28.%2A%3F%29%22%5C%27%2C%20source.text%29%5Cn%20par1%20%3D%20formula1.group%281%29.replace%28%5C%27%5C%5C%22%5C%27%2C%20%5C%27%5C%27%29.replace%28%5C%27%2C%5C%27%2C%20%5C%27%5C%27%29.replace%28%5C%27%5C%5C%5C%5C/%5C%27%2C%20%5C%27/%5C%27%29%5Cn%20prepar2%20%3D%20re.findall%28%5C%27var%20%5C%27%20%2B%20formula1.group%282%29%20%2B%20%5C%27.%2A%3F%5C%5C%5B%28%22.%2A%3F%29%5C%5C%5D%5C%27%2C%20source.text%29%5B0%5D%5Cn%20par2%20%3D%20prepar2.replace%28%5C%27%5C%5C%22%5C%27%2C%20%5C%27%5C%27%29.replace%28%5C%27%2C%5C%27%2C%20%5C%27%5C%27%29.replace%28%5C%27%5C%5C%5C%5C/%5C%27%2C%20%5C%27/%5C%27%29%5Cn%20par3%20%3D%20re.findall%28%5C%27id%3D%5C%27%20%2B%20formula1.group%283%29%20%2B%20%5C%27%3E%28.%2A%3F%29%3C%5C%27%2C%20source.text%29%5B0%5D%5Cn%5Cn%20finalm3u8%3D%20par1%20%2B%20par2%20%2Bpar3%5Cn%20return%20finalm3u8%5Cn%5Cn%27%2C%20%27name%27%3A%20u%27get-m3u8%27%2C%20%27page%27%3A%20None%7D%7D'
                     

url = "http://tumarcador.xyz"

guia = "http://pastebin.com/raw/CiH3edWn"

def tumarcador0(params):
	###################################################################### DMO ######################################################################
	mi_version = ["2016","09","29"]  # OJO!! Cambiar la Version, por supuesto... AQUI Y EN EL FICHERO DE LA NUBE

	r = requests.get("http://pastebin.com/raw/2baqp6N8")

	data = r.content

	fecha = plugintools.find_single_match(data,'tumarcador>(.*?)<')
	ult_version = fecha.split(".")

	hay_nueva = False
	if mi_version[0] <> ult_version[0]:
		hay_nueva = True
	else:
		if mi_version[1] < ult_version[1]:
			hay_nueva = True
		else:
			if mi_version[2] < ult_version[2]:
				hay_nueva = True
				
	if hay_nueva == True:
		titu = "¡¡¡ATENCION!!!!"
		lin1 = "      Versión [COLOR red]OBSOLETA de TuMarcador[/COLOR] updated by DarioMO"
		lin2 = " Ya tienes disponible la Ultima Versión para poder actualizarlo"
		lin3 = "         [COLOR yellow]Descarga:[/COLOR] [COLOR red][B]http://adf.ly/7448402/tu-marcador[/COLOR][/B]"
		xbmcgui.Dialog().ok(titu, lin1, lin2, lin3)
	###################################################################### DMO ######################################################################

	ruta_pro = xbmc.translatePath(os.path.join('special://home/userdata/addon_data/plugin.video.live.streamspro', ''))
	#headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0', "Referer": url}
	r=requests.get(guia)
	data = r.content

	if not os.path.exists(ruta_pro):
		os.makedirs(ruta_pro)  # Si no existe el directorio, LSP nos va a dar error... así q lo creo
	
	logo = "https://pbs.twimg.com/profile_images/1851363673/logo.jpg"
	fondo = "http://www.sportyou.es/blog/wp-content/uploads/2016/09/Neymar-Benzema-Cristiano.jpg"
	
	plugintools.add_item(action="",url="",title="               "+parser+autor,thumbnail="http://imgur.com/l8fKJMB.png",fanart=fondo,folder=False,isPlayable=False)
	plugintools.add_item(action="",url="",title="",thumbnail=logo, fanart=fondo, folder=False, isPlayable=False)
	
	plugintools.add_item(action="zap_marcador",url="",title="[COLOR white][B]- Zapping de Canales -[/COLOR][/B]",thumbnail="http://lafava.com/wp-content/uploads/2015/06/zapping1.jpg",fanart=fondo,folder=True,isPlayable=False)
	plugintools.add_item(action="muestra_guia",url="",title="[COLOR red][B]- Mostrar Guía en Imagenes -[/COLOR][/B]",thumbnail="http://i.imgur.com/BNQwcS6.png",fanart=fondo,folder=True,isPlayable=False)
	plugintools.add_item(action="",url="",title="",thumbnail=logo, fanart=fondo, folder=False, isPlayable=False)

	dias = plugintools.find_multiple_matches(data,'<dia>(.*?)<fin dia>')
	for item in dias:
		dia = "             [COLOR white]Día: " + plugintools.find_single_match(item,'(.*?)<')
		plugintools.add_item(action="",url="",title=dia,thumbnail=logo, fanart=fondo, folder=False, isPlayable=False)
		
		lineas = plugintools.find_multiple_matches(item,'<linea>(.*?)<fin')
		print lineas
		
		for item2 in lineas:
			linea = item2 + "<"
			hora = plugintools.find_single_match(linea,'<hora>(.*?)<')
			competicion = plugintools.find_single_match(linea,'<competi>(.*?)<')
			partido = plugintools.find_single_match(linea,'<partido>(.*?)<')
			canal = plugintools.find_single_match(linea,'<canal>(.*?)<')
			logo_ext = plugintools.find_single_match(linea,'<logo>(.*?)<')

			if len(canal) > 1:
				letrero = "Canales: "
			else:
				letrero = "Canal: "
			
			canal_regex = canal
			if canal == "1":
				canal_regex = "x"
			if canal == "2":
				canal_regex = "y"

			el_canal = "http://tumarcador.xyz/canal" + canal_regex + ".php"
				
			completa = hora + "   [COLOR white](" + competicion + ") - [/COLOR]" + partido + "    [COLOR white][I]["+letrero+canal+"] [/COLOR][/I]"
			lanzo_spd = url_montada.replace("MI_CANAL", el_canal)
			#plugintools.log("*************Canal: "+el_canal+"**************")
			if len(logo_ext) > 0:
				logo = logo_ext

			plugintools.runAddon(action="runPlugin",url=lanzo_spd,title=completa,thumbnail=logo, fanart=fondo, folder=False, isPlayable=True)
		
				
	return

def lanza_marca(params):
	canal = params.get("url")
	fanart = params.get("fanart")
	thumbnail = params.get("thumbnail")
	partido = params.get("extra")
	
	if upper(canal) == "X":
		canal = "1"
	if upper(canal) == "Y":
		canal = "2"
		
	if len(canal) > 1:
		canales = canal.split(", ")
		titu = partido + "  en canal "
		for i in range(len(canales)):
			linea = "- ver " + titu + canales[i-1]
			lanzo_spd = url_montada.replace("MI_CANAL", canales[i-1])
			plugintools.log("*************Canal: "+canales[i-1]+"**************")
			plugintools.runAddon(action="runPlugin",url=lanzo_spd,title=partido,thumbnail=logo, fanart=fondo, folder=False, isPlayable=True)
	else:
		linea = "- ver " + titu + canal
		lanzo_spd = url_montada.replace("MI_CANAL", canal)
		plugintools.log("*************Canal: "+canal+"**************")
		plugintools.runAddon(action="runPlugin",url=lanzo_spd,title=partido,thumbnail=logo, fanart=fondo, folder=False, isPlayable=True)
		
	


def zap_marcador(params):
	fondo = params.get("fanart")
	logo = params.get("thumbnail")
	r=requests.get(url)
	data = r.content

	plugintools.add_item(action="",url="",title="               [COLOR skyblue][B]Zapping de "+parser+autor,thumbnail=logo,fanart=fondo,folder=False,isPlayable=False)
	plugintools.add_item(action="",url="",title="",thumbnail=logo, fanart=fondo, folder=False, isPlayable=False)
	

	canales = plugintools.find_single_match(data,'dropdown-menu">(.*?)</ul>')  # Cojo el bloque de canales
	cada_canal = plugintools.find_multiple_matches(canales,'href=(.*?)/a>')  # Separo todos los canales y los monto en su url
				
	#Los saco a pantalla
	for item in cada_canal:
		canal_url = plugintools.find_single_match(item,'"(.*?)"')
		nombre_canal = plugintools.find_single_match(item,'">(.*?)<')
		titulo = "[COLOR aqua]- Ver el " + nombre_canal + "[/COLOR]"

		el_canal = "http://tumarcador.xyz/" + canal_url
		lanzo_spd = url_montada.replace("MI_CANAL", el_canal)
		
		#Montamos la línea.
		plugintools.runAddon(action="runPlugin",url=lanzo_spd,title=titulo,thumbnail=logo,fanart=fondo,folder=False,isPlayable=True)


def muestra_guia(params):
	fanart = params.get("fanart")
	logo = params.get("thumbnail")

	r=requests.get(url)
	data = r.content
	logo = "http://i.imgur.com/BNQwcS6.png"

	cada_guia = plugintools.find_multiple_matches(data,'div class="col-(.*?)</div>')  # Hay días que pone mas de una Imagen para la guia

	i = 0
	for item in cada_guia:
		imagenes = plugintools.find_multiple_matches(item,'src="(.*?)"')
		for item2 in imagenes:
			if len(item2) > 0:
				i = i + 1
				plugintools.add_item(action="lanza_imagen",url=item2,title="-Ver Guía "+str(i),thumbnail=logo,fanart=fanart,folder=True,isPlayable=False)
				
	return

def lanza_imagen(params):
	imagen = params.get("url")
	
	ACTION_PREVIOUS_MENU = 10
	ACTION_SELECT_ITEM = 7
	ACTION_PARENT_DIR = 9
	class MyClass(xbmcgui.Window):
		def __init__(self):
			xbmcgui.Window.__init__(self)
			self.addControl(xbmcgui.ControlImage(0,0,1280,720, imagen))
			self.strActionInfo = xbmcgui.ControlLabel(100, 200, 200, 200, "", "font13", "0xFFFF00FF")
			self.addControl(self.strActionInfo)
			self.strActionInfo.setLabel("")

	mydisplay = MyClass()
	mydisplay.doModal()
	del mydisplay

	return

			
	

def lanza_marca(params):
	lanzame = 'PlayMedia(' + params.get("url") + ')'

	plugintools.log("********LANZO: "+lanzame+"**************")    

	xbmc.executebuiltin(lanzame)
	
	
	
	
