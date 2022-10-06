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
## DLM=',' 
DATA scores;
  INFILE CARDS DLM=','
  INPT test1 test2 test3;
CARDS;
91,87,95
97,,92
1,1,1
;
RUN;

# 결과
 test1 test2 test3
  91    87    95
  97    92    1

DATA scores;
  INFILE CARDS DSD;
  INPT test1 test2 test3;
CARDS;
91,87,95
97,,92
1,1,1
;
RUN;

  
