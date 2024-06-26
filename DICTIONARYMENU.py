#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 17:45:11 2023

@author: dai
"""
import sys

course={"DBDA":(100,60),"DAI":(200,50)}
def addnewcourse():
    cname=input("Enter Course name:")
    duration=int(input("Enter the duration:"))
    capacity=int(input("Enter capacity:"))
    value=course.get(cname,-1)
    if value==-1:
        course[cname]=(duration,capacity)
        return True
    else:
        return False
    
def displayall():
    for k,v in course.items():
        print(f"{k}--->{v}")

def displaybycapacity(capacity):
    d={}
    for k,v in course.items():
        if v[1]>capacity:
            d[k]=v
    if len(d)!=0:
        return d
    return None

def deletecourse(str1):
    
    for k in course:        
        if str1==k:
            course.pop(k)            
            return True   
    return False
        
def courseupdate(str1,str2):

  for k in course:
      if str1==k:
          course[k] = (course[k][0],str2)
          return True
  return  False

def nameupdate(str1,str2):

  for k in course:
      if str1==k:
          course[str2] = course.pop(k)
          return True
  return  False


    
    
choice=0

while choice!=7:
    choice=int(input("""\n\nMENU
1. Add course
2. Delete any Course
3. Modify Course Capacity
4. Modify Course Name
5. Display all
6. Display only Course with capacity > given capacity
7. Exit
\n\nNow enter your choice:"""))


    match choice:
        case 1:
            status=addnewcourse()
            if status:
                print("Course added")
            else:
                print("Course exists")
        case 2:
            str1=input("Enter course name to delete")
            v=deletecourse(str1)
            if v!=0:
                print("Course deleted")
            else:
                print("Course not found")
            
        case 3:
            str1=input("Enter the course name to update capacity")
            str2=int(input("Enter course capacity"))
            v=courseupdate(str1,str2)
            if v:
                print("Course capacity updated")
            else:
                print("Wromg course entered")
        case 4:
            str1=input("Enter the course name to update")
            str2=input("Enter new name")
            v=nameupdate(str1,str2)
            if v:
                print("Course name updated")
            else:
                print("Wromg course entered")
        case 5:
            displayall()
        case 6:
            capacity=int(input("Enter capacity"))
            data=displaybycapacity(capacity)
            if data!=None:
                displayall(data)
            else:
                print("No course found")
        case 7:
            print("Thank you for visiting")
            sys.exit()
        case _:
            print("Wromg Choice")
