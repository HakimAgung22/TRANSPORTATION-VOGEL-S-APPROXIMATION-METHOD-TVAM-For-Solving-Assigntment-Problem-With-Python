import random as rand
import os


# Created 16/03/2020
# By DonatKeju21
# This Library Created for only case matrix heuristic maximum and minimum
# Element class can be used for element matrix


#Object For Value Pinalty
#value : value of result counting pinalty
#typeM : type result pinalty (row/column)
#index : position result pinalty
class Pinalty:
    def __init__(self,value,typeM,index):
        self.value = value
        self.typeM = typeM
        self.index = index
        self.__s = ""
    
    def __str__(self):
        self.__s = "type : " + str(self.typeM) + " | index : " + str(self.index) + " | value : " + str(self.value)
        return self.__s

    def getValue(self):
        return self.value
    
    def getTypeM(self):
        return self.typeM
    
    def getIndex(self):
        return self.index

    def setValue(self,value):
        self.value = value

    def setTypeM(self,typeM):
        self.typeM = typeM

#Object For Element in Matrix
#value : value
#row : position row of element matrix
#col : position column of element matrix
class Element(object):
    def __init__(self,value,row,col):
        self.value = value
        self.row = row
        self.col = col
    
    def __str__(self):
        self.__s = "row : " + str(self.row) + " | col : " + str(self.col) + " | value : " + str(self.value)
        return self.__s

    def getValue(self):
        return self.value
    
    def getRow(self):
        return self.row

    def getCol(self):
        return self.col

    def setValue(self,value):
        self.value = value
    
    def setRow(self,row):
        self.row = row
    
    def setCol(self,col):
        self.col = col
    
#Input : filename in folder with format .csv
#output : array 2D
def FileToMatrix(nameFile):
    fileMat = open("data/"+nameFile+".csv","r")
    mat = fileMat.readlines()
    fileMat.close()
    arrMat = []
    arrMatRow = []
    for elementRow in mat:
        elementRow=elementRow.rstrip('\n')
        arrMatRow = elementRow.split(",")
        arrMat.append(list(map(float,arrMatRow)))
    return arrMat

# input : array 2D
#output : object matrix
def CreateMatrix(array):
    row = len(array)
    col = len(array[0])
    mat = array
    nMat = []
    i = 0
    while(i < row):
        j = 0
        arrC = []
        while(j < col):
            elm = Element(mat[i][j],i,j)
            arrC.append(elm)
            j += 1
        nMat.append(arrC)
        i += 1
    return nMat

#For Read File with type .csv
def ReadFile():
    l = os.listdir("data")
    arr = []
    print("******************")
    print("Pilih Data: ")
    i=0
    for x in l:
        y = x.split(".")
        if(y[1]=="csv"):
            arr.append(y[0])
            print(i+1,end="")
            print("."+str(x))
            i+=1
    print(str(i+1)+".create your own random matrix")
    arr.append("random")
    return arr
#************************Manipulate Matrix**********************#
#input : object matrix
#output : array2D
def MatrixToArray(mat):
    row = len(mat)
    col = len(mat[0])
    nMat = []
    i = 0
    while(i < row):
        j = 0
        arrC = []
        while(j < col):
            arrC.append(mat[i][j].getValue())
            j += 1
        nMat.append(arrC)
        i += 1
    return nMat

#input  : object matrix/ array 2D
#output : Transpose object matrix/ array 2D
def Transpose(m):
    mat = m
    row = len(mat)
    col = len(mat[0])
    newMat = []
    newMat = CreateZeroMatrix(col,row)
    i=0
    while i < row:
        y = 0
        while y < col:
            newMat[y][i] = mat[i][y]
            y +=1
        i += 1
    return newMat

#input  : n = total row matrix, m = total column matrix
#output : object matrix element zero
def CreateZeroMatrix(n,m):
    mat = []
    for i in range(n):
        arrC = []
        for j in range(m):
            elm = Element(0,i,j)
            arrC.append(0)
        mat.append(arrC)
    return mat

#input  : n = total row matrix, m = total column matrix, f = minimum value, e=maximum value
#output : object matrix element random
def CreateRandomMatrix(n,m,f,e):
    mat = []
    for i in range(n):
        arrC = []
        for j in range(m):
            val = rand.randint(f,e)
            elm = Element(val,i,j)
            arrC.append(elm)
        mat.append(arrC)
    return mat

