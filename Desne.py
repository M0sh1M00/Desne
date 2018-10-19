import contextlib
import os
with contextlib.redirect_stdout(None):
    import pygame as game
import random
import News
import pickle
global year,minsize,maxsize,minrectgen,maxrectgen,chanceremove,chanceamount,popdiviser
popdiviser = 0
year = 0
maxyear = 0
minsize = 8
maxsize = 14
minrectgen = 6
maxrectgen = 6
chanceremove = 200
chanceamount = 200
game.init()
game.mixer.init()
game.init()
game.font.init()
game.mixer.music.load('Audio/background.mp3')
game.mixer.music.play(-1)
Newmus = game.mixer.Sound('Audio/New.wav')
Tribemus = game.mixer.Sound('Audio/Tribe.wav')
Iconmus = game.mixer.Sound('Audio/Icon.wav')

screenWidth = 640+320-128
screenHeight = 640+320-128
win = game.display.set_mode((screenWidth, screenHeight))
game.display.set_caption("Desne")

water = game.image.load("Terrain/water.png")
mountain = game.image.load("Terrain/mountain.png")
grass = game.image.load("Terrain/grass.png")
snow = game.image.load("Terrain/snow.png")
sand = game.image.load("Terrain/desert.png")
tree = game.image.load("Terrain/tree.png")

mouse = game.image.load("Other/mouse.png")
test = game.image.load("Other/test.png")

bar = game.image.load("Bar/bar.png")
titleimg = game.image.load("Bar/titleimg.png")
button = game.image.load("Bar/button.png")
politicalicon = game.image.load("Bar/politicalicon1.png")
treeicon = game.image.load("Bar/treeicon1.png")
bothicon = game.image.load("Bar/bothicon1.png")
politicalicon2 = game.image.load("Bar/politicalicon2.png")
treeicon2 = game.image.load("Bar/treeicon2.png")
bothicon2 = game.image.load("Bar/bothicon2.png")
earth1 = game.image.load("Bar/earth1.png")
earth2 = game.image.load("Bar/earth2.png")
mail1 = game.image.load("Bar/mail1.png")
mail2 = game.image.load("Bar/mail2.png")
quest1 = game.image.load("Bar/quest1.png")
quest2 = game.image.load("Bar/quest2.png")

arrow1 = game.image.load("Bar/arrow1.png")
arrow2 = game.image.load("Bar/arrow2.png")


###Numbers
num11 = game.image.load("Bar/num11.png")
num12 = game.image.load("Bar/num12.png")
num101 = game.image.load("Bar/num101.png")
num102 = game.image.load("Bar/num102.png")
num51 = game.image.load("Bar/num51.png")
num52 = game.image.load("Bar/num52.png")



class gen():

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

            if random.randint(1,2) == 1:
                possiblesizesx = random.randint(2,3)
                possiblesizesy = random.randint(5,7)
            else:
                possiblesizesy = random.randint(2,3)
                possiblesizesx = random.randint(5,7)

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
            amount = random.randint(20,40)
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

        for tile in mountainCoords:
            mountainOffset[tile] = random.randint(0,4)
        for tile in treeCoords:
            treeOffset[tile] = random.randint(0,8)

        posSpawnCoords = set((list(landCoords))[:])
        posCoastCoords = set()
        for i in posSpawnCoords:
            if ((i[0]-16,i[1])) in seaCoords or ((i[0]+16,i[1])) in seaCoords or ((i[0],i[1]-16)) in seaCoords or ((i[0],i[1]+16)) in seaCoords:
                posCoastCoords.add(i)

        return landCoords,seaCoords,allCoords,mountainCoords,snowCoords,grassCoords,desertCoords,treeCoords,posCoastCoords,posSpawnCoords,mountainOffset,treeOffset
