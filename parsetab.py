
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ASSIGN DOT FOR ID INT LBRACE LE LPAREN NUMBER OUT PLUS PRINTLN RBRACE RPAREN SEMIprogram : declaration for_statementdeclaration : INT ID SEMIfor_statement : FOR LPAREN ID ASSIGN NUMBER SEMI ID LE NUMBER SEMI ID PLUS RPAREN LBRACE statement RBRACEstatement : OUT DOT PRINTLN LPAREN ID RPAREN SEMI'
    
_lr_action_items = {'INT':([0,],[3,]),'$end':([1,4,23,],[0,-1,-3,]),'FOR':([2,8,],[5,-2,]),'ID':([3,7,12,16,26,],[6,9,13,17,27,]),'LPAREN':([5,25,],[7,26,]),'SEMI':([6,11,15,28,],[8,12,16,29,]),'ASSIGN':([9,],[10,]),'NUMBER':([10,14,],[11,15,]),'LE':([13,],[14,]),'PLUS':([17,],[18,]),'RPAREN':([18,27,],[19,28,]),'LBRACE':([19,],[20,]),'OUT':([20,],[22,]),'RBRACE':([21,29,],[23,-4,]),'DOT':([22,],[24,]),'PRINTLN':([24,],[25,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'declaration':([0,],[2,]),'for_statement':([2,],[4,]),'statement':([20,],[21,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> declaration for_statement','program',2,'p_program','app.py',51),
  ('declaration -> INT ID SEMI','declaration',3,'p_declaration','app.py',55),
  ('for_statement -> FOR LPAREN ID ASSIGN NUMBER SEMI ID LE NUMBER SEMI ID PLUS RPAREN LBRACE statement RBRACE','for_statement',16,'p_for_statement','app.py',60),
  ('statement -> OUT DOT PRINTLN LPAREN ID RPAREN SEMI','statement',7,'p_statement','app.py',71),
]