#input  : mat = matrix, index = row index will be delete
#output : matrix with row index already deleted, list row matrix which deleted
def DelRow(mat,index):
    i = 0
    for x in mat:
        if(x[0].getRow() == index):
            break
        i += 1
    de = mat.pop(i)
    return mat,de

#input  : mat = matrix, index = column index will be delete
#output : matrix with column index already deleted, list column matrix which deleted
def DelCol(mat,index):
    i = 0
    de = []
    deC = -9999
    for x in mat:
        i = 0
        for y in x:
            if(y.getCol() == index):               
                deC = x.pop(i)
                de.append(deC)  
            i += 1
    return mat,de
#********************Aproximaxy Method***********************#

#input  : mat = matrix,sIter = iterasi for recursif
#output : list pinalty row and column
def CountAllPinalty(mat,sIter,tM,case):
    #case for counting pinalty row
    matV = MatrixToArray(mat)
    lP = []
    i = 0
    if(case == "tvam"):
        tM = "min"
    for x in matV:
        mm1 = GetNMinMax(x,sIter,tM)
        mm2 = GetNMinMax(x,sIter+1,tM)
        val = abs(mm1 - mm2)
        p = Pinalty(val,"row",i)
        lP.append(p)
        i += 1
    
    #case for counting pinalty column
    matV = Transpose(matV)
    i = 0
    for x in matV:
        mm1 = GetNMinMax(x,sIter,tM)
        
        mm2 = GetNMinMax(x,sIter+1,tM)
        val = abs(mm1 - mm2)
        p = Pinalty(val,"col",i)
        lP.append(p)
        i += 1
    return lP

#input  : listPinalty = list pinalty, pinalty = value of penalty will be delete
#output : one of element listPinalty already deleted
def PopListPinalty(listPinalty,pinalty):
    i = 0
    for val in listPinalty:
        if(val.getTypeM() == pinalty.getTypeM() and val.getIndex() == pinalty.getIndex()):
            break
        i+=1
    listPinalty.pop(i)
    return listPinalty

#input  : mat= matrix, listPinalty = list pinalty, tM = type of methode (min/max)
#output : list pinalty with value already updated
def UpdatePinalty(mat,listPinalty,tM):
    j=0
    min1= 0
    min2= 0
    matV = MatrixToArray(mat)
    aRow = []
    aCol = []

    if(len(mat[0])==1):
        val = GetNMinMax(matV,0,tM)
        tP = listPinalty[0]
        for pinalty in listPinalty:
            
            if(pinalty.getValue() == val):
                tP = pinalty
                break
        listPinalty = []
        listPinalty.append(pinalty)
    else:
        for x in matV:
            mm1 = GetNMinMax(x,0,tM)
            mm2 = GetNMinMax(x,1,tM)
            val = abs(mm1 - mm2)
            aRow.append(val)
        matV = Transpose(matV)
        for x in matV:
            mm1 = GetNMinMax(x,0,tM)
            mm2 = GetNMinMax(x,1,tM)
            val = abs(mm1 - mm2)
            aCol.append(val)
        i = 0
        for x in mat:
            for pinalty in listPinalty:
                if(pinalty.getTypeM() == "row" and pinalty.getIndex() == x[0].getRow()):
                    pinalty.setValue(aRow[i])
            i+=1
        i=0
        for x in mat[0]:
            for pinalty in listPinalty:
                if(pinalty.getTypeM() == "col" and pinalty.getIndex() == x.getCol()):
                    pinalty.setValue(aCol[i])
            i+=1
    return listPinalty

#input  : mat= matrix, sIter = value of iteration for recursif, listPinalty = list pinalty
#output : calculation of the specified penalty value
def CountPinalty(mat,sIter,listPinalty,case):
    #case row
    lP = []
    i = 0
    #case row
    for pinalty in listPinalty:
        for x in mat:
            if(x[0].getRow() == pinalty.getIndex() and pinalty.getTypeM()=="row"):
                arr = []
                for v in x:
                    arr.append(v.getValue())
                mm1 = GetNMinMax(arr,sIter,"min")
                if(mm1 == 0 and case=="tvam" and len(mat) > 2):
                    sIter =+ 1
                    mm1 = GetNMinMax(arr,sIter,"min")
                mm2 = GetNMinMax(arr,sIter+1,"min")
                val = abs(mm1 - mm2)
                p = Pinalty(val,"row",pinalty.getIndex())
                lP.append(p)
                i+=1
    #case column
    tMat = Transpose(mat)
    i = 0
    for pinalty in listPinalty:
        for x in tMat:
            if(x[0].getCol() == pinalty.getIndex() and pinalty.getTypeM() == "col"):
                arr = [] 
                for v in x:
                    arr.append(v.getValue())
                mm1 = GetNMinMax(arr,sIter,"min")
                if(mm1 == 0 and case=="tvam" and len(mat) > 2):
                    sIter =+ 1
                    mm1 = GetNMinMax(arr,sIter,"min")
                mm2 = GetNMinMax(arr,sIter+1,"min")
                val = abs(mm1 - mm2)
                p = Pinalty(val,"col",pinalty.getIndex())
                lP.append(p)
                i+=1
    return lP

