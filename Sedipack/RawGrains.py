#The Object 
import math 

import pandas as pd 
import numpy as np

class GrainPreprocess():
    def __init__(self):
        pass
    
    def MM_to_Phi(d):
#         self.d = d
        phi=[round(-(math.log2(i)/math.log2(2)),2) for i in d]
        
        """this function converts an array/list of grain seive sizes in mm to phi scale 
        and returns the phi reading for sedimentological analysis"""
        return phi
    
    def Bed_To_100(x):
        """This is used to scale beds that are less than 100 in total weight to 100"""
        total=sum(x)
        bed =[round(((i/total) *100),2) for i in x]
    
        #     for i in x:
        #         bed.append(round(((i/total) *100),2))
        return bed
    
    
    def CummulateBed(bed):
        """this function returns the cummulative score of an array (0-100)"""
        from itertools import accumulate
   
    
    
        cum_bed=list(accumulate(bed))
        cum_beds=[round(i,2) for i in cum_bed]

        return cum_beds




    def Percentiles(bed_data):
        """This get the percentile for the data passed. 
        it returns  a dataframe of the percentage passing,percentile of the data
        and the bed_data.
        """
        sedi_passing=[5,16,25,50,75,84,95,100]
   
        bed=bed_data
       
        sed_passing=[str(i)+ '%' for i in sedi_passing]
        percentiles= dict(zip(sed_passing,bed))
   
        return percentiles
        

