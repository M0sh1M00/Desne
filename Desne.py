import pygame as game
import random
import time
import News

year = 0
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
game.mixer.music.load('background.mp3')
game.mixer.music.play(-1)
Newmus = game.mixer.Sound('New.wav')
Tribemus = game.mixer.Sound('Tribe.wav')
Iconmus = game.mixer.Sound('Icon.wav')

screenWidth = 640+320-128
screenHeight = 640+320-128
win = game.display.set_mode((screenWidth, screenHeight))
game.display.set_caption("Desne")
water = game.image.load("water.png")
mountain = game.image.load("mountain.png")
grass = game.image.load("grass.png")
snow = game.image.load("snow.png")
sand = game.image.load("desert.png")
mouse = game.image.load("mouse.png")
bar = game.image.load("bar.png")
titleimg = game.image.load("titleimg.png")
button = game.image.load("button.png")
politicalicon = game.image.load("politicalicon1.png")
treeicon = game.image.load("treeicon1.png")
bothicon = game.image.load("bothicon1.png")
politicalicon2 = game.image.load("politicalicon2.png")
treeicon2 = game.image.load("treeicon2.png")
bothicon2 = game.image.load("bothicon2.png")
earth1 = game.image.load("earth1.png")
earth2 = game.image.load("earth2.png")
mail1 = game.image.load("mail1.png")
mail2 = game.image.load("mail2.png")
quest1 = game.image.load("quest1.png")
quest2 = game.image.load("quest2.png")

arrow1 = game.image.load("arrow1.png")
arrow2 = game.image.load("arrow2.png")

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


    def mountain(landCoords,seaCoords,allCoords,mountainCoords):
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
    def snowgen(landCoords):
        snowCoords = set()
        nom = random.randint(5,6)*16#7 10
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
    def sandgen(landCoords,desertCoords):
        coord = random.sample(landCoords, 1)
        x = (coord[0])[0]
        y = (coord[0])[1]
        possiblesizesx = random.randint(5,12)
        possiblesizesy = random.randint(1,2)
        tries = 0
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

        for i in range(3000):
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
        mountainCoords = set()
        desertCoords = set()


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
        for i in range(4):
            landCoords,seaCoords,allCoords,mountainCoords = gen.mountain(landCoords,seaCoords,allCoords,mountainCoords)
        snowCoords = gen.snowgen(landCoords)
        for i in range(2):
            desertCoords = gen.sandgen(landCoords,desertCoords)

        grassCoords = landCoords-seaCoords-snowCoords-desertCoords
        tempCoords = set()
        for tile in grassCoords:
            if ((tile[0]+16,tile[1])) in desertCoords and ((tile[0]-16,tile[1])) in desertCoords and ((tile[0],tile[1]+16)) in desertCoords and ((tile[0],tile[1]-16)) in desertCoords:
                tempCoords.add(tile)
                desertCoords.add(tile)
        for i in tempCoords:
            grassCoords.remove(i)

        posSpawnCoords = landCoords
        posCoastCoords = set()
        for i in posSpawnCoords:
            if ((i[0]-16,i[1])) in seaCoords or ((i[0]+16,i[1])) in seaCoords or ((i[0],i[1]-16)) in seaCoords or ((i[0],i[1]+16)) in seaCoords:
                posCoastCoords.add(i)

        return landCoords,seaCoords,allCoords,mountainCoords,snowCoords,grassCoords,desertCoords,posCoastCoords,posSpawnCoords

