#Object



class GrainViz():

    
    def help():
       print( '''Generate a DataFrame(Spread Sheet of the data),
        Initial plot of the Cumulative Mass Retain Vs Phi_scale,
        to pick the percentiles of interest on the Phi scale.''')
    
    def Data_Frame(q,phi,bed_data):
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
    
    



    def plot_data_point(data,name_of_bed,fig=False,save_data=False):
        
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
        
        elif fig == True or save_data =True:
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
           
   
    
    
    
    
    
  
GrainViz = GrainViz