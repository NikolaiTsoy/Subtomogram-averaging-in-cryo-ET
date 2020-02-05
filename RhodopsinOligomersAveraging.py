#!/usr/bin/env python
# coding: utf-8

# In[158]:


#define coordinates of the target point (t) and two corner points (p) and (q) in tomog coordin. system

import numpy as np

#difene tomog number 
#function to automaticaly a) shift for several nm from chosen point and b) run for each shifted point
#function to estimate sigma for each set {point} {direction} {point/direction}

t = np.array ([0,0,0]);
q = np.array ([7,4,-1]);
p = np.array ([2,1,1]);

# planar vector k1 = p - t; planar vector k2 = q - t;                                          DONE
 
k1 = p - t;
k2 = q - t;

# normal vector n = k1 x k2, basis vector e1 = k1/|k1|, e2 = n x e1 /|n|                      DONE

n = np.cross (k1,k2); 

length_k1 = np.linalg.norm(k1);

e1 = k1 * (1/length_k1); 
e2 = np.cross (e1,n)/np.linalg.norm(n); 

# define sampling angle "u" in degrees and radius of sampling "sr" in pixels                   DONE

u = 10;               #######  sampling angle
sr = 10;                ########## radius for averaging in pixels

print("phi  ", "AverInt  ", "point ", "tomoNum   ");
ArrSize = int(360/u);
print("Size is 4 x (angles number)", ArrSize);
print("   ");
Tomo1point1 = np.empty((4,ArrSize));      #array for final results 
tomos13 = np.zeros((20,20,20))         ###array with intensities form the tomogram


# sampling among angles                     DONE 
for k in range(0, int (360/u)):
    phi = k*u;
    # define direction of sampling 
    alpha = np.sin(phi);
    beta = np.cos(phi); 
    sd = alpha * e1 + beta * e2;
    print ("   ");
    for m in range(-sr, sr+1):
        theorCoord = t + m * sd; 
        pixelCoord = np.round (theorCoord);
        
        Int = tomos13[int(pixelCoord[0]), int(pixelCoord[1]), int(pixelCoord[2])];
        ## get intensity value "Int" from array tomos13 in the point with coordinates "pixelCoord"
        
        if (m == -sr):
            summInt = Int;
        else:
            summInt = summInt + Int;
    averInt = summInt / (2 * sr + 1);
    Tomo1point1[0,k] = phi;
    Tomo1point1[1,k] = averInt;
    Tomo1point1[2,k] = 123;
    Tomo1point1[3,k] = 2.25;
    print(Tomo1point1[0,k], " ", Tomo1point1[1,k], "  ", Tomo1point1[2,k], "  ", Tomo1point1[3,k]);
    
# put {phi/<intensity>} to final array 

# plot array tomog/point (tetha, aver)



# In[ ]:





# In[ ]:




