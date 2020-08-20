#The Object 
import math 

import pandas as pd 
import numpy as np



from matplotlib.ticker import AutoMinorLocator,FormatStrFormatter
import matplotlib.pyplot as plt
from matplotlib import style
from matplotlib.widgets import Cursor,Button


style.use('ggplot')

%matplotlib inline






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
        


#Object


class GrainViz():

    
    def InfoHelp():
       print( '''Generate a DataFrame(Spread Sheet of the data),
        Initial plot of the Cumulative Mass Retain Vs Phi_scale,
        to pick the percentiles of interest on the Phi scale.''')
    
    def DataFrame(q,phi,bed_data):
        """
        Passing the dictionary, from the percentile function, 
        the phi scale list/array.
        the bed_data.
        """
    
    

        Outcrop_Bed_data= dict(zip(phi,bed_data))
        Outcrop_Bed= pd.DataFrame(Outcrop_Bed_data.items(), columns= ['Phi_scale','Cummulative_Mass_Retained'])
    
        percentile_table=pd.DataFrame(q.items(),columns=['Percentiles','Percentile_Passings' ])
        percentile_table.drop(['Percentile_Passings'],1, inplace=True)
    
        Out=percentile_table.join(Outcrop_Bed)
    
    
        return Out
    

    def DataFrame_PhiPercentiles(data,phi_percentile):
        data['Percentile_Grain_size_(Phi)']=phi_percentile
        return data
    
    



    def DataPlot(data,name_of_bed,fig=False,save_data=False):
        
        if fig == True or save_data == False:
            """Plots the Cuumulative Mass Retained vs the Phi Scale for easy picking of the percentiles"""
            fig,ax=plt.subplots(figsize=(10,8))
            plt.plot(data['Phi_scale'],data['Cummulative_Mass_Retained'])
            plt.scatter(data['Phi_scale'],data['Cummulative_Mass_Retained'])
            ax.xaxis.set_minor_locator(AutoMinorLocator(n=5))
            ax.yaxis.set_minor_locator(AutoMinorLocator(n=5))
            ax.xaxis.set_minor_formatter(FormatStrFormatter("%.1f"))
            ax.yaxis.set_minor_formatter(FormatStrFormatter("%.0f"))
       

            plt.rc('grid', linestyle="-", color='black')
            ax.spines['bottom'].set_color('1.5')
            ax.spines['top'].set_color('1.5')
            ax.spines['right'].set_color('1.5')
            ax.spines['left'].set_color('1.5')
            plt.grid(True, which='minor', color='k', linestyle='-')
            plt.grid(True, which='major', color='r', linestyle='-')
 
            plt.xlabel('Grain Size (Phi)',fontsize=16)
            plt.ylabel('Cumulative Mass Retained (%)',fontsize=16)
            plt.title(f'Cummulative Frequncy Curve {name_of_bed}',fontsize=20,fontweight='bold')
            fig.savefig(f'{name_of_bed}.png',pdi=fig.dpi)
           
            
        
        elif fig == False or save_data == True:
            """Plots the Cuumulative Mass Retained vs the Phi Scale for easy picking of the percentiles"""
            fig,ax=plt.subplots(figsize=(10,8))
            plt.plot(data['Phi_scale'],data['Cummulative_Mass_Retained'])
            plt.scatter(data['Phi_scale'],data['Cummulative_Mass_Retained'])
            ax.xaxis.set_minor_locator(AutoMinorLocator(n=5))
            ax.yaxis.set_minor_locator(AutoMinorLocator(n=5))
            ax.xaxis.set_minor_formatter(FormatStrFormatter("%.1f"))
            ax.yaxis.set_minor_formatter(FormatStrFormatter("%.0f"))
       

            plt.rc('grid', linestyle="-", color='black')
            ax.spines['bottom'].set_color('1.5')
            ax.spines['top'].set_color('1.5')
            ax.spines['right'].set_color('1.5')
            ax.spines['left'].set_color('1.5')
            plt.grid(True, which='minor', color='k', linestyle='-')
            plt.grid(True, which='major', color='r', linestyle='-')
 
            plt.xlabel('Grain Size (Phi)',fontsize=16)
            plt.ylabel('Cumulative Mass Retained (%)',fontsize=16)
            plt.title(f'Cummulative Frequncy Curve {name_of_bed}',fontsize=20,fontweight='bold')
            
            data.to_csv(f'{name_of_bed}.csv', index=False)
        
        elif fig == True or save_data == True:
            """Plots the Cuumulative Mass Retained vs the Phi Scale for easy picking of the percentiles"""
            fig,ax=plt.subplots(figsize=(10,8))
            plt.plot(data['Phi_scale'],data['Cummulative_Mass_Retained'])
            plt.scatter(data['Phi_scale'],data['Cummulative_Mass_Retained'])
            ax.xaxis.set_minor_locator(AutoMinorLocator(n=5))
            ax.yaxis.set_minor_locator(AutoMinorLocator(n=5))
            ax.xaxis.set_minor_formatter(FormatStrFormatter("%.1f"))
            ax.yaxis.set_minor_formatter(FormatStrFormatter("%.0f"))
       

            plt.rc('grid', linestyle="-", color='black')
            ax.spines['bottom'].set_color('1.5')
            ax.spines['top'].set_color('1.5')
            ax.spines['right'].set_color('1.5')
            ax.spines['left'].set_color('1.5')
            plt.grid(True, which='minor', color='k', linestyle='-')
            plt.grid(True, which='major', color='r', linestyle='-')
 
            plt.xlabel('Grain Size (Phi)',fontsize=16)
            plt.ylabel('Cumulative Mass Retained (%)',fontsize=16)
            plt.title(f'Cummulative Frequncy Curve {name_of_bed}',fontsize=20,fontweight='bold')
            fig.savefig(f'{name_of_bed}.png',pdi=fig.dpi)
            data.to_csv(f'{name_of_bed}.csv', index=False)
            
            
        else:
              
            """Plots the Cuumulative Mass Retained vs the Phi Scale for easy picking of the percentiles"""
            fig,ax=plt.subplots(figsize=(10,8))
            plt.plot(data['Phi_scale'],data['Cummulative_Mass_Retained'])
            plt.scatter(data['Phi_scale'],data['Cummulative_Mass_Retained'])
            ax.xaxis.set_minor_locator(AutoMinorLocator(n=5))
            ax.yaxis.set_minor_locator(AutoMinorLocator(n=5))
            ax.xaxis.set_minor_formatter(FormatStrFormatter("%.1f"))
            ax.yaxis.set_minor_formatter(FormatStrFormatter("%.0f"))
       

            plt.rc('grid', linestyle="-", color='black')
            ax.spines['bottom'].set_color('1.5')
            ax.spines['top'].set_color('1.5')
            ax.spines['right'].set_color('1.5')
            ax.spines['left'].set_color('1.5')
            plt.grid(True, which='minor', color='k', linestyle='-')
            plt.grid(True, which='major', color='r', linestyle='-')
 
            plt.xlabel('Grain Size (Phi)',fontsize=16)
            plt.ylabel('Cumulative Mass Retained (%)',fontsize=16)
            plt.title(f'Cummulative Frequncy Curve {name_of_bed}',fontsize=20,fontweight='bold')
           
   
    
    
    
    
    
