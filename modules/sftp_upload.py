# -*- coding: utf-8 -*-
import pysftp

def sftp_upload(sftp_server, sftp_user, sftp_pass, target_folder, put_file, old_name, new_name):
    with pysftp.Connection(sftp_server, username=sftp_user, password=sftp_pass) as sftp:
        with sftp.cd(target_folder):
            if sftp.exists(new_name) and sftp.exists(old_name):
                try:
                    sftp.remove(new_name)
                    sftp.remove(old_name)
                    sftp.put(put_file)
                    sftp.rename(old_name, new_name)
                    print "was 2 files"
                except IOError as err:
                    print "was 2 files ", err 
            elif sftp.exists(old_name):
                try:
                    sftp.remove(old_name)
                    sftp.put(put_file)
                    sftp.rename(old_name, new_name)
                except IOError as err:
                    print "was 1 file before remame", err
            elif sftp.exists(new_name):
                try:
                    sftp.remove(new_name)
                    sftp.put(put_file)
                    sftp.rename(old_name, new_name)
                except IOError as err:
                    print "was 1 file after remame", err
            else:
                try:
                    sftp.put(put_file)
                    sftp.rename(old_name, new_name)
                except IOError as err:
                    print "was no any file", err