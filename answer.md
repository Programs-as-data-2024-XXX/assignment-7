### Exercise 8.1:
All the answers can be found in the file exercise8_1.md

### Exercise 8.3:
The changes made for this exercise can be found in: 
- Absyn.fs on line 27-28

```| PreInc of access```

```| PreDec of access```
- CLex.fsl on line 55-56

```| "++" { PREINC }```

```| "--" { PREDEC }```
- Comp.fs on line 170-171

```| PreInc(acc)    -> cAccess acc varEnv funEnv  @ [DUP; LDI; CSTI 1; ADD; STI]```

```| PreDec(acc)    -> cAccess acc varEnv funEnv  @ [DUP; LDI; CSTI 1; SUB; STI] ```

- CPar.fsy on line 19 and 137-138

```%token PREINC PREDEC PLUS MINUS TIMES DIV MOD```

```| PREINC Access{ PreInc($2) }```

```| PREDEC Access{ PreDec($2) }```

### Exercise 8.4:
prog1 is much faster than ex8.c, because it doesn't use any local variables, and only uses the top of the stack. Therefore it never needs to store or read from memory other than the top of the stack. 

In ex13.out we see that loops and conditionals really just interact as by jumping around the instructions with GOTOS or IF/IFN instructions.



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
Changes have been made in Absyn.fs, CLex.fsl, Comp.fs and CPar.fsy.

In CPar.fsy:
```
| SWITCH LPAR Expr RPAR LBRACE StmtM RBRACE   { Switch($3, $6)       }
;

SwitchCases:
    /* if no cases */                   { []        }
    SwitchCase                          { []        }
    SwitchCase SwitchCases              { $1 :: $2  }
;

SwitchCase:
    CASE CSTINT ELSESYMBOL Block        { Case($2, $4)         }
```

In Absyn.fs:
```
| Switch of expr * case list            (* Switch statement            *)

and case = 
  | Case of int * stmt               (* A switch case               *)
```

In CLex.fsl:
```
| "switch"  -> SWITCH
    | "case"    -> CASE
```

In Comp.fs:
```
| Switch(e, cases) ->
      let endLabel = newLabel()
      let caseLabels = List.map (fun _ -> newLabel()) cases.Tail @ [endLabel]
      let caseBody = 
        List.map2 (fun (Case(caseValue, caseStatement)) caseLabel -> 
          [DUP; CSTI caseValue; EQ; IFZERO caseLabel] @ cStmt caseStatement varEnv funEnv @ [GOTO endLabel] @ [Label caseLabel]
        ) cases caseLabels
      cExpr e varEnv funEnv @ List.concat caseBody @ [INCSP -1]
```


Test for this can be seen in ex8_6.c