import random

def news(datapack,newstype):
    specialthing = newstype[1]
    newstype = newstype[0]
    sp = " "
    co = ","
    fu = "."
    citychoosen = random.choice(list(datapack[10].keys()))
    city = datapack[10][citychoosen].capitalize()
    ### Words lists
    people = ["people","citzens","civilians","commoners","villagers","students","militias"]
    government = ["government","authority","bureaucracy","regime"]
    near = ["in","near","close to","inside"]
    response = ["in response","in reaction"]#,"as a response","as a reaction"]
    turned = ["turned to","transitioned to","became"]
    explosion = ["an explosion","a blast","a detonation"]
    numbers = ["1000","2000","3000","4000","1500","2500","3500","4500","5000"]
    killed = ["murded","killed","exterminated","shot"]
    goodthings =["a free and independent","a united","an equal and just","a peoples"]
    flag = ["flag","emblem","symbol"]
    badthings = ["riots","attacks on policemen","brawls","protests","trouble","strife"]
    badadjs = ["corrupt","villainous","selfish","nefarious","reactionary","dirty","cruel","crooked","vile","wicked"]
    amountoftime = ["months","days","weeks","fortnights"]
    goodthingsinland = ["cultures and ethnicites","rivers and hills","fruits and grains","animals and plants"]
    living = ["living","residing","dwelling","inhabiting"]
    freedom = ["freedom","liberty","autonomy","self-sovereignty"]
    culminated = ["culminated","concluded","climaxed","ended"]
    several = ["several","multiple","various","definite"]
    ### Sentence lists REV

    REVtimes = ["early in the year","late in the year","on the summer solstice","on the winter solstice","as the leaves turned from green to brown",
             "in the middle of the year","while spring "+random.choice(turned)+" summer","while summer "+random.choice(turned)+" winter","while winter "+random.choice(turned)+" autumn","while autumn "+random.choice(turned)+" spring"]

    REVangerythought = [random.choice(response)+" to a growing disillusiment with the "+random.choice(government),random.choice(response)+" to failed reforms and economic policies",random.choice(response)+" to the "+random.choice(badadjs)+sp+ random.choice(government)+" leeching from the "+random.choice(people)]

    REVangeryaction = ["an explosion was planned by the "+random.choice(people),random.choice(people)+" took to the streets","a high ranking government official was kidnapped",
                    random.choice(people)+" demanded change " +random.choice(near)+" the capital of "+datapack[3], random.choice(people)+" raised their "+random.choice(flag)+", stained in the blood of the worker","in "+city+", one of the largest cities in "+datapack[3]+", riots ensued on the streets"]

    REVmilreaction = ["whilst support continued to plummet",random.choice(response)+" to the events forementioned"]

    REVmilaction = ["anyone suspected of being a traitor was "+random.choice(killed)+" by the military, amounting to "+random.choice(numbers)+" casualities"]


    REVresult = ["leading to a chain of events culminating in the overthowing of the old regime",". This "+random.choice(culminated)+" in groups of "+random.choice(people)+" storming the palace",]

    REVproclaiming = ["and the proclamation of a new goverment, "+random.choice(goodthings)+" government. The commune of "+datapack[3]+"!"]

    ### Sentence lists CIT

    #The central government of x

    #before

    CITstarter = ["the lands of "+datapack[3]+ " are comprised of vast tracts of land with bountiful differing "+random.choice(goodthingsinland)+" inhabiting it which has led to a certain degree of freedom for the peoples "+random.choice(living)+" there","the peoples of "+datapack[3]+" have freely manifested their destiny for much time"]

    CITproblem = ["unfortunately the central "+random.choice(government)+" has had several issues controlling fringe rebbelious areas as","however the "+random.choice(freedom)+" of these peoples has "+random.choice(freedom)+sp+random.choice(culminated)+" in a group of "+random.choice(badadjs)+sp+random.choice(people)+" attacking an official "+datapack[3]+ " government building"]

    CITfix = ["To counteract issues on the frontier where events such as "+random.choice(badthings)+" become increasingly common, it was in the "+random.choice(government)+" intrest to found a central city in the region"]

    #during

    #"As"

    #after

    result = ["for the several "+random.choice(amountoftime)+"it has been inhabited","whilst this government project has been underway"]



    bad = ["it has experienced "+random.choice(several)+" roadbumps such as claims of 'forced colonisation' ","several issues have surfaced like the urbanisation and loss of once valuable natural areas"]

    good = []

    #result+bad+govreaction , result+govreaction+bad , govreaction + bad + result , govreaction+result+bad , bad+result+govreaction, bad+govreaction+result
    govreaction = ["to the governments dismay","to the taxpayers funding the projects dismay"]
    beggining = [""]
    if newstype == "expand":
        rannum = random.randint(1,3)
        if rannum == 1:
            template1 = (random.choice(REVtimes).capitalize()+co+sp+random.choice(REVangerythought)+sp+random.choice(REVangeryaction))
        elif rannum == 2:
            template1 = (random.choice(REVangerythought).capitalize()+sp+random.choice(REVangeryaction)+sp+random.choice(REVtimes))
        elif rannum == 3:
            template1 = (random.choice(REVangeryaction).capitalize()+sp+random.choice(REVangerythought)+sp+random.choice(REVtimes))
        rannum = random.randint(1,2)
        if rannum == 1:
            template2 = (random.choice(REVmilreaction).capitalize()+sp+random.choice(REVmilaction)+sp+random.choice(REVresult))
        elif rannum == 2:
            template2 = (random.choice(REVmilaction).capitalize()+sp+random.choice(REVmilreaction)+random.choice(REVresult))
        story = template1+fu+sp+template2+sp+random.choice(REVproclaiming)
        return ["Revolt in "+datapack[3],story]



    if newstype == "expand":
        return "expansion test"



    if newstype == "consolidation":
        return "consolidation test"



    if newstype == "colonize":
        return "colonize test"



    if newstype == "proclamation":
        return "proclamation test"

    if newstype == "cityfounded":
        rannum = random.randint(1,2)
        if rannum == 1:
            template1 = (random.choice(CITstarter).capitalize()+sp+random.choice(CITproblem)+fu+sp+random.choice(CITfix)+fu)
        if rannum == 2:
            template1 = (random.choice(CITproblem).capitalize()+sp+random.choice(CITstarter)+fu+sp+random.choice(CITfix)+fu)

        return ["City of "+datapack[10][specialthing]+" founded",template1]


        return "nothing test"

    if newstype == "nothing":
        return "nothing test"