#input  : listPinalty = list pinalty, mat = matrix, sIter = iteration for recurtion
#output : key pinalty for reduction matrix
def GetPinalty(listPinalty,mat,sIter,case):
    tMax = listPinalty[0].getValue()
    same = 0
    pMax = listPinalty[0]
    nListPinalty = []
    fp = []
    
    for pinalty in listPinalty:
        if(tMax < pinalty.getValue() ):
            tMax = pinalty.getValue()
            pMax = pinalty
    for pinalty in listPinalty:
        if(pMax.getValue() == pinalty.getValue() and pMax != pinalty):
            same += 1
            fp.append(pinalty)
    nListPinalty.append(pMax)
    # if more than 2 max same
    if(same != 0):
        for x in fp:
            nListPinalty.append(x)
    if(len(nListPinalty) > 1):
        lp = CountPinalty(mat,sIter,nListPinalty,case)
        sIter += 1
        if(len(mat) == sIter+1):
            keyP = nListPinalty[0]
        else:
            keyP = GetPinalty(lp,mat,sIter,case)
    else:
        keyP = nListPinalty[0]
    return keyP   

#input  : mat= matrix, key= penalty value submitted as a reference to delete the matrix, tM= type of Method (max/min)
#output : mat = matrix, temp = value of element, pinalty = pinalty
def ReductionMatrix(mat,key,tM):
    if(key.getTypeM()=="row"):
        for x in mat:
            if(x[0].getRow()==key.getIndex()):
                temp = x[0]
                break
        for elm in x:
            if(tM == "min"):
                if(temp.getValue() > elm.getValue()):
                    temp = elm
            else:
                if(temp.getValue() < elm.getValue()):
                    temp = elm
        mat,de = DelRow(mat,key.getIndex())
        mat,de = DelCol(mat,temp.getCol())
        pinalty = Pinalty(0,"col",temp.getCol())
    else:
        i = 0
        for y in mat[0]:
            if(y.getCol()==key.getIndex()):
                temp = y
                break
            i += 1
        for x in mat:
            elm = x[i]
            if(tM == "min"):
                if(temp.getValue() > elm.getValue()):
                    temp = elm
            else:
                if(temp.getValue() < elm.getValue()):
                    temp = elm
        mat,de = DelCol(mat,key.getIndex())
        mat,de = DelRow(mat,temp.getRow())
        pinalty = Pinalty(0,"row",temp.getRow())
    return mat,temp,pinalty



#input  : mat= matrix,tM = type of method (min/max)
#output : matrix
def FirstCountTvam(mat,tM):
    nMat = mat
    aMat = MatrixToArray(nMat)
    print("\n")
    for i in range(2):
        l=[]
        if(i>0):
            nMat = Transpose(nMat)
            aMat = MatrixToArray(nMat)
        for arr in aMat:
            if(tM == "min"):
                val = min(arr)
            else:
                if(i > 0):
                    val = min(arr)
                else:
                    val = max(arr)
            l.append(val)
        j = 0
        for arr in nMat:
            for x in arr:
                x.setValue(abs(x.getValue()-l[j]))
            j+=1
    nMat = Transpose(nMat)
    return nMat

#input  : result = list Element,mat = matrix
#output : list Element
def ConvertValueResultTvam(listResult,mat):
    newLResult = []
    for aRow in mat:
        for val in aRow:
            for x in listResult:
                if(x.getRow() == val.getRow() and x.getCol() == val.getCol()):
                    newLResult.append(val)
    return newLResult

#input  : arr = array, i = position value, tVal = (min/max)
#output : minimum/maximum value by index i
def GetNMinMax(arr,i,tVal):
    if(tVal == "min"):
        aSort = sorted(arr)
    else:
        aSort = sorted(arr,reverse=True)
    return aSort[i]

