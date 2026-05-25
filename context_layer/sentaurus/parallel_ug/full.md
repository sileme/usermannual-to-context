<!-- page:1 -->
# TCAD Parallelization Environment Setup User Guide

<!-- page:1 -->
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

# Chapter 1 Environment Setup 1

Overview of Parallelization . .

Shared-Memory Parallelization . . .

Parallelization Using the Message Passing Interface . . .

Installing TCAD Sentaurus on DP Systems . . . .

Hardware and Software Setup . . .

Installing Clusters . . .

Running TCAD Sentaurus Tools on a Cluster . . .

Configuring SSH . .

Creating the MPICH Host File . . .

Automatically Executing an MPI Simulation on a Cluster Using Command-Line Options . . . . 5

Executing an MPI Simulation on a Cluster Using Low-Level MPI Commands. . . . . . 6

Hardware Acceleration Using Graphics Processing Units . . . .

Parallel Job Control Using Sentaurus Workbench . . .

References. .

# Appendix A Message Passing Interface 9

Verifying the MPI Setup . . .

# Glossary 11

<!-- page:4 -->
Contents

<!-- page:5 -->
The user guide describes how to set up a parallelization environment for TCAD Sentaurus™ tools.

# Related Publications

For additional information, see:

The TCAD Sentaurus release notes, available on the Synopsys SolvNet® support site (see Accessing SolvNet on page vi).   
■ Documentation available on SolvNet at https://solvnet.synopsys.com/DocsOnWeb.

# Conventions

The following conventions are used in Synopsys documentation.

<table><tr><td>Convention</td><td>Description</td></tr><tr><td>Blue text</td><td>Identifies a cross-reference (only on the screen).</td></tr><tr><td>Bold text</td><td>Identifies a selectable icon, button, menu, or tab. It also indicates the name of a field or an option.</td></tr><tr><td>Courier font</td><td>Identifies text that is displayed on the screen or that the user must type. It identifies the names of files, directories, paths, parameters, keywords, and variables.</td></tr><tr><td>Italicized text</td><td>Used for emphasis, the titles of books and journals, and non-English words. It also identifies components of an equation or a formula, a placeholder, or an identifier.</td></tr></table>

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
This chapter describes the setup for different parallelization strategies used by TCAD Sentaurus tools.

# Overview of Parallelization

Several TCAD Sentaurus tools use parallelization to improve performance when they run on one of the following supported systems:

■ Shared-memory parallelization (SMP) systems (usually referred to as multicores)   
■ Distributed processing (DP) systems (usually referred to as clusters)   
Hardware-accelerated systems (usually referred to as servers, each equipped with a dedicated hardware accelerator such as a graphics processing unit)

Some TCAD Sentaurus tools also use a combination of SMP, DP, and hardware-accelerated systems, which is referred to as mixed parallel mode.

# Shared-Memory Parallelization

In general, no special setup is needed to run simulations using SMP.

Depending on the TCAD Sentaurus tool, you can specify the number of threads either on the command line, in the command file, or by using an environment variable.

For tool-specific details, including the precedence rules of different options, refer to the respective documentation.

# Parallelization Using the Message Passing Interface

In general, distributed computation by TCAD Sentaurus tools is implemented using the message passing interface (MPI) [1]. All tools use the MPICH library for MPI implementation [2]. Typically, separate processes are distributed over the cores of different server nodes, but you can also run all processes on the cores of a single node.

Distributing processes over a network of machines requires more setup steps than singlemachine MPI simulations.

# Installing TCAD Sentaurus on DP Systems

<!-- page:8 -->
Setting up a distributed application is considerably more complex than setting up its serial or SMP version, because it requires an experienced system administrator with networking expertise on Linux operating systems.

You can try a preconfigured Linux cluster distribution such as Rocks before building a cluster [3].

# Hardware and Software Setup

TCAD Sentaurus is available for Red Hat Enterprise Linux v6.6 and v7.1 on x86-64 platforms. All cluster nodes must be configured with a Synopsys QSC-compliant Linux distribution.

All nodes of the cluster should have the same software setup including the operating system version and TCAD Sentaurus tool version. You should install TCAD Sentaurus on a shared network drive that is accessible using the same path on all nodes. This configuration reduces potential sources of errors due to inconsistent software versions and configuration issues.

NOTE Some TCAD Sentaurus tools might require a cluster to have one head node that has more CPU power and RAM than the computing nodes, because the master process might require maximum RAM for all computed results and maximum CPU power for not yet DP-parallelized portions of the tool.

The overall speed of a TCAD Sentaurus tool is usually limited by the slowest node. The communication bandwidth between nodes can also affect significantly the overall performance, depending on the amount of data exchanged over the network for a specific tool.

