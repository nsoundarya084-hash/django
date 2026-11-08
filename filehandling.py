#mode "r method" = read file
file = open("demo.txt", mode ='r')
read_data = file.read()
print(read_data)
file.close()


#readline
file = open("demo.txt" , mode ='r')
read_data = file.readline()
print(read_data)
file.close()


#readlines
file = open("demo.txt",mode ='r')
read_data = file.readlines()
print(read_data)
file.close()



#append
file = open("demo.txt",mode ='a')
write_data = file.write("\n this is append operation by using mode a")
file.close()

#write opa = create new file
file = open("demo1.txt",mode = 'w')
write_data = file.write("create a newfile by using mode w")
file.close()


# a mode also create new file
file = open("demo2.txt",mode = 'a')
file.close()

#writelines
voter_data = ["\nsoundarya","\nsridharreddy","\nkrithikareddy","\nkarthikeyareddy"]
file = open("demo1.txt",mode='a')
write_data = file.writelines(voter_data)
file.close()


#mode = w+=create newfile read and write "tell"=findout curser "seek"=using curserline after 0
file = open("demo3.txt",mode = 'w+')
write_data = file.write("welcome to pythonlife")
print(file.tell())
file.seek(0)
read_data = file.read()
print(read_data)
file.close()



#mode r+
file = open("demo1.txt",mode= 'r+')
write_data = file.write("hello everyone by using r+mode")
read_data = file.read()
print(read_data)
file.close()

#mode a+
file = open("demo4.txt",mode='a+')
write_data = file.write("\nwelcome to pythonlife by using mode a+")
print(file.tell())
file.seek(0)
read_data =file.read()
print(read_data)

file.close()




file = open("C:\\Users\\Admin\\Desktop\\python1.txt",mode ='r')
read_data = file.read()
print(read_data)
file.close()


file = open("C:\\Users\\Admin\\Desktop\\python123.txt",mode ='w')
file.close()


