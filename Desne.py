import contextlib
import os
with contextlib.redirect_stdout(None):
    import pygame as game
import random
import News
import pickle
import time
from ast import literal_eval
from itertools import chain

LEFT = 1
RIGHT = 3

game.init()
game.display.set_icon(game.image.load("Images/Bar/earth2.png"))
game.font.init()

size40 = game.font.Font('Other/blockfont.ttf', 35)
size30 = game.font.Font('Other/blockfont.ttf', 30)
size18 = game.font.Font('Other/blockfont.ttf', 16)
size15 = game.font.Font('Other/blockfont.ttf', 15)
size13 = game.font.Font('Other/blockfont.ttf', 12)
size100 = game.font.Font('Other/blockfont.ttf', 100)
size85 = game.font.Font('Other/blockfont.ttf', 85)
size80 = game.font.Font('Other/blockfont.ttf', 60)
size17 = game.font.Font('Other/blockfont.ttf', 17)
size25 = game.font.Font('Other/blockfont.ttf', 25)

global year,minsize,maxsize,minrectgen,maxrectgen,chanceremove,chanceamount,maptype,fileOpenType,colorcodes,fullcolorlist,textcolor,rotations,allcities,beachtype,names

#textcolor = (253,253,150)
textcolor = (253,213,10)
with open("TextFiles/colors.txt","r") as colors:
    fullcolorlist = list()
    for color in colors:
        color = color.rstrip("\n")
        color = literal_eval(color)
        fullcolorlist.append(color)
colorcodes = fullcolorlist[:]
#random.seed(1)

allcities = list()
with open("TextFiles/cities.txt","r") as file:
    for line in file:
        allcities.append(line.rstrip("\n"))

f = open("TextFiles/SocietyNames.txt","r")
names = list()
for line in f:
    names.append(line.rstrip("\n"))
names.remove(names[-1])

popdiviser = 0

game.mixer.init()
#game.mixer.music.load('Audio/background.mp3')
#game.mixer.music.play(-1)
Newmus = game.mixer.Sound('Audio/New.wav')
Tribemus = game.mixer.Sound('Audio/Tribe.wav')
Iconmus = game.mixer.Sound('Audio/Icon.wav')

screenWidth = 838
screenHeight = 838

#win = game.display.set_mode((screenWidth, screenHeight))
win = game.display.set_mode((screenHeight,screenWidth))
game.display.set_caption("Desne", "Desne")
#game.display.set_caption("title", icontitle=None) #-> None


water = game.image.load("Images/Terrain/water.png")
ocean = game.image.load("Images/Terrain/ocean.png")
wave = game.image.load("Images/Terrain/wave.png")
mountain = game.image.load("Images/Terrain/mountain.png")
grass = game.image.load("Images/Terrain/grass.png")
grass2 = game.image.load("Images/Terrain/grass2.png")
grass3 = game.image.load("Images/Terrain/grass3.png")
grass4 = game.image.load("Images/Terrain/grass4.png")

snow = game.image.load("Images/Terrain/snow.png")
snowhalf1 = game.image.load("Images/Terrain/snowhalf1.png")
snowhalf2 = game.image.load("Images/Terrain/snowhalf2.png")
snowhalf3 = game.image.load("Images/Terrain/snowhalf3.png")
grasshalf1 = game.image.load("Images/Terrain/grasshalf1.png")
grasshalf2 = game.image.load("Images/Terrain/grasshalf2.png")
grasshalf3 = game.image.load("Images/Terrain/grasshalf3.png")
snowcorner1 = game.image.load("Images/Terrain/snowcorner1.png")
snowcorner2 = game.image.load("Images/Terrain/snowcorner2.png")
snowcorner3 = game.image.load("Images/Terrain/snowcorner3.png")
grasscorner1 = game.image.load("Images/Terrain/grasscorner1.png")
grasscorner2 = game.image.load("Images/Terrain/grasscorner2.png")
grasscorner3 = game.image.load("Images/Terrain/grasscorner3.png")
sand = game.image.load("Images/Terrain/desert.png")
tree = game.image.load("Images/Terrain/tree.png")

vol1 = game.image.load("Images/Terrain/volcano1.png")
vol2 = game.image.load("Images/Terrain/volcano2.png")
vol3 = game.image.load("Images/Terrain/volcano3.png")
vol4 = game.image.load("Images/Terrain/volcano4.png")
vol5 = game.image.load("Images/Terrain/volcano5.png")
vol6 = game.image.load("Images/Terrain/volcano6.png")

mouse = game.image.load("Other/mouse.png")
test = game.image.load("Other/selected.png")
morebutton1 = game.image.load("Other/morebutton1.png")
morebutton2 = game.image.load("Other/morebutton2.png")

bar = game.image.load("Images/Bar/bar.png")
baroption1 = game.image.load("Images/Bar/baroption.png")
baroption2 = game.image.load("Images/Bar/baroption2.png")
titleimg = game.image.load("Images/Bar/titleimg.png")
button = game.image.load("Images/Bar/button.png")
politicalicon = game.image.load("Images/Bar/politicalicon1.png")
treeicon = game.image.load("Images/Bar/treeicon1.png")
bothicon = game.image.load("Images/Bar/bothicon1.png")
politicalicon2 = game.image.load("Images/Bar/politicalicon2.png")
treeicon2 = game.image.load("Images/Bar/treeicon2.png")
bothicon2 = game.image.load("Images/Bar/bothicon2.png")
earth1 = game.image.load("Images/Bar/earth1.png")
earth2 = game.image.load("Images/Bar/earth2.png")
mail1 = game.image.load("Images/Bar/mail1.png")
mail2 = game.image.load("Images/Bar/mail2.png")
quest1 = game.image.load("Images/Bar/quest1.png")
quest2 = game.image.load("Images/Bar/quest2.png")
historychanger1 = game.image.load("Images/Bar/historychanger1.png")
historychanger2 = game.image.load("Images/Bar/historychanger2.png")
camera1 = game.image.load("Images/Bar/camera1.png")
camera2 = game.image.load("Images/Bar/camera2.png")
nocamera1 = game.image.load("Images/Bar/nocamera1.png")
nocamera2 = game.image.load("Images/Bar/nocamera2.png")
city1 = game.image.load("Images/Bar/city1.png")
city2 = game.image.load("Images/Bar/city2.png")
house1 = game.image.load("Images/Bar/house1.png")
house2 = game.image.load("Images/Bar/house2.png")



arrow1 = game.image.load("Images/Bar/arrow1.png")
arrow2 = game.image.load("Images/Bar/arrow2.png")
Barrow1 = game.image.load("Images/Bar/Backarrow1.png")
Barrow2 = game.image.load("Images/Bar/Backarrow2.png")
newsarrow1 = game.image.load("Images/Bar/newsarrow1.png")
newsarrow2 = game.image.load("Images/Bar/newsarrow2.png")

###Numbers
num11 = game.image.load("Images/Bar/num11.png")
num12 = game.image.load("Images/Bar/num12.png")
num101 = game.image.load("Images/Bar/num101.png")
num102 = game.image.load("Images/Bar/num102.png")
num51 = game.image.load("Images/Bar/num51.png")
num52 = game.image.load("Images/Bar/num52.png")
###Floopies
redfloppy1 = game.image.load("Images/Disks/redfloppy1.png")
redfloppy2 = game.image.load("Images/Disks/redfloppy2.png")
greenfloppy1 = game.image.load("Images/Disks/greenfloppy1.png")
greenfloppy2 = game.image.load("Images/Disks/greenfloppy2.png")
bluefloppy1 = game.image.load("Images/Disks/bluefloppy1.png")
bluefloppy2 = game.image.load("Images/Disks/bluefloppy2.png")

cityorb = game.image.load("Images/Terrain/cityorb.png")
capitalorb = game.image.load("Images/Terrain/capitalorb.png")

def truncline(text, font, maxwidth):
        real=len(text)
        stext=text
        l=font.size(text)[0]
        cut=0
        a=0
        done=1
        old = None
        while l > maxwidth:
            a=a+1
            n=text.rsplit(None, a)[0]
            if stext == n:
                cut += 1
                stext= n[:-cut]
            else:
                stext = n
            l=font.size(stext)[0]
            real=len(stext)
            done=0
        return real, done, stext

def wrapline(text, font, maxwidth):
    done=0
    wrapped=[]

    while not done:
        nl, done, stext=truncline(text, font, maxwidth)
        wrapped.append(stext.strip())
        text=text[nl:]
    return wrapped



class menu():
    def title(word):
        win.blit(titleimg,((0,0)))
        tit = size100.render(word, True, (200, 200, 200))
        win.blit(tit,(tit.get_rect(center=(416+16, 64))))
        #416 is important for center
    def bar(barOptions):
        for option in barOptions:
            win.blit(baroption1,(256,option[0]))
            if baroption2.get_rect(top=(option[0]),left=(256)).collidepoint(game.mouse.get_pos()):
                win.blit(baroption2,(256,option[0]))
            opt1 = size80.render(option[1], True, textcolor)
            win.blit(opt1,(baroption1.get_rect(center=(476, option[2]))))
