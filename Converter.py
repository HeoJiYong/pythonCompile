# -*- coding: utf-8 -*-
###################################################
# Name : Converter.py
# Version : ver2.80
# Developer : hjy
# Modify Date : 2020. 01. 14   11:05
# Description : 하위 디렉토리 내의 .py 파일을 .pyc로 변환하는 코드
# 변경사항 : 예외처리할 디렉토리 리스트 추가.
###################################################

import os
import py_compile
ExceptionDir = ['venv','UI']
cnt = 0
def IsExceptionDir(pFile):
    if (pFile  in ExceptionDir):
        return True
    return False

def Converter(PATH):
    PathList = os.listdir(PATH)
    #현재 위치, 하위 디렉토리 목록 출력
    print()
    #print("Current Path : ",PATH)
    #print("SubDirectory : ",end ="")
    for File in PathList:
        if (os.path.isdir(PATH+File)):
            if (not IsExceptionDir(File)):
                print(File,end=", ")
    print()
    #디렉토리 순회(재귀)
    for File in PathList:
        if (os.path.isdir(PATH+File)):
            if (not IsExceptionDir(File)):
                Converter(PATH+File+'/')

    #위 과정을 거쳤다면 현재 PATH는 최하단 위치일 것임.
    #여기서부터 컴파일하면 Bottom-Up 방식으로 return하며 compile
    global cnt
    for File in PathList:
        if(os.path.isfile(PATH+File)):
            Fname,ext = os.path.splitext(PATH+File)
            if(ext == '.py'):
                print("Converting  : ",Fname+ext)
                #실제 컴파일하는 부분(한줄)
                py_compile.compile(PATH+File,Fname+'.pyc')
                cnt += 1
def main():
    print("main executed")
    Converter('./')
    print("Exception Directory : ",ExceptionDir)
    print ('총',cnt,"개의 파일이 컴파일 되었습니다")

if __name__ == '__main__':
    main()
