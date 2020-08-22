
import math 

import pandas as pd 
import numpy as np


class GrainPreprocess():

    '''
    Class to preprocess grains for sedimentological analysis
    Beds and grain conversions
    '''

    def __init__(self,d=None):
        self.d = None

    def MM_ToPhiScale(self,d):

        """
        Method to convert an array/list of grain seive sizes in mm to phi scale
        
        args:: 
            d: array of grain sieve sizes
        
        Returns the phi reading for sedimentological analysis
        """

        self.d = d

        assert self.d == list, "d should be a list"
        phi=[round(-(math.log2(i)/math.log2(2)),2) for i in self.d]

        return phi
    
    def Bed_To_100(self,bed):

        """
        Method to scaleup beds and truncate beds greater than 100 to 100
        args::
            bed: Bed
        Returns:
            Scaled Bed
        
        """
        self.bed = bed
        assert self.bed == list, "Bed should be a list"
        total=sum(self.x)
        bed =[round(((i/total) *100),2) for i in self.bed]
    
        return bed
    
    
    def CummulateBed(self,bed):

        """
        Method to return the cummulative score of an array (0-100)
        """
        self.bed = bed
        assert self.bed == list, "Bed should be a list"
        from itertools import accumulate
   
    
    
        cum_bed=list(accumulate(self.bed))
        cum_beds=[round(i,2) for i in cum_bed]

        return cum_beds




    def Percentiles(self, bed_data):

        """
        This get the percentile for the data passed. 
        
        Returns  a Dictionary of the percentage passing,percentile of the data
        and the bed_data.
        """

        sedi_passing=[5,16,25,50,75,84,95,100]
        self.bed_data = bed_data
        assert self.bed == list, "bed should be a list"
        bed=self.bed_data
       
        sed_passing=[str(i)+ '%' for i in sedi_passing]
        percentiles= dict(zip(sed_passing,bed))
   
        return percentiles
        
