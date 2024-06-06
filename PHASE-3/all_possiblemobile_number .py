store={
    "2":"abc",
    "3" :"def",
    "4":"ghi",
    "5":"jkl",
    "6":"mno",
    "7":"pqrs",
    "8":"tuv",
    "9":"wxyz"
}

def printLetter(word,index,result):
    if index == len(word):
        print("".join(result))
        return
    ch=word[index]
    for val in store[ch]:
        result.append(val)
        printLetter(word,index+1,result)
        result.pop()

word="23"
printLetter(word,0,[])