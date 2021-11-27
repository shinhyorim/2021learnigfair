
score=0

print("지금부터 한국사 능력 검정 시험 연습을 시작하겠습니다.")
print("총 문항은 15문항으로, 각 문항의 배점은 10점, 6점, 4점입니다.")
print("이 퀴즈는 100점 만점으로 진행됩니다.")
print("")


print("1번 문제")
ans1=input("신석기 시대에 농경과 목축이 시작되었다. (o,x) (4점) : ")

if ans1 == "o":
    score=score+4
else :
    score=score

#print(score)

print("")
print("2번 문제")
ans2=input("고구려의 혼인 풍습에는 민며느리제가 있었다. (o,x) (6점) : ")

if ans2 == "o":
    score=score
else :
    score=score+6
#print(score)

print("")
print("3번 문제")
ans3=input("고구려 고국원앙은 불교 도입, 태학 설립 율령을 반포하여 고구려 전성기의 기틀은 마련하였다. (o,x) (6점) : ")

if ans3 == "o":
    score=score
else :
    score=score+6
#print(score)

print("")
print("4번 문제")
ans4=input("백제의 부흥 운동의 주도 인물로는 복신, 흑치상지, 도침 등이 있다. (o,x) (6점) : ")

if ans4 == "o":
    score=score+6
else :
    score=score
#print(score)

print("")
print("5번 문제")
ans5=input("고려의 광종은 쌍기의 건의로 과거제를 실시하였다. (o,x) (4점): ")

if ans5 == "o":
    score=score+4
else :
    score=score
#print(score)

print("")
print("6번 문제")
ans6=input("의천은 수선사 결사를 결성하고, 수행방법으로 정혜쌍수와 돈오점수를 주장했다. (o,x) (6점) : ")

if ans6 == "o":
    score=score
else :
    score=score+6
#print(score)

print("")
print("7번 문제")
ans7=input("사간원, 사헌부와 함께 3사로 불리고 왕의 물음에 대비하여 경연을 담당하는 조선시대 조직은?) (주관식) (10점) : ")

if ans7 == "홍문관":
    score=score+10
else :
    score=score
#print(score)

print("")
print("8번 문제")
ans8=input("조선 후기에 농사직설이 저술되었다. (o,x) (4점) : ")

if ans8 == "o":
    score=score
else :
    score=score+4

print("")
print("9번 문제")
ans9=input("임오군란 이후 맺어진 일본과의 조약으로,  일본 군대가 주둔할 수 있는 조항이 포함된 조약의 이름은? (주관식, 띄어쓰기 금지) (6점) : ")

if ans9 == "제물포조약":
    score=score+6
else :
    score=score

print("")
print("10번 문제")
ans10=input("광무개혁때 지계를 발급했다. (o,x) (4점) : ")

if ans10 == "o":
    score=score+4
else :
    score=score

print("")
print("11번 문제")
ans11=input("항일 무장 투쟁 중 청산리 전투를 이끈 인물은 김좌진 장군이다 (o,x) (4점) : ")

if ans11 == "o":
    score=score+4
else :
    score=score

print("")
print("12번 문제")
ans12=input("민족의 얼을 강조하고 조선학 운동을 추진한 인물은? (주관식) (10점) : ")

if ans12 == "정인보":
    score=score+10
else :
    score=score

print("")
print("13번 문제")
ans13=input("우리나라 최초의 민주 선거이며, 임기 2년의 국회의원 198명이 선출된 선거는 5.10 총선거이다. (o,x) (10점) : ")

if ans13 == "o":
    score=score+10
else :
    score=score

print("")
print("14번 문제")
ans14=input("허정 과도 내각 3차 개헌의 주요 내용 2가지는 대통령제, 단원제이다. (o,x) (10점) : ")

if ans14 == "x":
    score=score+10
else :
    score=score

print("")
print("15번 문제")
ans15=input("노태우 정부 시기 남북 관계를 진전시킨 활동은 남북 고위급 회담, 남북한 유엔 동시가입, 남북 기본합의서, 한반도 비핵화 공동 선언이다. (o,x) (10점) : ")

