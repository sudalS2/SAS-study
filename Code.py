# 예제 1-1)
DATA one;
INFILE CARD DML='&$.';
INPUT a b c;
CARDS;
11&$12, 13 
2$$$22* 23
  3* 32,33 
;
RUN;

# 결과: 입력된 데이터에서 &, $, *, ,로 이루어진 &$, ,, $$$, * 등은 모두 하나의 독립적인 구분자로 사용된다.
A  B  C
11 12 13
2  22 23
3  32 33

# 예제 1-2)
## DLM 옵션
DATA scores;
  INFILE CARDS DLM=','
  INPT test1 test2 test3;
CARDS;
91,87,95
97,,92
1,1,1
;
RUN;

# 결과: 인용부호 안에 있는 문자는 구분자로 인식하지 않고, 데이터 값으로 받아들이지 않음. 
 test1 test2 test3
  91    87    95
  97    92    1

## DSD 옵션 1
DATA scores;
  INFILE CARDS DSD;
  INPT test1 test2 test3;
CARDS;
91,87,95
97,,92
1,1,1
;
RUN;

# 결과: 연속된 구분자들 사이를 결측값으로 처리
 test1 test2 test3
  91    87    95
  97    .     92
  1     1     1
  
## DSD 옵션 2
DATA topics;
  INFILE CARDS DSD;
  INPUT speaker : $1. title : $40. location $ $10.; # 포맷 수정자: :(콜론)은 고정포맷으로 데이터를 읽는 경우에 구분자까지만 변수 값을 읽도록 함.
CARDS;
Whitfield, "Looking at  Water. Looking at Life", Blue Room
Fuentes, "Life After the Ravolution", Red Room
TOWNSEND, "Peace in Our Times", Green Room
;
RUN;

# 결과
speaker                title                     location
Whitfield   Looking at  Water. Looking at Life   Blue Room
Fuentes     Life After the Ravolution            Red Room
TOWNSEND    Peace in Our Times                  Green Room

# 예제 1-3)
DATA one;
  INFILE 'a:\ex13.txt' EXPANDTABS;
  INPUT a b c;
RUN;


 
  
