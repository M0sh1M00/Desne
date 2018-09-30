# imports
import pygame as game
import random, time, News

# game variables
year = 0
minsize = 8
maxsize = 14
minrectgen = 6
maxrectgen = 6
chanceremove = 200
chanceamount = 200
screenWidth = 640+320-128
screenHeight = 640+320-128

# initialise pygame
game.init()
game.mixer.init()
game.init()
game.font.init()
game.display.set_caption("Desne")
win = game.display.set_mode((screenWidth, screenHeight))

# initialise music
game.mixer.music.load('background.mp3')
game.mixer.music.play(-1)
Newmus = game.mixer.Sound('New.wav')
Tribemus = game.mixer.Sound('Tribe.wav')
Iconmus = game.mixer.Sound('Icon.wav')

# initialise images
water = game.image.load("water.png")
mountain = game.image.load("mountain.png")
grass = game.image.load("grass.png")
snow = game.image.load("snow.png")
sand = game.image.load("desert.png")
tree = game.image.load("tree.png")
mouse = game.image.load("mouse.png")
test = game.image.load("test.png")
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

# initialise numbers
num11 = game.image.load("num11.png")
num12 = game.image.load("num12.png")
num101 = game.image.load("num101.png")
num102 = game.image.load("num102.png")
num51 = game.image.load("num51.png")
num52 = game.image.load("num52.png")

# terrain gen class
class gen():
    # tile gen
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
        
    # island gen
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
                
            if test == True:
                if landmass.issubset(allCoords):
                    return landmass
                    
    # realism gen
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
        
    # mountain gen
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
            
    # snow gen
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
        
    # tree and sand gen
    def sandtreegen(desertCoords,landCoords,isDesert):
        if isDesert == True:
            amounts = [2000,1900,1800,1700,1600,1500,3000]
            amount = random.choice(amounts)
            possiblesizesx = random.randint(5,12)
            possiblesizesy = random.randint(1,2)
            
        else:
            amount = random.randint(30,50)
            possiblesizesx = random.randint(1,1)
            possiblesizesy = random.randint(1,1)
            
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
        
    # final gen compilation using above functions
    def finalgen():
        allCoords = set(gen.allTiles())
        landCoords = set()
        snowCoords = set()
        mountainCoords = set()
        desertCoords = set()
        treeCoords = set()
        mountainOffset = {}
        treeOffset = {}


        # generate land squares
        for i in range(random.randint(int(minrectgen),int(maxrectgen))):
            tempCoords = gen.island(allCoords)
            for Coord in tempCoords:
                landCoords.add(Coord)
                
        # generate sea coordinates
        seaCoords = allCoords - landCoords
        
        # generate coastline
        for i in range(int(chanceamount)):
            landCoords,seaCoords = gen.realism(seaCoords,landCoords)
            
        # generate mountains
        for i in range(random.randint(5,8)):
            landCoords,seaCoords,allCoords,mountainCoords = gen.mountain(mountainCoords,landCoords,seaCoords,allCoords)
        
        # generate snow
        snowCoords = gen.snowgen(snowCoords,landCoords)
        
        # generate desert
        if random.randint(1,5) != 5:
            for i in range(random.randint(1,2)):
                desertCoords = gen.sandtreegen(desertCoords,landCoords,True)
                
        grassCoords = landCoords-seaCoords-snowCoords-desertCoords
        for i in range(random.randint(5,9)):
            treeCoords = gen.sandtreegen(treeCoords,grassCoords,False) - mountainCoords
        
        # generate grass
        tempCoords = set()
        for tile in grassCoords:
            if ((tile[0]+16,tile[1])) in desertCoords and ((tile[0]-16,tile[1])) in desertCoords and ((tile[0],tile[1]+16)) in desertCoords and ((tile[0],tile[1]-16)) in desertCoords:
                tempCoords.add(tile)
                desertCoords.add(tile)
        
        # misc    
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

# society evolution class
class societygen():
    # society spawning
    def spawning(posSpawnCoords,colorcodes):
        spawntile = random.choice(list(posSpawnCoords))

        while spawntile not in posSpawnCoords:
            spawntile = random.choice(list(posSpawnCoords))
        if year == 0:
            posSpawnCoords.remove(spawntile)
            
        color = (random.choice(colorcodes)) #150
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
        if year == 0:
            governmenttype = "Chieftan"
        else:
            governmenttype = "Provisional"

        currency = 0
        military = 10 #K
        citzensatisfaction = random.randint(60,90) #percent
        datapack = [[spawntile],color,societycharacteristics,name,governmenttype,currency,military,citzensatisfaction,spawntile]
        
        return datapack,posSpawnCoords,colorcodes

    # society expansion
    def expand(datapack,posSpawnCoords,seaCoords):
        allTiles = datapack[0]
        if allTiles:
            curTile = random.choice(allTiles)
        else:
            return datapack,posSpawnCoords
            
        tempTile = allTiles[:]
        mynums = [1,2,3,4,5,6,7,8]
        mynum = random.choice(mynums)
        
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
        
    # society colonisation
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

# sidebar class
class sidebar():
    # bottom sidebar
    def bottom():
        win.blit(bar,((0,640)))
        bar1 = game.transform.rotate(bar, 180)
        win.blit(bar1,((320,640)))
        
    # righthand sidebar
    def right():
        bar1 = game.transform.rotate(bar, 270)
        win.blit(bar1,((640,0)))
        bar2 = game.transform.rotate(bar, 90)
        win.blit(bar2,((640,320)))
        
    # icons in sidebar
    def icons(turnamount):
        win.blit(treeicon,(672,576))
        win.blit(bothicon,(720,576))
        win.blit(politicalicon,(768,576))
        
        if turnamount!=1:
            win.blit(num11,(672,464))
        else:
            win.blit(num12,(672,464))
            
        if turnamount!= 5:
            win.blit(num51,(720,464))
        else:
            win.blit(num52,(720,464))
            
        if turnamount!=10:
            win.blit(num101,(768,464))
        else:
            win.blit(num102,(768,464))

        if earth1.get_rect(top=576,left=672).collidepoint(game.mouse.get_pos()):
            win.blit(treeicon2,(672,576))
        if earth1.get_rect(top=576,left=720).collidepoint(game.mouse.get_pos()):
            win.blit(bothicon2,(720,576))
        if earth1.get_rect(top=576,left=768).collidepoint(game.mouse.get_pos()):
            win.blit(politicalicon2,(768,576))

        win.blit(arrow1,(688,512))
        if arrow1.get_rect(top=512,left=688).collidepoint(game.mouse.get_pos()):
            win.blit(arrow2,(688,512))

        if earth1.get_rect(top=464,left=672).collidepoint(game.mouse.get_pos()):
            win.blit(num12,(672,464))
        if earth1.get_rect(top=464,left=720).collidepoint(game.mouse.get_pos()):
            win.blit(num52,(720,464))
        if earth1.get_rect(top=464,left=768).collidepoint(game.mouse.get_pos()):
            win.blit(num102,(768,464))

# misc functions class
class other():
    # track and display cursor
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
            
    # find area around random coordinate
    def findarea(Coords):
        ranTile = random.choice(list(Coords))
        area = {(ranTile)}
        temp = set()
        
        for i in range(len(Coords)):
            for tile in area:
                for num in range(8):
                    xplus = 0
                    yplus = 0
                    
                    if num == 1 or num == 5 or num == 6:
                        xplus = -16
                    if num == 2 or num == 7 or num == 8:
                        xplus = 16
                    if num == 3 or num == 5 or num == 7:
                        yplus = -16
                    if num == 4 or num == 8 or num == 6:
                        yplus = 16

                    if ((tile[0]+xplus,tile[1]+yplus)) in Coords and ((tile[0]+xplus,tile[1]+yplus)) not in area:
                        temp.add(((tile[0]+xplus,tile[1]+yplus)))
                    elif ((tile[0]+xplus,tile[1]+yplus)) in Coords and ((tile[0]+xplus,tile[1]+yplus)) not in area:
                        temp.add(((tile[0]+xplus,tile[1]+yplus)))
                    else:
                        pass
                        
            for tile in temp:
                area.add(tile)
                
        return area

    # determine chances of events 1
    def turnsB(sizeCondition,condition,turnType,bigpack,itemnum,possibleTurns):
        if len((bigpack[itemnum])[0]) > sizeCondition:
            for i in range(condition):
                possibleTurns.append(turnType)
            return possibleTurns
        else:
            return possibleTurns
            
    # determine chances of events 2
    def turnsS(sizeCondition,condition,turnType,bigpack,itemnum,possibleTurns):
        if len((bigpack[itemnum])[0]) <= sizeCondition:
            for i in range(condition):
                possibleTurns.append(turnType)
            return possibleTurns
        else:
            return possibleTurns

# data needed for game
landCoords,seaCoords,allCoords,mountainCoords,snowCoords,grassCoords,desertCoords,treeCoords,posCoastCoords,posSpawnCoords,mountainOffset,treeOffset = gen.finalgen()
myalpha = 180
colorcodes = [(0,255,255),(255,0,255),(0,255,0),(255,182,34),(253,179,241),(205,255,0),(161,114,255),(173,255,47),(144,238,144), (64,224,208),(127,255,212),(216,191,216),(95,158,160),]

# data formatting
bigpack = list()
for i in range(random.randint(3,7)):
    datapack,posSpawnCoords,colorcodes = societygen.spawning(posSpawnCoords,colorcodes)
    bigpack.append(datapack)

