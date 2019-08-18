from tia_counter import *


# Create a list-based counter object
tia1 = TiaCounterV1()

# Create a bit-based counter object
tia2 = TiaCounterV2()

# Cycle through every period of each and compare states
print('\n i   List Counter     Bit Counter     Match?')
print('--   ------------     -----------     ------')
for i in range(2 ** 6):
    s = "{:>2d}   ".format(i+1)
    s += str(tia1) + '      ' + str(tia2) + '      '
    if int(tia1) == int(tia2):
        s += "Yes"
    else:
        s += "No"
    print(s)
    
    # Cycle both counters to their next state
    tia1.shift()
    tia2.shift()


print('\n')