#    As they protested they were fired upon by the military causing a chain of events that culminated in

#    the storming of the parliament building toppling the old regime

#    and proclaiming a new government, “The commune of [civilization]”

#    Internationally several nations have already restored diplomatic ties with the newly formed government

#    though some for both ideological and politically reasons still recognise the old disempowered government

if __name__ == "__main__":


    spawntile = ((0,0))



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
    governmenttype = "Chieftan"

    pop = 0
    #pop = society.populationcalc([spawntile],fertilityIndex)
    #print(pop)
    military = 10 #K

    citzensatisfaction = random.randint(60,90) #percent
    newslol=list()
    cities = dict()
    #try:
    cities[spawntile] = "Sydney"#random.choice(allcities)

    #create civilization
    #war = [with who,with who 2,turns since started,win battle chance (use randint), has taken turn yet]
    war = [-1,0,0,0]

    datapack = [[spawntile],(0,0,0),societycharacteristics,name,governmenttype,pop,military,citzensatisfaction,spawntile,news,cities,war]

    for i in range(5):
        #while True:
            #["cityfounded","expand"]
            #random.choice(datapack[10])
            print(news(datapack,["cityfounded",(0,0) ]))
            #ews([[spawntile],(0,0,0),societycharacteristics,name,governmenttype,pop,military,citzensatisfaction,spawntile,news,{(0,0):"hello"}],"expand")
            input()
