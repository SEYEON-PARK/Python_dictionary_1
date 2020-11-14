'''
engDict=dict()

engDict["happy"]="기쁜"
engDict["good"]="좋은"
engDict["ride"]="타다"
engDict["one"]="하나"

word=input("영어 단어를 입력하시오. : ")
print(engDict.get(word, "이 사전에는 입력하신 단어가 없습니다."))
'''

engDict=dict()

engDict["happy"]="기쁜"
engDict["good"]="좋은"
engDict["ride"]="타다"
engDict["one"]="하나"

word=input("영어 단어를 입력하시오. : ")

if(word in engDict):
    print(engDict[word])
else:
    print("이 사전에는 입력하신 단어가 없습니다.")