# more data formatting
for i in range(10):
    for itemnum in range(len(bigpack)):
        if random.randint(1,2) == 1:
            bigpack[itemnum],posSpawnCoords = societygen.expand(bigpack[itemnum],posSpawnCoords,seaCoords)
            for item in bigpack:
                for tile in item[0]:
                    if tile in posSpawnCoords:
                        posSpawnCoords.remove(tile)
                        
# game loop variables
allbigpacks = list()
civselected = -1
worldGameState = False
titleGameState = True
area = set()

# game fonts
treb50 = game.font.SysFont("Trebuchet MS",100)
treb20 = game.font.SysFont("Trebuchet MS",17)

# game loop
while True:
    # title screen
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
        win.blit(button,(640,640,640+192,640+192))

        sidebar.right()
        sidebar.bottom()

        # if play is clicked
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

    # gameplay loop
    turnamount = 1
    while worldGameState == True:
        # draw sidebar
        sidebar.right()
        sidebar.bottom()
        sidebar.icons(turnamount)
        
        # draw tiles (ocean, grass, desert, snow, mountain, tree)
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
            win.blit(mountain,((tile[0]+mountainOffset[tile]),(tile[1])))
        for tile in treeCoords:
            win.blit(tree,((tile[0]+treeOffset[tile]),(tile[1])))
        
        # draw button
        win.blit(button,(640,640,640+192,640+192))

        # check if a tribe has been clicked
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
                            civselected = bigpack.index(item)

        # if a tribe actually has been selected
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

        # get pressed keys
        keys = game.key.get_pressed()

        # if a pygame event occurs
        for event in game.event.get():
                        
            # if an icon has been clicked
            if event.type == game.MOUSEBUTTONDOWN:
                if treeicon.get_rect(top=576,left=672).collidepoint(game.mouse.get_pos()):
                    myalpha = 0
                    Iconmus.play()
                elif bothicon.get_rect(top=576,left=720).collidepoint(game.mouse.get_pos()):
                    myalpha = 180
                    Iconmus.play()
                elif politicalicon.get_rect(top=576,left=768).collidepoint(game.mouse.get_pos()):
                    myalpha = 1000
                    Iconmus.play()
                elif num11.get_rect(top=464,left=672).collidepoint(game.mouse.get_pos()):
                    Iconmus.play()
                    turnamount = 1
                elif num51.get_rect(top=464,left=720).collidepoint(game.mouse.get_pos()):
                    Iconmus.play()
                    turnamount = 5
                elif num101.get_rect(top=464,left=768).collidepoint(game.mouse.get_pos()):
                    Iconmus.play()
                    turnamount = 10

                # if the terrain gen button is clicked
                if button.get_rect(top=(640),left=(640)).collidepoint(event.pos):
                    colorcodes = [(0,255,255),(255,0,255),(0,255,0),(255,182,34),(253,179,241),(205,255,0),(161,114,255),(173,255,47),(144,238,144),(64,224,208),(127,255,212),(216,191,216),(95,158,160)]
                    Newmus.play()
                    year = 0
                    landCoords,seaCoords,allCoords,mountainCoords,snowCoords,grassCoords,desertCoords,treeCoords,posCoastCoords,posSpawnCoords,mountainOffset,treeOffset = gen.finalgen()
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

                # if the next turn button has been clicked
                if arrow1.get_rect(top=512,left=688).collidepoint(game.mouse.get_pos()):
                    for i in range(turnamount):
                        year+=1
                        Iconmus.play()
                        
                        # compute random chance events
                        for itemnum in range(len(bigpack)):
                            newsstuff = list()
                            newslist = list()
                            possibleTurns = list()
    
                            possibleTurns=other.turnsB(20,4,"consolidate",bigpack,itemnum,possibleTurns)
                            cancolonize = False
                            
                            for i in (bigpack[itemnum])[0]:
                                if ((i[0]-16,i[1])) in seaCoords or ((i[0]+16,i[1])) in seaCoords or ((i[0],i[1]-16)) in seaCoords or ((i[0],i[1]+16)) in seaCoords:
                                    cancolonize = True
                                    
                            if cancolonize == True:
                                possibleTurns=other.turnsB(20,5,"colonize",bigpack,itemnum,possibleTurns)
    
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
    
                                if random.randint(1,5) == 1: # rebellion
                                    area = other.findarea(bigpack[itemnum][0])
                                    if bigpack[itemnum][8] not in area:
                                        datapack,area,colorcodes = societygen.spawning(area,colorcodes)
                                        datapack[0] = list(area)
                                        datapack[8] = random.choice(list(area))
                                        bigpack[itemnum][0] = set(bigpack[itemnum][0])
                                        bigpack[itemnum][0] -= area
                                        bigpack[itemnum][0] = list(bigpack[itemnum][0])
                                        bigpack.append(datapack)
    
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
    
                    allbigpacks.append(bigpack)

            if event.type == game.QUIT:
                endGame = True
                worldGameState = False
                
        other.mousemovement()
        game.display.flip()

    # if the game is quit
    if endGame == True:
        break
        
# end game
game.quit()
