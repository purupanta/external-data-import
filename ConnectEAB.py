#Integrate EAB SFTP
#filename: ConnectEAB.py

import pysftp
import fnmatch
#import SFTPConfig
from SFTPConfig import SFTPConfig
from datetime import datetime

def ProcessEAB():
    try:

        SC = SFTPConfig()
        SC.SFTPConfig(ESType = "eab")

        ##cnopts = sftp.CnOpts(knownhosts='known_hosts')
        #cnopts.hostkeys = None
       
        sftp_ = pysftp.Connection(host= SC.host, port= SC.port, cnopts= SC.cnopts, username= SC.username, password= SC.password)
        #with pysftp.Connection(host= SC.host, port= SC.port, cnopts= SC.cnopts, username= SC.username, password= SC.password):
        

        #for filename in sftp.listdir('/remote/path'):
            #if fnmatch.fnmatch(filename, "*.txt"):
                #sftp.get("/remote/path/" + filename, "/local/path/" + filename)



        #UK30629_Search_20211020.xlsx
        SC.remotepath = SC.remotepath + "UK30629_Search_20211020.xlsx"
        #SC.remotepath = SC.remotepath + "UK30629_Search_" + datetime.today().strftime('%Y%m%d') + ".xlsx"
        SC.localpath = SC.localpath + "UK30629_Search_20211020.xlsx"
        sftp_.get(SC.remotepath, SC.localpath)

        sftp_.close

    except Exception as e:
        print(str(e))


def RunAll():
    ProcessEAB();

RunAll()
