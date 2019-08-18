###############################################################################
#
#   tia_lsfr.py
#
#   Python implementations of the six-bit polynomial counter (linear
#   feedback shift register) used in several places within the Atari
#   VCS's TIA graphics chip.
#
#   Two "register" classes are defined: One represents the register
#   bits as a list of boolean values, manipulated "manually". The
#   other simply stores a single variable and uses Python's built-in
#   bitwise operators to manipulate it. Externally, the two classes
#   work the same way (as the demonstration code shows).
#
#   Both classes display as strings by first showing the binary
#   form of the register state, followed by the decimal equivalent.
#
#   Integer representations of the classes return the decimal form
#   of the register state.
#
#
#   Jeff Jetton
#   August 2019
#
###############################################################################



class TiaCounterV1:
    '''
    Implementation of a six-bit LFSR with an XNOR-based feedback
    function and taps on bits 0 and 1.
    
    "Bits" are stored internally as a list of booleans, and regular
    boolean logic operators are used to manipulate them.
    
    The initial "seed" value can be specified on instantiation, or
    it can be left to default to zero. Setting the seed to the
    "illegal" state (all 1 bits, or 63) or a value larger than
    the bit width is not allowed.
    '''
    
    
    # The bit width is theoretically adjustable, but since the taps
    # are hard-coded to be on bits 0 and 1, the resulting counter
    # will probably not generate a maximum-lengh sequence.
    # (Also, the string conversions assume a six-bit width, so
    # object printing will be wonky if you go any wider.)
    bit_width = 6
    illegal_state = (2 ** bit_width) - 1
  
  
    def __init__(self, seed=0):
        if seed < 0 or seed >= (2 ** self.bit_width):
            raise ValueError('Seed value out of range')
        elif seed == self.illegal_state:
            raise ValueError('Seed value creates illegal state')
        else:
            # Set up initial state from seed...
            # First convert seed to binary string, left-padded
            # to the current bit width
            seed = "{:06b}".format(seed)
            # Then split out into a boolean list
            self.state = []
            for bit in seed:
                self.state.append(bool(int(bit)))


    def __int__(self):
        i = 0
        for j, bit in enumerate(self.state):
            i += int(bit) * (2 ** (self.bit_width - j - 1))
        return i


    def __str__(self):
        # Turn the booleans into numbers
        s = ''.join([str(int(bit)) for bit in self.state])
        # Tack on the decimal representation
        s = s + "   {:>2}".format(int(self))
        return s


    def shift(self):
        # Our taps are bits 0 and 1 (rightmost and next-rightmost)
        tap0 = self.state[-1]
        tap1 = self.state[-2]
        
        # Figure out the "input" bit by XNOR-ing the two taps.
        # XNOR is only true if the operands match each other
        # and is always false if they don't, so...
        inbit = (tap0 == tap1)
        
        # Shift the register to the right by copying everything except
        # the last element back into the list, one position over
        self.state[1:] = self.state[0:-1]
        
        # Write the input bit into the first element of the list
        self.state[0] = inbit





###############################################################################


class TiaCounterV2:
    '''
    Same basic idea as TiaCounterV2, except that it implements the
    LFSR using a single numeric variable and bitwise operators.
    (This is closer to how the actual TIA chip would do it.)
    '''
    
    
    bit_width = 6
    illegal_state = (2 ** bit_width) - 1


    def __init__(self, seed=0):
        if seed < 0 or seed >= 2 ** (self.bit_width):
            raise ValueError('Seed value out of range')
        elif seed == self.illegal_state:
            raise ValueError('Seed value creates illegal state')
        else:
            self.state = seed
        
        
    def __str__(self):
        return "{:06b}   {:>2}".format(self.state, self.state)


    def __int__(self):
        return self.state


    def shift(self):
        # Isolate bit 0 (rightmost bit) by AND-ing with 1
        tap0 = self.state & 0b000001
        # Shift the register to the right one bit
        self.state >>= 1
        # Now bit 0 is the old bit 1
        # Isolate it as our second tap
        tap1 = self.state & 0b000001
        
        # Figure out the "input" bit by XNOR-ing the two taps.
        # Python doesn't have XNOR, so we'll do an XOR...
        inbit =  tap1 ^ tap0
        # ...then do the NOT part by flipping the rightmost
        # bit (and only the rightmost bit) with an XOR 1
        inbit ^= 0b000001

        # Push the input bit into the end of the register
        # by first shifting it all the way to the left...
        inbit <<= (self.bit_width - 1)
        # ...then OR-ing it to the register
        self.state |= inbit






