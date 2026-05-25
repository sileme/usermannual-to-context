<!-- page:1 -->
# Utilities User Guide

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
# About This Guide v

Related Publications . .

Conventions

Customer Support . . .

Accessing SolvNet . . .

Contacting Synopsys Support . . . vi

Contacting Your Local TCAD Support Team Directly. . . . vi

# Chapter 1 The datexcodes.txt File 1

File Structure. .

Header . .

Materials .

Variables . . .

Doping Specification . . .

Search Strategy . . . .

# Chapter 2 TCAD Log File Browser 5

Launch the TCAD Log File Browser . . .

User Interface . . .

Table of Contents. .

Active Tags Panel . .

Info Level Selector Panel. .

Main Panel . .

Integration in Sentaurus Workbench. . .

Custom Markups for Sentaurus Process . . .

Custom Color Schemes. . . 10

Limitations . . . 10

# Chapter 3 Sentaurus spice2sdevice Utility 11

HSPICE Netlist Files . .

Comments

Continuation Lines. . . 12

.INCLUDE Statements . 12

Numeric Constants. . . . 12

Parameters and Expressions. . . 13

<!-- page:4 -->
Subcircuits . 14

.MODEL Statements . 15

Elements. . . 17

Netlist Commands . . 18

Command-Line Options . . . 18

Inverter Example. . . . . 19

Subcircuit Example . . . 22

References. . . 23

# Chapter 4 Box Method Utility 25

Usage. . . . 25

Syntax . . . . 25

Definitions. . . 26

Obtuse Element . . . 26

Obtuse Face . . . . 26

Non-Delaunay Element . . . 26

Flat Element . . . 27

Non-Delaunay Measure . . . 27

Tetrahedron Quality . . . . 28

Log Files . . . . . 28

Region Non-Delaunay Elements . . . . 28

Interface Non-Delaunay Elements. . . . 29

Datasets . . . . . 30

EdgesPerVertex and ElementsPerVertex. . . . 30

ElementVolume . . . . 32

AngleElements. . . . 32

AngleVertex. . . . . 34

ShortestEdge . . . . 35

IntersectionNonDelaunayElements . . . . 36

VolumeIntersectionNonDelaunayElements and CoeffIntersectionNonDelaunayElements (Two Dimensions) . . . . 37

ElementsWithCommonObtuseFace. . . . . 38

ElementsWithObtuseFaceOnBoundaryDevice . . . . 38

TetQualityEdge and TetQualityHeight . . . . 40

<!-- page:5 -->
This user guide describes various utilities used by the Synopsys TCAD Sentaurus™ tools.

# Related Publications

For additional information, see:

The TCAD Sentaurus release notes, available on the Synopsys SolvNet® support site (see Accessing SolvNet on page v).   
■ Documentation available on SolvNet at https://solvnet.synopsys.com/DocsOnWeb.

# Conventions

The following conventions are used in Synopsys documentation.

<table><tr><td>Convention</td><td>Description</td></tr><tr><td>Blue text</td><td>Identifies a cross-reference (only on the screen).</td></tr><tr><td>Courier font</td><td>Identifies text that is displayed on the screen or that the user must type. It identifies the names of files, directories, paths, parameters, keywords, and variables.</td></tr><tr><td>Italicized text</td><td>Used for emphasis, the titles of books and journals, and non-English words. It also identifies components of an equation or a formula, a placeholder, or an identifier.</td></tr></table>

# Customer Support

Customer support is available through the Synopsys SolvNet customer support website and by contacting the Synopsys support center.

# Accessing SolvNet

The SolvNet support site includes an electronic knowledge base of technical articles and answers to frequently asked questions about Synopsys tools. The site also gives you access to a wide range of Synopsys online services, which include downloading software, viewing documentation, and entering a call to the Support Center.

<!-- page:6 -->
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

■ support-tcad-us@synopsys.com from within North America and South America   
support-tcad-eu@synopsys.com from within Europe   
support-tcad-ap@synopsys.com from within Asia Pacific (China, Taiwan, Singapore, Malaysia, India, Australia)   
support-tcad-kr@synopsys.com from Korea   
support-tcad-jp@synopsys.com from Japan

<!-- page:7 -->
This chapter describes the datexcodes.txt file.

# File Structure

The datexcodes.txt file is the Synopsys configuration database for materials, doping species, and other quantities that are used in semiconductor process and device simulations. Various TCAD tools refer to the database for different purposes. The file does not contain the physical properties of materials or quantities, but rather configuration properties such as names, colors, and labels.

The file is divided into three sections: header, materials, and variables. Each material in the materials section and each quantity in the variables section are described by several properties that are explained here.

# Header

The first four lines in the datexcodes.txt file constitute the header. The first two lines specify the version number and the file type. The last two lines are strings containing comments. For example:

```csv
DATEX2.1
Datacode
"$Id$"
"Data codes for semiconductor process and device simulation" 
```

# Materials

A material (for example, silicon) can be specified as follows:

```hcl
Silicon {
    label = "Silicon"
    group = Semiconductor
    color = #ffb6c1
    alter1 = Si
    alter2 = 3
} 
```

Table 1 Fields used for material specification 

<table><tr><td>Field</td><td>Description</td></tr><tr><td>alter1</td><td>Name used for translation to and from SUPREM-4a.</td></tr><tr><td>alter2</td><td>Name used for translation to and from SUPREM-4b.</td></tr><tr><td>color</td><td>Color used for display (hexadecimal format for red, green, blue). Default: #b0b0b0</td></tr><tr><td>group</td><td>Material classification. Options are All, Conductor, Insulator, or Semiconductor. Default: All</td></tr><tr><td>label</td><td>Name used for display purposes. Default: Unknown</td></tr></table>

<!-- page:8 -->
You can declare multiple names (or aliases) for a material. For example:

```txt
Vacuum, Gas, Ambient {
...
} 
```

Alternative colors can be listed after the primary color. For example:

```txt
Silicon {
    ...
    color = #ffb6c1, #ac3320, #f18010
} 
```

# Variables

A variable such as ElectrostaticPotential can be specified as follows:

```hcl
ElectrostaticPotential {
    label = "electrostatic potential"
    symbol = "u"
    unit = "V"
    factor = 1.0e+00
    precision = 7
    interpol = linear
    material = All
    alter1 = v
    alter2 = 100
    property("floops") = "Potential"
} 
```

Table 2 Fields used for variable specification 

<table><tr><td>Field</td><td>Description</td></tr><tr><td>alter1</td><td>Name used for translation to and from SUPREM-4a.</td></tr><tr><td>alter2</td><td>Name used for translation to and from SUPREM-4b.</td></tr><tr><td>arsinh</td><td>Scaling factor for arsinh interpolation mode. Default:  $10^{14}$ </td></tr><tr><td>doping</td><td>Specification of doping species (seeDoping Specification on page 4).</td></tr><tr><td>factor</td><td>Scaling factor. Default: 1</td></tr><tr><td>interpol</td><td>Interpolation mode. Options are asinh, linear, or log. Default: linear</td></tr><tr><td>label</td><td>Name used for display purposes. Default: undefined</td></tr><tr><td>material</td><td>Specifies the validity (domain of definition) of this quantity. Options are All, Conductor, Insulator, or Semiconductor. Default: All</td></tr><tr><td>parity</td><td>Symmetry property of tensors, either +1 or -1. Default: +1</td></tr><tr><td>precision</td><td>Number of significant digits (used in graphics tools). Default: 7</td></tr><tr><td>property</td><td>Tool-specific variable properties.</td></tr><tr><td>symbol</td><td>Symbol used for display. Default: ?</td></tr><tr><td>unit</td><td>Unit used for display and data exchange. Default: 1</td></tr></table>

<!-- page:9 -->
You can declare multiple names (or aliases) for a variable. For example:

```txt
BoronConcentration, BoronChemicalConcentration {
    ...
} 
```

The following keywords are also valid for the precision field: half, single, and double.

They correspond to the numeric values of 3, 7, and 14.

The material field can specify multiple materials or material groups. For example:

```txt
material = Semiconductor, Insulator
material = Silicon, PolySilicon, Germanium 
```

<!-- page:10 -->
# Doping Specification

Doping species are identified by the doping field. For example:

```txt
CarbonDoping {
    doping = acceptor (
    active = CarbonActiveDoping
    ionized = CarbonIonizedDoping
    material = GaN
    )
    doping = donor (
    active = CarbonActiveDoping
    ionized = CarbonIonizedDoping
    material = SiliconGermanium, Silicon
    )
} 
```

The doping field indicates whether the variable is an acceptor or a donor. The active field links a chemical doping concentration to its corresponding active doping concentration. Similarly, the ionized field links a chemical doping concentration to its corresponding ionized concentration.

The definition of a doping species can be limited to a list of substrate materials by the material field. By default, a doping species is defined for all substrate materials.

See Sentaurus™ Device User Guide, Specifying Doping Species on page 11 for more information.

# Search Strategy

You can use multiple datexcodes.txt files, in which case, the following search strategy is observed:

\$STROOT/tcad/\$STRELEASE/lib/datexcodes.txt or \$STROOT\_LIB/datexcodes.txt if the environment variable STROOT\_LIB is not defined (lowest priority)   
\$HOME/datexcodes.txt (medium priority)   
datexcodes.txt in local directory (highest priority)

Definitions in later files replace or add to the definitions in the earlier files. In this way, the local file only needs to contain materials or variables that you want to add or modify.

<!-- page:11 -->
This chapter discusses the TCAD Log File Browser.

The TCAD Log File Browser enables you to access information in a TCAD log file efficiently. It displays the structure of the log file content in the form of an interactive Table of Contents, in which you can expand or collapse each subsection to see more details or to have an overview.

# Launch the TCAD Log File Browser

The TCAD Log File Browser is available for log files generated using Sentaurus Process, Sentaurus Interconnect, and Sentaurus Device, Version K-2015.06 or later, if you use the --xml command-line option.

These tools write the version of the file that contains XML-like tags. The marked-up version of the log file has the \*.xml extension.

For example, the following call to Sentaurus Process creates the marked-up log file n1\_fps\_log.xml:

```batch
> sprocess --xml n1_fps.cmd 
```

You can launch the TCAD Log File Browser by entering, for example:

```txt
> logbrowser n1_fps_log.xml 
```

The XML tag information is preprocessed and optimized for efficient display in a browser. The TCAD Log File Browser calls the browser that you selected in the Sentaurus Workbench preferences.

NOTE Depending on the size of the log file and the number of tags it contains, this preprocessing stage might take a few seconds.

During preprocessing, the TCAD Log File Browser provides information about the progress of preprocessing and the action taken. This information is written to the standard output pipe.

If you start the TCAD Log File Browser from the command line of a terminal window, the output is shown in that window. If you start it from Sentaurus Workbench, the output is shown in the terminal window from which you started Sentaurus Workbench (see Integration in Sentaurus Workbench on page 8).

<!-- page:12 -->
You can control the verbosity level of the output during the preprocessing stage with the -info option. The value of this option can be either 0, 1, 2, or 3. For example, to increase the verbosity to level 1, enter on the command line:

```batch
> logbrowser -info 1 n1_fps_log.xml
```

NOTE The -info option controls only the output of the TCAD Log File Browser during preprocessing and does not influence the content of the log file itself.

After preprocessing is completed, your default browser opens automatically. The preprocessed marked-up version of the log file is saved with the \*.html extension. To reload a log file that has been preprocessed already, you can call the browser directly by entering, for example:

```txt
> firefox n1_fps_log.html 
```

# User Interface

The user interface of the TCAD Log File Browser consists of the following areas:

Table of Contents   
■ Active Tags panel   
■ Info Level Selector panel   
Main panel

# Table of Contents

The Table of Contents shows the structure of the log file as a tree of section tags, where each section tag is a button. When you click a section tag button, the log file content corresponding to that section is displayed in the main panel.

If a particular section tag contains other section tags, the ± button is shown to the left of the section tag button and is used to expand or collapse the list of contained section tags.

The number of angle brackets displayed to the left of each section tag button shows the level of containment. All section tags are contained in the root section tag. For a Sentaurus Process log file, this is fpslog. For example, a text block that is part of the log file output of an etch command shows two angle brackets.

When you click a word in the main panel, all section tag buttons leading to sections that contain the clicked word are shown in bold. This allows you to quickly locate the relevant section tags in the Table of Contents.

![](images/utilities_ug_c9d1abae17196f6ed4c20765ef30902b4b175e44a38a867fd82b0c60e6bc30a9.jpg)

<details>
<summary>text_image</summary>

active Tags
bye CONTACT deposit (12) DeviceMesh diffuse (4) EpiWell etch (8) gridqual (48) HEADER implant (32) INITIALIZATION
meshing (48) METAL msg (463) PARAMETERS photo (14) POLY REFINE (5) SAVE SD STI system text (552) warning (3)
Info Level Selector
Info: 0 1 2 ?
fslog
> system
> text
> HEADER
> PARAMETERS
> ± - INITIALIZATION
> ± - EpiWell
> ± - STI
> ± - POLY
> ± - SD
> ± - METAL
> ± - DeviceMesh
> SAVE
> ± - bye
**************************
*** Sentaurus Process ***
*** Version 0-2018.06 ***
*** (1.563, x86_64, Linux) ***
*** Copyright (C) 1993-2002 ***
*** The board of regents of the University of Florida ***
*** Copyright (C) 1994-2018 ***
*** Synopsys, Inc. ***
*** This software and the associated documentation are confidential ***
*** and proprietary to Synopsys, Inc. Your use or disclosure of this ***
*** software is subject to the terms and conditions of a written ***
*** license agreement between you, or your company, and Synopsys, Inc. ***
**************************
Compiled Fri Apr 20 11:55:03 PST 2018 on tcadprod30
Main Panel
Started at: Fri Apr 20 13:48:41 2018 (PDT)
User name: sayed
Host name: tcadpe1
PID: 19701
Architecture: x86_64
Operating system: Linux rel. 2.6.18-274.el5 ver. #1 SMP Fri Jul 7 17:36:59 EDT 2017
Checking syntax of n50_fps.cmd:
</details>

Figure 1 User interface of the TCAD Log File Browser

<!-- page:13 -->
# Active Tags Panel

The Active Tags panel shows an ordered list of all section tags contained in the section tag selected in the Table of Contents. Initially, the selected tag is the root section tag and, therefore, all section tags of the log file are displayed. If a particular section tag is found more than once in the selected section of the log file, the number of instances is shown to the right of the section tag name in parentheses (see Figure 1).

Clicking a section tag button restricts the display in the main panel to only the log file content that belongs to that section tag. You can choose multiple section tags at the same time. Selected buttons become gray. You deselect them by clicking the section tag buttons again.

You can use this feature to view all the mesh quality messages and to find the message that showed a sudden increase in the mesh count. Then, you can click the text in that message to find its location in the Table of Contents, thereby finding which geometric operation triggered this change in mesh.

<!-- page:14 -->
# Info Level Selector Panel

Each section tag is associated with an information level. The buttons of the Info Level Selector panel affect the content shown in the main panel. The buttons allow you to filter out all log file content that belongs to an information level higher than the one noted on the button.

The selector button for a given information level is shown only if the log file contains information tagged for that level.

For example, in Figure 1 on page 7, the button for info level 3 is missing because, in the Sentaurus Process input file, the info level was set to 2 and, therefore, the log file does not contain any information tagged for info level 3.

Clicking the 1 button filters out all content belonging to higher information levels. Clicking the 0 button restores the display to the content for all information levels.

The help (?) button of this panel opens this content.

# Main Panel

The main panel displays the selected sections of the log file. Initially, this panel shows the entire content of the log file, using different foreground and background colors. The background color depends on the information level. For example, all content belonging to info level 0 is black and content belonging to info level 1 is blue.

Specifically marked sections of the log file are displayed with a different background color. For example, for Sentaurus Process, content from the implant command is displayed with a purple background. You can customize the color scheme (see Custom Color Schemes on page 10).

Clicking text in the main panel highlights all section tag buttons that are associated with this text by making the text label bold. This allows you to find out more about the context of specific text in the main panel. For example, if you find log messages from a meshing operation, you might want to know which etch command triggered this remeshing step.

# Integration in Sentaurus Workbench

To use the TCAD Log File Browser in Sentaurus Workbench, you must first activate the --xml option for the respective TCAD tool. For example, open the Tool Properties dialog box for a

<!-- page:15 -->
Sentaurus Process tool instance. On the Tool Properties tab, enter --xml in the Command Line text box.

You can launch the TCAD Log File Browser directly from the Node Explorer of Sentaurus Workbench by double-clicking the \*.xml file.

To reopen already processed log files, double-click the \*.html file.

Cleaning up the nodal output removes both the \*.xml file and the \*.html file.

# Custom Markups for Sentaurus Process

You can add custom section tags to Sentaurus Process log files to mark important processing units such as the gate stack definition or the contact formation.

To insert a main section tag, use the Section command:

```txt
Section tag=<c> [title=<c>] 
```

For example:

```txt
Section tag= EpiWell title= Creation of the Epitaxial Well
...
Section tag= STI 
```

When using the Section command, the section tag terminates automatically when the next section tag is encountered.

To add subsections, use the SubSection.Start command and the SubSection.End command. For example:

```txt
Section tag= EpiWell title= Creation of the Epitaxial Well
...
SubSection.Start tag= REFINE title= Global Refinement
...
SubSection.End tag= REFINE
...
Section tag= STI 
```

Section tags for the main Sentaurus Process commands deposit, diffuse, etch, and implant are added automatically. In addition, important sections containing mesh and grid quality information as well as version and system information are tagged automatically. The Sentaurus Process ending message that contains the CPU runtime report and a summary of all warnings is contained in the bye tag. Warning messages are tagged as warning.

<!-- page:16 -->
All messages sent at information levels other than 0 are contained in msg tags. Log file content that is not otherwise contained in a tag is wrapped in a text tag.

# Custom Color Schemes

To customize the color scheme, copy the cascading style sheet \$STROOT/tcad/ \$STRELEASE/lib/logbrowser/logbrowser.css to your local project directory and edit it as required.

For example, to alter the background color of text tagged with etch to a light gray, change the setting for the background color to:

```css
span.etch {
    background-color: #cccccc;
    display: block; } 
```

# Limitations

The TCAD Log File Browser can visualize log files generated with only Version K-2015.06 (or later versions) of Sentaurus Process, Sentaurus Interconnect, or Sentaurus Device.

The TCAD Log File Browser was designed for Firefox version 3.6.18, the default browser that ships with Red Hat Enterprise Linux v5. It was tested with later versions of Firefox (including versions 16.0 and 33.1.1), Chrome 33.0, and Internet Explorer 11.

NOTE For Internet Explorer 11, the TCAD Log File Browser requires that ActiveX is enabled.

