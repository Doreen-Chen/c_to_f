# 35_Casting_Temprature
# 攝氏('C) 轉換成華氏('F) 程式
#
# 讓使用者輸入 攝氏溫度
# 然後印出華氏溫度
# F = (C * 9/5) + 32
# + - * /

temp_c = input('請輸入攝氏溫度: ')
#temp_c = int(temp_c)    ### 這裡執行不會有Error, 但是轉成 float 更好
temp_c = float(temp_c)
temp_c = (temp_c * (9 / 5)) + 32
print('轉換華氏溫度為: ', str(temp_c))