class GrainStatsDes():
    def help():
        print('''A suite of codes that calculate the Graphic Mean, Graphic Standard  Deviation, Kurtosis and Skewness''')
    
    
    
    def GraphicMean(data):
    
        '''A function to calculate the graphic mean for the Data using the 16th, 50th, 84th percentiles'''

    
    #     percentiles = [16,50,84]
        phi_percentile=list(data['Percentile_Grain_size_(Phi)'])
   
        
        sumation=phi_percentile[1] + phi_percentile[3] + phi_percentile[5]
     
    
        graphicMean= round((sumation/3),2)
        
        return graphicMean

    
    def GraphicStandard_Dev(data):
    
        '''A function to calculate the graphic standard deviation for the Data 
        using the 95th, 5th, 84th,16th percentiles'''

    #     percentiles_right = [95,5]
    #     percentiles_left = [84,16]
        phi_percentile=list(data['Percentile_Grain_size_(Phi)']) 
    
    
    
#     for i in percentiles_left:
#         left_side.append(round(np.percentile(data.Phi_scale,i),2))
    
    
#     for j in percentiles_right:
#         right_side.append(round(np.percentile(data.Phi_scale,j),2))

        left_math = phi_percentile[5] - phi_percentile[1]
        right_math = phi_percentile[6] - phi_percentile[0]
    
        graphic_std = round((left_math/ 4) + (right_math/6.6),2)
        
        return graphic_std
    
    
    def GraphicSkewness(data):
        '''Function of the graphic_skewness using the 5th, 16th, 50th, 84th,95th percentiles'''
        #percentiles = [5,16,50,84,95]
    
        phi_percentile=list(data['Percentile_Grain_size_(Phi)'])
    
    
    
        left_numerator = phi_percentile[5] + phi_percentile[1]- (2 * phi_percentile[3])
        right_numerator = (phi_percentile[6] + phi_percentile[0])- (2* phi_percentile[3])
    
        left_denometer = 2 *(phi_percentile[5]- phi_percentile[1])
        right_denometer = 2 *(phi_percentile[6] - phi_percentile[0])
        graph_skew = round((left_numerator/left_denometer) + (right_numerator/right_denometer),3)



        return graph_skew
    
    
    
    def GraphicKurtosis(data):
        '''
        This is a function for Graphic Kurtosis, using the 5th, 25th,75th and the 95th percentile
        '''
    
    #     percentile = [5,25,75,95]
    
        phi_percentile=list(data['Percentile_Grain_size_(Phi)'])
    
        numerator = phi_percentile[6] - phi_percentile[0]
        denumator = 2.44*(phi_percentile[4] - phi_percentile[3])
    
        graphic_kurtosis = round((numerator / denumator),2)
        return graphic_kurtosis
    
    

    
