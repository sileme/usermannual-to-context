<!-- page:1 -->
# Calibration Kit User Guide

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
# About This Guide v

Related Publications . .

Conventions

Customer Support . . .

Accessing SolvNet. . . vi

Contacting Synopsys Support . . . vi

Contacting Your Local TCAD Support Team Directly. . . . vi

# Chapter 1 Introduction to the Calibration Kit 1

Functionality of the Calibration Kit

Input Modules . . .

Calibration Libraries .

Process Directory . . . .

Experiment Directory . . . .

Preference Directory. . . .

Calibration Files. . .

Advanced Calibration for Sentaurus Process . . .

Advanced Calibration for Sentaurus Process Kinetic Monte Carlo . . . . .

Structure of Calibration Kit Projects. . . .

Sentaurus Process . . .

Sentaurus Mesh (Optional) .

Sentaurus Device (Optional) . . .

Inspect . . . . 8

Sentaurus Visual

# Chapter 2 Working With Calibration Kit Projects 9

Manipulating Calibration Kit Projects . . .

Creating a New Project or a New Scenario for an Existing Project . . . .

Creating a New Scenario for a Project. . . . 13

Creating a New Short-Loop Experiment . . . 14

Creating a New Parameterized Project . . . 1

Creating a New Project for Optimization . . . . 20

Editing Variables . . . . . 25

Visualizing Project Files . . . . . 26

Viewing Process Files . . . . 26

Viewing Profile Files . . . . . 27

<!-- page:4 -->
Viewing Visualization Files. . . . . 27

Confidentiality Warning . . . . 28

# Chapter 3 Calibration Library, Process Searches, and Profiles 29

Experiment Database: Calibration Library . . . . 29

Process File Syntax . . . . 29

Restrictions on Sentaurus Process Syntax . . . . 29

Process Searches . . . . . . 30

Syntax of the QPS List File . . . . . . 30

Database Process Search . . . 31

Calibration Project Process Search . . . . 32

Profiles . . . 33

Visualizing Profiles . . . . . 33

Comparing Profile Curves . . . . . 33

Relative Logarithmic Square Difference . . . . 34

Relative Linear Square Difference . . . . 35

Arithmetic Mean of Relative Error. . . . . 35

Quadratic Mean of Relative Error . . . . . 35

<!-- page:5 -->
The Calibration Kit is the calibration environment that is part of Synopsys Sentaurus™ Workbench Advanced. The Calibration Kit is the interface to the calibration libraries and calibration files.

# Related Publications

For additional information, see:

The documentation installed with the Calibration Kit software package and available from the Help menu of the Calibration Kit.   
The TCAD Sentaurus release notes, available on the Synopsys SolvNet® support site (see Accessing SolvNet on page vi).   
■ Documentation available on SolvNet at https://solvnet.synopsys.com/DocsOnWeb.

# Conventions

The following conventions are used in Synopsys documentation.

<table><tr><td>Convention</td><td>Description</td></tr><tr><td>Blue text</td><td>Identifies a cross-reference (only on the screen).</td></tr><tr><td>Bold text</td><td>Identifies a selectable icon, button, menu, or tab. It also indicates the name of a field or an option.</td></tr><tr><td>Courier font</td><td>Identifies text that is displayed on the screen or that the user must type. It identifies the names of files, directories, paths, parameters, keywords, and variables.</td></tr><tr><td>Italicized text</td><td>Used for emphasis, the titles of books and journals, and non-English words. It also identifies components of an equation or a formula, a placeholder, or an identifier.</td></tr><tr><td>Menu &gt; Command</td><td>Indicates a menu command, for example, File &gt; New (from the File menu, select New).</td></tr></table>

# Customer Support

Customer support is available through the Synopsys SolvNet customer support website and by contacting the Synopsys support center.

<!-- page:6 -->
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

<!-- page:7 -->
This chapter presents an overview of the Calibration Kit.

# Functionality of the Calibration Kit

The Calibration Kit extends the functionality of Sentaurus Workbench, with which you can perform efficient 1D calibrations of the Synopsys process simulators Sentaurus Process and Sentaurus Process Kinetic Monte Carlo.

Sentaurus Workbench is the primary graphical front end of TCAD Sentaurus that integrates the simulation tools into one environment (see the Sentaurus™ Workbench User Guide). The Sentaurus Workbench Advanced mode provides customized calibration viewers and wizards. The Calibration menu of Sentaurus Workbench also includes wizards for manipulating simulation flows and generating reports (see Chapter 2 on page 9).

Using calibration libraries containing secondary ion mass spectrometry (SIMS) data, the Calibration Kit provides a fast and accurate method of evaluating and optimizing process conditions. It allows a predictive analysis of the influence of process equipment parameters on electrical device data. In addition, the Calibration Kit helps you to understand the sensitivity of processes to various control parameters, enabling you to optimize equipment operation quickly.

The Calibration Kit is the calibration environment in Sentaurus Workbench Advanced. It serves as a database browser and a simulation and project manager.

The Optimizer tool, which is integrated in Sentaurus Workbench Advanced, is used for the automatic analysis and optimization of process and calibration parameters (see the Optimizer User Guide).

In addition to the analytic extraction in the process simulators, Sentaurus Device can be integrated for electrical parameter extraction, preceded by Sentaurus Mesh for mesh generation.

For visualization, Inspect and Sentaurus Visual are integrated into the Calibration Kit.

<!-- page:8 -->
# Input Modules

Process descriptions and data, which are calibration libraries such as the Calibration Library, and simulator calibration files such as Advanced Calibration are used as input to the Calibration Kit.

# Calibration Libraries

Calibration libraries are experiment databases consisting of the following directories:

processes \*   
experiments   
preferences

You can add your own experimental data to the measurement database or create your own database. In the latter case, it is recommended to keep the same directory structure, with process files, profile files, and preference files in three directories (see Experiment Database: Calibration Library on page 29).

In general, process recipes use the Sentaurus Process syntax, with specific restrictions for the Calibration Kit (see Restrictions on Sentaurus Process Syntax on page 29). The experiments directory can contain SIMS profiles and spreading resistance profiles.

# Process Directory

In the processes\_\* directory, each process file contains a recipe for wafer processing and a reference to the corresponding SIMS measurements. By default, these recipes are written in Sentaurus Process syntax. In this case, the directory is called processes\_sp.

The file name of the process is the same as the name of the process. The input files of Sentaurus Process are created automatically before simulation by copying the recipes and by extending the pure recipes with simulation models. For Sentaurus Process, calibration parameters and models are sourced before a process recipe is applied.

In the process files, SIMS measurements are represented by insert statements. The insert statement is translated to the Calibration Kit–specific SetPltList statement for Sentaurus Process. Each SetPltList statement specifies the measured chemical dopant species and the file name of the SIMS profile. A process file can have several SetPltList statements, which correspond to several SIMS profiles.

<!-- page:9 -->
In a Sentaurus Workbench project generated by the Calibration Kit, the file names of process flows change to b@node@\_fps.cmd, where @node@ is the number of a project node of Sentaurus Workbench. See Structure of Calibration Kit Projects on page 5.

# Experiment Directory

The experiments directory contains the measured SIMS profiles in xy format. The first column is the depth [nm] and the second column is the concentration of the chemical dopant [ ]. File names match the names specified in the 1D commands of the recipe files.cm–3

