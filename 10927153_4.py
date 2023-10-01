# 演算法分析機測
# 學號: 10927153 / 10927248 /10927256
# 姓名: 吳上玲 / 連翊安 / 姜美羚
# 中原大學資訊工程系


import numpy as np

def find_tree( matrix ):
    matrix = np.array(matrix)
    smatrix = np.ma.masked_equal(matrix, -1)
    #print(smatrix)
    mini = np.unravel_index(np.argmin(smatrix), smatrix.shape)
    weight = matrix[mini[0]][mini[1]]
    record = [] # 目前路徑
    record.append(mini[0])
    record.append(mini[1])
    #print(f"{mini[0]}{mini[1]}")
    while len(record) < len(matrix):
        re = []
        for i in record:
            for j in range(len(matrix[i])):
                if matrix[i][j] > 0 and j not in record:
                    re.append( (i,j) ) #紀錄可用邊位置
                    #print(f"{i}{j}")
        nums = []
        for u in re :
            nums.append(matrix[u[0]][u[1]]) #找出所有權重
        if len(nums) == 0 :
            print( "\nnot have spanning tree !\n" )
            return 0 ;
        
        value = min(nums)  # 找到權重最小值value
        index = nums.index(value)  # 找到最小值的索引( , )
        record.append(re[index][1]) #加入record
        weight = weight + value
        #print(weight)
    return weight
        
    
    

            
def count_tree(matrix):
    n = []
    ns = []
    num = 0
    for i in range(len(matrix)):
        num = 0
        n = []
        for j in range(len(matrix)): #計算個數
            if matrix[i][j] > 0 :
                num = num + 1
        for j in range(len(matrix)): #填表
            if i != j and matrix[i][j] != -1 :
                n.append(-1)
            elif i == j:
                n.append(num)
            else :
                n.append(0)
            
        ns.append(n)
    
    #計算數量
    ans = np.array(ns)
    ans = ans[1:, 1:]
    return np.linalg.det(ans)
    
    
answer = []
paths = []
while True :
    m = input("continue?(y/n)")
    if m != 'y':
        break
    
    n = []
    m = []
    matrix = []
    ans = []
    num = int(input("size:"))
    while num != 0 :
        for i in range(num) :
            n = input().split()
            n = [-1 if w == '-' or w == '0' else int(w) for w in n]
            matrix.append(n)
        #print(matrix)
            
        count = round(count_tree(matrix)) #找個數
        #print(count)
        weight = find_tree(matrix)
        #print(weight)
        ans.append( (count, weight))
        num = int(input("size:"))
        matrix = []
        answer = []
    
    case = 1 ;
    for i in ans :
        count, weight = i
        print(f"Case {case}")
        print(f"Number of Spanning Trees = {count}")
        print(f"Minimum Cost = {weight}")
        case = case + 1