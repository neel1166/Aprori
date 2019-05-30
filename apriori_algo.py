import itertools as it

def apriori_gen(input_file_name,min_supp):
    f=open(map_file_name,'r')
    map_list=[words for words in f.read().split()]
    map_dict={map_list[i+1]:map_list[i] for i in range(0,len(map_list),2)} #creating a dictionary for mapping items
    f.close()
    output =open("cs634_Neel Patel_apriori_"+str(min_supp)+".txt", "a")
    output.write("a. ID: njp62, course: CS634-101 Data Mining\n b. Name: Neel Patel\n c. File-name: cs634_Neel Patel_apriori.py\n d. Assignment due date: 11:59pm on Monday October 29\n e. Program pursose: To find out frequent itemsets using apriori algorithm"+"\n\n")
    output.close()
    transactions = []
    s=open(input_file_name,'r')
    for l in s:
        transactions.append(l.replace(';',' ').split()) #removing the delimineter
    for k,v in map_dict.items():
     for i in transactions:
         if k in i:
            i[i.index(k)]=map_dict[k]
    count={}
    for i in sorted(transactions):
      for j in i:
        if(sum(x.count(j) for x in transactions)) >= min_supp:
          count[j]=sum(x.count(j) for x in transactions)
    if not count:
        output.write(" NO frequent itemsets found!!! ")

    output = open("cs634_Neel Patel_apriori_"+str(min_supp)+".txt", "a")
    output.write("Frequent itemsets having minimum support of "+str(min_supp)+" are as follows:\n")
    output.write('\n'.join("{}: ({})".format(k, v) for k, v in sorted(count.items()))+'\n')
    output.close()

    n=2
    while True:
        transactions_L =sorted(list(it.combinations(count, n)))
        count_L,l2= {},[]
        for i in transactions:
            l2.append(list(it.combinations(i, n)))

        for j in transactions_L:
            k = sum(x.count(j) for x in l2)
            if k >= min_supp:
                count_L[j] = k
        for j in count_L.copy().keys():
            if n >= 3:
                if set(sorted(it.combinations(j, n - 1))).issubset(subs):
                    continue
                else:
                    del count_L[j]
        output = open("cs634_Neel Patel_apriori_"+str(min_supp)+".txt", "a")
        output.write('\n'.join("{}: ({})".format(k,v) for k, v in sorted(count_L.items()))+'\n')
        output.close()

        n=n+1
        subs = set(sorted(count_L.keys()))
        count=sorted(set(it.chain(*count_L)))
        if not count_L:
           break
        transactions_L.clear()

input_file_name=input("Enter the name of text file which contains the transaction for frequent itemset mining (include file extention .txt): ")
print("The provided file contains : ")
print("1. Clean Transactions\n2. Unclean Transactions")
options=int(input("Enter the choice from above 1 or 2"))
if options==2:
    map_file_name=input("Enter the name of mapping file for eliminating unclean transactions (include file extention .txt): ")
min_supp=int(input("Enter the minimum support value(for example: 4,5): "))
apriori_gen(input_file_name,min_supp)