In a Sentaurus Workbench project generated by the Calibration Kit, SIMS profiles are named b@node@\_[profile].plx, where @node@ is the number of a project node of Sentaurus Workbench. See Structure of Calibration Kit Projects on page 5.

# Preference Directory

The preferences directory contains additional information. For each SIMS profile name.sims in the experiments directory, there is one preference file name\_sims.prf in the preferences directory that specifies the following (Tcl) variables:

sims\_xmin and sims\_xmax give the depth [nm] range for which the SIMS profile should be compared to the simulation results.   
vis\_xmin and vis\_xmax are the preferred minimal depth [nm] and maximal depth [nm], respectively, to be shown in a graphical representation of the profile.   
vis\_ymin and vis\_ymax are the preferred minimal concentration [ ] and maximalcm–3 concentration [ ], respectively, to be shown in a graphical representation of the profile.cm–3   
probe\_xmax gives the depth [nm] of the contact for device simulation to calculate the sheet resistance.

In a Sentaurus Workbench project generated by the Calibration Kit, all preference files are named b@node@\_[profile].prf, where @node@ is the number of a project node of Sentaurus Workbench. See Structure of Calibration Kit Projects on page 5.

# Calibration Files

The directory \$STROOT/tcad/\$STRELEASE/lib/fabpackagelib contains calibration (text) files with physical models and parameters for Sentaurus Process and Sentaurus Process Kinetic Monte Carlo.

# Advanced Calibration for Sentaurus Process

<!-- page:10 -->
Two files in the fabpackagelib directory are used for calibrated 1D simulations of Sentaurus Process with the Calibration Kit: AdvCal\_2018.06.fps and calib\_1d\_2018.06.fps.

The file AdvCal\_2018.06.fps is the latest version of Advanced Calibration for Sentaurus Process. It contains a selection of physical models and parameters that are calibrated for deepsubmicron technology. This file is identical to the AdvCal\_2018.06.fps file in the directory \$STROOT/tcad/\$STRELEASE/lib/sprocess/TclLib/AdvCal.

NOTE When improvements to the model calibration are made, between feature releases, the file in the fabpackagelib directory will contain the latest version. The contents of the AdvCal\_2018.06.fps file are explained in the Advanced Calibration for Process Simulation User Guide, which can be accessed from Sentaurus Workbench (choose Help > Manuals).

The file calib\_1d\_2018.06.fps contains information needed for simulations, which does not belong to the process flow or the physical models, and includes:

■ The creation of a 1D simulation mesh, which is optimized for accurate 1D simulations   
■ A procedure (WritePlt) definition for writing 1D profiles in .plt format   
■ A procedure (OxideThickness) definition for extracting the cap-oxide thickness   
■ A selection of meshing parameters

The last lines of the calib\_1d\_2018.06.fps file create a 1D mesh and source the file AdvCal\_2018.06.fps, which contains the physical models.

NOTE Older versions of the calibration files are available in the directory \$STROOT/tcad/\$STRELEASE/lib/fabpackagelib and can be used with the latest release of Sentaurus Process.

# Advanced Calibration for Sentaurus Process Kinetic Monte Carlo

Two files in the fabpackagelib directory are used for calibrated pseudo-1D simulations of Sentaurus Process Kinetic Monte Carlo (Sentaurus Process KMC) with the Calibration Kit: AdvCal\_KMC\_2018.06.fps and calib\_KMC\_2018.06.fps.

The file AdvCal\_KMC\_2018.06.fps is the latest version of Advanced Calibration for Sentaurus Process KMC. It contains a selection of physical models and parameters that are calibrated for deep-submicron technology. This file is identical to the AdvCal\_KMC\_2018.06.fps file in the directory \$STROOT/tcad/\$STRELEASE/lib/ sprocess/TclLib/AdvCal.

<!-- page:11 -->
The file calib\_KMC\_2018.06.fps contains information needed for simulations, which does not belong to the process flow or the physical models, and includes:

The creation of a 3D atomistic simulation cell and a 1D projection mesh, which is optimized for accurate pseudo-1D simulations   
A procedure (WritePlt) definition for writing 1D profiles in .plt format and for logging the thickness of the amorphous layer   
■ A selection of recording options for atomistic data   
■ A selection of atomistic parameters

The last lines of the calib\_KMC\_2018.06.fps file create the simulation cell, select the atomistic mode, and source the file AdvCal\_KMC\_2018.06.fps, which contains the physical models.

# Structure of Calibration Kit Projects

A Calibration Kit project is a special type of Sentaurus Workbench project with either three or five tools, and one to seven parameters. Both traditional and hierarchical project organizations are supported. For details about Sentaurus Workbench and its general project structure, see the Sentaurus™ Workbench User Guide.

Figure 1 shows an example of a Calibration Kit project. The first tool instance in the tool flow is Sentaurus Process for process simulation. Optionally, a Sentaurus Mesh tool instance can be used for mesh generation and a Sentaurus Device tool instance can be used for device simulation. The Inspect tool instance for variable value extraction is followed by Sentaurus Visual for visualization.

![](images/calikit_ug_fd41b5d74716d6283cf75cefe65cbe22d2e7303f022f3207b4662cd4ae58e8a9.jpg)

<details>
<summary>text_image</summary>

/remote/ch10tcad1/testDB/Calibration_Example (Runtime Mode : Editable) - SWB
Project Edit Scheduler View Scenario Tool Parameter Experiments Nodes Variables Optimization Calibration PCM Studio Extensions Help
Scenario: all
Projects
remote/ch10tcad1/testDB
Calibration_Example
Project Scheduler
SPROCESS INSPECT VISUAL
nr process process_info calibration
1 2 -- -- Example_Process_As As 5keV 1e15 7/0 calib_1d.fps
2 5 -- -- Example_Process_B B 5keV 1e15 7/0 calib_1d.fps
3 8 -- -- Example_Process_As As 5keV 1e15 7/0 calib_1d.fps
4 11 -- -- Example_Process_B B 5keV 1e15 7/0 calib_1d.fps
Edit mode none queued ready pending running done failed aborted virtual pruned folded
</details>

Figure 1 Calibration Kit project loaded in Sentaurus Workbench; tool flow is horizontal and experiment flow is vertical

<!-- page:12 -->
The nr parameter of Sentaurus Process represents the index of the process. Each experiment has a unique process recipe. The process file-naming convention is b@nr@\_fps.cmd for Sentaurus Process. In general, files starting with b@nr@\_\* belong to the experiment of the parameter value @nr@.

The Calibration Kit uses different Sentaurus Workbench variables:

process names the process recipe.   
process\_info lists process information.   
1 n\_profile shows the number of profiles per experiment, which are named by the variables profile\_@integer@, where integer is equal to 1, 2, 3, …, 10.

For each profile, the file b@nr@\_@{profile\_@integer@}@.plx contains the experiment data, and the file b@nr@\_@{profile\_@integer@}@.prf contains the preferences.

To identify a Sentaurus Workbench project as a Calibration Kit project, an empty hidden file .fabpackage is included in the project directory. You can use the greadme.txt file (choose Project > Readme) to collect project information.

# Sentaurus Process

The project structure is the same for Sentaurus Process in continuum mode or in kinetic Monte Carlo mode. The mode is defined in the calibration files.

Sentaurus Process uses the command file n@node@\_fps.cmd as input. This command file sources the calibration file @calibration@ of Sentaurus Process, evaluates the nr parameter for each experiment, and sources the process recipe b@nr@\_fps.cmd. Therefore, the nr parameter of Sentaurus Process represents the process.

