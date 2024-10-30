### Exercise 8.1:
All the answers can be found in the file exercise8_1.md

### Exercise 8.3:

### Exercise 8.4:

### Exercise 8.5:
The changes to exercise 8.5 are in CPar.fsy, Comp.fs, CLex.fsl and Absyn.fs

In CPar.fsy:
```| Expr IFSYMBOL Expr ELSESYMBOL Expr      { IfSymbol($1, $3, $5)  }```
```%token IFSYMBOL ELSESYMBOL```

In CLex.fsl:
```| '?'             { IFSYMBOL }```
```| ':'             { ELSESYMBOL }```

In Absyn.fs:
```| IfSymbol of expr * expr * expr   (* If statements with symbols  *)```

In Comp.fs:
```
| IfSymbol(e, e1, e2) -> 
      let labelse = newLabel()
      let labend  = newLabel()
      cExpr e varEnv funEnv @ [IFZERO labelse] 
      @ cExpr e1 varEnv funEnv @ [GOTO labend]
      @ [Label labelse] @ cExpr e2 varEnv funEnv
      @ [Label labend]
```



Test for this can be seen in ex8_5.c

### Exercise 8.6:
