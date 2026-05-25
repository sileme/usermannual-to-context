<!-- page:1 -->
# Inspect User Guide

Version O-2018.06, June 2018

# Copyright and Proprietary Information Notice

<!-- page:2 -->
© 2018 Synopsys, Inc. This Synopsys software and all associated documentation are proprietary to Synopsys, Inc. and may only be used pursuant to the terms and conditions of a written license agreement with Synopsys, Inc. All other use, reproduction, modification, or distribution of the Synopsys software or the associated documentation is strictly prohibited.

# Destination Control Statement

All technical data contained in this publication is subject to the export control laws of the United States of America. Disclosure to nationals of other countries contrary to United States law is prohibited. It is the reader’s responsibility to determine the applicable regulations and to comply with them.

# Disclaimer

SYNOPSYS, INC., AND ITS LICENSORS MAKE NO WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, WITH REGARD TO THIS MATERIAL, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.

# Trademarks

Synopsys and certain Synopsys product names are trademarks of Synopsys, as set forth at https://www.synopsys.com/company/legal/trademarks-brands.html.

All other product or company names may be trademarks of their respective owners.

# Third-Party Links

Any links to third-party websites included in this document are for your convenience only. Synopsys does not endorse and is not responsible for such websites and their practices, including privacy practices, availability, and content.

Synopsys, Inc.

690 E. Middlefield Road

Mountain View, CA 94043

www.synopsys.com

<!-- page:3 -->
# About This Guide xi

Related Publications . . xi

Conventions . xi

Customer Support . . . xi

Accessing SolvNet. . . . xii

Contacting Synopsys Support . . . . xii

Contacting Your Local TCAD Support Team Directly. . . . . xi

# Chapter 1 Introducing Inspect 1

Functionality of Inspect .

User Interface . .

Datasets Group Box . . .

Curves Group Box . . . .

Plot Area . .

Supported File Types and Data Formats. . . . .

Data Formats . .

Parameter Files . . .

Save Files . . . .

Starting Inspect From the Command Line . . .

Examples of Using Command-Line Options. . . .

# Chapter 2 Basic Operations Using the User Interface 7

Loading Datasets. . .

Reloading Datasets . . .

Updating Datasets Automatically . . . .

Applying Plotting Actions . . .

Zoom Operations. . . .

Working With Scripts . . .

Creating Scripts . . . .

Running Scripts . . . . . . 10

Preferences . . . 10

Saving Files . . . .

Exporting Curve Data . . . .

Printing Curves Shown in the Plot Area . . .

Saving Curves in PNG Format . . . 12

<!-- page:4 -->
# Chapter 3 Working With Curves 13

Selecting Multiple Projects and Groups . . . . 13

Creating Curves. . . . 13

Automatically Generated Curve Names and Legend Text . . . . 14

Selecting and Unselecting Curves. . . . 14

Changing Attributes of a Curve . . . 15

Example: Displaying a Curve With Data Points and No Lines Between Points. . . . . 16

Moving the Legend . . . 17

Reordering Curves . . . 17

Creating Curves. . . . 17

Creating Curves Automatically When Loading Files . . . .

Creating Curves Using Formulas. . . . 18

Example: Creating a Curve That Is the Difference Between Two Curves. . . . . . . 19

Creating Curves Using Macros and Library Formulas . . . 19

Deleting Curves. . . . 20

# Chapter 4 Configuring the View 21

Modifying Axes . . . . 21

Scaling an Axis . . . . 21

Handling Data When Axes Set to Logarithmic Scale . . . . . 21

Limits of Axes Set to Logarithmic Scale. . . . 22

Changing Attributes of Axes . . . . 22

Configuring the Plot Area . . . . 24

Changing Attributes of Plot Area . . . . 24

Adding Labels . . . 26

Displaying the Dataset of a Curve . . . 27

Cleaning Up the Plot Area . . . . . 27

Sampling Points in the Plot Area . . . . 28

# Chapter 5 Curve Interpolation and Operations 29

Curve Operations . . . . 29

Limitation of the X-Axis Values of the Dataset . . . 30

More Than One Curve in a Formula . . . 30

Handling Datasets in Formula Processing . . . . 31

Dataset Created for Result Curves . . . . 32

Curve Handling on Interpolation . . . . 32

Determining the Scale (Linear or Logarithmic) of Curves . . . . 33

<!-- page:5 -->
# Chapter 6 Formulas and Macros 35

Using Formulas . . . . 35

Formula Library . . . . 35

Using Macros . . . 38

Example: ADD Macro . . . . 38

Example: DIFFMULT Macro . . . . 39

# Chapter 7 Using the Scripting Language 41

Overview of the Scripting Language . . . . 41

General-Purpose Commands. . . . 42

ft\_scalar . . . . 42

Reading and Writing Files . . . . 42

cv\_write . . . . 42

fi\_writeBitmap . . . . . . 43

fi\_writeEps . . . . . . 43

fi\_writePs . . . . 44

graph\_load . . . . 44

graph\_write . . . . . 45

param\_load. . . . . 45

param\_write . . . . . 45

proj\_getDataSet . . . . . 46

proj\_getList . . . . . 46

proj\_getNodeList . . . . . . . 46

proj\_load . . . . 47

proj\_unload . . . 47

proj\_write . . . . . 47

Creating, Displaying, and Deleting Curves . . . . . 48

cv\_create . . . . 48

cv\_createDS . . . . 48

cv\_createFromScript . . . 49

cv\_createWithFormula. . . . . 49

cv\_delete . . . . 50

cv\_display . . . . . . 50

cv\_logScale, cv\_log10Scale . . . . . . 50

cv\_split . . . . 51

cv\_split\_disc . . . . 51

Changing Attributes . . . . . 52

cv\_lineColor. . . . 52

cv\_lineStyle . . . . 52

cv\_renameCurve . . . . 52

<!-- page:6 -->
cv\_set\_interpol. . . 53

cv\_setCurveAttr . . . . . 53

gb\_setpreferences. . . . . 54

gr\_createLabel . . . 54

gr\_deleteLabel . . . 54

gr\_formatAxis . . . . 55

gr\_mappedAxis . . . . 55

gr\_precision . . . 55

gr\_setAxisAttr . . . . . . 56

gr\_setGeneralAttr. . . . 56

gr\_setGridAttr . . . 57

gr\_setLegendAttr . . . . . 57

gr\_setLegendPos . . . . 58

gr\_setTitleAttr . . . 58

Accessing Curve Data . . . . . . 58

cv\_getVals . . . . . 58

cv\_getValsX. . . 59

cv\_getValsY. . . 59

cv\_getXaxis . . . . 59

cv\_getYaxis . . . . . 60

cv\_printVals. . . . . 60

Transforming Curve Data . . . . . 60

cv\_abs . . 60

cv\_delPts . . . . 61

cv\_inv. . . . 61

cv\_reset . . . 61

Extracting Parameters . . . . 62

f\_Gamma . . . 62

f\_gm . . . . 62

f\_hideInternalCurves . . . . . 62

f\_IDSS . . . . 63

f\_KP . . . 63

f\_Ron . . . . 63

f\_Rout . . . . 64

f\_showInternalCurves . . . . . 64

f\_TetaG . . 64

f\_VT. . . 65

f\_VT1. . . 65

f\_VT2. . . 66

Computing. . . . . . 66

cv\_compute . . . 66

<!-- page:7 -->
cv\_getZero . . . . . . 66

macro\_define . . . . 67

Controlling Scripts . . . . . . 67

script\_break . . . . 67

script\_exit. . . . 67

script\_sleep . . . . . 68

Examples of Using the Scripting Language . . . . . 68

Computing the Dose of Implanted Arsenic . . . . 68

Creating a Macro to Compute Vt. . . . 68

# Chapter 8 Working With Script Libraries 69

Loading Libraries . . . 69

Adding a Site Library . . . . 69

Extraction Library . . . . . . 70

cv\_linTransCurve. . . . . 70

cv\_scaleCurve . . . 71

ExtractBVi . . . 71

ExtractBVv . 72

ExtractEarlyV . . 72

ExtractGm . 73

ExtractGmb . . 73

ExtractIoff . . 73

ExtractMax. . . . 74

ExtractRon . . . . 74

ExtractSS . . . 75

ExtractValue . . . 75

ExtractVtgm . . . . . . 76

ExtractVtgmb. . . . 77

ExtractVti . . . 77

FilterTable . . . 78

Syntax of FilterTable . . . . 78

The extend Library . . . . . . 80

cv\_addCurve . . . . . 81

cv\_addDataset . . . 81

cv\_angularMap . . . . 82

cv\_autoIncrStyle . . . . . 82

cv\_disp . . . . . 83

cv\_exists. . . . . . 83

cv\_getGlobalExtrema . . 84

cv\_getLocalExtrema . . . . 84

cv\_getNames . . . . . . 85

<!-- page:8 -->
cv\_getRange. . . . . 85

cv\_getXmax . . . . 85

cv\_getXmin . . . . . 86

cv\_getYmax . . . . . 86

cv\_getYmin . . . . 86

cv\_integrate . . . . . . 87

cv\_isVisible . . . . . 87

cv\_linFit . . . . 88

cv\_linTrans . 88

cv\_monotonicX . . 89

cv\_nextColor . . . . . 89

cv\_nextLine . . . . . 90

cv\_nextSymbol . . 90

cv\_resetColor . . . 91

cv\_resetFillColor . . . . . 91

cv\_resetLine. . . . . 92

cv\_resetStyle . . . 92

cv\_resetSymbol . . . 93

cv\_round . . 93

cv\_scale . . 9 4

cv\_setFillColor. . . . . 94

cv\_setSymbol. . . . 95

cv\_sort . . 95

cv\_write . . . . . 96

dbputs . . . . . 96

ds\_getValue . . . . . 97

fi\_readTxtFile . . . 97

fi\_readTxtFileHeader. . . . 98

gr\_axis . . 98

gr\_resetAxis . . . . . . 99

gr\_setStyle . . . . . . 99

ldiff. . . . 100

lintersect . . . . 100

ltranspose . . . . . 101

lunion . . . . 101

proj\_check . . . . 102

proj\_datasetExists . . . . . . 102

proj\_getGroups . . . . . 103

proj\_groupExists . . . . . . 103

proj\_loadPlx . . . . . . 104

The PhysicalConstants Library . . . . 105

<!-- page:9 -->
IC-CAP Model Parameter Extraction Library . 106

Exporting Data . . . . . 106

Header Information . . 107

userInput . . . . . 107

iccapInput . . . . . . 107

output . . . . 108

Array Data . . . . . 108

Curve Comparison Library . . . . . 109

cvcmp\_CompareTwoCurves . . . . . 109

cvcmp\_DeltaTwoCurves . . . . . 109

References. . . 110

# Appendix A Elements of User Interface 111

Toolbar Buttons. . . 1

File Menu 112

Edit Menu . . 113

Curve Menu. . . . . 113

Script Menu . . . . . . 114

Extensions Menu. . . . . 115

Help Menu. . . . 115

# Appendix B Limitations in Inspect 117

The diff(…formula…) and integr(…formula…) Operators . . . 117

The vecvalx(…formula…) and vecvaly(…formula…) Operators . . . . 117

No Support for Right Y-Axes . . . . . 118

<!-- page:10 -->
Contents

<!-- page:11 -->
Inspect is a curve display and analysis program. It works with curves specified at discrete points. Inspect enables users to work interactively with data using both a user interface and a scripting language.

# Related Publications

For additional information, see:

The TCAD Sentaurus™ release notes, available on the Synopsys SolvNet® support site (see Accessing SolvNet on page xii).   
■ Documentation available on SolvNet at https://solvnet.synopsys.com/DocsOnWeb.

# Conventions

The following conventions are used in Synopsys documentation.

<table><tr><td>Convention</td><td>Description</td></tr><tr><td>Blue text</td><td>Identifies a cross-reference (only on the screen).</td></tr><tr><td>Bold text</td><td>Identifies a selectable icon, button, menu, or tab. It also indicates the name of a field or an option.</td></tr><tr><td>Courier font</td><td>Identifies text that is displayed on the screen or that the user must type. It identifies the names of files, directories, paths, parameters, keywords, and variables.</td></tr><tr><td>Italicized text</td><td>Used for emphasis, the titles of books and journals, and non-English words. It also identifies components of an equation or a formula, a placeholder, or an identifier.</td></tr><tr><td>Key+Key</td><td>Indicates keyboard actions, for example, Ctrl+I (press the I key while pressing the Control key).</td></tr><tr><td>Menu &gt; Command</td><td>Indicates a menu command, for example, File &gt; New (from the File menu, select New).</td></tr></table>

# Customer Support

Customer support is available through the Synopsys SolvNet customer support website and by contacting the Synopsys support center.

<!-- page:12 -->
# Accessing SolvNet

The SolvNet support site includes an electronic knowledge base of technical articles and answers to frequently asked questions about Synopsys tools. The site also gives you access to a wide range of Synopsys online services, which include downloading software, viewing documentation, and entering a call to the Support Center.

To access the SolvNet site:

1. Go to the web page at https://solvnet.synopsys.com.   
2. If prompted, enter your user name and password. (If you do not have a Synopsys user name and password, follow the instructions to register.)

If you need help using the site, click Help on the menu bar.

# Contacting Synopsys Support

If you have problems, questions, or suggestions, you can contact Synopsys support in the following ways:

Go to the Synopsys Global Support Centers site on synopsys.com. There you can find email addresses and telephone numbers for Synopsys support centers throughout the world.   
Go to either the Synopsys SolvNet site or the Synopsys Global Support Centers site and open a case online (Synopsys user name and password required).

# Contacting Your Local TCAD Support Team Directly

Send an e-mail message to:

support-tcad-us@synopsys.com from within North America and South America   
support-tcad-eu@synopsys.com from within Europe   
support-tcad-ap@synopsys.com from within Asia Pacific (China, Taiwan, Singapore, Malaysia, India, Australia)   
support-tcad-kr@synopsys.com from Korea   
support-tcad-jp@synopsys.com from Japan

<!-- page:13 -->
This chapter introduces Inspect and its user interface.

# Functionality of Inspect

Inspect can display and analyze curves. It features a user interface, a scripting language, and an interactive language for computations with curves.

An Inspect curve is a sequence of points defined by a one-dimensional array of x-coordinates and y-coordinates (floating-point values). An array of coordinates that can be mapped to one of the axes is referred to as a dataset. In Inspect, datasets can be combined and mapped to the x-axis and y-axis to create and display a curve.

Inspect works on data consisting of groups of datasets. Each group consists of two or more datasets of equal length, where elements with an identical index represent related values. Datasets in a group can be divided into named groups. By pairing related values of two datasets from the same group, points (or nodes) of a discrete curve are obtained.

Usually, a dataset represents a physical quantity, such as voltage, current, or time. Groups of datasets represent functionally related physical quantities, for example, measurements of current and voltage, and the times at which these measurements are taken. Named groups represent semantically related datasets, for example, meshing results at one of several contacts of a semiconductor device.

In addition to its name, a dataset can have other attributes associated with it, for example, the name of the physical quantity represented by the dataset, the name of the unit in which this quantity has been measured, the preferred color of the curve when it is visualized, and interpolating function. Depending on the particular input file format, this information can be stored partially in the data file and partially in separate files.

Inspect can read different data formats and file formats (see Data Formats on page 4).

Data in TDR and TIF formats contains the names of the physical quantities that datasets represent. The TDR and TIF formats allow you to split a dataset group into named groups.

Data in XGRAPH format always has groups consisting of two datasets only. Additional dataset attributes are specified inside the file with appropriate keywords.

<!-- page:14 -->
To distinguish datasets from different data files, the datasets from one data file are grouped into a project. The name of the data file without an extension is taken as the project name. When more than one file with the same name is loaded, Inspect adds the suffix .n to the project name, where n is the smallest number not yet used as a suffix for another project name.

# User Interface

The user interface of Inspect has the following work areas (see Figure 1):

■ Datasets group box   
Curves group box   
Plot area

![](images/inspect_ug_ae521086937454598949adf0f508d5af296c7fbf0242cc01367113ace43f18d7.jpg)

<details>
<summary>line</summary>

| Curve Type             | Value       |
| ---------------------- | ----------- |
| TotalCurrent_substrate | 0           |
| TotalCurrent_source    | -8e-17      |
| TotalCurrent_drain     | 0           |
</details>

Figure 1 Main window of Inspect showing work areas

The menus and toolbar buttons are documented in Appendix A on page 111.

The status line at the bottom of the main window displays information about the current Inspect session and the position of the pointer in the plot area.

<!-- page:15 -->
# Datasets Group Box

This group box has the following panes for selecting and combining datasets to create curves:

The top pane lists the currently loaded data files (or projects). In the example shown in Figure 1 on page 2, only one data file n57\_des has been loaded (the file extension is not displayed).   
The middle pane lists the names of the dataset groups belonging to the selected data file. A group having one or more datasets can correspond to an electrode or a thermode of a device. Datasets that do not belong to any group are also displayed. In Figure 1, hTave and hTmax are independent datasets. In addition, drain, source, substrate, and gate are groups, each having several datasets.   
■ The bottom pane lists the names of the datasets belonging to the selected group.

The To X-Axis, To Left Y-Axis, and To Right Y-Axis buttons map datasets to a particular axis.

# Curves Group Box

This group box has one pane that displays the names of existing curves, and it has the following buttons:

Click New to create a curve using the formula library (see Creating Curves Using Formulas on page 18).   
Click Edit to change the graphical attributes of a curve (see Changing Attributes of a Curve on page 15).   
Click Delete to remove curves that are selected in the pane.   
■ Click Delete All to remove all curves in the pane.

# Plot Area

The plot area is where curves are drawn. The toolbar buttons are used to change the coordinate system for zooming sessions, to display or remove the legend text, to change the order in which curves are displayed, and to switch between linear and logarithmic scale.

<!-- page:16 -->
# Supported File Types and Data Formats

This section describes the supported file types and data formats in Inspect.

# Data Formats

Inspect works with different file formats, which contain a series of points, described by x-coordinates and y-coordinates, representing datasets. Inspect handles and displays these datasets as curves.

Table 1 Supported data formats 

<table><tr><td>Data format</td><td>Description</td></tr><tr><td>CSV</td><td>Comma-separated value format, which is recognized by many applications. The file extension is .csv.</td></tr><tr><td>PLT</td><td>Plain text format for 1D curves.</td></tr><tr><td>PLX</td><td>Format generated by Sentaurus Process.</td></tr><tr><td>TDR</td><td>Format recognized by most Synopsys TCAD tools. The file extension is .tdr.For a description of the TDR format, see the  $Sentaurus^{TM} Data Explorer User Guide$ .</td></tr><tr><td>TIF</td><td>Synopsys TCAD format for I–V curves, recognized by most Synopsys TCAD tools. The file extension is .ivl. For a description of the TIF format, see the  $Taurus^{TM} Visual User Guide$ , Data Formats.</td></tr><tr><td>TXT</td><td>Tab-delimited text format. The file extension is .txt. Each curve is written into a block with the curve name, and the x- and y-data.</td></tr><tr><td>XGRAPH</td><td>Each curve is written into a block with the curve name, and the x- and y-data. The file extension is .xy. Typically, there is one xy data–point pair per line. Each value or column is separated by space, tabs, commas, semicolons, or colons.For more information, go to http://www.xgraph.org.</td></tr><tr><td>XMGR</td><td>Format used by the shareware xy plotting tool Xmgr. The file extension is .xmgr.For more information, go to http://plasma-gate.weizmann.ac.il/Xmgr/.</td></tr></table>