class gen():
    def fancytiles(landtype,beachtype):
        if landtype == grassCoords:
            landdictionary = {
            1:grasshalf1,
            2:grasshalf2,
            3:grasshalf3,
            4:grasscorner1,
            5:grasscorner2,
            6:grasscorner3
            }
        elif landtype == snowCoords:
            landdictionary = {
            1:snowhalf1,
            2:snowhalf2,
            3:snowhalf3,
            4:snowcorner1,
            5:snowcorner2,
            6:snowcorner3
            }
        for tile in landtype:
            if ((tile[0]+16,tile[1]-16)) in allCoords:
                win.blit(game.transform.rotate(landdictionary[beachtype[(tile[0]+16,tile[1]-16)]+3],270),(tile[0]+16,tile[1]-16))
            if ((tile[0]+16,tile[1]+16)) in allCoords:
                win.blit(game.transform.rotate(landdictionary[beachtype[(tile[0]+16,tile[1]+16)]+3],180),(tile[0]+16,tile[1]+16))
            if ((tile[0]-16,tile[1]-16)) in allCoords:
                win.blit(game.transform.rotate(landdictionary[beachtype[(tile[0]-16,tile[1]-16)]+3],360),(tile[0]-16,tile[1]-16))
            if ((tile[0]-16,tile[1]+16)) in allCoords:
                win.blit(game.transform.rotate(landdictionary[beachtype[(tile[0]-16,tile[1]+16)]+3],90),(tile[0]-16,tile[1]+16))

            if ((tile[0]+16,tile[1])) in allCoords:
                win.blit(game.transform.rotate(landdictionary[beachtype[(tile[0]+16,tile[1])]],270),(tile[0]+16,tile[1]))
            if ((tile[0]-16,tile[1])) in allCoords:
                win.blit(game.transform.rotate(landdictionary[beachtype[(tile[0]-16,tile[1])]],90),(tile[0]-16,tile[1]))
            if ((tile[0],tile[1]+16)) in allCoords:
                win.blit(game.transform.rotate(landdictionary[beachtype[(tile[0],tile[1]+16)]],180),(tile[0],tile[1]+16))
            if ((tile[0],tile[1]-16)) in allCoords:
                win.blit(game.transform.rotate(landdictionary[beachtype[(tile[0],tile[1]-16)]],360),(tile[0],tile[1]-16))
    def allTiles():
        allCoords = set()
        i = 640-16
        z = 640-16
        while i != -16:
            while z != -16:
                allCoords.add((i,z))
                z -= 16
            i -= 16
            z = 640-16
        return allCoords
    def island(allCoords):
        while True:
            test = True
            landmass = set()
            a,b = (random.randint(1,39))*16,(random.randint(1,39))*16
            org1y = b
            possiblesizesx = random.randint(int(minsize),int(maxsize))
            possiblesizesy = random.randint(int(minsize),int(maxsize))
            for size in range(possiblesizesx):
                for size in range(possiblesizesy):
                    landmass.add((a,b))
                    if b >= 640-16 or b <= 0 or a >= 640-16 or a <= 0:
                        test = False


                    b-=16
                b = org1y
                a-=16
           # print size of island
           #print(possiblesizesx,possiblesizesy)
            if test == True:
                if landmass.issubset(allCoords):
                    return landmass
    def realism(seaCoords,landCoords):
        temp = set()
        for Coord in landCoords:
            if (((Coord[0]-16),Coord[1])) in seaCoords or (((Coord[0]+16),Coord[1])) in seaCoords or (((Coord[0]),Coord[1]-16)) in seaCoords or (((Coord[0]),Coord[1]+16)) in seaCoords:
                seed = random.randint(1,int(chanceremove))
                if seed == 1:
                    temp.add(Coord)
        for i in temp:
            landCoords.remove(i)
            seaCoords.add(i)
        temp = set()
        for Coord in landCoords:
            if (((Coord[0]-16),Coord[1])) in seaCoords and (((Coord[0]+16),Coord[1])) in seaCoords and (((Coord[0]),Coord[1]-16)) in seaCoords and (((Coord[0]),Coord[1]+16)) in seaCoords:
                temp.add(Coord)

        for i in temp:
            landCoords.remove(i)
            seaCoords.add(i)
        return landCoords,seaCoords
    def mountain(mountainCoords,landCoords,seaCoords,allCoords):

            coord = random.sample(landCoords, 1)
            a = (coord[0])[0]
            b = (coord[0])[1]
            originaly = b

            if maptype == "random":
                mountnum1 = random.randint(2,4)
                mountnum2 = random.randint(3,9)
            elif maptype == "island":
                mountnum1 = random.randint(2,3)
                mountnum2 = random.randint(5,9)
            elif maptype == "pangea":
                mountnum1 = random.randint(3,5)
                mountnum2 = random.randint(6,13)

            if random.randint(1,2) == 1:
                possiblesizesx = mountnum1
                possiblesizesy = mountnum2
            else:
                possiblesizesy = mountnum1
                possiblesizesx = mountnum2

            for size in range(possiblesizesx):
                for size in range(possiblesizesy):
                    if ((a,b)) in landCoords:
                        if random.randint(1,2) == 1:
                            if ((a-16,b)) in mountainCoords or ((a+16,b)) in mountainCoords or ((a,b-16)) in mountainCoords or ((a,b+16)) in mountainCoords:

                                if random.randint(1,3) == 1:
                                    mountainCoords.add((a,b))
                            else:
                                mountainCoords.add((a,b))
                    b-=16
                a-=16
                b = originaly

            return landCoords,seaCoords,allCoords,mountainCoords
    def snowgen(snowCoords,landCoords):

        nom = random.randint(7,8)*16#7 10
        y = nom
        x = 640-16
        firsttime = True
        secondtime = True

        while y != -16:
            while x != -16:
                if ((x,y)) in landCoords:
                    if secondtime == True:
                        if firsttime == True:
                            if random.randint(1,4) == 1:
                                snowCoords.add((x,y))
                        else:
                            if random.randint(1,3) < 3:
                                snowCoords.add((x,y))
                    else:
                        snowCoords.add((x,y))
                x -= 16
            y -= 16
            x = 640-16
            if firsttime == True:
                firsttime = False
            else:
                secondtime = False



        y = 640-nom
        x = 640-16
        firsttime = True
        secondtime = True

        while y != 640:
            while x != -16:

                if ((x,y)) in landCoords:

                    if secondtime == True:

                        if firsttime == True:
                            if random.randint(1,4) == 1:
                                snowCoords.add((x,y))
                        else:
                            if random.randint(1,3) < 3:
                                snowCoords.add((x,y))
                    else:
                        snowCoords.add((x,y))
                x -= 16
            y += 16
            x = 640-16
            if firsttime == True:
                firsttime = False
            else:
                secondtime = False


        return snowCoords
    def sandtreegen(desertCoords,landCoords,isDesert):


        if isDesert == True:
            amount = random.choice([2000,1900,1800,1700,1600,1500,3000])
            possiblesizesx = random.randint(5,12)
            possiblesizesy = random.randint(1,2)
        else:
            if maptype == "island":
                amount = random.randint(20,40)
            elif maptype == "pangea":
                amount = random.randint(40,60)
            elif maptype == "random":
                amount = random.randint(20,60)

            possiblesizesx = random.randint(1,5)
            possiblesizesy = random.randint(1,5)
        coord = random.sample(landCoords, 1)
        x = (coord[0])[0]
        y = (coord[0])[1]

        tries = 0
        if isDesert == True:
            while y not in range(16*22,416):
                coord = random.sample(landCoords, 1)
                x = (coord[0])[0]
                y = (coord[0])[1]
                possiblesizesx = random.randint(9,19)
                possiblesizesy = random.randint(1,2)
                tries += 1
                if tries == 200:
                    return desertCoords
        a = x
        b = y
        originaly = b
        for size in range(possiblesizesx):
            for size in range(possiblesizesy):
                if ((a,b)) in landCoords:
                    desertCoords.add((a,b))

                b-=16
            a-=16
            b = originaly

        for i in range(amount):
            tile = (random.sample(desertCoords, 1))[0]
            if random.randint(1,2) == 1:
                if random.randint(1,2) == 1:
                    if ((tile[0]-16,tile[1])) in landCoords:
                        if random.randint(1,3) == 1:
                            desertCoords.add((tile[0]-16,tile[1]))
                else:
                    if ((tile[0]+16,tile[1])) in landCoords:
                        if random.randint(1,3) == 1:
                            desertCoords.add((tile[0]+16,tile[1]))
            else:
                if random.randint(1,2) == 1:
                    if ((tile[0],tile[1]-16)) in landCoords:
                        if random.randint(1,3) == 1:
                            desertCoords.add((tile[0],tile[1]-16))
                else:
                    if random.randint(1,2) == 1:
                        if ((tile[0],tile[1]+16)) in landCoords:
                            if random.randint(1,3) == 1:
                                desertCoords.add((tile[0],tile[1]+16))
        return desertCoords
    def finalgen():
        allCoords = set(gen.allTiles())
        landCoords = set()
        snowCoords = set()
        mountainCoords = set()
        desertCoords = set()
        treeCoords = set()
        mountainOffset = {}
        treeOffset = {}


        ### Generate Land Squares
        for i in range(random.randint(int(minrectgen),int(maxrectgen))):
            tempCoords = gen.island(allCoords)
            for Coord in tempCoords:
                landCoords.add(Coord)
        ###Creat seaCoords
        seaCoords = allCoords -  landCoords
        ### Generate Coastline
        for i in range(int(chanceamount)):
            landCoords,seaCoords = gen.realism(seaCoords,landCoords)
        ###Generate Mountains
        #    for i in range(random.randint(3,6)):
        for i in range(random.randint(5,8)):
            landCoords,seaCoords,allCoords,mountainCoords = gen.mountain(mountainCoords,landCoords,seaCoords,allCoords)
        ###Generate Snow
        snowCoords = gen.snowgen(snowCoords,landCoords)
        ###Generate Desert
        if random.randint(1,5) != 5:
            for i in range(random.randint(1,2)):
                desertCoords = gen.sandtreegen(desertCoords,landCoords,True)



        grassCoords = landCoords-seaCoords-snowCoords-desertCoords

        for i in range(random.randint(5,9)):
            treeCoords = (gen.sandtreegen(treeCoords,grassCoords,False))-mountainCoords
        ### Creat Grass

        tempCoords = set()


        for tile in grassCoords:
            if ((tile[0]+16,tile[1])) in desertCoords and ((tile[0]-16,tile[1])) in desertCoords and ((tile[0],tile[1]+16)) in desertCoords and ((tile[0],tile[1]-16)) in desertCoords:
                tempCoords.add(tile)
                desertCoords.add(tile)
        for tile in tempCoords:
            grassCoords.remove(tile)

        volcanoCoords =list()
        for volcano in range(random.randint(0,3)):
            myvolcano = random.choice(list(mountainCoords))
            ##coords,clock
            volcanoCoords.append([myvolcano])
            mountainCoords.remove(myvolcano)

        for tile in allCoords:
            mountainOffset[tile] = random.randint(0,4)
        for tile in allCoords:
            treeOffset[tile] = random.randint(0,8)
        posSpawnCoords = set((list(landCoords))[:])
        posCoastCoords = set()
        for i in posSpawnCoords:
            if ((i[0]-16,i[1])) in seaCoords or ((i[0]+16,i[1])) in seaCoords or ((i[0],i[1]-16)) in seaCoords or ((i[0],i[1]+16)) in seaCoords:
                posCoastCoords.add(i)


        beachtype = dict()
        for tile in allCoords:
            beachtype[tile] = random.choice([1,2,3])

        return landCoords,seaCoords,allCoords,mountainCoords,snowCoords,grassCoords,desertCoords,treeCoords,posCoastCoords,posSpawnCoords,mountainOffset,treeOffset,volcanoCoords,beachtype
class societygen():
    def spawning(posSpawnCoords,colorcodes,names):
        spawntile = random.choice(list(posSpawnCoords))

        while spawntile not in posSpawnCoords:
            spawntile = random.choice(list(posSpawnCoords))
        if year == 0:
            posSpawnCoords.remove(spawntile)
        if colorcodes:
            color = (random.choice(colorcodes))#150
            colorcodes.remove(color)

        else:
            colorcodes = fullcolorlist[:]
            color = (random.choice(colorcodes))#150
            colorcodes.remove(color)
        char = open("TextFiles/SocietyCharacteristics.txt","r")
        charlist1 = list()
        for line in char:
            #charlist1.append(line.rstrip("\n"))
            charlist1.append(line)
        char.close()
        charlist1.remove(charlist1[-1])

        char = open("TextFiles/SocietyCharacteristicsOp.txt","r")
        charlist2 = list()
        for line in char:
            #charlist2.append(line.rstrip("\n"))
            charlist2.append(line)
        char.close()
        charlist2.remove(charlist2[-1])
        mynum = 0
        for line in charlist1:
            line=list(line)
            line = line[:-1]
            line="".join(line)
            charlist1[mynum] = line
            mynum+=1
        mynum = 0
        for line in charlist2:
            line=list(line)
            line = line[:-1]
            line="".join(line)
            charlist2[mynum] = line
            mynum+=1
        del mynum
        societycharacteristics = list()
        for i in range(3):
            if random.randint(1,2) == 1:
                currentchar = random.choice(charlist1)
                societycharacteristics.append(currentchar)
                charlist2.remove(charlist2[charlist1.index(currentchar)])
                charlist1.remove(currentchar)

            else:
                currentchar = random.choice(charlist2)
                societycharacteristics.append(currentchar)
                charlist1.remove(charlist1[charlist2.index(currentchar)])
                charlist2.remove(currentchar)
        #try:
        if len(names) > 2:
            part1 = random.choice(names)
            part2 = random.choice(names)
            while part2 == part1:
                part2 = random.choice(names)
            names.remove(part1)
            names.remove(part2)
        else:
            f = open("TextFiles/SocietyNames.txt","r")
            names = list()
            for line in f:
                names.append(line.rstrip("\n"))
            f.close()
            names.remove(names[-1])
            part1 = random.choice(names)
            part2 = random.choice(names)
            while part2 == part1:
                part2 = random.choice(names)
            #print(part1,part2)
            names.remove(part1)
            names.remove(part2)

        name = part1+part2
        name = name[0].upper()+name[1:]
        if year == 0:
            governmenttype = "Chieftan"
        else:
            governmenttype = "Interm Government"
        pop = 0
        #pop = society.populationcalc([spawntile],fertilityIndex)
        #print(pop)
        military = random.randint(0,5) #K

        citzensatisfaction = random.randint(60,90) #percent
        news=list()

        cities = dict()
        try:
            cities[spawntile] = random.choice(allcities)
        except:
            with open("TextFiles/cities.txt","r") as file:
                for line in file:
                    allcities.append(line.rstrip("\n"))
            cities[spawntile] = random.choice(allcities)
        #create civilization
        #war = [with who,with who 2,turns since started,win battle chance (use randint), has taken turn yet]
        war = [-1,0,0,0]

        datapack = [[spawntile],color,societycharacteristics,name,governmenttype,pop,military,citzensatisfaction,spawntile,news,cities,war]
        return datapack,posSpawnCoords
    def expand(datapack,posSpawnCoords,seaCoords):
        allTiles = datapack[0]

        if allTiles:
            curTile = random.choice(allTiles)
        else:
            return datapack,posSpawnCoords
        tempTile = allTiles[:]

        mynums = [1,2,3,4,5,6,7,8]
        mynum = random.choice(mynums)
        tries = 0
        while tempTile:

            for i in range(8):
                xplus = 0
                yplus = 0
                if mynum == 1 or mynum == 5 or mynum == 6:
                    xplus = -16
                if mynum == 2 or mynum == 7 or mynum == 8:
                    xplus = 16
                if mynum == 3 or mynum == 5 or mynum == 7:
                    yplus = -16
                if mynum == 4 or mynum == 8 or mynum == 6:
                    yplus = 16
                if mynum <= 4:

                    if ((curTile[0]+xplus), curTile[1]+yplus) in posSpawnCoords:
                        curTile = ((curTile[0]+xplus,curTile[1]+yplus))
                        datapack[0].append(curTile)

                        return datapack, posSpawnCoords
                    else:
                        mynums.remove(mynum)

                elif mynum <= 8:

                    if ((curTile[0]+xplus), curTile[1]) in seaCoords and ((curTile[0]), curTile[1]+yplus) in seaCoords and ((curTile[0]+xplus), curTile[1]+yplus) in posSpawnCoords:
                        curTile = ((curTile[0]+xplus,curTile[1]+yplus))
                        datapack[0].append(curTile)
                        posSpawnCoords.remove(curTile)
                        return datapack, posSpawnCoords
                    else:
                        mynums.remove(mynum)
                if mynums:
                    mynum = random.choice(mynums)



            tempTile.remove(curTile)
            if tempTile:
                curTile = random.choice(tempTile)
            else:
                return datapack,posSpawnCoords
            mynums = [1,2,3,4,5,6,7,8]
            mynum = random.choice(mynums)
        return datapack,posSpawnCoords
    def colonize(datapack,posSpawnCoords,seaCoords):
        allTiles = datapack[0]
        tempTile = allTiles[:]
        while tempTile:
            if posSpawnCoords:
                curTile = (random.sample((posSpawnCoords), 1))[0]

                if ((curTile[0]-16,curTile[1])) in seaCoords or ((curTile[0]+16,curTile[1])) in seaCoords or ((curTile[0],curTile[1]-16)) in seaCoords or ((curTile[0],curTile[1]+16)) in seaCoords:
                    datapack[0].append(curTile)
                    return datapack,posSpawnCoords
                else:
                    tempTile.remove(curTile)

            else:
                return datapack,posSpawnCoords
        return datapack,posSpawnCoords
