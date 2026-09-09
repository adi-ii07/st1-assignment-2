#week 5 class work
#while --> depends on the condition
#for loop --> depends on the sequences or number of iteration
#while loop
counter: int = 0
while counter < 5:
    print(counter, "hello")
#will keep printing
    counter += 1
#unless counter+=1 is used

# for loop
print(list(range(5))) # start=0, stop=5, inc/dec=+1
print(list(range(1, 5))) # start=1, stop=5, inc/dec=+1
print(list(range(1, 5, 2))) # start=1, stop=5, inc/dec=+2

for counter in range(1, 5, 2):
    print(counter, "hello")

#problem --> inpute grade and check valid input and out of range
    input_grade = str(input("Enter your grade: "))

    if input_grade.replace(".", "", 1).isnumeric():
        grade: float = float(input_grade)

        if 0 <= grade <= 100:
            print(grade)
        else:
            print("out of range")
    else:
        print("wrong input, try again")







