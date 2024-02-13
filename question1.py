

def main():

    count = 0

    with open('input.txt','r') as file:
        for line in file:
            line.strip()

            for n in line: 
                if n.isdigit():
                    firstnum = int(n)
                    break
    
            for n in range(len(line)-1,-1,-1):
                if line[n].isdigit():
                    lastnum = int(line[n])
                    break

            number = firstnum *10 + lastnum
            count += number

    print(count)
    
main()



    



 