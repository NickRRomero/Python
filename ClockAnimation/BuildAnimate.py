def write():
    num = 1
    rotation = 180
    while rotation  > -1:
        print("{\n" +
            "\"number\":" + str(num) + ",\n" +
            "\"x\":0,\n" +
            "\"y\":0,\n" +
            "\"width\":107,\n" +
            "\"height\":107,\n" +
            "\"rotation\":" + str(rotation)  + ",\n" +
            "\"opacity\":1\n},")
        rotation -= 1
        num += 1
write()