GrainStatsDes=GrainStatsDes



class GrainDataTables():
    
    
    def help():
        print('''Input the very First Bed Data into the BedData function,
        Then when passing the rest of the bed data
        you include the first data initiated and the data points for other beds. ''')
    
    
    
    def BedData(name_of_bed,graphic_mean,graphic_std,graphic_skewness,graphic_kurtosis):
    
        name = name_of_bed
        graphic_mean=graphic_mean
        graphic_standard_dev=graphic_std
        graphic_skewness = graphic_skewness
        graphic_kurtosis= graphic_kurtosis
        
        bed_stat_data = pd.DataFrame({'Name_of_bed':[name],
                      'Graphic Mean':[graphic_mean],
                      'Graphic Standard deviation':[graphic_standard_dev],
                       'Graphic Skewness':[graphic_skewness],
                      'Graphic Kurtosis':[graphic_kurtosis]
                     })
    
        return bed_stat_data

    def CompleteBeds(bed_stat,name_of_bed,graphic_mean,graphic_std,graphic_skewness,graphic_kurtosis):
    
        name = name_of_bed
        graphic_mean=graphic_mean
        graphic_standard_dev=graphic_std
        graphic_skewness = graphic_skewness
        graphic_kurtosis= graphic_kurtosis
        
        update={'Name_of_bed':name,
                      'Graphic Mean':graphic_mean,
                      'Graphic Standard deviation':graphic_standard_dev,
                       'Graphic Skewness':graphic_skewness,
                      'Graphic Kurtosis':graphic_kurtosis
                     }
        bed_stat =bed_stat.append(update,ignore_index=True)
    
        return bed_stat
    
    def SaveBeds(data,name_of_rock_unit):
        '''Saves Bed Grains stats from the CompleteBeds and creates a CSV file in your Present working Directory.'''
        data=data
        name= name_of_rock_unit
    
        data.to_csv(f'{name}.csv')
    
    
    
    
GrainDataTables = GrainDataTables