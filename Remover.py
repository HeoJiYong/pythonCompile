# -*- coding: utf-8 -*-
###################################################
#  Name : remover.py
# Version : ver1.10
# Developer : hjy
# Modify Date : 2020. 01. 20  14:12
# Description : 하위 디렉토리 내의 .py 파일을 찾아 삭제
# 변경사항 : 1. 예외처리할 디렉토리 목록기능 있음
# 주의 : 해당 코드로 삭제시 복구 불가.
###################################################
import os

'''삭제 안할 파일'''
ExceptionFile = ['__init__.py','Remover.py']
'''삭제 안할 디렉토리'''
ExceptionDir = ['venv', 'UI']
cnt = 0     # 컴파일 몇개 했는지 카운트

# 현재 가르키는 디렉토리가 예외디렉토리인지 판별
def IsExceptionDir(pFile):
    if pFile in ExceptionDir:
        return True
    return False

# pyc파일을 삭제하는 함수
def Remover(PATH):
    PathList = os.listdir(PATH)
    '''
    #현재 위치, 하위 디렉토리 목록 출력
    print("Current Path : ",PATH)
    print("SubDirectory : ",end ="")
    for File in PathList:
        if (os.path.isdir(PATH+File)):
            if (not IsExceptionDir(File)):
                print(File,end=", ")
    print()
    '''
    # 디렉토리 순회(재귀하여 최하단 디렉토리까지)
    # 조건문 : 예외가 아닌 & 디렉토리라면
    for File in PathList:
        if (os.path.isdir(PATH+File)) and (not IsExceptionDir(File)):
            Remover(PATH+File+'/')

    # 위 과정을 거쳤다면 현재 PATH는 최하단 위치일 것임.
    # 여기서부터 삭제하면 Bottom-Up 방식으로 삭제
    global cnt
    for File in PathList:
        if os.path.isfile(PATH+File):
            Fname, ext = os.path.splitext(PATH+File)
            if (File not in ExceptionFile) and (ext == '.py'):
                print('removing : ',Fname+ext)

                '''---------------------------------실 사용시 아래 주석 지우고 사용---------------------------------'''
                #os.remove(Fname+'.py') #실제 삭제하는 부분
                cnt +=1

def main():
    print("main executed")
    Remover('./')
    print("Exception Directory : ", ExceptionDir)
    print("Exception File : ", ExceptionFile)
    print('총', cnt, "개의 파일이 삭제 되었습니다")

if __name__ == '__main__':
    main()
