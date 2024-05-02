# -*- coding: utf-8 -*-
#------------------------------------------------------------
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon


addonID = 'plugin.video.doqmental'

local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID1 = "UCGtFh-sO0mpk5dgEXVzMhKw"
YOUTUBE_CHANNEL_ID2 = "UC0QO3TaHg14sRc3pPFmaXnQ"
YOUTUBE_CHANNEL_ID3 = "UC259MSTQbJjxYGzUM0SvYGA"
YOUTUBE_CHANNEL_ID4 = "UCJCen5xxTtU7cnVHe3n424A"
YOUTUBE_CHANNEL_ID5 = "PlanetDocFilms"
YOUTUBE_CHANNEL_ID6 = "UCV5OEc-nA4Ge5tOLUPWosaQ"
YOUTUBE_CHANNEL_ID7 = "UCaXupcZvG8NMZwbFO4vh4Tg"
YOUTUBE_CHANNEL_ID8 = "UCGNk1YgQf8zeFX7uP04O_uw"
YOUTUBE_CHANNEL_ID9 = "UCQ1GpKa15ulyoQuxz7H4rng"
YOUTUBE_CHANNEL_ID10 = "UC_PkkoCXPpIH8Ip5RXUwccA"
YOUTUBE_CHANNEL_ID11 = "UC9eCLBSj2fCYUsnMuelRloQ"
YOUTUBE_CHANNEL_ID12 = "UCBIMW0ZhwULY_x7fdaPRPiQ"
YOUTUBE_CHANNEL_ID13 = "UCv05qOuJ6Igbe-EyQibJgwQ"
YOUTUBE_CHANNEL_ID14 = "UCwRvBitYM27PF-Yz2LSfABA"
YOUTUBE_CHANNEL_ID15 = "UC1W_Jc9UmyttYlSo0i5DzJg"
YOUTUBE_CHANNEL_ID16 = "UCAx8AK17j6BKqdQefiHWGag"
YOUTUBE_CHANNEL_ID17 = "UCv7ZxMpxzixEAi5mR_eDqHw"





