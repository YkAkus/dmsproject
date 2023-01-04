FTP_HOST = "216.48.190.85"
FTP_USER = "root"
FTP_PASS = "EXSRXF@deuku725"
# FTP_HOST = "216.48.189.99"
# FTP_USER = "root"
# FTP_PASS = "NHYKXN@sxpkc988"
def time(time):
    import datetime
    return datetime.datetime.fromtimestamp(int(time))

def test(username, r, folder=None):
    import pysftp as sftp
    cnopts = sftp.CnOpts()
    cnopts.hostkeys = None
    with sftp.Connection(host=FTP_HOST, username=FTP_USER, password=FTP_PASS, cnopts=cnopts) as sftp:
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
        
        if r=='admin':
            if folder:
                sftp.cwd(f'/JnP/{folder.replace("%20", " ")}/')
            else:
                sftp.cwd(f'/JnP/')
        elif r=='Rh_operator':
            if folder:
                sftp.cwd(f'/JnP/B/{folder.replace("%20", " ")}/')
            else:
                sftp.cwd(f'/JnP/B/')
        elif r=='Rp_operator':
            if folder:
                sftp.cwd(f'/JnP/A/{folder.replace("%20", " ")}/')
            else:
                sftp.cwd(f'/JnP/A/')
        else:
            if folder:
                sftp.cwd(f'/JnP/{username}/{folder.replace("%20", " ")}/')
            else:
                sftp.cwd(f'/JnP/{username}/')
        sftp.put(file)
        print("File uploading is successfully")
    return

def delfile(username, r, file, folder=None):
    import pysftp as sftp
    cnopts = sftp.CnOpts()
    cnopts.hostkeys = None
    with sftp.Connection(host=FTP_HOST, username=FTP_USER, password=FTP_PASS, cnopts=cnopts) as sftp:
        
        if r=='admin':
            if folder:
                sftp.cwd(f'/JnP/{folder.replace("%20", " ")}/')
            else:
                sftp.cwd(f'/JnP/')
        elif r=='Rh_operator':
            if folder:
                sftp.cwd(f'/JnP/B/{folder.replace("%20", " ")}/')
            else:
                sftp.cwd(f'/JnP/B/')
        elif r=='Rp_operator':
            if folder:
                sftp.cwd(f'/JnP/A/{folder.replace("%20", " ")}/')
            else:
                sftp.cwd(f'/JnP/A/')
        else:
            if folder:
                sftp.cwd(f'/JnP/{username}/{folder.replace("%20", " ")}/')
            else:
                sftp.cwd(f'/JnP/{username}/')
        sftp.remove(file)
    return

def delfolder(username, r,id, folder=None):
    import pysftp as sftp
    cnopts = sftp.CnOpts()
    cnopts.hostkeys = None
    con = sftp.Connection(FTP_HOST, username=FTP_USER, password=FTP_PASS, cnopts=cnopts)
    # if r:
    #     if folder:
    #         dirs = [f'/JnP/{folder.replace("%20", " ")}/{id}/']
    #     else:
    #         dirs = [f'/JnP/{id}/']
    # else:
    #     if folder:
    #         dirs = [f'/JnP/{username}/{folder}/{id}/']
    #     else:
    #         dirs = [f'/JnP/{username}/{id}/']
    
    if r=='admin':
        if folder:
            dirs = [f'/JnP/{folder.replace("%20", " ")}/{id}/']
        else:
            dirs = [f'/JnP/{id}/']
    elif r=='Rh_operator':
        if folder:
            dirs = [f'/JnP/B/{folder.replace("%20", " ")}/{id}/']
        else:
            dirs = [f'/JnP/B/{id}/']
    elif r=='Rp_operator':
        if folder:
            dirs = [f'/JnP/A/{folder.replace("%20", " ")}/{id}/']
        else:
            dirs = [f'/JnP/A/{id}/']
    else:
        if folder:
            dirs = [f'/JnP/{username}/{folder.replace("%20", " ")}/{id}/']
        else:
            dirs = [f'/JnP/{username}/{id}/']

    # print(dirs[0])
    con.walktree(dirs[0], fcallback=con.remove, dcallback=dirs.append, ucallback=con.remove, recurse=True)

    # print(dirs)

    for d in reversed(dirs):
        # print("Delete directory", d)
        con.rmdir(d)
        
    con.close()
    return
