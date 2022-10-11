# 예제 1-1)
## DLM 옵션 1
DATA one;
INFILE CARD DLM='&$.';
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

## DLM 옵션 2
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

# 예제 1-2)
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

# 결과: EXPANDTABS 옵션 없을 시 오류남.
a b c
1 2 3
4 5 6
7 8 9

# 예제 1-4)
## flowover 옵션
data one;
  infile cards flowover;
  input a b c;
cards;
123
45
678
9012
345
;
run;

# 결과
a b c
1 2 3
4 5 6
9 0 1
3 4 5

## missover 옵션
# 결과
a b c
1 2 3
4 5 .
6 7 8
9 0 1
3 4 5

## stopover 옵션
# 결과
a b c
1 2 3

# 예제 1-5)
## flowover 옵션
data one;
  infile 'a:\ex15.txt' flowover;
  input a 5.;
run;

# 결과
a
12233
44445

## missover 옵션
# 결과
a
.
.
.
.
55555

## truncover
# 결과
a
    1
   22
  333
 4444
55555

# 예제 1-6)
PROC SORT DATA=one;
  BY name;
RUN; -> 데이터 one을 name에 의해서 정렬

DATA TWO;
  RETAIN oldname; -> 변수 oldname을 초기값이 결측값인 변수로 유지할 것을 지정
  SET one;
  IF name = oldname THEN DELETE; -> 만약 변수 name과 oldname의 값이 같으면 그 개체를 제거
  oldname = name; -> 변수 name의 값을 변수 oldname에 저장
  DROP oldname;
RUN;