class societygen():
    def spawning(posSpawnCoords,colorcodes):
        spawntile = random.choice(list(posSpawnCoords))

        while spawntile not in posSpawnCoords:
            spawntile = random.choice(list(posSpawnCoords))
        if year == 0:
            posSpawnCoords.remove(spawntile)
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
        f = open("TextFiles/SocietyNames.txt","r")
        names = list()
        for line in f:
            names.append(line.rstrip("\n"))
        names.remove(names[-1])
        part1 = random.choice(names)
        names.remove(part1)
        part2 = random.choice(names)
        name = part1+part2
        f.close()
        name = name[0].upper()+name[1:]
        if year == 0:
            governmenttype = "Chieftan"
        else:
            governmenttype = "Provisional"
        pop = 0
        #pop = society.populationcalc([spawntile],fertilityIndex)
        #print(pop)
        military = 10 #K

        citzensatisfaction = random.randint(60,90) #percent

        datapack = [[spawntile],color,societycharacteristics,name,governmenttype,pop,military,citzensatisfaction,spawntile]
        return datapack,posSpawnCoords,colorcodes
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
    def icons(turnamount,myalpha):

        politicalicon2,treeicon2,bothicon2,num11,num51,num101
        values = [

        [myalpha,0,432,672,treeicon,treeicon2],
        [myalpha,180,432,720,politicalicon,politicalicon2],
        [myalpha,1000,432,768,bothicon,bothicon2],

        [turnamount,1,480,672,num11,num12],
        [turnamount,5,480,720,num51,num52],
        [turnamount,10,480,768,num101,num102],

        ]
        for itemnum in range(len(values)):

            if values[itemnum][0]!=values[itemnum][1]:

                if earth1.get_rect(top=values[itemnum][3],left=values[itemnum][2]).collidepoint(game.mouse.get_pos()):
                    win.blit(values[itemnum][5],(values[itemnum][2],values[itemnum][3]))
                else:
                    win.blit(values[itemnum][4],(values[itemnum][2],values[itemnum][3]))
            else:
                win.blit(values[itemnum][5],(values[itemnum][2],values[itemnum][3]))

        win.blit(arrow1,(528,672))
        if arrow1.get_rect(top=672,left=528).collidepoint(game.mouse.get_pos()):
            win.blit(arrow2,(528,672))
        win.blit(arrow1,(528,752))
        if arrow1.get_rect(top=752,left=528).collidepoint(game.mouse.get_pos()):
            win.blit(arrow2,(528,752))
class society():
    def soilfertility(mountainCoords,snowCoords,grassCoords,desertCoords,treeCoords):
        fertilityIndex = {}
        for tile in allCoords:
            if tile in snowCoords: fertilityIndex[tile] = [random.randint(1,1000),random.randint(3000,5000),1.005]
            if tile in grassCoords: fertilityIndex[tile] = [random.randint(10000,15000),random.randint(50000,100000),1.005]
            if tile in desertCoords: fertilityIndex[tile] = [random.randint(1,2000),random.randint(3000,10000),1.005]
            if tile in treeCoords: fertilityIndex[tile] = [random.randint(8000,14000),random.randint(16000,40000),1.005]
            if tile in mountainCoords: fertilityIndex[tile] = [random.randint(500,1500),random.randint(2000,3000),1.005]
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
class other():
    def mousemovement():
        x = (game.mouse.get_pos())[0]
        y = (game.mouse.get_pos())[1]
        i = 0
        mynums = list()
        while i != 640:
            mynums.append(i)
            i+=16
        if (game.mouse.get_pos())[0] < 640 and (game.mouse.get_pos())[1] < 640:
            game.mouse.set_visible(False)
            treb = game.font.SysFont("Trebuchet MS",15)
            xy = treb.render(("X: "+ str(int(x/16)+1) + "  Y: "+ str(int(y/16)+1))   , True, (0, 0, 0))
            win.blit(xy,((0,640-16)))
            while x not in mynums:
                x-=1

            while y not in mynums:
                y-=1
            win.blit(mouse,((x,y)))
        else:
            treb = game.font.SysFont("Trebuchet MS",15)
            xy = treb.render(( "X:      Y: ")   , True, (0, 0, 0))
            win.blit(xy,((0,640-16)))
            game.mouse.set_visible(True)
    def findarea(Coords):
        ranTile = random.choice(list(Coords))
        area = {(ranTile)}
        temp = set()
        for i in range(  len(Coords)  ):
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
                        temp.add(((tile[0]+xplus,tile[1]+yplus)))

            for tile in temp:
                area.add(tile)
        return area
    def displayyr():
        treb = game.font.SysFont("Trebuchet MS",15)
        yeardisplay = treb.render(( "Year: "+str(year))   , True, (0, 0, 0))
        win.blit(yeardisplay,((640-64-16,640-16)))
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

