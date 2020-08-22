
import math 

import pandas as pd 
import numpy as np

class GrainDataTables():
    
    def __init__(self,z=None):
        self.z= z




    def infohelp(self,x=None):
        self.x=x
        print('''Input the very First Bed Data into the BedData function,
        Then when passing the rest of the bed data
        you include the first data initiated and the data points for other beds. ''')
    
    
    
    def BedData(self, name_of_bed,graphic_mean,graphic_std,graphic_skewness,graphic_kurtosis):
        """
        To save to a bed with it is respective mean, standard dev,skewness,kurtosis.
        the returned data will then be passed into the complete the beds function to complete the beds for an outcrop.
        
        """
        self.name = name_of_bed
        self.graphic_mean=graphic_mean
        self.graphic_standard_dev=graphic_std
        self.graphic_skewness = graphic_skewness
        self.graphic_kurtosis= graphic_kurtosis
        
        bed_stat_data = pd.DataFrame({'Name_of_bed':[self.name],
                      'Graphic Mean':[self.graphic_mean],
                      'Graphic Standard deviation':[self.graphic_standard_dev],
                       'Graphic Skewness':[self.graphic_skewness],
                      'Graphic Kurtosis':[self.graphic_kurtosis]
                     })
    
        return bed_stat_data

    def CompleteBeds(self,bed_stat,name_of_bed,graphic_mean,graphic_std,graphic_skewness,graphic_kurtosis):
        """ 
         To save to a bed with it is respective mean, standard dev,skewness,kurtosis.
        
        """
        self.name = name_of_bed
        self.graphic_mean=graphic_mean
        self.graphic_standard_dev=graphic_std
        self.graphic_skewness = graphic_skewness
        self.graphic_kurtosis= graphic_kurtosis
        
        update={'Name_of_bed':self.name,
                      'Graphic Mean':self.graphic_mean,
                      'Graphic Standard deviation':self.graphic_standard_dev,
                       'Graphic Skewness':self.graphic_skewness,
                      'Graphic Kurtosis':self.graphic_kurtosis
                     }
        self.bed_stat =bed_stat.append(update,ignore_index=True)
    
        return self.bed_stat
    
    def SaveBeds(self,data,name_of_rock_unit):

        '''
        Saves Bed Grains stats from the CompleteBeds and creates a CSV file in your Present working Directory.
        '''
        
        self.data=data
        self.name= name_of_rock_unit
    
        self.data.to_csv(f'{self.name}.csv')
    
    
    