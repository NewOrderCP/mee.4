file1=open('allwords.txt','r')
aws_list0=file1.readlines()
aws_str="".join(aws_list0)
aws_list=aws_str.split("', '")
file1.close()
input_str=raw_input("Please enter the letters:")
input_list=input_str.split(",")

print('sadsdad')

