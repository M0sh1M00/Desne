import random

def news(datapack,newstype):
    sp = " "
    co = ","
    fu = "."
    ### Words lists
    people = ["people","citzens","civilians","commoners","villagers"]
    government = ["government","authority","bureaucracy","regime"]
    near = ["in","near","close to","inside"]
    response = ["in response","in reaction","as a response","as a reaction"]
    turned = ["turned to","transitioned to","became"]
    explosion = ["an explosion","a blast","a detonation"]
    numbers = ["1000","2000","3000","4000","1500","2500","3500","4500","5000"]
    ### Sentence lists REV

    times = ["early in the year","late in the year","on the summer solstice","on the winter solstice","as the leaves turned from green to brown",
             "in the middle of the year","as spring "+random.choice(turned)+" summer","as summer "+random.choice(turned)+" winter","as winter "+random.choice(turned)+" autumn","as autumn "+random.choice(turned)+" spring"]

    angerythought = [random.choice(response)+" to a growing disillusiment with the "+random.choice(government),random.choice(response)+" to failed reforms and economic policies"]

    angeryaction = ["an explosion was planned by the "+random.choice(people),random.choice(people)+" took to the streets","a high ranking government official was kidnapped",
                    random.choice(people)+" demanded change " +random.choice(near)+" the capital of "+datapack[3]]


    milreaction = ["as support continued to plummet","in response to the events forementioned"]

    milaction = ["anyone suspected of being a traitor was murdered in cold blood by the military, a number amounting to "+random.choice(numbers)+" casualities","the "]



    result = ["leading to a chain of events culminating in the overthowing of [leader]","This culminated with groups of [people] storming the [palace]"]



    ### Sentence lists EXP

    beggining = [""]
    if newstype == "expand":
        rannum = random.randint(1,3)
        if rannum == 1:
            template1 = (random.choice(times)+co+sp+random.choice(angerythought)+sp+random.choice(angeryaction))
        elif rannum == 2:
            template1 = (random.choice(angerythought)+sp+random.choice(angeryaction)+sp+random.choice(times))
        elif rannum == 3:
            template1 = (random.choice(angeryaction)+sp+random.choice(angerythought)+sp+random.choice(times))
        return template1



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
    color = (random.randint(0,150),random.randint(0,150),random.randint(0,150))

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

    for i in range(1):
        while True:
            print(news(datapack,"revolution"))
            input()
