# Assignment6

#Part D:
  #i: the maximum absolute difference between my results and the interior points is
    #0.0
  #ii Your method can’t compute derivatives at the edges of the grid, but np.gradient does. What method does it use there? Compare its error at the edges to its error in the interior and explain the difference in terms of truncation error.
    # The interior points use central differences that have a second order truncation error, the edges use a forward or backward difference method which have a first order truncation error. The maximum absolute error of the interior points (K/m) is 0.64635 while the edge points only had 0.02517

#Part E
  #Heat flows in the direction of −∇T. Plot the vector field −∇T using quiver on top of your contour plot from (a). (You may want to plot every 5th arrow so the figure is readable.) Describe the direction of the arrows relative to the contours.
    #The arrows point out from the center of the temp distribution, moving from regions of higher temps and toward regions of lower temps. They are perpindicular to the contour lines becuase the gradient points in the direction of the greatest temp change.