# Parameter Files

When Inspect is customized interactively according to user preferences, the current setup can be stored in a parameter file, which usually has the extension .par. In a parameter file, Inspect stores the following information:

Plot area attributes   
Coordinate area attributes

Axes attributes   
User-defined macros   
Printer setup   
Curve attributes

<!-- page:17 -->
When Inspect is started, it looks for a parameter file named inspect.par in the current directory. If such a file is found, Inspect loads it and sets the plot settings, macros, and printer setup according to the values in this file. If no file is found in the current directory, Inspect looks for a parameter file named inspect.par in the STDB directory. If no file is found, Inspect uses the default values.

You can also load a parameter file explicitly when starting Inspect or during its execution.

Curve attributes saved in the parameter file are not applied automatically to curves in Inspect. To do this, you must specify the command-line option -applyCurveAttr when starting Inspect.

# Save Files

The entire current state of Inspect (projects, curves, and settings) can be saved to a save file, which is used to restore the saved state at any time and usually has the extension .sav.

Data from all loaded projects is also stored in a save file. This means that for restoring the saved state, the data files are no longer necessary.

# Starting Inspect From the Command Line

You can start Inspect from the command line by typing:

inspect [<options>] [<FILES>]

You can also specify options (see Table 2 on page 6) and files on the command line. See Examples of Using Command-Line Options on page 6.

The <FILES> arguments can be one or several data files, or a save file that is loaded when Inspect is started. Inspect automatically distinguishes between data files and save files.

NOTE You can also start Inspect from Sentaurus Workbench.

Table 2 Command-line options 

<table><tr><td>Option</td><td>Description</td></tr><tr><td>-applyCurveAttr</td><td>Applies curve attributes saved in a parameter file (.par) and a save file (.sav).</td></tr><tr><td>-batch</td><td>If specified, Inspect does not open the user interface while executing a script file.</td></tr><tr><td>-c FILE $^{1}$ </td><td>Reads the specified setup file after Inspect is launched.</td></tr><tr><td>-display</td><td>Sets the display to use.</td></tr><tr><td>-f FILE $^{1}$ </td><td>Executes the specified script file after Inspect is launched.</td></tr><tr><td>-geometry</td><td>Sets the size and position of the main window of Inspect.</td></tr><tr><td>-h[elp]</td><td>Displays information about the command-line options.</td></tr><tr><td>-m FILE $^{1}$ </td><td>Executes the specified macro file after Inspect is launched.</td></tr><tr><td>-oldInterpol</td><td>Forces Inspect to use the interpolation criteria of earlier versions.</td></tr><tr><td>-oldplx</td><td>Loads a .plx file and automatically creates curves with the old scheme.</td></tr><tr><td>-v[ersion]</td><td>Prints the version of Inspect.</td></tr><tr><td>-verbose</td><td>Displays all messages.</td></tr></table>

1. Simulation results (.plt, .tdr, .ivl) files as well as save (.sav) files.

<!-- page:18 -->
# Examples of Using Command-Line Options

Inspect starts in interactive mode and loads datasets from the n53\_des.plt file:

inspect n53\_des.plt

Inspect starts in interactive mode, loads three data files, and reads the plot area, axes, macros, and printer setup from the parameter file mySetup.par:

inspect file1.plt file2.plt file3.plt -c mySetup.par

Inspect starts in interactive mode and executes the bipolar.cmd script file:

inspect -f bipolar.cmd

Inspect starts in batch mode and executes the bipolar.cmd script file:

inspect -batch -f bipolar.cmd

<!-- page:19 -->
# CHAPTER 2

# Basic Operations Using the User Interface

This chapter describes the basic operations in Inspect using its user interface.

# Loading Datasets

You must open a data file to load a dataset.

To load a dataset:

1. Choose File > Load Dataset, or press Ctrl+L. The Load Dataset dialog box is displayed.

2. Select a data file by changing the Files of type field if needed.

3. Click Open or double-click a file to open it.

# Reloading Datasets

You can reload displayed datasets if the file is updated while viewing it in Inspect.

To reload a dataset:

■ Choose File > Update Datasets, or press Ctrl+U.

# Updating Datasets Automatically

If a dataset displayed in the plot area is updated frequently by other tools, such as the Optimizer tool, it can be useful to reload the dataset frequently so that refreshed data is shown in the plot area.

<!-- page:20 -->
To update datasets automatically:

1. Choose File > Automatically Update Datasets.

The Automatic Update dialog box is displayed.

![](images/inspect_ug_bdd71e43f6cd13968f0e765842a0782820dd17cb5260058c69313afce797bee8.jpg)

<details>
<summary>text_image</summary>

Automatic Update
Enable
Seconds 60
OK Cancel
</details>

2. Select Enable.   
3. Set the time (in seconds) between reloads.   
4. Click OK.

# Applying Plotting Actions

When working with multiple datasets of a similar structure, it is useful to apply several plotting actions made on one dataset to other datasets. These plotting actions include creating curves (explicitly and by formula) and changing curve attributes. Inspect stores the set of actions made on the current dataset.

To repeat plotting actions for another dataset:

1. Select the dataset or datasets.   
2. Choose Edit > Redo Last Plot, or press Ctrl+E.

All plotting actions are applied to the selected datasets.

This feature is helpful when datasets contain data of a similar structure, for example, projects with groups of the same names. Otherwise, it can happen that the current dataset does not contain some data necessary for creating a curve. In this case, Inspect generates an error message.

NOTE Inspect stores plotting actions applied to the currently selected dataset only. When you select another dataset, the accumulated set of stored actions is cleaned up.

<!-- page:21 -->
# Zoom Operations

To perform zoom operations on curves displayed in the plot area, use the relevant toolbar buttons (see Table 7 on page 111).

# Working With Scripts

In Inspect, any sequence of operations can be stored and reproduced using scripts (see Chapter 7 on page 41). The recorded operations are repeated when the script is executed. The following operations can be recorded in a script:

■ Loading and unloading projects   
■ Loading and saving the current project   
■ Changing axis attributes   
■ Exporting, creating, and deleting curves   
Changing curve attributes   
Transforming actions on curves   
■ Any use of the formula library to create other curves

# Creating Scripts

To create a script:

1. Choose Script > Record > Start.   
The Record Script File dialog box is displayed.   
2. Select or create a script file, and click Save.   
Inspect starts to store every operation until you stop recording.   
3. Choose Script > Record > Stop.

<!-- page:22 -->
# Running Scripts

# To run a script:

1. Choose Script > Run Script, or press Ctrl+R.   
The Run Script File dialog box is displayed.   
2. Select a script file.   
3. Click Open.

# Preferences

In Inspect, preferences relate to the precision of values handled for curve coordinates and the interpolation method used to operate on and display curves.

# To set the preferences:

1. Choose File > Preferences.

The Preferences dialog box is displayed.

![](images/inspect_ug_a074f0a454de4461260c8d56cd1f8e7bc71c3563ea970e65796f7fc4fbfb0920.jpg)

<details>
<summary>text_image</summary>

Preferences
General
Use Old Interpolation
Precision: 0
OK Apply Cancel
</details>

2. In the Precision box, select the number that indicates how many decimal digits are used to handle coordinates for curve points.   
3. If required, select Use Old Interpolation to force Inspect to use the interpolation criteria of earlier versions to handle all computations with curves.   
4. Click OK.

<!-- page:23 -->
# Saving Files

To save files, you can either:

■ Choose File > Save Setup to save the current setup in a parameter .par file.   
■ Choose File > Save All to save the entire current state of Inspect in a .sav file.

# Exporting Curve Data

Curve data can be written to data files in different formats (see Data Formats on page 4). You can select different formats from the File > Export command.

To export curve data in TDR format:

1. Choose File > Export > TDR.   
The Write .tdr File dialog box is displayed.   
2. Select or create a TDR file.   
3. Click Save.

# Printing Curves Shown in the Plot Area

Curves shown in the plot area can be printed as a single image.

To print curves shown in the plot area:

1. Choose File > Print, or press Ctrl+P.

The Printer Setup dialog box is displayed.

On the Windows operating system, a standard print dialog box is displayed. On Linux operating systems, a special print dialog box is displayed (see Figure 2 on page 12).

2. Specify the print configuration as required.

NOTE In the Command field, you can specify a command for using the printer.

3. Click OK.

![](images/inspect_ug_9f4bef0cca5c4b64b60b3a0655a7020fc1774dff6e7dab6c136daef80e2a56dc.jpg)

<details>
<summary>text_image</summary>

Printer Setup
Image Size
Height: 9.0
Width: 6.0
Paper Size
A4
A3
US Letter
Image Offset
Height: 1.0
Width: 1.0
Orientation
Portrait
Landscape
Units
inches mm cm
Command lpr @
OK Cancel
</details>

Figure 2 Printer Setup dialog box

<!-- page:24 -->
# Saving Curves in PNG Format

Curves shown in the plot area can be saved as a bitmap file in PNG format. This bitmap file can be imported into applications for documentation and reporting purposes.

To save curves in PNG file format:

1. Choose File > Write Bitmap, or press Ctrl+W.

The Write PNG bitmap file dialog box is displayed.

2. Enter the name of the file.   
3. Click Save.

You can save the curves shown in the plot area in a .png file directly from your Inspect script using the fi\_writeBitmap command (see fi\_writeBitmap on page 43). This is a screenimage exporting method that works when Inspect starts in interactive mode.

NOTE Since this exporting method is based on the X11 utility xwd, it works only if a valid DISPLAY is available, that is, an X server is required.

<!-- page:25 -->
This chapter describes how to create and work with curves using the user interface of Inspect.

# Selecting Multiple Projects and Groups

Inspect displays curves that are formed by datasets from different data files.

You select projects and groups from the Datasets group box (see Datasets Group Box on page 3). If you select more than one group, only the dataset names that exist in all the selected groups appear in the bottom pane.

In Figure 1 on page 2, if two groups (drain and source) are selected in the middle pane, the dataset names OuterVoltage, InnerVoltage, QuasiFermiPotential, DisplacementCurrent, eCurrent, and hCurrent appear in the bottom pane. If the group hTmax is selected, in addition, no dataset names are displayed in the bottom pane because no datasets with identical names exist in all the selected groups.

NOTE The names of datasets must be identical. Datasets, themselves, can be different.

When more than one project is loaded, the same rule applies. Consequently, Inspect shows only common groups and datasets of multiple-selected projects in the middle and bottom panes of the Datasets group box.

# Creating Curves

The first curve displayed in Figure 1 maps time to the x-axis and TotalCurrent of drain to the left y-axis.

# To create a curve:

1. Select the dataset group time in the middle pane of the Datasets group box.   
2. Click To X-Axis.   
3. Select the group drain in the middle pane of the Datasets group box.

4. Select the dataset TotalCurrent from the bottom pane of the Datasets group box.   
5. Click To Left Y-Axis.

<!-- page:26 -->
Inspect draws a curve in the plot area using these two datasets. The name of the curve is generated automatically using names and other attributes of groups and datasets (and possibly projects). The upper-right corner of the plot area shows the legend, which displays curve names and drawing styles.

The second curve is created in the same way: time is mapped to the x-axis and TotalCurrent from source is mapped to the left y-axis. The next curve is created with time mapped to the x-axis and TotalCurrent from substrate mapped to the right y-axis.

When these steps are completed, the main window of Inspect resembles Figure 1 on page 2.

# Automatically Generated Curve Names and Legend Text

When a curve is created, a default name for it is generated. With plot files (TDR or TIF files), the name is a combination of the physical quantity name and the group name of the y-dataset if the dataset belongs to a group.

For example, if the physical quantity name is OuterVoltage and the dataset belongs to a group named drain, the curve name is OuterVoltage\_drain.

With XGRAPH files, a default name is created using the data file name and the comment line preceding the dataset pair in the file. If the generated curve name already exists, an .n suffix is added, where n is the smallest number not yet used as a suffix in another name.

In addition to a name, a curve has legend text, which identifies the curve in the plot area. When a curve is created, the corresponding text is initialized with the curve name.

# Selecting and Unselecting Curves

To select a curve:

■ Click the curve name in the Curves group box, or click the curve name in the legend.

After selection, the curve name is highlighted in the Curves group box, the plot area, and the legend.

To unselect a curve:

Right-click in the plot area.

<!-- page:27 -->
# Changing Attributes of a Curve

A curve is displayed according to its attributes. When a curve is created, default values are assigned to all attributes. A curve is drawn with lines connecting nodes and, optionally, with node markers.

To change the attributes of a curve:

1. Double-click a curve in the plot area or in the Curves group box.

The Curve Attributes dialog box is displayed (see Figure 3 on page 16).

2. On the General tab, change the axis to which the curve is mapped, if required.

3. On the Line tab, change the following attributes of lines:

Color Default color is assigned from a list of colors that are not assigned to existing curves.

Style When all available colors are exhausted, a line drawing style is assigned from a list of styles, so that each curve has a unique combination of color and style.

Width Line width in pixels. Default: 1.

4. On the Marker tab, change the following attributes of node markers:

Shape No node markers by default.

Size Size of markers in pixels. Default: 5.

Outline Color It is the same as the line color by default.

Outline Width Width of markers in pixels. Default: 1.

Fill Color It is the same as the line color by default.

5. On the Interpolation tab, change the interpolation used on the x-axis and y-axis, if required.

6. Click Apply.

7. Click OK.

![](images/inspect_ug_30f320b386db2af783df97658711c1cb7465483e4d44f981ec50350bfa55d7f7.jpg)

<details>
<summary>text_image</summary>

Curve Attributes
General Line Marker Interpolation
Name: TotalCurrent_source
Legend: TotalCurrent_source
Quantity: TotalCurrent
X Dataset: n57_des time
Y Dataset: n57_des source TotalCurrent
Map Curve To
◆ Left Y-Axis ◆ Right Y-Axis
OK Apply Cancel
</details>

![](images/inspect_ug_485ad58dfb4f23f55aedebab54acd3ca42c9c45b2c5834ec26a8d6695e741c53.jpg)

<details>
<summary>text_image</summary>

Curve Attributes
General Line Marker Interpolation
Color:
Style: solid
Width: 3
OK Apply Cancel
</details>

![](images/inspect_ug_df062096c3fa0506c1748a4e52aa6e6faa889d506b9f448f21d9eae33dbf2e02.jpg)

<details>
<summary>text_image</summary>

Curve Attributes
General Line Marker Interpolation
Shape: none
Size: 5
Outline Color:
Outline Width: 1
Fill Color:
OK Apply Cancel
</details>

![](images/inspect_ug_1cdd8f1a90bdb72c157ead80d118786ccb0e2701d5c4aa8282cd67793315cd8a.jpg)

<details>
<summary>text_image</summary>

Curve Attributes
General Line Marker Interpolation
X-Axis Lin Log Auto
Y-Axis Lin Log Auto
OK Apply Cancel
</details>

Figure 3 Curve Attributes dialog box with all tabs shown

# Example: Displaying a Curve With Data Points and No Lines Between Points

<!-- page:28 -->
To display a curve with data points and no lines between these points:

1. Double-click a curve in the plot area or in the Curves group box.   
The Curve Attributes dialog box is displayed (see Figure 3).   
2. Click the Marker tab.   
3. In the Shape box, select circle.

4. Click the Line tab.   
5. Set Width to 0.   
6. Click Apply.   
7. Click OK.

<!-- page:29 -->
# Moving the Legend

To move the legend in the plot area:

■ Use the middle mouse button and drag the legend to its new location.

# Reordering Curves

You can change the order in which curves are displayed in the plot area to distinguish one curve from another, for example, if some have a significant intersection.

To reorder curves:

Choose one of the following options from the Curve menu (see Curve Menu on page 113) or click the corresponding toolbar button:

• Drawing Order > Move to Front   
• Drawing Order > Move to Back   
• Drawing Order > Move Forward   
• Drawing Order > Move Backward

![](images/inspect_ug_a13b6687c1c56f5637fe5d33a3463ca1eb202595389e11f3d97417e4d550546a.jpg)

![](images/inspect_ug_1ff610b79b90f7d9d7e6eda19cf5509ee6acbead4fa211742ae7d7197f7859d6.jpg)

![](images/inspect_ug_a62881b56559bc85c88f930291803bbe8fee4ae303a9a62550b30548a03d7299.jpg)

# Creating Curves

You can create curves in different ways.

# Creating Curves Automatically When Loading Files

When a PLT, TDR, or TIF file is loaded, Inspect does not create curves immediately in the plot area. This is because a curve might be formed from any pair of datasets belonging to different groups and only a few of these are likely to interest users. Curves must be created explicitly, when required, by mapping pairs of datasets to x-axes and y-axes.

<!-- page:30 -->
When a PLX or an XGRAPH file is loaded, Inspect creates curves automatically in the plot area, from the pairs of datasets defined in the loaded file, with the y-dataset being mapped to the left y-axis. The y-dataset can be remapped later to the right y-axis.

# Creating Curves Using Formulas

You can create curves by applying formulas to existing curves (see Using Formulas on page 35).

To create a curve using a formula:

1. In the Curves group box, click New.

The Create Curve dialog box is displayed.

![](images/inspect_ug_52829e6f3726712e2caeaf865bf241ac70d5b16b249bcb782bfc2c29b58896f8.jpg)

<details>
<summary>text_image</summary>

Create Curve
Curves
TotalCurrent_substrate
TotalCurrent_source
TotalCurrent_drain
Macros
ADD
VT
VT1
gm
Rout
Ron
IDSS
test1
testt2
Name: DiffCurve
Formula: <TotalCurrent_drain><TotalCurrent_source>
Map Curve To Left Y-Axis Right Y-Axis
available formula commands are:
acos, acosh, asin, asinh, atan, atanh, cbrt, ceil, cos, cosh, erf,
erfc, exp, fabs, floor, gamma, j0, j1, lgamma, log, log10, pow, sin,
sinh, sqrt, tan, tanh, y0, y1, diff, integr
vecmax, vecmin, vecvalx, vecvaly, tangent, veczero
Curve names in the formula must be surrounded by "<" and ">". If you are
using macros, CURVE must be replaced with the curve name and N with
a scalar value.
OK Apply Cancel
</details>

2. In the Curves pane, click a curve to highlight it.   
3. In the Name field, enter the name of the new curve.

Inspect provides a default.

4. In the Formula field, enter the formula to be used to create the curve.   
5. Map the curve to either the left y-axis or the right y-axis.

6. Click Apply.   
7. Click OK.

# Example: Creating a Curve That Is the Difference Between Two Curves

<!-- page:31 -->
To create a curve that is the difference between two curves:

