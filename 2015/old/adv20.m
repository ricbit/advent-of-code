Print[Select[ParallelTable[{x, DivisorSigma[1, x]}, {x, 1, 
    1000000}], #[[2]] >= 3400000 &][[1]]]
