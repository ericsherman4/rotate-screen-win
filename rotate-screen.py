import rotatescreen

screen2 = rotatescreen.get_secondary_displays()

file = open("data.txt", "r")
data = file.readlines()[0]
file.close()

data2write = ""

if data == "True":
    screen2[0].set_portrait()
    data2write = "False"
else:
    screen2[0].set_landscape()
    data2write = "True"

file = open("data.txt", "w")
file.writelines(list(data2write))

file.close()