# Installing Clusters

# To install a cluster:

1. Ensure the prerequisites for running a TCAD Sentaurus tool in DP parallel mode are met:

a) SSH is installed on each system and is available in the search path of each user.

b) Use a network file system for the installation and user directories, where the path will be the same for all nodes.

2. Install the TCAD Sentaurus distribution in the target directory on your network file system following the instructions in the TCAD Installation Notes.

<!-- page:9 -->
3. Ensure each user has the correct environment settings to run TCAD Sentaurus, following the instructions in the TCAD Installation Notes.

# Running TCAD Sentaurus Tools on a Cluster

You can run a TCAD Sentaurus tool on a cluster using plain Linux, MPI, and tool-specific commands.

In its simple form, to perform a simulation in DP parallel mode, you should:

1. Configure SSH for a password-less log-on to all required hosts. See Configuring SSH.   
2. Create a file with a list of required hosts. The file must also include the head node on which the master process runs. See Creating the MPICH Host File on page 4.   
3. Run the TCAD Sentaurus tool. See Automatically Executing an MPI Simulation on a Cluster Using Command-Line Options on page 5.

NOTE Steps 1 and 2 are required only if you run a simulation on more than one node. For best performance, the number of processes requested on each node must not exceed the number of cores available on the node.

Step 1 is required only once for each cluster; whereas, adapting the host file might be necessary if additional or different computational resources are required for a specific simulation.

You can also run a TCAD Sentaurus tool on a cluster using Sentaurus Workbench (see Parallel Job Control Using Sentaurus Workbench on page 7).

# Configuring SSH

TCAD Sentaurus uses MPICH Hydra as the MPI process manager. As such, you must ensure that password-less SSH command invocations work from the head node to all computing nodes in a cluster.

Assuming a standard SSH installation and a shared home directory on all cluster nodes, you configure SSH by logging on to any of the cluster nodes as follows:

1. Generate a pair of authentication keys on the host:   
ssh-keygen -t rsa   
2. Enter an empty passphrase by pressing the Enter key when asked for the passphrase, and use the default file name.

<!-- page:10 -->
# 1: Environment Setup

Running TCAD Sentaurus Tools on a Cluster

3. Add the public key to the authorized keys:

```shell
touch ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys 
```

For alternatives, refer to the SSH documentation.

Use the following UNIX commands to verify that log-on without a password is possible for each relevant node with the name <nodename>:

```txt
ssh <nodename> hostname 
```

If necessary, answer the question about the RSA key fingerprint with yes.

Moreover, the same commands should display the name of the cluster node without requiring any passwords, passphrases, RSA keys, or other input:

```txt
ssh <nodename> hostname 
```

Alternative configurations include:

The system administrator can provide you with a preconfigured \~/.ssh/known\_hosts file to avoid the RSA key fingerprint question.   
You can provide a suitable /etc/ssh/known\_hosts file on each system.   
You can use the ssh-keyscan command to collect the necessary keys.

For more information about SSH configurations, refer to the SSH and SSHD documentation [4].

# Creating the MPICH Host File

The MPICH host file lists the names of all the nodes of your cluster.

NOTE The host file must not contain empty lines.

For example, the mpichhostfile.txt host file has the following content:

```yaml
$ cat ~/mpichhostfile.txt
node1:4
node2:4
node3:4
node4:4 
```

<!-- page:11 -->
In the example, if the total number of requested processes is 16, then four MPI processes must run on each of the four nodes. More precisely, the first four processes will run on host node1, the next four processes will run on host node2, and so on.

If only a list of nodes is specified, then MPICH Hydra tries to divide the processes equally among the specified nodes in a round-robin manner.

In the following example, the mpichhostfile.txt file is used for a simulation using 16 processes:

```txt
$ cat ~/mpichhostfile.txt
node1
node2
node3
node4 
```

The first and fifth processes will run on host node1, the second and the sixth processes will run on host node2, and so on.

# Automatically Executing an MPI Simulation on a Cluster Using Command-Line Options

After successfully completing Steps 1 and 2 (see Running TCAD Sentaurus Tools on a Cluster on page 3) and verifying the MPI setup (see Verifying the MPI Setup on page 9), it is recommended to run the TCAD Sentaurus tool in DP parallel mode using the command-line option --processes from either the command line or Sentaurus Workbench.

You can use the following command to start a TCAD Sentaurus tool from the command line:

```erb
$ <tool_name> --processes <#processes> [--mpi-file <hostfile>]
    [--threads <#threads_per_process>]
    [<tool_command_line_options>] <command_file> 
```

For the format of the host file, see Creating the MPICH Host File on page 4.

