#SFTP Configuration file
#filename: SFTPConfig.py

import pysftp
import os


class SFTPConfig(object):
    """description of class"""
    
    host = ""
    port = 0
    username = ""
    password = ""
    
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None
    note = ""
    localpath = ""
    remotepath = ""
    
    ROOT_DIR = os.path.dirname(os.path.abspath("./"))
    PROJ_DIR = os.path.abspath(os.curdir)

    

    def BuildCacheDir(self, CacheDir):
        #if(CacheDir):
        # Check whether the specified path exists or not
        
        if not os.path.exists(CacheDir):
            os.makedirs(CacheDir)

        return CacheDir


    def eabConfig(self):

        self.host = "ft.royall.com"
        self.port = 22
        self.username = "puru.panta"
        self.password = "yh6ffty6z9h"
        self.cnopts.hostkeys = None
        self.localpath = self.BuildCacheDir(self.PROJ_DIR + "\\CacheDir\\")
        self.remotepath = "/UNIVERSITY_OF_KENTUCKY_810_93DF/Search_responders/"

        self.note = "NA"

    def SFTPConfig(self, ESType):
        if(ESType == "eab"):
            self.eabConfig()
    
    

