import xbmc, xbmcaddon
import sqlite3
import xbmcvfs
import os
from libs.common import var
from sqlite3 import Error

#Account Manager Metadata
accountmgr = xbmcaddon.Addon("script.module.accountmgr")
your_omdb_api = accountmgr.getSetting("omdb.api.key")

###################### Connect to Database ######################
def create_conn(db_file):
    try:
        conn = None
        try:
            conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)

        return conn
    except:
        xbmc.log('%s: Meta_db Connect Failed!' % var.amgr, xbmc.LOGINFO)
        pass

########################## Metadata #########################
def connect_meta(conn, setting):
    try:
        # Update settings database
        omdb_api = ''' UPDATE settings
                  SET setting_value = ?
                  WHERE setting_id = ?'''

        cur = conn.cursor()
        cur.execute(omdb_api, setting)
        conn.commit()
        cur.close()
    except:
        xbmc.log('%s: Meta_db Auth Failed!' % var.amgr, xbmc.LOGINFO)
        pass



    
#################### Auth Fen Light Metadata ###################
def auth_fenlt_meta():
    try:
        # Create database connection
        conn = create_conn(var.fenlt_settings_db)
        with conn:
            connect_meta(conn, (your_omdb_api, 'omdb_api'))
    except:
        xbmc.log('%s: Meta_db Fen Light Failed!' % var.amgr, xbmc.LOGINFO)
        pass



#################### Auth afFENityt Metadata ###################
def auth_affen_meta():
    try:
        # Create database connection
        conn = create_conn(var.affen_settings_db)
        with conn:
            connect_meta(conn, (your_omdb_api, 'omdb_api'))
    except:
        xbmc.log('%s: Meta_db afFENity Failed!' % var.amgr, xbmc.LOGINFO)
        pass
