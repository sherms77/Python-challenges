'''
# original code
def grade_percentage(user_score, pass_score):
   s=''
   if int(user_score[:-1])<=int(pass_score[:-1]): # [:-1] index is stripping the % from the string value to convert to an int.
      s=s+'FAILED'
   if int(user_score[:-1])>=int(pass_score[:-1]):
      s=s+'PASSED'
   return 'You'+' '+s+' '+'the Exam'

# print(grade_percentage('40%', '70%'))
print(grade_percentage('80%', '70%'))
'''

# refer to repl.it for solution
# tip - run all test cases before submitting

# v4
def grade_percentage(user_score, pass_score):
   s=''
   if int(user_score[:-1])<=int(pass_score[:-1]): 
      s=s+'FAILED'
   if int(user_score[:-1])>=int(pass_score[:-1]):
      s=s+'PASSED'
   return 'You'+' '+s+' '+'the Exam'
   # return 'Your score ' +user_score + '\nYou'+ ' ' +s+ ' ' + 'the Exam' + '\nRequired score ' +pass_score

print(grade_percentage('40%', '70%'))
# print(grade_percentage('80%', '70%'))

'''
# v3
def grade_percentage(user_score, pass_score):
   s=''
   if int(user_score[:-1])<=int(pass_score[:-1]): 
      s=s+'FAILED'
   if int(user_score[:-1])>=int(pass_score[:-1]):
      s=s+'PASSED'
   return 'Your score ' +user_score + '\nYou'+ ' ' +s+ ' ' + 'the Exam' + '\nRequired score ' +pass_score

print(grade_percentage('40%', '70%'))
# print(grade_percentage('80%', '70%'))

# v1
# getting errors with this code on edabit
def grade(user, req): 
   u = user.strip('%') # strips % to convert to int
   r = req.strip('%')
   if int(u)<=int(r):
      print('Your score ', user)
      print('You FAILED the Exam')
      print('Required score', req)
   else:
      print('Your score ', user)
      print('You PASSED the Exam')
      print('Required score', req)

grade('30%', '70%') # works
# grade('80%', '70%')

# v2
# getting errors with this code on edabit
# FAILED: None should equal 'You PASSED the Exam'
def grade_percentage(user, req): 
   if int(user[:-1])<=int(req[:-1]):
      print('Your score ', user)
      print('You FAILED the Exam')
      print('Required score', req)
   else:
      print('Your score ', user)
      print('You PASSED the Exam')
      print('Required score', req)

grade_percentage('40%', '70%')
'''

