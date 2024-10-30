# Exercise 8.1(i)
## ex3.c
LDARGS; CALL (1, "L1"); STOP;                               ->              void main(int n)

[Label "L1"; INCSP 1; GETBP; CSTI 1; ADD; CSTI 0; STI; INCSP -1; GOTO "L3";]    ->    int i; i=0; 


[Label "L2"; GETBP; CSTI 1; ADD; LDI; PRINTI; INCSP -1; GETBP; CSTI 1; ADD; GETBP; CSTI 1; ADD; LDI; CSTI 1; ADD;STI; INCSP -1; INCSP 0; ]                                                  ->              print i; i=i+1;


[Label "L3"; GETBP; CSTI 1; ADD; LDI; GETBP; CSTI 0;ADD; LDI; LT; IFNZRO "L2"; INCSP -1; RET 0]         -> while (i < n)

## ex5.c
LDARGS; CALL (1, "L1"); STOP;                               ->              void main(int n)

Label "L1"; INCSP 1; GETBP; CSTI 1; ADD;                    ->              int r; 

GETBP; CSTI 0; ADD; LDI; STI; INCSP -1;                     ->              r = n;

INCSP 1; GETBP; CSTI 0; ADD; LDI; GETBP; CSTI 2; ADD;       ->              int r;

CALL (2, "L2"); INCSP -1; GETBP; CSTI 2; ADD;               ->              square(n, &r);

LDI; PRINTI; INCSP -1; INCSP -1; GETBP; CSTI 1; ADD;        ->              print r;

LDI; PRINTI; INCSP -1; INCSP -1; RET 0;                     ->              print r;


Label "L2"; GETBP; CSTI 1; ADD; LDI; GETBP; CSTI 0; ADD; LDI; GETBP; CSTI 0; ADD; LDI; MUL; STI; INCSP -1; INCSP 0; RET 1   -> *rp = i * i;

# Exercise 8.1(ii)
## Explanation of stack trace
In the beginning the stack is empty `[ ]`, then we call opcode 0, I.e. `LDARGS`.  Which will load from arguments, and set up the stack. On top of the stack is now a `4`, this is the value loaded from the argument. After this instruction, we have a CALL, setting up a return address (4) (this is the offset in the program to the `STOP` opcode), then setting up a base bointer -999.  We push the argument to the top of the stack since that's given as an argument to call `CALL 1 <-`, I.e. take one argument from the top of the stack.

We increment the stack pointer by one to allocate place for a local variable. Then we get the base pointer, and then add the integer constant 1 to the top of the stack. 

Then we perform an add `2 + 1` and store the result on the top of the stack, so we now have `4 -999 4 0 3`. 

This value is used as a pointer to a value on the stack, so when LDI is called it looks at the 3rd stack value, which is 0, and the top of the stack is then set to 0. Afterwards we do a GETBP, and add 2 with 0, and look at that value, i.e. the 2nd stack value, which is 4. Then it does a less than comparing the two values on the top of the stack, the value on top of the stack is larger than the one just below, and this returns a 1. We then get the offset of the current accumulator, i.e. the one at stack offset 3 (zero-indexing) from the bottom, and print it. This logic is then continuing until the IFNZRO at PC 54 returns 0, and the program call returns and hits the STOP. 

```
[ ]{0: LDARGS}
[ 4 ]{1: CALL 1 5}
[ 4 -999 4 ]{5: INCSP 1}
[ 4 -999 4 0 ]{7: GETBP}
[ 4 -999 4 0 2 ]{8: CSTI 1}
[ 4 -999 4 0 2 1 ]{10: ADD}
[ 4 -999 4 0 3 ]{11: CSTI 0}
[ 4 -999 4 0 3 0 ]{13: STI}
[ 4 -999 4 0 0 ]{14: INCSP -1}
[ 4 -999 4 0 ]{16: GOTO 43}
[ 4 -999 4 0 ]{43: GETBP}
[ 4 -999 4 0 2 ]{44: CSTI 1}
[ 4 -999 4 0 2 1 ]{46: ADD}
[ 4 -999 4 0 3 ]{47: LDI}
[ 4 -999 4 0 0 ]{48: GETBP}
[ 4 -999 4 0 0 2 ]{49: CSTI 0}
[ 4 -999 4 0 0 2 0 ]{51: ADD}
[ 4 -999 4 0 0 2 ]{52: LDI}
[ 4 -999 4 0 0 4 ]{53: LT}
[ 4 -999 4 0 1 ]{54: IFNZRO 18}
[ 4 -999 4 0 ]{18: GETBP}
[ 4 -999 4 0 2 ]{19: CSTI 1}
[ 4 -999 4 0 2 1 ]{21: ADD}
[ 4 -999 4 0 3 ]{22: LDI}
[ 4 -999 4 0 0 ]{23: PRINTI}
0 [ 4 -999 4 0 0 ]{24: INCSP -1}
```


Else we increment our local variable which is seen below:
```
[ 4 -999 4 0 ]{26: GETBP}
[ 4 -999 4 0 2 ]{27: CSTI 1}
[ 4 -999 4 0 2 1 ]{29: ADD}
[ 4 -999 4 0 3 ]{30: GETBP}
[ 4 -999 4 0 3 2 ]{31: CSTI 1}
[ 4 -999 4 0 3 2 1 ]{33: ADD}
[ 4 -999 4 0 3 3 ]{34: LDI}
[ 4 -999 4 0 3 0 ]{35: CSTI 1}
[ 4 -999 4 0 3 0 1 ]{37: ADD}
[ 4 -999 4 0 3 1 ]{38: STI}
[ 4 -999 4 1 1 ]{39: INCSP -1}
[ 4 -999 4 1 ]{41: INCSP 0}
```
The local variable at BP is incremented to 1, because we're counting our variable `i` up, until it reaches `n`.

