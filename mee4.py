file1=open('allwords.txt','r')
aws_list0=file1.readlines()
aws_str="".join(aws_list0)
aws_list=aws_str.split("', '")
file1.close()
input_str=raw_input("Please enter the letters:")
input_list=input_str.split(",")

place=[[1,1],[1,2],[1,3],[1,4],[1,5],
       [2,1],[2,2],[2,3],[2,4],[2,5],
       [3,1],[3,2],[3,3],[3,4],[3,5],
       [4,1],[4,2],[4,3],[4,4],[4,5],
       [5,1],[5,2],[5,3],[5,4],[5,5]]

letter_list=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

all_key=""

while(True):
    c=raw_input("Do you want to continue? Yes(y) or No(n):")

    if c=='y':
        num=0
        num1=0

        for word in aws_list:
            num=0
            for letter in letter_list:

                if (letter in word)&(letter in input_str):
                    if word.count(letter)<=input_str.count(letter):
                        num=num+word.count(letter)
                    else:
                        num=0
                        break

                if (letter in word)&(letter not in input_str):
                    num=0
                    break

            if num>num1:
                key=word
                num1=num
                print num

        if key in all_key:
            aws_list.remove(key)

        try:

            aws_list.remove(key)
            all_key = all_key + ',' + key
            print "The key word is:",key

            output=[]

            for i in key:
                output=output+[place[input_list.index(i)]]
            print output

        except:
            print "Game Over!"
            exit()

    else:
        exit()


