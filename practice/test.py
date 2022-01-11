
# # list

# users = ["Yo", "Ken", "Nao", "Shin", "Lee"]
# users.append("Miu")

# print (users[0])
# print (users[0:2])
# print (users[1:])
# print (users[::2])
# print (users[::-1])

# users.remove("Nao")
# print(users)

# users = [u.lower() for u in users if u.find("e") != -1]
# print(users)



# # dictionary
# user_dict = {
#     "Yohei": 30,
#     "John": 35
# }

# user_dict.get("Nao", 20)

# user_dict["Yohei"] = 31
# del user_dict["John"]

# for k, v in user_dict.items():
#     print(k, v)

# print(user_dict["Yohei"])


# # Set
# set_ = {
#     "Tennis", "Ramen", "Programming"
# }

# set_.add("Gs")
# set_.remove("Ramen")

# for s in set_:
#     print(s)

# set1 = set([1, 2, 3, 4, 5])
# set2 = set([3, 4, 5])
# print(set1 - set2)



# # tuple
# nums = "One", "Two", "Three"

# print(nums[0])

# for n in nums:
#     print(n)

# a, b, c = nums
# print(a)


# # <2> 文字列とインデックスアクセス
# str = "じこーだすまあさかんでのみしーゅっみてはたなのんしだいろな"
# print(str[0::2])
# print(str[1::2])


# # <3> Setの練習
# set_1 = set("「ではみなさんは、そういうふうに川だと云いわれたり、乳の流れたあとだと云われたりしていたこのぼんやりと白いものがほんとうは何かご承知ですか。」先生は、黒板に吊つるした大きな黒い星座の図の、上から下へ白くけぶった銀河帯のようなところを指さしながら、みんなに問といをかけました。")
# #print (set_1)
# print (len("「ではみなさんは、そういうふうに川だと云いわれたり、乳の流れたあとだと云われたりしていたこのぼんやりと白いものがほんとうは何かご承知ですか。」先生は、黒板に吊つるした大きな黒い星座の図の、上から下へ白くけぶった銀河帯のようなところを指さしながら、みんなに問といをかけました。"))
# print (len(set_1))


# # <4> リスト内包表記
# print([str(num) + "円" for num in range(0, 101)])


# <2> 関数
def old(x, y=20):
    print("私の名前は" + x +"で" + str(y) + "歳です")

old("Yohei", 30)
old("Hide")