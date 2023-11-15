dic = {}
# 1.파일 읽어오기
try :
    f = open('dictionary.txt','r',encoding='UTF8')
except FileNotFoundError as e:
        print(e)
else:
    if f.readable() :
        for line in f.readlines() : #파일에서 한줄을 읽어 문자열로 가져옮
            item = line.split(':')
            key = item[0].strip()
            value = item[1][:-1].strip()
            dic[key] = value
        f.close()        
print(dic)    

line = '*' * 20
print(line)
print('영어단어사전 어플')
print(line)

stop = False
while not stop :
    print('메뉴: 1.저장 2.검색 3.수정 4.삭제 5.목록 6.통계 7.종료')
    menu = input('메뉴선택 : ')
    
    if menu == '1':
        word = input('단어 : ')
        meaning = input('뜻 : ')
        dic[word] = meaning
    elif menu == '2':
        pass
    elif menu == '5':
       for key, value in dic.items() :
           print(key,value)    
    elif menu == '7':
        stop = True
        f = open('dictionary.txt','w',encoding='UTF8')
        if f.writable() :
            for key, value in dic.items():
                key = key.strip()
                value = value.strip()
                f.write(f'{key} : {value}\n')
            f.close()
    else:
        pass        