1. In the Curves group box, click New.   
The Create Curve dialog box is displayed.   
2. In the Curves pane, click a curve to highlight it.   
The curve name appears in the Formula field enclosed by angle brackets.   
3. Type a hyphen after the closing angle bracket in the Formula field.   
4. Double-click a different curve in the Curves pane.

The name of the second curve appears in the Formula field.

5. Select the axis to which the new curve is mapped.

6. Click Apply.

7. Click OK.

The new curve is displayed in the plot area.

# Creating Curves Using Macros and Library Formulas

You can create and handle new curves using macros and library formulas included in Inspect. You can create macros using the Macro Editor, which allows you to select existing macro functions, different operations, and formulas from the libraries (see Figure 4 on page 20). For more information about using macros, see Using Macros on page 38.

Macros are stored in the file inspect\_macro.par in the STDB directory. This file is created automatically the first time Inspect is run. Initially, it stores predefined macros. You can then add or modify macros using the Macro Editor.

To open the Macro Editor:

■ Choose Edit > Define Macros.

![](images/inspect_ug_f7e60bc2633a375ee94efa2733ae400a299ce9b8d21ebff4f4aecaba27658e0e.jpg)

<details>
<summary>text_image</summary>

Macro Editor
Macro List
ADD
Name: ADD
VT
VT1
gm
Rout
Ron
IDSS
test1
testt2
Macro: <c 1> + <c 2>
available formula commands to create macros are:
acos, acosh, asin, asinh, atan, atanh, cbrt, ceil, cos, cosh, erf,
erfc, exp, fabs, floor, gamma, j0, j1, lgamma, log, log10, pow, sin,
sinh, sqrt, tan, tanh, y0, y1, diff, integr
vecmax, vecmin, vecvalx, vecvaly, tangent, veczero
Use "<c n>" as placeholders for curves and "<s n>" for scalar values
in the macros, where n represents the argument used in the macro (n
must start with 1).
Close
</details>

Figure 4 Macro Editor

<!-- page:32 -->
# Deleting Curves

You can delete either selected curves or all curves listed in the Curves group box.

To delete selected curves:

1. Select the curves in the Curves group box.   
2. Click Delete.   
3. Confirm the deletion.

To delete all curves:

1. Click Delete All.   
2. Confirm the deletion.

<!-- page:33 -->
This chapter describes how to modify the way in which Inspect displays loaded datasets.

# Modifying Axes

This section describes different ways you can modify the axes.

# Scaling an Axis

You can scale the x-axis, the left y-axis, and the right y-axis. The scale of each axis can be changed independently.

To change the scale of an axis:

1. Click the relevant toolbar button:

Click the $\exists z$ button to switch on logarithmic scale on the x-axis.   
Click the log $y$ button to switch on logarithmic scale on the left y-axis.   
• Click the $y _ { 2 }$ button to switch on logarithmic scale on the right y-axis.

2. Click the corresponding toolbar button again to switch off logarithmic scale for an axis.

When logarithmic scale is switched off, the axis reverts to linear scale.

# Handling Data When Axes Set to Logarithmic Scale

If an axis is set to logarithmic scale, Inspect handles data in the following way:

Negative values are set to positive.

Zero values are set to 1e-20.

When an axis switches to linear scale, data is restored to its original values.

# Limits of Axes Set to Logarithmic Scale

<!-- page:34 -->
When an axis is set to linear scale, you can set the minimum and maximum values of the axis.

When an axis is set to logarithmic scale, Inspect might be unable to set an axis to the given values. In this case, Inspect sets the minimum and maximum values of the axis to the nearest power of 10 values.

# Changing Attributes of Axes

To change the attributes of axes:

1. Choose Edit > Axes, or press Ctrl+A, or double-click any axis in the plot area.

The Axes dialog box is displayed (see Figure 5 on page 23).

2. Click the required tabs to change attributes.   
3. Click OK or Apply to accept the changes.

For example, to change the x-axis from linear scale to logarithmic scale:

1. Click the X-Axis tab.   
2. Click the Scale tab.   
3. Select Log.   
4. Click OK or Apply to accept the changes.

![](images/inspect_ug_f4e3d76ad9710f91c50483959d5cda2e010bf3d97d0f8966a93d893bbf61e346.jpg)

<details>
<summary>text_image</summary>

Axes
X-Axis Left Y-Axis Right Y-Axis
Patterns Scale Title Ticks
■ Display Left Y-Axis
□ Display Horizontal Line at Y=0
Width: 1
Color:
OK Apply Cancel
</details>

![](images/inspect_ug_197997237b0ffa7d56e9db2dad509c79186a5a3ab37b7a76423c54673063d0b3.jpg)

<details>
<summary>text_image</summary>

Axes
X-Axis Left Y-Axis Right Y-Axis
Patterns Scale Title Ticks
Min: 
Max: 
Scale: Lin Log
OK Apply Cancel
</details>

![](images/inspect_ug_44daf6317f9ff87d70b75344ab8325ca2f86573f950d65a1f020bcd114b962f3.jpg)

<details>
<summary>text_image</summary>

Axes
X-Axis	Left Y-Axis	Right Y-Axis
Patterns	Scale Victoria	Ticks
Title: This is a title
Color:
Font Selection
OK	Apply	Cancel
</details>

![](images/inspect_ug_f20434ab641ac2e0e116512dbb0dc7b5a141c265cb24f221fae23f961cd51335.jpg)

<details>
<summary>text_image</summary>

Axes
X-Axis Left Y-Axis Right Y-Axis
Patterns Scale Title Ticks
Tick Label Angle: 0
Subdivision: 5
Type: default
Precision: 6
Font Selection
OK Apply Cancel
</details>

Figure 5 Axes dialog box

<!-- page:36 -->
# Configuring the Plot Area

This section describes different ways you can modify the plot area.

# Changing Attributes of Plot Area

You can change the appearance of the plot area and modify attributes such as the name of the plot area, the legend text that references the displayed curves, the plot frame, and the grid.

To change the attributes of the plot area:

1. Choose Edit > Plot Area, or press Ctrl+G.   
The Plot Area dialog box is displayed (see Figure 6 on page 25).   
2. Click the required tabs to change attributes.   
3. Click OK or Apply to accept the changes.

For example, to change the position of the legend text in the plot area:

1. Click the Legend tab.   
2. In the Position box, select the new position.   
3. Click OK or Apply to accept the changes.

![](images/inspect_ug_55ebd74e3c4abf8f04f95c098346604174ec26efb0a29c7f1f5433b75db51d9c.jpg)

<details>
<summary>text_image</summary>

Plot Area
Title Legend General Grid
■ Title
This is the title
Font Selection
Justify: center
OK Apply Cancel
</details>

![](images/inspect_ug_02f79a0c46126bb25848cb66e9328f0d99136751c5b775135a1ad5e8b3187170.jpg)

<details>
<summary>text_image</summary>

Plot Area
Title Legend General Grid
Show Legend
Font Selection
Background Color:
Foreground Color:
Frame Color:
Frame Width: 1
Position: right
Anchor: n
OK Apply Cancel
</details>

![](images/inspect_ug_603aae315bdadc80cc4d8dac36a6e935641a4e20bac1c3404324f043a2a33bf1.jpg)

<details>
<summary>text_image</summary>

Plot Area
Title | Legend | General | Grid |
Show Frame
Axes Tight
Background Color:
Selection Color:
OK	Apply	Cancel
</details>

![](images/inspect_ug_fa2dcbfcfaa00a010352262d652966b688a204a1a81cd4ad3640f9907624e616.jpg)

<details>
<summary>text_image</summary>

Plot Area
Title | Legend | General | Grid |
Show Grid
Align: Left Right
Minor Ticks
Style: short dashed
Color:
Width: 1
OK Apply Cancel
</details>

Figure 6 Plot Area dialog box showing all tabs

<!-- page:38 -->
# Adding Labels

You can add labels to the plot area. These labels provide useful information about the mapped curves. Labels can be edited and removed from the plot area.

To add a label:

1. Choose Edit > Labels > Add.

The Labels dialog box is displayed.

![](images/inspect_ug_0c01fb5c5827e6226823a3ce5acb837ee42096ecde2772f0a35c5b9c734f21ce.jpg)

<details>
<summary>text_image</summary>

Labels
Text: Mas Slope
Foreground Color:
Font...
Background Fill:
Background Color:
OK	Apply	Cancel
</details>

2. In the Text field, type the label text.   
3. Select a color and font for the label.   
4. Click OK or Apply to insert the new label in the plot area.

To move a label:

1. Select a label in the plot area using the middle mouse button.   
2. Move the label inside the plot area as required and release the middle mouse button.

To delete a label:

1. Choose Edit > Labels > Remove.

The pointer changes to the delete mode.

2. In the plot area, click the label to be removed.

When the label is removed, the pointer reverts to the standard mode.

<!-- page:39 -->
# Displaying the Dataset of a Curve

Each curve displayed in the plot area has an associated dataset.

To view the points (data) included in the dataset of a specific curve:

1. Select a curve from the Curves group box.   
2. Choose Curve > Curve Data, or press Ctrl+D.

The Curve Data dialog box is displayed, which shows a table of the x-coordinates and y-coordinates for each point in the datasets represented by the selected curve (see Figure 7).

3. Highlight a data point in the table.

4. Click Delete to remove it from the displayed curve.

![](images/inspect_ug_b43ad951ecdb7440816f10186220a9345469e76b2dddc0f88046bafd7c21e700.jpg)

<details>
<summary>other</summary>

Curve Data
| n | x | y |
|---|---|---|
| 4 | 2 | 4.5 |
| 5 | 3 | 5 |
| 6 | 4 | 5.25 |
| 7 | 5 | 5.3 |
| 8 | 6 | 5.32 |
| 9 | 7 | 5.33 |
| 10 | 8 | 5.34 |
Delete Close
</details>

Figure 7 Curve Data dialog box

# Cleaning Up the Plot Area

You can clean up the plot area, in which case, all existing curves are deleted, the legend is removed, and the plot area is reinitialized.

To clean up the plot area:

Choose Edit > Clean Plot Area, or click the toolbar button.

<!-- page:40 -->
# Sampling Points in the Plot Area

To sample points in the plot area:

1. Choose Curve > Inspector.

The Inspector dialog box is displayed (see Figure 8).

2. In the plot area, select the first point by clicking a specific location (usually on a curve).   
3. Drag the pointer to a second location (usually on another curve) to mark the second point.

NOTE The Inspector dialog box works only for the x-axis and left y-axis.

Positions are represented by circles that are connected by a line. The Inspector dialog box shows different values calculated from the two selected positions.

![](images/inspect_ug_3a4517e4b69d791db9b549bb1fc511293c269bb36542e266e590ea37896512fb.jpg)

<details>
<summary>line</summary>

| Time (s) | TotalCurrent_source | TotalCurrent_drain |
|----------|---------------------|--------------------|
| 0        | 0.477376            | -2.4999e-12        |
| 0.5      | 0.000000            | 0                  |
| 1        | -8e-17              | 0                  |
</details>

Figure 8 Example of using Inspector dialog box to sample points in the plot area

<!-- page:41 -->
This chapter discusses curve interpolation and operations.

# Curve Operations

A curve is defined as a set of two or more (x, y) points. Each curve has its own set of points called datasets. Inspect can display the resulting (continuous) curve by plotting all data points and completing the curve with a graphical linear interpolation method. Figure 9 shows three different curves, each defined by different datasets.

![](images/inspect_ug_b1e40e145893dab8371b322137c8347a85350f66ba32333bb73f03fd93dbab53.jpg)

<details>
<summary>line</summary>

| x  | sum  | curve2 | curve1 |
|----|------|--------|--------|
| 0  | 0    | 0      | 0      |
| 10 | 30   | 20     | 15     |
| 20 | 80   | 45     | 35     |
| 30 | 150  | 90     | 60     |
| 40 | 200  | 130    | 80     |
| 50 | 250  | 170    | 100    |
| 60 | 300  | 200    | 120    |
| 70 | 350  | 230    | 140    |
| 80 | 400  | 260    | 160    |
| 90 | 450  | 290    | 180    |
| 100| 500  | 320    | 200    |
</details>

Figure 9 Different curves displayed as lines

Inspect offers different operations with curves. This requires an efficient way to handle curves and to create datasets for curves resulting from operations with other curves. Some operations result in a new curve or a scalar value. These operations include the sum of two or more curves, integration, differentiation, and the maximum value on the y-axis or the x-axis.

# Limitation of the X-Axis Values of the Dataset

<!-- page:42 -->
NOTE Only curve segments that have x-axis values monotonically increasing or decreasing can be used in a formula.

Curves used in a formula are checked for monotonically increasing or decreasing values inside the range defined by the current zoom level in the plot area. This means formulas apply only to the currently displayed points. By defining the optimal zoom level for the selected curves, it is possible to cut off curve segments that do not have monotonically increasing or decreasing x-values.

This general rule has one exception. An Inspect formula can involve only one curve with nonmonotonous x-axis values. In this case, Inspect splits this curve into monotonous segments of x-axis values, applies the formula to those segments, and builds the resulting curve automatically. For example, a scaling formula can be applied to a curve that is nonmonotonous on the x-axis. However, calculating the sum of two curves, where both curves are nonmonotonous on the x-axis, is not possible.

# More Than One Curve in a Formula

If a formula includes more than one curve, Inspect interpolates all curves to a common x-axis dataset. This is demonstrated in the following example.

The data points of curves A, B, and C are marked with circles, squares, and diamonds, respectively. The points in the resulting curve are marked with plus signs. The formula used is . The resulting curve includes points of all three input curves:   A + +   B   C

![](images/inspect_ug_8e4f7ea020ca0fab878448ad42d6d4f1f57c5adb11ec9e4e1a7239434baa016b.jpg)

<details>
<summary>line</summary>

| Curve     | Value |
| --------- | ----- |
| Curve A   | ●     |
| Curve A   | ●     |
| Curve A   | ●     |
| Curve A   | ●     |
| Curve A   | ●     |
| Curve B   | ■     |
| Curve B   | ■     |
| Curve B   | ■     |
| Curve C   | ◆     |
| Curve C   | ◆     |
| Curve C   | ◆     |
</details>

Inspect creates an array of all x-coordinates of all curves that are used in a formula and interpolates those curves to obtain y-values for each of the new x-values added to each curve.

# Handling Datasets in Formula Processing

<!-- page:43 -->
The following examples illustrate the dataset handling method that Inspect uses to work with more than one curve in a formula (see Figure 10).

![](images/inspect_ug_83db9009035c834396fb7d48449e927abaf385ab5ac6f2258c3f41e9b3c4218d.jpg)

<details>
<summary>line</summary>

| x    | Resulting Curve y = 2x² | Curve 2 y = x² (log) | Curve 1 y = x² (lin) |
| ---- | ------------------------ | --------------------- | --------------------- |
| 0    | 0                        | 0                     | 0                     |
| 10   | ~500                     | ~300                  | ~200                  |
| 20   | ~1500                    | ~800                  | ~600                  |
| 30   | ~3000                    | ~1500                 | ~1200                 |
| 40   | ~5000                    | ~2500                 | ~2000                 |
| 50   | ~7500                    | ~3500                 | ~3000                 |
| 60   | ~10000                   | ~4500                 | ~4000                 |
| 70   | ~12500                   | ~5500                 | ~5500                 |
| 80   | ~15000                   | ~6500                 | ~7000                 |
| 90   | ~17500                   | ~7500                 | ~8500                 |
| 100  | ~20000                   | ~8500                 | ~10000                |
</details>

Figure 10 Resulting plot showing curves

Curve 1: $\mathbf { y } = \mathbf { x } ^ { 2 }$ , linear scale on x

<table><tr><td>X</td><td>1</td><td>10</td><td>20</td><td>30</td><td>40</td><td>50</td><td>60</td><td>70</td></tr><tr><td>Y</td><td>1</td><td>100</td><td>400</td><td>900</td><td>1600</td><td>2500</td><td>3600</td><td>4900</td></tr></table>

Curve 2: $\mathbf { y } = \mathbf { x } ^ { 2 }$ , logarithmic scale on x

<table><tr><td>X</td><td>1</td><td>2</td><td>4</td><td>8</td><td>16</td><td>32</td><td>64</td></tr><tr><td>Y</td><td>2</td><td>4</td><td>16</td><td>64</td><td>256</td><td>1024</td><td>4096</td></tr></table>

<!-- page:44 -->
The combined set of x-coordinates needed to produce the resulting curve (the sum of both curves) is:

Resulting curve: $\mathbf { y } \ = \ 2 \mathbf { x } ^ { 2 }$

<table><tr><td>X</td><td>1</td><td>2</td><td>4</td><td>8</td><td>10</td><td>16</td><td>20</td><td>30</td><td>32</td><td>40</td><td>50</td><td>60</td><td>64</td></tr></table>

The last point of Curve 1 (x = 70) is not included because no data is available beyond x = 64 in Curve 2.

For y-values, interpolation is performed on Curve 1 and Curve 2 to fill the gaps and sum both curves. Therefore, y-values for this resulting curve are:

<table><tr><td>Y</td><td>2</td><td>8</td><td>32</td><td>128</td><td>200</td><td>512</td><td>800</td><td>1800</td><td>2048</td><td>3200</td><td>5000</td><td>7200</td><td>8192</td></tr></table>

# Dataset Created for Result Curves

For each curve created by a formula that involves more than one curve, Inspect generates a new dataset. During the Inspect session, this dataset is stored in a special project called AuxProject. When the current project is saved in a file, the AuxProject is also saved; otherwise, this project with all its datasets is lost when Inspect is closed.

The datasets in AuxProject are handled in the same way as datasets from loaded data files.

# Curve Handling on Interpolation

Inspect handles both linear-scaled and logarithmic-scaled curves. Each curve is treated independently. Therefore, when working with two curves, one with linear scale and the other with logarithmic scale, Inspect:

Creates new points for the first curve for all x-values of the second curve using a linear interpolation method.   
Creates new points for the second curve for all x-values of the first curve using a logarithmic interpolation method.   
Operates with the common set of points.

# Determining the Scale (Linear or Logarithmic) of Curves

<!-- page:45 -->
Deciding how to handle a curve involves analyzing its slope, which is defined as:

$$
\frac {d y}{d x} = \frac {y _ {i 1} - y _ {i}}{x _ {i 1} - x _ {i}} \tag {1}
$$

First, the curve is treated as linear, and the minimum (MinSlope) and maximum (MaxSlope) slopes are calculated.

Second, a quotient is created:

$$
\frac {\text { MaxSlope }}{\text { MinSlope }} \tag {2}
$$

The same calculation is performed by treating:

Τhe x-axis as logarithmically scaled.   
Τhe y-axis as logarithmically scaled.   
Both axes as logarithmically scaled.

Of these four values, the one closest to 1.0 indicates the best way of handling the curve.

<!-- page:46 -->
# 5: Curve Interpolation and Operations

Curve Handling on Interpolation

<!-- page:47 -->
This chapter describes how to use formulas and macros in Inspect.

# Using Formulas

Inspect recognizes two variable types: curve and scalar. Mixed curve–curve and curve–scalar operations are evaluated as follows:

