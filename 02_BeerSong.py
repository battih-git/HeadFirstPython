word = "bottles"
for beer_num in range(5,0,-1):
    print (beer_num, word, " of beer on the wall.")
    print(beer_num, word, " of beer.")
    print("Take one down")
    print("Pass it around")
    if beer_num == 1:
        print("No more bootles of beer on the wall.")
    else:
        new_num = beer_num - 1
        if new_num == 1:
            word = "bottle"
        print(new_num, word, " of beer on the wall.")
    print()
# range(start, stop, step)
# The START value lets you control from WHERE the range begins.
# The STOP value lets you control WHEN the range ends.
# The STEP value lets you control HOW the range is generated.
