FTP_HOST = "216.48.189.99"
FTP_USER = "root"
FTP_PASS = "NHYKXN@sxpkc988"
def time(time):
    import datetime
    return datetime.datetime.fromtimestamp(int(time))

def test(username, folder=None):
    import pysftp as sftp
    cnopts = sftp.CnOpts()
    cnopts.hostkeys = None
    with sftp.Connection(host=FTP_HOST, username=FTP_USER, password=FTP_PASS, cnopts=cnopts) as sftp:
        print("Connection succesfully stablished ... ")
        if folder:
            sftp.cwd(f'/JnP/{username}/{folder}/')
        else:
            sftp.cwd(f'/JnP/{username}/')
        # sftp.cwd('/akus5/')
        # if sftp.is
        files = sftp.listdir_attr(".")
        # print(files)
        res = sftp.listdir()
        fo={}
        fi={}
        for a in sftp.listdir_attr():
            if sftp.isdir(a.filename)==True:
                fo.update({a.filename:{"size":a.st_size,"mtime":time(a.st_atime),"atime":time(a.st_mtime),"perm":a.st_mode}})
            else:
                fi.update({a.filename:{"size":a.st_size,"mtime":time(a.st_atime),"atime":time(a.st_mtime),"perm":a.st_mode}})
        return fo,fi
def createfol(username,folname, folder=None):
    import pysftp as sftp
    cnopts = sftp.CnOpts()
    cnopts.hostkeys = None
    with sftp.Connection(host=FTP_HOST, username=FTP_USER, password=FTP_PASS, cnopts=cnopts) as sftp:
        print("Connection succesfully stablished ... ")
        if folder:
            sftp.cwd(f'/JnP/{username}/{folder.replace("%20", " ")}/')
        else:
            sftp.cwd(f'/JnP/{username}/')
        sftp.mkdir(folname, mode=777)
        print("Folder created successfully")
    return

def upfile(username,file, folder=None):
    import pysftp as sftp
    cnopts = sftp.CnOpts()
    cnopts.hostkeys = None
    with sftp.Connection(host=FTP_HOST, username=FTP_USER, password=FTP_PASS, cnopts=cnopts) as sftp:
        print("Connection succesfully stablished ... ")
        if folder:
            sftp.cwd(f'/JnP/{username}/{folder.replace("%20", " ")}/')
        else:
            sftp.cwd(f'/JnP/{username}/')
        sftp.put(file)
        print("File uploading is successfully")
    return


