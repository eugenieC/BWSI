def student_func(x):
  ans=""
  if (x % 3) == 0:
    ans+="three"
    
  if (x % 5) == 0:
    ans+="five"

  if (x % 3) != 0 and (x % 5) != 0:
    return x
    
  return ans
  pass

from bwsi_grader.python.three_five import grader
grader(student_func)
