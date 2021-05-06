#(2020 카카오 인턴)키패드 누르기
def solution(numbers, hand):
    answer=""
    pad = {1:(0,0),2:(0,1),3:(0,2),
            4:(1,0),5:(1,1),6:(1,2),
            7:(2,0),8:(2,1),9:(2,2),
            -1:(3,0),0:(3,1),-2:(3,2)
            }
    cL, cR, check = pad[-1], pad[-2], ()
    for i in numbers:
        if i in (1,4,7):
            answer +="L"
            cL = pad[i]
            continue
        if i in (3,6,9):
            answer += "R"
            cR = pad[i]
            continue
        else:
            check=pad[i]
            print(cL)
            print(cR)
            print(check)
            if abs(cL[0]-check[0])+abs(cL[1]-check[1]) < abs(cR[0]-check[0])+abs(cR[1]-check[1]):
                answer+="L"
                cL=check
            elif abs(cL[0]-check[0])+abs(cL[1]-check[1]) > abs(cR[0]-check[0])+abs(cR[1]-check[1]):
                answer+="R"
                cR=check
            else:
                if hand=="right":
                    answer+="R"
                    cR=check
                else:
                    answer+="L"
                    cL=check
                                    
    return answer
                        

                        
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],"left")=="LRLLRRLLLRR")