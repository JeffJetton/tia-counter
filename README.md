# TIA Counter

Python implementations of the sort of six-bit, two-tap, XNOR-based polynomial counter ([linear feedback shift register](https://en.wikipedia.org/wiki/Linear-feedback_shift_register)) used in several places within the Atari VCS's TIA graphics chip.

`tia_counter.py` defines two classes:

* **TiaCounterV1** - Represents the register bits internally as a list of boolean values, manipulated "manually" using standard boolean operators
* **TiaCounterV2** - Stores register contents in a single integer variable, manipulated using bit-wise operators

V2 is closer in spirit to how the TIA chip actually works, but V1 might be a bit more intuitive to understand.

`tia_counter_demo.py` demonstrates instantiating both classes and cycling through all their possible states. The output (reproduced below) shows that their states are identical to each other at each period. 

Note that the states are identical to those produced by the real TIA counter circuits, as outlined in Andrew Towers' [Atari 2600 TIA Hardware Notes](http://www.bjars.com/resources/tia_hw_notes.txt).



```
 i   List Counter     Bit Counter     Match?
--   ------------     -----------     ------
 1   000000    0      000000    0      Yes
 2   100000   32      100000   32      Yes
 3   110000   48      110000   48      Yes
 4   111000   56      111000   56      Yes
 5   111100   60      111100   60      Yes
 6   111110   62      111110   62      Yes
 7   011111   31      011111   31      Yes
 8   101111   47      101111   47      Yes
 9   110111   55      110111   55      Yes
10   111011   59      111011   59      Yes
11   111101   61      111101   61      Yes
12   011110   30      011110   30      Yes
13   001111   15      001111   15      Yes
14   100111   39      100111   39      Yes
15   110011   51      110011   51      Yes
16   111001   57      111001   57      Yes
17   011100   28      011100   28      Yes
18   101110   46      101110   46      Yes
19   010111   23      010111   23      Yes
20   101011   43      101011   43      Yes
21   110101   53      110101   53      Yes
22   011010   26      011010   26      Yes
23   001101   13      001101   13      Yes
24   000110    6      000110    6      Yes
25   000011    3      000011    3      Yes
26   100001   33      100001   33      Yes
27   010000   16      010000   16      Yes
28   101000   40      101000   40      Yes
29   110100   52      110100   52      Yes
30   111010   58      111010   58      Yes
31   011101   29      011101   29      Yes
32   001110   14      001110   14      Yes
33   000111    7      000111    7      Yes
34   100011   35      100011   35      Yes
35   110001   49      110001   49      Yes
36   011000   24      011000   24      Yes
37   101100   44      101100   44      Yes
38   110110   54      110110   54      Yes
39   011011   27      011011   27      Yes
40   101101   45      101101   45      Yes
41   010110   22      010110   22      Yes
42   001011   11      001011   11      Yes
43   100101   37      100101   37      Yes
44   010010   18      010010   18      Yes
45   001001    9      001001    9      Yes
46   000100    4      000100    4      Yes
47   100010   34      100010   34      Yes
48   010001   17      010001   17      Yes
49   001000    8      001000    8      Yes
50   100100   36      100100   36      Yes
51   110010   50      110010   50      Yes
52   011001   25      011001   25      Yes
53   001100   12      001100   12      Yes
54   100110   38      100110   38      Yes
55   010011   19      010011   19      Yes
56   101001   41      101001   41      Yes
57   010100   20      010100   20      Yes
58   101010   42      101010   42      Yes
59   010101   21      010101   21      Yes
60   001010   10      001010   10      Yes
61   000101    5      000101    5      Yes
62   000010    2      000010    2      Yes
63   000001    1      000001    1      Yes
64   000000    0      000000    0      Yes
```

