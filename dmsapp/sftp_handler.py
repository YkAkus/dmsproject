# FTP_HOST = "216.48.190.85"
# FTP_USER = "root"
# FTP_PASS = "EXSRXF@deuku725"
FTP_HOST = "216.48.189.99"
FTP_USER = "root"
FTP_PASS = "NHYKXN@sxpkc988"
def time(time):
    import datetime
    return datetime.datetime.fromtimestamp(int(time))

def test(username, r, folder=None):
    import pysftp as sftp
    cnopts = sftp.CnOpts()
    cnopts.hostkeys = None
    with sftp.Connection(host=FTP_HOST, username=FTP_USER, password=FTP_PASS, cnopts=cnopts) as sftp:
        print("Connection succesfully stablished ... ")
        if r=='admin':
            if folder:
                sftp.cwd(f'/JnP/{folder}/')
            else:
                sftp.cwd(f'/JnP/')
        elif r=='Rh_operator':
            if folder:
                sftp.cwd(f'/JnP/B/{folder}/')
            else:
                sftp.cwd(f'/JnP/B/')
        elif r=='Rp_operator':
            if folder:
                sftp.cwd(f'/JnP/A/{folder}/')
            else:
                sftp.cwd(f'/JnP/A/')
        else:
            if folder:
                sftp.cwd(f'/JnP/{username}/{folder}/')
            else:
                sftp.cwd(f'/JnP/{username}/')
        fo={}
        fi={}
        for a in sftp.listdir_attr():
            if sftp.isdir(a.filename)==True:
                fo.update({a.filename:{"size":a.st_size,"mtime":time(a.st_atime),"atime":time(a.st_mtime),"perm":a.st_mode}})
            else:
                fi.update({a.filename:{"size":a.st_size,"mtime":time(a.st_atime),"atime":time(a.st_mtime),"perm":a.st_mode}})
        return fo,fi
def createfol(username,folname,r, folder=None):
    import pysftp as sftp
    cnopts = sftp.CnOpts()
    cnopts.hostkeys = None
    with sftp.Connection(host=FTP_HOST, username=FTP_USER, password=FTP_PASS, cnopts=cnopts) as sftp:
        print("Connection succesfully stablished ... ")
        if r=='admin':
            if folder:
                sftp.cwd(f'/JnP/{folder}/')
            else:
                sftp.cwd(f'/JnP/')
        elif r=='Rh_operator':
            if folder:
                sftp.cwd(f'/JnP/B/{folder}/')
            else:
                sftp.cwd(f'/JnP/B/')
        elif r=='Rp_operator':
            if folder:
                sftp.cwd(f'/JnP/A/{folder}/')
            else:
                sftp.cwd(f'/JnP/A/')
        else:
            if folder:
                sftp.cwd(f'/JnP/{username}/{folder}/')
            else:
                sftp.cwd(f'/JnP/{username}/')
        sftp.mkdir(folname, mode=777)
        print("Folder created successfully")
    return

def upfile(username,file,r, folder=None):
    import pysftp as sftp
    cnopts = sftp.CnOpts()
    cnopts.hostkeys = None
    with sftp.Connection(host=FTP_HOST, username=FTP_USER, password=FTP_PASS, cnopts=cnopts) as sftp:
        print("Connection succesfully stablished ... ")
        if r=='admin':
            if folder:
                sftp.cwd(f'/JnP/{folder.replace("%20", " ")}/')
            else:
                sftp.cwd(f'/JnP/')
        elif r=='Rh_operator':
            if folder:
                sftp.cwd(f'/JnP/B/{folder}/')
            else:
                sftp.cwd(f'/JnP/B/')
        elif r=='Rp_operator':
            if folder:
                sftp.cwd(f'/JnP/A/{folder}/')
            else:
                sftp.cwd(f'/JnP/A/')
        else:
            if folder:
                sftp.cwd(f'/JnP/{username}/{folder}/')
            else:
                sftp.cwd(f'/JnP/{username}/')
        sftp.put(file)
        print("File uploading is successfully")
    return


def filedelete(username,file):
    import pysftp as sftp
    cnopts = sftp.CnOpts()
    cnopts.hostkeys = None
    with sftp.Connection(host=FTP_HOST, username=FTP_USER, password=FTP_PASS, cnopts=cnopts) as sftp:
        print("Connection succesfully stablished ... ")
        sftp.cwd(f'/JnP/{username}/')
        sftp.remove(file)
    return(("File is remove successfully"))



def search(username, searched, r=None, folder=None):
    import pysftp as sftp
    cnopts = sftp.CnOpts()
    cnopts.hostkeys = None
    with sftp.Connection(host=FTP_HOST, username=FTP_USER, password=FTP_PASS, cnopts=cnopts) as sftp:
        sftp.cwd(f'/JnP/{username}/')
        print("Connection succesfully stablished ... for search ")
        # if r:
        #     if folder:
        #         sftp.cwd(f'/JnP/{folder}/')
        #     else:
        #         sftp.cwd(f'/JnP/')
        # else:
        #     if folder:
        #         sftp.cwd(f'/JnP/{username}/{folder}/')
        #     else:
        #         sftp.cwd(f'/JnP/{username}/')
        fo={}
        fi={}
        for a in sftp.listdir_attr():
            temp=""
            temp=a.filename.find(searched)
            print(temp)
            if temp != -1:
                if sftp.isdir(a.filename)==True:
                    fo.update({a.filename:{"size":a.st_size,"mtime":time(a.st_atime),"atime":time(a.st_mtime),"perm":a.st_mode}})
                else:
                    fi.update({a.filename:{"size":a.st_size,"mtime":time(a.st_atime),"atime":time(a.st_mtime),"perm":a.st_mode}})
        return fo,fi