worldGameState = False
titleGameState = True

###FONTS
treb50 = game.font.SysFont("Trebuchet MS",100)
treb20 = game.font.SysFont("Trebuchet MS",17)
gamereset = True
endGame = False
turnamount = 1
myalpha = 180
while True:
    if gamereset == True:






        landCoords,seaCoords,allCoords,mountainCoords,snowCoords,grassCoords,desertCoords,treeCoords,posCoastCoords,posSpawnCoords,mountainOffset,treeOffset = gen.finalgen()
        ### NEED THESE VARS
        fertilityIndex = society.soilfertility(mountainCoords,snowCoords,grassCoords,desertCoords,treeCoords)


        year = 0
        maxyear = 0
        colorcodes = [(0,255,255),(255,0,255),(0,255,0),(255,182,34),(253,179,241),(205,255,0),(161,114,255),(173,255,47),(144,238,144), (64,224,208),(127,255,212),(216,191,216),(95,158,160)]
        civselected = -1
        area = set()
        ### SOCIETYGEN
        bigpack = list()
        for i in range(random.randint(3,7)):
            datapack,posSpawnCoords,colorcodes = societygen.spawning(posSpawnCoords,colorcodes)
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


        with open("DataFiles/data"+str(year)+".pickle","wb") as file:
            pickle.dump([bigpack,fertilityIndex], file)


        worldGameState = True
        gamereset = False

    #while titleGameState == True:
    while titleGameState == True:
        win.blit(titleimg,((0,0)))
        tit = treb50.render("DESNE", True, (200, 200, 200))
        Para1 = treb20.render("Welcome to Desne, a game in which you can watch empires, communes and", True, (200, 200, 200))
        Para2 = treb20.render("confederations rise and fall, watching their population, leaders and currency.", True, (200, 200, 200))
        Para3 = treb20.render("Every time you click                      a turn will pass, allowing for each civ a", True, (200, 200, 200))
        Para4 = treb20.render("chance to: expand, colonise, mine for minerals, revolt and much much more.", True, (200, 200, 200))
        Para5 = treb20.render("These three buttons will allow you to toggle the viewability of the environment.", True, (200, 200, 200))
        #Para6 = treb20.render("Click this button to see a civilisations top new stories!", True, (200, 200, 200))
        Para7 = treb20.render("Finally the red button will display the map, click it to get started.", True, (200, 200, 200))
        win.blit(tit,(tit.get_rect(center=(320+16, 64))))
        win.blit(Para1,(Para1.get_rect(left=(32),top=(128))))
        win.blit(Para2,(Para1.get_rect(left=(32),top=(128+20))))
        win.blit(arrow1,(128+64,128+56))
        win.blit(Para3,(Para1.get_rect(left=(32),top=(128+80))))
        win.blit(Para4,(Para1.get_rect(left=(32),top=(128+100))))
        win.blit(Para5,(Para1.get_rect(left=(32),top=(128+100+60))))
        win.blit(treeicon,(64,256+64))
        win.blit(bothicon,(64+48,256+64))
        win.blit(politicalicon,(64+48+48,256+64))
        win.blit(Para7,(Para1.get_rect(left=(32),top=(128+100+60+60+20))))

        sidebar.right()
        sidebar.bottom()

        win.blit(button,(640,640,640+192,640+192))




        for event in game.event.get():
            if event.type == game.MOUSEBUTTONDOWN:
                    if button.get_rect(top=(640),left=(640)).collidepoint(event.pos):
                        Newmus.play()
                        worldGameState = True
                        titleGameState = False
            if event.type == game.QUIT:
                endGame = True
                titleGameState = False

        game.display.flip()


    while worldGameState == True:

        ### TURN LOOP

        sidebar.right()
        sidebar.bottom()
        sidebar.icons(turnamount,myalpha)
            ### ORDER SHOULD BE OCEAN GRASS DESERT SNOW MOUNTAIN
            ### GEN
        for tile in seaCoords:
            win.blit(water,(tile))
        for tile in snowCoords:
            win.blit(snow,(tile))
        for tile in grassCoords:
           win.blit(grass,(tile))
        for tile in desertCoords:
           win.blit(sand,(tile))
        for tile in mountainCoords:
            win.blit(mountain,((tile[0]+mountainOffset[tile]),(tile[1])))
        for tile in treeCoords:
            win.blit(tree,((tile[0]+treeOffset[tile]),(tile[1])))