class sidebar():
    def bottom():

        win.blit(bar,((0,640)))
        bar1 = game.transform.rotate(bar, 180)
        win.blit(bar1,((320,640)))
    def right():
        bar1 = game.transform.rotate(bar, 270)
        win.blit(bar1,((640,0)))
        bar2 = game.transform.rotate(bar, 90)
        win.blit(bar2,((640,320)))
    def icons(turnamount,myalpha,savegame,fancyview,displayCitiesButton):
        politicalicon2,treeicon2,bothicon2,num11,num51,num101
        values = [
        [myalpha,0,432,672,treeicon,treeicon2,True],
        [myalpha,180,432,720,politicalicon,politicalicon2,True],
        [myalpha,1000,432,768,bothicon,bothicon2,True],

        [turnamount,1,480,672,num11,num12,True],
        [turnamount,5,480,720,num51,num52,True],
        [turnamount,10,480,768,num101,num102,True],

        [savegame,1,48,672,redfloppy1,redfloppy2,True],
        [savegame,2,48,720,greenfloppy1,greenfloppy2,True],
        [savegame,3,48,768,bluefloppy1,bluefloppy2,True],

        #[False,True,48+48,672,quest1,quest2,True],
        #32
        #52
        #20
        #192
        #640
        [False,True,640+(int(192/2)-16) ,640-48,quest1,quest2,True],

        [fancyview,True,384,672+48,camera1,camera2,True],
        [fancyview,False,384,672+48+48,nocamera1,nocamera2,True],
        [False,True,384,672,historychanger1,historychanger2,True],

        [False,True,384-48,672,mail1,mail2,True],

        [displayCitiesButton,2,288,672,house1,house2,True],
        [displayCitiesButton,3,288,720,city1,city2,True],

        [civselected,-1,640+48,288+48,morebutton1,morebutton2,False],
        ]
        for itemnum in range(len(values)):

            if values[itemnum][0]!=values[itemnum][1]:

                if values[itemnum][4].get_rect(top=values[itemnum][3],left=values[itemnum][2]).collidepoint(game.mouse.get_pos()):
                    win.blit(values[itemnum][5],(values[itemnum][2],values[itemnum][3]))
                else:
                    win.blit(values[itemnum][4],(values[itemnum][2],values[itemnum][3]))
            else:
                if values[itemnum][6]==True:
                    win.blit(values[itemnum][5],(values[itemnum][2],values[itemnum][3]))
                else:
                    pass


        win.blit(Barrow1,(528,752))
        if arrow1.get_rect(top=752,left=528).collidepoint(game.mouse.get_pos()):
            win.blit(Barrow2,(528,752))
        win.blit(arrow1,(528,672))
        if arrow1.get_rect(top=672,left=528).collidepoint(game.mouse.get_pos()):
            win.blit(arrow2,(528,672))


    def tribetext(civselected):
        if civselected != -1:
            try:
                tribename = size30.render(bigpack[civselected][3], True, textcolor)
                char1 = bigpack[civselected][2][0]
                char1N = size18.render(char1, True, textcolor)
                char2 = bigpack[civselected][2][1]
                char2N = size18.render(char2, True, textcolor)
                char3 = bigpack[civselected][2][2]
                char3N = size18.render(char3, True, textcolor)


                if bigpack[civselected][4] == "Interm Government":
                    gov = size18.render("Gov: Interm", True, textcolor)
                else:
                    gov = size18.render("Gov: "+bigpack[civselected][4], True, textcolor)
                population = size18.render("Pop: "+str(bigpack[civselected][5]), True, textcolor)
                win.blit(tribename,(640+24,16))
                win.blit(char1N,(640+24,64+32))
                win.blit(char2N,(640+24,64+48+32))
                win.blit(char3N,(640+24,128+32+32))
                win.blit(gov,(640+24,240))
                win.blit(population,(640+24,288))
            except:
                civselected = -1
    #def worldtext():


    def landtext(tileselected):
        type = "Null"
        addition = "Null"
        if tileselected in grassCoords:
            type = "Plains"
        if tileselected in desertCoords:
            type = "Desert"
        if tileselected in snowCoords:
            type = "Tundra"
        if tileselected in seaCoords:
            type = "Coast"
        if tileselected in oceanCoords:
            type = "Ocean"
        if tileselected in treeCoords:
            addition = "Forested "
        elif tileselected in mountainCoords:
            addition = "Mountainous "
        elif tileselected in actualVolcanoCoords:
            addition = "Volcanic "
        else:
            addition = ""


        x,y = other.findxy(tileselected[0],tileselected[1])
        #thing = size18.render("Biome: "+type, True, textcolor)
        #win.blit(size25.render("Biome", True, textcolor),(640+24,288+64+32))
        win.blit(size13.render(addition+type, True, textcolor),(640+24,288+128))
        win.blit(size13.render("Coords: ("+str(int((x/16)+1))+" , "+str(int((y/16)+1))+")", True, textcolor),(640+24,288+128+32))

        try:
            win.blit(size13.render("City: "+bigpack[civselected][10][(tileselected[0],tileselected[1])], True, textcolor),(640+24,288+128+32+32))
        except:
            pass
class society():
    def soilfertility(mountainCoords,snowCoords,grassCoords,desertCoords,treeCoords):
        fertilityIndex = {}
        for tile in allCoords:
            if tile in snowCoords: fertilityIndex[tile] = [random.randint(1,1000),random.randint(3000,5000),1.0025]
            if tile in grassCoords: fertilityIndex[tile] = [random.randint(10000,15000),random.randint(50000,100000),1.0025]
            if tile in desertCoords: fertilityIndex[tile] = [random.randint(1,2000),random.randint(3000,10000),1.0025]
            if tile in treeCoords: fertilityIndex[tile] = [random.randint(8000,14000),random.randint(16000,40000),1.0025]
            if tile in mountainCoords: fertilityIndex[tile] = [random.randint(500,1500),random.randint(2000,3000),1.0025]
        return fertilityIndex
    def populationcalc(Coords,fertilityIndex):
        pop = 0
        Coords = list(set(Coords))
        #    print(fertilityIndex,"\n")
        for tile in Coords:
            pop+=fertilityIndex[tile][0]

        return pop
    def popadd(Coords,fertilityIndex,plus):

        for tile in Coords:

            if fertilityIndex[tile][0] >= fertilityIndex[tile][1]:
                if plus == True:
                    fertilityIndex[tile][2] /= 10


            if plus == False:

                fertilityIndex[tile][0] = int(fertilityIndex[tile][0]-((fertilityIndex[tile][0]/100)*fertilityIndex[tile][2]))
            else:
                fertilityIndex[tile][0] = int(fertilityIndex[tile][0]+((fertilityIndex[tile][0]/100)*fertilityIndex[tile][2]))

        return fertilityIndex
    def displaytribes(myalpha,posSpawnCoords,bigpack):
        x=-1
        for item in bigpack:
            x+=1
            if myalpha == 180:
                thicc = 4
                if civselected == x:
                    thicc = 6
            else:
                thicc = 1
                if civselected == x:
                    thicc = 4
            territory = game.Surface((16,16))
            territory.fill((item[1]))
            territoryA = game.Surface((thicc,16))
            territoryB = game.Surface((16,thicc))
            territoryC = game.Surface((thicc,thicc))

            territory.set_alpha(myalpha)
            if myalpha == 180:
                if civselected != x:
                    territoryA.fill((item[1]))
                    territoryB.fill((item[1]))
                    territoryC.fill((item[1]))
                else:
                    territoryA.fill((0,0,0))
                    territoryB.fill((0,0,0))
                    territoryC.fill((0,0,0))

            for tile in item[0]:
                if tile in posSpawnCoords:
                    posSpawnCoords.remove(tile)
                if myalpha == 1000:
                    win.blit(territory, ((tile)))
                if myalpha != 0:
                    if ((tile[0]+16,tile[1])) not in item[0]:
                        win.blit(territoryA, ((tile[0]+(16-thicc),tile[1])))
                    if ((tile[0]-16,tile[1])) not in item[0]:
                        win.blit(territoryA, ((tile)))
                    if ((tile[0],tile[1]+16)) not in item[0]:
                        win.blit(territoryB, ((tile[0],tile[1]+(16-thicc))))
                    if ((tile[0],tile[1]-16)) not in item[0]:
                        win.blit(territoryB, ((tile)))
                    if ((tile[0]-16,tile[1]-16)) not in item[0]:
                        win.blit(territoryC, ((tile)))
                    if ((tile[0]+16,tile[1]+16)) not in item[0]:
                        win.blit(territoryC, ((tile[0]+(16-thicc),tile[1]+(16-thicc))))
                    if ((tile[0]-16,tile[1]+16)) not in item[0]:
                        win.blit(territoryC, ((tile[0],tile[1]+(16-thicc))))
                    if ((tile[0]+16,tile[1]-16)) not in item[0]:
                        win.blit(territoryC, ((tile[0]+(16-thicc),tile[1])))
    def getnews (forward,newselected):
        if forward == True:
            try:
                newselected+=1
                headline = allnews[newselected][0]
                story = wrapline(str(allnews[newselected][1]), size18, 700)
            except:newselected=0
        else:
            try:
                newselected-=1
                headline = allnews[newselected][0]
                story = wrapline(str(allnews[newselected][1]), size18, 700)
            except:newselected=-1
        headline = allnews[newselected][0]
        story = wrapline(str(allnews[newselected][1]), size18, 700)
        return headline,story,newselected
    def displaycities (bigpack):
        for itemnum in range(len(bigpack)):
            for city in bigpack[itemnum][10]:
                win.blit(cityorb,(city))
    def displaycapitals (bigpack):
        for itemnum in range(len(bigpack)):
            #for city in bigpack[itemnum][10]:
            win.blit(capitalorb,(bigpack[itemnum][8]))
