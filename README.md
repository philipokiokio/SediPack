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
* MM_to_Phi()

* Bed_To_100()

* CummulateBed()

* Percentiles()

2. GrainViz: houses serveral calls which are

* DataFrame()

* DataFrame_PhiPercentiles()


* DataPlot()

3. GrainStatsDes: houses several calls which are 

* GraphicMean()

* GraphicStandard_Dev()

* GraphicSkewness()

* GraphicKurtosis()


4. GrainDataTables: houses several call which are 

* BedData()

* CompleteBeds()

* SaveBeds()



Which call contains a docstring which contains information on how to use it.


# How to use this package.


To use the function present in this package, the package has to be installed and that can be done with `pip install sedipack`.

Then importing the functionalities needed,

`from sedipack.grainpreprocess import GrainPreprocess`

`from sedipack.grainviz import GrainViz`

`from sedipack.grainstats import GrainStatsDes`

`from sedipack.grainstatsdata import GrainDataTables`
 

 Once this has been done then you can initialize the import,
 `viz = GrainViz()` Then all other functionality can be gotten with a dot call.
 `viz.DataPlot()`.

 Using `viz.infohelp()` provides info about the type of functionality present and each method contains docstrings showing both inputs and outputs.

### Acknowledgements

I will like to also acknowledge the input of mentors and friends in this project.

1. Olawale Ibrahim (Machine Learning Engineer & The Author of Petroeval) & Emmanuel Jolaiya ( Machine Learning Engineer & The Author of rsgis and the Famous GISBOT on Twitter)

2. You  for using and reading this, Thank you.


Thank you all.

Philip Ireoluwa Okiokio