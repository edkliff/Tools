import paramiko, datetime

from config import FTP_HOST, FTP_PASSWD, FTP_USER, PATH_IN_FTP, COUNT

"""
Small tool for removing old backups
"""

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=FTP_HOST, username=FTP_USER, password=FTP_PASSWD)
ftp_client = ssh_client.open_sftp()
files = sorted(ftp_client.listdir(PATH_IN_FTP), reverse=True)

date_now = datetime.datetime.now().date()


def bases_names(filelist):
    basenames = []
    for file in filelist:
        z = file.split('.')[0]
        basenames.append(z)
    basenames = tuple(set(basenames))
    return basenames


def backup(filename):
    print('{} not prepared. I will spare him. For now.'.format(filename))


def destroy(filename):
    print('DESTRUCTION {}{}'.format(PATH_IN_FTP, filename))
    try:
        ftp_client.remove(PATH_IN_FTP + filename)
    except:
        print('I have problem with {}'.format(filename))


types = bases_names(files)
base_types_dict = {base: COUNT for base in types}

for i in files:
    isplit = i.split('.')
    base_type = isplit[0]
    backup_time_list = [int(e) for e in isplit[1].split('_')[0].split('-')]
    backup_day = backup_time_list[2]
    if base_types_dict[base_type] == 0 and backup_day != 1:
        destroy(i)
    elif backup_day == 1:
        backup(i)
    else:
        base_types_dict[base_type] -= 1
        backup(i)
