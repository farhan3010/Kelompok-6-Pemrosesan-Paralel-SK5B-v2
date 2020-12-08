import paramiko
import socket

def masuk_luas():
    masuk=True
    while masuk==True:
        print("\n1. Luas Persegi\n2. Luas Segitiga\n3. Luas Lingkaran")
        input_luas=input("Masukkan mau luas apa (1/2/3): ")
        if input_luas=='1':
            sisi = float(input("Masukkan sisi persegi : "))
            tulis = open("inputpersegi.txt","w")
            tulis.write("{} {}".format(sisi,sisi))
            tulis.close()
            masuk=False
                
        elif input_luas=='2':
            alas = float(input("Masukkan alas segitiga : "))
            tinggi = float(input("Masukkan tinggi segitiga : "))
            tulis = open("inputsegitiga.txt","w")
            tulis.write("{} {}".format(alas, tinggi))
            tulis.close()
            masuk=False

        elif input_luas=='3':
            jari = float(input("Masukkan jari-jari lingkaran : "))
            tulis = open("inputlingkaran.txt","w")
            tulis.write("{} {}".format(jari, jari))
            tulis.close()
            masuk=False
                
        else:
            print("Maaf, ", input_luas, " tidak tersedia. Coba lagi!")

    return input_luas

#----------------------------------------------------------------------

keluar=False
while keluar==False:
    print("1. PC1\n2. PC2")
    input_pc=input("Masukkan mau masuk PC berapa (1/2): ")
    if input_pc=='1':
        ip = "xxx.xxx.xxx.xxx" #ganti jadi ip ubuntu
        usern = "xxxxxxxx" #ganti jadi username ubuntu
        passw = "xxxxxxxx" #ganti jadi password ubuntu
    elif input_pc=='2':
        ip = "xxx.xxx.xxx.xxx" #ganti jadi ip ubuntu
        usern = "xxxxxxxx" #ganti jadi username ubuntu
        passw = "xxxxxxxx" #ganti jadi password ubuntu
    else:
        print("Maaf, ", input_pc, " tidak tersedia. Coba lagi!")
        continue
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh_client.connect(hostname= ip,username= usern,password= passw,timeout=3)
        sftp = ssh_client.open_sftp()
        input_luas = masuk_luas()
        if input_luas=='1':
            sftp.put("inputpersegi.txt","inputpersegi.txt")
            #sftp.put("luaspersegi.py","luaspersegi.py")
            stdin,stdout,stderr=ssh_client.exec_command("python3 luaspersegi.py")
        elif input_luas=='2':
            sftp.put("inputsegitiga.txt","inputsegitiga.txt")
            #sftp.put("luassegitiga.py","luassegitiga.py")
            stdin,stdout,stderr=ssh_client.exec_command("python3 luassegitiga.py")
        elif input_luas=='3':
            sftp.put("inputlingkaran.txt","inputlingkaran.txt")
            #sftp.put("luaslingkaran.py","luaslingkaran.py")
            stdin,stdout,stderr=ssh_client.exec_command("python3 luaslingkaran.py")
        baca = stdout.readlines()
        baca_err = stderr.readlines()

        for i in baca_err:
            print(i)
        for i in baca:
            print(i)

    except (socket.timeout):
        print("\nMaaf, PC sedang offline\n")

    input_keluar=input("Keluar (y/n): ")
    if input_keluar=='y':
        keluar=True