from django.http import HttpResponse
from rest_framework import generics


def get_queryset(request,x=0):
  try:
    x = int(request.GET.get('x'))
  except(ValueError, TypeError, AttributeError):
    return HttpResponse("Please enter the parameter-a in the form http://localhost:9999/testcgo/?x=1&a=1,2,3,4,5,7")

  try:
    a = request.GET.get('a')
    listA = a.split(",")
    listA = list(map(int, listA))
  except(ValueError, TypeError, AttributeError ):
    return HttpResponse("Please enter the parameter-a in the form http://localhost:9999/testcgo/?x=1&a=1,2,3,4,5,7")

  output = solution(x,listA)
  return HttpResponse("The earliest time when the frog can jump to the other side of the river is " + str(output) + " second")

def solution(X, A):
  '''
  :param X: Position across the river from 1 to X
  :param A: An array A consisting of N integers representing the falling leaves
  :return: The earliest time when the frog can jump to the other side of the river
  '''

  # Define a list for checking whether leaves have ever fallen at this location or not.
  numberOfElementList = [0] * len(A)

  # Define list that represent the position to come across to the other side of the river.
  # If the item in this list completely removed, it can pass through the river.
  uniqueList = [i for i in range(1,X+1)]

  # Check condition
  if X > len(A) or X > 100000 or len(A)>100000:
      # Never able to jump to the other side of the river,
      return -1

  # Loop in A
  for index,position in enumerate(A):

      # Check a leaves have ever fallen in this postion.
      if numberOfElementList[position-1] == 0:
          # A leaves never fall off this postion .
          numberOfElementList[position-1] = numberOfElementList[position-1] + 1

          # remove this position from uniqueList
          uniqueList.remove(position)


      if not uniqueList:
          # this list completely removed, it can pass through the river.
          return index

  # At the end of the loop never able to jump to the other side of the river,
  if uniqueList:
      return -1
