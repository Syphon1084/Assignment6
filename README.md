# Assignment6

#Part D:
  #i: the maximum absolute difference between my results and the interior points is
    #0.0
  #ii Your method can’t compute derivatives at the edges of the grid, but np.gradient does. What method does it use there? Compare its error at the edges to its error in the interior and explain the difference in terms of truncation error.
    # The interior points use central differences that have a second order truncation error, the edges use a forward or backward difference method which have a first order truncation error. The maximum absolute error of the interior points (K/m) is 0.64635 while the edge points only had 0.02517