class societygen():

    def spawning(posSpawnCoords,colorcodes):
        spawntile = (random.sample((landCoords), 1))
        if spawntile[0] not in posSpawnCoords:
            spawntile[0] = (random.sample((landCoords), 1))
        posSpawnCoords.remove(spawntile[0])
        color = (random.choice(colorcodes))#150
        colorcodes.remove(color)
        char = open("SocietyCharacteristics.txt","r")
        charlist1 = list()
        for line in char:
            #charlist1.append(line.rstrip("\n"))
            charlist1.append(line)
        char.close()
        charlist1.remove(charlist1[-1])

        char = open("SocietyCharacteristicsOp.txt","r")
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
        f = open("SocietyNames.txt","r")
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

        governmenttype = "Chieftan"

        currency = 0

        military = 10 #K

        citzensatisfaction = 75 #percent

        datapack = [spawntile,color,societycharacteristics,name,governmenttype,currency,military,citzensatisfaction]
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
                if mynum == 1:
                    xplus = -16
                elif mynum == 2:
                    xplus = 16
                elif mynum == 3:
                    yplus = -16
                elif mynum == 4:
                    yplus = 16
                if mynum <= 4:
                    if ((curTile[0]+xplus), curTile[1]+yplus) in posSpawnCoords:

                        curTile = ((curTile[0]+xplus,curTile[1]+yplus))

                        ###
                        allTiles.append(curTile)
                        newdatapack = [allTiles,datapack[1],datapack[2],datapack[3],datapack[4],datapack[5],datapack[6],datapack[7]]
                        return newdatapack, posSpawnCoords
                    else:
                        mynums.remove(mynum)

                elif mynum == 5:
                    if ((curTile[0]-16), curTile[1]) in seaCoords and ((curTile[0]), curTile[1]-16) in seaCoords and ((curTile[0]-16), curTile[1]-16) in posSpawnCoords:
                        curTile = ((curTile[0]-16,curTile[1]-16))
                        allTiles.append(curTile)
                        newdatapack = [allTiles,datapack[1],datapack[2],datapack[3],datapack[4],datapack[5],datapack[6],datapack[7]]
                    #    posSpawnCoords.add(curTile)
                        return newdatapack, posSpawnCoords
                    else:
                        mynums.remove(mynum)
                elif mynum == 6:
                    if ((curTile[0]-16), curTile[1]) in seaCoords and ((curTile[0]), curTile[1]+16) in seaCoords and ((curTile[0]-16), curTile[1]+16) in posSpawnCoords:
                        curTile = ((curTile[0]-16,curTile[1]+16))
                        allTiles.append(curTile)
                        newdatapack = [allTiles,datapack[1],datapack[2],datapack[3],datapack[4],datapack[5],datapack[6],datapack[7]]
                    #    posSpawnCoords.add(curTile)
                        return newdatapack, posSpawnCoords
                    else:
                        mynums.remove(mynum)
                elif mynum == 7:
                    if ((curTile[0]+16), curTile[1]) in seaCoords and ((curTile[0]), curTile[1]-16) in seaCoords and ((curTile[0]+16), curTile[1]-16) in posSpawnCoords:
                        curTile = ((curTile[0]+16,curTile[1]-16))
                        allTiles.append(curTile)
                        newdatapack = [allTiles,datapack[1],datapack[2],datapack[3],datapack[4],datapack[5],datapack[6],datapack[7]]
                    #    posSpawnCoords.add(curTile)
                        return newdatapack, posSpawnCoords
                    else:
                        mynums.remove(mynum)
                elif mynum == 8:
                    if ((curTile[0]+16), curTile[1]) in seaCoords and ((curTile[0]), curTile[1]+16) in seaCoords and ((curTile[0]+16), curTile[1]+16) in posSpawnCoords:
                        curTile = ((curTile[0]+16,curTile[1]+16))
                        allTiles.append(curTile)
                        newdatapack = [allTiles,datapack[1],datapack[2],datapack[3],datapack[4],datapack[5],datapack[6],datapack[7]]
                    #    posSpawnCoords.add(curTile)
                        return newdatapack, posSpawnCoords
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
                    allTiles.append(curTile)
                    datapack = [allTiles,datapack[1],datapack[2],datapack[3],datapack[4],datapack[5],datapack[6],datapack[7]]
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
    def icons():
        win.blit(treeicon,(672,576))
        win.blit(bothicon,(720,576))
        win.blit(politicalicon,(768,576))

        win.blit(earth1,(672,576-128))
        win.blit(quest1,(720,576-128))
        win.blit(mail1,(768,576-128))
        #print(arrow2.get_rect(top=576,left=768))

        if earth1.get_rect(top=576,left=672).collidepoint(game.mouse.get_pos()):
            win.blit(treeicon2,(672,576))
        if earth1.get_rect(top=576,left=720).collidepoint(game.mouse.get_pos()):
            win.blit(bothicon2,(720,576))
        if earth1.get_rect(top=576,left=768).collidepoint(game.mouse.get_pos()):
            win.blit(politicalicon2,(768,576))


        win.blit(arrow1,(688,512))
        if arrow1.get_rect(top=512,left=688).collidepoint(game.mouse.get_pos()):
            win.blit(arrow2,(688,512))

        if earth1.get_rect(top=576-128,left=672).collidepoint(game.mouse.get_pos()):
            win.blit(earth2,(672,576-128))
        if earth1.get_rect(top=576-128,left=720).collidepoint(game.mouse.get_pos()):
            win.blit(quest2,(720,576-128))
        if earth1.get_rect(top=576-128,left=768).collidepoint(game.mouse.get_pos()):
            win.blit(mail2,(768,576-128))

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

