inp = input("Enter Matrix : ").split()
temp = [row.split(",") for row in inp]
matrix = [[int(x) for x in row] for row in temp]

f = open("myfile.txt", "w")

def writer(matrix):
    f.write('[')
    for row in matrix:
        f.writelines(row.__str__() + "," + "\n")
    f.write(']\n')
writer(matrix)
f.write('\n')

def solver(matrix):
    if len(matrix)==2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    det = 0
    sym = 1
    #loop all column
    for target in range(len(matrix)):
        res = []
        to_cal = []
        for i in range(len(matrix)):
            temp_row = []
            temp_to_cal = []
            for j in range(len(matrix)):
                if i==0 and j==target:
                    temp_row.append(matrix[i][j])
                elif j!=target and i!=0:
                    temp_row.append(matrix[i][j])
                    temp_to_cal.append(matrix[i][j])
                else:
                    temp.append(" ")
            if i!=0:
                to_cal.append(temp_to_cal)
            res.append(temp_row)
            
        #file writer
        writer(res)
        f.write(((str(sym * matrix[0][target] * solver(to_cal))) + "\n"))
        f.write("\n")
        
        det += sym * matrix[0][target] * solver(to_cal)
        sym *= -1
    return det
f.write("Answer :" + str(solver(matrix)))