def student_func(x):
  # `x` is a string
  # this function should return either `True` or `False`

  # make case-insensitive and remove space
  x = x.lower().replace(" ","")

  # find the half way point
  if (len(x) % 2) == 1:
    half = int((len(x) - 1)/2)
  else:
    half = int(len(x)/2)
  
  # compare the paired character
  for i in range(0,half):
    if x[i] != x[len(x)-1-i]:
      return False

  return True
  pass

from bwsi_grader.python.palindrome import grader
grader(student_func)