<!-- page:17 -->
This chapter discusses the Sentaurus spice2sdevice utility that converts a subset of Synopsys HSPICE® netlist files into equivalent circuit files of Sentaurus Device.

HSPICE netlist files (extension .cir) are documented in the HSPICE® User Guide: Basic Simulation and Analysis. The circuit files of Sentaurus Device (extension .scf) are discussed in the Sentaurus™ Device User Guide.

NOTE Sentaurus Device also can read HSPICE netlist files directly in the System section. Refer to the Sentaurus™ Device User Guide.

# HSPICE Netlist Files

The first line of a netlist file is assumed to be a title line and is ignored. For example:

.TITLE 'amplifier netlist'

The title line is followed by a sequence of HSPICE statements, and the netlist is terminated by an optional .END statement:

.END

Everything after the final .END statement is ignored.

The command-line option -m must be used if no title line is present (for HSPICE model files).

The netlist parser is case insensitive, except for string literals or file names in .INCLUDE statements. For example:

```txt
.PARAM s = str('This is a case sensitive string.')
.INCLUDE 'Case/Sensitive/Filename' 
```

# Comments

A line starting with either a dollar sign (\$) or an asterisk (\*) is a comment. For example:

\* This is a comment.

<!-- page:18 -->
You can use in-line comments after the dollar sign. For example:

R1 1 2 R=100 \$ drain resistor

# Continuation Lines

Use the plus sign (+) in the first column to indicate a continuation line. For example:

```txt
R1 1 0
+ R=500 
```

# .INCLUDE Statements

Use an .INCLUDE statement to include another netlist in the current netlist. For example:

.INCLUDE models.sp

# Numeric Constants

You can enter numbers in one of the following formats:

■ Integer (for example, 7)   
■ Floating point (for example, -4.5)   
■ Floating point with an integer exponent (for example, 3e8 and -1.2e9)   
■ Integer with a scale factor listed in Table 3 (for example, 6k)   
■ Floating point with a scale factor listed in Table 3 (for example, -8.9meg)

Table 3 Scale factors 

<table><tr><td>Scale factor</td><td>Description</td><td>Multiplying factor</td></tr><tr><td>t</td><td>tera</td><td> $10^{12}$ </td></tr><tr><td>g</td><td>giga</td><td> $10^9$ </td></tr><tr><td>meg or x</td><td>mega</td><td> $10^6$ </td></tr><tr><td>k</td><td>kilo</td><td> $10^3$ </td></tr><tr><td>m</td><td>milli</td><td> $10^{-3}$ </td></tr><tr><td>mil</td><td>one-thousandth of an inch</td><td> $25.4 \cdot 10^{-6}$ </td></tr><tr><td>u</td><td>micro</td><td> $10^{-6}$ </td></tr><tr><td>n</td><td>nano</td><td> $10^{-9}$ </td></tr><tr><td>p</td><td>pico</td><td> $10^{-12}$ </td></tr><tr><td>f</td><td>femto</td><td> $10^{-15}$ </td></tr><tr><td>a</td><td>atto</td><td> $10^{-18}$ </td></tr></table>

<!-- page:19 -->
NOTE The scale factor a is not a scale factor in a character string that contains amps. For example, the expression 20amps is interpreted as 20 amperes of current, not as 20e-18mps.

# Parameters and Expressions

In the HSPICE tool, parameters are names that you associate with a value. Numeric and string parameters are supported. For example:

```python
.PARAM a = 4
.PARAM b = '2*a + 7'
.PARAM s = str('This is a string')
.PARAM t = str(s) 
```

Table 4 Supported built-in mathematical functions 

<table><tr><td>Function</td><td>Description</td></tr><tr><td>sin</td><td>Returns the sine of x (radians).</td></tr><tr><td>cos</td><td>Returns the cosine of x (radians).</td></tr><tr><td>tan</td><td>Returns the tangent of x (radians).</td></tr><tr><td>asin</td><td>Returns the inverse sine of x (radians).</td></tr><tr><td>acos</td><td>Returns the inverse cosine of x (radians).</td></tr><tr><td>atan</td><td>Returns the inverse tangent of x (radians).</td></tr><tr><td>sinh</td><td>Returns the hyperbolic sine of x (radians).</td></tr><tr><td>cosh</td><td>Returns the hyperbolic cosine of x (radians).</td></tr><tr><td>tanh</td><td>Returns the hyperbolic tangent of x (radians).</td></tr><tr><td>abs</td><td>Returns the absolute value of x: |x|.</td></tr><tr><td>sqrt</td><td>Returns the square root of the absolute value of x: sqrt(-x)=-sqrt(|x|).</td></tr><tr><td>pow</td><td>Absolute power. Returns the value of x raised to the integer part of y:  $x^{(integer\ part\ of\ y)}$ .</td></tr><tr><td>pwr</td><td>Signed power. Returns the absolute value of x, raised to the y power, with the sign of x:(sign of x)| $x^y$ .</td></tr><tr><td>log</td><td>Natural logarithm. Returns the natural logarithm of the absolute value of x, with the sign of x: (sign of x) $\log(|x|)$ .</td></tr><tr><td>log10</td><td>Base 10 logarithm. Returns the base 10 logarithm of the absolute value of x, with the sign of x: (sign of x) $\log_{10}(|x|)$ .</td></tr><tr><td>exp</td><td>Exponential. Returns e, raised to the power x:  $e^x$ .</td></tr><tr><td>db</td><td>Decibels. Returns the base 10 logarithm of the absolute value of x, multiplied by 20, with the sign of x: (sign of x) $20\log_{10}(|x|)$ .</td></tr><tr><td>int</td><td>Returns the integer portion of x (which ignores the fractional portion of the number).</td></tr><tr><td>nint</td><td>Rounds x up or down, to the nearest integer.</td></tr><tr><td>sgn sign</td><td>Return sign, as follows:• Returns -1 if x is less than 0.• Returns 0 if x is equal to 0.• Returns 1 if x is greater than 0.</td></tr><tr><td>floor</td><td>Rounds down to the nearest integer (ignores the fractional part of the number).</td></tr><tr><td>ceil</td><td>Rounds up to the nearest integer (ignores the fractional part of the number).</td></tr><tr><td>min</td><td>Smaller of two arguments. Returns the numeric minimum of x and y.</td></tr><tr><td>max</td><td>Larger of two arguments. Returns the numeric maximum of x and y.</td></tr></table>

<!-- page:20 -->
# Subcircuits

Reusable cells can be specified as subcircuits. The general definition is given by:

.SUBCKT name n1 n2 ... [param1=val] [param2=val] ...

.ENDS

or:

.MACRO name n1 n2 ... [param1=val] [param2=val] ...

.EOM

String parameters are also supported:

.SUBCKT name n1 n2 ... [param=str('string')] ...

.ENDS

Examples   
```txt
.PARAM P5=5 P2=10
.SUBCKT SUB1 1 2 P4=4
R1 1 0 P4
R2 2 0 P5
X1 1 2 SUB2 P6=7
X2 1 2 SUB2
.ENDS
.MACRO SUB2 1 2 P6=11
R1 1 2 P6
R2 2 0 P2
.EOM
X1 1 2 SUB1 P4=6
X2 3 4 SUB2 P6=15 
```

<!-- page:21 -->
# .MODEL Statements

The .MODEL statement has the following general syntax:

.MODEL model\_name type [level=num] [pname1=val1] [pname2=val2] ...

Table 5 Supported model types 

<table><tr><td>Type</td><td>Description</td><td>Type</td><td>Description</td></tr><tr><td>c</td><td>Capacitor model</td><td>npn</td><td>NPN BJT model</td></tr><tr><td>csw</td><td>Current-controlled switch</td><td>pjf</td><td>P-channel JFET model</td></tr><tr><td>d</td><td>Diode model</td><td>pmf</td><td>P-channel MESFET</td></tr><tr><td>l</td><td>Mutual inductor model</td><td>pmos</td><td>P-channel MOSFET model</td></tr><tr><td>njf</td><td>N-channel JFET model</td><td>pnp</td><td>PNP BJT model</td></tr><tr><td>nmf</td><td>N-channel MESFET</td><td>r</td><td>Resistor model</td></tr><tr><td>nmos</td><td>N-channel MOSFET model</td><td>sw</td><td>Voltage-controlled switch</td></tr></table>

Examples   
```txt
.MODEL mod1 NPN BF=50 IS=1e-13 VFB=50 PJ=3 N=1.05
.MODEL mod2 PMOS LEVEL=72
+ aigbinv = 0.0111
+ at = -0.00156 
```

<!-- page:22 -->
Table 6 lists the values for the parameter level in recognized MOSFET models. In the case of Levels 1, 2, and 3, the corresponding device can be either an HSPICE MOSFET (HMOS\_L1, HMOS\_L2, or HMOS\_L3) or a Berkeley SPICE MOSFET (Mos1, Mos2, or Mos3). By default, the Sentaurus spice2sdevice utility selects an HSPICE MOSFET, but you can use the command-line option -b to switch to a Berkeley SPICE MOSFET.

Table 6 Supported SPICE MOSFET models 