1. The range of the result of a curve–curve operation is the intersection of the x-range of the operands.   
2. When one operand is a curve and the other is a scalar, the respective operation is performed as a scalar operation on each element of the curve operand.

The binary operators that can be used are +, –, \*, /, and ^ (power operator).

# Formula Library

The formula library allows you to perform some basic calculations on one or more curves. The result can be a new curve or a scalar value (see Table 3 on page 36). The following examples show how the formula library is used:

```txt
sin (<curve_1> + 10) The result is a new curve. Inspect adds 10 to the y-value of each curve point from curve_1 and computes the sinus. 
```

```txt
maxslope(<curve_1>) The result is a scalar value, which is the maximum slope of curve_1. 
```

Table 3 on page 36 lists functions that create a new curve by applying a mathematical transformation to each element of the curve. These functions can also be applied to scalar values. Table 4 on page 37 lists special functions that either require more than one parameter or do not return a curve. Table 5 on page 37 lists functions that manage or compute fast Fourier transformation (FFT) and related operations.

NOTE A curve can be defined by one point only, in which case, the curve is treated as a scalar input. Some curves require as input a curve only, that is, a curve that has at least two points.

Table 3 Standard mathematical functions 

<table><tr><td>Function</td><td>Input type</td><td>Output type</td><td>Description</td></tr><tr><td>acos</td><td>curve</td><td>curve</td><td>Returns the arc cosine. The returned angle [radian] is given in the range 0 (zero) to π.</td></tr><tr><td>acosh</td><td>curve</td><td>curve</td><td>Returns the inverse hyperbolic cosine. Curve values must be greater than or equal to 1.</td></tr><tr><td>asin</td><td>curve</td><td>curve</td><td>Returns the arc sine. The returned angle [radian] is given in the range from -π/2 to π/2.</td></tr><tr><td>asinh</td><td>curve</td><td>curve</td><td>Returns the inverse hyperbolic sine.</td></tr><tr><td>atan</td><td>curve</td><td>curve</td><td>Returns the arc tangent. The returned angle [radian] is given in the range from -π/2 to π/2.</td></tr><tr><td>atanh</td><td>curve</td><td>curve</td><td>Returns the inverse hyperbolic tangent. Curve values must be between -1 and 1 (excluding -1 and 1).</td></tr><tr><td>cbrt</td><td>curve</td><td>curve</td><td>Returns the cube root.</td></tr><tr><td>ceil</td><td>curve</td><td>curve</td><td>Rounds up each element to the smallest integer not less than itself.</td></tr><tr><td>cos</td><td>curve</td><td>curve</td><td>Returns the cosine.</td></tr><tr><td>cosh</td><td>curve</td><td>curve</td><td>Returns the hyperbolic cosine.</td></tr><tr><td>diff</td><td>curve only</td><td>curve</td><td>Returns the first derivative of the curve.</td></tr><tr><td>erf</td><td>curve</td><td>curve</td><td>Returns an error function of the curve values.</td></tr><tr><td>erfc</td><td>curve</td><td>curve</td><td>Returns the complementary error function of the curve values.</td></tr><tr><td>exp</td><td>curve</td><td>curve</td><td>Returns the number raised to the power of each curve value.</td></tr><tr><td>fabs</td><td>curve</td><td>curve</td><td>Returns the absolute value.</td></tr><tr><td>floor</td><td>curve</td><td>curve</td><td>Rounds down each element to the largest integer not greater than itself.</td></tr><tr><td>gamma</td><td>curve</td><td>curve</td><td>Returns the Gamma function.</td></tr><tr><td>integr</td><td>curve only</td><td>curve</td><td>Returns the integral of the curve.</td></tr><tr><td>j0</td><td>curve</td><td>curve</td><td>Returns the Bessel function of the first kind of order 0.</td></tr><tr><td>j1</td><td>curve</td><td>curve</td><td>Returns the Bessel function of the first kind of order 1.</td></tr><tr><td>lgamma</td><td>curve</td><td>curve</td><td>Returns the natural logarithm of the absolute value of the Gamma function.</td></tr><tr><td>log</td><td>curve</td><td>curve</td><td>Returns the natural logarithm of the given curve.</td></tr><tr><td>log10</td><td>curve</td><td>curve</td><td>Returns the base 10 logarithm of the given curve.</td></tr></table>

Table 3 Standard mathematical functions 

<table><tr><td>Function</td><td>Input type</td><td>Output type</td><td>Description</td></tr><tr><td>sin</td><td>curve</td><td>curve</td><td>Returns the sine.</td></tr><tr><td>sinh</td><td>curve</td><td>curve</td><td>Returns the hyperbolic sine.</td></tr><tr><td>sqrt</td><td>curve</td><td>curve</td><td>Returns the square root.</td></tr><tr><td>tan</td><td>curve</td><td>curve</td><td>Returns the tangent.</td></tr><tr><td>tanh</td><td>curve</td><td>curve</td><td>Returns the hyperbolic tangent.</td></tr><tr><td>y0</td><td>curve</td><td>curve</td><td>Returns the Bessel function of the second kind of order 0.</td></tr><tr><td>y1</td><td>curve</td><td>curve</td><td>Returns the Bessel function of the second kind of order 1.</td></tr></table>

Table 4 Special functions 

<table><tr><td>Function</td><td>Input type</td><td>Output type</td><td>Description</td></tr><tr><td>pow</td><td>curve, scalar</td><td>curve</td><td>Returns the curve raised to the power of the given scalar.</td></tr><tr><td>tangent</td><td>curve, scalar</td><td>curve</td><td>Returns a curve that is tangent to the given curve, at the given x-value.</td></tr><tr><td>vecmax</td><td>curve</td><td>scalar</td><td>Maximum y-value.</td></tr><tr><td>vecmin</td><td>curve</td><td>scalar</td><td>Minimum y-value.</td></tr><tr><td>vecvalx</td><td>curve, scalar</td><td>scalar</td><td>The x-value at a given y.</td></tr><tr><td>vecvaly</td><td>curve, scalar</td><td>scalar</td><td>The y-value at a given x.</td></tr><tr><td>veczero</td><td>curve</td><td>scalar</td><td>The x-value at y = 0.</td></tr></table>

Table 5 Fast Fourier transformation (FFT) and related functions 

<table><tr><td>Function</td><td>Input type</td><td>Output type</td><td>Description</td></tr><tr><td>cffim</td><td>curve_real, curve_imaginary</td><td>curve</td><td>Returns the imaginary part of the FFT of the given complex curve.</td></tr><tr><td>cfftre</td><td>curve_real, curve_imaginary</td><td>curve</td><td>Returns the real part of the FFT of the given complex curve.</td></tr><tr><td>cifftim</td><td>curve_real, curve_imaginary</td><td>curve</td><td>Returns the imaginary part of the inverse FFT of the given complex curve.</td></tr><tr><td>cifftre</td><td>curve_real, curve_imaginary</td><td>curve</td><td>Returns the real part of the inverse FFT of the given complex curve.</td></tr><tr><td>fftabs</td><td>curve_real, curve_imaginary</td><td>curve</td><td>Returns a vector holding the absolute value of the given complex curve.</td></tr><tr><td>fftim</td><td>curve</td><td>curve</td><td>Returns the imaginary part of the FFT of the given curve.</td></tr><tr><td>fftre</td><td>curve</td><td>curve</td><td>Returns the real part of the FFT of the given curve.</td></tr></table>

Table 5 Fast Fourier transformation (FFT) and related functions 

<table><tr><td>Function</td><td>Input type</td><td>Output type</td><td>Description</td></tr><tr><td>ifftim</td><td>curve</td><td>curve</td><td>Returns the imaginary part of the inverse FFT of the given curve.</td></tr><tr><td>ifftre</td><td>curve</td><td>curve</td><td>Returns the real part of the inverse FFT of the given curve.</td></tr></table>

<!-- page:50 -->
# Using Macros

Macros can define complex formulas. Inspect expands a macro by using the actual arguments specified in the call to the macro (see Figure 4 on page 20).

In a macro definition, the argument type must be specified. Types can be curve or scalar. This information is needed to expand the macro into the correct formula.

The syntax for argument placeholder specification is <c n> for curves and <s n> for scalars, where n is an integer value used to distinguish between different arguments; n must start with 1.

In the Inspect macro parser, the macro prototype is not specified explicitly. It is determined automatically from the formula that defines the macro. The order of arguments is determined by their first appearance in the formula and not by numbers in the argument placeholders.

# Example: ADD Macro

The macro ADD is defined as:

```txt
<c 1> + <c 2> 
```

This macro adds two curves. The macro prototype looks like:

```txt
ADD (<CURVE>, <CURVE>) 
```

The argument placeholder <CURVE> must be replaced by an actual curve name.

<!-- page:51 -->
# Example: DIFFMULT Macro

The macro DIFFMULT is defined as:

$$
\text { diff } (<   \text { c } 1 >) + (<   \text { s } 3 > * <   \text { c } 2 >)
$$

This macro takes the derivative of a curve <c 1> and adds to it a curve <c 2> multiplied by a scalar <s 3>. A call to this macro has the form:

$$
\text { DIFFMULT } (<   \text { CURVE } >, \text { S }, <   \text { CURVE } >)
$$

The argument placeholder <CURVE> must be replaced by an actual curve name, and S must be replaced by an expression that generates a scalar value.

<!-- page:52 -->
6: Formulas and Macros

Using Macros

<!-- page:53 -->
This chapter describes the operations available using the scripting language of Inspect.

# Overview of the Scripting Language

In addition to the user interface, you can control Inspect using a scripting language (see Working With Scripts on page 9). The scripting language allows you to manipulate and display data without using the user interface, and it is very useful for running complex calculations on datasets and displaying results, for example:

■ Repeated manual actions can be recorded and run later by simple script invocation.   
■ Several computations using the formula library can be performed in one run.   
Results can be written automatically to a file.

You can write a script manually or create a script by recording actions performed in the user interface (see Creating Scripts on page 9).

Inspect uses the tool command language (Tcl) as its scripting language. For more information about Tcl, go to http://www.tcl.tk.

Some commands have been added to Tcl (in the form of Tcl procedures) to perform application-specific actions. For more specific needs, you can create your own commands.

Most of the additional commands in Inspect return a status string. A return status not equal to 1 indicates an error. If an error occurs, Inspect prints an error message to the standard error output and terminates the execution of the script.

NOTE Arguments in braces are optional. The first term in the braces is the name of the argument, and the second term is the default value of the argument. For example, a command that has been defined as command {arg def\_value} can be called as command (which is equivalent to command def\_value) and also as command other\_value.

<!-- page:54 -->
# General-Purpose Commands

# ft\_scalar

ft\_scalar variableName variableValue

Action: Produces the following output line:

DOE: variableName variableValue

If the current Inspect command file belongs to a Sentaurus Workbench project, this output line results in the creation of a new Sentaurus Workbench extracted variable with the name variableName and the value variableValue (see Sentaurus™ Workbench User Guide, Extracted Variables on page 135).

Input: variableName, name of the Sentaurus Workbench variable to extract variableValue, value of this Sentaurus Workbench variable

Returns: None

# Reading and Writing Files

# cv\_write

cv\_write type fileName curveList

Action: Writes (exports) the data of the specified curves to a file in the specified format.

Input: type, output format to use: plt, xgraph, or xmgr fileName, file to write curveList, list of curve names

Returns: Status of the write operation

<!-- page:55 -->
# fi\_writeBitmap

fi\_writeBitmap fileName

Action: Writes the plot area to a PNG file.

Input: fileName, file to write

Returns: Status of the write operation

# fi\_writeEps

fi\_writeEps fileName {orientation portrait} {height ""} {width ""}

Action: Writes the plot area to an EPS file. This command is not generated automatically when script recording is switched on. If height or width is not specified, the actual plot size is taken into account. Some examples are:

```txt
fi_writeEps test.eps
fi_writeEps test.eps landscape
fi_writeEps test.eps landscape 200 100 
```

Input: fileName, file to write orientation, image orientation: portrait (default) or landscape height, height of the saved image in pixels width, width of the saved image in pixels

Returns: Status of the write operation

<!-- page:56 -->
# fi\_writePs

```txt
fi_writePs fileName {orientation portrait} {printSize US_LETTER} {height ""} {width ""} {offsetHeight ""} {offsetWidth ""} {sizeUnit ""} 
```

```txt
Action: Writes the plot area to a PostScript® file. This command is not generated automatically when script recording is switched on. When height or width is not specified, the actual plot size is taken into account. Some examples are:
fi_writePs test.ps
fi_writePs test.ps landscape
fi_writePs test.ps landscape DIN_A4
fi_writePs test.ps portrait US_LETTER 450 300 5 5 m 
```

```txt
Input: fileName, file to write orientation, image orientation: portrait (default) or landscape printSize, page size: US_LETTER (default), DIN_A3, or DIN_A4 height, height of the saved image in size units (sizeUnit) width, width of the saved image in size units (sizeUnit) offsetHeight, vertical page offset in size units (sizeUnit) offsetWidth, horizontal page offset in size units (sizeUnit) sizeUnit, unit for height, width, offsetHeight, and offsetWidth: i: inch (default) m: millimeter c: centimeter 
```  
Returns: Status of the write operation

# graph\_load

```txt
graph_load fileName 
```

Action: Loads the specified save file into Inspect. All currently loaded projects are deleted.

Input: fileName, name of file to load

Returns: Status of the load operation

<!-- page:57 -->
# graph\_write

graph\_write fileName

Action: Saves the current state to a specified file.

Input: fileName, name of file

Returns: Status of the write operation

# param\_load

param\_load fileName

Action: Loads a parameter file.

Input: fileName, name of file to load

Returns: Status of the load operation

# param\_write

param\_write fileName

Action: Saves a parameter file.

Input: fileName, name of file

Returns: Status of the write operation

<!-- page:58 -->
# proj\_getDataSet

```txt
proj_getDataSet projectName dataSetId 
```

Action: If no dataset is found, the return value is an empty list. For example, the following commands set the variable x\_data to the values of the dataset time and the variable y\_data to the values of the dataset data\_1 of node\_A:

```tcl
set x_data [proj_getDataSet "tutorial_ins" "time"]
set y_data [proj_getDataSet "tutorial_ins" "node_A data_1"] 
```

Input: projectName, name of project dataSetId, name of a dataset including its group name if applicable

Returns: List of all the values of the dataset

# proj\_getList

```txt
proj_getList 
```

Action: Returns a list of all projects. If no projects are found, an empty list is returned.

Input: None

Returns: List of all loaded projects

# proj\_getNodeList

```txt
proj_getNodeList projectName 
```

Action: Returns a list of group names of the given project. If no groups have been found, an empty list is returned.

Input: projectName, name of project

Returns: List of group names

<!-- page:59 -->
# proj\_load

```txt
proj_load fileName 
```

Action: Loads a data file and creates a new project. The base name of the file is used as the project name (see Data Formats on page 4).

Input: fileName, name of file

Returns: Status of the load operation

# proj\_unload

```csv
proj_unload projectName 
```

Action: Deletes a project and all the project-related curves.

Input: projectName, name of project

Returns: Status of the delete operation

# proj\_write

```txt
proj_write projectName fileName 
```

Action: Writes a project to a specified file.

Input: projectName, name of project fileName, name of file

Returns: Status of the write operation

# Creating, Displaying, and Deleting Curves

<!-- page:60 -->
A dataset used for curve creation is identified by its data path, which consists of the project name, the group name when the dataset belongs to a group, and the dataset name.

# cv\_create

```txt
cv_create curveName xDataPath yDataPath {axis y}
```

```txt
Action: Creates a curve with the given name using the specified datasets without displaying it. The datasets must be already loaded; otherwise, an error is returned. For example, the following command creates a curve mycurve using the dataset time on the x-axis and the dataset OuterVoltage of the group Gate on the y-axis, with both datasets belonging to the project nmos_n7_des:
cv_create mycurve "nmos_n7_des time" "nmos_n7_des Gate OuterVoltage" 
```

```txt
Input: curveName, unique name for the new curve xDataPath, x-dataset data path yDataPath, y-dataset data path axis, axis to use; the default is y 
```

```txt
Returns: Status of the create operation 
```

# cv\_createDS

```txt
cv_createDS curveName xDataPath yDataPath {axis y}
```

Same as cv\_create except that the curve is displayed. See cv\_create.

<!-- page:61 -->
# cv\_createFromScript

```txt
cv_createFromScript CurveName xdata ydata {axis y} 
```

Action: Creates a curve using the given name and data. If the number of values for x and y are not the same, the number of curve points is according to that of the smaller dataset. Curves created with this command are stored in AuxProject. For example, the following command creates the curve mycurve defined by the specified data:

```txt
cv_createFromScript mycurve "0 1 2 3 4 5 6 7 8 9" "1 2 1 2 1 2 1 2 1 2" 
```

Input: curveName, unique name for the new curve xdata, list of data to use for the x-dataset ydata, list of data to use for the y-dataset axis, axis to use: y (default) or y2

Returns: Status of the create operation

# cv\_createWithFormula

```txt
cv_createWithFormula curveName formula xmin xmax ymin ymax 
```

Action: Computes a new curve using the formula applied to the data of the argument curves within the given range. Setting the range to any nonnumeric value (for example, A) instructs Inspect to set no limit in the corresponding direction. For example, the following command creates the curve f3 using the entire data range of curves f1 and f2:

```txt
cv_createWithFormula f3 "<f1>+<f2>+10" A A A A 
```

Input: curveName, unique name for the new curve formula, formula or macro xmin, xmax, ymin, ymax, range for which the formula is applied

Returns: Status of the create operation

<!-- page:62 -->
# cv\_delete

cv\_delete curveName

Action: Deletes a curve.

Input: curveName, name of curve

Returns: Status of the delete operation

# cv\_display

cv\_display curveName {axis y}

Action: Displays a curve using the specified y-axis.

Input: curveName, name of curve to display axis, axis to use; the default is y

Returns: None

# cv\_logScale, cv\_log10Scale

cv\_logScale curveName newCurveName {axis x} cv\_log10Scale curveName newCurveName {axis x}

Action: Creates a new curve where all values on a given axis are transformed to a log (log10) scale.

Input: curveName, curve to transform newCurveName, name of the new curve axis, axis on which the curve is scaled; the default is x

Returns: Status of the create operation

<!-- page:63 -->
# cv\_split

cv\_split curveName axis newCurveList

Action: Splits the input curve into several curves at the points where the x-values are nonmonotonic, that is, . The number of names for the new curvesx i 1 [ ] + < x i[ ] must match the actual number of created curves; otherwise, an error is returned.

This command is similar to choosing Curve > Transform > Suppress Backtrace (see Table 10 on page 113). The difference is that this command creates a set of new curves. With Suppress Backtrace selected, the backtrace lines are suppressed only on the plot.

Input: curveName, name of curve to split axis, y-axis to map the new curves onto newCurveList, list of names for new curves

Returns: Status of the operation

# cv\_split\_disc

cv\_split\_disc curveName axis newCurveList

Action: Splits the input curve into several curves at the points where there are discontinuities, that is, and . The number ofx i 1 [ ] + ==x i[ ] y i 1 [ ] + != y i[ ] names for the new curves must match the actual number of created curves; otherwise, an error is returned.

Input: curveName, curve to split axis, y-axis to map the new curves onto newCurveList, list of names for new curves

Returns: Status of the operation

<!-- page:64 -->
# Changing Attributes

These commands change the attributes of the title, axes, curves, and legend.

# cv\_lineColor

cv\_lineColor curveName color

Action: Sets the color of the curve line.

Input: curveName, name of curve color, color of the curve line

Returns: None

# cv\_lineStyle

cv\_lineStyle curveName style

Action: Sets the drawing style of the curve line.

Input: curveName, name of curve style, drawing style of the curve line: dashed, dotted, "long dashed", "long dotted", or solid

Returns: None

# cv\_renameCurve

cv\_renameCurve curveName newName

Action: Renames a curve.

Input: curveName, name of curve newName, new name of curve

Returns: None

<!-- page:65 -->
# cv\_set\_interpol

cv\_set\_interpol curveId axis type

Action: Sets the interpolation method to be applied to each particular dataset of a curve.

Input: curveId, curve identification axis, axis on which the interpolation is set: X or Y type, interpolation method to set: AUTO, LIN, or LOG

Returns: None

# cv\_setCurveAttr

cv\_setCurveAttr curveName legend color style width shape size outColor outWidth fillColor

Action: Sets curve-drawing attributes.

Input: curveName, name of curve legend, curve legend color, color of the curve line style, drawing style of the curve line: dashed, dotted, "long dashed", "long dotted", or solid width, width of the curve line shape, marker shape: none, circle, cross, diamond, plus, scross, splus, square, or triangle size, marker size outColor, color of the marker outline outWidth, width of the marker outline fillColor, fill color of the marker

Returns: None

<!-- page:66 -->
# gb\_setpreferences

```txt
gb_setpreferences type val 
```

Action: Sets new values for the preference options. The following options can be modified:

precision: Defines the precision used to display coordinate values in the status line; any integer can be set.

old\_interpolation: Specifies whether the old interpolation is used to compute curves:

1: Activates old interpolation.

0: Deactivates old interpolation.

Input: type, preference option to be modified val, new value for option

Returns: None

# gr\_createLabel

gr\_createLabel label coordX coordY fontStr color

Action: Creates a label in the plot area.

Input: label, label text coordX, x-coordinate coordY, y-coordinate fontStr, label font color, label color

Returns: Label ID

# gr\_deleteLabel

```txt
gr_deleteLabel labelId 
```

Action: Deletes a label from the plot area.

Input: labelId, label ID

Returns: None

<!-- page:67 -->
# gr\_formatAxis

gr\_formatAxis axis format

Action: Changes the format of the displayed axis.

Input: axis, axis to be formatted format, the options are default, engineering, fixed, or scientific

Returns: None

# gr\_mappedAxis

gr\_mappedAxis axis yesno

Action: Changes the visibility of an axis.

Input: axis, specifies a y-axis: y or y2 yesno, specifies the axis visibility: True or False

Returns: None

# gr\_precision

gr\_precision axis prec

Action: Changes the precision of a given axis.

Input: axis, axis to be formatted prec, numeric precision to be set for the axis

Returns: None

<!-- page:68 -->
# gr\_setAxisAttr

gr\_setAxisAttr axis title tfont min max color width font angle div scale {tcolor}

Action: Sets the axis attributes.

```csv
Input: axis, specifies an axis: X, Y, or Y2
title, axis title
tfont, font size of the axis title
min, max, minimum and maximum values of the axis
color, color of the axis
width, width of the axis line
font, font size of the tick label
angle, angle at which the tick labels are drawn
div, number of secondary ticks between the main ticks
scale, specifies linear (lin) or logarithmic (log) display of the axis
tcolor, color of the axis title 
```

Returns: None

# gr\_setGeneralAttr

gr\_setGeneralAttr {showFrame true} {axesTight true} {backColor white} {selectColor cyan}

Action: Sets the general attributes of the plot.

Input: showFrame, Boolean indicator of plot frame appearance; default is true axesTight, Boolean indicator of the tightness of axes; default is true backColor, plot background color; default is white selectColor, color of the selected curve; default is cyan

Returns: None

gr\_setGridAttr   
```txt
gr_setGridAttr {showGrid false} {gridAlign left} {minorTicks false} {gridStyle "short dashed"} {gridColor black} {gridWidth 1} 
```  
Action: Sets the grid attributes of the plot.

```txt
Input: showGrid, Boolean indicator of grid appearance; default is false
gridAlign, grid alignment: left (default) or right
minorTicks, Boolean indicator of the appearance of minor ticks; default is false
gridStyle, attribute of the grid style: dashed, "dot-dashed", dotted, "long dashed", "long dotted", "short dashed" (default), or solid
gridColor, color of the grid lines; default is black
gridWidth, thickness of the grid lines; default is 1 
```  
Returns: None

gr\_setLegendAttr   
```tcl
gr_setLegendAttr {showFlag true} {fontName helvetica} {fontSize 10} {fontStyle {} } {backColor white} {foreColor black} {frameColor black} {frameWidth 1} {framePos right} {frameAnchor n} 
```  
Action: Sets the attributes of the legend.

```csv
Input: showFlag, Boolean indicator of legend appearance
fontName, legend font name; default is helvetica
fontSize, legend font size; default is 10
fontStyle, legend font style: bold, italic, overstrike, or underline;
default is an empty list {}
backColor, legend background color; default is white
foreColor, legend foreground color; default is black
frameColor, legend frame color; default is black
frameWidth, legend frame width; default is 1
framePos, legend frame position: left, right (default), top, bottom, free, or plot
frameAnchor, legend frame anchor: n (default), e, s, w, ne, se, sw, or nw 
```  
Returns: None

<!-- page:70 -->
# gr\_setLegendPos

```txt
gr_setLegendPos x y 
```

Action: Changes the position of the displayed legend in the plot area.

Input: x, new x-coordinate for the legend in the plot area y, new y-coordinate for the legend in the plot area

Returns: None

# gr\_setTitleAttr

```tcl
gr_setTitleAttr title {fontSize 14} {just center} 
```

Action: Sets the title attributes.

Input: title, title text fontSize, size of title font; default is 14 just, title justification: center (default), left, or right

Returns: None

# Accessing Curve Data

# cv\_getVals

```txt
cv_getVals curveName 
```

Action: Returns a list of the x- and y-data. The x-data and y-data can be assessed using:

```tcl
set xy [cv_getVals "f1"]
set x [lindex $xy 0]
set y [lindex $xy 1] 
```

After this, the variables x and y hold the x- and y-datasets, respectively.

Input: curveName, name of curve

Returns: List of the x- and y-data

<!-- page:71 -->
# cv\_getValsX

cv\_getValsX curveName

Action: Returns a list that holds the x-dataset.

Input: curveName, name of curve

Returns: List of the x-data

# cv\_getValsY

cv\_getValsY curveName

Action: Returns a list that holds the y-dataset.

Input: curveName, name of curve

Returns: List of the y-data

# cv\_getXaxis

cv\_getXaxis curveName

Action: Returns the project name and the dataset ID using:

```tcl
set answer [cv_getXaxis "myCurve"]
set projectName [lindex $answer 0]
set dataSetId [lindex $answer 1] 
```

Input: curveName, name of curve

Returns: List with the project name and the dataset ID of the x-dataset

<!-- page:72 -->
# cv\_getYaxis

```txt
cv_getYaxis curveName 
```

Action: Returns the project name and the dataset ID as for cv\_getXaxis. See cv\_getXaxis.

Input: curveName, name of curve

Returns: List with the project name and the dataset ID of the y-dataset

# cv\_printVals

```txt
cv_printVals curveName 
```

Action: Writes the x- and y-data of a curve to standard output.

Input: curveName, name of curve

Returns: List of the printed values

# Transforming Curve Data

These commands change the way in which curve data is displayed without changing the curve datasets.

# cv\_abs

```txt
cv_abs curveName axis 
```

Action: Replaces negative values of the x- or y-dataset by their absolute values, depending on the axis argument. This command has the same effect as choosing Curve > Transform > Abs X or Abs Y (see Table 10 on page 113).

Input: curveName, name of curve axis, axis specifier

Returns: Status of the operation

<!-- page:73 -->
# cv\_delPts

cv\_delPts curveName indexList

Action: Deletes the points in the indexList from the set of points being displayed.

Input: curveName, name of curve indexList, list of indices of curve points

Returns: Status of the delete operation

# cv\_inv

cv\_inv curveName axis

Action: Reflects a curve about the specified axis. This command is equivalent to choosing Curve > Transform > Reflect X or Reflect Y (see Table 10 on page 113).

Input: curveName, name of curve axis, axis specifier

Returns: Status of the operation

# cv\_reset

cv\_reset curveName

Action: Restores the original appearance of the curve after a transformation. This command is equivalent to choosing Curve > Restore Data (see Table 10 on page 113).

Input: curveName, name of curve

Returns: Status of the operation

<!-- page:74 -->
# Extracting Parameters

These commands extract standard parameters of semiconductor devices. Some arguments of the commands have default values that are used when an argument is not specified.

# f\_Gamma

```txt
f_Gamma VT1 VT2 VB1 VB2 const 
```

Action: Computes the body-effect parameter at two different source–substrate voltages. The formula used to compute the body-effect parameter is: $\text{Gamma} = (\text{VT2} - \text{VT1}) / ((\text{const} + \text{VB2})^{1/2} - (\text{const} + \text{VB1})^{1/2})$

Input: VT1, VT2, two threshold voltages
VB1, VB2, two different source–substrate voltages
const, $2\varphi_{F}$ where $\varphi_{F}$ is the Fermi-level potential; default value is 0.8 V

Returns: Gamma $[V^{1/2}]$ as a scalar or f_error in the case of an error

# f\_gm

```txt
f_gm curveName xmin xmax ymin ymax 
```

Action: Computes the maximum of transconductance for a given $I_{d}-V_{g}$ curve.

```txt
Input: curveName, curve used to calculate gm
xmin, xmax, ymin, ymax, range for computing the result; the default values correspond to the full curve range 
```

```txt
Returns: Value of gm [A/V] of the curve or f_error in the case of an error 
```

# f\_hideInternalCurves

```txt
f_hideInternalCurves 
```

```txt
Action: Hides the internally used curves created by the commands of this section. See f_showInternalCurves on page 64. 
```

```txt
Input: None 
```

```txt
Returns: None 
```

<!-- page:75 -->
# f\_IDSS

f\_IDSS curveName xmin xmax ymin ymax

Action: Computes the saturation current.

Input: curveName, $\mathrm { I _ { d } - V _ { d } }$ curve at the fixed gate–source voltage xmin, xmax, ymin, ymax, range for computing the result; the default values correspond to the full curve range

Returns: Saturation current value or f\_error in the case of an error

# f\_KP

f\_KP gm VDS

Action: Computes the transconductance parameter.

Input: gm, transconductance value VDS, drain source voltage; default is 0.1

Returns: KP $[ \mathrm { A } / \mathrm { V } ^ { 2 } ]$ value or f\_error in the case of an error

# f\_Ron

f\_Ron curveName xmin xmax ymin ymax

Action: Computes the on-state resistance in the linear region.

Input: curveName, $\mathrm { I _ { d } - V _ { d } }$ curve at the fixed gate–source voltage xmi $^ { n , }$ xmax, ymin, ymax, range for computing the result; the default values correspond to the full curve range

Returns: Value of $\mathrm { R } _ { \mathrm { o n } } \left[ \mathrm { k } \Omega \right]$ or f\_error in the case of an error

<!-- page:76 -->
# f\_Rout

f\_Rout curveName xmin xmax ymin ymax

Action: Computes the output resistance in the saturation region.

Input: curveName, $\mathrm { I _ { d } - V _ { d } }$ curve at the fixed gate–source voltage xmin, xmax, ymin, ymax, range for computing the result; the default values correspond to the full curve range

Returns: Value of $\mathbf { R } _ { \mathrm { o u t } } \left[ \mathrm { k } \Omega \right] \mathrm { o r } \mathtt { E } _ { - }$ \_error in the case of an error

# f\_showInternalCurves

f\_showInternalCurves axis

Action: Displays the internally used curves created by the commands of this section. See f\_hideInternalCurves on page 62.

Input: axis, axis to use; default is left

Returns: None

# f\_TetaG

f\_TetaG VT gm idvgs vgsvgs xmin xmax ymin ymax

Action: Computes the mobility modulation TetaG using the formula: TetaG = gm(VGSlow)/ID(VGShigh) - 1/(VGShigh - VT)

Input: VT, threshold voltage value ${ \mathfrak { g m } } ,$ transconductance value idvgs, $\mathrm { I _ { d } { - } V _ { g } }$ curve vgsvgs, Vg–Vg $\mathrm { V _ { g } - V _ { g } }$ curve xmin, xmax, ymin, ymax, range for computing the result; the default values correspond to the full curve range

Returns: Value of TetaG $[ \mathsf { V } ^ { - 1 } ]$ or f\_error in the case of an error

<!-- page:77 -->
# f\_VT

f\_VT curveName xmin xmax ymin ymax   
Action: Computes the threshold voltage [V] of the given curve. The formula used to compute the threshold voltage is:
    VT = intercept (maxslope(curve))

Example 1: This statement computes V $_{th}$ using default values for the range:
    set vt1 [f_VT idvgs]

Example 2: This statement computes V $_{th}$ using xmin = 0.1 xmax = 0.3 and default values for the y-range:
    set vt2 [f_VT idvgs 0.1 0.3]

Input: curveName, name of curve
xmin, xmax, ymin, ymax, range for computing the result; the default values correspond to the full curve range

Returns: Threshold voltage value or f_error in the case of an error

# f\_VT1

f\_VT1 curveName xmin xmax ymin ymax   
Action: Computes the threshold voltage [V] of the given curve. $V_{th}$ is typically extracted at $I_d = 0.1 \mu A/\mu m$ .  
Input: curveName, name of curve  
xmin, xmax, ymin, ymax, range for computing the result; the default values correspond to the full curve range  
Returns: Threshold voltage value or f_error in the case of an error

<!-- page:78 -->
# f\_VT2

f\_VT2 curveName

Action: Computes the threshold voltage [V] of the given curve. The method used to extract $\mathrm { V _ { t h } }$ is the intersection of MaxSlope and MinSlope lines in the log of the given curve.

Input: curveName, name of curve

Returns: Threshold voltage as a scalar value or f\_error in the case of an error

# Computing

# cv\_compute

cv\_compute formula xmin xmax ymin ymax

Action: Computes a scalar value using the formula.

Input: formula, string with the formula to evaluate xmin, xmax, ymin, ymax, range for which the formula is applied

Returns: Scalar computation result

# cv\_getZero

cv\_getZero curveName xmin xmax ymin ymax

Action: Computes the x-coordinate of the point where the curve intersects the x-axis. If the curve does not cross the x-axis, an empty string is returned.

Input: curveName, name of curve xmin, xmax, ymin, ymax, range for which the command applies

Returns: The x-value where the curve intersects the x-axis

<!-- page:79 -->
# macro\_define

macro\_define macroName macroDef

Action: Defines a macro, which can be used later for computations.

Input: macroName, name of the macro macroDef, macro definition

Returns: Status of the operation

# Controlling Scripts

# script\_break

script\_break

Action: Suspends the execution of a script and passes control to the user interface. The script execution can be resumed by choosing Script > Continue Script (see Table 11 on page 114).

Input: None

Returns: None

# script\_exit

script\_exit

Action: Stops the execution of a script and exits Inspect.

Input: None

Returns: None

<!-- page:80 -->
# script\_sleep

script\_sleep sec

Action: Stops the execution of a script for a given number of seconds.

Input: sec, time in seconds

Returns: None

# Examples of Using the Scripting Language

# Computing the Dose of Implanted Arsenic

If As\_Implant is the name of an As profile previously created, compute the dose of implanted As by integrating the profile. Limit the integration to portions of the curve with a concentration larger than 1e14 but without other limitations in depth or maximum concentration value:

set Dose\_As [cv\_compute "vecmax(integr(<n30\_sd\_Arsenic\_Implant>))" A A 1e14 A]

If IdVg is the name of an $\mathrm { I _ { d s } - V _ { g s } }$ curve previously created, compute a transconductance curve using diff. Limit the computation to the window in the $\mathrm { I _ { d } { - } V _ { g } }$ curve defined by Vmin = 1.0 V, Vmax = 4.0 V, Id\_min = 1e-10, and Id\_max = 5e-6:

set gm [cv\_compute "vecmax(diff(<IdVg>))" 1.0 4.0 1e-10 5e-6]

# Creating a Macro to Compute Vt

Create a macro to compute $\mathrm { V _ { t } }$ from the maximum of the second derivative of an $\mathrm { I _ { d } { - } V _ { g } }$ curve. Use <c n> as placeholders for curves and <s n> for scalars, where n represents the argument used in the macro and must start at 1. In the example, <c 1> should be an $\mathrm { I _ { d } { - } V _ { g } }$ curve and <s 2> is a multiplication factor:

macro\_define Vt2d "<s 2>\*vecvalx(diff(diff(<c 1>)), 0.999\*vecmax(diff(diff(<c 1>))))"

If IdVg is the name of an $\mathrm { I _ { d s } - V _ { g s } }$ curve previously created, use the macro created to compute $\mathrm { V _ { t } }$ in mV:

set Vt2 [cv\_compute "Vt2d(<IdVg>,1e3)" A A A A]

<!-- page:81 -->
This chapter describes how to work with script libraries in Inspect.

The scripting language of Inspect is complemented by libraries that provide additional functionality for specific operations such as curve comparison.

# Loading Libraries

You use the load\_library command to load libraries:

load\_library libraryName

where libraryName is a library identifier.

This command makes available all the functionality provided by the specified library.

All commands of a particular library have a common prefix, for example, iccap for commands provided by the IC-CAP model parameter extraction library (see IC-CAP Model Parameter Extraction Library on page 106).

# Adding a Site Library

The \$STROOT\_LIB/inspectlib directory stores all libraries as well as the lib\_index file, which provides an index of all available libraries.

To add a library, the administrator (a person with write permissions to the TCAD distribution directory \$STROOT) copies the library to the \$STROOT\_LIB/inspectlib directory and enters text in the index that describes the new library. The following fields must be provided:

<library\_name> <library\_prefix> <library\_filename>

# where:

<library\_name> is the name specified to call this library.   
<library\_prefix> is the prefix used for all commands.   
■ <library\_filename> is the name of the file where all commands are implemented.

<!-- page:82 -->
# Extraction Library

The commands provided by this library extract parameters from I–V curves. You can load the library with the command:

```txt
load_library EXTRACT 
```

The library is located at \$STROOT/\$STRELEASE/lib/inspectlib/EXTRACT.tcl. If you need to customize the library, you can create a local copy of the library and edit the scripts. In this case, the local version is loaded by sourcing the script:

```batch
source EXTRACT.tcl 
```

# cv\_linTransCurve

This command applies a linear transformation to the x- and y-values of a curve. It is called using:

```html
cv_linTransCurve <Curve> <Xm> <Xb> <Ym> <Yb> <Axis> 
```

where:

<Curve> is the name of the curve.   
■ The x- and y-values of the curve are replaced by the transformed values given by and , respectively.X' = X\*Xm Xb + Y' = Y\*Ym Yb +   
<Axis> can be either $\yen 012$ , and determines on which y-axis the transformed curve is displayed.

# Example

Shift an $\mathrm { I _ { d } { - } V _ { g s } }$ curve by 0.55 V:

```txt
cv_linTransCurve IdVgs 1 0.55 1.0 0.0 y 
```

<!-- page:83 -->
# cv\_scaleCurve

This command scales the x- and y-values of a curve. It is called using:

```txt
cv_scaleCurve <Curve> <XFactor> <YFactor> <Axis> 
```

where:

<Curve> is the name of the curve.   
■ The x- and y-values of the curve are multiplied by <XFactor> and <YFactor>, respectively.   
<Axis> can be either y or y2, and determines on which y-axis the scaled curve is displayed.

# Example

Scale an $\mathrm { I _ { d } { - } V _ { g s } }$ curve from to mA/mm:A/μm

```txt
cv_scaleCurve IdVgs 1 1e6 y 
```

# ExtractBVi

Breakdown curves sometimes exhibit a pronounced snapback, in which case, another relevant definition is the bias voltage at which the current reaches a certain level. This type of extraction is performed with the ExtractBVi command. It is called using:

```txt
ExtractBVi <Name> <Curve> <Ilevel> 
```

where:

<Name> is the name of the extracted parameter.   
<Curve> is the name of the curve.   
<Ilevel> refers to the mentioned current level.

# Example

```txt
ExtractBVi BVcboi VcIc 1e-12 
```

results in output such as:

DOE: BVcboi 9.09e+00

BVi: 9.09e+00

<!-- page:84 -->
# ExtractBVv

The breakdown voltage can be defined as the maximum voltage that can be applied to a contact.

The ExtractBVv command extracts this value. It is called using:

```txt
ExtractBVv <Name> <Curve> <Sign> 
```

# where:

<Name> is the name of the extracted parameter.   
<Curve> is the name of the curve.   
<Sign> can take the values +1 (n-p-n) or –1 (p-n-p), and distinguishes different types of bipolar transistor. (In general, specify –1 if the breakdown occurs at a negative bias.)

# Example

```txt
ExtractBVv BVcbov VcIc 1.0 
```

results in output such as:

```txt
DOE: BVcbov 9.09e+00 
```

```txt
BVv: 9.09e+00 V 
```

# ExtractEarlyV

This command extracts the Early voltage from an $\mathrm { I } _ { \mathrm { c } } { - } \mathrm { V } _ { \mathrm { c e } }$ curve. It is called using:

```txt
ExtractEarlyV <Name> <Curve> <Vtarget> 
```

# where:

<Name> is the name of the extracted parameter.   
<Curve> is the name of the curve.   
<Vtarget> is the bias point at which the slope of the $\mathrm { I } _ { \mathrm { c } } { - } \mathrm { V } _ { \mathrm { c e } }$ curve is determined for the computation of the Early voltage.

# Example

```txt
ExtractEarlyV Va IcVc 1.25 
```

results in output such as (where Ro is the output resistance and Va is the Early voltage):

```txt
DOE: Ro 3.283e+04 
```

```txt
DOE: Va -1.836e+01 
```

<!-- page:85 -->
# ExtractGm

This command extracts the maximum transconductance from an $\mathrm { I _ { d } { - } V _ { g s } }$ curve. It is called using:

```txt
ExtractGm <Name> <Curve> [<Type>] 
```

where:

<Name> is the name of the extracted parameter.   
<Curve> is to the name of the $\mathrm { I _ { d } { - } V _ { g s } }$ curve.   
See ExtractVtgm on page 76 for details about Type.

<!-- page:86 -->
# Example

set gm [ExtractGm gmLin IdVg]

results in output such as:

DOE: gmLin 1.123e-04 gm: 1.123e-04

S/um Max gm is at Vg= 0.540 V

# ExtractGmb

This command is the same as ExtractGm except that the ExtractGmb command uses parabolic interpolation to find the gate bias at which the maximum transconductance occurs (see ExtractGm).

For $\mathrm { I _ { d } { - } V _ { g s } }$ curves with a limited number of gate–bias sample points, better accuracy is achieved with the ExtractGmb command.

# ExtractIoff

This command extracts the drain leakage current from an $\mathrm { I _ { d } { - } V _ { g s } }$ curve. It is called using:

```txt
ExtractIoff <Name> <Curve> <Voff> 
```

where:

<Name> is the name of the extracted parameter.   
<Curve> is the name of the $\mathrm { I _ { d } { - } V _ { g s } }$ curve (computed for a high drain bias).   
<Voff> defines the gate voltage at which the drain leakage current is extracted, typically, at a small nonzero value to avoid noise.

<!-- page:87 -->
# Example

```tcl
if { $Type == "nMOS" } { set SIGN 1.0 } \
else { set SIGN -1.0 }
set Ioff [ExtractIoff Ioff [expr $SIGN*1e-4]] 
```

results in output such as:

```txt
DOE: Ioff 5.167e-11
Ioff: 5.167e-11 A/um 
```

# ExtractMax

This command extracts the maximum of a curve. It is called using:

```txt
ExtractMax <Name> <Curve> 
```

where:

<Name> is the name of the extracted parameter.   
<Curve> is the name of the curve.

# Example

```txt
set IdSat [ExtractMax IdSat IdVg] 
```

results in output such as:

```typescript
DOE: IdSat 4.028e-04
Max: 4.028e-04 
```

# ExtractRon

This command extracts the on-state resistance from an $\mathrm { I _ { d } - V _ { d s } }$ curve. It is called using:

```htaccess
ExtractRon <Name> <Curve> <Von> 
```

where:

<Name> is the name of the extracted parameter.   
<Curve> is the name of the $\mathrm { I _ { d } - V _ { d s } }$ curve (computed for a high gate bias).   
<Von> defines the drain voltage at which the on-state resistance is extracted, typically, well beyond saturation.

# Example

set Ron [ExtractRon Ron IdVd 1.1]

results in output such as:

```txt
DOE: Ron 14909.555
Ron: 14909.555 Ohm um 
```

# ExtractSS

This command extracts the subthreshold voltage swing from an $\mathrm { I _ { d } { - } V _ { g s } }$ curve. It is called using:

```txt
ExtractSS <Name> <Curve> <Vgo> 
```

where:

<Name> is the name of the extracted parameter.   
<Curve> is the name of the $\mathrm { I _ { d } { - } V _ { g s } }$ curve.   
<Vgo> defines the gate voltage at which the slope is extracted. It should be a value well below the threshold voltage.

NOTE The slope can be noisy at the beginning of the curve or at very low current levels, so better results are often obtained when setting Vgo > 0 V.

# Example

set SS [ExtractSS SSlin IdVg(\$N) 0.01]

results in output such as:

```txt
DOE: SSlin 79.758
SS (subthreshold voltage swing): 79.758 mV/dec 
```

# ExtractValue

This command extracts the y-value at a given x-point. It is called using:

```txt
ExtractValue <Name> <Curve> <Xo> 
```

where:

<Name> is the name of the extracted parameter.   
<Curve> is the name of the curve.

<!-- page:88 -->
<Xo> defines the x-point at which the value is extracted.

<!-- page:89 -->
# Example

```txt
set CggP [ExtractValue CgP Cgg 1.2] 
```

results in output such as:

```txt
DOE: CgP 1.426e-15
```

```javascript
CgP: 1.426e-15
```

Here, Cgg is the name of the Inspect total gate–capacitance versus the gate–voltage curve.

# ExtractVtgm

This command extracts the threshold voltage from an $\mathrm { I _ { d } { - } V _ { g s } }$ curve using the maximum transconductance method. It is called using:

```txt
ExtractVtgm <Name> <Curve> [<Type>] 
```

where:

<Name> is the name of the extracted parameter as it appears in the Variable Values column of Sentaurus Workbench.   
<Curve> is the name of the $\mathrm { I _ { d } { - } V _ { g s } }$ curve.   
<Type> specifies the transistor type, which can be one of the following values:

nMOS or nMOSneg for NMOSFETs with a positive or negative drain current convention.   
pMOS or pMOSneg for PMOSFETs with a positive or negative drain current convention.

The MOSFET threshold and transconductance extraction commands require prior knowledge of the transistor type and the sign convention for the drain current.

If <Type> is omitted, the transistor type is determined internally by analyzing the first and last points of the given curve.

The command ExtractVtgm passes the extracted value to Sentaurus Workbench and prints it to the log file. It also returns the value to Inspect.

# Example

set Vt [ExtractVtgm Vtgm IdVg]

results in output such as:

DOE: Vtgm 0.392

Vt (Max gm method): 0.392 V

# ExtractVtgmb

This is the same as ExtractVtgm except that the ExtractVtgmb command uses parabolic interpolation to find the gate bias at which the maximum transconductance occurs (see ExtractVtgm on page 76).

For $\mathrm { I _ { d } { - } V _ { g s } }$ curves with a limited number of gate–bias sample points, better accuracy is achieved with the ExtractVtgmb command.

# ExtractVti

This command extracts the gate voltage from an $\mathrm { I _ { d } { - } V _ { g s } }$ curve at which the drain current exceeds a given current level. It is called using:

ExtractVti <Name> <Curve> <Ilevel>

# where:

<Name> is the name of the extracted parameter.   
<Curve> is the name of the $\mathrm { I _ { d } { - } V _ { g s } }$ curve.   
■ <Ilevel> defines the drain current level at which to extract the gate voltage.

# Example

set Vti [ExtractVti Vti IdVg 1e-7]

results in output such as:

DOE: Vti 1.476

Vti (Vg at Io=1.000e-06): 1.476 V

<!-- page:90 -->
# FilterTable

The FilterTable command processes data from the Sentaurus Workbench Family Tree to create a plot of one Sentaurus Workbench parameter as a function of another Sentaurus Workbench parameter for a certain subset of experiments. Threshold voltage roll-off plots are a typical application of this utility.

To better understand this utility, it is helpful to first consider the kind of data on which it is designed to operate.

In an Inspect script, you can use the dynamic preprocessing feature of Sentaurus Workbench @<parameter\_name>:all@ to access a list of input parameters and extracted values for all Sentaurus Workbench experiments. For example:

```batch
set Types [list @Type:all@]
set Lgs [list @lgate:all@]
set Vts [list @Vt:all@]
set Ids [list @Id:all@]
... 
```

Here, the Tcl list Types contains, for all experiments, the values of the Sentaurus Workbench input parameter Type, which for example can take the value nMOS or pMOS, depending on whether an NMOS or a PMOS structure is created in this experiment.

Similarly, the Tcl list Lgs contains for all experiments a parallel list of values of another Sentaurus Workbench input parameter, which for example contains the value of the gate length of the given MOSFETs. The corresponding extracted parameter can be accessed in the same way. The Tcl lists Vts and Ids can contain the extracted values for the threshold voltage and the drain current for each respective experiment.

NOTE The values in the various lists might or might not be numeric, and they might not be ordered.

# Syntax of FilterTable

The FilterTable command takes lists of Sentaurus Workbench parameters as arguments. The first two lists identify the x- and y-values, which will be processed to create a plot. The subsequent arguments control the conditions an experiment must fulfill to be included in the plot. These conditions are defined using optional pairs of a target value and a Sentaurus Workbench list.

<!-- page:91 -->
The syntax of FilterTable is:

```powershell
FilterTable XList YList [ConditionTarget1 ConditionList1] \
[ConditionTarget2 ConditionList2] [ConditionTarget3 ConditionList3] [...] 
```

The command returns two lists of values:

The first list contains a subset of the XList. The subset is restricted to the selected experiments. The values are given in ascending order.   
The second list contains the corresponding values of the YList.

In addition, FilterTable ignores all entries of YList that contain a nonnumeric value. You can use this feature to omit failed extractions. In the tool input file that performs the extraction (for example, a previous Inspect instance), use the #set directive to preset the extracted variable to the value x:

```tcl
#set Vt x
...
set Vt [ExtractVtgmb Vt IdVg] 
```

The actual extraction process, here using the ExtractVtgmb command, overwrites the preset value x with the actual value. However, if the extraction process fails, the preset value persists.

For example, after preprocessing, Sentaurus Workbench preprocessor references such as @Type:all@ are expanded and the resulting preprocessed file can look like:

```tcl
set Types [list nMOS nMOS nMOS nMOS pMOS pMOS pMOS pMOS]
set Lgs [list 0.090 0.045 0.130 0.065 0.065 0.045 0.130 0.090]
set Vts [list 0.424 0.313 0.414 0.408 -0.344 -0.232 x -0.374]

set XYLists [FilterTable $Lgs $Vts "nMOS" $Types]
cv_createFromScript Vt_vs_Lg_nMOS [lindex $XYLists 0] [lindex $XYLists 1] y
cv_display Vt_vs_Lg_nMOS y

set XYLists [FilterTable $Lgs $Vts "pMOS" $Types]
cv_createFromScript Vt_vs_Lg_pMOS [lindex $XYLists 0] [lindex $XYLists 1] y
cv_display Vt_vs_Lg_pMOS y 
```

This script creates two separate Vt roll-off curves: one for all nMOS experiments and one for all pMOS experiments. The values are shown in order and the data point for Type=pMOS and Lg=0.130, for which the extraction failed (Vt=x), is omitted.

<!-- page:92 -->
# The extend Library

The extend library implements high-level commands to provide:

Better control of curve attributes (cv\_autoIncrStyle, cv\_disp, cv\_nextColor, cv\_nextSymbol, cv\_setFillColor)   
<!-- page:93 -->
■ Curve manipulation (cv\_addCurve, cv\_addDataset, cv\_linTrans, cv\_monotonicX, cv\_scale, cv\_sort)   
■ Additional curve information (cv\_getGlobalExtrema, cv\_getLocalExtrema, cv\_getNames, cv\_getRange, cv\_getXmax, cv\_integrate, cv\_linFit)   
Extraction of dataset information (ds\_getValue, proj\_datasetExists)   
■ A simple debug print function (dbputs)   
■ Functions to work with lists (ldiff, lintersect, ltranspose, lunion)   
■ An ASCII file import filter (fi\_readTxtFileHeader)

You can load the library with the command:

load\_library extend

The library is located at \$STROOT/\$STRELEASE/lib/inspectlib/extend.tcl.

If you need to customize the library, you can create a local copy of the library and edit the scripts. In this case, the local version is loaded by sourcing the script:

source extend.tcl

The commands of the library are described in the following sections. If a command is applied to a curve, the creation of the curve is not mentioned explicitly in the examples for brevity. For test purposes, curves can be created easily with the following line:

cv\_createFromScript c1 {0 1} {1 2}

NOTE Arguments in braces are optional. The first term in the braces is the name of the argument, and the second term is the default value of the argument. For example, a command that has been defined as command {arg def\_value} can be called as command (which is equivalent to command def\_value) and also as command other\_value.

# cv\_addCurve

```txt
cv_addCurve cname cname2 
```

Action: Adds the y-values of the curve cname2 to the y-values of the curve cname.

Input: cname, cname2, name of curves

Returns: None

# Example

```tcl
cv_createFromScript c1 {0 1} {1 2}
cv_createFromScript c2 {0 1} {3 4}
cv_addCurve c1 c2
puts "y: [cv_getValsY c1]"
> y: 4 6 
```

# cv\_addDataset

```txt
cv_addDataset cname xdset ydset 
```

Action: Adds the y-values of a dataset to an existing curve.

Input: cname, name of curve to which datasets will be added xdset, dataset name of the x-values to be added ydset, dataset name of the y-values to be added

Returns: None

# Example

```ruby
# sum the total currents of nContact and nContact2
cv_addDataset iv "n4_des pContact OuterVoltage" "n4_des nContact TotalCurrent"
cv_addDataset iv "n4_des pContact OuterVoltage" "n4_des nContact2
TotalCurrent" 
```

cv\_angularMap   
```txt
cv_angularMap cname {astart 0} {aend 360} 
```

Action: Maps a periodic curve to a fixed angular range of $astart$ to $aend$ . For angular data, you might want to reduce all data points to the first period. For example, if a full circle with $0..360^\circ$ will be plotted, but datapoints with x-values higher than 360 exist, these should be mapped to the first period, that is, the y-value at x=361 will be added to the datapoint x=1.

```txt
Input: cname, name of curve
astart, start of the angular range; default is 0
aend, end of the angular range; default is 360 
```

```txt
Returns: None 
```

Example   
```txt
cv_createFromScript a {0 1 2 90 91 92} {1 2 3 4 5 6}
cv_angularMap a 0 90
puts [cv_getVals a]
-> {0 1 2 90} {1 7 9 4} 
```

cv\_autoIncrStyle   
```typescript
cv_autoIncrStyle {stylelist {color fillColor line symbol}} | off
Action: Sets the curve attributes to be incremented by one whenever a curve is displayed using cv_disp. The attributes are incremented in the order given by stylelist.
Input: stylelist, list of options; default is {color fillColor line symbol} off, switches off the automatic increment feature
Returns: None 
```

Example   
```txt
# First increment color. If all colors are used, increment symbol
# and start with first color again.
cv_autoIncrStyle {color symbol}
cv_disp c1
cv_disp c2 
```

<!-- page:95 -->
# cv\_disp

```txt
cv_disp cname {label ""} {axis "y"} 
```

Action: Displays a curve using the specified label and axis. The curve attributes are incremented by default, such that each displayed curve can be easily distinguished.

Additional control of the curve attributes is given by the following commands:

```javascript
cv_autoIncrStyle, cv_nextColor, cv_nextLine, cv_nextSymbol, cv_resetColor, cv_resetFillColor, cv_resetLine, cv_resetStyle, cv_resetSymbol. 
```

Input: cname, name of curve

label, specifies the curve label to be displayed in the legend; default is the curve name

axis, specifies the axis to use: y (default) or y2

Controlling attributes manually makes most sense when cv\_autoIncrStyle is switched off.

Returns: None

# Example

cv\_disp iv "simulated IV" y

# cv\_exists

```txt
cv_exists cname 
```

Action: Checks whether a curve exists.

Input: cname, name of curve

Returns: 1 (the curve exists) or 0 (the curve does not exist)

# Example

if {[cv\_exists iv]} {puts "curve iv exists"}

cv\_getGlobalExtrema   
```txt
cv_getGlobalExtrema cname {type max}
Action: Returns the global maximum or minimum of a curve as a list.
Input: cname, name of curve
type, specifies either the global maximum (max) or global minimum (min);
default is max
Returns: If type equals max: {xmax ymax}
If type equals min: {xmin ymin} 
```

Example   
```tcl
set cmin [cv_getGlobalExtrema iv min]
puts "The minimum of the iv-curve is [lindex $cmin 1] and occurred at [lindex $cmin 0]" 
```

cv\_getLocalExtrema   
```txt
cv_getLocalExtrema cname {type max}

Action: Returns all local maxima or minima of a curve as a list.

Input: cname, name of curve
type, specifies either the local maxima (max) or local minima (min); default is max

Returns: If type equals max: {{xmax1 ymax1} {xmax2 ymax2} ...}
If type equals min: {{xmin1 ymin1} {xmin2 ymin2} ...} 
```

