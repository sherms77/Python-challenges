# determine if its a first, second or third class lever

def determine_lever(l):
  f = ['e', 'f', 'l'] # first class
  s = ['e', 'l', 'f'] # second class
  t = ['f', 'e', 'l'] # third class
  if l == f:
    return 'first class lever.'
  elif l == s:
    return 'second class lever.'
  else:
    return 'third class lever.'

print(determine_lever(['e', 'f', 'l'])) # first class
print(determine_lever(['e', 'l', 'f'])) # second class
print(determine_lever(['f', 'e', 'l'])) # third class

# 231220: completed exercise today. third easy exercise.
# cannot submit bc free trial ended on edabit.
# cannot do anymore exercises on edabit bc free trial ended.
# will switch to hackerrank