<table><tr><td>Level</td><td>Device</td><td>Description</td></tr><tr><td>1</td><td>HMOS_L1 or Mos1</td><td>Shichman-Hodges</td></tr><tr><td>2</td><td>HMOS_L2 or Mos2</td><td>Grove-Frohman</td></tr><tr><td>3</td><td>HMOS_L3 or Mos3</td><td>Empirical model</td></tr><tr><td>4</td><td>BSIM1</td><td>BSIM</td></tr><tr><td>5</td><td>BSIM2</td><td>BSIM2</td></tr><tr><td>6</td><td>Mos6</td><td>MOS6</td></tr><tr><td>8</td><td>BSIM3</td><td>BSIM3</td></tr><tr><td>9</td><td>B3SOI</td><td>Partially depleted SOI MOSFET model</td></tr><tr><td>14</td><td>BSIM4</td><td>BSIM4</td></tr><tr><td>28</td><td>HMOS_L28</td><td>Modified BSIM model</td></tr><tr><td>49</td><td>HMOS_L49</td><td>BSIM3v3 MOS model</td></tr><tr><td>53</td><td>HMOS_L53</td><td>BSIM3v3 MOS model</td></tr><tr><td>54</td><td>HMOS_L54</td><td>BSIM4 model</td></tr><tr><td>57</td><td>HMOS_L57</td><td>UC Berkeley BSIM3-SOI model</td></tr><tr><td>59</td><td>HMOS_L59</td><td>UC Berkeley BSIM3-SOI fully depleted (FD) model</td></tr><tr><td>61</td><td>HMOS_L61</td><td>RPI a-Si TFT model</td></tr><tr><td>62</td><td>HMOS_L62</td><td>RPI Poly-Si TFT model</td></tr><tr><td>64</td><td>HMOS_L64</td><td>STARC HiSIM model</td></tr><tr><td>68</td><td>HMOS_L68</td><td>STARC HiSIM2 model</td></tr><tr><td>69</td><td>HMOS_L69</td><td>PSP100 DFM support series model</td></tr><tr><td>72</td><td>HMOS_L72</td><td>BSIM-CMG multigate MOSFET model</td></tr><tr><td>73</td><td>HMOS_L73</td><td>STARC HiSIM-LDMOS/HiSIM-HV model</td></tr><tr><td>76</td><td>HMOS_L76</td><td>LETI-UTSOI MOSFET model</td></tr></table>

<!-- page:23 -->
# Elements

Element names must begin with a specific letter for each element type.

Table 7 Supported HSPICE element types 

<table><tr><td>First letter</td><td>Element</td><td>Example</td></tr><tr><td>c</td><td>Capacitor</td><td>Cbypass 1 0 10pf</td></tr><tr><td>d</td><td>Diode</td><td>D7 3 9 D1</td></tr><tr><td>e</td><td>Voltage-controlled voltage source</td><td>Ea 1 2 3 4 K</td></tr><tr><td>f</td><td>Current-controlled current source</td><td>Fsub n1 n2 vin 2.0</td></tr><tr><td>g</td><td>Voltage-controlled current source</td><td>G12 4 0 3 0 10</td></tr><tr><td>h</td><td>Current-controlled voltage source</td><td>H3 4 5 Vout 2.0</td></tr><tr><td>i</td><td>Current source</td><td>IA 2 6 1e-6</td></tr><tr><td>j</td><td>JFET or MESFET</td><td>J1 7 2 3 model_jfet w=10u l=10u</td></tr><tr><td>k</td><td>Linear mutual inductor</td><td>K1 L1 L2 0.98</td></tr><tr><td>l</td><td>Linear inductor</td><td>Lx a b 1e-9</td></tr><tr><td>m</td><td>MOS transistor</td><td>M834 1 2 3 4 N1</td></tr><tr><td>q</td><td>Bipolar transistor</td><td>Q5 3 6 7 8 pnp1</td></tr><tr><td>r</td><td>Resistor</td><td>R10 21 10 1000</td></tr><tr><td>v</td><td>Voltage source</td><td>V1 8 0 5</td></tr><tr><td>x</td><td>Subcircuit call</td><td>X1 2 4 17 31 MULTI WN=100 LN=5</td></tr></table>

Table 8 Supported Berkeley SPICE element types [1] 

<table><tr><td>First letter</td><td>Element</td><td>Example</td></tr><tr><td>s</td><td>Voltage-controlled switch</td><td>S1 1 2 3 4 SWITCH1 ON</td></tr><tr><td>w</td><td>Current-controlled switch</td><td>W1 1 2 VCLOCK SWITCHMOD1</td></tr><tr><td>z</td><td>GaAs MESFET</td><td>Z1 7 2 3 ZM1 AREA=2</td></tr></table>

<!-- page:24 -->
# Netlist Commands

A limited set of netlist commands is recognized.

To make node names global across all subcircuits, use a .GLOBAL statement. For example:

.GLOBAL node1 node2 node3 ...

Use the .OPTION PARHIER statement to specify scoping rules. For example:

.OPTION PARHIER=GLOBAL|LOCAL

Other HSPICE netlist commands that have not been already mentioned explicitly are ignored.

# Command-Line Options

Table 9 lists the command-line options of the Sentaurus spice2sdevice utility.

Table 9 Command-line options 

<table><tr><td>Option</td><td>Description</td></tr><tr><td>-b</td><td>Use Berkeley SPICE models instead of HSPICE (applies only to MOSFETs Level 1, 2, and 3).</td></tr><tr><td>-c</td><td>Translates a SPICE circuit file (default).</td></tr><tr><td>-d</td><td>Prints additional debug information.</td></tr><tr><td>-h</td><td>Displays a help message.</td></tr><tr><td>-m</td><td>Translates a SPICE model file.</td></tr><tr><td>-o filename</td><td>Stores the Sentaurus Device circuit file in filename.</td></tr><tr><td>-v</td><td>Shows version information.</td></tr></table>

A SPICE model file is assumed to have no title line. Otherwise, it is identical to a SPICE circuit file.

<!-- page:25 -->
# Inverter Example

This example considers a simple resistor transistor logic (RTL) inverter as shown in Figure 2.

![](images/utilities_ug_48edc84d914dfbf6bf9e298abb3985a273fed73c8f6e145e477ee66240b3e113.jpg)

<details>
<summary>text_image</summary>

1
2
3
4
0
</details>

Figure 2 Simple RTL inverter

This circuit can be described by the following SPICE circuit file (rtl.cir):

```asm
SIMPLE RTL INVERTER
VCC 4 0 5
VIN 1 0 PULSE 0 5 2NS 2NS 2NS 30NS 100NS
RB 1 2 10K
Q1 3 2 0 Q1
RC 3 4 1K
.PLOT DC V(3)
.PLOT TRAN V(3) (0,5)
.PRINT TRAN V(3)
.MODEL Q1 NPN BF 20 RB 100 TF .1NS CJC 2PF
.DC VIN 0 5 0.1
.TRAN 1NS 100NS
.END 
```

The following command:

```batch
spice2sdevice -o rtl.scf rtl.cir 
```

produces the following output file (rtl.scf):

```txt
PSET q1
DEVICE BJT
PARAMETERS
bf = 20
cjc = 2e-12
npn = 1
pnp = 0
rb = 100
tf = 1e-10
END PSET 
```

3: Sentaurus spice2sdevice Utility Inverter Example   
```txt
INSTANCE q1
    PSET q1
    ELECTRODES
    3 2 0 0
    PARAMETERS
END INSTANCE

INSTANCE rb
    PSET Resistor_pset
    ELECTRODES
    1 2
    PARAMETERS
    resistance = 10000
END INSTANCE

INSTANCE rc
    PSET Resistor_pset
    ELECTRODES
    3 4
    PARAMETERS
    resistance = 1000
END INSTANCE

INSTANCE vcc
    PSET Vsource_pset
    ELECTRODES
    4 0
    PARAMETERS
    dc = 5
END INSTANCE

INSTANCE vin
    PSET Vsource_pset
    ELECTRODES
    1 0
    PARAMETERS
    pulse = [0 5 2e-09 2e-09 2e-09 3e-08 1e-07]
END INSTANCE 
```

<!-- page:27 -->
The following command file of Sentaurus Device can then be used to perform a transient simulation:

```hcl
File {
    SpicePath = "."
}

System {
    Plot "rtl.plt" (time() v(1) v(3))
}

Solve {
    Set (vcc."dc" = 0)

    Quasistationary (Goal {Parameter=vcc."dc" Value=5})
    { Coupled { Circuit } }

    NewCurrentPrefix = "new_"

    Transient (InitialTime=0 FinalTime=100e-9
    InitialStep=1e-9 MaxStep=1e-9)
    { Coupled { Circuit } }
} 
```

Figure 3 shows the voltages and as a function of time.v1 v3   
![](images/utilities_ug_9d2b96b90105a8e51514569418e1194d33bc80b5d22392f61fa43dab2a61a260.jpg)

<details>
<summary>line</summary>

| Time     | v(1) | v(3) |
| -------- | ---- | ---- |
| 0        | 5.0  | 0.0  |
| 2e-08    | 5.0  | 0.0  |
| 4e-08    | 0.0  | 0.0  |
| 6e-08    | 0.0  | 3.0  |
| 8e-08    | 0.0  | 5.0  |
| 1e-07    | 0.0  | 5.0  |
</details>

Figure 3 Transient simulation of a simple RTL inverter

<!-- page:28 -->
# Subcircuit Example

The Sentaurus spice2sdevice utility supports basic SPICE subcircuits. This example considers a chain of low-pass filters as shown in Figure 4.

![](images/utilities_ug_655f4689eb149b0d851b0aaad438be879995d9bcca01d91d35dc53c185bc6959.jpg)

<details>
<summary>text_image</summary>

in
R 1 R 2 R out
Vin C C C
0
</details>

