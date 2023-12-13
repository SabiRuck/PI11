max = 30
body = int(input("Zadaj body: "))
percent = (body / max) * 100
print(f"Ziskal si {round(percent, 2)}%.")

# if percent >= 90:
#     print("Vyborny")
# else:
#     if percent >= 75:
#         print("Chvalitebny")
#     else:
#         if percent >= 50:
#             print("Dobry")
#         else:
#             if percent >= 30:
#                 print("Dostatocny")
#             else:
#                 print("Nedostatocny")

if percent >= 90:
    print("Vyborny")
elif 75 <= percent:
    print("Chvalitebny")
elif 50 <= percent:
    print("Dobry")
elif 30 <= percent:
    print("Dostatocny")
else:
    print("Nedostatocny")

