# Entry point
def run():
    plugintools.log("doqmental.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        pass
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("doqmental.main_list "+repr(params))

	
     
    plugintools.add_item( 
        #action="", 
        title="RTVE Documentales",
        url="plugin://plugin.video.youtube/playlist/PLFLBjMW4wU7jWKp3V_k8pw8HH4d-AAy9M/",
   		fanart="https://wallpaperstock.net/wallpapers/thumbs1/45301hd.jpg",
        thumbnail="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjGN96M-brBizgjeJnmXJwBWpHv12LanDJN2DlkyjDQESeBt5z3tie-I2zmQJKpI9Lwqiemav1DuCwDI2U0Gn-uUyjE0eek454Zg8aHGX35Oclh-Z2zJlZiu4Oi2uy4GsZbjecDCRj47G02kKxgIorJClWs8ZXspS-55oVF2xVGtgJmUOTnfurpyI7oW21m/s461/Logo_rtvees.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="DMAX España",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID11+"/",
        thumbnail="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg5YrM91jlz6kkV8ajRDbP9N049BgmYN_5wQFKCRk5OnmkWfygYU3NJYnLSdcmjKFMcSgVTlRmkk6kJo36X0kR1eNTYRixorrOXhVKX6hvbxTjpAaArJqtwaff8jrDnsEj0xeRKLaSwtPMu63BF4gvR_-Mk9ut5YulVjHDkiNR5mBXgll3LUcjmCv0-hH6H/s900/channels4_profile%20%283%29.jpg",
        fanart="https://1.bp.blogspot.com/-0ecnBpV9cMU/YKZ0ksrvq-I/AAAAAAABs7k/YVRBCuXh3pA_K4ArBWqnb3oubzn8MlhtwCLcBGAsYHQ/s1920/david-kohler-VFRTXGw1VjU-unsplash.jpg",
        folder=True ) 
        
        
    plugintools.add_item( 
        #action="", 
        title="DW Documental",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID9+"/",
        thumbnail="https://1.bp.blogspot.com/-wRK6k6XTNTo/YKQDNkHLvhI/AAAAAAABs7A/BtcXQgKsiKsw8-MhyEdN7L4X2LcSyCSqQCLcBGAsYHQ/s900/unnamed%2B%25286%2529.jpg",
        fanart="https://1.bp.blogspot.com/-px579CXQ2p0/YKQDGscbYXI/AAAAAAABs68/-UzP_ltdH-0W10ETkxrZFAUCME6v2PoWACLcBGAsYHQ/s1200/importancia-de-los-iconos-en-la-creacion-de-paginas-web.jpg",
        folder=True )             
   
    
    plugintools.add_item( 
        #action="", 
        title="Wild Stories",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID1+"/",
        thumbnail="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgPwCs9Gv2L_1U3QI3egd62aSlCZieYINooFpFVUV9c2lcBgsjaI0ja97po99Pm7OVAjUPxXrn9M0ZG6AaZJOtCOIiG9qscLv67efN5pfJ2ERDpJZOTrS8P0TzyRGn5it6e6D7QPboUC6tzUMXv1sMkCGe8CS1tLvbt75geCQgYARSnYk6qwdSswoBfYLUT/s900/channels4_profile.jpg",
		fanart="https://1.bp.blogspot.com/-piQo6wAYXdI/YKKLYuVmoII/AAAAAAABs4o/M0BVKhk4t5wjzQdedJ9f0e5qMR8t9T06ACLcBGAsYHQ/s1920/bailey-zindel-NRQV-hBF10M-unsplash.jpg",
        folder=True )     
        
    plugintools.add_item( 
        #action="", 
        title="Lethal Crysis",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID4+"/",
        thumbnail="https://1.bp.blogspot.com/-YgbRGkUPIkk/YKPv3e44x3I/AAAAAAABs5E/wBK35zRhwIc3v_U1Gg81H8zB58eFIE5yQCLcBGAsYHQ/s802/icon.jpg",
        fanart="https://1.bp.blogspot.com/-mW0Ub3CWgl8/YKPvv45NXuI/AAAAAAABs5A/B5098cWDV3gQZXWOqkMrP_E60Hp99AC5ACLcBGAsYHQ/s1280/EZh45pKWkAcEqlT.jpg",
        folder=True )
        
       
    plugintools.add_item( 
        #action="", 
        title="Rubén Villalobos",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID2+"/",
        thumbnail="https://1.bp.blogspot.com/-PM45NLHVqBw/YKPz656_K4I/AAAAAAABs5g/iA8feIg5bgMNiUB1qvFBRKmFvwKrm7-uQCLcBGAsYHQ/s900/unnamed%2B%25282%2529.jpg",
        fanart="https://1.bp.blogspot.com/-7xxLs0WGnDQ/YKPzydNuA0I/AAAAAAABs5c/fa-bo2-Wd8UJWebYhJvln6mXALkfez0XQCLcBGAsYHQ/s1920/aussieactive-oTRD-P4nU8Q-unsplash.jpg",
        folder=True )    
  
    plugintools.add_item( 
        #action="", 
        title="Planet Doc",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID5+"/",
        thumbnail="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhF_L-C18h5wU8TpLL8S7g8Bkid7gtVTix2x73dJ6Qn5KgZjaJicHYXj3Emk4RCmtW6sTC50uDnhASYdVzaT2al5HCSlBz6pq3dwD_zIAfWPV0QhIhOZRBfmQzecntXvCgkCc-VG0fcTMvTDDlXjHlEoM2iGJtWR5rubZYCdX6c0imyzTGdOBiVNtFLGkv9/s420/OIP.jpg",
        fanart="https://1.bp.blogspot.com/-YgBD0TXydaA/YKPyB_d0S1I/AAAAAAABs5U/63gXTSXvG40cTwEwzMDQvXTCGDxZZ3fKQCLcBGAsYHQ/s1920/kalen-emsley-Bkci_8qcdvQ-unsplash.jpg",
        folder=True )  
        
           
           
    plugintools.add_item( 
        #action="", 
        title="Documentales Gratuitos",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID3+"/",
        thumbnail="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiwXDq1c_7WYGV4AQ2irvK9lzwn3AWgCA825YwhJAOwWDXZJ9pYUeXMiiuOvbvC3dIt-at1h8ceWYK0KtaDCoapBo_Evx6V76PS7Dx4Kw3yxzqiKhY4ZpEclaj-o96nX4pRUGVYQSGzf1WRZR70pcWb7IdoZ2nF2XCtBhL7wMmvj4cyFOc0aT49YT5bIzJb/s340/world-1348808__340.jpg",
        fanart="https://1.bp.blogspot.com/-q1QGyYBzvE8/YKP3aWA88JI/AAAAAAABs50/IVqAIEcdzfYBzTrczWTswebBgKZqkSPnQCLcBGAsYHQ/s1920/ken-cheung-KonWFWUaAuk-unsplash.jpg",
        folder=True )    
        
                   
    plugintools.add_item( 
        #action="", 
        title="Documental Z",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID6+"/",
        thumbnail="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgeSwLwFBx4nZ6x1DVPLWgfwtWO-kpVwOgHClwJ_wilEBGn7RAPHF2lcWzOHTQrCO5QRRIU_AxXAZWjO5E3XX-k1FH_xsCiPqqTc5RrXXvdgwUP8njWMQWMTxa0tzHRz_Q_EGaAmGfz1P6ZbGkfEJ4oTvXUW-zeRQ4dv-RE_Sn218KtfhRvERcG5r-3_9XY/s900/channels4_profile%20%281%29.jpg",
        fanart="https://1.bp.blogspot.com/-I3rf6DBsmew/YKP5Q6DvAsI/AAAAAAABs58/Wl19C0WAlRc35CJHhQhFmNGaxNyfv9igQCLcBGAsYHQ/s1920/shot-by-cerqueira-0o_GEzyargo-unsplash.jpg",
        folder=True ) 
    
    
    plugintools.add_item( 
        #action="", 
        title="Misterios Ocultos",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID7+"/",
        thumbnail="https://1.bp.blogspot.com/-EXX99ypIUo0/YKP7Q-Xx2aI/AAAAAAABs6U/FtV_s_2EGEgFitNC-ZZSs1XPRtkkK8PxACLcBGAsYHQ/s900/unnamed%2B%25285%2529.jpg",
        fanart="https://1.bp.blogspot.com/-SVgn9sffdrs/YKP7KgVyH_I/AAAAAAABs6Q/g6JrjjTo1Cwfb7xWuS7DFiEo-Mwgh3TowCLcBGAsYHQ/s1280/maxresdefault.jpg",
        folder=True ) 
            
            
    plugintools.add_item( 
        #action="", 
        title="Daniel Geohistoria",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID8+"/",
        thumbnail="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhFboFlvH1Ow06mxprdVZGPr7sncfbuNzpCABzK3QrRbkV3rRrmwxT57mkLFUyfyNnYie6t6ZZri770wRWcEDFMDBNvKZcKPoN-tuqeaJqA0ikmtPj9W5l_0h6X69ckKH2GYFGycSZQ0nzXKN0eEeXoVHpSYgwAAkl0mn8OL2Xz716Z58gGFsQDqfj6WVS5/s176/unnamed.jpg",
        fanart="https://1.bp.blogspot.com/-o13XJDHn_WA/YKQApav223I/AAAAAAABs6s/Bw3XRZH9HoMpdb9FMC37oeFJRY7hc721QCLcBGAsYHQ/s1920/actionvance-t7EL2iG3jMc-unsplash.jpg",
        folder=True )         

    
   
    plugintools.add_item( 
        #action="", 
        title="DTOM",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID10+"/",
        thumbnail="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhCQ5CUujnUZ2qkP_ZfseUKFHkNGE1pF7_6KylJVQAoG9s_aDh_2etsSe3EMrmugI72cwOlHFEzCfpS36Ff4dELzKlapeeQcCxq_DXlKXcZocgF9dcG2SW25AIJLQnlozYvj8gWApTJmhrrnD3QdPM0D9g0lrCr4OxOfuHbq-g51tLK5cD-RJ8yQnNHq_Ty/s900/channels4_profile%20%282%29.jpg",
        fanart="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhjps-GZpx9Ur8DFsSHF3ENYnS7fL-2EsyLzyPpEazewl2OLzp-vB0ot6pk2ncl51h3db2-mWmUtpgLzdCSH9VFKtxkksNwP1IYH475NcJ0MMETYikhUWPIZRhzakR39DKOO84DegkE2FSxsbroVa_5F7OgwKkib64w-0NMG6wkXwa78OX1LmtPk0d1Blcu/s2400/matt-popovich-7mqsZsE6FaU-unsplash%20%281%29%20%281%29.jpg",
        folder=True )  
         

 
    plugintools.add_item( 
        #action="", 
        title="Academia Play",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID13+"/",
        thumbnail="https://1.bp.blogspot.com/-eGN8kls3K-A/YKkScvIZoUI/AAAAAAABs8M/6ehj40XnpDIqadkJaePguXbl7yPxhTJogCLcBGAsYHQ/s225/descarga.jpg",
        fanart="https://1.bp.blogspot.com/-RRy1vV1G-3U/YKkSljD_g2I/AAAAAAABs8Q/iOUS7IrID7MF_9zjZPJVwIqWtNEYtYNDACLcBGAsYHQ/s1280/maxresdefault%2B%25281%2529.jpg",
        folder=True ) 
        
    plugintools.add_item( 
        #action="", 
        title="Pero eso es otra Historia",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID12+"/",
        thumbnail="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgJFx4TSdwGjZ-Y7IRU1wBrepXyWZ666KH5eDOY4Z-5mRaXWUHFlv9xZdWETwcmKMysruWTmN-wIofFtaqWCtxfHaddk_wRhTlrEwm-f87zsivMhmxvbh2LM0XDkCSDhl9GnLQkI2JoXftfRFGmqDtnMiYCkD645jqfZO0Dyw52F0BkfQVKQPg_5mc-UJEk/s900/unnamed%20%281%29.jpg",
        fanart="https://1.bp.blogspot.com/-iC9v8AH0eJg/YKkUNQ_rwyI/AAAAAAABs8k/md1Pv0iaa8kEpi2t6Mv4T6lPHhhSuPzjwCLcBGAsYHQ/s1365/Tierra_planeta.jpg",
        folder=True ) 

    plugintools.add_item( 
        #action="", 
        title="Explora Planet",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID14+"/",
        thumbnail="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj62EhgxX2j47l2VN9BWvJPZkFL1NqYXriL3aNNoGJ7qOK503SI2361_eR-FXIlV_3t6IEl_Z1v_iV_TLrmD0lz7BBrAzRVohLlKncAELd84vjqolDsx9e-DFoNO9OS1iu2yQnYct8LygeGkfIqY2e80q6pgzrTCHoeBqeVSO_2wHVqOGKCGuQ0UOJl-J5a/s900/unnamed.jpg",
        fanart="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi4AzmKhDFv3OVv6UGT-SvMCXWt7nUY7pY6wpu4RXChv6c0Oqk0x-M2uxTD8N0rpnquwbkeMS3anQrJ3NMJAHF1T5hXwdPi2KXVJNQgxhL5QAscdX3K9WeRK7VO_RegdwHDxLPyh6_sqzdugpNpYsR5bI8AsPBS0f10htkMI-OsvsAMWjUfUGD6fQ7tZKiG/s4608/adam-bouse-qfi4bEHYhOA-unsplash%20%281%29.jpg",
        folder=True ) 
        
        
    plugintools.add_item( 
        #action="", 
        title="Show Me the World",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID15+"/",
        thumbnail="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjaLSBJKbfYiyrDs8FpU4MwJCWrjCx9fAurlpzuj1jqbEpjZXmY52WCDlU4iV1Qb8BgzZVDhA0nnQDVYEwIls4VC97WeJbEMQ9W3APp5-i8KcMIxITzCf1PyRKwkB5oi3_PG04xUsK46sgGPFc8h7PDnfgLna1CUWsd4CSr511uykORE2pOnuVZ-9-iAL1P/s176/unnamed.jpg",
        fanart="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh6mgOuVr11XnOIMLIStJsbiieLQr2PcNPTuhwtrXxk_ecOBNv83CD4N9Ybxb8hUpyle7TJHUqcBiiNN9imDY3TjIz3pQiDwzdlrMjaNPpWH9zlwp0sSWxZVQ-v9VOppVLyl_cH0sfpLtivkf9Gfe9v3L5dmvdL2Z8iS0etgSbUWpYRUG1GJfuoK6_QWH3N/s3578/actionvance-t7EL2iG3jMc-unsplash%20%281%29.jpg",
        folder=True ) 

    plugintools.add_item( 
        #action="", 
        title="Historias Vivas",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID16+"/",
        thumbnail="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjkLAbqM76gUWDPDFtfSw07ZavKiDq23Mcto8TqUmrsgDiR95db2hsFUzr7KnoAKfbVjTSYyCbz_px-FFXpndyiVLxgAMBuI3Oz445Blcy_AButMV_Avw1Ccif7DzthnV9hosj1gUU7mzaBRcbuPkkpgvEcfM949Eoz_kg6pXWMb-OI0eKoscKdXDnBpBwA/s900/channels4_profile.jpg",
        fanart="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg5umrWojMDV1_PXhcZzTyNy9hoK8ojDO-8HAH-tKROIODHhrA3s77QJp6r5Aa3iwA4YuV6ydqsSV0Xp3aLexIA2kUsIheCV910KLBEFOC4q7sUul52726je-7ROlXmedFk4SqU7tUmeLid1xbHTme5t7CHx0VIwhoA4LMmoAA0XCQi2vjQF2LGx7ITtoQ2/s2600/qingbao-meng-01_igFr7hd4-unsplash%20%281%29.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="Documania Historia",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID17+"/",
        thumbnail="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjJ9iGEPExiFqNMXJBtOkEEc-uNJChxe7CGLlPapelSNTukc8LpE8CVFEK34eIWeTuPQHDXO9OLujWNdjRQZASzPLU3hIIqS2xNALuiIqbJvkCckHAjEFGRXUAXWgf_odMsduj_6nfXRFU3_ufWwxo-J2Fk-nASyRpNpLQYiSwbwEMoc-YZfEDVqP1HE_hk/s900/channels4_profile.jpg",
        fanart="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhVtnHi8e3iofbGInYdhp0FhebrqZ4kRWmwpTD2dlXqV9s8hfTyrHfkhUzaXAHtyvaspAp4FtHi-kI9u7g_gSf7t6BbunRXZEarbNP-vyASMKGjNdeCrSFHcuBdH4U08YMbTxUsil9XKgL4IYc61GxpkbWVQwmzshBe5e3eCFfDnIBXGRZEwAqUrEmoAL54/s2400/ronda-darby-HbMLSB-uhQY-unsplash%20%281%29.jpg",
        folder=True )          
        
        
run()