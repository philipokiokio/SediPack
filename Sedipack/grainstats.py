#The Object 
import math 

import pandas as pd 
import numpy as np



from matplotlib.ticker import AutoMinorLocator,FormatStrFormatter
import matplotlib.pyplot as plt
from matplotlib import style
from matplotlib.widgets import Cursor,Button


style.use('ggplot')








#    
class GrainStatsDes():

    def __init__(self, s=None):
        self.s=s

    def Infohelp():
        print('''A suite of codes that calculate the Graphic Mean, Graphic Standard  Deviation, Kurtosis and Skewness''')
    
    
    
    def GraphicMean(self, data):
    
        '''A function to calculate the graphic mean for the Data using the 16th, 50th, 84th percentiles'''

        self.data =data
    #     percentiles = [16,50,84]
        phi_percentile=list(self.data['Percentile_Grain_size_(Phi)'])
   
        
        sumation=phi_percentile[1] + phi_percentile[3] + phi_percentile[5]
     
    
        graphicMean= round((sumation/3),2)
        
        return graphicMean

    
    def GraphicStandard_Dev(self,data):

    
        '''
        Method to calculate the graphic standard deviation for the Data 
        using the 95th, 5th, 84th,16th percentiles
        '''
        self.data = data
    #     percentiles_right = [95,5]
    #     percentiles_left = [84,16]
        phi_percentile=list(self.data['Percentile_Grain_size_(Phi)']) 
    
    
    
#     for i in percentiles_left:
#         left_side.append(round(np.percentile(data.Phi_scale,i),2))
    
    
#     for j in percentiles_right:
#         right_side.append(round(np.percentile(data.Phi_scale,j),2))

        left_math = phi_percentile[5] - phi_percentile[1]
        right_math = phi_percentile[6] - phi_percentile[0]
    
        graphic_std = round((left_math/ 4) + (right_math/6.6),2)
        
        return graphic_std
    
    
    def GraphicSkewness(self,data):

        '''
        Method for the the graphic_skewness using the 5th, 16th, 50th, 84th,95th percentiles
        '''
        self.data =data
        #percentiles = [5,16,50,84,95]
    
        phi_percentile=list(self.data['Percentile_Grain_size_(Phi)'])
    
    
    
        left_numerator = phi_percentile[5] + phi_percentile[1]- (2 * phi_percentile[3])
        right_numerator = (phi_percentile[6] + phi_percentile[0])- (2* phi_percentile[3])
    
        left_denometer = 2 *(phi_percentile[5]- phi_percentile[1])
        right_denometer = 2 *(phi_percentile[6] - phi_percentile[0])
        graph_skew = round((left_numerator/left_denometer) + (right_numerator/right_denometer),3)



        return graph_skew
    
    
    
    def GraphicKurtosis(self,data):

        '''
        Method for the Graphic Kurtosis, using the 5th, 25th,75th and the 95th percentile
        '''
        self.data = data
    #     percentile = [5,25,75,95]
    
        phi_percentile=list(self.data['Percentile_Grain_size_(Phi)'])
    
        numerator = phi_percentile[6] - phi_percentile[0]
        denumator = 2.44*(phi_percentile[4] - phi_percentile[3])
    
        graphic_kurtosis = round((numerator / denumator),2)
        return graphic_kurtosis
    
    