class other():
    def deletenonpickle(files):
        newfile=list()
        for file in files:
            if ".pickle" in file:
                newfile.append(file)
            else:
                pass
                #files.remove(file)

        return newfile
    def mousemovement(*inCreateMode):
        x = (game.mouse.get_pos())[0]
        y = (game.mouse.get_pos())[1]
        i = 0
        mynums = list()
        while i != 640:
            mynums.append(i)
            i+=16
        if (game.mouse.get_pos())[0] < 640 and (game.mouse.get_pos())[1] < 640 and (game.mouse.get_pos())[0] != 0 and (game.mouse.get_pos())[1] != 0:
            game.mouse.set_visible(False)
            xy = size15.render(("X: "+ str(int(x/16)+1) + "  Y: "+ str(int(y/16)+1))   , True, (textcolor))
            win.blit(xy,((0,640-16)))
            while x not in mynums:
                x-=1
            while y not in mynums:
                y-=1
            if inCreateMode:
                win.blit(inCreateMode[0],((x,y)))
                #win.blit(game.transform.rotate(inCreateMode[0],rotations[(x,y)]),((x,y)))
            win.blit(mouse,((x,y)))
        else:
            xy = size15.render(( "X:      Y: ")   , True, (textcolor))
            win.blit(xy,((0,640-16)))
            game.mouse.set_visible(True)
    def findarea(Coords):
        ranTile = random.choice(list(Coords))
        for i in range(200):
            if ((ranTile[0]+16,ranTile[1])) in seaCoords or ((ranTile[0]-16,ranTile[1])) in seaCoords or ((ranTile[0],ranTile[1]+16)) in seaCoords or ((ranTile[0],ranTile[1]-16)) in seaCoords:
                pass
            else:
                ranTile = random.choice(list(Coords))
        if ((ranTile[0]+16,ranTile[1])) in seaCoords or ((ranTile[0]-16,ranTile[1])) in seaCoords or ((ranTile[0],ranTile[1]+16)) in seaCoords or ((ranTile[0],ranTile[1]-16)) in seaCoords:
            pass
        else:
            return Coords
        area = {(ranTile)}
        temp = set()
        for i in range(int( random.randint(5,15))):#len(Coords)/3) ):
            for tile in area:
                for num in range(8):
                    xplus= 0
                    yplus = 0
                    if num == 0 or num == 4 or num == 5:
                        xplus = -16
                    if num == 1 or num == 6 or num == 7:
                        xplus = 16
                    if num == 2 or num == 4 or num == 6:
                        yplus = -16
                    if num == 3 or num == 7 or num == 5:
                        yplus = 16

                    if ((tile[0]+xplus,tile[1]+yplus)) in Coords and ((tile[0]+xplus,tile[1]+yplus)) not in area:
                        if random.randint(1,5) > 3:
                            if num >4:
                                if random.randint(1,5) > 3:
                                    temp.add(((tile[0]+xplus,tile[1]+yplus)))
                            else:
                                temp.add(((tile[0]+xplus,tile[1]+yplus)))

            for tile in temp:
                area.add(tile)
        return area
    def findbordercountries(datapack,bigpack):
        possibleborders = []
        for otherdatapack in bigpack:
            if datapack != otherdatapack:
                for Coord in otherdatapack[0]:
                    if ((Coord[0]+16,Coord[1])) in datapack[0] or ((Coord[0]-16,Coord[1])) in datapack[0] or ((Coord[0],Coord[1]+16)) in datapack[0] or ((Coord[0],Coord[1]-16)) in datapack[0]:
                        possibleborders.append(bigpack.index(otherdatapack))
        if possibleborders:
            return random.choice(possibleborders)
        else:
            return "false"


        possibleborders = []
        possiblelocations = []
        for pack in range(len(bigpack)):
            if datapack != pack:
                possiblelocations+=pack[0]


        for Coord in datapack[0]:
            if ((Coord[0]+16,Coord[1])) in possiblelocations:
                for pack in range(len(bigpack)):
                    if ((Coord[0]+16,Coord[1])) in pack:
                        possibleborders.append(bigpack.index(pack))

            if ((Coord[0]-16,Coord[1])) in possiblelocations:
                for pack in range(len(bigpack)):
                    if ((Coord[0]-16,Coord[1])) in pack:
                        possibleborders.append(bigpack.index(pack))
            if ((Coord[0],Coord[1]+16)) in possiblelocations:
                for pack in range(len(bigpack)):
                    if ((Coord[0],Coord[1]+16)) in pack:
                        possibleborders.append(bigpack.index(pack))
            if ((Coord[0],Coord[1]-16)) in possiblelocations:
                for pack in range(len(bigpack)):
                    if ((Coord[0],Coord[1]-16)) in pack:
                        possibleborders.append(bigpack.index(pack))


        if possibleborders:
            return random.choice(possibleborders)
        else:
            return "false"
    def displayyr():
        yeardisplay = size15.render(( "Year: "+str(year))   , True, (textcolor))
        win.blit(yeardisplay,((640-64-16-16,640-16)))
    def warturn(bigpack,civ1):
        civ2 = bigpack[civ1][11][0]
        try:
            #war = [with who,turns since started,win battle chance (use randint),has taken turn yet]  11 name is 3

            #0 is now who they are vsing
            #1 is the turns the battle, starts high
            #2 chance, should be calucted using random
            #3 have they taken turn yet


            if bigpack[civ1][11][0] == -1:

                #bigpack[civ1][11][1] = -1

                return bigpack
            else:
                if bigpack[civ1][11][3] == 0 and bigpack[civ2][11][3] == 0:

                    bigpack[civ1][11][2]=random.randint(1,10)
                    bigpack[civ2][11][2]=random.randint(1,10)



                    for i in range(random.randint(1,3)):
                        if bigpack[civ1][11][2]==bigpack[civ2][11][2]:
                            #print("no land changed")
                            pass
                        elif bigpack[civ1][11][2]>bigpack[civ2][11][2]:
                            #print(bigpack[civ1][3]+" won")
                            tilegot = other.findbordertile(bigpack,civ1,civ2)
                            if tilegot == -1:
                                continue
                            bigpack[civ2][0].remove(tilegot)

                            bigpack[civ1][0].append(tilegot)
                            for tile in bigpack[civ2][0]:
                                if ((tile[0]-16,tile[1])) in bigpack[civ1][0] and ((tile[0]+16,tile[1])) in bigpack[civ1][0] and ((tile[0],tile[1]-16)) in bigpack[civ1][0] and ((tile[0],tile[1]+16)) in bigpack[civ1][0]:
                                    bigpack[civ2][0].remove(tile)
                                    bigpack[civ1][0].append(tile)
                            #if tilegot in bigpack[civ1][0] and tilegot in bigpack[civ2][0]:
                            #    print("wtf")
                            #    bigpack[civ2][0].remove(tilegot)

                        elif bigpack[civ1][11][2]<bigpack[civ2][11][2]:
                            #print(bigpack[civ2][3]+" won")
                            tilegot = other.findbordertile(bigpack,civ2,civ1)
                            if tilegot == -1:
                                continue
                            bigpack[civ1][0].remove(tilegot)

                            bigpack[civ2][0].append(tilegot)
                            for tile in bigpack[civ1][0]:
                                if ((tile[0]-16,tile[1])) in bigpack[civ2][0] and ((tile[0]+16,tile[1])) in bigpack[civ2][0] and ((tile[0],tile[1]-16)) in bigpack[civ2][0] and ((tile[0],tile[1]+16)) in bigpack[civ2][0]:
                                    bigpack[civ1][0].remove(tile)
                                    bigpack[civ2][0].append(tile)
                            #if tilegot in bigpack[civ1][0] and tilegot in bigpack[civ2][0]:
                            #    print("wtf")
                            #    bigpack[civ1][0].remove(tilegot)


                    try:
                        #print("tile got is: " +  str(int( (tilegot[0]/16)+1  ))+","+str(int(   (tilegot[1]/16)+1  )))
                        pass

                        #if tilegot in bigpack[civ1][0] and tilegot in bigpack[civ2][0]:
                        #    print("wtf")
                    except:
                        pass
                    #print("  ")
                    bigpack[civ1][11][1]-=1
                    bigpack[civ2][11][1]-=1
                    #print(bigpack[civ1][3]+" turns: "+str(bigpack[civ1][11][1]))
                    #print(bigpack[civ2][3]+" turns: "+str(bigpack[civ2][11][1]))

                    if bigpack[civ1][11][1] == 0 and bigpack[civ2][11][1] == 0:
                        bigpack[civ1][11][0]=-1
                        bigpack[civ2][11][0]=-1


                    bigpack[civ1][11][3]=1
                    bigpack[civ2][11][3]=1
                    return bigpack
                else:
                    return bigpack
        except:
            bigpack[civ1][11][0] = -1
            bigpack[civ2][11][0] = -1
            bigpack[civ1][11][2] = 0
            bigpack[civ2][11][2] = 0
            bigpack[civ1][11][3] = 1
            bigpack[civ2][11][3] = 1
            return bigpack
    def findbordertile(bigpack,civ1,civ2):
        atiles =list()
        for tile in bigpack[civ1][0]:

            if ((tile[0]-16,tile[1])) in bigpack[civ2][0]:
                atiles.append((tile[0]-16,tile[1]))

            if ((tile[0]+16,tile[1])) in bigpack[civ2][0]:
                atiles.append((tile[0]+16,tile[1]))

            if ((tile[0],tile[1]-16)) in bigpack[civ2][0]:
                atiles.append((tile[0],tile[1]-16))

            if ((tile[0],tile[1]+16)) in bigpack[civ2][0]:
                atiles.append((tile[0],tile[1]+16))
        if atiles:
            return random.choice(atiles)
        else:
            return -1


    def turnsB(sizeCondition,condition,turnType,bigpack,itemnum,possibleTurns):
        if len((bigpack[itemnum])[0]) > sizeCondition:
            for i in range(condition):
                possibleTurns.append(turnType)
            return possibleTurns
        else:
            return possibleTurns
    def turnsS(sizeCondition,condition,turnType,bigpack,itemnum,possibleTurns):
        if len((bigpack[itemnum])[0]) <= sizeCondition:

            for i in range(condition):
                possibleTurns.append(turnType)
            return possibleTurns
        else:
            return possibleTurns
    def findxy(x,y):
        if x>640 or y>640 or 0>x or 0>y:
            return x,y
        i = 0
        mynums = list()
        while i != 640:
            mynums.append(i)
            i+=16
        while x not in mynums:
            x-=1
        while y not in mynums:
            y-=1
        return x,y
class nature():
    def volcanostuff(volcanoCoords):

        try:
            for volcano in range(len(volcanoCoords)):
                volcanoCoords[volcano][1]
                if random.randint(1,5) == 1:
                    volcanoCoords[volcano][1]+=1
        except:
            for volcano in range(len(volcanoCoords)):
                volcanoCoords[volcano].append(random.randint(0,75))
        for volcano in volcanoCoords:
            if volcano[1] == 80:
                volcano[1] = 0
            if volcano[1] >= 75:
                win.blit(vol6,(volcano[0]))
            elif volcano[1] >= 70:
                win.blit(vol5,(volcano[0]))
            elif volcano[1] >= 65:
                win.blit(vol4,(volcano[0]))
            elif volcano[1] >= 60:
                win.blit(vol3,(volcano[0]))
            elif volcano[1] >= 20:
                win.blit(vol2,(volcano[0]))
            elif volcano[1] >= 0:
                win.blit(vol1,(volcano[0]))
        return volcanoCoords

