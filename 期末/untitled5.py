import numpy as np
# distance(km) between 2 points

def haversine_distance(lat1, lon1, lat2, lon2):  
    r = 6371  
    phi1 = np.radians(lat1) 
    phi2 = np.radians(lat2)   
    delta_phi = np.radians(lat2 - lat1)  
    delta_lambda = np.radians(lon2 - lon1)  
    a = np.sin(delta_phi / 2)**2 + np.cos(phi1) * np.cos(phi2) *   np.sin(delta_lambda / 2)**2 
    res = r * (2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a)))
    return np.round(res, 8)
import numpy as np

Z = np.array([30, 27, 35, 13, 20, 10, 25, 47, 26, 38, 38, 23, 40, 39, 23, 33, 31, 20, 37, 44])

R = np.array([2.7, 1.9, 5.5, 0.6, 0.7, 0.3, 1.4, 38.9, 1.7, 9, 8.9, 1, 12.5, 10.4, 1.1, 4.1, 3.2, 0.8, 7.8, 23.8])