Figure 4 Sample chain of low-pass filters

The following SPICE command file analyzes the transient response of this network to a pulse signal (file filter.sp):

```txt
low-pass filter
.subckt filter 1 2 g
r1 1 2 100
c1 2 g 5n
.ends
    vin in 0 pulse (0 5 1u 0.5u 0.5u 1u 4u)
    x1 in 1 0 filter
    x2 1 2 0 filter
    x3 2 out 0 filter
    .tran 10n 12u
    .print tran v(in) v(1) v(2) v(out)
.end 
```

To run the same simulation in Sentaurus Device, an equivalent .scf circuit file must be generated (file filter.scf). For example:

```batch
spice2sdevice -o filter.scf filter.sp 
```

The following Sentaurus Device command file then performs the same transient simulation as the previous SPICE command file:

```hcl
File {
    Output = "filter"
    SPICEPath = "."
} 
```

```swift
System {
    Plot "filter_des.plt" (time() v(in) v(1) v(2) v(out))
}

Solve {
    Transient (InitialTime = 0 FinalTime = 12u
    InitialStep = 10n MaxStep = 10n MinStep = 1n) {
    Coupled { Circuit }
    }
} 
```

Figure 5 shows the resulting voltages $\nu _ { \mathrm { i n } } , \nu _ { 1 } , \nu _ { 2 }$ , and $\nu _ { \mathrm { o u t } }$ as a function of time.   
![](images/utilities_ug_4d464b3d30906acfea13da0609f96933a9fa74ef366c6e159e614525f2c7419f.jpg)

<details>
<summary>line</summary>

| Time     | v(in) | v(1) | v(2) | v(out) |
| -------- | ----- | ---- | ---- | ------ |
| 0        | 4.0   | 0.0  | 0.0  | 0.0    |
| 5e-06    | 4.0   | 3.5  | 2.5  | 1.5    |
| 1e-05    | 4.0   | 3.5  | 2.5  | 2.0    |
</details>

Figure 5 Transient simulation of a low-pass filter

<!-- page:29 -->
# References

[1] T. Quarles et al., SPICE 3 Version 3F5 User’s Manual, Department of Electrical Engineering and Computer Sciences, University of California, Berkeley, CA, USA, 1994.

<!-- page:30 -->
3: Sentaurus spice2sdevice Utility References

<!-- page:31 -->
This chapter describes the box method utility.

# Usage

The box method utility analyzes the quality of a mesh. It reads a TDR mesh and reports various measures for the mesh quality. The result is a TDR data file that contains mesh information (for example, GridFile\_bxm.tdr).

There are two versions of this utility:

■ Double precision (boxmethod)   
Long double precision (boxmethodl)

The boxmethodl version computes the box method parameters with long double precision, after which the data is converted to double precision, and the output TDR file contains only double precision information.

# Syntax

The syntax of the box method utility is one of the following:

boxmethod [options] GridFile

boxmethodl [options] GridFile

Here, GridFile is a TDR file. The available options are:

```txt
-a Algorithm Algorithm can be one of the following:
    • AverageBoxMethod
    • CVPL_AverageBoxMethod (default)
    • MaterialBoundaryTruncatedVoronoiBox
    • RegionBoundaryTruncatedVoronoiBox
    • TruncatedVoronoiBox

-h Show this help message and exit

-NoGas Without computation in Gas

-numThreads n Parallel computation where n is the number of threads (default: 1) 
```

<!-- page:32 -->
-StackSize n Parallel computation where n is the size of the stack (default: 0)

-v Print header with version number

For detailed descriptions, see Sentaurus™ Device User Guide, Chapter 36 on page 1003.

# Definitions

The following sections provide definitions of basic elements.

# Obtuse Element

An element is obtuse if the center of the circumsphere (circumcircle) is outside this element.

# Obtuse Face

Let Pf be the plane that contains the face f of an element. Each plane splits 3D space into two half-spaces Sf1 and Sf2. A face f is obtuse if the center of the circumsphere of the element and the element itself lie in different half-spaces Sf1 and Sf2.

NOTE In the 2D case, an obtuse triangle has only one obtuse edge. In the 3D case:

• An obtuse prism has only one obtuse face.   
• An obtuse tetrahedron has one or two obtuse faces.   
• An obtuse pyramid has one, two, or three obtuse faces.

# Non-Delaunay Element

An obtuse element is non-Delaunay if the interior of the circumsphere (circumcircle) around this element contains another mesh vertex.

<!-- page:33 -->
# Flat Element

Let ${ \bf { \alpha } } _ { i }$ be an angle between faces for edge (in the 2D case, between edges for vertex ). Ani i element is $f l a t$ if for all angles (a tetrahedron has six angles) $\alpha _ { i } < { 1 0 } ^ { - 8 }$ (the angle is close to zero) or $\alpha _ { i } > \pi - 1 0 ^ { - 8 }$ (the angle is close to ).π

# Non-Delaunay Measure

Figure 6 shows the following elements of a non-Delaunay measure:

■ $V _ { 1 , 2 }$ is the Voronoï center (center of circumcircle) of elements $T _ { 1 , 2 }$   
$h _ { 1 }$ is the height of $T _ { 1 }$ .   
$T _ { 1 }$ is the non-Delaunay element.   
$T _ { 2 }$ is the Delaunay element.

![](images/utilities_ug_76608c50d19ef4b7ceeca930d10cc4d40fa5191330c5649ed362718e11d332f6.jpg)

<details>
<summary>text_image</summary>

0
2
h₁
Element T₁(0,1,2)
v₂
d₁
V₁
1
Element T₂(0,3,1)
3
</details>

Figure 6 Schematic of a non-Delaunay measure

There are three definitions of a non-Delaunay measure:

1. $\delta _ { 1 } = d _ { 1 } = \mathrm { L e n g t h } ( V _ { \mathrm { 1 } } , V _ { \mathrm { 2 } } ) , [ \mu \mathrm { m } ]$ . For Delaunay element $T _ { 2 }$ , the value is $d _ { 2 } = 0$ .   
2. $\delta _ { 2 } = \frac { \mathrm { A r e a } ( 0 , V _ { 1 } , 1 , V _ { 2 } , 0 ) } { \mathrm { A r e a } ( T _ { 1 } ) } = \frac { d _ { 1 } } { h _ { 1 } }$ . In the 3D case, Area = Volume.   
3. For 2D only, $\delta _ { 3 } = \frac { d _ { 1 } } { \mathrm { L e n g t h } ( 0 , 1 ) }$ , delta of coefficients for obtuse edge (0,1).

<!-- page:34 -->
The Area $( 0 , V _ { 1 } , 1 , V _ { 2 } , 0 )$ is called the non-Delaunay volume for element $T _ { 1 }$ . A non-Delaunay measure is defined for each element. In this example, for Delaunay element $T _ { 2 }$ , the value is $d _ { 2 } = 0$ , which means all non-Delaunay measures $\delta _ { k }$ are equal to zero.

# Tetrahedron Quality

The box method utility has the following tetrahedron (triangle) quality criteria:

$\mathtt { T e t Q u a l i t y E d g e } = \frac { \mathtt { R } } { \mathrm { L } _ { \operatorname* { m i n } } }$   
$\mathtt { T e t Q u a l i t y H e i g h t } = \frac { \mathtt { R } } { \mathtt { H } _ { \operatorname* { m i n } } }$ Hmin

Here, R is the radius of a circumscribed sphere (a circle in two dimensions) around an element, $\mathrm { L } _ { \mathrm { m i n } }$ is the length of the shortest edge of an element, and $\mathrm { H } _ { \mathrm { m i n } }$ is the shortest height of an element.

The box method utility saves the maximum values of TetQualityEdge and TetQualityHeight in the log file.

# Log Files

This section describes the content of log files.

# Region Non-Delaunay Elements

A log file contains common data about the mesh and information about non-Delaunay elements per region (for Delaunay mesh DeltaVolume=0 and non-DelaunayVolume=0).

For example: 

<table><tr><td colspan="8">Region non-Delaunay elements</td></tr><tr><td>Region name</td><td>Volume [um2]</td><td>BoxMethodVolume [um2]</td><td>DeltaVolume [%]</td><td>Elements</td><td>non-Delaunay Elements</td><td>non-DelaunayVolume [um2]</td><td>[%]</td></tr><tr><td>Nitride</td><td>1.9500000e-04</td><td>2.2635574e-04</td><td>16.080</td><td>53</td><td>12 (22.64 %)</td><td>1.8215e-04</td><td>(1.1e-05)</td></tr><tr><td>Oxide</td><td>6.0618645e-03</td><td>8.0705629e-03</td><td>33.137</td><td>2500</td><td>818 (32.72 %)</td><td>2.3715e-04</td><td>(2.0e-04)</td></tr><tr><td>Silicon</td><td>3.5548100e-02</td><td>4.9531996e-02</td><td>39.338</td><td>12656</td><td>5057 (39.96 %)</td><td>1.0715e-04</td><td>(1.0e-05)</td></tr><tr><td>Total</td><td>4.6402113e-02</td><td>6.4934852e-02</td><td>39.939</td><td>16550</td><td>6383 (38.57 %)</td><td>2.9218e-04</td><td>(2.1e-05)</td></tr></table>

<!-- page:35 -->
# Interface Non-Delaunay Elements

An interface element is an element that has a face (or an edge in two dimensions) lying on the interface. A non-Delaunay element is an interface non-Delaunay element only if its obtuse face lies on the surface of the interface (see Figure 7).

In Figure 7, the elements 2, 3, and 4 are non-Delaunay elements, but only element 3 is an interface non-Delaunay element (that is, only this element has an obtuse edge that lies on the surface of the interface).

![](images/utilities_ug_656b3b3a3fc3aee33fc36e0d155b28529da6b881c3fbdc67f008c0e96b4eeba0.jpg)

<details>
<summary>text_image</summary>

1
2
3
4
5
6
Oxide
Silicon
</details>

Figure 7 Blue (1, 2, 3) and green (4, 5, 6) elements are oxide and silicon interface elements, respectively

The following example is a log file for interface non-Delaunay elements:

<table><tr><td colspan="5">Interface non-Delaunay elements</td></tr><tr><td>Region1</td><td>Elements</td><td>non-Delaunay Elements</td><td>Volume [um2]</td><td>non-Delaunay DeltaVolume [um2]</td></tr><tr><td>silicon</td><td>3</td><td>0 ( 0.00 %)</td><td>1.5775139e-03</td><td>0.0000000e+00 ( 0.00 %)</td></tr><tr><td>oxide</td><td>3</td><td>1 ( 33.0 %)</td><td>1.6776069e-03</td><td>0.1100000e-03 ( 0.10 %)</td></tr><tr><td>Total</td><td>6</td><td>1 ( 16.0 %)</td><td>3.6951838e-02</td><td>0.1100000e+00 ( 0.05 %)</td></tr></table>

<!-- page:36 -->
# Datasets

This section describes datasets that are vertex based and defined on all regions. The examples consider the mesh information for a given vertex v.

# EdgesPerVertex and ElementsPerVertex

For the example in Figure 8, the dataset value is:

```txt
EdgesPerVertex(v) = ElementsPerVertex(v) = 5 
```

![](images/utilities_ug_442edb249ff3241ddd4a1379414723bcf28d244f21aa22a7c76947240088aa2a.jpg)

<details>
<summary>text_image</summary>

T₃
T₂
v
T₄
T₁
T₅
</details>

Figure 8 Triangular elements around vertex v

If vertex v lies on the boundary of a device, then (in the 2D case only, see Figure 9 and Figure 10 on page 31):

```javascript
EdgesPerVertex(v) = ElementsPerVertex(v) + 1 
```

The interface edges are additional and are defined in Regions with the parameter:

```txt
"material = Interface" 
```

If there are interface edges, these edges are added to the list of EdgesPerVertex. For example, if there are interface edges between elements $T _ { 1 } , T _ { 2 }$ and $T _ { 3 } , T _ { 4 }$ , then:

```javascript
EdgesPerVertex(v) = 7, ElementsPerVertex(v) = 5 
```

<!-- page:37 -->
The examples in Figure 9 and Figure 10 show distribution edges and elements per vertex, respectively. Only the boundary values differ.

![](images/utilities_ug_bcf0cc09a9c6797d7fafa4f98c88fa9b2cf981d6b0e9a3f8923c740c896e2660.jpg)

<details>
<summary>heatmap</summary>

| X\Y | 0    | 5    | 10   | 15   |
|-----|------|------|------|------|
| 0   | 3.000e+00 | 4.333e+00 | 5.667e+00 | 6.333e+00 |
| 5   | 3.000e+00 | 4.333e+00 | 5.667e+00 | 6.333e+00 |
| 10  | 3.000e+00 | 4.333e+00 | 5.667e+00 | 6.333e+00 |
| 15  | 3.000e+00 | 4.333e+00 | 5.667e+00 | 6.333e+00 |
| 20  | 3.000e+00 | 4.333e+00 | 5.667e+00 | 6.333e+00 |
| 25  | 3.000e+00 | 4.333e+00 | 5.667e+00 | 6.333e+00 |
| 30  | 3.000e+00 | 4.333e+00 | 5.667e+00 | 6.333e+00 |
| 35  | 3.000e+00 | 4.333e+00 | 5.667e+00 | 6.333e+00 |
| 40  | 3.000e+00 | 4.333e+00 | 5.667e+00 | 6.333e+00 |
| 45  | 3.000e+00 | 4.333e+00 | 5.667e+00 | 6.333e+00 |
| 50  | 3.000e+00 | 4.333e+00 | 5.667e+00 | 6.333e+00 |
| 55  | 3.000e+00 | 4.333e+00 | 5.667e+00 | 6.333e+00 |
| 60  | 3.000e+00 | 4.333e+00 | 5.667e+00 | 6.333e+00 |
| 65  | 3.000e+00 | 4.333e+00 | 5.667e+00 | 6.333e+00 |
| 70  | 3.000e+00 | 4.333e+00 | 5.667e+00 | 6.333e+00 |
| 75  | 3.000e+00 | 4.333e+00 | 5.667e+00 | 6.333e+00 |
| 80  | 3.000e+00 | 4.333e+00 | 5.667e+00 | 6.333e+00 |
| 85  | 3.000e+00 | 4.333e+00 | 5.667e+00 | 6.333e+00 |
| 90  | 3.000e+00 | 4.333e+00 | 5.667e+00 | 6.333e+00 |
| 95  | 3.000e+00 | 4.333e+00 | 5.667e+00 | 6.333e+00 |
|1    | -    | -    | -    | -    |
| X=5, Y=1    | -    | -    | -    | -    |
| X=12, Y=12, X=12, Y=12, X=15, Y=15, X=2    | -    | -    | -    | -    |
| X=2, Y=2, X=2, Y=2, X=2, X=2, X=2, X=2, X=2, X=2, X=2, X=2, X=2, X=2, X=2, X=2, X=2, X=2, X=2, X=2, X=2, X=2, X=2, X=2, X=2, X=2, X=2, X=2, X=2, N/A    |
| X=5, Y=5, X=5, Y=5, X=5, X=5, X=5, X=5, X=5, X=5, X=5, X=5, X=5, X=5, X=5, X=5, X=5, X=5, X=5, X=5, X=5, X=5, X=5, X=5, X=5, X=5, X=5, X=5, X=5, N/A    |
| X=12, Y=12, X=12, Y=12, X=12, Y=12, X=12, Y=12, X=12, Y=12, X=12, Y=12, X=12, Y=12, X=12, Y=12, X=12, Y=12, X=12, Y=12, N/A    |
| X=18, Y=18, X=18, Y=18, X=18, Y=18, X=18, Y=18, X=18, Y=18, X=18, Y=18, X=18, Y=18, X=18, Y=18, N/A    |
| X[2] = [X,Y], [X,Y], [X,Y], [X,Y], [X,Y], [X,Y], [X,Y], [X,Y], [X,Y], [X,Y], [X,Y], [X,Y], [X,Y], [X,Y], [X,Y], [X,Y], [X,Y], [X,Y], [X,Y], [X,Y], [X,Y], [X,Y], [X,Y], [X,Y], [X,Y], [X,Y] , [X,Y] , [X,Y] , [X,Y] , [X,Y] , [X,Y] , [X,Y] , [X,Y] , [X,Y] , [X,Y] , [X,Y] , [X,Y] , [X,Y] , [X,Y] , [X,Y] , [X,Y] , [X,Y] , [X,Y] , [X,Y] , [X,Y] , [X,Y] . , [X,Y] , [X,Y] , [X,Y] , [X,Y] , [X,Y] , [X,Y] , [X,Y] , [X,Y] , [X,Y] , [X,Y] , [X,Y] , [X,Y] , [X,Y] , [X,Y] , [X,Y] , [X,Y] , [X,Y] , [X,Y] , [X,Y] , [X,Y]\ , [X,Y] , [X,Y] , [X,Y] , [X,Y] , [X,Y] , [X,Y] , [X,Y] , [X,Y] , [X,Y] , [X,Y] , [X,Y] , [X,Y] , [X,Y] , [X,Y] , [X,Y] , [X,Y] , [X,Y] , [X,Y] , [X,Y] , [X,Y][N,A]
The chart displays a single data series with values ranging from approximately -7 to +7 for each vertex and axis labels (Y,X) are provided in the code format.
</details>

Figure 9 Example of EdgesPerVertex

![](images/utilities_ug_50160ec7e140172bd8f98c0dd566178679d479d612ca5a714378aeecf4792189.jpg)  
Figure 10 Example of ElementsPerVertex

<!-- page:38 -->
# ElementVolume

This dataset has location=element.

![](images/utilities_ug_63ca843d79e8bbdb3f86232c9cbac0778e2b0fbb8e0119ec8ae041494768cfc8.jpg)

<details>
<summary>heatmap</summary>

| X\Y | 0    | 5    | 10   | 15   |
|-----|------|------|------|------|
| 0   | 1.600e+01 | 1.342e+01 | 1.083e+01 | 8.250e+00 |
| 5   | 1.600e+01 | 1.342e+01 | 1.083e+01 | 8.250e+00 |
| 10  | 1.600e+01 | 1.342e+01 | 1.083e+01 | 8.250e+00 |
| 15  | 1.600e+01 | 1.342e+01 | 1.083e+01 | 8.250e+00 |
| 20  | 1.600e+01 | 1.342e+01 | 1.083e+01 | 8.250e+00 |
| 25  | 1.600e+01 | 1.342e+01 | 1.083e+01 | 8.250e+00 |
| 30  | 1.600e+01 | 1.342e+01 | 1.083e+01 | 8.250e+00 |
| 35  | 1.600e+01 | 1.342e+01 | 1.083e+01 | 8.250e+00 |
| 40  | 1.600e+01 | 1.342e+01 | 1.083e+01 | 8.250e+00 |
| 45  | 1.600e+01 | 1.342e+01 | 1.083e+01 | 8.250e+00 |
| 50  | 1.600e+01 | 1.342e+01 | 1.083e+01 | 8.250e+00 |
| 55  | 1.600e+01 | 1.342e+01 | 1.083e+01 | 8.250e+00 |
| 60  | 1.600e+01 | 1.342e+01 | 1.083e+01 | 8.250e+00 |
| 65  | 1.600e+01 | 1.342e+01 | 1.083e+01 | 8.250e+00 |
| 70  | 1.600e+01 | 1.342e+01 | 1.083e+01 | 8.250e+00 |
| 75  | 1.600e+01 | 1.342e+01 | 1.083e+01 | 8.250e+00 |
| 80  | 1.600e+01 | 1.342e+01 | 1.083e+01 | 8.250e+00 |
| 85  | 1.600e+01 | 1.342e+01 | 1.083e+01 | 8.250e+00 |
| 90  | 1.600e+01 | 1.342e+01 | 1.083e+01 | 8.250e+00 |
| 95  | 1.600e+01 | 1.342e+01 | 1.083e+01 | 8.250e+00 |
| 100 | 1.600e+01 | 1.342e+01 | 1.083e+01 | 8.250e+00 |
| 165 | -    | -    | -    | -    |
| 225 | -    | -    | -    | -    |
| 275 | -    | -    | -    | -    |
| 325 | -    | -    | -    | -    |
| 375 | -    | -    | -    | -    |
| 425 | -    | -    | -    | -    |
| 475 | -    | -    | -    | -    |
| 525 | -    | -    | -    | -    |
| 575 | -    | -    | -    | -    |
| 625 | -    | -    | -    | -    |
| 675 | -    | -    | -    | -    |
| 725 | -    | -    | -    | -    |
| 775 | -    | -    | -    | -    |
| 825 | -    | -    | -    | -    |
| 875 | -    | -    | -    | -    |
| 925 | -    | -    | -    | -    |
| 975 | -    | -    | -    | -    |
| Note: The Y-axis label is 'Y' and the X-axis label is 'X'. The color legend indicates 'ElementVolume [μm³]' with values ranging from ~5.667e-01 to ~5.999e-01 for the color scale.
</details>

Figure 11 Example of ElementVolume

# AngleElements

Let $\alpha _ { i }$ be an angle between faces for edge (in the 2D case, between edges for vertex ). Thei i angle of element has the following definition:T

$$
\operatorname{Angle} (T) = \frac {1 8 0}{\pi} \cdot \operatorname{asin} (\max (\sin (\alpha_ {i}))) \tag {1}
$$

For example, the angle of triangle has the value:T

$$
\operatorname{Angle} (T) = \frac {1 8 0}{\pi} \cdot \operatorname{asin} (\max (\sin (\alpha_ {1}), \sin (\alpha_ {2}), \sin (\alpha_ {3}))) \tag {2}
$$

![](images/utilities_ug_363efc235af2bcf5c8ded2ea52b0fdc64ba9340b8092e0cf6b0371647770769b.jpg)

<details>
<summary>text_image</summary>

α₁
α₃
α₂
</details>

Element T

<!-- page:39 -->
For the dataset AngleElements:

■ If the element has a right angle, then ${ \mathrm { A n g l e } } ( T ) = 9 0 ^ { \circ }$ .   
■ In the 2D case, if ${ \mathrm { A n g l e } } ( T ) < 6 0 ^ { \circ }$ , then this triangle is obtuse:

$$
\alpha_ {1}, \alpha_ {2} <   \operatorname{Angle} (T) \quad \alpha_ {3} > 1 8 0 - \operatorname{Angle} (T) \tag {3}
$$

■ If $\mathrm { A n g l e } ( T ) < 1 0 ^ { - 8 }$ , then this element is flat (see Definitions on page 26).

The dataset AngleElements has location=element.

![](images/utilities_ug_3039b5874b1d017ced657f51e29c9a52d1ff7b21f0295c4e56347a02798ff880.jpg)  
Figure 12 Example of AngleElements

<!-- page:40 -->
# AngleVertex

The dataset AngleVertex has the following definition (see Figure 13):

$$
\text { AngleVertex } (v) = \max (\text { Alpha } (T k, v)), k = 1, \dots , n b E l e m e n t s (v)
$$

Here, nbElements(v) is equal to the number of elements per vertex v, and Alpha(Tk,v) corresponds to the element–vertex angle.

In Figure 13, the AngleVertex dataset shows a poor vertex of the mesh as a red vertex.

![](images/utilities_ug_33a81e6ad274ae3050f72301093d91a410fbf33d0e6cdd1b887ecde5cf8a6a80.jpg)

<details>
<summary>heatmap</summary>

| X\Y | 0    | 5    | 10   | 15   |
|-----|------|------|------|------|
| 0   | 4.500e+01 | 6.307e+01 | 8.114e+01 | 9.922e+01 |
| 5   | 4.500e+01 | 6.307e+01 | 8.114e+01 | 9.922e+01 |
| 10  | 4.500e+01 | 6.307e+01 | 8.114e+01 | 9.922e+01 |
| 15  | 4.500e+01 | 6.307e+01 | 8.114e+01 | 9.922e+01 |
| 20  | 4.500e+01 | 6.307e+01 | 8.114e+01 | 9.922e+01 |
| 25  | 4.500e+01 | 6.307e+01 | 8.114e+01 | 9.922e+01 |
| 30  | 4.500e+01 | 6.307e+01 | 8.114e+01 | 9.922e+01 |
| 35  | 4.500e+01 | 6.307e+01 | 8.114e+01 | 9.922e+01 |
| 40  | 4.500e+01 | 6.307e+01 | 8.114e+01 | 9.922e+01 |
| 45  | 4.500e+01 | 6.307e+01 | 8.114e+01 | 9.922e+01 |
| 50  | 4.500e+01 | 6.307e+01 | 8.114e+01 | 9.922e+01 |
| 55  | 4.500e+01 | 6.307e+01 | 8.114e+01 | 9.922e+01 |
| 60  | 4.500e+01 | 6.307e+01 | 8.114e+01 | 9.922e+01 |
| 65  | 4.500e+01 | 6.307e+01 | 8.114e+01 | 9.922e+01 |
| 70  | 4.500e+01 | 6.307e+01 | 8.114e+01 | 9.922e+01 |
| 75  | 4.500e+01 | 6.307e+01 | 8.114e+01 | 9.922e+01 |
| 80  | 4.500e+01 | 6.307e+01 | 8.114e+01 | 9.922e+01 |
| 85  | 4.500e+01 | 6.307e+01 | 8.114e+01 | 9.922e+01 |
| 90  | 4.500e+01 | 6.307e+01 | 8.114e+01 | 9.922e+01 |
| 95  | 4.500e+01 | 6.307e+01 | 8.114e+01 | 9.922e+01 |
| 100 | 4.500e+01 | 6.307e+01 | 8.114e+01 | 9.922e+01 |
| 165 | -    | -    | -    | -    |
| 235 | -    | -    | -    | -    |
| 325 | -    | -    | -    | -    |
| 425 | -    | -    | -    | -    |
| 525 | -    | -    | -    | -    |
| 625 | -    | -    | -    | -    |
| 725 | -    | -    | -    | -    |
| 825 | -    | -    | -    | -    |
| 925 | -    | -    | -    | -    |
| 135 | -    | -    | -    | -    |
| 225 | -    | -    | -    | -    |
| Note: The y-axis label 'Y' and x-axis label 'X' are not explicitly provided in the image, so they are not included in the data table for this example. The y-axis label 'Y' and x-axis label 'X' are estimated based on the grid lines used in the heatmap.
</details>

Figure 13 Example of AngleVertex

<!-- page:41 -->
# ShortestEdge

The dataset ShortestEdge has the following definition:

```txt
ShortestEdge(v) = min(Length(Edge_k)), k=1,...,nbEdges(v) 
```

Here, nbEdges(v) is equal to the number of edges per vertex v. The unit of ShortestEdge is . μm

![](images/utilities_ug_4df2a79dc57573e4dbd2b5776040ffd696abd0fd80f3e261953e4ae5d49652d7.jpg)

<details>
<summary>heatmap</summary>

| X  | Y  | ShortestEdge [µm] |
|----|----|-------------------|
| 0  | 0  | 1.000e+00         |
| 5  | 5  | 1.579e+00         |
| 10 | 10 | 2.157e+00         |
| 15 | 15 | 2.736e+00         |
| 20 | 20 | 3.315e+00         |
| 25 | 25 | 3.893e+00         |
| 30 | 30 | 4.472e+00         |
</details>

Figure 14 Example of ShortestEdge

<!-- page:42 -->
# IntersectionNonDelaunayElements

This dataset has location=element. It is equal to $\delta _ { 1 } ( T )$ (see Definitions on page 26).

Figure 15 shows a mesh that contains seven non-Delaunay elements.   
![](images/utilities_ug_ed214dd2a39d61825c5fba0bdcf28e3e79d195ea63b25fe36a9dcbebda115f6a.jpg)

<details>
<summary>heatmap</summary>