#        for tile in area:
#            win.blit(test,(tile))
    #    for tile in range(len(bigpack)):
    #        win.blit(test,(bigpack[tile][8]))

        win.blit(button,(640,640,640+192,640+192))
        for itemnum in range(len(bigpack)):
            bigpack[itemnum][5] = society.populationcalc(bigpack[itemnum][0],fertilityIndex)

    ### IF CLICKED ON TRIBE
        for item in bigpack:
            thicc = 1
            if myalpha == 180:
                thicc = 4
            territory = game.Surface((16,16))
            territory.fill((item[1]))
            territoryA = game.Surface((thicc,16))
            territoryB = game.Surface((16,thicc))
            territoryC = game.Surface((thicc,thicc))

            territory.set_alpha(myalpha)
            if myalpha == 180:
                territoryA.fill((item[1]))
                territoryB.fill((item[1]))
                territoryC.fill((item[1]))


            for tile in item[0]:


                if tile in posSpawnCoords:
                    posSpawnCoords.remove(tile)


                if myalpha != 180:
                    win.blit(territory, ((tile)))

                if myalpha == 180 or myalpha == 1000:
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

                if territory.get_rect(top=(tile[1]),left=(tile[0])).collidepoint(game.mouse.get_pos()):
                    for event in game.event.get():
                        if event.type == game.MOUSEBUTTONDOWN:
                            Tribemus.play()
                            #print(item[1])
                            civselected = bigpack.index(item)
            #    thicc = random.randint(1,6)
        if civselected != -1:
            try:
                helve = game.font.SysFont("Trebuchet MS",45)
                helve2 = game.font.SysFont("Trebuchet MS",18)
                tribename = helve.render(bigpack[civselected][3], True, (bigpack[civselected][1]))
                char1 = bigpack[civselected][2][0]
                char1 = char1.split(":")
                char1N = helve2.render(char1[0], True, (bigpack[civselected][1]))
                char2 = bigpack[civselected][2][1]
                char2 = char2.split(":")
                char2N = helve2.render(char2[0], True, (bigpack[civselected][1]))
                char3 = bigpack[civselected][2][2]
                char3 = char3.split(":")
                char3N = helve2.render(char3[0], True, (bigpack[civselected][1]))
                gov = helve2.render("Gov: "+bigpack[civselected][4], True, (bigpack[civselected][1]))
                population = helve2.render("Pop: "+str(bigpack[civselected][5]), True, (bigpack[civselected][1]))
                win.blit(tribename,(640+16,16))
                win.blit(char1N,(640+16,64+32))
                win.blit(char2N,(640+16,64+48+32))
                win.blit(char3N,(640+16,128+32+32))
                win.blit(gov,(640+16,240))
                win.blit(population,(640+16,288))
            except:
                pass
        keys = game.key.get_pressed()
        for event in game.event.get():
            if event.type == game.MOUSEBUTTONDOWN:
                ### ICON BUTTON
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


                ### REFRESH BUTTON
                elif button.get_rect(top=(640),left=(640)).collidepoint(event.pos):
                    Newmus.play()
                    gamereset = True
                    worldGameState = False

                ### NEXT TURN BUTTON
                elif arrow1.get_rect(top=752,left=528).collidepoint(game.mouse.get_pos()):
                    Iconmus.play()

                    if year == maxyear:
                        for i in range(turnamount):
                            year+=1
                            maxyear = year


                            for itemnum in range(len(bigpack)):


                                ###BASE POPULATION CHANGE

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

                                possibleTurns=other.turnsS(15,800,"expand",bigpack,itemnum,possibleTurns)

                                possibleTurns=other.turnsB(15,600,"expand",bigpack,itemnum,possibleTurns)

                                turnchoice = random.choice(possibleTurns)
                                if turnchoice == "expand":
                                    for num in range(random.randint(1,10)):
                                        if posSpawnCoords:
                                            bigpack[itemnum],posSpawnCoords = societygen.expand(bigpack[itemnum],posSpawnCoords,seaCoords)
                                    newsstuff.append("expand")
                                if turnchoice == "other":


                                    ### Smallchance events

                                    ### Rebelion
                                    if random.randint(1,25) == 1:
                                        area = other.findarea(bigpack[itemnum][0])
                                        if bigpack[itemnum][8] not in area:
                                            #if len(area) > 5:
                                            datapack,area,colorcodes = societygen.spawning(area,colorcodes)
                                            datapack[0] = list(area)
                                            datapack[8] = random.choice(list(area))
                                            bigpack[itemnum][0] = set(bigpack[itemnum][0])
                                            bigpack[itemnum][0] -= area
                                            bigpack[itemnum][0] = list(bigpack[itemnum][0])
                                            bigpack.append(datapack)


                                    else:
                                        newsstuff.append("nothing")
                                if turnchoice == "colonize":

                                    if posCoastCoords:
                                        newsstuff.append("colonize")
                                        bigpack[itemnum],posCoastCoords = societygen.colonize(bigpack[itemnum],posCoastCoords,seaCoords)
                                    else:
                                        turnchoice = "consolidate"
                                if turnchoice == "consolidate":
                                    newsstuff.append("consolidation")


                                for item in bigpack:
                                    for tile in item[0]:

                                        if tile in posSpawnCoords:
                                            posSpawnCoords.remove(tile)
                                        if tile in posCoastCoords:
                                            posCoastCoords.remove(tile)

                                ### SECONDARY
                                if random.randint(1,5) == 1:

                                    if ((bigpack[itemnum])[4] == "Chieftan" or (bigpack[itemnum])[4] == "Provisional")and len((bigpack[itemnum])[0]) > 20:
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

                                for object in newsstuff:
                                    newslist.append(News.news(bigpack[itemnum],object))

                                #print(newslist)

                            #    datapack = [spawntile,color,societycharacteristics,name,governmenttype,pop,military,citzensatisfaction]

                            ###WorldEvents
                            if random.randint(1,2) == 1:
                                pass
                                ###Plague
                                ###divide a random continents pop by random number


                            with open("DataFiles/data"+str(year)+".pickle","wb") as file:
                                pickle.dump([bigpack,fertilityIndex], file)
                    else:
                            for i in range(turnamount):
                                if year != maxyear:
                                    year += 1
                            with open("DataFiles/data"+str(year)+".pickle","rb") as pickle_in:
                                fulllist = (pickle.load(pickle_in))
                                bigpack = fulllist[0][:]
                                fertilityIndex = dict(fulllist[1])
                elif arrow1.get_rect(top=672,left=528).collidepoint(game.mouse.get_pos()):

                        for i in range(turnamount):
                            if year != 0:
                                year -=1

                        with open("DataFiles/data"+str(year)+".pickle","rb") as pickle_in:
                            fulllist = (pickle.load(pickle_in))
                            bigpack = fulllist[0][:]
                            fertilityIndex = dict(fulllist[1])




            if event.type == game.QUIT:
                endGame = True
                worldGameState = False


        other.mousemovement()
        other.displayyr()
        game.display.flip()
    for item in range(maxyear):
        os.remove(  os.getcwd()+"/DataFiles/"+ "data"+str(maxyear-item)+".pickle")
    os.remove(  os.getcwd()+"/DataFiles/"+ "data0.pickle")
    if endGame == True:
        break

game.quit()
