
# generated\parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = '2\xd8]\x959\x8d\x17\x1e?\t\xdd>K\xbdq\x02'
    
_lr_action_items = {'COLOR':([7,],[8,]),'$end':([2,3,4,8,],[-1,-2,0,-3,]),'MOTIF':([0,],[1,]),'NUMBER':([5,],[6,]),'.':([1,6,],[5,7,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,],[3,]),'statement':([0,],[2,]),'programme':([0,],[4,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programme","S'",1,None,None,None),
  ('programme -> statement','programme',1,'p_programme_statement','C:/Users/Kevin/PycharmProjects/Turturem/parser.py',7),
  ('statement -> expression','statement',1,'p_statement','C:/Users/Kevin/PycharmProjects/Turturem/parser.py',15),
  ('expression -> MOTIF . NUMBER . COLOR','expression',5,'p_expression_motif','C:/Users/Kevin/PycharmProjects/Turturem/parser.py',19),
]