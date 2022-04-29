import shutil
import os


Start = 'D:/Coco image/COCOTOYOLO/train2017'
Destination = 'D:/Coco image/COCOTOYOLO/txt2017'

# 경로 읽기
file_list = os.listdir(Start)
file_list2 = os.listdir(Destination)

# 파일을 담는 배열 객체
moving_files = []




file_name1 = []
# . 기준으로 슬라이싱
for file in file_list: 
    if file.count(".") == 1: 
        name = file.split('.')[0]
        file_name1.append(name)
    # .이 하나가 아닐 경우
    else: 
        for k in range(len(file)-1,0,-1):
            if file[k]=='.':
                file_name.append(file[:k])
                break

file_name2 = []
for file in file_list2:
    if file.count(".") == 1: 
        name = file.split('.')[0]
        file_name2.append(name)
    else:
        for k in range(len(file)-1,0,-1):
            if file[k]=='.':
                file_name.append(file[:k])
                break


# 파일 담기
for j in range(len(file_name2)):
               for i in range(len(file_name1)):
                   if file_name2[j]==file_name1[i]:
                       moving_files.append(file_list[i])
        

# 파일 이동
for movefile in moving_files:
	shutil.move(Start + '/' + movefile, Destination + '/' + movefile)
