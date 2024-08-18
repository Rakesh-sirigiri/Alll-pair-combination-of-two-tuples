tuple1 = (4,5)
tuple2 = (7,8)
filtered_tuples = []
for element1 in tuple1:
    for element2 in tuple2:
        filtered_tuples.append((element1,element2))
        filtered_tuples.append((element2,element1))
        print(filtered_tuples)
