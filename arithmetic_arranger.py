''' A function created for arranging up to five addition and subtraction problems'''

def arithmetic_arranger(maths, results=0):


    '''Takes a list of maths problems and arranges them vertically. If the optional parameter "results" is inputted, the function also      	displays the answers to the problems'''

    if len(maths) > 5:
        print("Error, too many problmes")
    else:
        operatorlist = []
        for problem in maths:
            problem_split = problem.split()
            operatorlist.append(problem_split[1])
    filteredmaths = list(filter(lambda z: z in ("-", "+"), operatorlist))
    if len(filteredmaths) != len(operatorlist):
        print("Operator must be '+' or '-' ")
    else:
        operandlist = []
        for problem in maths:
            problem_split = problem.split()
            operandlist.append(problem_split[0])
            operandlist.append(problem_split[2])
        filteredmaths2 = list(filter(lambda z: not z.isdigit(), operandlist))
        if len(filteredmaths2) != 0:
            print("Error: Numbers must only contain digits")

        else:
            filteredmaths3 = list(filter(lambda z: len(z) > 4, operandlist))
            if len(filteredmaths3) != 0:
                print("Error: Numbers cannot be more than four digits.")
            else:
                if len(filteredmaths3) == 0:
                    for problem in maths:
                        problem_split = problem.split()
                        topline = ("  " + problem_split[0]).rjust(15)
                        print(topline.format(4), end="")
                    print("")
                    for problem in maths:
                        problem_split = problem.split()
                        bottomline = (problem_split[1] + " " + problem_split[2]).rjust(15)
                        print(bottomline.format(4), end="")
                    print("")
                    for problem in maths:
                        problem_split = problem.split()
                        if len(problem_split[0]) >= len(problem_split[2]):
                            print(((len(problem_split[0])+1)*"-").rjust(15), end="")
                        else:
                            print(((len(problem_split[2])+1)* "-").rjust(15), end="")
                    print("")
                    if results:
                        for problem in maths:
                            problem_split = problem.split()
                            subtrctn_formatting = str(int(problem_split[0]) - int(problem_split[2])).rjust(15)
                            addtn_formatting = str(int(problem_split[0]) + int(problem_split[2])).rjust(15)
                            if problem_split[1] == "-":
                                print(subtrctn_formatting.format(4), end="")
                            if problem_split[1] == "+":
                                print(addtn_formatting.format(4), end="")
                    else:
                        print("   ")
        return 
