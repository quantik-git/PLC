
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ATRIB DEC DIV DO ELIF ELSE EQUIV GEQ GT ID IF INC INTDec LCPARENT LEQ LSQBRACKET LT MOD MULT NUM OR PRINT QUOTE RCPARENT RSQBRACKET STRING SUB SUM WHILEPrograma : CorpoPrograma : Decls CorpoDecls : DeclDecls : Decls DeclDecl : INTDec IDDecl : INTDec ID ATRIB NUMCorpo : ProcProc : PrintPrint : NonFormattedNonFormatted : PRINT LCPARENT QUOTE STRING QUOTE RCPARENT'
    
_lr_action_items = {'INTDec':([0,3,5,11,12,16,],[7,7,-3,-4,-5,-6,]),'PRINT':([0,3,5,11,12,16,],[9,9,-3,-4,-5,-6,]),'$end':([1,2,4,6,8,10,19,],[0,-1,-7,-8,-9,-2,-10,]),'ID':([7,],[12,]),'LCPARENT':([9,],[13,]),'ATRIB':([12,],[14,]),'QUOTE':([13,17,],[15,18,]),'NUM':([14,],[16,]),'STRING':([15,],[17,]),'RCPARENT':([18,],[19,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Programa':([0,],[1,]),'Corpo':([0,3,],[2,10,]),'Decls':([0,],[3,]),'Proc':([0,3,],[4,4,]),'Decl':([0,3,],[5,11,]),'Print':([0,3,],[6,6,]),'NonFormatted':([0,3,],[8,8,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> Programa","S'",1,None,None,None),
  ('Programa -> Corpo','Programa',1,'p_Programa','yacc.py',6),
  ('Programa -> Decls Corpo','Programa',2,'p_Programa_Decls','yacc.py',11),
  ('Decls -> Decl','Decls',1,'p_Decls','yacc.py',15),
  ('Decls -> Decls Decl','Decls',2,'p_Decls_Recursiva','yacc.py',19),
  ('Decl -> INTDec ID','Decl',2,'p_Decl_Int','yacc.py',23),
  ('Decl -> INTDec ID ATRIB NUM','Decl',4,'p_Decl_Int_Val','yacc.py',34),
  ('Corpo -> Proc','Corpo',1,'p_Corpo','yacc.py',47),
  ('Proc -> Print','Proc',1,'p_Atrib_Print','yacc.py',61),
  ('Print -> NonFormatted','Print',1,'p_Print_NonFormatted','yacc.py',65),
  ('NonFormatted -> PRINT LCPARENT QUOTE STRING QUOTE RCPARENT','NonFormatted',6,'p_NonFormatted','yacc.py',69),
]
