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
