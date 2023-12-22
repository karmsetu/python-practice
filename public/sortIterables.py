
#? 
from re import T


student = [
('a', "f", 32),
('b', "f", 32),
('c', "f", 32),
('d', "f", 32),
('e', "f", 32),
('e', "f", 32),
('reverse', "f", 32),
('T', "f", 32)
]
name = lambda name:name[0]
student.sort(key=name, reverse=True)
sortedStd = sorted(student, reverse=True)
print(student, sortedStd)