Example   
```batch
set cmax [cv_getLocalExtrema iv "max"]
puts "All maxima of the iv-curve: $cmax" 
```

<!-- page:97 -->
# cv\_getNames

```txt
cv_getNames 
```

Action: Returns all existing curve names.

Input: None

Returns: List of curve names

# Example

puts "the following curves exist currently: [cv\_getNames]"

# cv\_getRange

```txt
cv_getRange cname 
```

Action: Returns the x- and y-range of a curve as a list.

Input: cname, name of curve

Returns: {xmin,xmax,ymin,ymax}

# Example

puts "{xmin,xmax,ymin,ymax}: [cv\_getRange iv]"

# cv\_getXmax

```txt
cv_getXmax cname 
```

Action: Returns the upper boundary of the x-values of a curve.

Input: cname, name of curve

Returns: xmax

# Example

puts "upper boundary of the x values of iv: [cv\_getXmax iv]"

<!-- page:98 -->
# cv\_getXmin

cv\_getXmin cname

Action: Returns the lower boundary of the x-values of a curve.

Input: cname, name of curve

Returns: xmin

# Example

puts "lower boundary of the x values of iv: [cv\_getXmin iv]"

# cv\_getYmax

cv\_getYmax cname

Action: Returns the upper boundary of the y-values of a curve.

Input: cname, name of curve

Returns: ymax

# Example

puts "upper boundary of the y values of iv: [cv\_getYmax iv]"

# cv\_getYmin

cv\_getYmin cname

Action: Returns the lower boundary of the y-values of a curve.

Input: cname, name of curve

Returns: ymin

# Example

puts "lower boundary of the y values of iv: [cv\_getYmin iv]"

<!-- page:99 -->
# cv\_integrate

```tcl
cv_integrate formula {xstart {} } {xend {} } {mode {} } {xdigits {} } 
```  
Action: Performs integration of a formula, and returns the integration value.

```txt
Input: formula, formula to be integrated as it is specified for cv_createWithFormula
xstart, start of the integration interval; if not specified, the start of the curve is used
xend, end of the integration interval; if not specified, the end of the curve is used mode, defines the integration mode:
- If not specified, it is set to {}, which performs the Inspect internal integration using integr()
- sumup sums all y-values
- trapez performs the integration using the trapezoidal rule
xdigits, when using sumup, the number of data points is crucial; xdigits specifies the number of digits to determine whether two x-values are identical 
```

When the formula contains more than one curve and these curves have different sets of x-values, summation is performed over all x-values.

Returns: Integration value

# Example

```txt
# P_t is the time-dependent power
puts "energy in the first second is: [cv_integrate P_t 0 1 trapez]" 
```

# cv\_isVisible

```txt
cv_isVisible cname 
```

Action: Checks whether a curve is displayed.   
```txt
Input: cname, name of curve 
```  
Returns: 1 if curve is currently displayed; otherwise, 0

# Example

```txt
if { [cv_isVisible iv]} {puts "curve iv visible"} 
```

cv\_linFit   
cv_linFit formula {xstart {} } {xend {}}

Action: Performs a linear fit $y = A + B \cdot x$ to a curve formula.

Input: formula, formula to be fitted, as it is specified for cv_createWithFormula xstart, start of the fit interval
xend, end of the fit interval

Returns: Fit results as a list:
- (Estimate of) Intercept A
- (Estimate of) Slope B
- Standard deviation of y relative to the fit correlation coefficient $R^{2}$ - Number of degrees of freedom df
- Standard error of intercept A
- Significance level of A
- Standard error of slope B
- Significance level of B

Example   
```txt
set res [cv_linFit "log(<cname>)"] 
```

cv\_linTrans   
cv_linTrans cname xm {xb 0} {ym 1} {yb 0}

Action: Scales a curve linearly, and replaces x with $xm \cdot x + xb$ and y with $ym \cdot y + yb$ .

Input: cname, name of curve
xm, slope of the x-values
xb, offset of the x-values
ym, slope of the y-values
yb, offset of the y-values

Returns: None

Example   
```txt
# Scaling an IV curve given in A over V, to mA over mV.
# In addition, the curve had a current offset of 2A, which you want to remove.
cv_linTrans iv 1e3 0 1e3 -2000 
```

<!-- page:101 -->
# cv\_monotonicX

```txt
cv_monotonicX cname 
```

Action: Extracts the part of a curve where the x-values increase monotonically to the maximal x-value.

Input: cname, name of curve

Returns: None

# Example

```txt
cv_createFromScript iv {0 1 2 0 2 4} {1 2 3 4 5 6}
cv_monotonicX iv
puts "values: [cv_getVals iv]"
-->values: {0 2 4} {4 5 6} 
```

# cv\_nextColor

```txt
cv_nextColor {cindex ""} 
```

Action: Sets the next color of the curve from the extend::COLORPALETTE list.

Input: cindex, if cindex is specified, the specified entry from the extend::COLORPALETTE list is taken; otherwise, the next entry is chosen

Controlling attributes manually makes most sense when cv\_autoIncrStyle is switched off.

Returns: None

# Example

```txt
cv_autoIncrStyle off
cv_disp iv1
cv_nextColor
cv_disp iv2 
```

<!-- page:102 -->
# cv\_nextLine

```txt
cv_nextLine {cindex ""} 
```

Action: Sets the next line style of the curve from the extend::LINEPALETTE list.

Input: cindex, if cindex is specified, the specified entry from the extend::LINEPALETTE list is taken; otherwise, the next entry is chosen. If the last line style is reached, the first line style is returned again.

Controlling attributes manually makes most sense when cv\_autoIncrStyle is switched off.

Returns: None

# Example

```txt
cv_autoIncrStyle off
cv_disp iv1
cv_nextLine
cv_disp iv2 
```

# cv\_nextSymbol

```txt
cv_nextSymbol {cindex ""} 
```

Action: Sets the next symbol type of the curve from the extend::SYMBOLPALETTE list.

Input: cindex, if cindex is specified, the specified entry from the extend::SYMBOLPALETTE list is taken; otherwise, the next entry is chosen. If the last symbol is reached, the first symbol is returned again.

Controlling attributes manually makes most sense when cv\_autoIncrStyle is switched off.

Returns: None

# Example

```txt
cv_autoIncrStyle off
cv_disp iv1
cv_nextSymbol
cv_disp iv2 
```

<!-- page:103 -->
# cv\_resetColor

```txt
cv_resetColor 
```

Action: Resets the color to the default entry that equals the first entry from the extend::COLORPALETTE list.

Input: None

Returns: None

# Example

```txt
cv_autoIncrStyle off
cv_disp iv1
cv_nextColor
cv_disp iv2
cv_resetColor
cv_nextSymbol
cv_disp iv3 
```

# cv\_resetFillColor

```txt
cv_resetFillColor 
```

Action: Resets the fill color to white.

Input: None

Returns: None

# Example

```txt
cv_autoIncrStyle off
cv_disp iv1
cv_nextColor
cv_disp iv2
cv_resetFillColor
cv_nextSymbol
cv_disp iv3 
```

<!-- page:104 -->
# cv\_resetLine

```txt
cv_resetLine 
```

Action: Resets the line style to the default entry that equals the first entry from the extend::LINEPALETTE list.

Input: None

Returns: None

# Example

```csv
cv_autoIncrStyle off
cv_disp iv1
cv_nextLine
cv_disp iv2
cv_resetLine
cv_nextSymbol
cv_disp iv3 
```

# cv\_resetStyle

```txt
cv_resetStyle 
```

Action: Resets all curve style attributes such as color, fill color, symbol, and line style to their default values.

Input: None

Returns: None

# Example

```txt
cv_autoIncrStyle off
cv_disp iv1
cv_nextSymbol
cv_nextColor
cv_disp iv2
cv_resetStyle
cv_disp iv3 
```

<!-- page:105 -->
# cv\_resetSymbol

```txt
cv_resetSymbol 
```

Action: Resets the symbol to the default entry that equals the first entry from the extend::SYMBOLPALETTE list.

Input: None

Returns: None

# Example

```txt
cv_autoIncrStyle off
cv_disp iv1
cv_nextSymbol
cv_disp iv2
cv_resetSymbol
cv_nextColor
cv_disp iv3 
```

# cv\_round

```txt
cv_round cname xdigits ydigits 
```

Action: Rounds off the x-data and y-data values to the specified number of digits.

Input: cname, name of curve xdigits, number of digits to be kept for x-values; default is -1 (no rounding) ydigits, number of digits to be kept for y-values; default is -1 (no rounding)

Returns: None

# Example

```tcl
cv_createFromScript c {1.01 5.05} {9.09 7.07}
cv_round c 1 1
puts "[cv_getVals c]"
=> {1 5.1} {9.1 7.1} 
```

<!-- page:106 -->
# cv\_scale

```txt
cv_scale cname xm ym 
```

Action: Scales a curve linearly, and replaces with and with .x xm x⋅ y ym y⋅

Input: cname, name of curve xm, scale applied to x-values ym, scale applied to y-values

Returns: None

# Example

\# Scales a current over time given in A over s to mA over us. cv\_scale i\_t 1e6 1e3

# cv\_setFillColor

```txt
cv_setFillColor {mode 1} 
```

Action: Switches the fill color on and off.

Input: mode, sets the fill color: – 1 fills the symbol with the curve color; default is 1 – 0 specifies the fill color is white

Returns: None

# Example

```txt
cv_autoIncrStyle off
cv_setSymbol 1
cv_disp iv1
cv_nextColor
cv_setFillColor 1
cv_disp iv2 
```

cv\_setSymbol   
```yaml
cv_setSymbol {mode 1}
Action: Switches symbols on and off.
Input: mode, sets the symbol:
    - 1 specifies that the symbols are shown
    - 0 specifies that the symbols are not shown; default is 1
Returns: None 
```

Example   
```csv
cv_autoIncrStyle off
cv_disp iv1
cv_nextColor
cv_setSymbol 1
cv_disp iv2 
```

cv\_sort   
```txt
cv_sort cname {xdigits 20}
Action: Sorts data points of a curve according to x-values, and removes duplicates.
Input: cname, name of curve
xdigits, number of digits of x-value to determine whether two values are identical
Returns: None 
```

Example   
```tcl
cv_createFromScript c {1 2 0.0001 3 0} {2 3 -1 4 1}
cv_sort c 3
puts "[cv_getVals c]"
==> {0 1 2 3} {1 2 3 4} 
```

<!-- page:108 -->
# cv\_write

```txt
cv_write type filename curveList 
```

Action: Exports curve data to a file. This command works like the native cv\_write command but, in addition, allows exporting data in CSV format, which is most suitable for transferring data to spreadsheet applications.

Input: type, type of file: csv, plt, xgraph, or xmgr filename, name of file in which to export data curveList, list of curves

Returns: 1 if successful, 0 otherwise

# Example

```batch
cv_write csv export.csv "idvg cv($n)" 
```

# dbputs

```txt
dbputs str {dbglevel 1} 
```

Action: Debugs output, where str is displayed in the log if the debug variable ::DEBUG is greater than or equal to the debug level.

Input: str, string to be printed to standard output dbglevel, sets the debug level

Returns: None

# Example

```asm
dbputs "test1"
set ::DEBUG 2
dbputs "test2"
dbputs "test3" 2
dbputs "test4" 3
set ::DEBUG 0
dbputs "test5"
==> test2, test3 
```

<!-- page:109 -->
# ds\_getValue

ds\_getValue proj datasetName {index end}

Action: Returns the index-th value of a dataset.

Input: proj, project name of the loaded .plt file datasetName, name of dataset index, the index of the dataset item to return; counting starts with 0 and finishes with end; default is end

Returns: Real number

# Example

```tcl
proj_load n5_des.plt
puts "first value [ds_getValue n5_des "anode OuterVoltage" 0]"
puts "last value [ds_getValue n5_des "anode OuterVoltage"]] 
```

# fi\_readTxtFile

fi\_readTxtFile fname cname {columnIdx 1}

