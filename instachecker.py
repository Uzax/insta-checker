
# Created by : UZAX (F5oo4 - koksal <3)





import requests


targetURL = "https://www.istaunch.com/instagram-username-availability/"
data_1= {"username" : "" , "search" : "s" }
wordlist_p = input("Enter the wordlist :")

not_exi_a = []


with open(wordlist_p) as users:
    for line in users:
        word = line.strip()
        data_1["username"] = word
        r = requests.post(targetURL, data=data_1)

        if b"is Exist On Instagram" in r.content:
            print("[-]"+ word + " ----> Exist")
        else:
            print("[-]" +word +"-------> Not Exist")
            not_exi_a.append(word)
i = 0
while i < len(not_exi_a):
    print(not_exi_a[i], file=open("Output.txt","a"))
    i+= 1
    print(line)

print("[==] Reached end of line :(")