The output of the Sentaurus Process tool instance is the following files:

■ b@nr@\_@{profile\_@integer@}@\_simulation.plt (xy plot file)   
b@nr@\_fps.tdr (TDR file)   
b@nr@\_bnd.tdr (TDR boundary file)

Therefore, the file name of the simulated profile (the xy plot file b@nr@\_@{profile\_@integer@}@\_simulation.plt) differs only from the file name of the measured profile (the b@nr@\_@{profile\_@integer@}@.plx file) in its file extension.

The Sentaurus Process tool instance defines the variables process, process\_info, calibration, n\_profile, and profile\_@integer@. Sentaurus Process can also have a second parameter (see Creating a New Parameterized Project on page 17).

<!-- page:13 -->
Sentaurus Process is called with the command-line option -n to switch off the syntax check.

Optionally, you can extract the sheet resistance analytically using the Sentaurus Process command SheetResistance, and the result is transferred to the Sentaurus Workbench variable Rs\_fps.

For Sentaurus Process KMC, you can store atomistic information using the following command:

kmc extract tdrWrite

# Sentaurus Mesh (Optional)

Sentaurus Mesh is used for the mesh generation of a 2D device simulation. For the calculation of sheet resistance, a 2D device is defined to represent the sheet of an ultrashallow junction of a transistor. The device definition is taken from the output files b@nr@\_fps.tdr and b@nr@\_bnd.tdr of Sentaurus Process.

The geometry is described by the following variables defined for Sentaurus Mesh:

■ x\_sheet defines the length [ ] of the sheet (default is 20 ).μm μm   
■ y\_sheet defines the depth [ ] of the sheet.μm   
■ y0\_sheet defines the top position [ ] of the sheet.μm   
■ y\_contact defines the depth [ ] of the contacts.μm   
■ y0\_contact defines the top position [ ] of the contacts.μm

The n@node@\_msh.tdr file stores doping and grid information.

# Sentaurus Device (Optional)

Sentaurus Device performs a 2D device simulation on the sheet defined in the n@node|mesh@\_msh.tdr file. The voltage and the total current distribution of the sheet are computed for a voltage of 0.01 V between the left and right contacts. The results are saved in the n@node@\_des.plt file. Sentaurus Device uses the default parameters for silicon, germanium, and SiGe from files by specifying the DefaultParametersFromFile flag in the global Physics section of the command file. The optional parameter file of Sentaurus Device is named sdevice.par.

<!-- page:14 -->
# Inspect

Inspect calculates the sheet resistance and the curve differences. Inspect takes the voltage and the total current distribution from the n@node|sdevice@\_des.plt file and calculates the sheet resistance. The Sentaurus Workbench variable Rs\_sim stores the results. You can compare the extracted value with experimental data for some experiments. The variable Rs\_exp, which is defined by Sentaurus Process, retains the measured value or is set to zero if no measurement value is present.

For each profile pair, Inspect computes the difference between the measured profile and the simulated profile, that is, between b@nr@\_@{profile\_@integer@}@.plx and b@nr@\_@{profile\_@integer@}@\_simulation.plt.

Different methodologies are available for this curve comparison (see Comparing Profile Curves on page 33). The variables cv\_delta\_@integer@, where integer is equal to 1, 2, 3, …, 10, hold the extracted curve difference per for profile\_@integer@.μm

You can view profiles in interactive mode. If you want to save the visualization in the Inspect format, this must be performed manually.

Optionally, a spline-based curve-smoothing (a smooth, piecewise, polynomial approximation) is applied to the measured profile or the simulated profile for curve comparison.

See Viewing Profile Files on page 27.

# Sentaurus Visual

Sentaurus Visual visualizes all measured and simulated profiles of a process in one xy plot. For each node, Sentaurus Visual takes all profiles (b@nr@\_@{profile\_@integer@}@.plx and b@nr@\_@{profile\_@integer@}@\_simulation.plt), the curve comparison results (cv\_delta\_@integer@), and the preferences (b@nr@\_@{profile\_@integer@}@.prf), and creates a Sentaurus Visual Tcl script n@node@\_vis\_out.tcl for customized xy plot visualization.

All profiles of the experiment are plotted on top of each other. The curve comparison results cv\_delta\_@integer@ are listed next to the curve label of the corresponding simulated profile. The borders of the curve comparison of the last profile pair are drawn in dashed style.

See Viewing Visualization Files on page 27.

<!-- page:15 -->
This chapter describes how to work with Calibration Kit projects.

# Manipulating Calibration Kit Projects

You can manipulate a Calibration Kit project like other Sentaurus Workbench projects (for details about editing projects, see the Sentaurus™ Workbench User Guide). However, you can use special Calibration Kit wizards to guide you through project creation and extension, scenario and experiment generation, and parameterization.

It is faster and more thorough to manipulate projects using these wizards rather than the standard features of Sentaurus Workbench. The wizards are available from the Calibration menu of Sentaurus Workbench.

NOTE The Calibration menu is shown only in Sentaurus Workbench Advanced mode.

![](images/calikit_ug_80233a81246a9b941940e76da1644968a9dd865ac0ca896c4fd3c92c6f5c988b.jpg)

<details>
<summary>text_image</summary>

Optimization
Calibration
Extensions
Help
Project Wizard...
Scenario Wizard...
Process Wizard...
Parameter Wizard...
Optimization Wizard...
</details>

Figure 2 Wizards available from the Calibration menu

NOTE Renumbering nodes of a Calibration Kit project can lead to a reduction of functionality. It is strongly advised not to renumber nodes.

# Creating a New Project or a New Scenario for an Existing Project

You can create a new Calibration Kit project or extend an existing project by adding a new scenario.

<!-- page:16 -->
To create a new Calibration Kit project or to add a new scenario to an existing project:

1. Choose Calibration > Project Wizard.

The Project Wizard opens.

2. Click Next to start.   
3. Select the calibration library database from the following options:

• Calibration Library is the default experiment database of the Calibration Kit.   
User Library is a user-specified database in either Sentaurus Process syntax or TSUPREM-4 syntax. If you select this option, you must specify the process, experiment, and preference directories, and select the syntax from either Sentaurus Process or TSUPREM-4.

![](images/calikit_ug_d569445a0c28d59aa63d0559487afa748282c5d904105a92d59e43224320cdfe.jpg)

<details>
<summary>text_image</summary>

Calibration Kit Project Wizard
Database
Calibration Kit Project
Select calibration library database and syntax.
◆ Calibration Library
✓ User Library:
Process Directory:
/u/isedist/sentaurus/tcad/lib/fabpackagelib/processes_sp
Browse...
Experiment Directory:
/u/isedist/sentaurus/tcad/lib/fabpackagelib/experiments
Browse...
Preference Directory:
/u/isedist/sentaurus/tcad/lib/fabpackagelib/preferences
Browse...
Syntax:
◆ Sentaurus Process
✓ TSUPREM-4
Click Next to continue.
< Back	Next >	Finish	Cancel
</details>

4. Click Next.   
5. Select a process list in one of the following ways:

Enter a search pattern in the Process Search Pattern box to look for processes using the Database Process Search (DBPS) module in the selected database and syntax (Step 3).

<!-- page:17 -->
Select Process Names or Process Recipes for the alphabetic order of the process list file.

Click Search to write the results to the selected process list file (see Database Process Search on page 31).