| X\Y | 0    | 5    | 10   | 15   | 20   |
|-----|------|------|------|------|------|
| 0   | 0.000e+00 | 0.000e+00 | 0.000e+00 | 0.000e+00 | 0.000e+00 |
| 5   | 0.000e+00 | 0.000e+00 | 0.000e+00 | 0.000e+00 | 0.000e+00 |
| 10  | 0.000e+00 | 0.000e+00 | 5.590e-01 | 1.677e+00 | 2.236e+00 |
| 15  | 3.354e+00 | 2.795e+00 | 1.118e+00 | 5.590e-01 | 2.236e+00 |
| 20  | 3.354e+00 | 2.795e+00 | 1.118e+00 | 5.590e-01 | 2.236e+00 |
| 25  | 3.354e+00 | 2.795e+00 | 1.118e+00 | 5.590e-01 | 2.236e+00 |
The chart displays a color-coded legend for each element value, but no explicit numerical data is plotted; the color values are estimated based on the scale of the pixel intensity. The grid structure is a mesh representation of the pixel intensity distribution.
</details>

Figure 15 Example of IntersectionNonDelaunayElements

# VolumeIntersectionNonDelaunayElements and CoeffIntersectionNonDelaunayElements (Two Dimensions)

<!-- page:43 -->
The difference between these datasets and the IntersectionNonDelaunayElements dataset (see IntersectionNonDelaunayElements on page 36) is the value of the non-Delaunay measures $\delta _ { 2 } ( T )$ and $\delta _ { 3 } ( T )$ , instead of $\delta _ { 1 } ( T )$ (see Definitions on page 26).

![](images/utilities_ug_8d9337096e6e2587d811b7f4d050b5ceff99e91d2d4c5bc12870964ab15118e5.jpg)

<details>
<summary>heatmap</summary>

| X\Y | 0    | 5    | 10   | 15   | 20   |
|-----|------|------|------|------|------|
| 0   | 0.000e+00 | 0.000e+00 | 0.000e+00 | 0.000e+00 | 0.000e+00 |
| 5   | 0.000e+00 | 0.000e+00 | 0.000e+00 | 0.000e+00 | 0.000e+00 |
| 10  | 0.000e+00 | 0.000e+00 | 0.000e+00 | 0.000e+00 | 0.000e+00 |
| 15  | 7.500e-01 | 6.250e-01 | 5.000e-01 | 3.750e-01 | 2.500e-01 |
| 20  | 7.500e-01 | 6.250e-01 | 5.000e-01 | 3.750e-01 | 2.500e-01 |
| 25  | 7.500e-01 | 6.250e-01 | 5.000e-01 | 3.750e-01 | 2.500e-01 |
</details>

Figure 16 Example of CoeffIntersectionNonDelaunayElements

<!-- page:44 -->
# ElementsWithCommonObtuseFace

This dataset is similar to the VolumeIntersectionNonDelaunayElements dataset. The value of this dataset is positive only for a pair of neighbor elements with a common obtuse face.

In the 2D case, Face is Edge. Figure 17 shows two elements with a common obtuse edge.

![](images/utilities_ug_b1d151cb306b74a6f7669493aa72a5bce346f571b47ad03341e20293804c2e13.jpg)

<details>
<summary>heatmap</summary>

| X    | Y    | ElementsWithCommonObtuseFace [1] |
|------|------|-----------------------------------|
| 15   | 10   | 3.125e+00                         |
| 15   | 15   | 3.125e+00                         |
| 15   | 20   | 3.125e+00                         |
| 15   | 25   | 3.125e+00                         |
| 15   | 30   | 3.125e+00                         |
| 15   | 35   | 3.125e+00                         |
| 15   | 40   | 3.125e+00                         |
| 15   | 45   | 3.125e+00                         |
| 15   | 50   | 3.125e+00                         |
| 15   | 55   | 3.125e+00                         |
| 15   | 60   | 3.125e+00                         |
| 15   | 65   | 3.125e+00                         |
| 15   | 70   | 3.125e+00                         |
| 15   | 75   | 3.125e+00                         |
| 15   | 80   | 3.125e+00                         |
| 15   | 85   | 3.125e+00                         |
| 15   | 90   | 3.125e+00                         |
| 15   | 95   | 3.125e+00                         |
| 15   | 100  | 3.125e+00                         |
| 15   | 105  | 3.125e+00                         |
| 15   | 110  | 3.125e+00                         |
| 15   | 115  | 3.125e+00                         |
| 15   | 120  | 3.125e+00                         |
| 15   | 125  | 3.125e+00                         |
| 15   | 130  | 3.125e+00                         |
| 15   | 135  | 3.125e+00                         |
| 15   | 140  | 3.125e+00                         |
| 15   | 145  | 3.125e+00                         |
| 15   | 150  | 3.125e+00                         |
| 16   | 16   | 3.125e+00                         |
| 16   | 17   | 3.125e+00                         |
| 16   | 18   | 3.125e+00                         |
| 16   | 19   | 3.125e+00                         |
| 16   | 20   | 3.125e+00                         |
| 16   | 21   | 3.125e+00                         |
| 16   | 22   | 3.125e+00                         |
| 16   | 23   | 3.125e+00                         |
| 16   | 24   | 3.125e+00                         |
| 16   | 25   | 3.125e+00                         |
| 16   | 26   | 3.125e+00                         |
| 16   | 27   | 3.125e+00                         |
| 16   | 28   | 3.125e+00                         |
| 16   | 29   | 3.125e+00                         |
| 16   | 30   | 3.125e+00                         |
| 16   | 31   | 3.125e+00                         |
| 16   | 32   | 3.125e+00                         |
| 16   | 33   | 3.125e+00                         |
| 16   | 34   | 3.125e+00                         |
| 16   | 35   | 3.125e+00                         |
| 16   | 36   | 3.125e+00                         |
| 16   | 37   | 3.125e+00                         |
| 16   | 38   | 3.125e+00                         |
| 16   | 39   | 3.125e+00                         |
| 16   | 40   | 3.125e+00                         |
| 17   | -    | -                                 |
| -    | -    | -                                 |
| -    | -    | -                                 |
| -    | -    | -                                 |
| -    | -    | -                                 |
| -    | -    | -                                 |
| -    | -    | -                                 |
| -    | -    | -                                 |
| -    | -    | -                                 |
| -    | -    | -                                 |
| -    | -    | -                                 |
| -     | -    | -                                 |
| -    | -    | -                                 |
| -    | -    | -                                 |
| -    | -    | -                                 |
| -    | -    | -                                 |
| -    | -    | -                                 |
| -    | -    | -                                 |
| -    | -    | -                                 |
| -    | -    | -                                 |
| -    | -    | -                                 |
| -      | -    | -                                 |
| -    | -    | -                                 |
| -    | -    | -                                 |
| -    | -    | -                                 |
| -    | -    | -                                 |
| -    | -    | -                                 |
| -    | -    | -                                 |
| -    | -    | -                                 |
| -    | -    | -                                 |
| -    | -    | -                                 |
| -        | -    | -                                 |
| -    | -    | -                                 |
| -    | -    | -                                 |
| -    | -    | -                                 |
| -    | -    | -                                 |
| -    | -    | -                                 |
| -    | -    | -                                 |
| -    | -    | -                                 |
| -    | -    | -                                 |
| -    | -    | -                                 |
| -       | -    | -                                 |
| -     | -    | -                                 |
| -     | -    | -                                 |
| -     | -    | -                                 |
| -     | -    | -                                 |
| -     | -    | -                                 |
| -     | -    | -                                 |
| -     | -    | -                                 |
| -     | -    | -                                 |
| -     | -    | -                                 |
| ... (additional elements) are not provided in the code image.)
</details>

Figure 17 Example of ElementsWithCommonObtuseFace

# ElementsWithObtuseFaceOnBoundaryDevice

This dataset has nonzero values only for elements that have an obtuse face on the boundary of the device. For these elements, the non-Delaunay measure is defined as (see Figure 18δ( ) T on page 39):

$$
\delta (T) = \frac {\text { Area } (0 , V , 1 , 0)}{\text { Area } (T)} = \frac {d}{h}, \text {   in   the   3D   case,   Area   =   Volume } \tag {4}
$$

The value of the dataset is equal to:

ElementsWithObtuseFaceOnBoundaryDevice(v) = $\mathfrak { m a x } ( \delta ( T _ { k } ) )$ , k=1,...,nbElements(v)

![](images/utilities_ug_eb21c7cd1082baeb60de3e483a618874cba165cee672b6a538e26b7b822e1cda.jpg)

<details>
<summary>text_image</summary>

2
h
Element T
0
d
1
V – Voronoi Center of Element T
</details>

Figure 18 Non-Delaunay measure for element with obtuse face on boundary device

Figure 19 shows one element with an obtuse edge on the boundary device.   
![](images/utilities_ug_6030aab72826f670f654c839c40683f4cbaafb0f4526c6983cf375c754026b13.jpg)

<details>
<summary>heatmap</summary>

| X  | Y  | ElementsWithObtuseFaceOnBoundaryDevice [1] |
|----|----|---------------------------------------------|
| 0  | 0  | 0.000e+0                                    |
| 5  | 5  | 0.000e+0                                    |
| 10 | 10 | 0.000e+0                                    |
| 15 | 15 | 0.000e+0                                    |
| 20 | 20 | 0.000e+0                                    |
</details>

Figure 19 Example of ElementsWithObtuseFaceOnBoundaryDevice

<!-- page:46 -->
# TetQualityEdge and TetQualityHeight

These datasets have location=element (see Definitions on page 26).

![](images/utilities_ug_0f11bfe6046874f42941352c1bcf62e0ade6a67e49497ec6483e8aeebb11c363.jpg)  
Figure 20 Examples of (left) TetQualityEdge and (right) TetQualityHeight
