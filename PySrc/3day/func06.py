# Func06.py

a= {'사과' :'apple',
    '포도' :'grape',
    '바나나':'banana',
    '컵' :'cup',
    '물': 'water'}

def pDict(**d):
    for i in d.items(): print(i)


#pDict(a)
pDict(사과='apple',
      포도='grape',
      바나나='banana')