. Click Browse to select a list or search for a list using the DBPS. (For the syntax of a process list file file.qps, see Process Searches on page 30.)

Click Edit to edit the selected list using the SEdit text editor.

# 6. Click Next.

7. Select the process simulator and calibration from the following options:

Sentaurus Process (default): If you select this option, select an implantation model and a diffusion model.

Select the parameters of either Advanced Calibration or User Calibration. If you select User Calibration, select up to two calibration files in the Alagator (Tcl) syntax of Sentaurus Process, which usually follow the naming scheme \*.fps.

• TSUPREM-4: If you select this option, select an implantation model.

Select the parameters of either Advanced Calibration or User Calibration. If you select User Calibration, select the calibration files.

# 8. Click Next.

9. Select the device simulation to calculate the sheet resistance from the following options:

• Device Simulation Disabled (default)

Device Simulation Enabled: If you select this option, the Sentaurus Mesh and Sentaurus Device tool instances are part of the project. Click Browse to select the parameter file for Sentaurus Device. The file format usually follows the naming convention \*.par and is named sdevice.par in the project. If no file is selected, Sentaurus Device uses the default parameters.

# 10. Click Next.

11. Select the methodology for the simulation and the experiment profile comparison.

For numeric comparison, select one of the following options:

Relative Logarithmic Square Difference (default)   
Relative Linear Square Difference   
• Arithmetic Mean of Relative Error   
Quadratic Mean of Relative Error

<!-- page:18 -->
The Noise Filter options are deactivated by default. Select to activate the noise filter (spline-based curve-smoothing) for Experiment Data, Simulation Data, or both.

Select the visualization tool. Sentaurus Visual is the default.

# 12. Click Next.

13. Select a project and scenario name in one of the following ways:

Enter the scenario name, and select Create New Project for a new project.

Click Browse to select a project directory, or enter the project name.

Enter the scenario name, and select Add to Project to add a new scenario to an existing project.

Click Browse to select a project directory.

The new experiments will have the same structure as the rest of the project; that is, the selection of device simulation follows the existing project selection.

# 14. Click Finish.

15. If the project or scenario is created and loaded successfully, click OK in the Progress dialog box.

The generated project has the structure described in Structure of Calibration Kit Projects on page 5. For each process in the process list, the Project Wizard creates an experiment that follows the file-naming convention of the Calibration Kit. In the case of a database in Sentaurus Process syntax, the process is copied; it is not translated. For Sentaurus Process, the resulting process file is b@nr@\_fps.cmd.

The file name of the process sets the variable process. The file names of the profiles set the variables profile\_@integer@.

The variable process\_info takes INFO as a value if processinfo appears as a remark or comment in the process file. For Sentaurus Process, processinfo is:

\## processinfo "INFO"

Analogously, the variable Rs\_exp is set to VALUE if sheetresistance appears as a remark or comment in the process file.

For Sentaurus Process, sheetresistance is one of the following:

\## sheetresistance "VALUE"

\## sheetresistance "Rs=VALUE"

<!-- page:19 -->
The variable y\_sheet is set to 1.25 times the valid depth (set as sims\_xmax in the preference file) of the deepest profile. If no preference (sims\_xmax) is present, the default value of 50 nm is used.

In addition, the variable y\_contact is set to 0.25 times the valid depth (set as sims\_xmax in the preference file) of the shallowest profile, unless the depth is defined explicitly (as probe\_xmax in the preference file). If no preference (probe\_xmax or sims\_xmax) is present, the default value of 5 nm is used.

# Creating a New Scenario for a Project

To focus on a specific selection of experiments for a Calibration Kit project, a project can be split into scenarios. For example, a project can be split into scenarios of different dopant elements.

To create a new scenario for a Calibration Kit project:

1. Open a Calibration Kit project.   
2. Choose Calibration > Scenario Wizard.   
The Scenario Wizard opens.

3. Click Next to start.

4. Enter a search pattern in the Process Search Pattern box to select experiments, and click Search (see Calibration Project Process Search on page 32).

![](images/calikit_ug_1da8705d339439016fed835ff8a73c69be4e8ef4f59eee4d8b70cda25ba00300.jpg)

<details>
<summary>text_image</summary>

Calibration Kit Scenario Wizard
Process Selection
Calibration Kit Scenario
Select experiments by CPPS.
CPPS - Calibration Project Process Search
Process Search Pattern:
impl(element==boron)
Search	Help
Click Next to continue.
< Back	Next >	Finish	Cancel
</details>

5. Click Next.   
6. Enter the name of the new scenario in the Scenario Name box.   
7. Click Finish.   
8. If the scenario is created and loaded successfully, click OK in the Progress dialog box.

<!-- page:20 -->
The structure of the Calibration Kit project is unchanged by the creation of a new scenario.

# Creating a New Short-Loop Experiment

You can add a new short-loop experiment in Sentaurus Process syntax to a database or add a new experiment to a Calibration Kit project.

To create a new short-loop experiment for a Calibration Kit project:

1. Open a Calibration Kit project.   
2. Choose Calibration > Process Wizard.

The Process Wizard opens.

3. Click Next to start.   
4. Select the substrate and oxide properties.

<!-- page:21 -->
If the oxide thickness is 0, the oxide deposition step is omitted.

5. Click Next.

6. Select the implantation properties of the first and second implantations.

If the Element field is set to 0, the corresponding implantation step is omitted.

7. Click Next.

8. Select the anneal ramp properties.

If the Rate or Time field is set to 0, the corresponding diffusion step is omitted.

![](images/calikit_ug_dbe898f1018c163c5012a58eaa536df4efdbdc5626623c2f9aeba81a93ed289a.jpg)

<details>
<summary>text_image</summary>

Calibration Kit Process Wizard
Anneal Ramp
Calibration Kit Process
Select temperatures, rates, times, ambient, and partial pressure.
3
Temp: 1000 C
Time: 1 s
4
Temp: 1000 C
Rate: 75 C/s
2
Temp: 700 C
Rate: -50 C/s
1
Temp: 500 C
5
Temp: 500 C
Ambient: n2
Partial Pressure: 0
Click Next to continue.
< Back	Next >	Finish	Cancel
</details>

9. Click Next.

<!-- page:22 -->
10. Select the properties for the first and second measurements:

• If the Element field is set to 0, the corresponding measurement step is omitted.   
• For the Experiment Data field, click Browse to select the experimental measurement data (SIMS).

Click View to view the selected SIMS using Inspect.

• Select the depth scale of the selected SIMS.   
• For the Preferences field, click Browse to select the preferences.

Click Create to create new preferences and to edit them with the SEdit text editor.

11. Click Next.

12. Select a process name and syntax:

Enter the name of a process in the Name box.   
• Select Sentaurus Process or TSUPREM-4 for the syntax.   
Click Edit to edit the flow if required.

The flow loads into a text editor.

If needed, you can further modify the flow beyond the guidelines of the previous steps.

When you click Edit, the current values of the process steps defined earlier are considered. Further changes to the process in the previous steps no longer affect the flow, unless you click Edit again.

If you click Edit again, the current values of the process steps defined in the previous steps are reconsidered, and the previous changes to the flow in the editor are deleted.

13. Click Next.

14. Select whether the process is added to a database or the currently loaded project:

Select Add to Project to add a new experiment with the created process flow to the currently loaded Calibration Kit project. This option is available only if the currently loaded project is a Calibration Kit project and contains the same simulator that was previously selected as the process syntax.   
Select Add to User Library to add the process flow permanently to a database. Select the process directory for the process recipes, the experiment directory for the measurement data, and the preference directory for the preferences.

