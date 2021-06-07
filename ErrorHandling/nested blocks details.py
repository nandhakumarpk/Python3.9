#control flow of nested try-except-finally block
try:
state1
state2
state3
try:
state4
state5
state6
except:
state7
finally:
state8
state9
except:
state10
finally:
state11
state12#case1: if there is not exception then
state1, 2, 3, 4, 5, 6, 8, 9, 11, 12 will be execute (Normal Termination)
#case2: if there is exception raised in state2, its corresponding except block is matched
the state1, 10, 11, 12 will be executed (Normal Termination)
#case3: if ther is exception raised in state2, its corresponding except-block is not matched thn
state1, 11, 12 will be executed (Abnormal Termination)
#case4: if there is exceptoin in nested try-block in state5, and inner except-block is matched then,
state1, 2, 3, 4, 7, 8, 9, 11, 12 will be executed (Normal Termination)
#case5: if there is exception in nested try-block in state5, and inner block is not matched thn,
state1, 2, 3, 4, state10, 11, 12 will be executed (Normal Termination)
#case6: if there is exception in nested try-block in state5, and both inner and outer except-block is not matched. Then
state1, 2, 3, 4, state8, state11 will be executed (Abmornam Termination)
#case7: if there is exception in inner except-block in state7, and its corresponding except-block is matched. then
state1, 2, 3,...,...,..., state8, state11 will be executed (Abnormal Termination)

'''

Note: if the control is entered into try-block then finally-block must execute.
Note: if the control is not entered into try-block then finally-block will not execute.
'''
