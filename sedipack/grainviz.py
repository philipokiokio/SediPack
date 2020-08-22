

#The Object 
import math 

import pandas as pd 
import numpy as np



from matplotlib.ticker import AutoMinorLocator,FormatStrFormatter
import matplotlib.pyplot as plt
from matplotlib import style
from matplotlib.widgets import Cursor,Button



class GrainViz():
    def __init__(self,f=None):
        self.f=f        
    
    def InfoHelp():

        '''
        Class Help
        '''
        print( '''Generate a DataFrame(Spread Sheet of the data)\n,
        Initial plot of the Cumulative Mass Retain Vs Phi_scale\n,
        to pick the percentiles of interest on the Phi scale.''')
    
    def DataFrame(self,q,phi,bed_data):

        """
        Argss::
            Passing the dictionary, from the percentile function, 
            the phi scale list/array.
            the bed_data.

        Returns:
            DataFrame object
        """
    
        self.q=q
        self.phi = phi

        assert self.phi == list, "phi must be a list"
        self.bed_data = bed_data

        Outcrop_Bed_data= dict(zip(self.phi,self.bed_data))
        Outcrop_Bed= pd.DataFrame(Outcrop_Bed_data.items(), columns= ['Phi_scale','Cummulative_Mass_Retained'])
    
        percentile_table=pd.DataFrame(self.q.items(),columns=['Percentiles','Percentile_Passings' ])
        percentile_table.drop(['Percentile_Passings'],1, inplace=True)
    
        Out=percentile_table.join(Outcrop_Bed)
    
    
        return Out
    

    def DataFrame_PhiPercentiles(self,data,phi_percentile):
        """
        Argss:: Data(DataFrame)
        Phi_percentile (list or array of the precentiles)


        Returns:
        DataFrame.
        
        
        """
        assert self.phi_percentile == list, "phi_percentile must be a list"
        self.data =data
        self.phi_percentile = phi_percentile

        self.data['Percentile_Grain_size_(Phi)']=self.phi_percentile
        return self.data
    
    



    def DataPlot(self,data,name_of_bed,fig=False,save_data=False):

        '''
        Method to plot data
        args::
            data: Data to be plotted
            name_of_bed: Bed to be plotted
            fig =False (To plot a shart without saving the plot) or Yes (to save the plot)
            save_data = False(This prevent the data from saving as a CSV file to save, pass True)
        '''
        self.data = data
        self.name_of_bed = name_of_bed
        self.fig = fig
        self.save_data = save_data
        
        assert self.name_of_bed == str, "Name of Bed must be a String"

        if self.fig == True or self.save_data == False:
            """Plots the Cuumulative Mass Retained vs the Phi Scale for easy picking of the percentiles"""
            fig,ax=plt.subplots(figsize=(10,8))
            plt.plot(self.data['Phi_scale'],self.data['Cummulative_Mass_Retained'],color='blue')
            plt.scatter(self.data['Phi_scale'],self.data['Cummulative_Mass_Retained'], color = 'blue')
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
            plt.title(f'Cummulative Frequncy Curve {self.name_of_bed}',fontsize=20,fontweight='bold')
            fig.savefig(f'{self.name_of_bed}.png',pdi=fig.dpi)
           
            
        
        elif self.fig == False or self.save_data == True:
            """Plots the Cuumulative Mass Retained vs the Phi Scale for easy picking of the percentiles"""
            fig,ax=plt.subplots(figsize=(10,8))
            plt.plot(self.data['Phi_scale'],self.data['Cummulative_Mass_Retained'],color = 'blue')
            plt.scatter(self.data['Phi_scale'],self.data['Cummulative_Mass_Retained'],color = 'blue')
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
            plt.title(f'Cummulative Frequncy Curve {self.name_of_bed}',fontsize=20,fontweight='bold')
            
            data.to_csv(f'{self.name_of_bed}.csv', index=False)
        
        elif self.fig == True or self.save_data == True:
            """Plots the Cuumulative Mass Retained vs the Phi Scale for easy picking of the percentiles"""
            fig,ax=plt.subplots(figsize=(10,8))
            plt.plot(self.data['Phi_scale'],self.data['Cummulative_Mass_Retained'],color = 'blue')
            plt.scatter(self.data['Phi_scale'],self.data['Cummulative_Mass_Retained'],color = 'blue')
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
            plt.title(f'Cummulative Frequncy Curve {self.name_of_bed}',fontsize=20,fontweight='bold')
            fig.savefig(f'{self.name_of_bed}.png',pdi=fig.dpi)
            data.to_csv(f'{self.name_of_bed}.csv', index=False)
            
            
        else:
              
            """Plots the Cuumulative Mass Retained vs the Phi Scale for easy picking of the percentiles"""
            fig,ax=plt.subplots(figsize=(10,8))
            plt.plot(self.data['Phi_scale'],self.data['Cummulative_Mass_Retained'],color = 'blue')
            plt.scatter(self.data['Phi_scale'],self.data['Cummulative_Mass_Retained'],color = 'blue')
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
            plt.title(f'Cummulative Frequncy Curve {self.name_of_bed}',fontsize=20,fontweight='bold')
           
   
    
    
    
    