15. Click Finish.

16. If the experiment is created successfully, click OK in the Progress dialog box.

<!-- page:23 -->
If the process recipe is added to a database, it is stored in the same format as those in the calibration libraries (see Process File Syntax on page 29). The process flow includes the correlated profile and process\_info information.

If the experiment is added to a project, it has the same structure as other experiments of the project. The variable process is defined by the process name. If an experiment profile is referenced, the variable profile\_@integer@ is defined by the name of the experiment profile. If no experiment profile is referenced, the variable profile\_@integer@ is defined by @process-name@\_@integer@. Depending on the declared implantation and diffusion steps, the variable process\_info is set.

The variable y\_sheet is set to 1.25 times the valid depth (set as sims\_xmax in the preference file) of the deepest profile. If no preference (sims\_xmax) is present, the default value of 50 nm is used.

In addition, the variable y\_contact is set to 0.25 times the valid depth (set as sims\_xmax in the preference file) of the shallowest profile, unless the depth is defined explicitly (as probe\_xmax in the preference file). If no preference (probe\_xmax or sims\_xmax) is present, the default value of 5 nm is used.

NOTE If you edit the process flow further after it is generated, you must ensure that the variable values (such as the number of profiles n\_profile) are correct.

# Creating a New Parameterized Project

You can create a new Calibration Kit project with new physical Sentaurus Process parameters, and an optional command file for the Optimizer tool.

To create a new Calibration Kit project with new physical Sentaurus Process parameters:

1. Open a Calibration Kit project and select an experiment.   
2. Choose Calibration > Parameter Wizard.   
The Parameter Wizard opens.   
3. Click Next to start.   
4. Parameterize the selected process (the name and simulator syntax of the selected process is displayed):

a) Select up to six parameter names for parameter (for example, energy).   
b) Select to either Include or Exclude the experiment data.

<!-- page:24 -->
If you include experiment data, the experiments of the resulting project contain the experiment profiles (SIMS) of the selected experiment.

c) Click Edit to load the flow into an editor.

Edit the flow by replacing the argument values to be parameterized with @parameter@. For example, for the parameter energy and Sentaurus Process syntax, enter:

implant Arsenic dose=1e+15 energy=@energy@ tilt=0 rot=0

Save the file.

5. Click Next.

6. Specify the parameter values of each parameter on the respective tabs:

a) Select the minimal value of the parameter.   
b) Select the iteration step between parameter values.   
c) Select the number of parameter values.   
d) If you select Linear, the difference between values is equal to the iteration step. If you select Log, the value of each step is equal to the value of the previous step multiplied by the value of the iteration step.

![](images/calikit_ug_c865901704cf2e3671118b8686c2e66bd9cbaa4adf06e1e304100076318b64fd.jpg)

<details>
<summary>text_image</summary>

Calibration Kit Parameter Wizard
Parameter Values
Calibration Kit Parameter
Select parameter values.
Parameters
Parameter 1	Parameter 2	Parameter 3	Parameter 4	Parameter 5	Parameter 6
Parameter: tox
Min Value: 0.001
Step: 0.003
Number of Values: 1
Linear	Logarithmic
Click Next to continue.
< Back	Next >	Finish	Cancel
</details>

<!-- page:25 -->
# 7. Click Next.

8. Select a calibration parameter file for the process simulator of the parameterized process file:

• Select an implantation model and a diffusion model.   
Select the parameters of either Advanced Calibration or User Calibration. If you select User Calibration, select up to two calibration files in the Alagator (Tcl) syntax of Sentaurus Process, which usually follow the naming scheme \*.fps.

# 9. Click Next.

10. Select the device simulation to calculate the sheet resistance from the following options:

• Device Simulation Disabled (default)   
Device Simulation Enabled: If you select this option, the Sentaurus Mesh and Sentaurus Device tool instances are part of the project. Click Browse to select the parameter file for Sentaurus Device. The file format usually follows the naming convention \*.par and is named sdevice.par in the project. If no file is selected, Sentaurus Device uses the default parameters.

# 11. Click Next.

12. Select an Optimizer task and the corresponding task conditions, if required, from the following options:

None   
• Sentaurus PCM Studio   
• Screening .   
• Optimization   
• Iterative Optimization   
• Generic Optimization

# 13. Click Next.

14. Select the methodology for the simulation and the experiment profile comparison.

For numeric comparison, select one of the following options:

Relative Logarithmic Square Difference (default)   
• Relative Linear Square Difference   
• Arithmetic Mean of Relative Error   
Quadratic Mean of Relative Error

<!-- page:26 -->
The Noise Filter options are deactivated by default. Select to activate the noise filter (spline-based curve-smoothing) for Experiment Data, Simulation Data, or both.

Select the visualization tool. Sentaurus Visual is the default.

15. Click Next.   
16. Select a project and scenario name:

a) Enter a scenario name.

b) Click Browse to select a project directory, or enter the project name.

17. Click Finish.

18. If the project is created and loaded successfully, click OK in the Progress dialog box.

If no Optimizer task is selected (Task Type is None), the new project has the structure of a Calibration Kit project with two to seven parameters: the nr parameter and the selected parameters. The variable process is the selected process name combined with the parameter value. The variable process\_info contains the parameter name and value. The values of the variables profile\_@integer@ consist of the process name process and sequential numbering, for example, <process>\_1.

The project contains as many experiments as there are possible combinations of parameter values.

If an Optimizer task is selected, the new project has the structure of a Calibration Kit project with two to seven parameters: the nr parameter is a user-defined Optimizer parameter and the selected parameters are design-of-experiments (DoE) Optimizer parameters.

The only available variables are the process name process, the calibration file calibration, and the number of profiles per process n\_profile. The project contains only one experiment with the mean parameter values. For each pair of profiles, a unique curve comparison variable cv\_delta\_@integer@\_@integer@ is evaluated and is used as a response for the Optimizer tool. The corresponding command file of Optimizer is included in the project.

For information about the Optimizer tool, see the Optimizer User Guide.

# Creating a New Project for Optimization

You can create a new Calibration Kit project with new calibration parameters of Sentaurus Process, and an optional command file of the Optimizer tool.

<!-- page:27 -->
To create a new Calibration Kit project with new calibration parameters of Sentaurus Process:

1. Choose Calibration > Optimization Wizard.

The Optimization Wizard opens.

2. Click Next to start.

3. Select the calibration library database from the following options:

• Calibration Library is the default experiment database of the Calibration Kit.

User Library is a user-specified database in either Sentaurus Process syntax or TSUPREM-4 syntax. If you select this option, you must specify the process, experiment, and preference directories, and select the syntax from either Sentaurus Process or TSUPREM-4.

4. Click Next.

5. Select a process list in one of the following ways:

• Enter a search pattern in the Process Search Pattern box to look for processes using the DBPS in the selected database and syntax (Step 3).

Select Process Names or Process Recipes for the alphabetic order of the process list file.

Click Search to write the results to the selected process list file (see Database Process Search on page 31).

. Click Browse to select a list or search for a list using the DBPS. (For the syntax of a process list file file.qps, see Process Searches on page 30.)

Click Edit to edit the selected list using the SEdit text editor.

6. Click Next.

7. Select the process simulator and calibration from the following options:

Sentaurus Process (default): If you select this option, select an implantation model and a diffusion model.

Select the parameters of either Advanced Calibration or User Calibration. If you select User Calibration, select up to two calibration files in the Alagator (Tcl) syntax of Sentaurus Process, which usually follow the naming scheme \*.fps.

• TSUPREM-4: If you select this option, select an implantation model.

Select the parameters of either Advanced Calibration or User Calibration. If you select User Calibration, select the calibration files.

8. Click Next.

<!-- page:28 -->
9. Parameterize the selected calibration file by entering the values of the fields for the parameters:

a) Select up to four parameter names for parameter (for example, ifactor).   
b) Select the minimal value and the maximal value of a parameter.   
c) Select Linear or Logarithmic.   
d) Click Edit to load the calibration file into an editor.

Edit the file by replacing the calibration parameter values to be parameterized with Sentaurus Workbench parameter calls @parameter@. (This calibration file is preprocessed by Sentaurus Workbench as well.)

Save the file.

NOTE For Sentaurus Process, only the second selected calibration file can be parameterized.

10. Click Next.

11. Select an Optimizer task and the corresponding task conditions, if required, from the following options:

• None: If you select this option, no Optimizer task is used, but you must select the number of different parameter values for each parameter.   
Sentaurus PCM Studio: If you select this option, no Optimizer task is used, but you can add more parameter values after the creation of the project.   
• Screening   
Optimization   
• Iterative Optimization   
• Generic Optimization

In addition, the project has a convenient structure for exporting the project view and profiles to Sentaurus PCM Studio. For all other task types, a project with the corresponding Optimizer command file is generated.

For information about Optimizer tasks, see the Optimizer User Guide.

![](images/calikit_ug_e148c2692ba23996e1d3de0e93d46eadae46b2c7669d149fb7342b1a8ff17dcd.jpg)

<details>
<summary>text_image</summary>

Calibration Kit Optimization Wizard
Optimizer Command
Calibration Kit Optimization
Select Sentaurus Workbench Optimizer task and conditions.
Optimizer Task
Task Type: Iterative Optimization
Simulations: 80
Conditions
RSM Degree: 2
Time: 5 hrs
Evaluations: 2000
Iterations: 20
Improvements: 5
LocalOpt r2Adj: 0.99
LocalOpt Range: 20
Click Next to continue.
< Back	Next >	Finish	Cancel
</details>

<!-- page:29 -->
# 12. Click Next.

13. Select the device simulation to calculate the sheet resistance from the following options:

• Device Simulation Disabled (default)   
Device Simulation Enabled: If you select this option, the Sentaurus Mesh and Sentaurus Device tool instances are part of the project. Click Browse to select the parameter file for Sentaurus Device. The file format usually follows the naming convention \*.par and is named sdevice.par in the project. If no file is selected, Sentaurus Device uses the default parameters.

# 14. Click Next.

15. Select the methodology for the simulation and the experiment profile comparison.

For numeric comparison, select one of the following options:

Relative Logarithmic Square Difference (default)   
Relative Linear Square Difference

• Arithmetic Mean of Relative Error   
Quadratic Mean of Relative Error

<!-- page:30 -->
The Noise Filter options are deactivated by default. Select to activate the noise filter (spline-based curve-smoothing) for Experiment Data, Simulation Data, or both.

Select the visualization tool. Sentaurus Visual is the default.

16. Click Next.   
17. Select a project and scenario name:

a) Enter a scenario name.

b) Click Browse to select a project directory, or enter the project name.

18. Click Finish.

19. If the project is created and loaded successfully, click OK in the Progress dialog box.

If no Optimizer task is selected (Task Type is None), the new project has the structure of a Calibration Kit project with two to seven parameters: the nr parameter and the selected parameters. For each process in the process list and each parameter value combination, the Optimization Wizard creates an experiment that follows the file-naming convention of the Calibration Kit.

In the case of a database in Sentaurus Process syntax, the process is copied; it is not translated. For Sentaurus Process, the resulting process file is b@nr@\_fps.cmd.

If an Optimizer task is selected, the new project has the structure of a Calibration Kit project with two to seven parameters: the nr parameter is a user-defined Optimizer parameter and the selected parameters are DoE Optimizer parameters.

The only available variables are the process name process, the calibration file calibration, and the number of profiles per process n\_profile. The project contains only one experiment per process in the process list with mean parameter values. For each pair of profiles, a unique curve comparison variable cv\_delta\_@integer@\_@integer@ is evaluated and is used as a response for the Optimizer tool. The corresponding command file of Optimizer is included in the project.

For information about the Optimizer tool, see the Optimizer User Guide.

<!-- page:31 -->
# Editing Variables

You can change the variable values of a Calibration Kit experiment using Sentaurus Workbench.

To edit a variable:

1. Select the corresponding node:

This is the second Sentaurus Process node for the variables process, calibration, process\_info, Rs\_exp, n\_profile, and profile\_@integer@ (where integer is equal to 1, 2, 3, ..., 10).   
• This is the Sentaurus Mesh node for the variables \*\_contact and \*\_sheet.

2. Edit the variable values in one of the following ways:

• Choose Nodes > Set Variable Value.

In the Add Variable to Node dialog box, enter the name and the value of the variable, and click OK.

Choose Nodes > Edit Properties.

In the Node information dialog box, edit the definition of the variable (as shown in the following example), and click OK.

![](images/calikit_ug_327776afacb4ce25ad524d72eba0f9482d05d1eee39c0e7006ddea2ca6409c09.jpg)

<details>
<summary>text_image</summary>

Defined Variables
process: Example_Process_As
calibration: calib_1d.fps
process_info: As 5keV 1e15 7/0
profile_1: example_profile_as_sims
n_profile: 1
</details>

<!-- page:32 -->
# Visualizing Project Files

Each Calibration Kit project has dedicated viewers that are defined in the project tool database (gtooldb.tcl) of Sentaurus Workbench. These viewers are specifically for the files of Calibration Kit projects.

![](images/calikit_ug_93f1699d5d3ef8d34707fa47f7929d2e03850aa10c15889c7f072b093e57a8f1.jpg)

<details>
<summary>text_image</summary>

Calibration PCM Studio Extensions Help
Sentaurus Visual (Select File...)
Sentaurus Visual (Select by Type)
Sentaurus Visual (All Files)
Tecplot SV (Select File...)
Tecplot SV (All Files)
Inspect (Select File...)
Inspect (All Files)
Text (Select File...)
SDE (Select .sat File...)
Sentaurus Visual - Sentaurus Process Link
XML LogFile (Select .xml File...)
HTML LogFile (Select .html File...)
Calibration Process Files (SEdit)
Calibration Profile Files (Inspect)
Calibration Visual Files (SVisual)
Run Selected Visualizer Nodes Together
Compare Command Files of Selected Nodes
PCM Studio: Export Current Scenario
PCM Studio: Configure Export
</details>

Figure 3 Specific viewers of files of Calibration Kit projects available from the visualization toolbar button

# Viewing Process Files

To view process files:

■ Choose the button > Calibration Process Files (SEdit).

These files open in the SEdit text editor. For Sentaurus Process, the process files are the Sentaurus Process command files (b@node@\_fps.cmd or pp@node@\_fps.cmd) and general files (\*.fps). The selection is restricted to the nr nodes of Sentaurus Process.

<!-- page:33 -->
# Viewing Profile Files

To view profile files:

■ Choose the button > Calibration Profile Files (Inspect).

The selected measured profiles (b@node@\_\*.plx) and simulated profiles (b@node@\_\*.plt) open in the Inspect tool. All of the selected profiles are loaded into one xy plot. The selection is restricted to the nr nodes of Sentaurus Process.

![](images/calikit_ug_f0c918df916d53fab659e17b9f8ab4848fee52dddc80dd38468b311616092e98.jpg)

<details>
<summary>line</summary>

| Depth [nm] | b2_example_profile_as_sims_simulation_Unknown | b2_example_profile_as_sims_Unknown |
| ---------- | ----------------------------------------------- | ------------------------------------ |
| 0          | 1E21                                            | 1E20                                 |
| 20         | 1E19                                            | 1E18                                 |
| 40         | 1E17                                            | 1E16                                 |
| 60         | 1E16                                            | 1E16                                 |
| 80         | 1E16                                            | 1E16                                 |
</details>

Figure 4 An experiment visualized in Inspect

# Viewing Visualization Files

To view visualization files:

■ Choose the button > Calibration Visual Files (SVisual).

The selected measured profiles (b@node@\_\*.plx) and the simulated profiles (b@node@\_\*.plt) open in Sentaurus Visual. All of the selected xy plot visualization scripts (n@node@\_vis\_out.tcl) are loaded and arranged next to each other. The selection is restricted to Sentaurus Visual nodes. For more information, see the Sentaurus™ Visual User Guide.

![](images/calikit_ug_89a2e676b2dac660286bad7aecb256e14b97c77e7c8d8399a28131e85be49a5d.jpg)  
Figure 5 Four experiments visualized in Sentaurus Visual

<!-- page:34 -->
# Confidentiality Warning

The file \$STROOT/tcad/\$STRELEASE/lib/fabpackagelib/confidentwarning.txt contains the text for the confidentiality warning that appears on the first page of the Project, Scenario, and Optimization wizards. If the file is empty or does not exist, no confidentiality warning is displayed.

The file \$STCALIB/confident.txt contains the text for the confidentiality warning that appears in a separate dialog box when the third page of the Project and Optimization wizards is displayed. If the file is empty or does not exist, no confidentiality warning is displayed.

<!-- page:35 -->
This chapter provides details about the Calibration Library, process searches, and working with profiles.

# Experiment Database: Calibration Library

The default experiment database of the Calibration Kit is the Calibration Library, which is defined using the system environment variable STCALIB. By default, STCALIB is set to the directory \$STROOT\_LIB/fabpackagelib, which contains a database and process examples for demonstration purposes only and without any real experimental relevance.

The STCALIB databases (such as the Calibration Library or user databases) include the following directories:

■ The process directory processes\_sp contains the process files in Sentaurus Process syntax.   
■ The experiments directory contains the SIMS profile files in xy plot format.   
The preferences directory contains the preference files (see Profiles on page 33).

# Process File Syntax

In general, the Calibration Kit uses databases of process recipes in Sentaurus Process syntax as input. For the Calibration Library and other user databases to be input to the Calibration Kit, Sentaurus Process syntax is subject to restrictions.

# Restrictions on Sentaurus Process Syntax

The process recipes in Sentaurus Process syntax in the database must include only process physics parameters. However, if you include simulator or model parameters in the process recipe files, the reliability of the simulation might be reduced.

The Sentaurus Process recipes must not contain line statements or region statements (the sourced file calib\_1d\_2018.06.fps or calib\_KMC\_2018.06.fps places these statements in the input files of Sentaurus Process).

<!-- page:36 -->
The 1D measurement statement is specified by the SetPltList statement, which is defined in calib\_1d\_2018.06.fps or calib\_KMC\_2018.06.fps. The SetPltList statement must contain only the species variable and a comment of the corresponding SIMS profile at the end of the same line. For example:

```txt
SetPltList BTotal ; # B_sims_profile.sims 
```

The 1D profile load statement is specified by the profile statement, which must contain only the species variable and a comment of the corresponding profile at the end of the same line. For example:

```python
profile name=Boron ; # B_sims_profile.sims 
```

The process information <INFO> can be declared in a comment line with processinfo "<INFO>" as a comment. For example:

```markdown
## processinfo "B 0.5keV 1e15" 
```

The measured sheet resistance value <VALUE> can be declared in a comment line with sheetresistance "Rs=<VALUE>" as a comment. For example:

```markdown
## sheetresistance "Rs=491" 
```

The measured cap-oxide thickness value <VALUE> in [nm] can be declared in a comment line with OxideThickness <VALUE> as a comment.

# Process Searches

The Quick Process Search (QPS) module provides basic functionality for the process search in the process directory of the database. The Database Process Search (DBPS) module and the Calibration Project Process Search (CPPS) module are based on QPS.

# Syntax of the QPS List File

The results of DBPS and CPPS as well as the input process list to the Calibration Kit project and the scenario wizards are QPS files file.qps. The file contains a header line and a process list. The syntax is:

```txt
Processes Profiles Processinfo R_sheet
<process> <profile_1> <info> <r_sheet>
<profile_2> 
```

<!-- page:37 -->
# Database Process Search

The DBPS module looks for process flows written in Sentaurus Process syntax in a directory (such as \$STCALIB/processes\_\*). Processes that match the search criterion are listed in the process list file.

The search criterion is the process search pattern, which consists of conditions connected by logical operators &&, ||, !, and grouped by parentheses. The operator && means and, || means or, and ! means not. Conditions consist of a keyword and arguments, for example, impl(element==As) or nimpl>0.

In general, the keyword takes only one argument. Only the impl() and diff() keywords can have more than one argument that are connected by logical operators. Some arguments consist of an argument type and a value connected by comparators: ==, <=, >=, <, >, or !=. Some arguments do not have comparators or argument types.

Table 1 DBPS process flow keywords and syntax allowed in DBPS criterion 

<table><tr><td>Keyword</td><td>Description</td><td>Argument</td><td>Example</td></tr><tr><td>impl()</td><td>Implantation statement scan, true if (1)</td><td>element, elem energy, endose tilt rotation, rot</td><td>impl(elem==as) impl(en&gt;0 &amp;&amp; en&lt;100) impl(dose&gt;=1e12) impl(tilt!=0) impl(rot&lt;1)</td></tr><tr><td>diff()</td><td>Diffusion statement scan, true if (1)</td><td>maxT (maximum temperature) totaltime peaktime (time at maximum temperature) pn2 (partial pressure for  $N_2$ ) po2 (partial pressure for  $O_2$ ) ph2o (partial pressure for  $H_2O$ )</td><td>diff(maxT==1000) diff(totaltime&gt;5) diff(peaktime!=0) diff(pn2==1) diff(po2&gt;0 &amp;&amp; po2&lt;1) diff(ph2o!=0)</td></tr><tr><td>plot()</td><td>Plot statement scan, true if (2)</td><td>X, Xtot, Xtotal, Xactive (where X is one of as, p, b, in, ge, sb, ga, al, n)</td><td>plot(bactive)</td></tr><tr><td>nimpl</td><td>Number of implantation statements scan, true if (3)</td><td>-</td><td>nimpl==1</td></tr><tr><td>ndiff</td><td>Number of diffusion statement scan, true if (3)</td><td>-</td><td>ndiff&gt;0</td></tr><tr><td>file()</td><td>File name scan, true if (2)</td><td></td><td>file(USJ)</td></tr><tr><td>grep()</td><td>Process file scan, true if (2)</td><td></td><td>grep(comment)</td></tr><tr><td colspan="4">(1) At least one statement exists in the process file, for which the arguments are evaluated as true.(2) At least one statement exists in the process file, for which the argument is evaluated as true.(3) Comparison is evaluated as true.</td></tr></table>

