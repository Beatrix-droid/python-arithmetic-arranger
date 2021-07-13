

''' A function created for arranging up to five addition and subtraction problems'''

def arithmetic_arranger(maths, results=0):


    '''Takes a list of maths problems and arranges them vertically. If the optional parameter "results" is inputted, the function alsO
    displays the answers to the problems'''

    if len(maths) > 5:
        arranged_problems = "Error: Too many problems."
        return arranged_problems
    else:
        toplines = ""
        bottomlines = ""
        lines = ""
        answers = ""
        operatorlist = []
        for problem in maths:
            problem_split = problem.split()
            operatorlist.append(problem_split[1])
            filteredmaths = list(filter(lambda z: z in ("-", "+"), operatorlist))
        
            if len(filteredmaths) != len(operatorlist):
              arranged_problems = "Error: Operator must be '+' or '-'."
              return arranged_problems
            else:
              operandlist = []
              operandlist.append(problem_split[0])
              operandlist.append(problem_split[2])
              filteredmaths2 = list(filter(lambda z: not z.isdigit(),       operandlist))
              if len(filteredmaths2) != 0:
                arranged_problems = "Error: Numbers must only contain digits."
                return arranged_problems
              elif len(problem_split[0]) > 4 or len(problem_split[2]) > 4:
                arranged_problems = "Error: Numbers cannot be more than four digits."
                return arranged_problems

              else:
                  
                  length = max([len(problem_split[0]), len( problem_split[2])]) + 2
                  toplines += (problem_split[0]).rjust(length)
                  bottomlines += problem_split[1]+ (problem_split[2]).rjust(length-1)

                  if len(problem_split[0]) >= len(problem_split[2]):
                        lines += (" " + (len(problem_split[0]) + 2) * "-").rjust(length-2)
                  else:
                        lines += (" " +  (len(problem_split[2]) + 2) * "-").rjust(length-2)

                  if results:
                        subtrctn_formatting = str(int(problem_split[0]) - int(problem_split[2])).rjust(length) + " "
                        addtn_formatting = str(int(problem_split[0]) + int(problem_split[2])).rjust(length)+ "    "
                        if problem_split[1] == "-":
                            answers += subtrctn_formatting.format(length)
                              
                        if problem_split[1] == "+":
                                answers += addtn_formatting.format(length)
                      
                  else:
                        answers += "\n"
                  if problem != maths[-1]:
                    toplines += "    "
                    bottomlines += "    "
                    lines += "    "
                    answers += "    "

                          
        arranged_problems = toplines +"\n" + bottomlines +"\n" + lines + "\n" + answers
        
        return arranged_problems
            ##