worldGameState = False
worldCreateState = False
titleGameState = True
saveScreen = False
isdoingworldreset = False
###FONTS
gamereset = True
endGame = False
turnamount = 1
savegame = 0
myalpha = 180
fancyview = False
displayCitiesButton = 2
while True:
    while titleGameState == True:
        mainScreen = True
        saveScreen = False
        worldChoiceScreen = False
        while mainScreen == True:
            mainScreenOptions = [[160,"New",240],
            [320,"Saves",240+160],
            [480,"Create",240+320],]
            menu.title("DESNE")
            menu.bar(mainScreenOptions)

            for event in game.event.get():
                if event.type == game.MOUSEBUTTONDOWN and event.button == LEFT:
                        if baroption1.get_rect(top=(160),left=(256)).collidepoint(event.pos):
                            Newmus.play()
                            savegame = 0
                            worldGameState = True
                            worldChoiceScreen = True
                            mainScreen = False
                        if baroption1.get_rect(top=(320),left=(256)).collidepoint(event.pos):
                            Newmus.play()
                            worldGameState = True
                            saveScreen = True
                            mainScreen = False
                        if baroption1.get_rect(top=(320+160),left=(256)).collidepoint(event.pos):
                            Newmus.play()
                            savegame=0
                            worldCreateState = True
                            titleGameState = False
                            mainScreen = False
                if event.type == game.QUIT:
                    endGame = True
                    gamereset=False
                    worldGameState = False
                    titleGameState = False
                    mainScreen = False

            game.display.flip()
        while worldChoiceScreen == True:

            worldChoiceScreenOptions = [[160,"Island",240],
            [320,"Pangea",240+160],
            [480,"Random",240+320],]
            menu.title("World Options")
            menu.bar(worldChoiceScreenOptions)
            for event in game.event.get():
                if event.type == game.MOUSEBUTTONDOWN and event.button == LEFT:
                        if baroption1.get_rect(top=(160),left=(256)).collidepoint(event.pos):
                            Newmus.play()
                            minsize = 8#6
                            maxsize = 14#12
                            minrectgen = 6
                            maxrectgen = 7
                            chanceremove = 200
                            chanceamount = 200
                            maptype = "island"
                            worldGameState = True
                            titleGameState = False
                            worldChoiceScreen = False
                        if baroption1.get_rect(top=(320),left=(256)).collidepoint(event.pos):
                            Newmus.play()
                            minsize = 8
                            maxsize = 10
                            minrectgen = 28
                            maxrectgen = 36
                            chanceremove = 200
                            chanceamount = 200
                            maptype = "pangea"
                            worldGameState = True
                            titleGameState = False
                            worldChoiceScreen = False
                        if baroption1.get_rect(top=(480),left=(256)).collidepoint(event.pos):
                            Newmus.play()
                            minsize = 6
                            maxsize = 12
                            minrectgen = 6
                            maxrectgen = 36
                            chanceremove = 200
                            chanceamount = 200
                            maptype = "random"
                            worldGameState = True
                            titleGameState = False
                            worldChoiceScreen = False
                if event.type == game.QUIT:
                    endGame = True
                    gamereset=False
                    worldGameState = False
                    titleGameState = False
                    worldChoiceScreen = False

            game.display.flip()
        while saveScreen == True:

            mainScreenOptions = [[160,"Save 1",240],
            [320,"Save 2",400],
            [480,"Save 3",560],]
            menu.title("Saves")
            menu.bar(mainScreenOptions)
            for event in game.event.get():
                if event.type == game.MOUSEBUTTONDOWN and event.button == LEFT:
                        if baroption1.get_rect(top=(160),left=(256)).collidepoint(event.pos):
                            Newmus.play()
                            savegame = 1
                            minsize = 6
                            maxsize = 12
                            minrectgen = 6
                            maxrectgen = 36
                            chanceremove = 200
                            chanceamount = 200
                            savegame =1
                            maptype = "random"
                            worldGameState = True
                            titleGameState = False
                            saveScreen = False
                        if baroption1.get_rect(top=(320),left=(256)).collidepoint(event.pos):
                            Newmus.play()
                            savegame = 2
                            minsize = 6
                            maxsize = 12
                            minrectgen = 6
                            maxrectgen = 36
                            chanceremove = 200
                            chanceamount = 200
                            savegame =2
                            maptype = "random"
                            worldGameState = True
                            titleGameState = False
                            saveScreen = False
                        if baroption1.get_rect(top=(480),left=(256)).collidepoint(event.pos):
                            Newmus.play()
                            savegame = 3
                            minsize = 6
                            maxsize = 12
                            minrectgen = 6
                            maxrectgen = 36
                            chanceremove = 200
                            chanceamount = 200
                            savegame =3
                            maptype = "random"
                            worldGameState = True
                            titleGameState = False
                            saveScreen = False
                if event.type == game.QUIT:
                    endGame = True
                    gamereset=False
                    worldGameState = False
                    titleGameState = False
                    saveScreen = False
            game.display.flip()
    if savegame == 1:
        fileOpenType = "Saves/World1"
    elif savegame == 2:
        fileOpenType = "Saves/World2"
    elif savegame == 3:
        fileOpenType = "Saves/World3"
    if savegame == 0 and worldGameState == True:
        fileOpenType = "DataFiles"
        while gamereset == True:
                landCoords,seaCoords,allCoords,mountainCoords,snowCoords,grassCoords,desertCoords,treeCoords,posCoastCoords,posSpawnCoords,mountainOffset,treeOffset,volcanoCoords,beachtype = gen.finalgen()
                Naturedata = [landCoords,seaCoords,allCoords,mountainCoords,snowCoords,grassCoords,desertCoords,treeCoords,posCoastCoords,posSpawnCoords,mountainOffset,treeOffset,volcanoCoords,beachtype]
                ### NEED THESE VARS
                fertilityIndex = society.soilfertility(mountainCoords,snowCoords,grassCoords,desertCoords,treeCoords)


                if len(names) > 2:
                    part1 = random.choice(names)
                    part2 = random.choice(names)
                    while part2 == part1:
                        part2 = random.choice(names)
                    names.remove(part1)
                    names.remove(part2)
                else:
                    f = open("TextFiles/SocietyNames.txt","r")
                    names = list()
                    for line in f:
                        names.append(line.rstrip("\n"))
                    f.close()
                    names.remove(names[-1])
                    part1 = random.choice(names)
                    part2 = random.choice(names)
                    while part2 == part1:
                        part2 = random.choice(names)
                    #print(part1,part2)
                    names.remove(part1)
                    names.remove(part2)
                WorldName = part1+part2
                WorldName = WorldName[0].upper()+WorldName[1:]

                year = 0
                maxyear = 0
                civselected = -1
                tileselected = (0,0)
                area = set()
                ### SOCIETYGEN
                bigpack = list()
                colorcodes = fullcolorlist[:]
                for i in range(random.randint(3,7)):
                #for i in range(random.randint(3,7)):
                    datapack,posSpawnCoords = societygen.spawning(posSpawnCoords,colorcodes,names)
                    bigpack.append(datapack)
                ### FIRST EXPANSION
                for i in range(10):
                    for itemnum in range(len(bigpack)):
                        if random.randint(1,2) == 1:
                            bigpack[itemnum],posSpawnCoords = societygen.expand(bigpack[itemnum],posSpawnCoords,seaCoords)
                            for item in bigpack:
                                for tile in item[0]:
                                    if tile in posSpawnCoords:
                                        posSpawnCoords.remove(tile)
                volcanoCoordsCopy=list()
                for item in volcanoCoords:
                    volcanoCoordsCopy.append(item)
                ###SMALL STUFF
                rotations = dict()
                for tile in allCoords:
                    rotations[tile] = random.choice([0,90,180,360])

                grasstype = dict()
                for tile in grassCoords:
                    grasstype[tile] = random.choice([grass,grass2,grass3,grass4])



                with open(fileOpenType+"/data"+str(year)+".pickle","wb") as file:
                    pickle.dump([bigpack,fertilityIndex,Naturedata], file)

                '''
                waveCoords = list()
                for i in range(random.randint(0,2)):
                    waveCoords.append(  [ (-16,(random.randint(1,16)*40)),random.randint(2,5)   ]   )
                print(waveCoords)
                '''

                worldGameState = True
                gamereset = False
    elif savegame > 0:
        path, dirs, files = next(os.walk(os.getcwd()+"/Saves/World"+str(savegame)))
        files = other.deletenonpickle(files)
        #print(files)
        maxyear =len(files)-1
        year = maxyear
        civselected = -1
        tileselected = (0,0)
    else:
        year = 0
        maxyear=year
    ###FIX THIS BUG
    win.blit(titleimg,((0,0)))
    ###ABLE TO SEE THROUGH WATER
    gameloops = 0
    mainGameScreen = True
    newsGameScreen = False
    tribeGameScreen = False
    while worldGameState == True:
        while mainGameScreen == True:
            ###LOADING IN THE SAVEGAMES FOR PREMADE WORLDS
            if savegame != 0 and gameloops == 0:
                #try:
                if year !=-1:
                    with open(fileOpenType+"/data"+str(year)+".pickle","rb") as pickle_in:
                        fulllist = (pickle.load(pickle_in))
                        bigpack = fulllist[0][:]
                        fertilityIndex = dict(fulllist[1])
                        Naturedata = fulllist[2][:]
                        landCoords = Naturedata[0]
                        seaCoords = Naturedata[1]
                        allCoords = Naturedata[2]
                        mountainCoords = Naturedata[3]
                        snowCoords = Naturedata[4]
                        grassCoords = Naturedata[5]
                        desertCoords = Naturedata[6]
                        treeCoords = Naturedata[7]
                        posCoastCoords = Naturedata[8]
                        posSpawnCoords = Naturedata[9]
                        mountainOffset = Naturedata[10]
                        treeOffset = Naturedata[11]
                        volcanoCoords = Naturedata[12]
                        beachtype = Naturedata[13]
                        volcanoCoordsCopy=list()
                        for item in volcanoCoords:
                            volcanoCoordsCopy.append(item)
                        rotations = dict()
                        for tile in allCoords:
                            rotations[tile] = random.choice([0,90,180,270])
                        grasstype = dict()
                        for tile in grassCoords:
                            grasstype[tile] = random.choice([grass,grass2,grass3,grass4])
                        #titleGameState=True
                        #break
                    #    worldGameState=False
                else:
                    worldGameState=False
                #except:
                #    print("you should only get this message if you are trying to click on an empty save file")
                #    worldGameState=False
            if worldGameState == False:
                titleGameState = True
                break
            if gameloops==0:
                coastCoords=set()
                oceanCoords=set()
                for tile in seaCoords:
                    if (tile[0]+16,tile[1]) not in landCoords and (tile[0],tile[1]+16) not in landCoords and (tile[0]-16,tile[1]) not in landCoords and (tile[0],tile[1]-16) not in landCoords and (tile[0]-16,tile[1]-16) not in landCoords and (tile[0]+16,tile[1]-16) not in landCoords and (tile[0]-16,tile[1]+16) not in landCoords and (tile[0]+16,tile[1]+16) not in landCoords and (tile[0]-32,tile[1]+16) not in landCoords and (tile[0]-32,tile[1]-16) not in landCoords and (tile[0]+32,tile[1]+16) not in landCoords and (tile[0]+32,tile[1]-16) not in landCoords and (tile[0]+16,tile[1]+32) not in landCoords and (tile[0]+16,tile[1]-32) not in landCoords and (tile[0]-16,tile[1]+32) not in landCoords and (tile[0]-16,tile[1]-32) not in landCoords and (tile[0],tile[1]-32) not in landCoords and (tile[0],tile[1]+32) not in landCoords and (tile[0]+32,tile[1]) not in landCoords and (tile[0]-32,tile[1]) not in landCoords:
                        oceanCoords.add(tile)
                    else:
                        coastCoords.add(tile)
                actualVolcanoCoords = set()
                for volcano in volcanoCoords:
                    actualVolcanoCoords.add(volcano[0])

            gameloops+=1
            ###LOADING IN THE ICONS AS WELL AS THE SIDEBARS
            civselected = -1
            for pack in bigpack:
                if tileselected in pack[0]:
                    civselected = bigpack.index(pack)
            sidebar.right()
            sidebar.bottom()
            sidebar.icons(turnamount,myalpha,savegame,fancyview,displayCitiesButton)
            win.blit(button,(640,640,640+192,640+192))

            ### BLITTING THE MAIN TERRAIN ONTO THE MAP
            for tile in coastCoords:win.blit(game.transform.rotate(water,rotations[tile]),(tile))
            for tile in oceanCoords:win.blit(game.transform.rotate(ocean,rotations[tile]),(tile))

            for tile in desertCoords:win.blit(game.transform.rotate(sand,rotations[tile]),(tile))

            for tile in grassCoords:win.blit(game.transform.rotate(grasstype[tile],rotations[tile]),(tile))
            if fancyview==True: gen.fancytiles(grassCoords,beachtype)#and myalpha!=1000
            for tile in snowCoords:win.blit(game.transform.rotate(snow,rotations[tile]),(tile))
            if fancyview==True: gen.fancytiles(snowCoords,beachtype)



            for tile in mountainCoords:win.blit(mountain,((tile[0]+mountainOffset[tile]),(tile[1])))
            for tile in treeCoords:win.blit(tree,((tile[0]+treeOffset[tile]),(tile[1])))
            #for tile in posSpawnCoords:win.blit(test,tile)
            #print(volcanoCoordsCopy)
            if volcanoCoordsCopy:
                volcanoCoordsCopy = nature.volcanostuff(volcanoCoordsCopy)
            ###CALCULATING POPULATION
            for itemnum in range(len(bigpack)):
                bigpack[itemnum][5] = society.populationcalc(bigpack[itemnum][0],fertilityIndex)
            ###BLITTING THE TRIBES TERRITORY + THE ABILITY TO CLICK ON THE TRIBES *

            society.displaytribes(myalpha,posSpawnCoords,bigpack)
            ###THE INFORMATION FOR THE TRIBES ON THE SIDEBAR *
            sidebar.tribetext(civselected)
            sidebar.landtext(tileselected)
            ### CITIES
            if displayCitiesButton ==3:
                society.displaycities (bigpack)
            if displayCitiesButton ==3 or displayCitiesButton ==2:
                society.displaycapitals(bigpack)
            #else if
            ###CLICKING EVENTS
            keys = game.key.get_pressed()
            for event in game.event.get():
                if event.type == game.MOUSEBUTTONDOWN and event.button == LEFT:

                    ###ICONS
                    for pack in bigpack:
                        for tile in pack[0]:
                            if game.Surface((16,16)).get_rect(top=(tile[1]),left=(tile[0])).collidepoint(game.mouse.get_pos()):
                                Tribemus.play()

                    x,y = other.findxy((game.mouse.get_pos())[0],(game.mouse.get_pos())[1])
                    if (x,y) in allCoords:
                        tileselected = (x,y)


                                #civselected = bigpack.index(pack)
                                #print(bigpack[civselected][1])
                    if treeicon.get_rect(top=672,left=432).collidepoint(game.mouse.get_pos()):
                        myalpha = 0
                        Iconmus.play()
                    elif bothicon.get_rect(top=720,left=432).collidepoint(game.mouse.get_pos()):
                        myalpha = 180
                        Iconmus.play()
                    elif politicalicon.get_rect(top=768,left=432).collidepoint(game.mouse.get_pos()):
                        myalpha = 1000
                        Iconmus.play()
                    elif num11.get_rect(top=672,left=480).collidepoint(game.mouse.get_pos()):
                        Iconmus.play()
                        turnamount =1
                    elif num51.get_rect(top=720,left=480).collidepoint(game.mouse.get_pos()):
                        Iconmus.play()
                        turnamount =5
                    elif num101.get_rect(top=768,left=480).collidepoint(game.mouse.get_pos()):
                        Iconmus.play()
                        turnamount =10
                    elif camera1.get_rect(top=672+48,left=384).collidepoint(game.mouse.get_pos()):
                        Iconmus.play()
                        fancyview=True
                    elif nocamera1.get_rect(top=672+48+48,left=384).collidepoint(game.mouse.get_pos()):
                        Iconmus.play()
                        fancyview=False

                    elif house1.get_rect(top=720-48,left=288).collidepoint(game.mouse.get_pos()):
                        Iconmus.play()
                        displayCitiesButton=2 #288,720
                    elif city1.get_rect(top=720,left=288).collidepoint(game.mouse.get_pos()):
                        Iconmus.play()
                        displayCitiesButton=3
                    elif historychanger1.get_rect(top=672,left=384).collidepoint(game.mouse.get_pos()):
                        Iconmus.play()
                        delyear = maxyear-year
                        for file in range(delyear):
                            try:
                                os.remove(  os.getcwd()+"/"+fileOpenType+ "/data"+str(maxyear-file)+".pickle")
                            except:
                                print("error, something might be wrong")
                                pass
                        maxyear=year
                    #640+(int(192/2)-16) ,640-48
                    elif quest1.get_rect(top=640-48,left=640+(int(192/2)-16)).collidepoint(game.mouse.get_pos()):
                        Iconmus.play()
                        if savegame != 0:
                            savegame = 0
                        gamereset = True
                        titleGameState = True
                        worldGameState = False
                    elif mail1.get_rect(top=672,left=384-48).collidepoint(game.mouse.get_pos()):
                        if civselected != -1:
                            newsGameScreen = True
                            mainGameScreen = False
                    elif morebutton1.get_rect(top=288+48,left=640+48).collidepoint(game.mouse.get_pos()):
                        if civselected != -1:
                            tribeGameScreen = True
                            mainGameScreen = False
                    ### SAVE GAMES *
                    Whenclickonsavebuttons = [
                    [672,"1",],
                    [720,"2",],
                    [768,"3",],
                    ]
                    if savegame == 0:
                        for worlds in Whenclickonsavebuttons:
                            if num101.get_rect(top=worlds[0],left=48).collidepoint(game.mouse.get_pos()):
                                Iconmus.play()
                                path, dirs, files = next(os.walk(os.getcwd()+"/Saves/World"+worlds[1]))
                                files = other.deletenonpickle(files)
                                for thing in range(len(files)):
                                    try:
                                        os.remove(os.getcwd()+"/Saves/World"+worlds[1]+"/data"+str(thing)+".pickle")
                                    except:
                                        pass
                                path, dirs, files = next(os.walk(os.getcwd()+"/DataFiles"))
                                files = other.deletenonpickle(files)
                                #print(files)

                                #print(files)
                                for thing in range(len(files)):
                                    with open(fileOpenType+"/data"+str(thing)+".pickle","rb") as pickle_in:
                                        fulllist = (pickle.load(pickle_in))
                                    with open("Saves/World"+worlds[1]+"/data"+str(thing)+".pickle","wb") as file:
                                        pickle.dump(fulllist, file)
                    ### NEW MAP BUTTON

                    if button.get_rect(top=(640),left=(640)).collidepoint(event.pos):
                        if savegame != 0:
                            savegame = 0
                        Newmus.play()
                        gamereset = True
                        isdoingworldreset = True
                        mainGameScreen= False
                        worldGameState = False

                    ### NEXT TURN BUTTON

                    elif arrow1.get_rect(top=672,left=528).collidepoint(game.mouse.get_pos()):
                        Iconmus.play()
                        for i in range(turnamount):
                            if year == maxyear:

                                deleteevents = list()
                                year+=1
                                maxyear = year
                                ###RESET WAR TURNS
                                #for thing in bigpack
                                for thing in range(len(bigpack)):
                                    bigpack[thing][11][3]=0

                                    bigpack[thing][0] = set(bigpack[thing][0])
                                    bigpack[thing][0] = list(bigpack[thing][0])
                                if 1==1:
                                    for itemnum in range(len(bigpack)):

                                        try:
                                            bigpack[itemnum]
                                        except:
                                            continue


                                        if len(bigpack[itemnum][0])==False:
                                            bigpack.remove(bigpack[itemnum])
                                        ###BASE POPULATION CHANGE

                                        try:
                                            bigpack[itemnum][0]
                                        except:
                                            continue

                                        if random.randint(1,4) != 1:
                                            ###INCREASE
                                            fertilityIndex = society.popadd(bigpack[itemnum][0],fertilityIndex,True)

                                        else:
                                            ###DECREASE
                                            fertilityIndex = society.popadd(bigpack[itemnum][0],fertilityIndex,False)
                                        newsstuff = list()
                                        newslist = list()
                                        possibleTurns = list()
                                        #turnsB(sizeCondition,randomConditionSmall,randomConditionBig,turnType,bigpack,itemnum,possibleTurns)
                                        possibleTurns=other.turnsB(20,4,"consolidate",bigpack,itemnum,possibleTurns)
                                        cancolonize = False
                                        for i in (bigpack[itemnum])[0]:
                                            if ((i[0]-16,i[1])) in seaCoords or ((i[0]+16,i[1])) in seaCoords or ((i[0],i[1]-16)) in seaCoords or ((i[0],i[1]+16)) in seaCoords:
                                                cancolonize = True
                                        if cancolonize == True:
                                            possibleTurns=other.turnsB(20,5,"colonize",bigpack,itemnum,possibleTurns)

                                        possibleTurns=other.turnsS(10,20,"other",bigpack,itemnum,possibleTurns)

                                        possibleTurns=other.turnsB(10,400,"other",bigpack,itemnum,possibleTurns)

                                        possibleTurns=other.turnsS(20,200,"expand",bigpack,itemnum,possibleTurns)

                                        possibleTurns=other.turnsB(20,500,"expand",bigpack,itemnum,possibleTurns)

                                        possibleTurns=other.turnsB(40,300,"expand",bigpack,itemnum,possibleTurns)
                                        turnchoice = random.choice(possibleTurns)
                                        ## ADDING CHECKS TO MAKE SURE EXPAND IS WORKING
                                        if turnchoice == "expand":
                                            for num in range(random.randint(1,10)):
                                                if posSpawnCoords:
                                                    bigpack[itemnum],posSpawnCoords = societygen.expand(bigpack[itemnum],posSpawnCoords,seaCoords)
                                            newsstuff.append(["expand","nothin"])
                                        if turnchoice == "other":
                                            ### Smallchance events
                                            ### Rebelion
                                            civgot = other.findbordercountries(bigpack[itemnum],bigpack)
                                            whathappens = random.randint(1,60)
                                            if whathappens == 1 or whathappens == 2:
                                                area = other.findarea(bigpack[itemnum][0])
                                                #print("attempted rev")
                                                if bigpack[itemnum][8] not in area:
                                                    #if len(area) > 5:
                                                    datapack,area = societygen.spawning(area,colorcodes,names)
                                                    datapack[0] = list(area)
                                                    #datapack[8] = random.choice(list(area))
                                                    bigpack[itemnum][0] = set(bigpack[itemnum][0])
                                                    bigpack[itemnum][0] -= set(area)
                                                    bigpack[itemnum][0] = list(bigpack[itemnum][0])
                                                    bigpack.append(datapack)
                                                    landchanged=False
                                                    while landchanged==False:
                                                        for tile in bigpack[itemnum][0]:
                                                            if tile != bigpack[itemnum][8]:
                                                                if (tile[0]+16,tile[1]) not in bigpack[itemnum][0] and (tile[0]-16,tile[1]) not in bigpack[itemnum][0] and (tile[0],tile[1]+16) not in bigpack[itemnum][0] and (tile[0],tile[1]-16) not in bigpack[itemnum][0]:
                                                                    ## if tile isnt in the avalable tiles north south east and west
                                                                    if (tile[0]+16,tile[1]) not in posSpawnCoords and (tile[0]-16,tile[1]) not in posSpawnCoords and (tile[0],tile[1]+16) not in posSpawnCoords and (tile[0],tile[1]-16) not in posSpawnCoords:
                                                                        bigpack[itemnum][0].remove(tile)
                                                                        posSpawnCoords.add(tile)
                                                                        ### AWFUL CODE, NEEDS TO BE REDONE AT SOME POINT
                                                                        ###IT VALUES EAST OVER EVERYTHING, NEED TO MAKE RANDOM
                                                                        for i in bigpack:
                                                                            if tile in posSpawnCoords:
                                                                                if (tile[0]+16,tile[1]) in i[0]:
                                                                                     i[0].append(tile)
                                                                                     posSpawnCoords.remove(tile)
                                                                                     landchanged=True
                                                                                elif (tile[0]-16,tile[1]) in i[0]:
                                                                                     i[0].append(tile)
                                                                                     posSpawnCoords.remove(tile)
                                                                                     landchanged=True
                                                                                elif (tile[0],tile[1]+16) in i[0]:
                                                                                     i[0].append(tile)
                                                                                     posSpawnCoords.remove(tile)
                                                                                     landchanged=True
                                                                                elif (tile[0],tile[1]-16) in i[0]:
                                                                                     i[0].append(tile)
                                                                                     posSpawnCoords.remove(tile)
                                                                                     landchanged=True
                                                            landchanged=True
                                            if whathappens == 3:
                                                if civgot != "false":
                                                    if len(bigpack[itemnum][0]) <= random.randint(50,100) and len(bigpack[civgot][0]) <= random.randint(50,100):
                                                        deleteevents.append([civgot,itemnum,"merge"])
                                            if whathappens == 4 or whathappens == 5 or whathappens == 6:
                                                if civgot != "false":
                                                    #if they are not against any country
                                                    if bigpack[itemnum][11][0]==-1 and bigpack[civgot][11][0]==-1:
                                                        warlength=random.randint(3,10)
                                                        #how long the war will be
                                                        bigpack[itemnum][11][1] = warlength
                                                        bigpack[civgot][11][1] = warlength
                                                        #who they are vsing
                                                        bigpack[itemnum][11][0] = civgot
                                                        bigpack[civgot][11][0] = itemnum
                                                        #warturn(bigpack,itemnum,civgot)
                                                        #def warturn(bigpack,civ1,civ2):
                                                        #print(bigpack[itemnum][11],"ebic")
                                                        #print(bigpack[civgot][11],"loser")
                                                        #bigpack[itemnum][1] = (0,0,0)
                                                        #bigpack[civgot][1] = (0,0,0)


                                            else:
                                                newsstuff.append("nothing")
                                            #war = [with who,turns since started,win battle chance (use randint),has taken turn yet]  11
                                        if turnchoice == "colonize":

                                            if posCoastCoords:
                                                newsstuff.append(["colonize","nothin"])
                                                bigpack[itemnum],posCoastCoords = societygen.colonize(bigpack[itemnum],posCoastCoords,seaCoords)
                                            else:
                                                turnchoice = "consolidate"
                                        if turnchoice == "consolidate":
                                            newsstuff.append(["consolidation","nothin"])

                                        bigpack = other.warturn(bigpack,itemnum)
                                        if bigpack[itemnum][8] in bigpack[itemnum][0]:
                                            pass
                                        else:
                                            print("Capital lost add effect l8r")
                                            if bigpack[itemnum][0]:
                                                bigpack[itemnum][8] = random.choice(bigpack[itemnum][0])
                                        for item in bigpack:
                                            for tile in item[0]:

                                                if tile in posSpawnCoords:
                                                    posSpawnCoords.remove(tile)
                                                if tile in posCoastCoords:
                                                    posCoastCoords.remove(tile)

                                        ### SECONDARY
                                        if random.randint(1,5) == 1:

                                            if ((bigpack[itemnum])[4] == "Chieftan" or (bigpack[itemnum])[4] == "Interm Government")and len((bigpack[itemnum])[0]) > 20:
                                                newsstuff.append("proclamation")

                                                govs = list()
                                                govs = ["Empire","Republic","Kingdom","Commune","Junta","Confederation"]
                                                if "Expansionist,+50%"+" Expansion" in (bigpack[itemnum])[2]:
                                                    for i in range(3):
                                                        govs.append("Empire")
                                                    govs.append("Junta")
                                                (bigpack[itemnum])[4] = random.choice(govs)

                                            elif (bigpack[itemnum])[4] == "Chieftan" and year > 40:
                                                (bigpack[itemnum])[4] = "City State"
                                        ###CITY GENERATION
                                        for i in range(len(bigpack[itemnum][0])):
                                            if random.randint(1,len(bigpack[itemnum][10])*30) == 1:

                                                newCity = random.choice(bigpack[itemnum][0])

                                                if newCity in bigpack[itemnum][10]:
                                                    pass
                                                else:
                                                    try:
                                                        bigpack[itemnum][10][newCity] = random.choice(allcities)
                                                    except:
                                                        with open("TextFiles/cities.txt","r") as file:
                                                            for line in file:
                                                                allcities.append(line.rstrip("\n"))
                                                        #cities[spawntile] = random.choice(allcities)
                                                        bigpack[itemnum][10][newCity] = random.choice(allcities)

                                                    newsstuff.append(["cityfounded",newCity])

                                        for object in newsstuff:
                                            if object!= "nothing":
                                                newslist.append(News.news(bigpack[itemnum],object))


                                        #newslist.append(["test","1"])
                                        #newslist.append(["test","2"])
                                        #newslist.append(["test","3"])
                                        #newslist.append(["test","4"])
                                        bigpack[itemnum][9] = newslist[:]
                                else:pass
                                ###WorldEvents
                                if random.randint(1,2) == 1:
                                    pass
                                    ###Plague
                                    ###divide a random continents pop by random number

                                if deleteevents:
                                    deleteeventdoing = random.choice(deleteevents)
                                    if deleteeventdoing[2] == "merge":

                                        civgot = deleteeventdoing[1]
                                        itemnum = deleteeventdoing[0]
                                        newdatapack,area = societygen.spawning(bigpack[itemnum][0][:],colorcodes,names)
                                        if random.randint(1,2) == 1:
                                            if random.randint(1,2) ==1:
                                                newdatapack[3] = bigpack[civgot][3]
                                            else:
                                                newdatapack[3] = bigpack[itemnum][3]
                                        newdatapack[0] = bigpack[civgot][0] + bigpack[itemnum][0]
                                        #newdatapack[6] = bigpack[civgot][6] + bigpack[itemnum][6]
                                        newdatapack[8] = bigpack[civgot][8]
                                        newdatapack[10].update(bigpack[civgot][10])
                                        newdatapack[10].update(bigpack[itemnum][10])
                                        if itemnum > civgot:
                                            bigpack.remove(bigpack[itemnum])
                                            bigpack.remove(bigpack[civgot])
                                        else:
                                            bigpack.remove(bigpack[civgot])
                                            bigpack.remove(bigpack[itemnum])

                                        bigpack.append(newdatapack)

                                        if civselected == itemnum or civselected == civgot:
                                            civselected = bigpack.index(newdatapack)
                                with open(fileOpenType+"/data"+str(year)+".pickle","wb") as file:
                                    pickle.dump([bigpack,fertilityIndex,Naturedata], file)
                            else:
                                try:
                                    if civselected != -1:
                                        curciv = bigpack[civselected]
                                    if year != maxyear:
                                        year += 1
                                    with open(fileOpenType+"/data"+str(year)+".pickle","rb") as pickle_in:
                                        fulllist = (pickle.load(pickle_in))
                                        bigpack = fulllist[0][:]
                                        fertilityIndex = dict(fulllist[1])
                                        Naturedata = fulllist[2][:]
                                    if civselected != -1:
                                        for i in bigpack:
                                            if curciv[3] in i:
                                                civselected = bigpack.index(i)
                                            else:
                                                if curciv[0] in i[0]:
                                                    civselected = bigpack.index(i)
                                except:
                                    print("you shouldnt be getting this message. please msg oscar if u are. errorcode #0012")
                    ### BACKWARD BUTTON

                    elif arrow1.get_rect(top=752,left=528).collidepoint(game.mouse.get_pos()):
                        Iconmus.play()
                        for i in range(turnamount):
                            if year != 0:
                                year -=1

                        with open(fileOpenType+"/data"+str(year)+".pickle","rb") as pickle_in:
                            fulllist = (pickle.load(pickle_in))
                            bigpack = fulllist[0][:]
                            fertilityIndex = dict(fulllist[1])
                            Naturedata = fulllist[2][:]
                ###QUIT FUNCTION

                if event.type == game.QUIT:
                    endGame = True
                    worldGameState = False
            if True:
                landCoords = Naturedata[0]
                seaCoords = Naturedata[1]
                allCoords = Naturedata[2]
                mountainCoords = Naturedata[3]
                snowCoords = Naturedata[4]
                grassCoords = Naturedata[5]
                desertCoords = Naturedata[6]
                treeCoords = Naturedata[7]
                posCoastCoords = Naturedata[8]
                posSpawnCoords = Naturedata[9]
                mountainOffset = Naturedata[10]
                treeOffset = Naturedata[11]
                volcanoCoords = Naturedata[12]
                beachtype = Naturedata[13]
            win.blit(test,tileselected)
            other.mousemovement()
            other.displayyr()
            game.display.flip()



        gameloops = 0
        while newsGameScreen == True:
            win.blit(titleimg,(0,0))
            if gameloops==0:#9 is news in datapack
                allnews = bigpack[civselected][9][:]
                newselected = 0
                #news1 = size18.render(str(bigpack[civselected][9][0]), True, textcolor)
                try:
                    headline = allnews[0][0]
                    story = wrapline(str(allnews[0][1]), size18, 700)
                    isnews=True
                except:
                    headline = "There has been no news this week!"
                    story = wrapline(str(""), size18, 700)
                    isnews=False
                bigearth = game.transform.scale(earth1, (208, 208))
                bigearth2 = game.transform.scale(earth2, (208, 208))
                bignewsarrow1 = game.transform.scale(newsarrow1, (208, 208))
                bignewsarrow2 = game.transform.scale(newsarrow2, (208, 208))
                bignewsarrow1back = game.transform.rotate(bignewsarrow1, 180)
                bignewsarrow2back = game.transform.rotate(bignewsarrow2, 180)

            if bignewsarrow1.get_rect(top=512,left=544).collidepoint(game.mouse.get_pos()):
                win.blit(bignewsarrow2,((544,512)))
            else:
                win.blit(bignewsarrow1,((544,512)))

            if bignewsarrow1back.get_rect(top=512,left=80).collidepoint(game.mouse.get_pos()):
                win.blit(bignewsarrow2back,((80,512)))
            else:
                win.blit(bignewsarrow1back,((80,512)))

            if bigearth.get_rect(top=512,left=312).collidepoint(game.mouse.get_pos()):
                win.blit(bigearth2,((312,512)))
            else:
                win.blit(bigearth,((312,512)))



            amount = 70
            titlerender = size40.render(headline, True, textcolor)
            win.blit(titlerender,(32,32))
            for section in story:
                amount+=16
                render = size17.render(section, True, textcolor)
                win.blit(render,(32,amount))
            for event in game.event.get():
                if event.type == game.MOUSEBUTTONDOWN and event.button == LEFT:
                    if bignewsarrow1.get_rect(top=512,left=544).collidepoint(game.mouse.get_pos()):
                        Iconmus.play()
                        if isnews==True:
                            headline,story,newselected = society.getnews(True,newselected)
                    if bignewsarrow1.get_rect(top=512,left=80).collidepoint(game.mouse.get_pos()):
                        Iconmus.play()
                        if isnews==True:
                            headline,story,newselected = society.getnews(False,newselected)
                    if bigearth.get_rect(top=512,left=312).collidepoint(game.mouse.get_pos()):
                        Iconmus.play()
                        mainGameScreen=True
                        newsGameScreen=False

                if event.type == game.QUIT:
                    endGame = True
                    worldGameState = False
                    newsGameScreen= False
            gameloops+=1
            game.display.flip()
        gameloops=0
        while tribeGameScreen == True:
            if gameloops==0:#9 is news in datapack
                bigearth = game.transform.scale(earth1, (208, 208))
                bigearth2 = game.transform.scale(earth2, (208, 208))
                bigmail = game.transform.scale(mail1, (208, 208))
                bigmail2 = game.transform.scale(mail2, (208, 208))
            win.blit(titleimg,(0,0))
            if bigearth.get_rect(top=624,left=624).collidepoint(game.mouse.get_pos()):
                win.blit(bigearth2,((624,624)))
            else:
                win.blit(bigearth,((624,624)))

            if bigmail.get_rect(top=624,left=0).collidepoint(game.mouse.get_pos()):
                win.blit(bigmail2,((0,624)))
            else:
                win.blit(bigmail,((0,624)))


            #datapack = [[spawntile],color,societycharacteristics,name,governmenttype,pop,military,citzensatisfaction,spawntile,news,cities]

            Char = size18.render("Characteristics:", True, textcolor)
            TribeChar1 = size18.render(bigpack[civselected][2][0], True, textcolor)
            TribeChar2 = size18.render(bigpack[civselected][2][1], True, textcolor)
            TribeChar3 = size18.render(bigpack[civselected][2][2], True, textcolor)

            TribeGov = size18.render("Government of "+bigpack[civselected][3]+": "+bigpack[civselected][4], True, textcolor)

            TribePop = size18.render("Population of "+bigpack[civselected][3]+": "+str(bigpack[civselected][5]), True, textcolor)

            TribeMil = size18.render("Military Strength of "+bigpack[civselected][3]+": "+str(bigpack[civselected][6])+"%", True, textcolor)

            TribeSat = size18.render("Citzen Satisfaction of "+bigpack[civselected][3]+": "+str(bigpack[civselected][7])+"%", True, textcolor)


            TribeCap = size18.render("Capital of "+bigpack[civselected][3]+": "+ bigpack[civselected][10][bigpack[civselected][8]] +" ("+ str(int(bigpack[civselected][8][0]/16)+1) +" , "+ str(int(bigpack[civselected][8][1]/16)+1)+")"   , True, textcolor)

            TribeLand = size18.render("Amount of Land in "+bigpack[civselected][3]+": "+str(len(bigpack[civselected][0])), True, textcolor)

            TribeCity = size18.render("Amount of Cities in "+bigpack[civselected][3]+": "+str(len(bigpack[civselected][10])), True, textcolor)
            #TribeSat = size18.render("Citzen Satisfaction of "+bigpack[civselected][3]+": "+str(bigpack[civselected][7])+"%", True, textcolor)
            #print(bigpack[civselected][10])
            TribeName = size40.render(bigpack[civselected][4]+" of "+bigpack[civselected][3], True, textcolor)
            TribeName_rect = TribeName.get_rect(center=(screenWidth/2,64))
            #win.blit(TribeName,(32,32))
            ###Tribe Name
            win.blit(TribeName, TribeName_rect)

            win.blit(TribePop,(64,128))

            win.blit(TribeMil,(64,128+48))

            win.blit(TribeGov,(64,128+48+48))

            win.blit(TribeSat,(64,128+48+48+48))

            win.blit(TribeCap,(64,128+48+48+48+48))
            win.blit(TribeLand,(64,128+48+48+48+48+48))
            win.blit(TribeCity,(64,128+48+48+48+48+48+48))
            #win.blit(char2N,(640+24,64+48+32))
            #win.blit(char3N,(640+24,128+32+32))
            #win.blit(gov,(640+24,240))
            #win.blit(population,(640+24,288))





            for event in game.event.get():
                if event.type == game.QUIT:
                    endGame = True
                    worldGameState = False
                    tribeGameScreen= False
                if event.type == game.MOUSEBUTTONDOWN and event.button == LEFT:
                    if bigearth.get_rect(top=624,left=624).collidepoint(game.mouse.get_pos()):
                        Iconmus.play()
                        mainGameScreen=True
                        tribeGameScreen=False
                    if bigmail.get_rect(top=624,left=0).collidepoint(game.mouse.get_pos()):
                        Iconmus.play()
                        newsGameScreen=True
                        tribeGameScreen=False
            gameloops+=1
            game.display.flip()
    while worldCreateState == True:
        if gameloops == 0:


            #game.mixer.music.pause()
            allCoords=gen.allTiles()
            seaCoords=gen.allTiles()
            snowCoords=set()
            grassCoords=set()
            desertCoords=set()
            mountainCoords=set()
            treeCoords=set()
            volcanoCoords=set()
            posSpawnCoords=set()
            rotations = dict()
            for tile in allCoords:
                rotations[tile] = random.choice([0,90,180,270])
            mountainOffset = {}
            treeOffset = {}
            biggrass = game.transform.scale(grass, (64, 64))
            bigsand = game.transform.scale(sand, (64, 64))
            bigsnow = game.transform.scale(snow, (64, 64))
            bigmouse = game.transform.scale(mouse, (64, 64))
            bigmountain = game.transform.scale(mountain, (64, 64))
            bigtree = game.transform.scale(tree, (64, 64))
            bigvolcano = game.transform.scale(vol1, (64, 64))
            inHand = grass
            bigpack=list()
            for tile in allCoords:
                mountainOffset[tile] = random.randint(0,4)
            for tile in allCoords:
                treeOffset[tile] = random.randint(0,8)
            beachtype = dict()
            for tile in allCoords:
                beachtype[tile] = random.choice([1,2,3])


        sidebar.right()
        sidebar.bottom()
        win.blit(button,(640,640,640+192,640+192))



        x = (game.mouse.get_pos())[0]
        y = (game.mouse.get_pos())[1]
        i = 0
        mynums = list()
        while i != 640:
            mynums.append(i)
            i+=16
        if (game.mouse.get_pos())[0] < 640 and (game.mouse.get_pos())[1] < 640 and (game.mouse.get_pos())[0] != 0 and (game.mouse.get_pos())[1] != 0:
            while x not in mynums:
                x-=1
            while y not in mynums:
                y-=1
            validMouseSpace = True
        else:
            validMouseSpace = False


        for event in game.event.get():
            if validMouseSpace:
                if game.mouse.get_pressed()[2]:
                    for coordSet in [snowCoords,grassCoords,desertCoords,mountainCoords,treeCoords,volcanoCoords]:
                        if ((x,y)) in coordSet:
                            coordSet.remove(((x,y)))
                            seaCoords.add(((x,y)))
                if game.mouse.get_pressed()[0] and gameloops > 3:
                    if inHand in [mountain,tree,vol1]:
                        if ((x,y)) in snowCoords|grassCoords|desertCoords:
                            if ((x,y)) not in volcanoCoords|mountainCoords|treeCoords:
                                if inHand == mountain:
                                    mountainCoords.add((x,y))
                                if inHand == tree:
                                    treeCoords.add((x,y))
                                if inHand == vol1:
                                     volcanoCoords.add((x,y))


                    if inHand in [snow,grass,sand] and ((x,y)) not in seaCoords:
                        for pack in [snowCoords,grassCoords,desertCoords,volcanoCoords,mountainCoords,treeCoords]:
                            if ((x,y)) in pack:
                                pack.remove(((x,y)))

                    if inHand == snow:
                        snowCoords.add((x,y))
                    if inHand == grass:
                        grassCoords.add((x,y))
                    if inHand == sand:
                        desertCoords.add((x,y))

                    posSpawnCoords = grassCoords|snowCoords|desertCoords
                    seaCoords -= grassCoords|snowCoords|desertCoords
                    landCoords = grassCoords|snowCoords|desertCoords
                    posCoastCoords = set()
                    for i in posSpawnCoords:
                        if ((i[0]-16,i[1])) in seaCoords or ((i[0]+16,i[1])) in seaCoords or ((i[0],i[1]-16)) in seaCoords or ((i[0],i[1]+16)) in seaCoords:
                            posCoastCoords.add(i)
            if event.type == game.MOUSEBUTTONDOWN and event.button == LEFT:
                if biggrass.get_rect(top=672,left=16).collidepoint(game.mouse.get_pos()):inHand = grass
                if biggrass.get_rect(top=672,left=96).collidepoint(game.mouse.get_pos()):inHand = sand
                if biggrass.get_rect(top=672,left=176).collidepoint(game.mouse.get_pos()):inHand = snow
                if biggrass.get_rect(top=672,left=256).collidepoint(game.mouse.get_pos()):inHand = mountain
                if biggrass.get_rect(top=672,left=336).collidepoint(game.mouse.get_pos()):inHand = tree
                if biggrass.get_rect(top=672,left=416).collidepoint(game.mouse.get_pos()):inHand = vol1
                ###SAVING WORLD
                if button.get_rect(top=(640),left=(640)).collidepoint(event.pos):

                    #try:
                    bigpack=list()
                    posSpawnCoords = grassCoords|snowCoords|desertCoords
                    for i in range(random.randint(3,7)):
                        datapack,posSpawnCoords = societygen.spawning(posSpawnCoords,colorcodes,names)
                        bigpack.append(datapack)
                    ### FIRST EXPANSION
                    for i in range(10):
                        for itemnum in range(len(bigpack)):
                            if random.randint(1,2) == 1:
                                bigpack[itemnum],posSpawnCoords = societygen.expand(bigpack[itemnum],posSpawnCoords,seaCoords)
                                for item in bigpack:
                                    for tile in item[0]:
                                        if tile in posSpawnCoords:
                                            posSpawnCoords.remove(tile)

                    fertilityIndex = society.soilfertility(mountainCoords,snowCoords,grassCoords,desertCoords,treeCoords)
                    volcanoCoordsCopy=list()
                    for i in volcanoCoords:
                        volcanoCoordsCopy.append([i])
                    Naturedata = [landCoords,seaCoords,allCoords,
                    mountainCoords,snowCoords,grassCoords,desertCoords,
                    treeCoords,posCoastCoords,posSpawnCoords,mountainOffset,
                    treeOffset,volcanoCoordsCopy,beachtype]

                    #except:continue


                    path, dirs, files = next(os.walk(os.getcwd()+"/Saves/World1"))
                    files = other.deletenonpickle(files)
                    for thing in range(len(files)):
                        try:
                            os.remove(os.getcwd()+"/Saves/World1/data"+str(thing)+".pickle")
                        except:
                            pass

                    with open("Saves/World1/data0.pickle","wb") as file:
                        pickle.dump([bigpack,fertilityIndex,Naturedata], file)





                    titleGameState = True
                    worldCreateState = False
                    win.blit(titleimg,(0,0))
            if False:#not validMouseSpace and game.mouse.get_pressed()[2]:
                bigpack=list()
                posSpawnCoords = grassCoords|snowCoords|desertCoords
                for i in range(random.randint(3,7)):
                    datapack,posSpawnCoords = societygen.spawning(posSpawnCoords,colorcodes,names)
                    bigpack.append(datapack)
                ### FIRST EXPANSION
                for i in range(10):
                    for itemnum in range(len(bigpack)):
                        if random.randint(1,2) == 1:
                            bigpack[itemnum],posSpawnCoords = societygen.expand(bigpack[itemnum],posSpawnCoords,seaCoords)
                            for item in bigpack:
                                for tile in item[0]:
                                    if tile in posSpawnCoords:
                                        posSpawnCoords.remove(tile)
            if event.type == game.QUIT:
                endGame = True
                worldCreateState = False

        for tile in seaCoords:win.blit(game.transform.rotate(water,rotations[tile]),(tile))
        for tile in snowCoords:win.blit(game.transform.rotate(snow,rotations[tile]),(tile))
        gen.fancytiles(snowCoords,beachtype)

        for tile in desertCoords:win.blit(game.transform.rotate(sand,rotations[tile]),(tile))

        for tile in grassCoords:win.blit(game.transform.rotate(grass,rotations[tile]),(tile))
        gen.fancytiles(grassCoords,beachtype)

        for tile in mountainCoords:win.blit(mountain,((tile[0]+mountainOffset[tile]),(tile[1])))
        for tile in treeCoords:win.blit(tree,((tile[0]+treeOffset[tile]),(tile[1])))
        for tile in volcanoCoords:win.blit(game.transform.rotate(vol1,360),(tile))
        #if volcanoCoords:
        #    volcanoCoords = nature.volcanostuff(volcanoCoords)


        try:
            society.displaytribes(1000,posSpawnCoords,bigpack)
        except:
            pass


        creationicons = {biggrass:(16,672),bigsand:(96,672),bigsnow:(176,672),bigmountain:(256,672),bigtree:(336,672),bigvolcano:(416,672)}
        for icon in creationicons:
            win.blit(icon,creationicons[icon])
            win.blit(bigmouse,creationicons[icon])
        other.displayyr()
        other.mousemovement(inHand)
        game.display.flip()
        gameloops+=1
    if isdoingworldreset == True:
        isdoingworldreset = False
        worldGameState = True
    for item in range(maxyear):
        try:os.remove(  os.getcwd()+"/DataFiles/"+ "data"+str(maxyear-item)+".pickle")
        except:pass
    try:os.remove(  os.getcwd()+"/DataFiles/"+ "data0.pickle")
    except:pass
    if endGame == True:break

game.quit()
game.quit()
game.quit()
### UNFINISHED WAVE ADDITION
'''    for pos in waveCoords:
    print(pos[0])
    win.blit(wave,(pos[0]))

    waveCoords[waveCoords.index(pos)][0] = ((pos[0][0]+pos[1],pos[0][1]))
    for number in range(1,16):
        if ((waveCoords[waveCoords.index(pos)][0][0]+number,waveCoords[waveCoords.index(pos)][0][1])) in landCoords:
            waveCoords.remove(pos)

if random.randint(1,40) == 1:
    waveCoords.append(  [ (-16,(random.randint(1,16)*40)),random.randint(2,5)   ]   )'''