The advantage of automated cluster execution is that it manages MPI processes and the execution of MPICH Hydra (mpiexec.hydra) with the required command-line options (see Executing an MPI Simulation on a Cluster Using Low-Level MPI Commands on page 6).

# Executing an MPI Simulation on a Cluster Using Low-Level MPI Commands

<!-- page:12 -->
In the following situations, it might be necessary to use low-level MPI commands to run a TCAD Sentaurus tool on a cluster:

■ Access to a cluster is granted only through a cluster management system.   
Additional MPI options must be set that are not supported by automated cluster execution using tool command-line options.   
You need to troubleshoot the MPI setup.

TCAD Sentaurus uses the MPICH library [2] for process management and communication between nodes.

NOTE The MPICH library requires Python version 2.3 or higher for execution.

A compiled version of MPICH is installed with TCAD Sentaurus in the installation directory \$STROOT/tcad/current/linux64/mpich/, including binaries, man pages, and documentation as provided by MPICH.

To make MPICH available, you must configure the environment as follows:

1. Include the paths to both the TCAD Sentaurus tool supporting MPI and MPICH in the \$PATH variable.   
2. Verify the correct settings by executing the following commands:

\$ which <tool\_name>

\$ which mpiexec.hydra

Ensure the \$PATH variable does not point to LAM MPI, Open MPI, and other MPI installations that might already exist on the system.

# Hardware Acceleration Using Graphics Processing Units

Only Sentaurus Device Electromagnetic Wave Solver supports hardware acceleration using graphics processing units (GPUs).

See Sentaurus™ Device Electromagnetic Wave Solver User Guide, Chapter 9 on page 93.

# Parallel Job Control Using Sentaurus Workbench

<!-- page:13 -->
Sentaurus Workbench provides special functionality that controls the submission of parallel jobs on both SMP and DP systems. It helps with the allocation of parallel resources, including the distribution of MPI processes according to different policies.

See Sentaurus™ Workbench User Guide, Configuring the Execution of Jobs on page 154.

# References

[1] For more information, go to https://www.mpi-forum.org/.   
[2] For more information, go to http://www.mpich.org/.   
[3] For more information, go to http://www.rocksclusters.org/.   
[4] For more information, go to http://www.openssh.com/.

<!-- page:14 -->
1: Environment Setup References

<!-- page:15 -->
This appendix describes how to verify the setup for the message passing interface (MPI).

# Verifying the MPI Setup

To verify that the MPI setup is correct:

1. Ensure that the location of the MPICH library installed with TCAD Sentaurus is in your \$PATH variable, before any other MPI implementations, by executing the following command:

\$ which mpiexec.hydra

Your path can be set in Bash using:

\$ export PATH=\$STROOT/tcad/current/linux64/mpich/bin:\${PATH}

Your path can be set in C shell using:

\$ setenv PATH \$STROOT/tcad/current/linux64/mpich/bin:\${PATH}

2. Check that you can run a command multiple times on the local node:

\$ mpiexec.hydra -n 10 hostname

3. If this succeeds, run the TCAD Sentaurus tool supporting MPI with multiple workers on one node:

\$ mpiexec.hydra -n 8 <tool\_name> <command\_file>

4. Ensure that all hosts listed in the MPICH host file (<hostfile>) run the TCAD Sentaurus tool correctly. Execute a command on all nodes specified in the host file:

\$ mpiexec.hydra -f <hostfile> hostname

If the command hangs or generates error messages, locate the cause by subsequent removal of host names from the file, and then return to Step 2 for that particular host.

5. Start the TCAD Sentaurus tool supporting MPI on the nodes specified in the host file:

\$ mpiexec.hydra -n <#processes> -f <hostfile> <tool\_name> <command\_file>

If all commands execute successfully, the system should be set up correctly to run the TCAD Sentaurus tool on a cluster.

<!-- page:17 -->
This glossary contains terms used in the TCAD Parallelization Environment Setup User Guide.

# D

# DP

Distributed processing.

# G

# GPU

Graphics processing unit.

# L

# LAM MPI

Local area multicomputer message passing interface.

# M

# MPI

Message passing interface.

# MPICH

An implementation of the MPI.

# MPICH Hydra

MPI process manager.

# O

# Open MPI

An implementation of the MPI.

<!-- page:18 -->
# Q

#

Qualified system configuration. The Synopsys Platforms Core Team defines and communicates the standard system configurations for the build and release environment for all Synopsys products. The environment is documented as the QSC and is part of the corresponding foundation.

# S

# SMP

Shared-memory parallelization.

# SSH

Secure shell.

# SSHD

OpenSSH daemon that runs and allows users to connect to a server.
