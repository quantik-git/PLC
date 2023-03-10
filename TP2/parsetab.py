
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "ProgramaInitleftSUMSUBleftMULTDIVMODAND ASSERT ATRIB CALL COLON DEC DEDENT DEF DIV DO ELSE ENDMARKER EQUIV GEQ GT ID IF INC INDENT INPUT INTDec LCPARENT LCURLBRACKET LEQ LSQBRACKET LT MOD MULT NEQ NEWLINE NOT NUM OR PRINT QUOTE RCPARENT RCURLBRACKET RSQBRACKET STRING SUB SUM WHILE WSProgramaInit : Programa ENDMARKERPrograma : Corpo\n                | Decls CorpoCorpo : Proc Newline\n             | Corpo Proc Newline\n             | NewlineEmpty : Newline : NEWLINE\n               | EmptyDedent : Dedent DEDENT\n              | EmptyDecls : Decl Newline\n             | Decls Decl NewlineDecl : INTDec IDDecl : INTDec ID ATRIB NUMDecl : INTDec ID ATRIB InputDecl : INTDec ID LSQBRACKET NUM RSQBRACKET ATRIB ArrayValuesDecl : INTDec ID LSQBRACKET NUM RSQBRACKETDecl : DefDef : DEF ID COLON Newline INDENT Corpo DEDENT\n           | DEF ID COLON Newline INDENT Decls Corpo DEDENTArrayValues : LCURLBRACKET ArrayIntValues RCURLBRACKETArrayIntValues : ArrayIntValues ',' ExprArrayIntValues : ExprProc : Atrib\n            | Print\n            | If\n            | Cycle\n            | Call\n            | AssertCall : CALLAssert : ASSERT LCPARENT Cond RCPARENTIf : IF LCPARENT Cond RCPARENT COLON Newline INDENT Corpo DedentIf : IF LCPARENT Cond RCPARENT COLON Newline INDENT Corpo Dedent ELSE COLON Newline INDENT Corpo DEDENTCycle : While\n             | DoWhileDoWhile : DO COLON Newline INDENT Corpo Dedent WHILE LCPARENT Cond RCPARENT NEWLINEWhile : WHILE LCPARENT Cond RCPARENT COLON Newline INDENT Corpo DedentCond : Expr GT Expr\n            | Expr LT Expr\n            | Expr GEQ Expr\n            | Expr LEQ Expr\n            | Expr EQUIV Expr\n            | Expr NEQ Expr\n            | Expr OR Expr\n            | Expr AND ExprCond : NOT CondAtrib : ID ATRIB ExprAtrib : ID ATRIB InputAtrib : ID INC\n             | ID DECAtrib : ID LSQBRACKET Expr RSQBRACKET ATRIB ExprPrint : NonFormattedNonFormatted : PRINT LCPARENT Argument RCPARENTArgument : StringArgument : ExprExpr : Var\n            | ExprIncDecExpr : NUMExpr : Expr SUM Expr\n            | Expr SUB Expr\n            | Expr MULT Expr\n            | Expr DIV Expr\n            | Expr MOD ExprExprIncDec : ID INC\n                  | ID DECVar : IDVar : ID LSQBRACKET Expr RSQBRACKETInput : INPUT LCPARENT String RCPARENTString : QUOTE STRING QUOTEString : Empty"
    