Action: Reads in data from an ASCII file, where columns are separated by space. The xvalues are taken from the first column; the column to be used for the y-values can be specified. The file can contain comment lines starting with a hash character (#).

Input: fname, name of ASCII file cname, name of curve to be created columnIdx, column index to be used for y-values; column-counting starts with 0; default is the second column (columnIdx = 1)

Returns: None

# Example

fi\_readTxtFile "am15g.txt" spec

<!-- page:110 -->
# fi\_readTxtFileHeader

```txt
fi_readTxtFileHeader fname 
```

Action: Reads and returns the header line – a single line that is neither data nor comment.

Input: fname, name of ASCII file

Returns: List of strings

# Example

```txt
puts "[fi_readTxtFileHeader "am15g.g"]"
==> Wavelength [um] Intensity [W*cm^-2] 
```

# gr\_axis

```txt
gr_axis axis title {xmin ""} {xmax ""} {scale lin} 
```

Action: Sets the attributes of the x-axis and y-axis.

Input: axis, specifies axis to be modified: x, y, or y2 title, axis label xmin, xmax, sets the range of the axis, where {} specifies automatic scaling scale, specifies the scaling to apply: lin (default) or log

Returns: None

# Example

```txt
gr_axis x {voltage [V]}
gr_axis y {current [A]} {} {} log 
```

<!-- page:111 -->
# gr\_resetAxis

```txt
gr_resetAxis 
```

Action: Resets all the axis attributes and, in particular, switches off the y2-axis.

Input: None

Returns: None

# Example

```tcl
gr_axis x {voltage [V]}
gr_axis y {current [A]} {} {} log
gr_resetAxis 
```

# gr\_setStyle

```txt
gr_setStyle mode 
```

Action: Sets the style of the plot area.

Input: mode, specifies the mode:

```txt
- "screen" (default) is used for the interactive mode
- "presentation" uses larger font sizes suitable for copying plots into presentations 
```

Returns: None

# Example

```txt
gr_setStyle "presentation" 
```

<!-- page:112 -->
# ldiff

```txt
ldiff list1 list2 {symmetric ""} 
```

Action: Returns all items of list1 that are not in list2.

Input: list1, list2, lists to be compared symmetric, if specified, indicates that the returned list will also contain all items of list2 that are not in list1

Returns: List

# Example

```tcl
set l1 {1 2 3 4}
set l2 {1 2 5}
puts "[ldiff $l1 $l2]"
==> {3 4}
puts "[ldiff $l1 $l2 1]"
==> {3 4 5} 
```

# lintersect

```batch
lintersect list1 list2 
```

Action: Returns all items that are members of both list1 and list2.

Input: list1, list2, lists to compare

Returns: List

# Example

```tcl
set l1 {1 2 3 4}
set l2 {1 2}
puts "[lintersect $l1 $l2]"
==> {1 2} 
```

<!-- page:113 -->
# ltranspose

ltranspose list

Action: Transposes a list.

Input: list, list to transpose

Returns: List

# Example

```tcl
set 1 {{1 2} {3 4} {5 6}}
puts "[ltranspose $1]"
==> {{1 3 5} {2 4 6}} 
```

# lunion

lunion list1 list2

Action: Returns a list of unique items that are members of list1 or list2.

Input: list1, list2, lists to compare

Returns: List

# Example

```tcl
set l1 {1 2 3 4}
set l2 {1 2 5}
puts "[lunion $l1 $l2]"
==> {1 2 3 4 5} 
```

<!-- page:114 -->
# proj\_check

```txt
proj_check proj 
```

Action: Checks all datasets in a project to see whether all entries are valid.

Input: proj, project name of the loaded .plt file

Returns: List of dataset names containing invalid data (nonnumeric values)

# Example

```batch
proj_load n5_des.plt 
```

```txt
proj_check n5_des 
```

# proj\_datasetExists

```txt
proj_datasetExists proj_datasetName {groupName ""} 
```

Action: Checks whether a project contains data with the specified dataset and group name.

Input: proj, project name of the loaded .plt file datasetName, name of dataset groupName, group name of dataset; if no group name is given and the dataset name contains a space, the first word of datasetName is taken as the group name

Returns: 1 (dataset exists) or 0 (dataset does not exist)

# Example

```tcl
proj_load n5_des.plt
if { [proj_datasetExists n5_des "anode OuterVoltage"] }
    {puts "anode OuterVoltage exists" }
if { [proj_datasetExists n5_des "OuterVoltage" "anode"] }
    {puts "anode OuterVoltage exists" }
if { [proj_datasetExists n5_des "NO_NODE time"] } {puts "time exists"} 
```

<!-- page:115 -->
# proj\_getGroups

```txt
proj_getGroups proj 
```

Action: Returns a sorted list containing all group names of the project.

Input: proj, project name of the loaded .plt file

Returns: List of strings

# Example

```txt
proj_load n5_des.plt
puts "all group names: [proj_getGroups n5_des]" 
```

# proj\_groupExists

```txt
proj_groupExists proj groupName 
```

Action: Checks whether a project contains a particular group.

Input: proj, project name of the loaded .plt file groupName, name of group

Returns: 1 (group exists) or 0 (group does not exist)

# Example

```tcl
proj_load n5_des.plt
if { [proj_groupExists n5_des "anode"] } {puts "group anode exists"} 
```

<!-- page:116 -->
# proj\_loadPlx

proj\_loadPlx fileName {curveName} {appendDatasetName}

Action: Opens a .plx file, and creates a curve without displaying it.

Input: fileName, name of .plx file from which to load data curveName, name of curve; if not specified, the dataset name is used appendDatasetName, if set to 1, it appends the dataset name to the curve name: – If curveName is empty, the dataset name is used – If a simple curve name is given, the dataset name is appended in parentheses, for example, cname(data) – If the curve name contains parentheses, the dataset name is appended in the parentheses, for example, cname(cval,data)

Returns: None

# Example

```txt
Content of test.plx:
"data"
0 0
1 2.8
...
proj_loadPlx test.plx
puts "visible: [cv_isVisible data]"
==> visible: 0
proj_loadPlx test.plx c(1) 1
puts "visible: [cv_isVisible c(1,data)]"
==> visible: 0 
```

<!-- page:117 -->
# The PhysicalConstants Library

This library defines a set of variables of major physical constants [1].

To load the library, use the command:

load\_library PhysicalConstants

Table 6 Variables defined in PhysicalConstants library 

<table><tr><td>Name of variable</td><td>Value</td><td>Unit</td></tr><tr><td>AtomicMassConstant</td><td>1.660540210e-27</td><td>kg</td></tr><tr><td>AvogadroConstant</td><td>6.022136736e23</td><td> $mol^{-1}$ </td></tr><tr><td>BohrMagneton</td><td>9.274015431e-24</td><td>J/T</td></tr><tr><td>BoltzmannConstant</td><td>1.38065812e-23</td><td>J/K</td></tr><tr><td>ElectronMass</td><td>9.109389754e-31</td><td>kg</td></tr><tr><td>ElectronVolt</td><td>1.6021773349e-19</td><td>J</td></tr><tr><td>ElementaryCharge</td><td>1.6021773349e-19</td><td>C</td></tr><tr><td>FaradayConstant</td><td>9.648530929e4</td><td>C/mol</td></tr><tr><td>FineStructureConstant</td><td>7.2973530833e-3</td><td>1</td></tr><tr><td>FreeSpaceImpedance</td><td>376.730313462</td><td>Ω</td></tr><tr><td>GravitationConstant</td><td>6.6725985e-11</td><td> $m^3/kg/s^2$ </td></tr><tr><td>MagneticFluxQuantum</td><td>2.0678346161e-15</td><td>Wb</td></tr><tr><td>MolarVolume</td><td>22.4141019e-3</td><td> $m^3/mol$ </td></tr><tr><td>Permeability</td><td>12.566370614e-7</td><td>H/m</td></tr><tr><td>Permittivity</td><td>8.854187817e-12</td><td>F/m</td></tr><tr><td>Pi</td><td>3.141592653589793</td><td>1</td></tr><tr><td>PlanckConstant</td><td>6.626075540e-34</td><td>Js</td></tr><tr><td>ProtonMass</td><td>1.672623110e-27</td><td>kg</td></tr><tr><td>RydbergConstant</td><td>1.097373153413e7</td><td> $m^{-1}$ </td></tr><tr><td>SpeedOfLight</td><td>299792458</td><td>m/s</td></tr><tr><td>StefanBoltzmannConstant</td><td>5.6705119e-8</td><td> $W/m^2/K^4$ </td></tr></table>

<!-- page:118 -->
All variables are defined in the namespace ::const::. To access a variable, use \$::const::<varName> or \$const::<varName>, where <varName> must be replaced by a particular variable name, for example:

```ruby
load_library PhysicalConstants puts "c=$const::SpeedOfLight" 
```

The function getVarNames returns a list of all variable names, for example:

```tcl
set varlist [const::getVarNames]
puts "all variables: $varlist"
==> all variables: AtomicMassConstant AvogadroConstant BohrMagneton ... 
```

To see a list of all variables, the function printVarNames prints directly the names of all available variables:

```txt
const::printVarNames
==> 
AtomicMassConstant
AvogadroConstant
BohrMagneton
... 
```

# IC-CAP Model Parameter Extraction Library

The commands of this library are used to export device simulation results to the Integrated Circuit Characterization and Analysis Program (IC-CAP) model extraction tool. These commands can create files that can be later imported by IC-CAP.

To load the library, use the command:

```txt
load_library ise2iccap 
```

# Exporting Data

```txt
iccap_Write fileName headerInfo data 
```

Action: Exports data to a file using the IC-CAP data management file data format [2].

```txt
Input: fileName, file name
headerInfo, header information (see Header Information on page 107)
data, array of curve data (see Array Data on page 108) 
```

```txt
Returns: None 
```

<!-- page:119 -->
# Header Information

The header information headerInfo is a list formed by the sublists userInput, iccapInput, and output.

A detailed description of the header section is presented in the literature [2]. You can use the following examples as guides.

# userInput

This sublist contains information about variables that cannot be swept in a traditional IC-CAP setup.

In the following example, no user sweeps are considered:

```txt
userInput: {} 
```

# iccapInput

This sublist contains information about variables that can be swept in an IC-CAP setup. For example:

```txt
iccapInput: {{vg V G GROUND {LIST 1 26 0.0...2.5}}  
{vb V D GROUND {LIN 2 -0.1 -0.5 3}}  
{vd V S GROUND {CON 0.0}}
```

In this example, there are three IC-CAP input variables, where:

The first element is the name of the input variable.   
The second element is the mode.   
The third and fourth elements are the names of the positive and negative nodes for the corresponding input variable.   
The fifth element is a list that describes the sweep. The first element of this list is the sweep type, which can be LIN, LIST, CON, LOG, or SYNC.

The sweep information for the first input variable (vg) is a list where:

LIST indicates that all sweep values are explicitly defined.   
■ 1 is the sweep order (1 is the innermost or fastest varying sweep).   
26 is the number of values.   
■ 0.0...2.5 indicate all values that the particular variable can take.

<!-- page:120 -->
The sweep information for the second input variable (vb) is a list where:

■ LIN indicates that the sweep values are a set of values defined in a linear scale.   
2 is the sweep order.   
-0.1 is the start value.   
-0.5 is the end value.   
3 is the number of values.

The sweep information for the third input variable (vd) is a list where:

CON indicates that there is only one value for this variable.   
0.0 is a constant value.

# output

This sublist contains information about output variables that can be recognized in an IC-CAP setup. For example:

```handlebars
output is {{id I D GROUND}} 
```

In this example, there is only one output variable, which is the drain current. The first element is the name of the output variable, the second element is the mode, and the third and fourth elements are the names of the positive and negative nodes for the corresponding output variable.

# Array Data

The array data must contain, at least, the following information:

```txt
data(<input tuples>,<output>) 
```

There is one array cell for each pair formed by a tuple of input variable values and an output variable. The <input tuples> order is the inverse of the sweep order.

For example, using the example in Header Information on page 107, the array data contains the following information:

```javascript
data (<vb>, <vg>, id) 
```

In this case, each cell stores the drain current (id) for a particular combination of substrate voltage value (<vb>) and gate voltage value (<vg>).

For example, the tuple data(-0.1,1.0,id) stores the drain current for vb = –0.1 V and vg = 1.0 V.

<!-- page:121 -->
# Curve Comparison Library

The commands of this library compare two curves by computing the square difference between the two curves within a given domain.

To load the library, use the command:

load\_library curvecomp

# cvcmp\_CompareTwoCurves

cvcmp\_CompareTwoCurves curve1 curve2 windowX use\_log n

Action: Computes the square difference between two curves within a given domain (window) using either linear scale or logarithmic scale.

Input: curve1, curve2, curves to compare windowX, window in the x-axis use\_log, true if logarithmic scale is used n, base name for the internal curves

Returns: Square difference between two curves

# cvcmp\_DeltaTwoCurves

cvcmp\_DeltaTwoCurves exp\_file sim\_file minX maxX use\_log name

Action: Writes the square difference between two curves within a given domain (window) to the standard output. This difference can be computed using either a linear or logarithmic scale. Both curves are read from files. This command uses the ft\_scalar command to export the computed difference to the Family Tree of Sentaurus Workbench.

Input: exp\_file, sim\_file, files where the two curves are stored minX, maxX, window in the x-axis use\_log, true if a logarithmic scale is used name, name of the column of the Family Tree of Sentaurus Workbench where the computed difference is stored

Returns: None

<!-- page:122 -->
# References

[1] G. Woan, The Cambridge Handbook of Physics Formulas, Cambridge: Cambridge University Press, 2000.   
[2] IC-CAP Data Management File Format Specification: Final IC-CAP 5.0 file specification, E. Arnold and M. Peroolmal (eds.), HP-EESOP document archive, March, 1997.

<!-- page:123 -->
This appendix lists the toolbar buttons and menus available from the user interface of Inspect.

# Toolbar Buttons

The toolbar provides quick access to commonly used operations that are also available from the menus.

Table 7 Inspect toolbar buttons 

<table><tr><td>Button</td><td>Description</td><td>Button</td><td>Description</td></tr><tr><td><img src="images/inspect_ug_17447de89d9c3999415f97edeaf74407e9958ed3216f7e65c23f6a3b3f20db0c.jpg"/></td><td>Loads a dataset file</td><td><img src="images/inspect_ug_ee115b058c39bbec8a8b6fb28b421a0e8c68563ea5429a05d98e11f05f20e11a.jpg"/></td><td>Shows or hides the grid</td></tr><tr><td><img src="images/inspect_ug_a976a740c1ba0fa923931fe0658fb61b6d692961e0e1958d2e47c702e389086c.jpg"/></td><td>Prints the current plot</td><td><img src="images/inspect_ug_4c2ba069972763a8af63e148b8fbb8fefceb44de99624a1debe497ec5889aaf0.jpg"/></td><td>Moves selected curve to the front of all curves</td></tr><tr><td><img src="images/inspect_ug_2520b5d9f16b19765565e4a2742afc07efe7c4639246228fea5bf38a85465f22.jpg"/></td><td>Reloads the dataset file</td><td><img src="images/inspect_ug_6e77d08d11fbb31720245f14f92fa28ca648a336b7eaab9da25c4c90b3aa1375.jpg"/></td><td>Moves selected curve to the back of all curves</td></tr><tr><td><img src="images/inspect_ug_ef3191a80bffcce20c1b4314889b837260ea8ea0c7df64cbaf398b6c2fb9963a.jpg"/></td><td>Applies recent plotting actions made on the previous dataset to the current dataset</td><td><img src="images/inspect_ug_d1f3362c6c7b0ce95b98aca6ad150b64abc21fb0e36831506d54c54fbc4e1174.jpg"/></td><td>Moves selected curve forward</td></tr><tr><td><img src="images/inspect_ug_d80cd67a71f927c61c150f786c7f90a7a51b2883c6e461ac4b235e20913cd0d1.jpg"/></td><td>Removes all curves, and cleans up the plot area</td><td><img src="images/inspect_ug_f4390309a36cb67e370336448321285fd34d21cecd7507727ef04c2562fe71ae.jpg"/></td><td>Moves selected curve backward</td></tr><tr><td>[BYH6]</td><td>Zooms in to a selected area</td><td>box=cal</td><td>Runs or continues executing script</td></tr><tr><td>[boxval]</td><td>Zooms out of an area</td><td><img src="images/inspect_ug_3f7f34ee5f2390644ed6e29902fa279dbfa0c9090c624c8a72ee0b3fd2853679.jpg"/></td><td>Stops executing script</td></tr><tr><td>[boxval]</td><td>Displays the entire plot area</td><td>[boxval]</td><td>Switches on or switches off logarithmic scale on the x-axis</td></tr><tr><td>[boxval]</td><td>Centers the view in the plot area (applies to a zoomed plot only)</td><td>boxval</td><td>Switches on or switches off logarithmic scale on the left y-axis</td></tr><tr><td>[boxval]</td><td>Zooms in to one selected curve</td><td>boxval</td><td>Switches on or switches off logarithmic scale on the right y-axis</td></tr><tr><td>[boxval]</td><td>Shows or hides the legend text</td><td></td><td></td></tr></table>

<!-- page:124 -->
# File Menu

Table 8 File menu commands 

<table><tr><td>Command</td><td>Toolbar button</td><td>Shortcut keys</td><td>Description</td></tr><tr><td>Load Dataset</td><td><img src="images/inspect_ug_eee3d13ad0c800ae22d2842e81a2d072f68dfebe6d3d5471db5580629ea6390c.jpg"/></td><td>Ctrl+L</td><td>Opens dataset file.</td></tr><tr><td>Update Datasets</td><td><img src="images/inspect_ug_849b4bbf88a13d1eb2acab14d73152927926d7ac6d5c82363da150c25df4df94.jpg"/></td><td>Ctrl+U</td><td>Reloads datasets from opened files and updates related curves.</td></tr><tr><td>Automatically Update Datasets</td><td></td><td></td><td>Automatically reloads datasets from opened files.</td></tr><tr><td>Delete Datasets</td><td></td><td></td><td>Deletes selected projects and the curves that use data from them.</td></tr><tr><td>Load Setup</td><td></td><td></td><td>Loads preferences stored in setup file.</td></tr><tr><td>Save Setup</td><td></td><td></td><td>Saves preferences to setup file.</td></tr><tr><td>Restore All</td><td></td><td></td><td>Loads a previously saved project from a .sav file.</td></tr><tr><td>Save All</td><td></td><td></td><td>Saves current state of Inspect to a .sav file.</td></tr><tr><td>Export</td><td></td><td></td><td>Saves current curves to different file formats.</td></tr><tr><td>Write Bitmap</td><td></td><td>Ctrl+W</td><td>Creates a bitmap file of plot area image in PNG format.</td></tr><tr><td>Write EPS</td><td></td><td></td><td>Creates an EPS file of plot area image.</td></tr><tr><td>Write PS</td><td></td><td></td><td>Creates a PostScript file of plot area image.</td></tr><tr><td>Print</td><td><img src="images/inspect_ug_9710aef642f44ff94857d8225276f78ae86a500223e0cc3a8642ee600ebe23f5.jpg"/></td><td>Ctrl+P</td><td>Opens the Printer Setup dialog box.</td></tr><tr><td>Preferences</td><td></td><td></td><td>Opens the Preferences dialog box.</td></tr><tr><td>Exit</td><td></td><td>Ctrl+Q</td><td>Exits Inspect.</td></tr></table>

<!-- page:125 -->
# Edit Menu

Table 9 Edit menu commands 

<table><tr><td>Command</td><td>Toolbar button</td><td>Shortcut keys</td><td>Description</td></tr><tr><td>Redo Last Plot</td><td><img src="images/inspect_ug_8daeba96defc04fb2d690f4f1349ba286a687fb2f61238d72c7cbf879f8d7c3f.jpg"/></td><td>Ctrl+E</td><td>Applies the last plotting actions to selected datasets.</td></tr><tr><td>Plot Area</td><td></td><td>Ctrl+G</td><td>Opens the Plot Area dialog box to change attributes of plot area.</td></tr><tr><td>Clean Plot Area</td><td><img src="images/inspect_ug_25694e6de8caa06ce956eba1c93280c19f658f4611b650a3c754db8e5a8a5680.jpg"/></td><td></td><td>Cleans up the plot area.</td></tr><tr><td>Axes</td><td></td><td>Ctrl+A</td><td>Opens the Axes dialog box to change attributes of axes.</td></tr><tr><td>Labels</td><td></td><td></td><td>Displays options to add, edit, and remove labels from the plot area.</td></tr><tr><td>Define Macros</td><td></td><td></td><td>Opens the Macro Editor.</td></tr></table>

# Curve Menu

Table 10 Curve menu commands 

<table><tr><td>Command</td><td>Toolbar button</td><td>Shortcut keys</td><td>Description</td></tr><tr><td>Transform</td><td></td><td></td><td>Displays the following options: Abs X: Maps x-value of all data points of selected curves to its absolute value and redisplays the curve. Abs Y: Maps y-value of all data points of selected curves to its absolute value and redisplays the curve. Reflect X: Reflects curve about x-axis. Reflect Y: Reflects curve about y-axis. Suppress Backtrace: Data points of a selected curve where the x values are not monotonically increasing (where the current x-value is less than the previous one) indicate the start of a new line. In this case, no line connects the previous point to the current point.</td></tr><tr><td>Curve Data</td><td></td><td>Ctrl+D</td><td>Opens a dialog box that shows the points of the dataset corresponding to the selected curve.</td></tr><tr><td>Restore Data</td><td></td><td></td><td>Undoes all changes to selected curves.</td></tr></table>

Table 10 Curve menu commands 

<table><tr><td>Command</td><td>Toolbar button</td><td>Shortcut keys</td><td>Description</td></tr><tr><td>DeltaX (X)</td><td></td><td></td><td>Creates a deltaX curve for each selected curve. The deltaX curve is obtained by taking the x-dataset of the original curve as the x-dataset of the new curve and computing the y-dataset at every point by subtracting the x-value at the current point from the x-value at the next point.</td></tr><tr><td>Intersect X ?</td><td></td><td></td><td>Opens a dialog box displaying the x-coordinate at which the selected curve crosses the x-axis. If more than one curve is selected, no action is taken.</td></tr><tr><td>Inspector</td><td></td><td></td><td>Opens the Inspector dialog box.</td></tr><tr><td>Drawing Order</td><td>[82KZ][60A0]<img src="images/inspect_ug_f5f407a16bfb99713f656da8d688ed265dc0c8a86293449ec038bb5f980f536b.jpg"/><img src="images/inspect_ug_ebbd8d32a4c996da40afc4bcc185b2151c8cc561a4e23d68aa247edb2f103f9f.jpg"/></td><td></td><td>Opens a submenu to rearrange order of curves. Options are:Move to Front: Moves the selected curve to the front of all curves.Move to Back: Moves the selected curve to the back of all curves.Move Forward: Moves the selected curve one step closer to the front.Move Backward: Moves the selected curve one step closer to the back.</td></tr></table>

<!-- page:126 -->
# Script Menu

Table 11 Script menu commands 

<table><tr><td>Command</td><td>Toolbar button</td><td>Shortcut keys</td><td>Description</td></tr><tr><td>Run Script</td><td></td><td>Ctrl+R</td><td>Opens a dialog box to select the script file to be run. The default filter for the script file is *. cmd.</td></tr><tr><td>Record</td><td></td><td></td><td>Creates a script file. Options are:Start: Opens the Record Script File dialog box for selecting the output file and starts to record a sequence of operations.Add Pause: Adds a sleep command to the script. The length of the pause is selected from the submenu.Add Break: Adds a break command to the script.Stop: Stops the recording.</td></tr><tr><td>Continue Script</td><td></td><td>Ctrl+C</td><td>When a break command is encountered in a script, the execution is suspended and user input is possible. This option reactivates the execution of the script.</td></tr><tr><td>Abort Script</td><td></td><td>Ctrl+N</td><td>When script execution is suspended by a break command, this command omits the remaining part of the script.</td></tr></table>

<!-- page:127 -->
# Extensions Menu

Table 12 Extensions menu command 

<table><tr><td>Command</td><td>Toolbar button</td><td>Shortcut keys</td><td>Description</td></tr><tr><td>Two-Port Networks</td><td></td><td>Ctrl+T</td><td>Opens the RF Parameter Extraction dialog box.</td></tr></table>

# Help Menu

Table 13 Help menu command 

<table><tr><td>Command</td><td>Toolbar button</td><td>Shortcut keys</td><td>Description</td></tr><tr><td>About</td><td></td><td>Ctrl+B</td><td>Provides version information.</td></tr></table>

<!-- page:128 -->
A: Elements of User Interface Help Menu

<!-- page:129 -->
This appendix describes known limitations that affect working with Inspect.

# The diff(…formula…) and integr(…formula…) Operators

The diff() and integr() operators require a curve only argument, which can be defined as a curve that contains more than one point, since a curve that contains only one point is treated as a scalar. When a formula is used as an argument for these operators, the parser cannot always decide if the argument curve for the diff() or integr() operators will have more than one point. Therefore, an error message is generated.

For example, to obtain proper results, diff(log10(...formula...)) must be performed in two steps:

1. Create the curve log10(...formula...).   
2. Apply the diff() operator to the resulting curve.

# The vecvalx(…formula…) and vecvaly(…formula…) Operators

It is advisable to compute the curve defined by ...formula... before applying the vecvalx() or vecvaly() operators. In addition, if the curve displays exponential behavior, better results are obtained if the curve is transformed to logarithmic scale before applying these operators.

For example, suppose you want to compute the value:

```txt
vecvalx(diff(<c1>), 1e-7) 
```

and the curve defined by diff(<c1>) has an exponential behavior. In this case, to obtain more precise results, create a curve <c2>, which will be equal to log(diff(<c1>)), and then compute the required value:

```lisp
vecvalx(<c2>, log(1e-7)) 
```

<!-- page:130 -->
# No Support for Right Y-Axes

The Inspector dialog box works only for the x-axis and left y-axis.
