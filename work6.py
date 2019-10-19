def song(a = 3, b = 3, c = 0):
    p = ("-".join(["la"] * b) + '\n') * a
    if c:
        return p[:-1] + '!'
    else:
        return p[:-1] + '.'

d = song()

# with open("hello.txt", "w") as myfile:
#     myfile.write(d)
# myfile.close()
#
# ################Открываем файл, читаем его и записываем его в другой файл.
# # Попробывать через ридлайн - читает строчку и врайтлайн
# # .read читает до конца.
# f = open("ex1.txt", 'r', encoding="UTF-8")
# f.readlines()
# second_file = open("Second.txt", "w", encoding="UTF-8")
# for line in f:
#     #print(line)
#     second_file.write(line)
#     if not line:
#         break
#
# f.close()
# second_file.close()
#
# testfile = open("ex1.txt", encoding="UTF-8")
# for line in testfile:
#     print(line.rstrip('\n') + "!")
#