<!-- page:38 -->
# Calibration Project Process Search

The CPPS module looks for experiments in a calibration project of Sentaurus Workbench. It scans process flows written in Sentaurus Process syntax in the same way as DBPS. However, CPPS scans variables of Sentaurus Workbench. Experiments that match the search criterion are listed in the process list file.

The search criterion is the process search pattern, which consists of conditions connected by logical operators &&, ||, !, and grouped by parentheses. The operator && means and, || means or, and ! means not. Conditions consist of a keyword and arguments, for example, impl(element==As) or nimpl>0.

In general, the keyword takes only one argument. Only the impl() and diff() keywords can have more than one argument that are connected by logical operators. Some arguments consist of an argument type and a value connected by comparators: ==, <=, >=, <, >, or !=. Some arguments do not have comparators or argument types.

Table 2 DBPS process flow keywords and syntax allowed in CPPS criterion 

<table><tr><td>Keyword</td><td>Description</td><td>Argument</td><td>Example</td></tr><tr><td>impl()</td><td>Implantation statement scan, true if (1)</td><td>element, elem energy, endose tilt rotation, rot</td><td>impl(elem==as) impl(en&gt;0 &amp;&amp; en&lt;100) impl(dose&gt;=1e12) impl(tilt!=0) impl(rot&lt;1)</td></tr><tr><td>diff()</td><td>Diffusion statement scan, true if (1)</td><td>maxT (maximum temperature) totaltime peaktime (time at maximum temperature) pn2 (partial pressure for  $N_2$ ) po2 (partial pressure for  $O_2$ ) ph2o (partial pressure for  $H_2O$ )</td><td>diff(maxT==1000) diff(totaltime&gt;5) diff(peaktime!=0) diff(pn2==1) diff(po2&gt;0 &amp;&amp; po2&lt;1) diff(ph2o!=0)</td></tr><tr><td>plot()</td><td>Plot statement scan, true if (2)</td><td>X, Xtot, Xtotal, Xactive (where X is one of as, p, b, in, ge, sb, ga, al, n)</td><td>plot(bactive)</td></tr><tr><td>nimpl</td><td>Number of implantation statements scan, true if (3)</td><td>-</td><td>nimpl==1</td></tr><tr><td>ndiff</td><td>Number of diffusion statement scan, true if (3)</td><td>-</td><td>ndiff&gt;0</td></tr><tr><td>grep()</td><td>Process file scan, true if (2)</td><td></td><td>grep(comment)</td></tr><tr><td colspan="4">(1) At least one statement exists in the process file, for which the arguments are evaluated as true.(2) At least one statement exists in the process file, for which the argument is evaluated as true.(3) Comparison is evaluated as true.</td></tr></table>

Table 3 Sentaurus Workbench keyword and syntax allowed in CPPS criterion 

<table><tr><td>Keyword</td><td>Description</td><td>Argument</td><td>Example</td></tr><tr><td>process()</td><td>Process variable scan, true if at least one statement exists in the process file, for which the arguments are evaluated as true</td><td></td><td>process (USJ)</td></tr></table>

<!-- page:39 -->
# Profiles

This section discusses different aspects of profiles.

# Visualizing Profiles

You can set the visualization limits of each profile in the preference file. The depth [nm] is set by:

```tcl
set vis_xmin [integer]
set vis_xmax [integer] 
```

The concentration [ ] is set by:cm–3

```tcl
set vis_ymin [integer]
set vis_ymax [integer] 
```

<!-- page:40 -->
These values are the lower and upper limits of the visualization to be shown. The visualization tool evaluates a limit if the corresponding limit is not present in the preference file.

# Comparing Profile Curves

Inspect calculates the differences of the measured and computed profile curves, which can be viewed in the Inspect log file. Optionally, you can filter the noise of profile curves by splinebased curve-smoothing. The difference is processed as the variable cv\_delta\_@integer@ of Sentaurus Workbench for each profile pair.

You can set the quality limits of each profile in the preference file. The depth [nm] is set by:

```tcl
set sims_xmin [integer]
set sims_xmax [integer] 
```

These values are the lower and upper limits of the profile curve comparison. The default limits are used as borders if the above limits are not defined. The default values are:

```txt
set sims_xmin 5
set sims_xmax 50 
```

The minimal and maximal concentrations [ ] are set by:cm–3

```tcl
set sims_ymin [double]
set sims_ymax [double] 
```

Concentrations outside of this range are set to the corresponding border value of the profile curve comparison. The default limits are used as borders if the above limits are not defined. By default, sims\_ymin is half the concentration of the smoothed experiment profile curve at the depth sims\_xmax. The default for sims\_ymax is 1e23.

NOTE If several profile pairs are visualized in one plot, only the comparison borders of the last profile pair are shown.

The profile curve comparison can be performed using different methodologies:

Relative logarithmic square difference   
Relative linear square difference   
Arithmetic mean of relative error   
Quadratic mean of relative error

# Relative Logarithmic Square Difference

The formula for the relative logarithmic square difference for the experiment profile curve  fe and the simulated profile curve is:fs

$$
\int_ {x m i n} ^ {x m a x} \left(\log (f e (x)) - \log (f s (x))\right) ^ {2} d x \tag {1}
$$

The borders of integration and are the lower and upper limits of the profile curvexmin xmax comparison, respectively. The relative logarithmic square difference is set per depth [ ].μm–1

<!-- page:41 -->
# Relative Linear Square Difference

The formula for the relative linear square difference for the experiment profile curve $f e$ and the simulated profile curve $f s$ is:

$$
\int_ {x \min} ^ {x \max} (f e (x) - f s (x)) ^ {2} d x \tag {2}
$$

The borders of integration and are the lower and upper limits of the profile curvexmin xmax comparison, respectively. The relative linear square difference is set per depth $[ \mu \mathrm { \bar { m } } ^ { - 1 } .$ ].

# Arithmetic Mean of Relative Error

The formula for the arithmetic mean of the relative error for the experiment profile curve $f e$ and the simulated profile curve $f s$ is:

$$
\frac {\int_ {x m i n} ^ {x m a x} P (x) \left| \frac {f e (x) - f s (x)}{f e (x)} \right| d x}{\int_ {x m i n} ^ {x m a x} P (x) d x} \tag {3}
$$

The borders of integration and are the lower and upper limits of the profile curvexmin xmax comparison, respectively. For each measurement point, results in 1, or else in 0.P x( )

# Quadratic Mean of Relative Error

The formula for the quadratic mean (or root-mean-square) of the relative error for the experiment profile curve $f e$ and the simulated profile curve $f s$ is:

$$
\sqrt {\frac {\int_ {x \min} ^ {x \max} P (x) \left| \frac {f e (x) - f s (x)}{f e (x)} \right| ^ {2} d x}{\int_ {x \min} ^ {x \max} P (x) d x}} \tag {4}
$$

The borders of integration and are the lower and upper limits of the profile curvexmin xmax comparison, respectively. For each measurement point, $P ( x )$ results in 1, or else in 0.

<!-- page:42 -->
3: Calibration Library, Process Searches, and Profiles Profiles
