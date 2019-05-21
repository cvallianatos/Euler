'''
In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
'''
count = 1
for p100 in range(3):
    for p50 in range(int(1+(200-100*p100)/50)):
        for p20 in range(int(1+(200-100*p100-50*p50)/20)):
            for p10 in range(int(1+(200-100*p100-50*p50-20*p20)/10)):
                for p5 in range(int(1+(200-100*p100-50*p50-20*p20-10*p10)/5)):
                    for p2 in range(int(1+(200-100*p100-50*p50-20*p20-10*p10-5*p5)/2)):
                        count = count + 1
print(count)