#input  : object matrix
def PrintMatrix(mat):
    lenValue = 20
    for elmRow in mat:
        for elmCol in elmRow:
            print(elmCol.getValue(),end='')
            i = len(str(elmCol.getValue()))
            while(i < lenValue):
                print(end=' ')
                i+=1
        print()

#input  : list value of element matrix
def PrintResult(list1):
    sum = 0
    print("_____________________________________________")
    print("Hasil Pengalokasian :")
    for x in list1:
        sum += x.getValue()
        print("     Baris : "+str(x.getRow()+1) +" --> Kolom : "+str(x.getCol()+1)+" Nilai : "+str(x.getValue()))
    print("_____________________________________________")
    print("Total Iterasi : "+str(len(list1)))
    print("_____________________________________________")
    print("Solusi Optimal : "+str(sum))


#********************** Method *******************/
#input : mat=matrix, tM = type of Method (min/max)
def Tvam(mat1,tM):
    mat = mat1
    mat1 = MatrixToArray(mat)
    mat1 = CreateMatrix(mat1)
    mat = FirstCountTvam(mat,tM)
    lp = CountAllPinalty(mat,0,tM,"tvam")
    i = 0
    l = []
    tP="min"
    print("****************MATRIKS AWAL*****************")
    PrintMatrix(mat)
    print("_____________________________________________")
    print("****************MULAI ITERASI****************")
    while True:
        key = GetPinalty(lp,mat,0,"tvam")
        lp = PopListPinalty(lp,key)
        mat,val,key = ReductionMatrix(mat,key,tP)
        lp = PopListPinalty(lp,key)
        if(len(mat) !=1):
            lp = UpdatePinalty(mat,lp,tP)
        print("_____________________________________________")
        print("******************ITERASI "+str(i+1)+"******************")
        PrintMatrix(mat)
        l.append(val)
        if(len(mat) == 1):
            if (len(mat[0]) == 1):
                l.append(mat[0][0])
            else:
                arr = []
                for x in mat[0]:
                    arr.append(x.getValue())
                l.append(mat[0][arr.index(min(arr))])
            break
        if(len(mat[0])==1):
            arr = []
            for y in mat:
                for x in y:
                    arr.append(x.getValue())
            if(tP == "min"):
                l.append(mat[arr.index(min(arr))][0])
            else:             
                l.append(mat[arr.index(max(arr))][0])
            break
        i += 1
    print("***************ITERASI SELESAI***************")
    l = ConvertValueResultTvam(l,mat1)
    return l


def BubbleSortMatrix(arr2): 
    arr = arr2
    n = len(arr) 
    # Traverse through all array elements 
    for i in range(n): 
        # Last i elements are already in place 
        for j in range(0, n-i-1): 
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
            if arr[j].getValue() > arr[j+1].getValue() : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
    return arr


if __name__ == "__main__":
    
    while True:
        print("PENYELESAIAN MASALAH PENUGASAN DENGAN MENGGUNAKAN TRANSPORTATION VOGEL’S APPROXIMATION METHOD(TVAM)")
        print("Pilih Metode dan Kasus : ")
        print("1.Kasus Minimasi")
        print("2.Kasus Maksimasi")
        choose  = int(input("Pilih : \n"))
        arr = ReadFile()
        nm = input("pilih : \n")
        
        if(int(nm) == len(arr)):
            n,m = input("masukan jumlah baris dan kolom *gunakan spasi untuk memisahkan nilai*\n").split()
            s,e = input("masukan nilai minimum dan maksimum\n").split()
            n = int(n)
            m = int(m)
            s = int(s)
            e = int(e)
            if(s > e):
                print("tidak memenuhi persyaratan karena input nilai minimum lebih besar dari maksimum *gunakan spasi untuk memisahkan nilai*")
                break
            mat = CreateRandomMatrix(n,m,s,e)
        else:
            mat = FileToMatrix(arr[int(nm)-1])
            mat = CreateMatrix(mat)
        if(choose == 1):
            result = Tvam(mat,"min")
        elif(choose == 2):
            result = Tvam(mat,"max")
        else:
            print("Tidak ada dalam pilihan")
            break
        
        PrintResult(result)
        loop = str(input("\n\nIngin Melakukan perhitungan lagi Y/N\n"))
        if(loop.lower()=='n'):
            break
        print("\n\n\n")
    