_lr_action_items = {'NEWLINE':([0,4,5,6,7,8,9,10,11,12,13,14,15,18,19,21,22,23,30,32,33,34,35,37,38,45,46,47,50,51,52,53,54,55,62,70,71,74,75,93,95,98,99,101,102,103,104,105,108,117,119,122,123,124,127,130,131,133,134,136,138,141,142,143,145,147,148,152,153,154,156,158,],[14,14,14,-6,14,-25,-26,-27,-28,-29,-30,-8,-9,-19,-53,-35,-36,-31,14,14,-4,-12,-14,-50,-51,14,-5,-13,-67,-48,-49,-57,-58,-59,14,-15,-16,-65,-66,-32,-54,14,-18,-60,-61,-62,-63,-64,14,14,14,-68,-69,-52,14,-11,-17,14,-20,14,-10,-7,-21,-7,-22,-33,-38,154,14,-37,14,-34,]),'INTDec':([0,4,7,14,15,18,32,34,35,47,70,71,99,117,123,127,131,134,142,145,],[16,16,-7,-8,-9,-19,-7,-12,-14,-13,-15,-16,-18,16,-69,16,-17,-20,-21,-22,]),'ID':([0,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,19,21,22,23,25,30,31,32,33,34,35,36,37,38,39,40,41,43,44,46,47,50,51,52,53,54,55,60,70,71,73,74,75,76,77,78,79,80,84,85,86,87,88,89,90,91,93,95,98,99,101,102,103,104,105,107,117,120,122,123,124,126,127,130,131,132,133,134,135,136,138,141,142,143,144,145,146,147,148,154,156,157,158,],[17,17,17,-7,-6,-7,-25,-26,-27,-28,-29,-30,-8,-9,35,-19,-53,-35,-36,-31,42,-7,17,-7,-4,-12,-14,50,-50,-51,50,50,50,50,50,-5,-13,-67,-48,-49,-57,-58,-59,50,-15,-16,50,-65,-66,50,50,50,50,50,50,50,50,50,50,50,50,50,-32,-54,17,-18,-60,-61,-62,-63,-64,50,17,17,-68,-69,-52,17,17,-11,-17,50,17,-20,17,17,-10,17,-21,17,50,-22,50,-33,-38,-37,17,17,-34,]),'IF':([0,3,4,5,6,7,8,9,10,11,12,13,14,15,18,19,21,22,23,30,31,32,33,34,35,37,38,46,47,50,51,52,53,54,55,70,71,74,75,93,95,98,99,101,102,103,104,105,117,120,122,123,124,126,127,130,131,133,134,135,136,138,141,142,143,145,147,148,154,156,157,158,],[20,20,20,-7,-6,-7,-25,-26,-27,-28,-29,-30,-8,-9,-19,-53,-35,-36,-31,-7,20,-7,-4,-12,-14,-50,-51,-5,-13,-67,-48,-49,-57,-58,-59,-15,-16,-65,-66,-32,-54,20,-18,-60,-61,-62,-63,-64,20,20,-68,-69,-52,20,20,-11,-17,20,-20,20,20,-10,20,-21,20,-22,-33,-38,-37,20,20,-34,]),'CALL':([0,3,4,5,6,7,8,9,10,11,12,13,14,15,18,19,21,22,23,30,31,32,33,34,35,37,38,46,47,50,51,52,53,54,55,70,71,74,75,93,95,98,99,101,102,103,104,105,117,120,122,123,124,126,127,130,131,133,134,135,136,138,141,142,143,145,147,148,154,156,157,158,],[23,23,23,-7,-6,-7,-25,-26,-27,-28,-29,-30,-8,-9,-19,-53,-35,-36,-31,-7,23,-7,-4,-12,-14,-50,-51,-5,-13,-67,-48,-49,-57,-58,-59,-15,-16,-65,-66,-32,-54,23,-18,-60,-61,-62,-63,-64,23,23,-68,-69,-52,23,23,-11,-17,23,-20,23,23,-10,23,-21,23,-22,-33,-38,-37,23,23,-34,]),'ASSERT':([0,3,4,5,6,7,8,9,10,11,12,13,14,15,18,19,21,22,23,30,31,32,33,34,35,37,38,46,47,50,51,52,53,54,55,70,71,74,75,93,95,98,99,101,102,103,104,105,117,120,122,123,124,126,127,130,131,133,134,135,136,138,141,142,143,145,147,148,154,156,157,158,],[24,24,24,-7,-6,-7,-25,-26,-27,-28,-29,-30,-8,-9,-19,-53,-35,-36,-31,-7,24,-7,-4,-12,-14,-50,-51,-5,-13,-67,-48,-49,-57,-58,-59,-15,-16,-65,-66,-32,-54,24,-18,-60,-61,-62,-63,-64,24,24,-68,-69,-52,24,24,-11,-17,24,-20,24,24,-10,24,-21,24,-22,-33,-38,-37,24,24,-34,]),'PRINT':([0,3,4,5,6,7,8,9,10,11,12,13,14,15,18,19,21,22,23,30,31,32,33,34,35,37,38,46,47,50,51,52,53,54,55,70,71,74,75,93,95,98,99,101,102,103,104,105,117,120,122,123,124,126,127,130,131,133,134,135,136,138,141,142,143,145,147,148,154,156,157,158,],[26,26,26,-7,-6,-7,-25,-26,-27,-28,-29,-30,-8,-9,-19,-53,-35,-36,-31,-7,26,-7,-4,-12,-14,-50,-51,-5,-13,-67,-48,-49,-57,-58,-59,-15,-16,-65,-66,-32,-54,26,-18,-60,-61,-62,-63,-64,26,26,-68,-69,-52,26,26,-11,-17,26,-20,26,26,-10,26,-21,26,-22,-33,-38,-37,26,26,-34,]),'WHILE':([0,3,4,5,6,7,8,9,10,11,12,13,14,15,18,19,21,22,23,30,31,32,33,34,35,37,38,46,47,50,51,52,53,54,55,70,71,74,75,93,95,98,99,101,102,103,104,105,117,120,122,123,124,126,127,129,130,131,133,134,135,136,138,141,142,143,145,147,148,154,156,157,158,],[27,27,27,-7,-6,-7,-25,-26,-27,-28,-29,-30,-8,-9,-19,-53,-35,-36,-31,-7,27,-7,-4,-12,-14,-50,-51,-5,-13,-67,-48,-49,-57,-58,-59,-15,-16,-65,-66,-32,-54,27,-18,-60,-61,-62,-63,-64,27,27,-68,-69,-52,27,27,137,-11,-17,27,-20,27,27,-10,27,-21,27,-22,-33,-38,-37,27,27,-34,]),'DO':([0,3,4,5,6,7,8,9,10,11,12,13,14,15,18,19,21,22,23,30,31,32,33,34,35,37,38,46,47,50,51,52,53,54,55,70,71,74,75,93,95,98,99,101,102,103,104,105,117,120,122,123,124,126,127,130,131,133,134,135,136,138,141,142,143,145,147,148,154,156,157,158,],[28,28,28,-7,-6,-7,-25,-26,-27,-28,-29,-30,-8,-9,-19,-53,-35,-36,-31,-7,28,-7,-4,-12,-14,-50,-51,-5,-13,-67,-48,-49,-57,-58,-59,-15,-16,-65,-66,-32,-54,28,-18,-60,-61,-62,-63,-64,28,28,-68,-69,-52,28,28,-11,-17,28,-20,28,28,-10,28,-21,28,-22,-33,-38,-37,28,28,-34,]),'ENDMARKER':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,18,19,21,22,23,30,31,32,33,34,35,37,38,46,47,50,51,52,53,54,55,70,71,74,75,93,95,99,101,102,103,104,105,122,123,124,130,131,133,134,136,138,141,142,143,145,147,148,154,158,],[-7,29,-2,-7,-7,-6,-7,-25,-26,-27,-28,-29,-30,-8,-9,-19,-53,-35,-36,-31,-7,-3,-7,-4,-12,-14,-50,-51,-5,-13,-67,-48,-49,-57,-58,-59,-15,-16,-65,-66,-32,-54,-18,-60,-61,-62,-63,-64,-68,-69,-52,-11,-17,-7,-20,-7,-10,-7,-21,-7,-22,-33,-38,-37,-34,]),'DEF':([0,4,7,14,15,18,32,34,35,47,70,71,99,117,123,127,131,134,142,145,],[25,25,-7,-8,-9,-19,-7,-12,-14,-13,-15,-16,-18,25,-69,25,-17,-20,-21,-22,]),'$end':([1,29,],[0,-1,]),'DEDENT':([5,6,7,8,9,10,11,12,13,14,15,18,19,21,22,23,30,32,33,34,35,37,38,46,47,50,51,52,53,54,55,70,71,74,75,93,95,98,99,101,102,103,104,105,117,120,122,123,124,126,127,129,130,131,133,134,135,136,138,141,142,143,145,147,148,154,156,157,158,],[-7,-6,-7,-25,-26,-27,-28,-29,-30,-8,-9,-19,-53,-35,-36,-31,-7,-7,-4,-12,-14,-50,-51,-5,-13,-67,-48,-49,-57,-58,-59,-15,-16,-65,-66,-32,-54,-7,-18,-60,-61,-62,-63,-64,-7,-7,-68,-69,-52,134,-7,138,-11,-17,-7,-20,142,-7,-10,-7,-21,-7,-22,138,138,-37,-7,158,-34,]),'ELSE':([5,6,8,9,10,11,12,13,14,15,19,21,22,23,30,33,37,38,46,50,51,52,53,54,55,74,75,93,95,101,102,103,104,105,122,123,124,130,133,136,138,141,143,147,148,154,158,],[-7,-6,-25,-26,-27,-28,-29,-30,-8,-9,-53,-35,-36,-31,-7,-4,-50,-51,-5,-67,-48,-49,-57,-58,-59,-65,-66,-32,-54,-60,-61,-62,-63,-64,-68,-69,-52,-11,-7,-7,-10,-7,-7,151,-38,-37,-34,]),'INDENT':([14,15,45,62,69,94,108,119,125,128,153,155,],[-8,-9,-7,-7,98,117,-7,-7,133,136,-7,156,]),'ATRIB':([17,35,82,99,],[36,48,107,121,]),'INC':([17,50,],[37,74,]),'DEC':([17,50,],[38,75,]),'LSQBRACKET':([17,35,50,],[39,49,73,]),'LCPARENT':([20,24,26,27,56,137,],[40,41,43,44,81,144,]),'COLON':([28,42,83,97,151,],[45,62,108,119,153,]),'NUM':([36,39,40,41,43,44,48,49,60,73,76,77,78,79,80,84,85,86,87,88,89,90,91,107,132,144,146,],[55,55,55,55,55,55,70,72,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,]),'INPUT':([36,48,],[56,56,]),'NOT':([40,41,44,60,144,],[60,60,60,60,60,]),'QUOTE':([43,81,96,],[66,66,118,]),'RCPARENT':([43,50,53,54,55,58,61,63,64,65,67,68,74,75,81,92,101,102,103,104,105,106,109,110,111,112,113,114,115,116,118,122,149,],[-7,-67,-57,-58,-59,83,93,95,-55,-56,-71,97,-65,-66,-7,-47,-60,-61,-62,-63,-64,123,-39,-40,-41,-42,-43,-44,-45,-46,-70,-68,152,]),'SUM':([50,51,53,54,55,57,59,65,74,75,100,101,102,103,104,105,109,110,111,112,113,114,115,116,122,124,140,150,],[-67,76,-57,-58,-59,76,76,76,-65,-66,76,-60,-61,-62,-63,-64,76,76,76,76,76,76,76,76,-68,76,76,76,]),'SUB':([50,51,53,54,55,57,59,65,74,75,100,101,102,103,104,105,109,110,111,112,113,114,115,116,122,124,140,150,],[-67,77,-57,-58,-59,77,77,77,-65,-66,77,-60,-61,-62,-63,-64,77,77,77,77,77,77,77,77,-68,77,77,77,]),'MULT':([50,51,53,54,55,57,59,65,74,75,100,101,102,103,104,105,109,110,111,112,113,114,115,116,122,124,140,150,],[-67,78,-57,-58,-59,78,78,78,-65,-66,78,78,78,-62,-63,-64,78,78,78,78,78,78,78,78,-68,78,78,78,]),'DIV':([50,51,53,54,55,57,59,65,74,75,100,101,102,103,104,105,109,110,111,112,113,114,115,116,122,124,140,150,],[-67,79,-57,-58,-59,79,79,79,-65,-66,79,79,79,-62,-63,-64,79,79,79,79,79,79,79,79,-68,79,79,79,]),'MOD':([50,51,53,54,55,57,59,65,74,75,100,101,102,103,104,105,109,110,111,112,113,114,115,116,122,124,140,150,],[-67,80,-57,-58,-59,80,80,80,-65,-66,80,80,80,-62,-63,-64,80,80,80,80,80,80,80,80,-68,80,80,80,]),'RSQBRACKET':([50,53,54,55,57,72,74,75,100,101,102,103,104,105,122,],[-67,-57,-58,-59,82,99,-65,-66,122,-60,-61,-62,-63,-64,-68,]),'GT':([50,53,54,55,59,74,75,101,102,103,104,105,122,],[-67,-57,-58,-59,84,-65,-66,-60,-61,-62,-63,-64,-68,]),'LT':([50,53,54,55,59,74,75,101,102,103,104,105,122,],[-67,-57,-58,-59,85,-65,-66,-60,-61,-62,-63,-64,-68,]),'GEQ':([50,53,54,55,59,74,75,101,102,103,104,105,122,],[-67,-57,-58,-59,86,-65,-66,-60,-61,-62,-63,-64,-68,]),'LEQ':([50,53,54,55,59,74,75,101,102,103,104,105,122,],[-67,-57,-58,-59,87,-65,-66,-60,-61,-62,-63,-64,-68,]),'EQUIV':([50,53,54,55,59,74,75,101,102,103,104,105,122,],[-67,-57,-58,-59,88,-65,-66,-60,-61,-62,-63,-64,-68,]),'NEQ':([50,53,54,55,59,74,75,101,102,103,104,105,122,],[-67,-57,-58,-59,89,-65,-66,-60,-61,-62,-63,-64,-68,]),'OR':([50,53,54,55,59,74,75,101,102,103,104,105,122,],[-67,-57,-58,-59,90,-65,-66,-60,-61,-62,-63,-64,-68,]),'AND':([50,53,54,55,59,74,75,101,102,103,104,105,122,],[-67,-57,-58,-59,91,-65,-66,-60,-61,-62,-63,-64,-68,]),'RCURLBRACKET':([50,53,54,55,74,75,101,102,103,104,105,122,139,140,150,],[-67,-57,-58,-59,-65,-66,-60,-61,-62,-63,-64,-68,145,-24,-23,]),',':([50,53,54,55,74,75,101,102,103,104,105,122,139,140,150,],[-67,-57,-58,-59,-65,-66,-60,-61,-62,-63,-64,-68,146,-24,-23,]),'STRING':([66,],[96,]),'LCURLBRACKET':([121,],[132,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'ProgramaInit':([0,],[1,]),'Programa':([0,],[2,]),'Corpo':([0,4,98,117,127,133,136,156,],[3,31,120,126,135,141,143,157,]),'Decls':([0,117,],[4,127,]),'Proc':([0,3,4,31,98,117,120,126,127,133,135,136,141,143,156,157,],[5,30,5,30,5,5,30,30,5,5,30,5,30,30,5,30,]),'Newline':([0,4,5,7,30,32,45,62,98,108,117,119,127,133,136,153,156,],[6,6,33,34,46,47,69,94,6,125,6,128,6,6,6,155,6,]),'Decl':([0,4,117,127,],[7,32,7,32,]),'Atrib':([0,3,4,31,98,117,120,126,127,133,135,136,141,143,156,157,],[8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,]),'Print':([0,3,4,31,98,117,120,126,127,133,135,136,141,143,156,157,],[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'If':([0,3,4,31,98,117,120,126,127,133,135,136,141,143,156,157,],[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'Cycle':([0,3,4,31,98,117,120,126,127,133,135,136,141,143,156,157,],[11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'Call':([0,3,4,31,98,117,120,126,127,133,135,136,141,143,156,157,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'Assert':([0,3,4,31,98,117,120,126,127,133,135,136,141,143,156,157,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'Empty':([0,4,5,7,30,32,43,45,62,81,98,108,117,119,120,127,133,136,141,143,153,156,],[15,15,15,15,15,15,67,15,15,67,15,15,15,15,130,15,15,15,130,130,15,15,]),'Def':([0,4,117,127,],[18,18,18,18,]),'NonFormatted':([0,3,4,31,98,117,120,126,127,133,135,136,141,143,156,157,],[19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,]),'While':([0,3,4,31,98,117,120,126,127,133,135,136,141,143,156,157,],[21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,]),'DoWhile':([0,3,4,31,98,117,120,126,127,133,135,136,141,143,156,157,],[22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,]),'Expr':([36,39,40,41,43,44,60,73,76,77,78,79,80,84,85,86,87,88,89,90,91,107,132,144,146,],[51,57,59,59,65,59,59,100,101,102,103,104,105,109,110,111,112,113,114,115,116,124,140,59,150,]),'Input':([36,48,],[52,71,]),'Var':([36,39,40,41,43,44,60,73,76,77,78,79,80,84,85,86,87,88,89,90,91,107,132,144,146,],[53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,]),'ExprIncDec':([36,39,40,41,43,44,60,73,76,77,78,79,80,84,85,86,87,88,89,90,91,107,132,144,146,],[54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,]),'Cond':([40,41,44,60,144,],[58,61,68,92,149,]),'Argument':([43,],[63,]),'String':([43,81,],[64,106,]),'Dedent':([120,141,143,],[129,147,148,]),'ArrayValues':([121,],[131,]),'ArrayIntValues':([132,],[139,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> ProgramaInit","S'",1,None,None,None),
  ('ProgramaInit -> Programa ENDMARKER','ProgramaInit',2,'p_Programa_Init','yacc.py',8),
  ('Programa -> Corpo','Programa',1,'p_Programa','yacc.py',12),
  ('Programa -> Decls Corpo','Programa',2,'p_Programa','yacc.py',13),
  ('Corpo -> Proc Newline','Corpo',2,'p_Corpo','yacc.py',19),
  ('Corpo -> Corpo Proc Newline','Corpo',3,'p_Corpo','yacc.py',20),
  ('Corpo -> Newline','Corpo',1,'p_Corpo','yacc.py',21),
  ('Empty -> <empty>','Empty',0,'p_Empty','yacc.py',26),
  ('Newline -> NEWLINE','Newline',1,'p_Newline','yacc.py',31),
  ('Newline -> Empty','Newline',1,'p_Newline','yacc.py',32),
  ('Dedent -> Dedent DEDENT','Dedent',2,'p_Dedent','yacc.py',38),
  ('Dedent -> Empty','Dedent',1,'p_Dedent','yacc.py',39),
  ('Decls -> Decl Newline','Decls',2,'p_Decls','yacc.py',44),
  ('Decls -> Decls Decl Newline','Decls',3,'p_Decls','yacc.py',45),
  ('Decl -> INTDec ID','Decl',2,'p_Decl_Int','yacc.py',49),
  ('Decl -> INTDec ID ATRIB NUM','Decl',4,'p_Decl_Int_Val','yacc.py',60),
  ('Decl -> INTDec ID ATRIB Input','Decl',4,'p_Decl_Int_Input','yacc.py',71),
  ('Decl -> INTDec ID LSQBRACKET NUM RSQBRACKET ATRIB ArrayValues','Decl',7,'p_Decl_Int_Array_Val','yacc.py',82),
  ('Decl -> INTDec ID LSQBRACKET NUM RSQBRACKET','Decl',5,'p_Decl_Int_Array','yacc.py',92),
  ('Decl -> Def','Decl',1,'p_DEF','yacc.py',104),
  ('Def -> DEF ID COLON Newline INDENT Corpo DEDENT','Def',7,'p_Def','yacc.py',109),
  ('Def -> DEF ID COLON Newline INDENT Decls Corpo DEDENT','Def',8,'p_Def','yacc.py',110),
  ('ArrayValues -> LCURLBRACKET ArrayIntValues RCURLBRACKET','ArrayValues',3,'p_ArrayValues','yacc.py',118),
  ('ArrayIntValues -> ArrayIntValues , Expr','ArrayIntValues',3,'p_ArrayIntValues_Rec','yacc.py',122),
  ('ArrayIntValues -> Expr','ArrayIntValues',1,'p_ArrayIntValues','yacc.py',127),
  ('Proc -> Atrib','Proc',1,'p_Proc','yacc.py',133),
  ('Proc -> Print','Proc',1,'p_Proc','yacc.py',134),
  ('Proc -> If','Proc',1,'p_Proc','yacc.py',135),
  ('Proc -> Cycle','Proc',1,'p_Proc','yacc.py',136),
  ('Proc -> Call','Proc',1,'p_Proc','yacc.py',137),
  ('Proc -> Assert','Proc',1,'p_Proc','yacc.py',138),
  ('Call -> CALL','Call',1,'p_Call','yacc.py',143),
  ('Assert -> ASSERT LCPARENT Cond RCPARENT','Assert',4,'p_Assert','yacc.py',148),
  ('If -> IF LCPARENT Cond RCPARENT COLON Newline INDENT Corpo Dedent','If',9,'p_If','yacc.py',155),
  ('If -> IF LCPARENT Cond RCPARENT COLON Newline INDENT Corpo Dedent ELSE COLON Newline INDENT Corpo DEDENT','If',15,'p_If_Else','yacc.py',160),
  ('Cycle -> While','Cycle',1,'p_Cycle','yacc.py',166),
  ('Cycle -> DoWhile','Cycle',1,'p_Cycle','yacc.py',167),
  ('DoWhile -> DO COLON Newline INDENT Corpo Dedent WHILE LCPARENT Cond RCPARENT NEWLINE','DoWhile',11,'p_Do_While','yacc.py',171),
  ('While -> WHILE LCPARENT Cond RCPARENT COLON Newline INDENT Corpo Dedent','While',9,'p_While','yacc.py',176),
  ('Cond -> Expr GT Expr','Cond',3,'p_Cond','yacc.py',193),
  ('Cond -> Expr LT Expr','Cond',3,'p_Cond','yacc.py',194),
  ('Cond -> Expr GEQ Expr','Cond',3,'p_Cond','yacc.py',195),
  ('Cond -> Expr LEQ Expr','Cond',3,'p_Cond','yacc.py',196),
  ('Cond -> Expr EQUIV Expr','Cond',3,'p_Cond','yacc.py',197),
  ('Cond -> Expr NEQ Expr','Cond',3,'p_Cond','yacc.py',198),
  ('Cond -> Expr OR Expr','Cond',3,'p_Cond','yacc.py',199),
  ('Cond -> Expr AND Expr','Cond',3,'p_Cond','yacc.py',200),
  ('Cond -> NOT Cond','Cond',2,'p_Cond_NOT','yacc.py',204),
  ('Atrib -> ID ATRIB Expr','Atrib',3,'p_Atrib_Expr','yacc.py',209),
  ('Atrib -> ID ATRIB Input','Atrib',3,'p_Atrib_Input','yacc.py',217),
  ('Atrib -> ID INC','Atrib',2,'p_Atrib_INC_DEC','yacc.py',225),
  ('Atrib -> ID DEC','Atrib',2,'p_Atrib_INC_DEC','yacc.py',226),
  ('Atrib -> ID LSQBRACKET Expr RSQBRACKET ATRIB Expr','Atrib',6,'p_Atrib_Array','yacc.py',232),
  ('Print -> NonFormatted','Print',1,'p_Print_NonFormatted','yacc.py',245),
  ('NonFormatted -> PRINT LCPARENT Argument RCPARENT','NonFormatted',4,'p_NonFormatted','yacc.py',249),
  ('Argument -> String','Argument',1,'p_Argument_String','yacc.py',253),
  ('Argument -> Expr','Argument',1,'p_Argument_Expr','yacc.py',257),
  ('Expr -> Var','Expr',1,'p_Expr_Var_Inc','yacc.py',262),
  ('Expr -> ExprIncDec','Expr',1,'p_Expr_Var_Inc','yacc.py',263),
  ('Expr -> NUM','Expr',1,'p_Expr_Num','yacc.py',267),
  ('Expr -> Expr SUM Expr','Expr',3,'p_Expr_Arith','yacc.py',278),
  ('Expr -> Expr SUB Expr','Expr',3,'p_Expr_Arith','yacc.py',279),
  ('Expr -> Expr MULT Expr','Expr',3,'p_Expr_Arith','yacc.py',280),
  ('Expr -> Expr DIV Expr','Expr',3,'p_Expr_Arith','yacc.py',281),
  ('Expr -> Expr MOD Expr','Expr',3,'p_Expr_Arith','yacc.py',282),
  ('ExprIncDec -> ID INC','ExprIncDec',2,'p_Expr_Inc_Dec','yacc.py',286),
  ('ExprIncDec -> ID DEC','ExprIncDec',2,'p_Expr_Inc_Dec','yacc.py',287),
  ('Var -> ID','Var',1,'p_Var','yacc.py',294),
  ('Var -> ID LSQBRACKET Expr RSQBRACKET','Var',4,'p_Var_Array','yacc.py',306),
  ('Input -> INPUT LCPARENT String RCPARENT','Input',4,'p_Input','yacc.py',319),
  ('String -> QUOTE STRING QUOTE','String',3,'p_String','yacc.py',324),
  ('String -> Empty','String',1,'p_String_Empty','yacc.py',328),
]
