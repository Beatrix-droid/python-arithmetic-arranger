
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
          arranged_problems = "Error: Operator must be '+' or '-'."
        else:
          operandlist = []
          for problem in maths:
             problem_split = problem.split()
             operandlist.append(problem_split[0])
             operandlist.append(problem_split[2])
          filteredmaths2 = list(filter(lambda z: not z.isdigit(),     operandlist))
          if len(filteredmaths2) != 0:
            arranged_problems = "Error: Numbers must only contain digits."

          else:
              filteredmaths3 = list(filter(lambda z: len(z) > 4, operandlist))
              if len(filteredmaths3) != 0:
                  arranged_problems =  "Error: Numbers cannot be more than four digits."
              else:
                  arranged_problems =""
                  if len(filteredmaths3) == 0:
                      toplines = ""
                      for problem in maths:
                          problem_split = problem.split()
                          toplines += ("  " + problem_split[0]).rjust(6) + "    "
                      toplines = toplines +"\n"
                      arranged_problems += toplines
                      
                      bottomlines = ""
                      for problem in maths:
                          problem_split = problem.split()
                          bottomlines += (problem_split[1] + " " + problem_split[2]).rjust(6) + "    "
                      bottomlines = bottomlines +"\n"
                      arranged_problems += bottomlines
                     
                      lines = ""
                      for problem in maths:
                        problem_split = problem.split()
                        if len(problem_split[0]) >= len(problem_split[2]):
                          lines += (" " + (len(problem_split[0]) + 1) * "-").rjust(6) + "    "
                        else:
                          lines += (" " +  (len(problem_split[2]) + 1) * "-").rjust(6) + "    "
                      lines = lines + "\n"
                      arranged_problems += lines

                      if results:
                          answers = ""
                          for problem in maths:
                              problem_split = problem.split()
                              subtrctn_formatting = str(int(problem_split[0]) - int(problem_split[2])).rjust(4) + "    "
                              addtn_formatting = str(int(problem_split[0]) + int(problem_split[2])).rjust(4)+ "    "
                              if problem_split[1] == "-":
                                  answers += subtrctn_formatting.format(4) + "    "
                                  arranged_problems += answers
                              if problem_split[1] == "+":
                                  answers += addtn_formatting.format(4)
                                  arranged_problems += answers + "    "
                      else:
                          answers = "\n"
                          arranged_problems += answers

    return arranged_problems
