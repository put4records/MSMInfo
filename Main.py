import os, struct, json

filelist=os.listdir('input/')
for fichier in filelist[:]: # filelist[:] makes a copy of filelist.
    if not(fichier.endswith(".msm")):
        filelist.remove(fichier)

codename = ''
msmclips = []

for i in filelist:
    firsthalf= []
    secondhalf = []
    with open('input/' + i, 'rb') as f:
     content = f.read()
     a = 200
     b = 204
     duration = struct.unpack('!f',bytes.fromhex(content[0x000C8:0x000CC].hex()))[0]
     print(duration)
     a+=4
     b+=4
     thing2bef = (struct.unpack('!f', bytes.fromhex(content[0x000CC:0x000D0].hex()))[0])
     a+=4
     b+=4
     thing3bef = (struct.unpack('!f', bytes.fromhex(content[0x000D0:0x000D4].hex()))[0])
     a+=4
     b+=4
     thing4bef = (struct.unpack('!f', bytes.fromhex(content[0x000D4:0x000D8].hex()))[0])
     a+=4
     b+=4
     thing5bef = (struct.unpack('!f', bytes.fromhex(content[0x000D8:0x000DC].hex()))[0])
     a+=4
     b+=4
     thing6bef = (struct.unpack('!f', bytes.fromhex(content[0x000DC:0x000E0].hex()))[0])
     a+=4
     b+=4
     thing7bef = int(content[0x000E8:0x000EC].hex(), 16)
     a+=4
     b+=4
     thing8bef = int(content[0x000E4:0x000E8].hex(), 16)
     a+=4
     b+=4
     thing9bef = (struct.unpack('!f', bytes.fromhex(content[a:b].hex()))[0])
     a+=4
     b+=4
     thing10bef = int(content[0x000EC:0x000F0].hex(), 16)
     a+=4
     b+=4
     thing11bef = (struct.unpack('!f', bytes.fromhex(content[a:b].hex()))[0])
     a+=4
     b+=4
     if len(codename) == 0:
      codename = (i[:-4].split('_')[0])
     par = int(content[232:236].hex(), 16) * 2
     a = 244
     b = 248
     c = 0
     while c < par // 2:
      firsthalf.append(struct.unpack('!f', bytes.fromhex(content[a:b].hex()))[0])
      print(firsthalf)
      a+=4
      b+=4
      c+=1
     while c < par:
      secondhalf.append(struct.unpack('!f', bytes.fromhex(content[a:b].hex()))[0])
      print(secondhalf)
      a+=4
      b+=4
      c+=1
     thing1 = (struct.unpack('!f', bytes.fromhex(content[a:b].hex()))[0])
     a+=4
     b+=4
     thing2 = (struct.unpack('!f', bytes.fromhex(content[a:b].hex()))[0])
     msmclip = json.loads(str({"name":i[:-4],"Duration of the Gesture":duration,"low Threshold Value":thing2bef,"Max Threshold Value":thing3bef,"Auto Correlation Threshold Value":thing4bef,"Move Direction Impact Factor Value":thing5bef,"SetCustomGestureFlags":thing6bef,"Amount of Sets in Bitfield":thing7bef,"Unknown":thing8bef,"Amount of Sets in Bitfield for Sweat/KCal values":thing10bef,"11thingbeforecords":thing11bef,"X,Y count":par,"cords":[],"thing_after_cords_1":thing1,"thing_after_cords_2":thing2}).replace("'",'"'))
     d = 0
     while d < (par // 2):
         cordclip = str(d+1) + ": " +  str(firsthalf[d]) + ", " + str(secondhalf[d])
         d+=1
         msmclip['cords'].append(cordclip)
     msmclips.append(msmclip)
with open('output/' + codename + '.json', 'w') as f:
      json.dump(msmclips, f, indent=4)
