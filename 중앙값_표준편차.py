# 중앙값
import random
import statistics

def median() :
    values = []
    print("데이터가 홀수인 경우")
    for i in range( 5 ) :
        values.append( random.randint(10, 50) )
    
    answer = int(input("중앙값은 " + str(values) + " : "))
    if int(statistics.median( values )) == answer :
        print("정답입니다", int(statistics.median( values )))
    else :
        print("틀렸습니다", int(statistics.median( values )))

    values = []
    print("데이터가 짝수인 경우") # 중앙값 2개 더하고, 나누기 2
    for i in range( 6 ) :
        values.append( random.randint(10, 50) )
    
    answer = int(input("중앙값은 " + str(values) + " : "))
    if int(statistics.median( values )) == answer :
        print("정답입니다", int(statistics.median( values )))
    else :
        print("틀렸습니다", int(statistics.median( values )))

# 표준편차
import math
import numpy as np
def standard_deviation() :
    values = []
    for i in range( 5 ) :
        values.append( random.randint(10, 50) )
    
    print("표준편차로 계산할 값", values)

    e = 0
    for i in range( 5 ) :
        e += math.pow( values[i] - statistics.mean( values ), 2 )
        print(i+1, "번째 값 :", values[i] - statistics.mean( values ))
    
    print( "표준편차 파이썬 복잡하게 구현 : ", math.sqrt( (e/5) ) ) 
    print( "표준편차 파이썬 더쉽게 구현 : ", np.std(values) )

if __name__ == "__main__":
    # median()
    standard_deviation()
