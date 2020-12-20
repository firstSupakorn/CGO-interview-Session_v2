from django.http import HttpResponse
from rest_framework import generics
from .forms import CreateNewList
from django.shortcuts import render


def input(request,x=0):
    form = CreateNewList()
    return render(request,"inputPage.html",{"form":form})

def output(request):
    if request.method == "GET":
        form = CreateNewList(request.GET)
        if form.is_valid():
            x = form.cleaned_data["x"]
            a = form.cleaned_data["a"]
            listA = a.split(",")
            listA = list(map(int, listA))
            output = solution(int(x),listA)
    return render(request,"outputPage.html",{"output":output})

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
