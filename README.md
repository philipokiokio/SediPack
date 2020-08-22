# Sedipack 

This is a simple package that is created to provide support to earth scientist and earth engineers (students in particular). This package seeks to help create an open-source solution to grain-size statistical analysis, and the production of grain plots.

Sedi pack is born out of the problems faced during the earlier days of the my Senior year project. The Problem I faced was: Software and Activation Keys which is or was expensive to get. After Which I then thought to my self why was there no existing way to do it in python. Then I went to work.



# Available Functions/Processes.

The Package comprises of 4 Houses  of serveral functions.

1. *GrainPreprocess.*
2. *GrainViz.*
3. *GrainStasDes.*
4. *GrainDataTables.*

## Methods Available.

There are about 14 functions/method that vcan be called and returns various data points.

1. GrainPreprocess: has four calls that can be made. which are 
    * MM_to_Phi(): converts the Sieve sizes from MM to Phi scale.

    * Bed_To_100(): Standardize the Bed to 100 if it is less than 100/ more.

    * CummulateBed(): Get the accumlated score of the bed.

    * Percentiles(): returns a Dictionary that contains the accmulated bed and percentiles.

2. GrainViz: houses serveral calls which are

    * DataFrame(): This produces a table/DataFrame of the available data points.

    * DataFrame_PhiPercentiles(): This is used to add the percentiles that was/has been manually read of the plots in the DataFrame.

    * DataPlot(): Plots the DataFrame of the Cummulative Mass retained (%) vs the Grain Size (Phi Scale). This Function gives you the ability to save the plot and also name the plot please check the docstrings. 

3. GrainStatsDes: houses several calls which are 

    * GraphicMean(): Calculates the Graphic Mean of the beds.

    * GraphicStandard_Dev():Calculates the Graphic Standard deviation of the beds.

    * GraphicSkewness(): Calculates the Graphic Skewness of the beds.

    * GraphicKurtosis():Calculates the Graphic Kurtosis of the beds.


4. GrainDataTables: houses several call which are 

    * BedData(): Creates the Bed DataFrame/Table for the grain statistics done.

    * CompleteBeds(): Completes the Bed DataFrame/Table for the grain statistics done after the first bed data has been created. The first BedData which is created with BedData is then passed as the first argument in CompleteBeds method.

    * SaveBeds(): this method saves the data above as a `.csv file`. Comma seperated values.



**Each method call contains a docstring which contains information on how to use it.**


# How to use this package.


To use the function present in this package, the package has to be installed and that can be done with `pip install sedipack`.

Then importing the functionalities needed,

`from sedipack.grainpreprocess import GrainPreprocess`

`from sedipack.grainviz import GrainViz`

`from sedipack.grainstats import GrainStatsDes`

`from sedipack.grainstatsdata import GrainDataTables`
 



# Sample Code Presentation.
So Here are code snippets on how call each method,

* To install the package

To install the package type in the command
```
pip install sedipack
```
This will always install the latest version that has been released.


* Then importing the functionalities needed,

```
from sedipack.grainpreprocess import GrainPreprocess

from sedipack.grainviz import GrainViz

from sedipack.grainstats import GrainStatsDes

from sedipack.grainstatsdata import GrainDataTables

```


* The intialiazation of the imports.

 
```
preprocess= GrainPreprocess()

viz = GrainViz()

stats = GrainStats()

stats = GrainDataTables()
```


* Calling of the methods.

```
Preprocess.MM_ToPhiScale()
```


Then all other functionality can be gotten with a dot call
 

 Using `viz.infohelp()` provides info about the type of functionality present and each method contains docstrings showing both inputs and outputs.



# Updates to be made in Future Versions.

- [ ] Bivariate Plot of Skewness vs Standard deviation( for delinating Beach Sands and River Sands)
- [ ] An automated way to pick the Percentiles with respect to the line plot on the X-axis accurately.
- [ ] Expand the Sedimentological packages to include stratigraphy.
- [ ] Work on a Sedimentological plotting library for beds and its type.

# LICENSE.

**GNU GENERAL PUBLIC LICENSE**


# State of the Project.

I hereby declare this project Open Source in the Universe Name (Jesus and God in my Case.)!
yes anyone can contribute.

# Role Call of Contributors.
List of contributors to this project. To get your name Here contribute.


1. Olawale Ibrahim and Emmanuel Jolaiya.
2. 




### Acknowledgements

I will like to also acknowledge the input of mentors and friends in this project.

1. Olawale Ibrahim(Machine Learning Engineer & The Author of Petroeval) &  Emmanuel Jolaiya( Machine Learning Engineer & The Author of rsgis and the Famous GISBOT on Twitter)

2. You  for using and reading this, Thank you.


Thank you all.

Philip Ireoluwa Okiokio