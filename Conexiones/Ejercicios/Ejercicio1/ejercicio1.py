import ftplib

def transfer_file(hostname, username, password, local_file, remote_file, mode='upload'):
    try:
        with ftplib.FTP() as conn:
            print("connect FTP")
            conn.connect(hostname, 21)
            conn.login(username, password)
            conn.cwd('/') 
            print(conn.pwd()) 
            print(conn.getwelcome()) 

            if mode == 'upload':
                with open(local_file,'rb') as f:
                    conn.storbinary(f'STOR {remote_file}', f)
                f.close()
                print(f'Successfully transferred {local_file} to {hostname}/{remote_file}')
            elif mode == 'download':
                with open(local_file,'wb') as f:
                    conn.retrbinary(f'RETR {remote_file}', f.write)
                f.close()
                print(f'Successfully transferred {hostname}/{remote_file} to {local_file}')
            
            conn.retrlines("LIST")
            print("FTP end")
        
    except ftplib.all_errors as e:
        print(f'Error: {e}')


hostname = '127.0.0.1'
username = 'admin'
password = 'preguntaraalguien'
local_file = 'file.txt'
remote_file = 'file2.txt'

transfer_file(hostname, username, password, local_file, remote_file)
transfer_file(hostname, username, password, remote_file, remote_file,'download')

