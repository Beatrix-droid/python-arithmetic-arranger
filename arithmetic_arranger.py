

''' A function created for arranging up to five addition and subtraction problems'''

def arithmetic_arranger(maths, results=0):


    '''Takes a list of maths problems and arranges them vertically. If the optional parameter "results" is inputted, the function also
    displays the answers to the problems'''

    if len(maths) > 5:
        return "Error: Too many problems."
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
            else:
              operandlist = []
              operandlist.append(problem_split[0])
              operandlist.append(problem_split[2])
              filteredmaths2 = list(filter(lambda z: not z.isdigit(),       operandlist))
              if len(filteredmaths2) != 0:
                arranged_problems = "Error: Numbers must only contain digits."
              elif len(problem_split[0]) > 4 or len(problem_split[2]) > 4:
                arranged_problems = "Error: Numbers cannot be more than four digits."


              else:
                  
                      length = max([len(problem_split[0]), len( problem_split[2])]) 
                      toplines += ("   " + problem_split[0]).rjust(length) + "    "
                      bottomlines += (problem_split[1] + " " + problem_split[2]).rjust(length) + "    "
                      
                      if len(problem_split[0]) >= len(problem_split[2]):
                            lines += (" " + (len(problem_split[0]) + 1) * "-").rjust(length -1) + "    "
                      else:
                            lines += (" " +  (len(problem_split[2]) + 1) * "-").rjust(length -1) + "    "
                        
                        

                      if results:
                            subtrctn_formatting = str(int(problem_split[0]) - int(problem_split[2])).rjust(length) + " "
                            addtn_formatting = str(int(problem_split[0]) + int(problem_split[2])).rjust(length)+ "    "
                            if problem_split[1] == "-":
                                answers += subtrctn_formatting.format(length) + "    "
                                arranged_problems += answers
                            if problem_split[1] == "+":
                                    answers += addtn_formatting.format(length)  + "    "
                      
                            arranged_problems = toplines +"\n" + bottomlines +"\n" + lines + "\n" + answers
                      else:
                            arranged_problems = toplines +"\n" + bottomlines +"\n" + lines

            return arranged_problems
            ##
