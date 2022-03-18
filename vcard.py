import time
def vcard_maker(file):
    counter=0
    counter2=0
    l=0
    m=1
    counter3=0
    list1=list()
    list2=list()
    print("vcard translator v1.0")
    file1= open(file,"r",encoding="utf-8")
    index=file1.read()
    f=""
    vcard="vcard"
    numbers = index.split(",")
    for i in range(71):
        list1.append(numbers[l])
        list2.append(numbers[m])
        l+=2
        m+=2
        counter3+=1
    for h in range(71):
        counter2 = str(counter2)

        a1=list1[counter]
        a2=list2[counter]
        vcard = a1 + counter2 + ".vcf"
        print(vcard)
        int(counter)
        file2=open(vcard, "x", encoding="utf-8".format(counter))
        file2.write("BEGIN:VCARD\nVERSION:3.0\nPRODID:-//Apple Inc.//iOS 12.4.1//EN\nN:21;{} ;;;\nFN:{} 21\nTEL;type=CELL;type=VOICE;type=pref:{}\nREV:2019-09-23T21:27:44Z\nEND:VCARD.format)" .format(a1,a1,a2))
        file2.close()
        counter2=int(counter2)
        counter+=1
        counter2+=1
    file1.close()

def vcard_maker2(file,file3):
    counter = 0
    counter2 = 0
    l = 0
    m = 1
    counter3 = 0
    list1 = list()
    list2 = list()
    print(type(counter2))
    print("vcard translator v2.0")
    file1 = open(file, "r", encoding="utf-8")
    file2 = open(file3, "a", encoding="utf-8".format(counter))
    index = file1.read()
    f = ""
    vcard = "vcard"
    numbers = index.split(",")
    print(len(numbers))
    for i in range(71):
        list1.append(numbers[l])
        list2.append(numbers[m])
        l += 2
        m += 2
        counter3 += 1

    for h in range(71):
        counter2 = str(counter2)
        vcard = "vcard" + counter2 + ".vcf"
        a1 = list1[counter]
        a2 = list2[counter]

        print(vcard)
        int(counter)

        file2.write(
            "BEGIN:VCARD\nVERSION:3.0\nPRODID:-//Apple Inc.//iOS 12.4.1//EN\nN:21;{} ;;;\nFN:{} 21\nTEL;type=CELL;type=VOICE;type=pref:{}\nREV:2019-09-23T21:27:44Z\nEND:VCARD)".format(
                a1, a1, a2))

        counter2 = int(counter2)
        counter += 1
        counter2 += 1

    print(numbers[0])

    # number = numbers.split("\t")
    print(numbers)
    # print(number)

    file1.close()
    file2.close()


print("Welcome to vcard translator..... ")
choice=int(input("Please select operation, \n1.------v1.0\n2.------v2.\nYour choice:"))
while True:
    if choice == 1:
        choice2=int(input("Enter Input File"))
        vcard_maker(choice2)
        time.sleep(5)
        print("Progress complete.")
        g=int(input("If you want to continue to the program press 1,or press other key for shutdown."))
        if g==1:
            continue
        else:
            break
    elif choice == 2:
        choice2 = int(input("Enter Input File"))
        choice3 = int(input("Enter Output File"))
        vcard_maker2(choice2,choice3)
        time.sleep(5)
        print("Progress complete")
        g = int(input("If you want to continue to the program press 1,or press other key for shutdown."))
        if g==1:
            continue
        else:
            break
    else:
        print("Wrong number.Please Try Again.")
        continue



