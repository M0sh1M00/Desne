import random

def news(datapack,newstype):
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
    ### Sentence lists REV

    times = ["early in the year","late in the year","on the summer solstice","on the winter solstice","as the leaves turned from green to brown",
             "in the middle of the year","while spring "+random.choice(turned)+" summer","while summer "+random.choice(turned)+" winter","while winter "+random.choice(turned)+" autumn","while autumn "+random.choice(turned)+" spring"]

    angerythought = [random.choice(response)+" to a growing disillusiment with the "+random.choice(government),random.choice(response)+" to failed reforms and economic policies",random.choice(response)+" to the "+random.choice(badadjs)+sp+ random.choice(government)+" leeching from the "+random.choice(people)]

    angeryaction = ["an explosion was planned by the "+random.choice(people),random.choice(people)+" took to the streets","a high ranking government official was kidnapped",
                    random.choice(people)+" demanded change " +random.choice(near)+" the capital of "+datapack[3], random.choice(people)+" raised their "+random.choice(flag)+", stained in the blood of the worker","in "+city+", one of the largest cities in "+datapack[3]+", riots ensued on the streets"]

    milreaction = ["whilst support continued to plummet",random.choice(response)+" to the events forementioned"]

    milaction = ["anyone suspected of being a traitor was "+random.choice(killed)+" by the military, amounting to "+random.choice(numbers)+" casualities"]


    result = [" leading to a chain of events culminating in the overthowing of the old regime",". This culminated in groups of "+random.choice(people)+" storming the palace",]

    proclaiming = ["and the proclamation of a new goverment, "+random.choice(goodthings)+" government. The commune of "+datapack[3]+"!"]

    ### Sentence lists EXP

    beggining = [""]
    if newstype == "expand":
        rannum = random.randint(1,3)
        if rannum == 1:
            template1 = (random.choice(times).capitalize()+co+sp+random.choice(angerythought)+sp+random.choice(angeryaction))
        elif rannum == 2:
            template1 = (random.choice(angerythought).capitalize()+sp+random.choice(angeryaction)+sp+random.choice(times))
        elif rannum == 3:
            template1 = (random.choice(angeryaction).capitalize()+sp+random.choice(angerythought)+sp+random.choice(times))
        rannum = random.randint(1,2)
        if rannum == 1:
            template2 = (random.choice(milreaction).capitalize()+sp+random.choice(milaction)+sp+random.choice(result))
        elif rannum == 2:
            template2 = (random.choice(milaction).capitalize()+sp+random.choice(milreaction)+random.choice(result))
        return ["Revolt in "+datapack[3],template1+fu+sp+template2+sp+random.choice(proclaiming)]



    if newstype == "expand":
        return "expansion test"



    if newstype == "consolidation":
        return "consolidation test"



    if newstype == "colonize":
        return "colonize test"



    if newstype == "proclamation":
        return "proclamation test"



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
    news=list()


    datapack = [[spawntile],(0,0,0),societycharacteristics,name,governmenttype,pop,military,citzensatisfaction,spawntile,news,{(0,0):"hello"}]

    for i in range(1):
        while True:
            #print(datapack)
            news([[spawntile],(0,0,0),societycharacteristics,name,governmenttype,pop,military,citzensatisfaction,spawntile,news,{(0,0):"hello"}],"expand")
            input()
