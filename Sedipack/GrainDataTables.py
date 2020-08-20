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