

import pandas as pd
from tqdm import tqdm


col_list = ["1", "41"]
#df = pd.read_csv("/home/crazyflie/Desktop/vinod/first20.ods", usecols=col_list)
#df1 = pd.read_excel('/home/crazyflie/Desktop/vinod/cut.ods', engine='odf')
df = pd.read_csv('/home/crazyflie/Desktop/vinod/first.csv')
print("hello")
#print(df['C42'])

values=df['C42'].unique()
i=0
for value in tqdm(values):
    #print(value)
    dftemp=df[df['C42']==value]
    #print(dftemp)
    dftemp.to_csv("/home/crazyflie/Desktop/vinod/" +str(i)+str(value)+'csv',index=False)
    i+=1




'''normal = []
back = []
buffer_overflow = []
ftp_write = []
guess_passwd = []
imap = []
ipsweep = []
land = []
loadmodule = []
multihop  = []
neptune  = []
nmap  = []
perl  = []
phf  = []
pod  = []
portsweep  = []
rootkit  = []
satan  = []
smurf  = []
spy  = []
teardrop  = []
warezclient  = []
warezmaster  = []

snmpgetattack = []
httptunnel = []
xsnoop = []
saint = []
processtable = []
mscan = []
mailbomb = []
porsweep = []

dos = []
u2r = []
r2l = []
probe = []
print(df1[2][42])
print(df1.iloc[7])
#print(df)
for i in range( 1,100):#311028):
    data = df1.iloc[i]
    print(data)
    break
    #normal op
    if data == "normal.":
        normal.append(df1.iloc[i])

    #dos attack
    if data == "back.":
        back.append(df1.iloc[i])
        dos.append(df1.iloc[i])
    if data == "neptune.":
        neptune.append(df1.iloc[i])
        dos.append(df1.iloc[i])
    if data == "smurf.":
        smurf.append(df1.iloc[i])
        dos.append(df1.iloc[i])
    if data == "teardrop.":
        teardrop.append(df1.iloc[i])
        dos.append(df1.iloc[i])
    if data == "snmpgetattack.":
        snmpgetattack.append(df1.iloc[i])
        dos.append(df1.iloc[i])

    #u2r attack
    if data == "loadmodule.":
        loadmodule.append(df1.iloc[i])
        u2r.append(df1.iloc[i])
    if data == "buffer_overflow.":
        buffer_overflow.append(df1.iloc[i])
        u2r.append(df1.iloc[i])
    if data == "rootkit.":
        rootkit.append(df1.iloc[i])
        u2r.append(df1.iloc[i])
    if data == "perl.":
        perl.append(df1.iloc[i])
        u2r.append(df1.iloc[i])

    #r2l attack
    if data == "ftp_write.":
        ftp_write.append(df1.iloc[i])
        r2l.append(df1.iloc[i])
    if data == "guess_passwd.":
        guess_passwd.append(df1.iloc[i])
        r2l.append(df1.iloc[i])
    if data == "imap.":
        imap.append(df1.iloc[i])
        r2l.append(df1.iloc[i])
    if data == "multihop.":
        multihop.append(df1.iloc[i])
        r2l.append(df1.iloc[i])
    if data == "phf.":
        phf.append(df1.iloc[i])
        r2l.append(df1.iloc[i])
    if data == "spy.":
        spy.append(df1.iloc[i])
        r2l.append(df1.iloc[i])
    if data == "warezclient.":
        warezclient.append(df1.iloc[i])
        r2l.append(df1.iloc[i])
    if data == "warezmaster.":
        warezmaster.append(df1.iloc[i])
        r2l.append(df1.iloc[i])


    #r2l attack
    if data == "ipsweep.":
        ipsweep.append(df1.iloc[i])
        probe.append(df1.iloc[i])
    if data == "nmap.":
        nmap.append(df1.iloc[i])
        probe.append(df1.iloc[i])
    if data == "portsweep.":
        portsweep.append(df1.iloc[i])
        probe.append(df1.iloc[i])
    if data == "satan.":
        satan.append(df1.iloc[i])
        probe.append(df1.iloc[i])
    if data == "ipsweep.":
        ipsweep.append(df1.iloc[i])
        probe.append(df1.iloc[i])
    
    #other:
    if data == "httptunnel.":
        httptunnel.append(df1.iloc[i])
    if data == "xsnoop.":
        xsnoop.append(df1.iloc[i])
    if data == "saint.":
        saint.append(df1.iloc[i])
    if data == "processtable.":
        processtable.append(df1.iloc[i])
    if data == "mscan.":
        mscan.append(df1.iloc[i])
    if data == "mailbomb.":
        mailbomb.append(df1.iloc[i])
        
    

normaldata = pd.DataFrame(normal)
normaldata.to_csv("/home/crazyflie/Desktop/vinod/data/normaldata.csv")

normaldata = pd.DataFrame(back)
normaldata.to_csv("/home/crazyflie/Desktop/vinod/data/back.csv")

normaldata = pd.DataFrame(buffer_overflow)
normaldata.to_csv("/home/crazyflie/Desktop/vinod/data/buffer_overflow.csv")

normaldata = pd.DataFrame(ftp_write)
normaldata.to_csv("/home/crazyflie/Desktop/vinod/data/ftp_write.csv")

normaldata = pd.DataFrame(guess_passwd)
normaldata.to_csv("/home/crazyflie/Desktop/vinod/data/guess_passwd.csv")

normaldata = pd.DataFrame(imap)
normaldata.to_csv("/home/crazyflie/Desktop/vinod/data/imap.csv")

normaldata = pd.DataFrame(ipsweep)
normaldata.to_csv("/home/crazyflie/Desktop/vinod/data/ipsweep.csv")

normaldata = pd.DataFrame(land)
normaldata.to_csv("/home/crazyflie/Desktop/vinod/data/land.csv")

normaldata = pd.DataFrame(loadmodule)
normaldata.to_csv("/home/crazyflie/Desktop/vinod/data/loadmodule.csv")

normaldata = pd.DataFrame(multihop)
normaldata.to_csv("/home/crazyflie/Desktop/vinod/data/multihop.csv")

normaldata = pd.DataFrame(neptune)
normaldata.to_csv("/home/crazyflie/Desktop/vinod/data/neptune.csv")

normaldata = pd.DataFrame(nmap)
normaldata.to_csv("/home/crazyflie/Desktop/vinod/data/nmap.csv")

normaldata = pd.DataFrame(perl)
normaldata.to_csv("/home/crazyflie/Desktop/vinod/data/perl.csv")

normaldata = pd.DataFrame(phf)
normaldata.to_csv("/home/crazyflie/Desktop/vinod/data/phf.csv")

normaldata = pd.DataFrame(portsweep)
normaldata.to_csv("/home/crazyflie/Desktop/vinod/data/portsweep.csv")

normaldata = pd.DataFrame(rootkit)
normaldata.to_csv("/home/crazyflie/Desktop/vinod/data/rootkit.csv")

normaldata = pd.DataFrame(satan)
normaldata.to_csv("/home/crazyflie/Desktop/vinod/data/satan.csv")

normaldata = pd.DataFrame(smurf)
normaldata.to_csv("/home/crazyflie/Desktop/vinod/data/smurf.csv")

normaldata = pd.DataFrame(spy)
normaldata.to_csv("/home/crazyflie/Desktop/vinod/data/spy.csv")

normaldata = pd.DataFrame(teardrop)
normaldata.to_csv("/home/crazyflie/Desktop/vinod/data/teardrop.csv")

normaldata = pd.DataFrame(warezclient)
normaldata.to_csv("/home/crazyflie/Desktop/vinod/data/warezclient.csv")

normaldata = pd.DataFrame(warezmaster)
normaldata.to_csv("/home/crazyflie/Desktop/vinod/data/warezmaster.csv")

normaldata = pd.DataFrame(mailbomb)
normaldata.to_csv("/home/crazyflie/Desktop/vinod/data/mailbomb.csv")

normaldata = pd.DataFrame(mscan)
normaldata.to_csv("/home/crazyflie/Desktop/vinod/data/mscan.csv")

normaldata = pd.DataFrame(processtable)
normaldata.to_csv("/home/crazyflie/Desktop/vinod/data/processtable.csv")

normaldata = pd.DataFrame(saint)
normaldata.to_csv("/home/crazyflie/Desktop/vinod/data/saint.csv")

normaldata = pd.DataFrame(xsnoop)
normaldata.to_csv("/home/crazyflie/Desktop/vinod/data/xsnoop.csv")

normaldata = pd.DataFrame(httptunnel)
normaldata.to_csv("/home/crazyflie/Desktop/vinod/data/httptunnel.csv")

normaldata = pd.DataFrame(snmpgetattack)
normaldata.to_csv("/home/crazyflie/Desktop/vinod/data/snmpgetattack.csv")





normaldata = pd.DataFrame(dos)
normaldata.to_csv("/home/crazyflie/Desktop/vinod/data/dos.csv")

normaldata = pd.DataFrame(u2r)
normaldata.to_csv("/home/crazyflie/Desktop/vinod/data/u2r.csv")

normaldata = pd.DataFrame(r2l)
normaldata.to_csv("/home/crazyflie/Desktop/vinod/data/r2l.csv")

normaldata = pd.DataFrame(warezmaster)
normaldata.to_csv("/home/crazyflie/Desktop/vinod/data/probe.csv")
'''