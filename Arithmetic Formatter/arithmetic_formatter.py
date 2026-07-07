def arithmetic_arranger(problems, show_answers=False):
    #too many problems error
    if len(problems) > 5:
        return 'Error: Too many problems.'
    
    #invalid opperator error plus remembering operations
    operator = []
    index = []

    for problem in problems:
        if problem.find("+") == -1 and problem.find("-") == -1:
            return "Error: Operator must be '+' or '-'."

        elif problem.find("+") != -1 and problem.find("-") == -1:
            operator.append("+")
            index.append(problem.find("+"))

        elif problem.find("-") != -1 and problem.find("+") == -1:
            operator.append("-")
            index.append(problem.find("-"))

    #separating numbers and error for invalid characters
    operand_1 = []
    operand_2 = []
    iterator_1 = 0

    try:
        for problem in problems:
            operand_1.append(int(problem[:index[iterator_1]].strip()))
            operand_2.append(int(problem[index[iterator_1] + 1:].strip()))
            iterator_1 += 1
    except:
        return 'Error: Numbers must only contain digits.'
        
    #finding length of numbers and calling out length limit error
    length = []
    iterator_2 = 0
    line_3 = ""

    for problem in problems:
        length.append(max(len(str(operand_1[iterator_2])), len(str(operand_2[iterator_2]))))

        #writing line-3
        for i in range(max(len(str(operand_1[iterator_2])), len(str(operand_2[iterator_2]))) + 2):
            line_3 += "-"
        line_3 += "    "    
        
        if max(len(str(operand_1[iterator_2])), len(str(operand_2[iterator_2]))) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        iterator_2 += 1 

    line_3 = line_3.rstrip()      

    #writing line-1  
    line_1 = ""
    iterator_3 = 0

    for operand in operand_1:
        line_1 += "  "
        upspace = max(len(str(operand)), len(str(operand_2[iterator_3]))) - len(str(operand))

        for i in range(upspace):
            line_1 += " "

        line_1 += str(operand) + "    "  
        iterator_3 += 1     

    line_1 = line_1.rstrip()
    
    #writing line-2
    line_2 = ""
    iterator_4 = 0

    for operand in operand_2:
        line_2 += operator[iterator_4] + " "
        downspace = max(len(str(operand_1[iterator_4])), len(str(operand))) - len(str(operand))

        for i in range(downspace):
            line_2 += " "
        
        line_2 += str(operand) + "    "
        iterator_4 += 1
    
    line_2 = line_2.rstrip()
    
    #final output
    if show_answers == False:
        return line_1 + "\n" + line_2 + "\n" + line_3

    elif show_answers == True:
        #writing line-4
        line_4 = ""
        iterator_5 = 0
        answer = None

        for problem in problems:
            if operator[iterator_5] == "+":
                answer = operand_1[iterator_5] + operand_2[iterator_5]
            else:
                answer = operand_1[iterator_5] - operand_2[iterator_5]  

            space = max(len(str(operand_1[iterator_5])), len(str(operand_2[iterator_5]))) - len(str(answer)) + 2

            for i in range(space):
                line_4 += " "

            line_4 += str(answer) + "    "
            iterator_5 += 1

        line_4 = line_4.rstrip()
        return line_1 + "\n" + line_2 + "\n" + line_3 + "\n" + line_4