if ans15 == "o":
    score=score+10
else :
    score=score



print("")
print("당신의 점수는", score, "점 입니다.")
ex=input("해설을 보시겠습니까? (y/n) : ")
print("")

if ex == "y" :
    if score == 100:
        print("당신의 점수는 100점이므로 해설 없이 시험을 끝내겠습니다. 수고하셨습니다.")
    else :
        if ans1 == "x":
            print("문제 1번 해설 : 신석기 시대에는 농경과 목축이 시작되었고, 움집을 지어 정착생활을 시작했습니다.")
            print("")
        if ans2 == "o":
            print("문제 2번 해설 : 고구려의 혼인 풍습은 서옥제이며, 민며느리제는 옥저의 혼인 풍습입니다.")
            print("")
        if ans3 == "o":
            print("문제 3번 해설 : 불교 도입, 태학 설립, 율령을 반포하여 고구려 전성기의 기틀은 마련한 왕은 소수림왕입니다.")
            print("")
        if ans4 == "x":
            print("문제 4번 해설 : 백제의 부흥 운동은 복신, 흑치상지, 도침이, 고구려의 부흥 운동은 검모잠, 안승, 고연무가 주도했습니다.")
            print("")
        if ans5 == "x":
            print("문제 5번 해설 : 광종은 과거제를 실시하고, 노비안검법을 제정하였습니다.")
            print("")
        if ans6 == "o":
            print("문제 6번 해설 : 지눌은 수선사 결사를 결성하고, 수행방법으로 정혜쌍수와 돈오점수를 주장했고, 의천은 천태종을 개창하고, 교관겸수를 수행방법으로 제시했습니다.")
            print("")
        if ans7 != "홍문관":
            print("문제 7번 해설 : 3사는 사간원, 사헌부, 홍문관을 가리키고, 3사는 언론 기능을 담당했습니다. 그 중 홍문관은 궁궐 안의 책을 관리하고, 왕의 물음에 대비하여 경연을 담당했습니다.")
            print("")
        if ans8 == "o":
            print("문제 8번 해설 : 농사직설은 조선 전기 세종때 저술된 책입니다. 조선 후기에는 농사집성이 저술되었습니다.")
            print("")
        if ans9 != "제물포조약":
            print("문제 9번 해설 : 임오군란 이후 조선과 일본이 맺은 제물포 조약은 일본에 배상금 지불, 일본 공사관 경비를 위한 일본군 주둔을 혀용했습니다.")
            print("")
        if ans10 == "x":
            print("문제 10번 해설 : 광무개혁은 구본신참을 기본 방향으로 삼고, 황제권을 강화하기 위해 원수부를 설치하고, 양전 사업을 통해 지계를 발급했습니다.")
            print("")
        if ans11 == "x":
            print("문제 11번 해설 : 1920년 10월 북로 군정서를 이끌어 청산리 대첩에서 대승을 거둔 인물은 김좌진 장군입니다.")
            print("")
        if ans12 != "정인보":
            print("문제 12번 해설 : 신채호와 박은식의 민족주의 사학을 계승한 정인보는 '얼'을 강조하여 민족정신을 고취하였습니다. 1930년대에 정인보는 안재홍 등과 우리 민족의 고유한 특색과 전통을 찾아 주체성을 유지하려는 조선학 운동을 전개했습니다.")
            print("")
        if ans13 == "x":
            print("문제 13번 해설 : 1948년 5월 10일 총선거를 통해 제주도 2곳을 제외한 선거구에서 임기 2년의 국회의원 198명이 선출되었습니다.")
            print("")
        if ans14 == "o":
            print("문제 14번 해설 : 허정 과도 내각 3차 개헌의 주요 내용은 의원내각제와 양원제입니다.")
            print("")
        if ans15 == "x":
            print("문제 15번 해설 : 노태우 정부는 북한과의 관계를 진전시키기 위해 남북 고위급 회담을 열고, 동시에 유엔 가입을 하고, 한반도 비핵화 공동선언을 했습니다.")
            print("")
            print("수고하셨습니다.")
    
else :
    print("수고하셨습니다.")