landCoords,seaCoords,allCoords,mountainCoords,snowCoords,grassCoords,desertCoords,posCoastCoords,posSpawnCoords = gen.finalgen()

myalpha = 180

colorcodes = [(0,255,255),(255,0,255),(0,255,0),(255,182,34),(253,179,241),(205,255,0),(161,114,255)]

bigpack = list()
for i in range(random.randint(3,7)):

    datapack,posSpawnCoords,colorcodes = societygen.spawning(posSpawnCoords,colorcodes)
    bigpack.append(datapack)

for i in range(10):
    for itemnum in range(len(bigpack)):
        if random.randint(1,2) == 1:
            bigpack[itemnum],posSpawnCoords = societygen.expand(bigpack[itemnum],posSpawnCoords,seaCoords)
            for item in bigpack:
                for tile in item[0]:
                    if tile in posSpawnCoords:
                        posSpawnCoords.remove(tile)
allbigpacks = list()
civselected = -1
worldGameState = False
titleGameState = True

###FONTS
treb50 = game.font.SysFont("Trebuchet MS",100)
treb20 = game.font.SysFont("Trebuchet MS",17)


while True:

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
        sidebar.icons()
            ### ORDER SHOULD BE OCEAN GRASS DESERT SNOW MOUNTAIN
            ### GEN
        for tile in seaCoords:
            win.blit(water,(tile))
        for tile in mountainCoords:
            win.blit(mountain,(tile))
        for tile in snowCoords:
            win.blit(snow,(tile))
        for tile in grassCoords:
           win.blit(grass,(tile))
        for tile in desertCoords:
           win.blit(sand,(tile))
        for tile in mountainCoords:
            win.blit(mountain,(tile))
        win.blit(button,(640,640,640+192,640+192))




    ### IF CLICKED ON TRIBE
        for item in bigpack:
            thicc = 4
            territory = game.Surface((16,16))
            territory.fill((item[1]))
            territoryA = game.Surface((thicc,16))
            territoryA.fill((item[1]))
            territoryB = game.Surface((16,thicc))
            territoryB.fill((item[1]))
            territoryC = game.Surface((thicc,thicc))
            territoryC.fill((item[1]))
            territory.set_alpha(myalpha)

            for tile in item[0]:
                if tile in posSpawnCoords:
                    posSpawnCoords.remove(tile)
                if myalpha == 180:
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

                else:
                    win.blit(territory, ((tile)))
                if territory.get_rect(top=(tile[1]),left=(tile[0])).collidepoint(game.mouse.get_pos()):
                    for event in game.event.get():
                        if event.type == game.MOUSEBUTTONDOWN:
                            Tribemus.play()
                            #print(item[1])
                            civselected = bigpack.index(item)



        if civselected != -1:
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
            gov = helve2.render(bigpack[civselected][4], True, (bigpack[civselected][1]))
            win.blit(tribename,(640+16,16))
            win.blit(char1N,(640+16,64+32))
            win.blit(char2N,(640+16,64+48+32))
            win.blit(char3N,(640+16,128+32+32))
            win.blit(gov,(640+16,128+32+32+48))

        keys = game.key.get_pressed()

        for event in game.event.get():
            if event.type == game.MOUSEBUTTONDOWN:
                ### ICON BUTTON
                if treeicon.get_rect(top=576,left=672).collidepoint(game.mouse.get_pos()):
                    myalpha = 0
                    Iconmus.play()
                elif bothicon.get_rect(top=576,left=720).collidepoint(game.mouse.get_pos()):
                    myalpha = 180
                    Iconmus.play()
                elif politicalicon.get_rect(top=576,left=768).collidepoint(game.mouse.get_pos()):
                    myalpha = 1000
                    Iconmus.play()
                elif quest1.get_rect(top=576-128,left=720).collidepoint(game.mouse.get_pos()):
                    Iconmus.play()
                ### REFRESH BUTTON
                if button.get_rect(top=(640),left=(640)).collidepoint(event.pos):
                    colorcodes = [(0,255,255),(255,0,255),(0,255,0),(255,182,34),(253,179,241),(205,255,0),(161,114,255)]
                    Newmus.play()

                    year=0
                    landCoords,seaCoords,allCoords,mountainCoords,snowCoords,grassCoords,desertCoords,posCoastCoords,posSpawnCoords = gen.finalgen()
                    bigpack = list()
                    for i in range(random.randint(3,7)):
                        datapack,posSpawnCoords,colorcodes = societygen.spawning(posSpawnCoords,colorcodes)
                        bigpack.append(datapack)
                    for i in range(10):
                        for itemnum in range(len(bigpack)):
                            if random.randint(1,2) == 1:
                                bigpack[itemnum],posSpawnCoords = societygen.expand(bigpack[itemnum],posSpawnCoords,seaCoords)
                                for item in bigpack:
                                    for tile in item[0]:
                                        if tile in posSpawnCoords:
                                            posSpawnCoords.remove(tile)
                    civselected = -1

                ### NEXT TURN BUTTON
                if arrow1.get_rect(top=512,left=688).collidepoint(game.mouse.get_pos()):

                 #for i in range(10):
                    year+=1
                    Iconmus.play()

                    for itemnum in range(len(bigpack)):

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
                            possibleTurns=other.turnsB(30,1,"colonize",bigpack,itemnum,possibleTurns)

                        possibleTurns=other.turnsS(10,20,"nothing",bigpack,itemnum,possibleTurns)

                        possibleTurns=other.turnsB(10,400,"nothing",bigpack,itemnum,possibleTurns)

                        possibleTurns=other.turnsS(15,800,"expand",bigpack,itemnum,possibleTurns)

                        possibleTurns=other.turnsB(15,600,"expand",bigpack,itemnum,possibleTurns)

                        turnchoice = random.choice(possibleTurns)
                        if turnchoice == "expand":
                            for num in range(random.randint(1,10)):
                                if posSpawnCoords:
                                    bigpack[itemnum],posSpawnCoords = societygen.expand(bigpack[itemnum],posSpawnCoords,seaCoords)
                            newsstuff.append("expand")
                        elif turnchoice == "nothing":
                            newsstuff.append("nothing")
                            pass
                        elif turnchoice == "colonize":
                            newsstuff.append("colonize")
                            if posCoastCoords:
                                bigpack[itemnum],posCoastCoords = societygen.colonize(bigpack[itemnum],posCoastCoords,seaCoords)
                        elif turnchoice == "consolidate":
                            newsstuff.append("consolidation")

                        for item in bigpack:
                            for tile in item[0]:
                                if tile in posSpawnCoords:
                                    posSpawnCoords.remove(tile)
                                if tile in posCoastCoords:
                                    posCoastCoords.remove(tile)

                        ### SECONDARY
                        if random.randint(1,5) == 1:

                            if (bigpack[itemnum])[4] == "Chieftan" and len((bigpack[itemnum])[0]) > 20:
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

                    #    datapack = [spawntile,color,societycharacteristics,name,governmenttype,currency,military,citzensatisfaction]

                    allbigpacks.append(bigpack)



            if event.type == game.QUIT:
                endGame = True
                worldGameState = False
        other.mousemovement()
        game.display.flip()


    if endGame == True:
        break
game.quit()
