#파이썬 DATA TYPE
x1 = 10 #int(정수)
x2 = 10.1 #float(실수)

x3 = "안녕하세요 \n반갑습니다" #str(문자열) #''도가능 # """" 있는 모든 글자를 포함할 때 이렇게 사용
x4 = """
    안녕하세요
    반갑습니다
    """

print(x3)
print(x4)

#형변환
x1_1 = float(x1) #int -> float #.0을 붙여줌
x2_1 = int(x2) #float -> int #정수만 뽑아줌
x2_2 = str(x2) #float -> str

print(x1_1, type(x1_1))
print(x2_1, type(x2_1))
print(x2_2, type(x2_2))

#리스트 #데이터 수정가능(튜플과 비교시)
x1 = ["1", 2, 2.5]  #꼭 같은데이터 형태만 들어가 있을 필요가 없다
x1.append("안녕")
for x in x1 :
    print(x)
print("-"*20)

#튜플(tuple) #데이터 수정불가
xt = ("1", 2, 2.5, [7,8,9])
for x in xt :
    print(x)
#xt.append #이런거 안된다고 합니당

xt1 = list(xt)
print(type(xt1))

#슬라이싱이 가능 - 문자열, 리스트, 튜플
print(xt[:3])
print(xt[3:])

#딕셔너리(dict)
#딕셕너리(didt): 키와 값의 쌍 #순서가 정해져 있지 않음
dic = {"a":1, "b":2, "c":3}
print(dic["a"])
print(dic.get("a"))
dic["d"] = 4
print(dic)

print("-" *20)
for item in dic:
    print(item, "=>", dic[item])
    
for item in dic.items():
    print(item)

for key, value in dic.items():
    print(key, "=>", value)


from func import fileToStr
import json



data =fileToStr("cdg.json")
dataj = json.loads(data)

# print(data)
# for key, value in data.items() :
#     print(key,value)

print("-"*30)
item = dataj.get("item")[0]
print(type(item))
LWCR_ICD_SUMRY = dataj.get("item")
print(item.get('LWCR_ICD_SUMRY'))
