<!-- page:1 -->
# Mystic User Guide

Version O-2018.06, June 2018

# Copyright and Proprietary Information Notice

<!-- page:2 -->
© 2018 Synopsys, Inc. This Synopsys software and all associated documentation are proprietary to Synopsys, Inc. and may only be used pursuant to the terms and conditions of a written license agreement with Synopsys, Inc. All other use, reproduction, modification, or distribution of the Synopsys software or the associated documentation is strictly prohibited.

# Destination Control Statement

All technical data contained in this publication is subject to the export control laws of the United States of America. Disclosure to nationals of other countries contrary to United States law is prohibited. It is the reader’s responsibility to determine the applicable regulations and to comply with them.

# Disclaimer

SYNOPSYS, INC., AND ITS LICENSORS MAKE NO WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, WITH REGARD TO THIS MATERIAL, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.

# Trademarks

Synopsys and certain Synopsys product names are trademarks of Synopsys, as set forth at https://www.synopsys.com/company/legal/trademarks-brands.html. All other product or company names may be trademarks of their respective owners.

# Free and Open-Source Licensing Notices

If applicable, Free and Open-Source Software (FOSS) licensing notices are available in the product installation.

# Third-Party Links

Any links to third-party websites included in this document are for your convenience only. Synopsys does not endorse and is not responsible for such websites and their practices, including privacy practices, availability, and content.

Synopsys, Inc.

Mountain View, CA 94043

www.synopsys.com

<!-- page:3 -->
# Contents

# 1 Introduction and Overview 6

1.1 Mystic Reference Guide 6   
1.2 Setup and Installation 7   
1.3 Running Mystic 7   
1.4 Command Line Options . . 7

1.4.1 Enigma Database Connections 8   
1.4.2 SPICE Simulator 9   
1.4.3 Supported SPICE Models 10   
1.4.4 Supported Optimisers 10

# 2 SPICE Model Extraction 12

2.1 Uniform Model Extraction 12

2.1.1 Exporting TCAD Data 12   
2.1.2 Loading a SPICE model 13   
2.1.3 Loading TCAD Simulation Data . . 13   
2.1.4 Manipulating Data 14   
2.1.5 Setting Up Optimisation Parameters 15   
2.1.6 Extraction . 17   
2.1.7 Error Calculation 18   
2.1.8 Outputting Data . 18

2.2 Statistical Extraction 20   
2.3 Device CV Parameter Extraction 20

2.3.1 Mystic DB CV Variables . 21

2.4 Using Verilog Models . 21

2.4.1 Debugging Verilog Model Usage . . 23

2.4.2 HSPICE Setup 24   
2.4.3 Examples 26

<!-- page:4 -->
2.5 Sub-Circuit Models 27

2.5.1 Sub-Circuit Model-Specific Commands 27   
2.5.2 Sub-Circuit Extraction with Verilog Models . 28   
2.5.3 Instance Parameters in Sub-Circuits 28   
2.5.4 Example 29

# 3 Mystic Command Reference 31

3.1 Global Objects 31

3.1.1 Optimisation Routines 33

3.2 Error Calculation Methods 40

3.2.1 Mean 40   
3.2.2 RMSD 41   
3.2.3 NRMSD 41

# 4 Mystic Database 42

4.1 Loading TCAD Data 42

4.1.1 Examples 43

4.2 Storing Mystic Fit Information 44

4.2.1 Creating a Mystic Project . . 44   
4.2.2 Deleting a Mystic Project . . 45   
4.2.3 Creating a Mystic Dataset 45   
4.2.4 Storing Mystic Fit Information . 46

4.3 Retrieving Mystic Fit Information 46

4.3.1 GetFitData 46   
4.3.2 GetModelCard 47   
4.3.3 GetInitialModel . 47   
4.3.4 GetFitParameters 47

<!-- page:5 -->
4.3.5 GetFitModel 48

4.4 Multi-Stage Extraction Example 48

4.4.1 Extraction Stage 1 48

4.4.2 Extraction Stage 2 49

# A Garand Dataset Type Strings 51

A.1 Id-Vg Simulation 51

A.2 Id-Vd Simulation 52

A.3 Vt Simulation 52

# Index 55

<!-- page:6 -->
# 1 Introduction and Overview

Mystic is a SPICE model extraction tool, specifically designed to facilitate the automated extraction of SPICE models that accurately capture the effects of process and statistical variability on transistor performance. Mystic supports the extraction of the current industry standard CMOS models including BSIM4, BSIM-CMG, BSIM-IMG, UTSOI and PSP, as well as VerilogA models such as Leti-NSP. Mystic also provides support for basic sub-circuit model extraction. It has been designed to perform semiautomated extraction of very large ensembles of SPICE models within the Synopsys TCAD to SPICE toolchain.

The Mystic environment provides a Python-scriptable suite of tools for SPICE model extraction, and therefore some familiarity with the Python language is required to use and understand Mystic. For those unfamiliar with Python, we recommend the tutorial on the Python website, and the following books:

■ Programming Python[1] by Mark Lutz   
■ Dive into Python[2] by Mark Pilgrim (Available online at http://www.diveintopython.net/)

It also provides communication with the Enigma TCAD to SPICE backend database, acting as the primary link between TCAD data and a variability-aware SPICE model.

# 1.1 Mystic Reference Guide

The Mystic environment provides a custom Python[3] environment with a range of objects and classes which are designed to aid the process of compact model extraction. Documentation for these objects is provided in the HTML Mystic API Reference which is installed along with the software and can be found in:

```shell
$STROOT/tcad/O-2018.06/manuals/tcad_spice/mystic_api 
```

They can be opened using any standard Web browser by running [browser\_cmd] \$STROOT/tcad/O-2018.06/manuals/tcad\_spice/mystic\_api/index.html or by opening file://\$STROOT/tcad/O-2018.06/manuals/tcad\_spice/mystic\_api/index.html in your web browser. They provide an interactive and searchable reference guide to the Mystic environment, the objects and classes available to the user, and the interfaces and capabilities that they provide.

<!-- page:7 -->
# 1.2 Setup and Installation

For detailed setup and installation instructions, see the Synopsys TCAD O-2018.06 installation notes.

# 1.3 Running Mystic

For instructions on setting up Mystic, refer to the Synopsys TCAD installation notes.

Once the TCAD to SPICE tools are loaded into your environment, Mystic can be run as follows:

```txt
Mystic <Strategy> -d <DBFile> -m <ModelFile> [Optional Arguments] 
```

# 1.4 Command Line Options

The command line options and optimisers that are supported by Mystic are summarised in Tables 1.1 and 1.3.

<table><tr><td>Short Flag</td><td>Long Flag</td><td>Arguments</td><td>Description</td><td>Type</td></tr><tr><td></td><td></td><td>Filename</td><td>Filename containing the extraction strategy to execute.</td><td>Required</td></tr><tr><td>-h</td><td>--help</td><td>-</td><td>Print usage help message and command line arguments then exit.</td><td>Optional</td></tr><tr><td>-v</td><td>--version</td><td>-</td><td>Print the Mystic version number and then exit.</td><td>Optional</td></tr><tr><td>-d</td><td>--db</td><td>Filename Database URI</td><td>Location of Enigma database configuration file. See 1.4.1.</td><td>Required</td></tr><tr><td>-ds</td><td>--dataset</td><td>Dataset</td><td>Name of dataset in which to store Mystic extraction data.</td><td>Optional</td></tr><tr><td>-o</td><td>--optimiser</td><td>Optimiser</td><td>Selects the optimiser to use for this particular execution of the strategy. See Table 1.3 on page 10.</td><td>Optional</td></tr><tr><td>-m</td><td>--modelfile</td><td>Filename</td><td>The filename of the initial model card to be loaded by Mystic.</td><td>Optional</td></tr><tr><td>-a</td><td>--script-args</td><td>string</td><td>A string containing any extra arguments to be passed to the user&#x27;s extraction strategy.</td><td>Optional</td></tr><tr><td>-x</td><td>--spice-args</td><td>string</td><td>A string containing any extra command line arguments to be passed to the back-end SPICE simulator. (See section 1.4.2 for more information)</td><td>Optional</td></tr><tr><td>-l</td><td>--location</td><td>string</td><td>Full path to a SPICE executable of the same type as that specified using the -s flag. This allows the user to override the system path.</td><td>Optional</td></tr></table>

Table 1.1: Mystic command line options

<!-- page:8 -->
# 1.4.1 Enigma Database Connections

As an input Mystic requires a database that contains the target data supplied by the user that is to be used as the fitting target of the SPICE model extraction process. This must be provided via the command line flags -d or --db. All support for postgres and SQLite databases has been deprecated in favour of MongoDB. The flag passed must be the path to an active Enigma MongoDB database. For more information on MongoDB and Enigma, refer to the Enigma User Guide.

<!-- page:9 -->
A pre-created dataset name can also be passed on the command line using the -ds or --dataset command line flag. This dataset will be attached to the Mystic database interface in the extraction environment and any data stored will be pushed to here. For more information on this working model, consult the Enigma user guide or the Mystic API reference.

When Mystic is run by Enigma, either standalone, or through Sentaurus Workbench, the database connection, including the creation and propagation of a dataset arguement, is handled for you.

# 1.4.2 SPICE Simulator

# Supported SPICE simulators

Support for all simulators apart from Synopsys HSPICE[4] has been removed. The -l flag allows you to pass the location of a specific executable of HSPICE. If this is not supplied, Mystic will use whichever version of HSPICE is loaded into the current working environment.

# Simulator Options

You can use the -x flag to pass additional arguments to HSPICE. This can be advantageous in situations where you want to set parameters for SPICE or specific models require the running of SPICE with nondefault command line flags.

# HSPICE Performance

Due to the large number of calls to SPICE required in an optimisation, Mystic extractions using an HSPICE back end can be slowed by license checkouts and software initialisation times.

This can be mediated by running HSPICE in advanced server mode, which reduces the individual simulation set up and tear down time. Instead of checking out an HSPICE license for every job spawned by Mystic, a single license is checked out at the start of the Mystic extraction and held until the extraction has concluded. This can be achieved by passing the ’-C’ or ’-CC’ flag to HSPICE via the Mystic command line. For example:

```batch
Mystic Stage1.py -d mongodb.conf -m InitialModel.mod -s hspice -x "-C" 
```

In some cases this can reduce the execution time of a Mystic extraction by as much as 5 times compared to running in non-server mode.

Note: When HSPICE is run in server mode it may not always be possible for Mystic to shut down the server in the case of a crash or abnormal exit. It is sensible to check to make sure that all HSPICE processes have been terminated after the conclusion of the Mystic job to make sure licenses are not accumulated.

<!-- page:10 -->
# 1.4.3 Supported SPICE Models

Mystic has native support for a range of SPICE models (See Table 1.2). Note that although Mystic may have native support for a specific SPICE model version, HSPICE must also provide support for this model in order to ensure correct operation.

If you require support for a model that is not listed here, contact your Synopsys sales representative.

<table><tr><td>Model</td><td>Technology Type</td><td>Level</td><td>Versions</td></tr><tr><td>BSIM 3[5]</td><td>Planar Bulk</td><td>49</td><td>3.2.4,3.3</td></tr><tr><td>BSIM 4[6]</td><td>Planar Bulk</td><td>54</td><td>4.0-4.8</td></tr><tr><td>BSIM-CMG[7]</td><td>Bulk FinFET, SOI FinFET, Nanowire</td><td>72</td><td>104-110</td></tr><tr><td>BSIM-IMG[8]</td><td>Planar SOI</td><td>78</td><td>102.6.1, 102.7</td></tr><tr><td>UTSOI[9]</td><td>FD-SOI, PD-SOI</td><td>76</td><td>1.11, 1.12, 2.11</td></tr><tr><td>PSP[10]</td><td>Planar Bulk</td><td>69</td><td>102.2,102.3</td></tr></table>

Table 1.2: Mystic supported SPICE models.

The SPICE model object Mystic injects into the extraction environment is determined by the level number supplied in the initial model card passed into Mystic using the -m command line flag. If a level number is supplied that is not in Table 1.2, Mystic will create a generic Model object that stores no information about the parameters or their bounds. If a level number does not exist in the supplied model card, Mystic will assume the SPICE model is Verilog-A, and it creates a Verilog Model to pass into the extraction environment. For more information on extracting Verilog models see Section 2.4.

# 1.4.4 Supported Optimisers

The Optimiser library supports four different backends, and each backend provides one or more optimisation method.

<table><tr><td>Optimiser Backend</td><td>Default Optimisation Method</td><td>Command Line Argument</td></tr><tr><td>Intel MKL Bounded Trust Region</td><td>Bounded Trust Region</td><td>BOUNDED_TRUST_REGION</td></tr><tr><td>Intel MKL Unbounded Trust Region</td><td>Unbounded Trust Region</td><td>TRUST_REGION</td></tr><tr><td>Scipy Least Squares</td><td>Bounded Trust Region</td><td>scipy_least_squares</td></tr><tr><td>Scipy Minimize</td><td>L-BFGS-B</td><td>scipy_minimize</td></tr></table>

Table 1.3: Supported optimisers in Mystic.

If one of scipy’s backends are chosen, the optimisation method can be changed in the Mystic script. For a more detailed decription of the available optimisation routines and optional parameters, see Section 3.1.

<!-- page:12 -->
# 2 SPICE Model Extraction

This section covers the process of running a SPICE model extraction strategy using Mystic and the general steps that an extraction procedure involves.

# 2.1 Uniform Model Extraction

In general, the process of extracting a uniform model is composed of several sub-steps, as documented in [11]. Initially, parameters are extracted against the long channel characteristics of the device in question. From there, parameters are extracted to match the low drain electrostatic performance of the device, followed by low drain transport parameters. Finally, we extract against high drain and $I _ { D } V _ { D }$ characteristics to complete the fit. In addition, parameters for effects such as temperature dependence can be extracted using further stages. The extracted uniform model then becomes the base for the variability SPICE model extraction process.

The remainder of this section will provide a step-by-step guide to the processes involved in an extraction stage, such as importing and processing target data, running the optimisation loop and outputting results.

# 2.1.1 Exporting TCAD Data

Before an extraction can be performed, the TCAD simulation target data must be loaded into an Enigma MongoDB Database so it is accessible through the Mystic DB API. There are multiple different ways this can be done and it will usually be performed as part of a TCAD to SPICE tool flow.

1. Garand Data - If the simulation data is coming from Garand run through Enigma, the data will have been uploaded to the Database at run time.   
2. Enigma - PLT or CSV data can be uploaded through the Enigma database interface prior to running Mystic. For further details on how this can be achieved, please consult the Enigma user guide.

Data browsing can be done through the database GUI MongoDB Compass. Further details of this can be found in the Enigma user guide.

<!-- page:13 -->
# 2.1.2 Loading a SPICE model

There are currently three ways for the user to specify the initial model card to be used:

1. From the command line using the -m or --modelfile   
2. Within the user’s extraction script using the LoadModel function provided by Mystic.   
3. Via a model card stored in the Enigma database from a previous extraction. (See Chapter 4 for more details)

Using any of these methods initialises the Mystic global instance Model to contain the SPICE model with the appropriate file name.

Please note that at least one of the methods of initialising a SPICE model MUST BE USED BEFORE attempting to call DoStage, PrintErrors or any other Mystic function that requires SPICE evaluation in order to complete. If this has not been done then Mystic will exit with an InputDataError at the first attempt to call SPICE.

# 2.1.3 Loading TCAD Simulation Data

When the extraction strategy is executed by Mystic, several objects and modules are preloaded into the execution environment and made available to the user. A full list of the pre-loaded objects is provided in Chapter 3. The database provided by the user on the command line when running Mystic is loaded by the core Mystic engine. The mdb object is loaded into the script environment, providing the user with access to the data. The mdb object provides a method, Load, to which various constraints may be provided in order to select the required TCAD simulation data from the database. Several examples illustrating the use of this method are shown in Loading TCAD Data. More information on the Load method of the mdb interface can be found in the Mystic Reference API.

The Load method returns a SimData object, which is the main storage object used throughout Mystic. The class for this is passed into the extraction environment as a global variable and can be initialised from scratch, however the most common usage model is to initialise the object through the mdb interface using the Load method. In this release, the underlying structure used by SimData objects is the TCAD to SPICE common data container that is used by Enigma and features regularly in TCAD to SPICE flows. A full description of this class can be found in the Enigma API reference. The following example shows how to load target data and print the object to standard output.

```python
## Load data from database.
IdVgld = mdb.Load(instances={"l":25e-9, "w":25e-9},
bias={"drain":0.05, "substrate":0.0})
print(IdVgld) 
```

```txt
Terminals = drain, gate, source, substrate
bias : {'drain': 0.05, 'gate': 0.0, 'source': 0.0, 'substrate': 0.0}
instances : {'1': 2.5e-08}
temperature : 27.0

idrain idrain-fit errors
vgate
0.000000e+00 -4.674308e-09 nan nan
8.000000e-03 -6.086274e-09 nan nan
1.796800e-02 -8.449600e-09 nan nan
3.147796e-02 -1.315784e-08 nan nan
.
.
.
.
.
.
.
.
7.440000e-01 -8.624389e-06 nan nan
7.680000e-01 -8.682976e-06 nan nan
7.920000e-01 -8.735670e-06 nan nan
8.000000e-01 -8.752033e-06 nan nan 
```

<!-- page:14 -->
Reviewing this output confirms that the data you loaded includes only the simulation conditions in which you are interested.

# 2.1.4 Manipulating Data

In SPICE model extraction, it is often necessary to target the fitting of a parameter within a specific region of the device operational characteristics. Unless otherwise specified, the full range of a dataset will be fitted by default. The Filters module provided by the Mystic environment enables the user to filter their data to only the region of interest or applicability.

The Filters module supplies a DataFilter class that can filter data based on the independent and dependent variables and values, respectively. These are then applied by calling the FilterData method of the SimData class, which is Mystic’s primary data container.

In addition to the data filter, it is also possible to create figure of merit “targets” from the data, so that the optimiser can fit to these as well as (or instead of) the data itself. These “targets” can be created using the MakeFoMTarget method of SimData. Currently, Mystic is able to directly fit to the threshold voltage, on-current, off-current and derivatives.

The following examples illustrate how to filter the data based on either the gate voltage or drain current for an $I _ { D } V _ { G }$ curve.

```txt
## Load data from database.
IdVg = mdb.Load(instances={"l":25e-9, "w":25e-9}, bias={"substrate":0.0})
## Filter the data to only include data with a drain bias of 0.05V 
```

```python
IdVgld = IdVg.FilterData('eq', 0.05, dtype="bias.drain")
## Filter for the gate voltage to only include
## bias points with a Vg of <= 0.2V.
Filtered1 = IdVgld.FilterData('le', 0.2, dtype="ivar")
## Filter for the drain current.
Filtered2 = IdVgld.FilterData('ge', 1e-7, dtype="dvar") 
```

To create FoM targets:   
```python
## Load data from database.
IdVg = mdb.Load(instances={"1":25e-9, "w":25e-9},
bias={"d":0.05, "b":0.0})
##
Create a Vt target.
Vt = IdVg.MakeFoMTarget('vt', 1e-7)
##
Create an Ion target.
Ion = IdVg.MakeFoMTarget('ion', 0.9) 
```

<!-- page:15 -->
The filtered data objects and FoM targets can be used in exactly the same way as those loaded directly from the database.

If a figure of merit is not going to used as an extraction target, its valuecan also be extracted directly from the SimData object without using MakeFoMTarget. The following example demonstrates how to extract the Vt of a data structure.

```python
## Load data from database.
IdVg = mdb.Load(instances={"l":25e-9, "w":25e-9},
bias={"d":0.05, "b":0.0})
## Set the FoM criteria and extract.
IdVg.SetFoMCriteria('vt', 1e-7)
Vt = IdVg.Vt() 
```

The figure of merit criteria are initialised with sensible default values but can also be changed using SetFoMCriteria, as show in the example above. The FoM values can then be used in other aspects of the extraction, such as filtering the data.

# 2.1.5 Setting Up Optimisation Parameters

Parameters used in the extraction process must first be set up with appropriate default values and boundaries. Default values can also be loaded from the initial SPICE model using methods in the ExtractionUtils module, which is documented fully in the Mystic API Reference.

<!-- page:16 -->
To set up SPICE model parameters for use in Mystic, the OptParam object is provided to the user. The OptParam object has the following API:

```javascript
OptParam(name, default, minval=None, maxval=None, scale=None) 
```

# Parameters:

<table><tr><td>name</td><td>Name of the SPICE model parameter, e.g. vth0.</td></tr><tr><td>default</td><td>Default value to use for the parameter. This is used only if the parameter does not already exist in the SPICE model.</td></tr><tr><td>minval</td><td>Minimum value to allow for the parameter. (maxval required if minval specified)</td></tr><tr><td>maxval</td><td>Maximum value to allow for the parameter. (minval required if maxval specified)</td></tr><tr><td>scale</td><td>Scaling factor for the parameter.</td></tr></table>

Only the name and default value for the parameter are required. Minimum and maximum values, if given, are only applicable to extractions using bounded optimisers, although Mystic will print warnings if a parameter goes out of the specified bounds regardless of the optimiser used. The scaling factor, if provided, is used to scale the absolute parameter values in order to improve the numerical stability of the optimisation procedure. By default a scaling factor of 1 is used, although this is not necessarily optimal when extracting parameters that have significantly different orders of magnitude.

# Examples

The following example illustrates the creation of a parameter object for the BSIM parameter vth0, with a default value of 0.2, bounded between 0 and 1 V and with a scaling factor of 0.2.

```txt
vth0 = OptParam("vth0", 0.2, 0.0, 1.0, 0.2) 
```

When extracting sub-circuit parameters the following syntax is used:

```txt
vth0 = OptParam("nmos.vth0", 0.2, 0.0, 1.0, 0.2) 
```

Where “nmos” is the name of the model in the netlist. Passive components and .PARAM values can also be optimised against in sub-circuit mode by defining them like so:

```txt
rdrain = OptParam("rdrain", 100.0, 50.0, 1000.0, 100.0) 
```

During an extraction, it might also be useful to link the values of two parameters. For example, when extracting the gate capacitance of a device using BSIM-CMG, you might want gate-drain capacitance (CGDL) and the gate-source capcitance (CGSL) to be identical. Mystic allows you to do this using LinkedOptParams as follows:

```python
cgs1 = OptParam('cgs1', 1e-12, 0.0, 100e-12, 1e-12)
cgdl = LinkedOptParam('cgdl', CGSL) 
```

<!-- page:17 -->
# 2.1.6 Extraction

# Pre-requisites

There are several setup steps necessary before commencing an extraction procedure. As indicated above, data must be exported and then loaded into Mystic, and parameters set up for extraction. For each parameter to be extracted, a new OptParam object must be created, as shown in the previous section. Starting from version O-2018.06, release ParameterSet objects have been deprecated in favour of bare lists, although they will remain in the environment to preserve backwards compatibility. Once the parameter objects have been created, the OptParams can be organised into lists for use by the optimiser. This allows multiple stages to be constructed within an extraction strategy, with each stage optimising a different set of parameters against different sections of target data.

# The Extraction Process

For the extraction process itself, a convenience function called DoStage, is provided by the ExtractionUtils module to automatically set up and run the parameter extraction step. This function has the following API:

```python
result = ExtractionUtils.DoStage(stagename, model, simulator, parameters, optimiser, data, weights=None) 
```

# Parameters:

```txt
stagename Name of the stage. Used as a prefix for output filenames.
model SPICE model to extract parameters for. (Provided by Mystic)
simulator Simulator to use for evaluating the model. (Provided by Mystic)
parameters List of parameters to extract or ParameterSet for releases before O-2018.06.
optimiser Optimiser object to use for extraction. (Provided by Mystic)
data Data to extract the model against.
weights List of weights, allowing particular data to be weighted higher or lower than others (e.g. to emphasise the nominal channel length, temperature, etc...) 
```

<!-- page:18 -->
Again, following the current example, this call would be:

```txt
result = ExtractionUtils.DoStage("example", Model, Simulator, ParamSet1, Optimiser, data) 
```

This will perform the extraction using the provided model and data, returning the extracted parameters in the result object. As part of the DoStage function, the final extracted model is written to stagename.mod, in this case, example.mod.

# 2.1.7 Error Calculation

In any optimisation, the goal is to minimise the difference between the output of a function and some reference or target data. The quality of an optimisation or fit is determined by the error associated with the evaluation of the target function given the input set of parameters under optimisation. Internally the various optimisation routines provided by Mystic use several numerical methods of estimating fit errors which are appropriate to the optimisation algorithms. However, users frequently find it useful to calculate specific errors or to calculate single errors e.g. percentage errors in order to gain a qualitative feel for the fit of a model over some range of data. In order to facilitate this, Mystic provides several error calculation methods and a utility function called PrintErrors.

Optimiser-specific calculated errors for each particular extraction stage are printed by Mystic when an optimisation completes, however the error between the output of SPICE with the current set of parameter values and the reference data is only calculated across the range of data that is part of the optimisation. In order to calculate the error across the entire range of data, or across a different data set, the PrintErrors function is provided by the ExtractionUtils module.

An example showing the use of this function, using the root mean squared percentage error calculation method, is shown below.

```txt
## Load some data.
IdVg = mdb.Load(instances={"1":25e-9}, bias={"d":[0.05, 1.0]})
## A method to calculate the errors is needed.
ErrorMethod = "rmsd"
## Print the errors to screen.
ExtractionUtils.PrintErrors("example", IdVg, Simulator, Model, ErrorMethod) 
```

A list of the available error calculation methods can be found in Section 3.2.

# 2.1.8 Outputting Data

# PLT and CSV File Output

Mystic supports the output of data in the Synopsys PLT format which provides compatibilty with Sentaurus Visual. The SimData object has a method called WritePLTFile which allows the user to output

Mystic User Guide

O-2018.06

<!-- page:19 -->
PLT formatted data. This is particularly useful for fit validation when working within an Sentaurus Workbench based DTCO flow. This method can be used as follows (see the Mystic API Reference for more information).

```python
# Loads a single device data object.
idvg_data = mdb.Load(instances={"1":25e-9},
    bias={"drain":0.05, "substrate"=0.0})
# Loads multiple substrate bias conditions so Load returns a list.
idvd_data = mdb.Load(instances={"1":25e-9},
    bias={"gate":0.4})
## Perform an extraction
# Write out the single IdVg curve.
idvg_data.WritePLTFile("Example_IdVg")
# Write out the first of the IdVd curves.
idvd_data.WritePLTFile("Example_IdVd_Vb=0.0") 
```

The fitted SimData object can also be written to a .csv file using the SaveFitData method. The file will include the ivar, dvar, fit value and error columns of the object, as well as static columns for the other terminal biases stored in the object metadata.

# Parameter History

The OptParam values are tracked during the course of the optimisation and output to a CSV file at the end of each call to DoStage, with the naming convention stagename-pars.csv. By default, the parameter history accumulates throughout the entire strategy so the final csv file will be an entire history of all the parameters used across all of the stages. So, in this example:

```elixir
ExtractionUtils.DoStage("Stage1", Model, Simulator, ParamSet1, Optimiser, data)
ExtractionUtils.DoStage("Stage2", Model, Simulator, ParamSet2, Optimiser, data) 
```

Stage2-pars.csv will contain both the Stage1 and Stage2 parameter histories. The parameter history can be cleared between stages using the following:

```elixir
ExtractionUtils.DoStage("Stage1", Model, Simulator, ParamSet1, Optimiser, data)
Optimiser.ClearParameterHistory()
ExtractionUtils.DoStage("Stage2", Model, Simulator, ParamSet2, Optimiser, data) 
```

<!-- page:20 -->
Parameter history can also be output manually at any point in the extraction using the WriteParameterCSV method of the Optimiser object. A detailed description of this can be found in the Mystic API reference.

# 2.2 Statistical Extraction

Statistical extraction is very similar to the uniform extraction process, except that involves only a small subset of the parameters that were extracted during the uniform model extraction. Consequently, the statistical extraction is a much simpler process and typically involves only a single stage.

Processes such as data export from the Enigma database, data import into Mystic, parameter setup and data output all remain essentially identical to the uniform strategy. Differences between the uniform and statistical extraction strategies are briefly outlined in the following sections.Unlike the uniform extraction strategy, the statistical strategy generally consists of a small number of stages that may be combined into a single file. This allows multiple models to be easily extracted in a single instance of Mystic by simply iterating over the stages with a different model each time. It should be noted that it is essential that the model is reloaded and updated with the correct parameters at the start of each statistical extraction to ensure that the starting point for each extraction is the base uniform model and not the final model from the previous extraction.

# 2.3 Device CV Parameter Extraction

CV simulation data can be treated in the same way as current-voltage data in an extraction strategy. A simple example showing the fitting of the gate capacitance parameters for a BSIM-CMG model is shown below:

```txt
#Load the CGG data from the DB.
D=mdb.Load(instances{"1":34.0e-9},dvar='c(gate,gate)', ivar="vgate")

cfs=OptParam('cfs',1e-11,1e-12,1e-10,1e-11)
cgso=OptParam('cgso',5e-10,1e-12,5e-9,1e-10)
qmtcencv=OptParam('qmtcencv',0.8,0.02,1.5,1.0)
cgsl=OptParam('cgsl',5e-10,1e-12,1e-9,1e-10)
ckappas=OptParam('ckappas',2.0,0.05,10.0,1.0)
dlc=OptParam('dlc',3.5e-9,1e-9,4e-9,1.0e-9)
deltawcv=OptParam('deltawcv',3.5e-9,1e-9,4e-9,1.0e-9)

#Link CGDO and CGSO since we are assuming that the device is symmetric.
cgdo=LinkedOptParam('cgdo',cgso)

#Make a parameter list 
```

```txt
Stage1Parameters=[cfs,cgso,qmtcencv,cgsl,ckappas,dlc,cgdo]

#Do the extraction
res = ExtractionUtils.DoStage("CV",Model, Simulator, Stage1Parameters, Optimiser, [D])

#Output results graph
D.WritePLTFile('./Graphs/CGG-fit-NG') 
```

<!-- page:21 -->
This example illustrates a common situation when extracting gate capacitance models in that the source and drain capacitance parameters cgdo and cgso have been linked in order to provide a symmetric variation in capacitance. The use of the LinkedOptParam ensures that when the optimiser changes the value of these parameters to minimise the error in the fit of CGG that they contain the same value as should be expected when extracting CGG at very low drain bias.

# 2.3.1 Mystic DB CV Variables

The CV data set types shown in table 2.1 are exported by Garand during CV simulation and can be used in Mystic. See section 4.3.4 in the Garand manual for more information. See Appendix A and the Garand User Guide [12] for a full list of available database strings.

<table><tr><td>Variable Name</td><td>Description</td><td>Variable Name</td><td>Description</td></tr><tr><td colspan="2">Gate</td><td colspan="2">Source</td></tr><tr><td>c(gate,gate)</td><td>Gate to gate</td><td>c(source,gate)</td><td>Source to gate</td></tr><tr><td>c(gate,drain)</td><td>Gate to drain</td><td>c(source,drain)</td><td>Source to drain</td></tr><tr><td>c(gate,source)</td><td>Gate to source</td><td>c(source,source)</td><td>Source to source</td></tr><tr><td>c(gate,substrate)</td><td>Gate to body</td><td>c(source,substrate)</td><td>Source to body</td></tr><tr><td colspan="2">Drain</td><td colspan="2">Body</td></tr><tr><td>c(drain,gate)</td><td>Drain to Gate</td><td>c(substrate,gate)</td><td>Body to Gate</td></tr><tr><td>c(drain,drain)</td><td>Drain to Drain</td><td>c(substrate,drain)</td><td>Body to Drain</td></tr><tr><td>c(drain,source)</td><td>Drain to source</td><td>c(substrate,source)</td><td>Body to source</td></tr><tr><td>c(drain,substrate)</td><td>Drain to Body</td><td>c(substrate,substrate)</td><td>Body to Body</td></tr></table>

Table 2.1: Mystic DB Capacitance Voltage names.

# 2.4 Using Verilog Models

Mystic provides support for the use of SPICE Models written in Verilog. With the advent and rapid development of both BSIM-CMG and BSIM-IMG for FinFET and FDSOI devices, respectively, it has become advantageous to be able to utilise the Verilog versions of these models for early PDK development and Design-Technology Co-optimisation (DTCO) purposes.

<!-- page:22 -->
Verilog Models Supported By Mystic

Mystic supports any Verilog implementation that can be compiled and successfully simulated by HSPICE. In order for Mystic to extract parameters for a Verilog model, the parameters must be exposed at the top level of the model so that they can be manipulated from the netlist generated by Mystic. For example, consider the following Verilog-A code:

```verilog
module device (a, b, c);
    inout a, b, c;
    electrical a, b, c, d;

    parameter real p1 = 100.0;
    parameter real p2 = 1e-12;

    resistor #(.r(50.0), .m(1)) Rin(a, d);
    resistor #(.r(p1), .m(1)) Rout(d, b);
    capacitor #(.c(p2), .m(1)) Cout(d, c);

endmodule 
```

The resistance value of Rout is available to the user through parameter p1 and the capacitance value of Cout is available through parameter p2. However, the value of the input resistor, Rin is hardcoded to 50.0Ω inside the model, and cannot be extracted by Mystic.

When using generic Verilog models, you must ensure that the terminals supplied in the target data match those used by the model. For the above example, target data would need to contain a bias value for each of the a, b and c terminals along with a node list of how these terminal values should be ordered when the model instance is written to the netlist.

Verilog Model-Specific Commands

To facilitate the extraction of Verilog SPICE models, Mystic provides several Verilog-specific commands. A brief description of this functionality is given here. Full details of the Verilog model class are given in the Mystic Reference API.

A Verilog Model will be created and injected into the environment by Mystic if no level parameter is specified in the model card. Verilog models can also be created ‘on the fly’ as part of the Mystic extraction strategy for cases where the model card contains a level parameter, such as the Verilog-A implementation of the BSIM-IMG model shown below. In the example given in Examples, a model is created by constructing a VerilogModel instance of the Mystic BaseCompactModel class using

```txt
M=VerilogModel(Model)
M.AddVerilogLocation("/Models/BSIMIMG/106.2.0/code/bsimimg.va")
M.AddPVADir("/Models/BSIMIMG/106.2.0/code/bsimimg.pvadir") 
```

<!-- page:23 -->
The Model card containing the parameters has been loaded into the standard Mystic SPICE model handler. A valid full path to the verilog code to be compiled and executed for this model must be supplied so that Mystic can instruct the back end SPICE simulator to include it correctly. By default HSPICE will recompile the model for every simulation run. In Mystic, this can cause very slow extraction times as verilog compilation can often take several seconds. To compact this, AddPVADir can be used to point HSPICE towards a pre-compiled Verilog directory, that is re-used for all the HSPICE simulations that Mystic launches.

Having defined a Verilog model, this can now be used as a replacement in optimisations for the global Model defined by Mystic. For example,

```txt
DoStage(name, M, Simulator, pset1, Optimiser,[IdVghd_BelowVt]) 
```

# 2.4.1 Debugging Verilog Model Usage

Working out what has gone wrong with a Verilog model can be tricky due to the multiple steps that must execute in the back-end SPICE simulator in order to successfully compile and run a user-provided Verilog model. The following are some tips which will help users to identify and solve problems when using Verilog Models.

# Check Paths

Mystic runs simulations using a secure temporary directory which is created at runtime. In most cases the compiled versions of the Verilog model will be located in this temporary directory by SPICE. Because of this, providing relative paths to Verilog code will cause problems as Mystic does not execute SPICE in the users current working directory. Users should provide absolute paths to Verilog code or use SPICE flags such as the -hdlpath flag for HSPICEto specify a location where the source can be found. Please see the documentation for the appropriate SPICE simulator for more information.

# Test with SPICE

If Mystic encounters problems when attempting to run a Verilog model extraction, then is is often advisable to check to ensure that the SPICE parameters and setup are correct. This can be facilitated by using the debug commands provided by the Mystic Simulator object.

```txt
Simulator.EnableDebugMode()
Simulator.KeepTemporaryData() 
```

<!-- page:24 -->
Adding these commands to your extraction script will cause Mystic to override the default behaviour of using a secure temporary directory which is removed after execution and will cause it to create a folder called tmp/ in the current working directory. In this folder the SPICE files generated by Mystic will be retained. Users can use these to manually test to see if the supplied verilog code and SPICE command line arguments are producing valid output.

# 2.4.2 HSPICE Setup

In order to work efficiently with Verilog models there are a few setup steps in the extraction environment that greatly improve the performance of extraction when using Synopsys HSPICE. See the HSPICE [4] documentation for more information.

Verilog SPICE models differ from native implementations in that the Verilog code requires compilation before use within SPICE. Incorrect set up of the SPICE environment can lead to continual recompilation of the Verilog code and results.

The first time that a Verilog model is used in an HSPICE simulation, it will be compiled into a folder in the current working directory, this directory will have the extension .pvadir appended to its name.

Using the command line Verilog compiler you can pre-compile the SPICE model for use within HSPICE, otherwise HSPICE will compile it automatically for you on the first execution and the .pvadir can be copied to a known location for re-use. The command line Verilog compiler that ships with HSPICE is called pva. A BSIM-IMG SPICE model can be pre-compiled using the command

```txt
pva -hdlpath <path to folder>/IMG -o <path to output folder> bsimimg.va 
```

This will create an output PVA\_DIR in the requested output folder containing the compiled model code.

This pre-compiled model can be used with HSPICE via the setting of the environment variable PVA\_DIR, if the requested model is found in this directory then HSPICE will use this in preference to compiling its own version of the model. The path to the Verilog source code also needs to be set using the HSP\_HDL\_DIR environment variable.

```shell
#Bash
export PVA_DIR=<path to folder>/IMG.pvadir
export HSP_HDL_DIR=<path to folder>/IMG
#Csh
setenv PVA_DIR <path to folder>/IMG.pvadir
setenv HSP_HDL_DIR <path to folder>/IMG 
```

<!-- page:25 -->
This environment variable must be set in the terminal in which Mystic is run in order that the HSPICE sub-process picks it up.

Depending on the version of HSPICE used, the following additional Verilog options may need to be passed to either the Verilog compiler or to HSPICE in order to expose internal Verilog variables.

```javascript
M.AddVerilogCompilerFlags(".options VAOPTS=str('-G')") 
```

or

-G passed to the pva compiler command.

The correct paths for the PVA\_DIR and HSP\_HDL\_DIR should be set up by the user to point to the location where the BSIM-IMG Verilog model can be found.

Alternatively the location of the PVA\_DIR can be defined in the strategy directly, using the AddPVADir method of the VerilogModel class as shown in the example in Section Using Verilog Models.

<!-- page:26 -->
# 2.4.3 Examples

Simple Verilog Example   
```python
Simulator.SetAdditionalSpiceArguments(("hdlpath",\
    "/Models/BSIMIMG/106.2.0/code/",\
    "--hdl", "/Models/BSIMIMG/106.2.0/code/bsimimg.va"))
# Create a custom model.
# Uses the imported model card stored in Model
# to initialise Verilog SPICE model.
M=VerilogModel(Model)

#Simple parameter set.
pset1 = [ETA0]

# Run simulation stage with imported verilog model
# rather than imported default model.
DoStage(name, M, Simulator, pset1, Optimiser,[IdVghd_BelowVt]) 
```

CV Extraction Example   
```python
#Name for output
name = "IMG_cv"

# Create Error calculator
ErrorMethod = ErrorCalculator.MeanPercentageRMSError()

# Define the paths to the model
Simulator.SetAdditionalSpiceArguments(("hdlpath", \
    "/Models/BSIMIMG/106.2.0/code/", \
    "-hdl", "/Models/BSIMIMG/106.2.0/code/bsimimg.va"))

# Load the Gate capacitance data for the low drain condition.
CggVg = mdb.Load(1=20e-9,vdrain=[0.01],vsubstrate=0.0,dvar='c(gate,gate)', 
    ivar='Vgate')

# Create a custom verilog model. Need to specify the dimensions as well as the
    → verilog code to be used.
# In this case you don't need the full path to the file as we assume the
# Validate model is set to false to stop the Verilog Model looking for the
    → verilog file in the current directory.
M=VerilogModel(Model,) 
```

```txt
# Parameters to be extracted.
# CFS and CFD should be linked in the model but are not in IMG version 102.6.0.
CFS=OptParam('CFS',1e-12,0.0,100e-12,1e-12)
#CFD=OptParam('CFD',1e-12,0.0,100e-12,1e-12)
CFD=LinkedOptParam("CFD",CFS)
CGSL=OptParam('CGSL',1e-12,0.0,100e-12,1e-12)
CGDL=LinkedOptParam("CGDL",CGSL)
CKAPPAS=OptParam('CKAPPAS',0.6,0.02,1.0,0.1)
CKAPPAD=LinkedOptParam('CKAPPAD',CKAPPAS)
DLC=OptParam("DLC",0.0,-10e-9,10e-9,1e-9)
QMTCENCV=OptParam("QMTCENCV",0.01,0.0,10.0,1.0)
LOVS=OptParam("LOVS",0.0,0.0,10e-9,1e-9)
# Create a parameter set for the extraction.
pset1 = ParameterSet([CFS,CFD,CGSL,CGDL,CKAPPAS,CKAPPAD,DLC,QMTCENCV,LOVS])
# Choose a fast jacobian.
Optimiser.SetOptimisationParameter('fast_jacobian',True)
# Extract the gate capacitance.
ExtractionUtils.DoStage(name, M, Simulator, pset1, Optimiser,[CggVg])
# Calculate a final error.

ExtractionUtils.PrintErrors(name,CggVg,Simulator,M,ErrorMethod)
CggVg.WritePLTFile('{0}-20nm'.format(name)) 
```

<!-- page:27 -->
# 2.5 Sub-Circuit Models

Mystic supports the extraction of full sub-circuit netlists. There are a few rules with regards to the contents and structure of the sub-circuit that must be adhered to, in order for Mystic to parse it correctly.All components must be included within the bounds of a sub-circuit, including modelcards.

1. Recursive sub-circuits are not currently supported.

# 2.5.1 Sub-Circuit Model-Specific Commands

The API of the sub-circuit Model object in Mystic is designed to mirror that of a regular Model, so that the transition from using a single SPICE Model to a sub-circuit is as simple as posible. Accessing model parameters within the sub-circuit uses a dot separated syntax like so

```lua
Model.SetModelParameter("nmos.tfin", 25e-9) 
```

Passive component values or .PARAM values can be accessed using the component or parameter name directly

```txt
Model.SetModelParameter("rdrain", 100.0) 
```

<!-- page:28 -->
SPICE Model objects within the sub-circuit can be accessed using the GetModel method and the name of the model as defined in the netlist. This can be useful for setting or adding instance parameters to individual models and for defining Verilog Models within sub-circuits.

```python
# Get the nmos model object from inside a sub-circuit
M = Model.GetModel("nmos")

# Set the nmos drain resistance
M.SetInstanceParam("rdc", 100.0) 
```

A full description of the sub-circuit module can be found in the Mystic API reference.

# 2.5.2 Sub-Circuit Extraction with Verilog Models

Verilog models within sub-circuits can be defined in two different ways. The first way is to supply the absolute path to the verilog code in the input netlist directly

```html
.hdl /<full>/<path>/<to>/bsimimg.va 
```

The Mystic netlist parser will treat this as a string and leave it untouched in the backend netlist. The second way is to dynamically create the VerilogModel from inside extraction strategy and add the Verilog file path at that point.

```txt
# Convert the internal nmos1 Model to Verilog
Model.ConvertModelToVerilog("nmos1")

# Add the Verilog location and PVA_DIR location
Model.GetModel("nmos1").AddVerilogLocation("/<full>/<path>/<to>/bsimimg.va")
Model.GetModel("nmos1").AddPVADir("/<full>/<path>/<to>/<compiled>/bsimimg.
    → pvadir") 
```

# 2.5.3 Instance Parameters in Sub-Circuits

Instance parameters associated with sub-circuits can set in the same way as with a regular SPICE Model, using the SetInstanceParams method. The setup of the sub-circuit will determine how these are propagated down to internal models.

```txt
Model.SetInstanceParams({"l":25e-9,"w":1e-6}) 
```

<!-- page:29 -->
Alternatively instance parameters can be applied to internal models directly using the GetModel method to access the model.

```txt
Model.GetModel("nmos1").SetInstanceParams({"l":25e-9,"w":1e-6}) 
```

Note that if a previous relationship existed between the top level instance parameters and the local model instance parameter this would be superseded by the above useage. It is also important to note that during extraction of a SimData object, any instance parameters associated with the SimData object will be applied to the sub-circuit model and not to any SPICE Models within. As usual these will take precident over model instance parameters.

# 2.5.4 Example

The initial netlist for a simple parasitic extraction is shown below.

```txt
.subckt xsub drain gate source substrate l=2.5e-9
rd drain d 100
rs source s 100
.PARAM phig=4.2
M1 d gate s substrate nmos1 l=1
.model nmos1 nmos
+ level=77
+ version=108.0
+ bulkmod=1
+ phig1='phig'
+ u0=0.15
...
+ pvag=1
+ pclm=1e-10
.ends 
```

When loaded into Mystic, the sub-circuit can be extracted as follows. Note that this example makes use most of the major features of the SubCktModel.

```python
# Set the Sub-Circuit model instance params
Model.SetInstanceParams({"1":28e-9})

# Define some extraction parameters
RD = OptParam("RD", 100, 0, 1000, 100) 
```

```julia
RS = LinkedOptParam("RS", RD)
PHIG = OptParam("PHIG", 4.2, 4.1, 4.3, 1.0)
U0 = OptParam("nmos.U0", 0.15, 0.06, 0.3, 0.1)

params = ParameterSet([RD, RS, PHIG, U0])

# Perform the extraction stage
DoStage("Stage1", Model, Simulator, params, Optimiser, [IdVg])

# Get the final error
idvg_err = ExtractionUtils.PrintErrors("example", IdVg, Model, Simulator, ErrorMethod)

# Output PLT File
IdVg.WritePLTFile("Stage1") 
```

<!-- page:31 -->
# 3 Mystic Command Reference

For user convenience, several modules and objects are pre-loaded into the Mystic execution environment. All of the automatically created objects and modules are listed and described in this chapter. This section provides a description of some of the modules/objects provided to the user in the extraction environment. Please see the Mystic API Reference for the full Mystic API.

All exceptions raised within Mystic can be treated as standard Python exceptions via the usual try/except method.

# 3.1 Global Objects

The Mystic environment predefines a set of globally accessible variables containing objects and modules which are necessary for performing SPICE model extraction (See Table 3.1).

Table 3.1: Mystic Global Variables. 

<table><tr><td>Name</td><td>Type</td><td>Description</td></tr><tr><td colspan="3">Optimisation</td></tr><tr><td>Global Objects</td><td>Object</td><td>A Python object containing the optimiser that the user has selected via the command line arguments to Mystic.</td></tr><tr><td>OptParam</td><td>Object</td><td>Python object for creating and manipulating Optimisation Parameters.</td></tr><tr><td>ParameterSet</td><td>Object</td><td>Python object used to collect optimisation parameters together.</td></tr><tr><td>LinkedOptParam</td><td>Object</td><td>Python Object used to tie together the values in OptParam objects.</td></tr><tr><td colspan="3">Utilities</td></tr><tr><td>ExtractionUtils</td><td>Module</td><td>Module containing utility functions for extraction.</td></tr><tr><td>LoadModel</td><td>Function</td><td>Utility function which allows the user to load a new SPICE model into the global model object.</td></tr><tr><td>MakeModel</td><td>Function</td><td>Utility function which makes a new model from a modelcard string</td></tr><tr><td>UpdateModel</td><td>Function</td><td>Utility function which update the model with new values</td></tr><tr><td colspan="3">SPICE model</td></tr><tr><td>Model</td><td>Object</td><td>Python object containing the currently loaded SPICE model.</td></tr><tr><td colspan="3">Data</td></tr><tr><td>mdb</td><td>Object</td><td>The Mystic database object loaded at run time.</td></tr><tr><td>SimData</td><td>Class</td><td>The main data storage class used in the Mystic extraction environment</td></tr></table>

<!-- page:32 -->
# Optimiser

The optimiser is the engine room of Mystic. By default Mystic injects the optimisation method that the user has selected at run time into the Mystic environment as the Optimiser object.

There are several optimisation routines available in Mystic through different backends (See Table 1.3). These include:

■ Bounded Trust Region (Intel MKL and scipy implementations)[13]   
■ Unbounded Trust Region(Intel MKL and scipy implementations)[13]   
■ Leavenberg-Marquardt (scipy implementation)[14]   
■ Constrained Optimisation By Linear Approximation[15][16] (COBYLA, scipy implementation)

Refer to the appropriate optimisation routine section and Optimiser API docs for more information.

In this document the terms Optimisation and Fitting are used interchangeably to indicate the matching of the output of a SPICE simulation utilising a SPICE model with modelcard parameters which will be adjusted to give the best overall fit to some target device data provided by the user.

There are two general classes of optimisation routine provided by Mystic; bounded and unbounded routines. Bounded, or constrained, optimisation routines impose limits on the values of the input function parameters which restrict the range of solutions that the optimiser can consider during SPICE model fitting. For example, when an OptParam object is created the user must provide an initial value, a minimum and a maximum value and a scaling factor. In a bounded model fit the minimum and maximum values will be used to clamp the possible OptParam values that the fitting algorithm can use in order to find the optimal fit with the target data. In an unbounded fit, these min and max values are used to set up limits where a warning is printed to inform the user that the parameter may be drifting out of the desired range. As a result it is important to note that any bounded optimisation routine is not guaranteed to be globally convergent, for the simple reason that the true global minimum may lie outside of the range of acceptable parameter values. It is therefore often a good idea to begin the development of a SPICE model extraction strategy with an unbounded optimiser and then proceed to a bounded optimisation only if necessary.

<!-- page:33 -->
All of the optimisation routines within Mystic attempt to minimise the objective function F (x) which is a measure of the error between our reference data y and the values obtained from the evaluation of a SPICE simulation using the conditions of the reference data and our current set of SPICE model parameters f(x). In general these algorithms will attempt to minimise the RMS deviation or sum of squares of the residuals of the function as defined by equation (3.1).

$$
\min (\parallel F (x) \parallel_ {2} ^ {2}) = \min (\parallel y - f (x) \parallel_ {2} ^ {2}) \tag {3.1}
$$

It is important to note that any optimiser will find the solution that minimises the magnitude of the objective function F (x) and for that reason it is important to target the range of data where an OptParam is being extracted in order to obtain the best results. Mystic provides the DataFilter functionality for this very purpose.

# 3.1.1 Optimisation Routines

Mystic provides several optimisation algorithms available through different backends, some of which are described in this section of the manual. We will begin with a general overview of the trust region methods since they are used by default and then a reference section is provided which describes the attributes of the various implementations.

# Trust Region Algorithms

Trust region algorithms are highly reliable optimisation routines which utilises localised modelling of the objective function within some ’trust region’ in order to approximate the unknown function. This local model is then used to calculate the direction to take towards the function minimum or optimal value. At this point the local model is compared to the objective function and the trust region and local model are updated. Mystic provides both a bounded and an unbounded version of the trust region algorithm and COBYLA can be viewed as a member of this class of optimisers due to the variable range of its linear approximation function, see [15] for more information.

Trust region optimisers are very robust but may be slow compared to other simpler algorithms such as Levenberg-Marquardt when a large number of target model parameters are required.

Because of the nature of the trust region optimiser algorithm, the solution with the minimum error is NOT always the last iteration, it can in fact be considerably further back in the process of optimisation. Users should take care to make sure that the caches within SimData objects which have been used in conjunction with the trust region optimisers are updated to use the minimum error solution by calling PrintErrors or an equivalent function which forces the update of the internal data cache from a fresh SPICE simulation.

<!-- page:34 -->
# Intel MKL Trust Region

For unbounded implementation of the Trust Region algorithm, see [13] for a detailed discussion on these methods. By default the Trust Region optimiser uses a centred difference to estimate the Jacobian of the target function, the jac control parameter can be used to change this to a forward difference which greatly reduces the number of objective function evaluations required at the expense of a slight reduction in numerical stability.

<table><tr><td>Backend Name</td><td>Type</td></tr><tr><td>TRUST_REGION</td><td>Unbounded Optimiser</td></tr></table>

# Control Parameters

The Trust Region optimiser will accept the following control attributes.

Table 3.2: Trust Region Control Attributes. 

<table><tr><td>Name</td><td>Type</td><td>Min</td><td>Max</td><td>Default</td><td>Description</td></tr><tr><td>max_nfev</td><td>int</td><td>1</td><td>N/A</td><td>N/A</td><td>Maximum number of calls to the objective function excluding Jacobian calculation.</td></tr><tr><td>eps</td><td>float</td><td> $1 \times 10^{-16}$ </td><td>1.0</td><td> $1 \times 10^{-3}$ </td><td>Step size for Jacobian calculation</td></tr><tr><td>delta</td><td>float</td><td>0.1</td><td>100</td><td>1.0</td><td>Trust region radius</td></tr><tr><td colspan="6">Stop Criteria</td></tr><tr><td>eps1/trtol</td><td>float</td><td>1e-18</td><td>100</td><td> $1 \times 10^{-5}$ </td><td>Minimum trust region area</td></tr><tr><td>eps2/ftol</td><td>float</td><td>1e-18</td><td>100</td><td> $1 \times 10^{-5}$ </td><td>Minimum magnitude of the objective function to be minimised</td></tr><tr><td>eps3/gtol</td><td>float</td><td>1e-18</td><td>100</td><td> $1 \times 10^{-5}$ </td><td>The Jacobian matrix has become singular if its magnitude becomes less than eps3</td></tr><tr><td>eps4/xtol</td><td>float</td><td>1e-18</td><td>100</td><td> $1 \times 10^{-5}$ </td><td>Minimum acceptable value for the size of the trial step.</td></tr><tr><td>eps5/ftol</td><td>float</td><td>1e-18</td><td>100</td><td> $1 \times 10^{-5}$ </td><td>The minimum relative change between successive estimates for the objective function.</td></tr><tr><td>eps6/atol</td><td>float</td><td>1e-18</td><td>100</td><td> $1 \times 10^{-5}$ </td><td>Trial step precision. Used to move the trust region.</td></tr><tr><td colspan="6">Additional Parameters</td></tr><tr><td>jacstep_type</td><td>boolstr</td><td>N/A’abs’</td><td>N/A’rel’</td><td>False’abs’</td><td>Use Mystic's simple Jacobian estimation rather than the Optimisers native one.Use an absolute or relative step when performing the Jacobian estimation. Only applicable if fast_jacobian is True.</td></tr><tr><td>step_method</td><td>str</td><td>’cd’</td><td>’fd’</td><td>’fd’</td><td>Use a forward difference or centered difference method for the Jacobian estimation. Only applicable if fast_jacobian is True.</td></tr></table>

<!-- page:36 -->
# Intel MKL Bounded Trust Region

For bounded implementation of the Trust Region algorithm, see [13] for a detailed discussion on these methods. By default the Trust Region optimiser uses a centred difference to estimate the Jacobian of the target function, the jac control parameter can be used to change this to a forward difference which greatly reduces the number of objective function evaluations required at the expense of a slight reduction in numerical stability.

This is the default optimisation method in Mystic.

<table><tr><td>Backend Name</td><td>Type</td></tr><tr><td>BOUNDED_TRUST_REGION</td><td>Bounded Optimiser</td></tr></table>

# Control Parameters

The Bounded Trust Region optimiser will accept the same control attributes as the unbounded Trust Region described in Table 3.2.

<!-- page:37 -->
# Scipy Trust Region

This is the Mystic implementation of the well-known Levenburg-Marquart algorithm[14]. It is an unbounded optimisation routine. The LEVMAR routine uses a forward difference function to approximate the Jacobian of the objective function, as such it may require fewer calls to SPICE than routines using a centred difference (such as the default in Intel MKL Trust Region). In addition to Intel MKL’s implementation, Mystic can use scipy’s implementation of the Trust Region algorithm. This is the default option when selecting the scipy\_least\_squares interface in the Optimiser object.

<table><tr><td>Backend Name</td><td>Type</td></tr><tr><td>scipy_least_squares</td><td>Bounded Optimiser</td></tr></table>

# Control Parameters

As part of the scipy least squares interface, the Trust Region optimiser will accept the following control attributes.

Table 3.3: Scipy’s Trust Region Control Attributes. 

<table><tr><td>Name</td><td>Type</td><td>Min</td><td>Max</td><td>Default</td><td>Description</td></tr><tr><td>max_nfev</td><td>int</td><td>1</td><td>N/A</td><td>N/A</td><td>Maximum number of calls to the objective function excluding Jacobian calculation.</td></tr><tr><td>eps</td><td>float</td><td> $1 \times 10^{-16}$ </td><td>1.0</td><td> $1 \times 10^{-3}$ </td><td>Step size for jacobian calculation</td></tr><tr><td colspan="6">Stop Criteria</td></tr><tr><td>ftol</td><td>float</td><td>1e-18</td><td>100</td><td> $1 \times 10^{-5}$ </td><td>Minimum magnitude of the change of the objective function to be minimised.</td></tr><tr><td>xtol</td><td>float</td><td>1e-18</td><td>100</td><td> $1 \times 10^{-5}$ </td><td>Minimum magnitude of the change of the parameters being optimised.</td></tr><tr><td>gtol</td><td>float</td><td>1e-18</td><td>100</td><td> $1 \times 10^{-5}$ </td><td>Minimum magnitude of the norm of the gradient of the objective function to be minimised.</td></tr><tr><td colspan="6">Additional Parameters</td></tr><tr><td>verbose</td><td>int</td><td>0</td><td>2</td><td>0</td><td>Enable additional verbosity in the output.</td></tr><tr><td>loss</td><td>str</td><td>N/A</td><td>N/A</td><td>’linear’</td><td>Loss function to be used. Can be ’linear’ (default, standard least square), ’soft_11’, ’huber’, ’cauchy’ or ’arctan’.</td></tr></table>

<!-- page:38 -->
# Levenberg-Marquardt

Mystic can use scipy’s implementation of the well-known Levenberg-Marquart algorithm[14]. It is an unbounded optimisation routine.

<table><tr><td>Backend Name</td><td>Option Required</td><td>Type</td></tr><tr><td>scipy_least_squares</td><td>method=&#x27;lm&#x27;</td><td>Unbounded Optimiser</td></tr></table>

To use it, after having selected the scipy\_least\_squares backend, the following option must be used:

```python
Optimiser.set_optimisation_parameters(method='lm') 
```

# Control Parameters

As part of the scipy least squares interface, the Levenberg-Marquardt optimiser will accept the following control attributes.

Table 3.4: Levenberg-Marquardt Control Attributes. 

<table><tr><td>Name</td><td>Type</td><td>Min</td><td>Max</td><td>Default</td><td>Description</td></tr><tr><td>max_nfev</td><td>int</td><td>1</td><td>N/A</td><td>N/A</td><td>Maximum number of calls to the objective function excluding Jacobian calculation.</td></tr><tr><td>eps</td><td>float</td><td> $1 \times 10^{-16}$ </td><td>1.0</td><td> $1 \times 10^{-3}$ </td><td>Step size for jacobian calculation</td></tr><tr><td colspan="6">Stop Criteria</td></tr><tr><td>ftol</td><td>float</td><td>1e-18</td><td>100</td><td> $1 \times 10^{-5}$ </td><td>Minimum magnitude of the change of the objective function to be minimised.</td></tr><tr><td>xtol</td><td>float</td><td>1e-18</td><td>100</td><td> $1 \times 10^{-5}$ </td><td>Minimum magnitude of the change of the parameters being optimised.</td></tr><tr><td>gtol</td><td>float</td><td>1e-18</td><td>100</td><td> $1 \times 10^{-5}$ </td><td>Minimum magnitude of the norm of the gradient of the objective function to be minimised.</td></tr><tr><td colspan="6">Additional Parameters</td></tr><tr><td>verbose</td><td>int</td><td>0</td><td>2</td><td>0</td><td>Enable additional verbosity in the output.</td></tr><tr><td>loss</td><td>str</td><td>N/A</td><td>N/A</td><td>’linear’</td><td>Loss function to be used. Can be ’linear’ (default, standard least square), ’soft_11’, ’huber’, ’cauchy’ or ’arctan’.</td></tr></table>

<!-- page:39 -->
# COBYLA

This optimiser provides, through the scipy\_minimize interface, an implementation of constrained optimisation by linear approximation algorithm[16, 15, 17] which is based on the linear approximation of the objective function within the specified constraints. COBYLA is a derivative free algorithm in that it does not require the calculation of the Jacobian in order to estimate the objective function to be optimised. This means that although COBYLA is generally relatively slow to converge compared to Intel MKL Trust Region or Levenberg-Marquardt, if the model extraction requires a large number of SPICE model parameters to be extracted simultaneously, which results in a very large Jacobian matrix requiring many SPICE evaluations, COBYLA may be a preferable optimisation method.

<table><tr><td>Backend Name</td><td>Option Required</td><td>Type</td></tr><tr><td>scipy_minimize</td><td>method=&#x27;COBYLA&#x27;</td><td>Bounded Optimiser</td></tr></table>

To use it, after having selected the scipy\_minimize backend, the following option must be used:

```python
Optimiser.set_optimisation_parameters(method='COBYLA') 
```

# Control Parameters

The COBYLA optimiser will accept the following control attributes. Since it conforms to the scipy\_minimize interface, the “Additional Parameters” must be passed as a dictionary using the options keyword. For example, to set the stopping tolerance to 1e-5, rhobeg to 0.1 and maxiter to 100, the following line should be used:

```python
Optimiser.set_optimisation_parameters(tol=1e-5, options={'rhobeg': 0.1, '→ maxiter': 100}) 
```

Table 3.5: COBYLA Control Attributes 

<table><tr><td>Name</td><td>Type</td><td>Min</td><td>Max</td><td>Default</td><td>Description</td></tr><tr><td colspan="6">Stop Criteria</td></tr><tr><td>tol</td><td>float</td><td> $1 \times 10^{-16}$ </td><td>1000</td><td> $1 \times 10^{-14}$ </td><td>Target final step length (not guaranteed)</td></tr><tr><td colspan="6">Additional Parameters</td></tr><tr><td>disp</td><td>bool</td><td>N/A</td><td>N/A</td><td>False</td><td>Enable additional debug output.</td></tr><tr><td>maxiter</td><td>int</td><td>1</td><td>N/A</td><td>1000</td><td>Maximum number of function evaluations</td></tr><tr><td>rhobeg</td><td>float</td><td> $1 \times 10^{-16}$ </td><td>1000</td><td>1.0</td><td>Initial step size for the parameters</td></tr></table>

<!-- page:40 -->
# 3.2 Error Calculation Methods

The ErrorCalculator model has been deprecated in favour of in-place error calculation on the target data objects. However, the same single error calculation method can still be supplied to some of the convenience functions in the ExtractionUtils module as before. Error calculations in Mystic are performed on a point wise basis, meaning that the same calculation is performed at each defined value of the input data set and then a total or average of these values is provided. The interpretation of the result of an error calculation will depend on the specifics of the current problem under investigation. It is often difficult to reduce the result of an optimisation to a single ’goodness of fit’ number which perfectly describes the quality of the generated solution. As a result, Mystic provides several different methods of calculating a single error to describe the error in a give solution.

The following strings can be passed to the functions to use as the error calculation method:

<table><tr><td>Method</td><td>Description</td></tr><tr><td>”mean”</td><td>The average point wise percentage error.</td></tr><tr><td>“rmsd”</td><td>The average point wise root mean squared error expressed as a percentage.</td></tr><tr><td>“nrmsd”</td><td>Normalized RMS deviation.</td></tr></table>

We use the following notation to describe the error calculation methods in the remainder of this section:

■ $N _ { d }$ is the number of data sets used in the current optimisation or target data for the error calculation.   
■ $N _ { p } ( d )$ is the number of data points in the dataset d.   
■ $N _ { t o t a l }$ is the total number of data points in the target data $\begin{array} { r } { N _ { t o t a l } = \sum _ { d = 1 } ^ { N _ { d } } N _ { p } ( d ) } \end{array}$   
■ $Y _ { d , x }$ is the value obtained when evaluating the extracted SPICE model at point x in dataset d.   
■ $R _ { d , x }$ is the reference value in the target data at point x in dataset d.

# 3.2.1 Mean

Calculates the average point wise relative error as defined by equation 3.2 expressed as a percentage.

$$
E r r o r = 1 0 0 \times \frac {\sum a b s (\frac {Y _ {d , x} - R _ {d , x}}{R _ {d , x}})}{N _ {t o t a l}} \tag {3.2}
$$

<!-- page:41 -->
# 3.2.2 RMSD

Calculates the average point wise relative RMS error expressed as a percentage using the expression given in equation 3.3.

$$
E r r o r = 1 0 0 \times \sqrt {\frac {\sum (\frac {Y _ {d , x} - R _ {d , x}}{Y _ {d , x}}) ^ {2}}{N _ {t o t a l}}} \tag {3.3}
$$

# 3.2.3 NRMSD

Calculates the Normalised Root Mean Square Deviation. This is the Root Mean Square error normalised by the range of the input data, as given by equation 3.4.

$$
E r r o r = \frac {\sqrt {\frac {\sum (Y _ {d , x} , - R _ {d , x}) ^ {2}}{N _ {t o t a l}}}}{Y _ {m a x} - Y _ {m i n}} \tag {3.4}
$$

<!-- page:42 -->
# 4 Mystic Database

The overall structure and functionality of the Enigma database is described in the Enigma User Guide[18]. This section introduces the functionality and concepts as they relate to Mystic.

Mystic uses the Mystic Database API (see the Mystic API Reference for more information) to communicate with the Enigma database in three distinct ways: to obtain target data stored from TCAD, to store Mystic fitting information and to retrieve Mystic fitting information. Each of these interaction models is described in the following sections.

# 4.1 Loading TCAD Data

TCAD simulation data can be loaded using the Load method of the mdb object.

```txt
data = mdb.Load (validate=False, **kwargs) 
```

Example Kwargs:

<table><tr><td>instances</td><td>Instance parameters attached to the metadata of the target data during upload, e.g gate length (l), device width (w). This should be supplied as a Python dictionary.</td></tr><tr><td>bias</td><td>Terminal biases attached to the target data. This should be supplied as a Python dictionary.</td></tr><tr><td>t</td><td>Simulation Temperature (K)</td></tr><tr><td>n</td><td>Device Index</td></tr><tr><td>dvar</td><td>Simulation Dependent Variable Name</td></tr><tr><td>ivar</td><td>Simulation Independent Variable Name</td></tr><tr><td>project</td><td>The name or project_id of the Enigma DB project to load from.</td></tr></table>

The following section gives some examples of how the Load method can be used within a Mystic extraction strategy. See the Mystic Reference API for more information.

None of the above constraints are required, and if none are specified, then all data in the database will be loaded. For each variable, a value or list of values can be specified and the data will be filtered accordingly. The above keys are just suggestions that are compatible with Garand data. If the data has been uploaded from other TCAD simulators, any key pushed in during upload can be used to access and filter the data.

<!-- page:43 -->
Note that in cases where multiple terminal configurations are matched a list of Mystic SimData objects will be returned. Your extraction script should check the return type in cases where this may occur.

# 4.1.1 Examples

Single IDVG curve   
```txt
data = mdb.Load(instances={"l":25e-9, "w":25e-9}, bias={"drain":0.05, "substrate":0.0}, n=1) 
```

This will load the low drain, zero substrate IDVG curve for device #1 in the database with geometry 25×25nm. If no device matching the given constraints is found then an exception will be raised by the Enigma DB interface.. If there is only a single device in the ensemble matching the constraints (which will almost always be the case during uniform model extraction), then the n=1 constraint is unnecessary.

Multiple gate lengths   
```javascript
data = mdb.Load(instances={"1":[25e-9, 32e-9]},
bias={"drain":0.05, "substrate":0.0}) 
```

This will load the low drain, zero substrate IDVG curves for devices with LG=25nm and 32nm.

Zero substrate data   
```javascript
data = mdb.Load(instances={"l":[25e-9, 32e-9]}, bias={"substrate":0.0}) 
```

This will load the zero substrate bias curves for LG=25nm and 32nm, for all drain biases that are available in the database.

IDVD curves   
```javascript
data = mdb.Load(instances={"l":25e-9}, bias={"gate":[0.4, 0.6, 0.8, 1.0], ivar="vdrain"}) 
```

This will load I V data for V =0.4, 0.6, 0.8 and 1.0V and L =25nm.

All data, single gate length   
```lua
data = mdb.Load(instances={"1":25e-9}) 
```

This will load all data, IDVG and IDVD, for LG=25nm.

All data, single gate length only IdVg curves

```python
data = mdb.Load(instances={"l":25e-9},dvar='idrain', ivar='vgate') 
```

<!-- page:44 -->
This will load all $I _ { D } V _ { G }$ data for $L _ { G } { = } 2 5 \mathrm { n m }$ .

All data, single gate length only IdVd curves from a single Garand project in the database.

```javascript
data = mdb.Load(instances={"l":25e-9},dvar='idrain', ivar='vdrain', project="34") 
```

This will load all $I _ { D } V _ { D }$ data from project 34 where $L _ { G } { = } 2 5 \mathrm { n m }$ .

# Loading multiple temperatures

```txt
data = mdb.Load(instances={"l":25e-9},dvar='idrain', ivar='vdrain', t=[300.0,250.0]) 
```

This will load all $I _ { D } V _ { D }$ data from the database where LG=25nm and the simulation temperature was either 300 or 250 K.

# 4.2 Storing Mystic Fit Information

In this release, the interaction model with the Enigma database has changed significantly from previous releases. The project and dataset framework is controlled entirely by Enigma and Mystic will push to pre-created datasets that are passed to Mystic on the command line as described in Section 1.4. For full details on this interaction model consult the Enigma User Guide.

This means that the methods for project and dataset manipulation are deprecated, but are preserved for backward compatibility.

# 4.2.1 Creating a Mystic Project

Mystic data is stored in projects within the database. These serve as a method of grouping data together in manageable locations. Project names must be unique within a database in order to allow users to search them and supplying a duplicate name will result in a MysticDBError being raised. If desired, this can be over-written using the clean flag.

```go
project = mdb.CreateMysticProject(name) 
```

Create project returns a Project document as described in the Mystic API Reference.

<!-- page:45 -->
# 4.2.2 Deleting a Mystic Project

In general circumstances it is preferable to manage the Enigma database via Enigma directly. However, Mystic does provide functionality to remove projects from the database if required. In order to do this the function DeleteMysticProject is provided.

```txt
mdb.DeleteMysticProject(project, delete_all=False) 
```

Where project is one of either: a project name, a project id or a project object. If the delete\_all argument is set to true then all of the data associated with this project is also deleted from the database. In general it is a good idea to delete data associated with projects as otherwise it is very hard to reference, however for archival purposes this may not be acceptable.

# 4.2.3 Creating a Mystic Dataset

Datasets (see the DB.MysticDataSet of the Mystic API Reference Manual (Section 1.1)) are the basic unit of data storage for Mystic. The Mystic DB API provides the CreateMysticDataset function to allow users to create datasets based on SimData objects, which are used in the users extraction script. This function is described in detail in the Mystic API Reference.

```python
MysticDataSet = mdb.CreateMysticDataset(name, project, SimData, base_model=None →, description=None, delete_duplicates=False) 
```

When creating a dataset the user must supply a name by which this dataset can be referred (this name should be unique within the project that the dataset is added to), a project to which is is to be added and a SimData which contains the electrical data that is to be stored in the database. For example:

```vba
prj = mdb.CreateMysticProject("Stage1")
ds = mdb.CreateMysticDataset("Stage1-LowDrain", prj, IdVG_LD) 
```

Optionally, users can also supply a base\_model which is an instance of a CompactModel, in this case the parameters of the model are stored alongside the device and data so that any SPICE generated data can be re-produced at a later date. The user can also supply a description of the dataset which will be stored in the database.

```javascript
ds = mdb.CreateMysticDataset("Stage1-LowDrain", prj, IdVG_LD, base_model=Model, description="25nm Low drain data from bob") 
```

If the delete\_duplicates flag is set to true, any existing dataset with the same name and the data associated with it will be deleted and then re-created.

<!-- page:46 -->
# 4.2.4 Storing Mystic Fit Information

Having performed a Mystic extraction for a SPICE model, it needs to be stored in the Enigma database for future use. To facilitate this, the Mystic DB API provides a single, high-level utility function called StoreFitData that takes care of all of the necessary interactions with the database (see the Mystic API Reference for more information).

```txt
mdb.StoreFitData(self, SimData, ParameterSet/Model, ensemble_id=0, description=None, error=None) 
```

StoreFitData requires a SimData object which contains the data to be stored, as well as a list of OptParams or a Model object that contains the extracted model parameters which are associated with this data. When fit data is pushed to the Enigma database, both the reference and the fitted data from the SimData object are stored. It is therefore often a good idea to make sure that the fitted data is up to date via a call to a function which triggers a SPICE evaluation such as PrintErrors. Optional parameters which provide a description of the fitted data and a single user calculated error associated with the fit can also be provided.

The ensemble\_id argument is provided for the purposes of Statistical Extraction where the same Dataset is going to be used to store multiple extractions for different devices in an ensemble. For example:

```python
ErrorMethod = "rmsd"
...
for n in range(1,10):  # Loop over statistical data
    ...
    #Calculate an error for this condition
    fit_error=ExtractionUtils.PrintErrors(name, IdVg25nm_LD, Simulator, Model, ErrorMethod)
    # Store the fit data.
    mdb.StoreFitData(IdVg25nm_LD, Stage1Parameters+Stage2Parameters, description="Final Low drain fitting data.", error=fit_error, ensemble_id=n) 
```

This example illustrates the ability to concatenate ParameterSet objects. This is useful in situations where multiple sub-stages are present in an extraction strategy but must be recombined in order to re-produce a final result.

# 4.3 Retrieving Mystic Fit Information

# 4.3.1 GetFitData

The GetFitData function retrieves previously stored fitting data from the Enigma database.

Mystic User Guide

O-2018.06

```txt
SimData = GetFitData(self, dataset, ensemble=None, project=None) 
```

<!-- page:47 -->
GetFitData returns a SimData object containing the reference data for the fitOptional arguments are the same as mdb.Load and allow you to filter the query of fitting data.

GetFitData can be used as part of a multi-stage extraction strategy to restore the state of the internal data to some previously stored condition.

# 4.3.2 GetModelCard

The GetModelCard utility function returns a string containing a previously stored base model card from a dataset. If no model card is available in the dataset, then None is returned.

Where dataset is the name, id or Dataset object which contains the modelcard of interest. Optional arguments allow the user to filter the data by project\_id and/or ensemble\_id. For example:

```txt
modeldata=mdb.GetModelCard(IdVg25nm_LD, project=project)
MakeModel(modeldata) 
```

The modeldata string returned here can be used to construct the global Model object using the MakeModel helper function.

# 4.3.3 GetInitialModel

The GetInitialModel method goes one step further than GetModelCard, constructing a Model object from the card as it’s pulled from the Database.

```python
Model = mdb.GetInitialModel(dataset, project=None, ensemble_id=0) 
```

Where dataset is the name, id or Dataset object which contains the modelcard of interest. Optional arguments allow the user to filter the data by project and/or ensemble\_id.

# 4.3.4 GetFitParameters

The GetfitParameters method returns a dictionary of the fitted model parameters attached to a dataset. This can be used to update the current Model object in the environment. For example/

```txt
Model = mdb.GetInitialModel(dataset, project=None, ensemble_id=0)
params = mdb.GetFitParameters(dataset, ensemble_id=0)
UpdateModel(params) 
```

<!-- page:48 -->
# 4.3.5 GetFitModel

GetFitModel is a three step process that, pulls the initial model card from the Database, constructs a Model object, then adds the fitted parameter values stored in the dataset of interest. It takes the same arguements as GetModelCard and GetModel.

```python
Model = mdb.GetFitModel(dataset, project=None, ensemble_id=0) 
```

# 4.4 Multi-Stage Extraction Example

These examples have been taken from a multi-stage 28nm bulk MOSFET extraction strategy. The first two stages of this extraction strategy are given here as an example of how the Enigma database can be used to transfer information through the tool flow and between extraction stages in Mystic.

# 4.4.1 Extraction Stage 1

In this first stage of the extraction strategy we fit the low drain bias behaviour of our test case device and store the result of the extraction in the Enigma database.

```txt
## Stage name, for file naming.
name = "Stage1"
## Load the data and filter the zero substrate bias data into a separate
    → SimData object
IdVg25nm_LD = mdb.Load(instances={"l":25e-9}, bias={"d":0.05})IdVg25nm_LD_Vb0 =
    → IdVg25nm_LD.FilterData("eq", 0.0, dtype="bias.b")

## Set up parameters.
vth0    = OptParam('vth0',0.25,0.0,1.0,0.3)
voff    = OptParam('voff',-0.08,-1.0,1.0,0.1)
nfactor   = OptParam('nfactor',1,0.4,6.0,1)
minv    = OptParam('minv',0,-2,2.0,0.1)
k1    = OptParam('k1',0.5,-1.0,1.0,0.5)
k2    = OptParam('k2',-0.0186,-0.2,0.01,0.01)
ua    = OptParam('ua',1e-9,0.0,1.0e-6,1e-9)

# Store the initial Model object in the database to be used
# throughout the extraction
mdb.StoreInitialModel(Model)

## Group parameters for the two sub-stages.
Stage1Parameters = [vth0, voff, nfactor, minv, ua]
Stage2Parameters = [vth0, voff, nfactor, k1, k2, minv, ua] 
```

```python
## Do the extraction.
# Set the Tolerance for the DC solution.
Simulator.SetDCTolerance(1e-14)
Simulator.SetSimulationGMIN(1e-18)

# Set optimisation parameters (using BOUNDED_TRUST_REGION)
Optimiser.SetOptimisationParameter('fast_jacobian', True)
Optimiser.SetOptimisationParameter('jacobian_eps', 1.0e-2)
Optimiser.SetOptimisationParameter('eps6', 1.0e-5)

# Perform the first extraction sub-stage.
ExtractionUtils.DoStage(name, Model, Simulator, Stage1Parameters, Optimiser, [→ IdVg25nm_LD_Vb0])

# Now the second sub-stage.
ExtractionUtils.DoStage(name, Model, Simulator, Stage2Parameters, Optimiser, [→ IdVg25nm_LD])

## Calculate the errors.
ErrorMethod = "rmsd"
fit_error=ExtractionUtils.PrintErrors(name, IdVg25nm_LD, Simulator, Model, → ErrorMethod)

# And store the fitted result.
mdb.StoreFitData(IdVg25nm_LD, Model, description="Stage1 Low drain fitting data → .", error=fit_error)

## Write output graphs.
IdVg25nm_LD.WritePLTFile('./Graphs/{0}-25nm'.format(name)) 
```

<!-- page:49 -->
# 4.4.2 Extraction Stage 2

In this extraction stage we fit the above threshold behaviour of the test device using mobility and resistance parameters but use the previously stored low drain fitting data as a starting point for the second stage.

```txt
## Stage name, for file naming.
name = "Stage2"
## Load the data from the previous stage Model = mdb.GetFitModel("IdVg25nm_LD", project=="25nmN-Type-Test")
## Load the data back out. 
```

```python
IdVg25nm_LD = mdb.Load(instances={"1":25e-9}, bias={"d":0.05})

IdVg25nm_LD_Vb0 = IdVg25nm_LD.FilterData("eq", 0.0, dtype="bias.b")

## Create filtered data using the calculated Vt of the device as a filter value
# Use the FoM calculation method of the data to calculate Vt.
Vt_ld = IdVg25nm_LD_Vb0.Vt() [0]
# The use this Vt as a threshold for a variable filter.
AboveVt = DataFilter('ge', Vt_ld)
IdVg25nm_LD_AboveVt = IdVg25nm_LD.FilterData(AboveVt)
IdVg25nm_LD_AboveVt_Vb0 = IdVg25nm_LD_Vb0.FilterData(AboveVt)

## Set up parameters.
u0 = OptParam('u0', 0.03, 0.001, 1.0, 0.03)
uc = OptParam('uc', 0, -1e-6, 1.0e-6, 1e-10)
rdsw = OptParam('rdsw', 73, 40, 200, 70)

## Group parameters for the two sub-stages.
Stage1Parameters = [rdsw]
Stage2Parameters = [u0, uc]

## Do the extraction.
ExtractionUtils.DoStage(name, Model, Simulator, Stage1Parameters,
    Optimiser, [IdVg25nm_LD_AboveVt_Vb0])
ExtractionUtils.DoStage(name, Model, Simulator, Stage2Parameters,
    Optimiser, [IdVg25nm_LD_AboveVt])

## Calculate the errors.
ErrorMethod = "rmsd"
fit_error=ExtractionUtils.PrintErrors(name, IdVg25nm_LD, Simulator,
    Model, ErrorMethod)

# And finally store the result.
mdb.StoreFitData(IdVg25nm_LD, Model,
    description="Stage2 Low drain fitting data.", error=fit_error)

## Write output graphs.
IdVg25nm_LD.WritePLTFile('./Graphs/{0}-25nm'.format(name)) 
```

<!-- page:51 -->
# A Garand Dataset Type Strings

Numerous types of data can be stored by Garand in the Enigma database. The following provides a list of the string identifiers used in the Enigma database to reference different types of data that can be queried and loaded. See the Garand User Guide for more information.

# A.1 Id-Vg Simulation

The following data types can be queried from Garand IdVg simulations. In this case the independent variable of the data is always the gate voltage.

<table><tr><td>Identifier</td><td>Dependent Variable Description</td></tr><tr><td colspan="2">Contact currents (A)</td></tr><tr><td>IdVg</td><td>Drain</td></tr><tr><td>IsVg</td><td>Source</td></tr><tr><td>IgVg</td><td>Gate</td></tr><tr><td>IbVg</td><td>Body (substrate)</td></tr><tr><td colspan="2">Contact Capacitances (F)</td></tr><tr><td>CggVg</td><td>Gate to gate</td></tr><tr><td>CsgVg</td><td>Source to gate</td></tr><tr><td>CdgVg</td><td>Drain to gate</td></tr><tr><td>CbgVg</td><td>Body to gate</td></tr><tr><td>CgdVg</td><td>Gate to drain</td></tr><tr><td>CsdVg</td><td>Source to drain</td></tr><tr><td>CddVg</td><td>Drain to drain</td></tr><tr><td>CbdVg</td><td>Body to drain</td></tr><tr><td>CgsVg</td><td>Gate to source</td></tr><tr><td>CssVg</td><td>Source to source</td></tr><tr><td>CdsVg</td><td>Drain to source</td></tr><tr><td>CbsVg</td><td>Body to source</td></tr><tr><td>CgbVg</td><td>Gate to body</td></tr><tr><td>CsbVg</td><td>Source to body</td></tr><tr><td>CdbVg</td><td>Drain to body</td></tr><tr><td>CbbVg</td><td>Body to body</td></tr></table>

<!-- page:52 -->
# A.2 Id-Vd Simulation

The following data types can be queried from Garand IdVd simulations. In this case the independent variable of the data is always the drain voltage.

<table><tr><td>Identifier</td><td>Dependent Variable Description</td></tr><tr><td colspan="2">Contact currents (A)</td></tr><tr><td>IdVd</td><td>Drain</td></tr><tr><td>IsVd</td><td>Source</td></tr><tr><td>IgVd</td><td>Gate</td></tr><tr><td>IbVd</td><td>Body (substrate)</td></tr><tr><td colspan="2">Contact Capacitances (F)</td></tr><tr><td>CggVd</td><td>Gate to gate</td></tr><tr><td>CsgVd</td><td>Source to gate</td></tr><tr><td>CdgVd</td><td>Drain to gate</td></tr><tr><td>CbgVd</td><td>Body to gate</td></tr><tr><td>CgdVd</td><td>Gate to drain</td></tr><tr><td>CsdVd</td><td>Source to drain</td></tr><tr><td>CddVd</td><td>Drain to drain</td></tr><tr><td>CbdVd</td><td>Body to drain</td></tr><tr><td>CgsVd</td><td>Gate to source</td></tr><tr><td>CssVd</td><td>Source to source</td></tr><tr><td>CdsVd</td><td>Drain to source</td></tr><tr><td>CbsVd</td><td>Body to source</td></tr><tr><td>CgbVd</td><td>Gate to body</td></tr><tr><td>CsbVd</td><td>Source to body</td></tr><tr><td>CdbVd</td><td>Drain to body</td></tr><tr><td>CbbVd</td><td>Body to body</td></tr></table>

# A.3 Vt Simulation

Only one data type can be queried from Garand Vt search simulations.

<table><tr><td>Identifier</td><td>Dependent Variable Description</td></tr><tr><td>Vt</td><td>Threshold Voltage (V)</td></tr></table>

<!-- page:53 -->
# Bibliography

[1] Mark Lutz. Programming Python. O’Reilly, December 2010.   
[2] Mark Lutz. Dive Into Python. May 2004.   
[3] Python Software Foundation. Python.org. https://www.python.org/, 2017.   
[4] Synopsys Inc. HSPICE: The Gold Standard for Accurate Circuit Simulation. https://www. synopsys.com/verification/ams-verification/circuit-simulation/hspice.html, 2017.   
[5] UC Berkeley Device Group. BSIM 3. http://bsim.berkeley.edu/models/bsim3/, 2017.   
[6] UC Berkeley Device Group. BSIM 4. http://bsim.berkeley.edu/models/bsim4/, 2017.   
[7] UC Berkeley Device Group. BSIM-CMG. http://bsim.berkeley.edu/models/bsimcmg/, 2017.   
[8] UC Berkeley Device Group. BSIM-IMG. http://bsim.berkeley.edu/models/bsimimg/, 2017.   
[9] CEA-Leti. UTSOI. http://www.leti-cea.com/cea-tech/leti/english/Pages/Applied-Research/ Facilities/UTSOI.aspx, 2017.   
[10] TU-Delft/NXP. PSP. http://www.nxp.com/products/software-and-tools/models-and-test-data/ compact-models-simkit/mos-models/model-psp:MODELPSP, 2017.   
[11] Binjie Cheng, D. Dideban, N. Moezi, C. Millar, G. Roy, Xingsheng Wang, S. Roy, and A. Asenov. Statistical-variability compact-modeling strategies for bsim4 and psp. Design Test of Computers, IEEE, 27(2):26 –35, March-April 2010.   
[12] Synopsys Inc. Garand User Guide, Version O-2018.06. Synopsys Inc., 2018.   
[13] Andrew R. Conn, Nicholas I. M. Gould, and Philippe L. Toint. Trust-region Methods. Society for Industrial and Applied Mathematics, Philadelphia, PA, USA, 2000.   
[14] William H. Press, Saul A. Teukolsky, William T. Vetterling, and Brian P. Flannery. Numerical Recipes in C (2Nd Ed.): The Art of Scientific Computing. Cambridge University Press, New York, NY, USA, 1992.   
[15] M.J.D. Powell. A Direct Search Optimization Method That Models the Objective and Constraint Functions by Linear Interpolation. In Susana Gomez and Jean-Pierre Hennart, editors, Advances in Optimization and Numerical Analysis, volume 275 of Mathematics and Its Applications, pages 51–67. Springer Netherlands, 1994.

[16] wikipedia.org. Constrained optimization by linear approximation. http://en.wikipedia.org/wiki/ COBYLA, 2017.   
[17] M. J. D. Powell. Direct Search Algorithms for Optimization Calculations, 1998.   
[18] Synopsys Inc. Enigma User Guide, Version O-2018.06. Synopsys Inc., 2018.

<!-- page:55 -->
# Index

# B

Bounded Optimisation, 32

BSIM-CMG, 21

BSIM-IMG, 21

BSIMIMGVerilogModel, 22

# C

Command Line

Database, 8

Command Line Arguments

-a –script-args, 8

-d –db, 8

-ds –dataset, 8

-h –help, 8

-l –location, 8

-m –modelfile, 8

-o –optimiser, 8

Reference, 7

Supported Optimisers, 7

-v –version, 8

-x –spice-args, 8

Command Line Options

-m, 13

–modelfile, 13

Constrained Optimisation, 32

CreateMysticDataset, 45

CreateMysticProject, 44

CV Variables, 21

# D

Database, 13

CreateMysticDataset, 45

CreateMysticProject, 44

Creating a project, 44

Creating Datasets, 45

DeleteMysticProject, 45

Deleting a project, 45

Examples, 43

<!-- page:56 -->
GetFitData, 46

GetModelCard, 47

StoreFitData, 46

Storing fit data, 46

Storing Mystic data, 44, 46

Databases, 8

Dataset

Creating, 45

Storing, 46

<!-- page:57 -->
Debugging Verilog Model Usage, 23

DeleteMysticProject, 45

DTCO, 22

# E

Enigma database

Loading Garand Data, 13

Stored model card, 13

Error Calculation

MeanPercentageError, 40

MeanPercentageRMSError, 41

NormalisedRMSDeviation, 41

Errors

InputDataError, 13

Errors, Calculating, 18

Exceptions

InputDataError, 13

Exporting TCAD Data, 12

Extraction, 12

Pre-requisites, 17

Stages, 17

Uniform Model, 12

Extraction strategy development, 32

Extraction Utils

PrintErrors, 18

ExtractionUtils

DoStage, 17

# F

FDSOI, 21

FinFET, 21

# G

Garand Data set types, 51 IdVd, 52 Vt, 52

GarandData set types IdVg, 51

GetFitData, 46

GetModelCard, 47

Global Variables Model, 13

# H

HSPICE, 9, 24 HDL\_DIR, 24 PVA\_DIR, 24

HSPICE performance, 9

# L

Loading a SPICE model, 13

# M

MakeFoMTarget, 14 mdb Loading CV values, 21

Mystic Command Line Arguments, 7 Database connection, 8 Installation, 7 Preloaded Variables, 31 Running, 7

Mystic DB, 42 Loading Data, 13, 42

# O

Optimisation Parameters, 15 Optimiser, 10, 32 Bounded Trust Region, 36 COBYLA, 32, 33, 39

Constrained Optimisation, 33, 36, 39

Default, 36

Leavenburg-Marquardt, 32

Levenberg-Marquardt, 33, 38, 39

Optimisation Routines, 33

Scipy Trust Region, 37

Trust Region, 34, 37, 39 fast\_jacobian, 34, 36

Trust region algorithm, 33

OptParam, 16, 17

Output Data, 18

Synopsys PLT, 18

# P

Parameter History, 19

PLT File Output, 18

Project Creating, 44 Deleting, 45

# S

SimData, 14, 18, 29, 43, 46 Simulator SetAdditionalSpiceArguments, 23

SPICE, 9 HSPICE, 9 Simulator Options, 9 Supported Simulators, 9

SPICE model Loading, 13

Spice Model, 10

Statistical, 20

StoreFitData, 46

Storing Mystic Data, 46

Sub-Circuit Models, 27

SubCktModel, 29

Supported Optimisers, 7

# T

Temporary directories, 23

# U

Utility Functions

LoadModel, 13

# V

Verilog, 10

Verilog Models, 21, 25

BSIMIMGVerilogModel, 22

Commands, 22

Debugging, 23

Example, 26

HSPICE, 24

SetAdditionalSpiceArguments, 23

Supported Models, 22
