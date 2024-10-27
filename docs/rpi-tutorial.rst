.. image:: rpi/media/image1.jpeg




|image1|\ Embedded Linux Systems: Using Buildroot for building Embedded
Linux Systems on Raspberry Pi 4 and 3 Model B by Mariano Ruiz is licensed
under a `Creative Commons Attribution-ShareAlike 4.0 International
License <http://creativecommons.org/licenses/by-sa/4.0/>`__.

.. |image1| image:: rpi/media/image2.png
   :width: 0.91667in
   :height: 0.32292in


Scope
=====


Document Overview
-----------------

This document describes the steps to develop an embedded Linux-based
system using the Raspberry PI board. The document has been specifically
written to use a Raspberry PI development system based on the BCM2837
processor. All the software elements used have a GPL license.

.. note:: 
   The time necessary to  complete all the tutorial steps is approximately 8 hours.    

Read all the instructions carefully before executing the practical part;
Otherwise, you will find errors, which are probably unpredicted. In
parallel, you need to review the slides available at the Moodle site or
at [RD1]

Acronyms
--------

.. list-table:: Acronyms
    :widths: 25 25 50
    
   * - CPU
     - Central Processing Unit 
   * - EABI
     - Extended Application Binary Interface
   * - EHCI     
     - Enhanced Host Controller Interface   
   * - I/O 
     - Input and Output
   * - MMC 
     - Multimedia card 
   * - NANDFlash 
     - memory type for fast sequential read and write
   * - PCI 
     - Peripheral Component Interconnect – computer bus standard
   * - PCI Express
     - Peripheral Component Interconnect Express 
   * - OS
     - Operating system
   * - UART
     - Universal Asynchronous Receiver Transmitter 
   * - USB 
     - Universal Serial Bus


References
==========

1. Embedded Linux system development. `Slides <https://moodle.upm.es/titulaciones/oficiales/course/view.php?id=1969>`_

2. https://bootlin.com/training/embedded-linux/

3. Mastering Embedded Linux Programming - Second Edition. Packt.
   https://www.packtpub.com/product/mastering-embedded-linux-programming-second-edition/9781787283282

4. Raspberry-Pi User Guide. Reference Manual.

   `www.myraspberry-pi.org/wp-content/.../Raspberry.Pi_.User_.Guide_.pdf‎ <http://www.myraspberry-pi.org/wp-content/.../Raspberry.Pi_.User_.Guide_.pdf‎>`__

Building Linux using buildroot
==============================

Elements needed for the execution of these LABS
-----------------------------------------------

In order to execute this lab properly, you need the following elements:

1. The VMware player software version 17.6.1 or above. Available at
   `Broadcom website <https://support.broadcom.com/group/ecx/productdownloads?subfamily=VMware+Workstation+Pro>`__ (free download and use but you need to register).
   This software has already been installed on the laboratory desktop
   computer.

2. A VMWare virtual machine with Ubuntu 24.04 and all the software
   packages installed is already available on the Desktop. This virtual
   machine is available for your personal use. If you want to set up
   your virtual machine by yourself, follow the instructions provided in
   `Annex I <#_annex_i:_Ubuntu>`__.

3. A Raspberry Pi, accessories and a USB cable are available at the
   laboratory.

4. Basic knowledge of Linux commands.

Starting the VMware
-------------------

Start VMware Player and open the RPI Virtual Machine. Wait until the
welcome screen is displayed (see Fig. 1 and Fig. 2). Login as
“\ *ubuntu”* user using the password “ubuntu”.

.. image:: rpi/media/image4.png
   :alt: A screenshot of a computer Description automatically generated
   :width: 4.92027in
   :height: 3.97031in

Fig. 1: Main screen of VMware player with some VM available to be
executed.

.. image:: rpi/media/image5.png
   :alt: A screenshot of a computer Description automatically generated
   :width: 6.69375in
   :height: 3.69514in

Fig. 2: Ubuntu Virtual Machine login screen.

Open the **Firefox** web browser and download from
https://buildroot.org/, the version identified as **buidlroot2024-08-1**
(use the download link, see Fig. 3, and navigate searching for earlier
releases if necessary, https://buildroot.org/downloads/ ). Save the file
to the **Documents** folder in your account (Fig. 4).

.. image:: rpi/media/buildrootweb.png
   :width: 5.97015in
   :height: 4.03801in

Fig. 3 Buildroot home page.

Buildroot is a tool to generate embedded Linux systems in our PC, and
then this Linux will be installed in the target.

.. image:: rpi/media/buildrootdownload.png
   :width: 5.25472in
   :height: 3.28499in

Fig. 4: Example of Downloading buildroot source code.

Create a folder “rpi” in “Documents”. Copy the file to the
“Documents/rpi” folder and decompress the file (Fig. 5).

.. image:: rpi/media/documentsfolder.png
   :alt: A screenshot of a computer Description automatically generated
   :width: 6.69375in
   :height: 1.5in

Fig. 5: Buildroot folder (the folder name depends on the version
downloaded).

Right-click in the window and execute “Open in Terminal” or execute the
Terminal application from Dash home as shown in Fig. 6 (if “Open in
Terminal” is not available, search how to install it in Ubuntu).

.. image:: rpi/media/openaterminal.png
   :width: 4.20139in
   :height: 2.0in

Fig. 6: Terminal application

In some seconds, a command window is displayed. Then, execute these
commands:

.. code-block:: bash 

    $ mkdir build
    $ cd build
    $ make O=$PWD -C /home/ubuntu/Documents/rpi/buildroot-2023.08.2/ menuconfig


.. important::
    
    For this course, you will need to become familiar with the Linux Terminal use. On the Moodle site of this course, you can find a cheat sheet with the basic Linux commands. 

.. tip::
    
    In a Linux terminal, the “TAB” key helps you to  autocomplete the commands, folders, and file names. 

In some seconds, you will see a new window similar to Fig. 7.

.. image:: rpi/media/image10.png
   :alt: A screenshot of a computer Description automatically generated
   :width: 6.69375in
   :height: 3.20208in

Fig. 7: Buildroot setup screen.

Configuring Buildroot for RPI4
------------------------------

Once the **Buildroot** configuration is started, it is necessary to
configure the different items. You need to navigate the different menus
and select the installation elements. Table I contains the specific
configuration of **Buildroot** for installing it in the Raspberry Pi.
Depending on the downloaded version, the organization and the items
displayed can differ. If an item of buildroot configuration does not
appear in the Table I leaves it with its default value.


.. important::

    The Buildroot configuration is an iterative process. In order to set up your embedded Linux system, you  will need to execute the configuration several times.      


Target Options
^^^^^^^^^^^^^^
This is the  selection of the processor to use.

.. list-table:: Target Options

   * - Target Architecture
     - AArch64 (little endian) 
     - ARM 64 bits
   * - Target Architecture Variants.
     - Cortex-A72
     - 
   * - Floating Point Strategy
     - VFPv4
     - 
   * - MMU  Page Size
     - 4KB
     -
   * - Target Binary Format
     - ELF
     - 

Toolchain
^^^^^^^^^
Cross Compiler, linker, and libraries to be  built to compile our embedded application. Select the options shown in the following table. 

.. list-table:: Toolchain

   * - Toolchain type
     - Buildroot toolchain
     - The Embedded Linux System will be compiled with tools integrated  into Buildroot
   * - Custom toolchain vendor name.
     - buildroot
     -
   * - C library
     - Library    containing the typical C  libraries used in  Linux    environments   (stdlib, stdio,   etc)
     - glib
   * - Kernel Headers
     - same as kernel being built
     - 
   * - Custom Kernel Headers  Series
     - 6.6.x
     - 
   * - Binutils Version
     - 2.41
     - Binutils contains  tools to manage    the binary files obtained in the   compilation of   the different     applications    
   * - GCC  compiler Version
     - gcc 13.x   
     - GCC tools version to be installed  
   * - Enable C++ support
     - Yes. 
     - Including support for C++ programming, compiling, and    linking. 
   * - Build cross gdb for the host
     - Yes. 
     - Includes the  support for GDB.  
   * - Add Python support 
     - 
     -
   * - GDB debugger version
     - gdb 14.x
     -

Build options
^^^^^^^^^^^^^
How Buidlroot will build the code. Leave the default values.


System Configuration 
^^^^^^^^^^^^^^^^^^^^
  
.. list-table:: System configuration

   * - Root FS skeleton
     - Default target skeleton. 
     - Linux folder filesystem organization for skeleton the embedded system 
   * - System hostname
     - **buildroot**.   
     - Name of the embedded system
   * - System Banner
     - **Linux RPI 4**
     - Banner.
   * - Passwords encoding
     - sha 256 
     -
   * - Init System
     - Busybox
     -
   * - /dev management
     - Dynamic using devtmpfs only
     - 
   * - Path to permissions for table  
     - **system/device_table.txt**  
     -
   * - Enable root login with password
     - yes
     - 
   * - Root password 
     - rpi
     -
   * - Busybox’ default shell 
     -  /bin/sh
     -
   * - Run a getty after boot
     - tty PORT: **console**. Baudrate: keep kernel default. TERM environment variable: vt100
     - 
   * - remount root filesystem read write during boot
     - Yes
     -
   * - Network interface to configure through DHCP
     - eth0
     -
   * - Set the system's default PATH
     - /bin/sbin:/usr/bin:/usr/sbin  
     -
   * - Purge unwanted locales
     - yes
     -
   * - Leave the default values for all others
     - 
     -
   * - Custom scripts to run path **before** creatating filesystem images
     - board/raspberrypi4-64/post build.sh 
     -
   * - Custom scripts to run inside the fakeroot environment 
     - 
     -
   * - Custom scripts to run **after** creating filesystem images
     - board/raspberrypi4_64/post image.sh 
     -                                                        


Linux Kernel
^^^^^^^^^^^^

.. list-table:: kernel 

	* - Kernel Version
	  - Custom tarball. URL
	  - $(call github,raspberrypi,linux,576cc10e1ed50a9eacffc7a05c796051d7343ea4)/linux-576cc10e1ed50a9eacffc7a05c796051d7343ea4.tar.gz  
	* - Kernel configuration 
	  - Using and intree defconfig file
	  -
	* - Defconfigname
	  - bcm2711
	  - This file containst the specific configuration of the kernel for the RPI
	* - Kernel binary format
	  - Image 
	  -
	* - Kernel  compression format
	  - Gzip compression
	  -
	* - Build aDevice Tree Blob (DTB)
	  - Yes
	  -
	* - Intree Device Tree Source file name 
	  - broadcom/bcm2711-rpi-4-b broadcom/bcm2711-rpi-400 broadcom/bcm2711-rpi-cm4 broadcom/bcm2711-rpi-cm4s
	  - 
        * - Need host OpenSSL 
          - Yes
          -
        * - Linux kernel Extensions
          - Nothing
          - 
	* -  Linux Kernel Tools 
	  - Nothing
	  - 
	  
Target Packages
^^^^^^^^^^^^^^^

.. list-table:: Busybox and target packages	

	* - Busybox
	  - yes
	  - 
	* - Busybox configuration file to use
	  - package/busybox/busybox.config
	  - 
	* - Audio and video applications
	  - Default values
	  - 
	* - Compresssors and decompressors
	  - Default values
	  - 
	* - Debugging, profiling and benchmark
	  - **gdb, gdbserver, full debugger** 
	  - 
	* - Developments tools
	  - Default values
	  -  
	* - Filesystem  and flash utilities 
	  - Default values
	  - 
	* - Games
	  - Default values 
	  - 
	* - Graphic libraries and applications (graphic/text) 
	  - Default values 
	  - 
	* - Hardware handling 
	  - **Firmware>rpifirmware** **rpi4 (default)**	
	  - **Path to a file stores as boot/config.txt board/raspberrypi4_64/config_4_64bit.txt** 
	* - Hardware handling 
	  - **Firmware>rpifirmware**	  
	  - **Path to a file stored as boot/cmdline.txt board/raspberrypi/cmdline.txt** 
	* - Hardware handling 
	  - **Firmware>rpifirmware** 
	  - **install DTB  overlays**
	* - Interpreters language and  scripting Libraries 
	  - Python3
	  - 
	* - Miscellaneous
	  - Default Values
	  -
	* - Libraries
	  - Default Values
	  - 
	* - Networking applications 
	  - **ifupdown scripts** **open ssh**
	  - 
	* - Package Managers
	  - Default values
	  - 
	* - Real Time, Shell and  utilities
	  - Default Values
	  -  
	* - System Tools, Text Editor and Viewers
	  - Default Values
	  - 

File System Images
^^^^^^^^^^^^^^^^^^

.. list-table:: Filesystem images	

	* - ext2/3/4 root filesystem 
	  - ext4
	  -
	* - filesystem label
	  - rootfs
	  -
	* - exact size 
	  - **400M** Leave the other default values
	  - Update this value with your specific needs
        * - Compression method 
          - No compression
          - 
    
Bootloaders
^^^^^^^^^^^

      
Host Utilities
^^^^^^^^^^^^^^      

.. list-table:: Host utilities	

    * - host environment setup
      - Yes
      -
    * - host genimage
      - Yes
      -
    * - host dosfstools
      - Yes
      -
    * - host kmod
      - Yes, support xz-compressed modules
      - 
    * - host mtools
      - Yes
      -

Once you have configured all the menus, you need to exit, saving the
values (File->Quit).



Compiling buildroot
-------------------

In the Terminal Window executes the following command:

.. code-block:: bash 

    $ make O=$PWD -C /home/ubuntu/Documents/rpi/buildroot-2023.08.2/ 

If everything is correct, you will see a final window similar to the one
represented in Fig. 8.

.. warning::

    In this step, buildroot will connect, using the internet, to different repositories. After downloading the code, Buildroot will compile the applications and generate a lot of files and folders. Depending on your internet speed access and the   configuration chosen, this step could take up to **one hour  and a half**. If you have errors in the buildroot configuration,  you could obtain errors in this compilation phase. Check your configuration correctly. Use “make O=$PWD -C /home/ubuntu/Documents/rpi/buildroot-2023.08.2/ clean” to clean up  your partial compilation.


.. note::

    dl subfolder in your buildroot folder contains all  the packages downloaded for the internet. If you want to  move your buildroot configuration from one computer to another, avoiding the copy of the virtual machine, you can copy this folder.                                            |


.. image:: rpi/media/buildrootok.png
   :width: 6.68125in
   :height: 4.46389in

Fig. 8: Successful compilation and installation of Buildroot

**Buildroot** has generated some folders with different files and
subfolders containing the tools for generating your Embedded Linux
System. The next paragraph explains the main outputs obtained,

Buildroot Output.
-----------------

The main output files of the execution of the previous steps can be
located in the folder “build/images”. Fig. 9 summarizes the use of
**Buildroot**. Buildroot generates a bootloader, a kernel image, and a
file system.

.. image:: rpi/media/buildroot.png
   :alt: Buildroot tool basic operation
   :width: 5.98081in
   :height: 2.5in

Fig. 9: Schematic representation of the Buildroot tool. Buildroot
generates the root file system, the kernel image, the bootloader, and
the toolchain. Figure copied from “Bootlin” training materials
(`http://bootlin.com/training/ <http://bootlins.com/training/>`__)

In our specific case, the folder content is shown in Fig. 10

.. image:: rpi/media/buildimages.png
   :alt: Output generated for the RaspberryPi Embedded Linux
   :width: 5.98081in
   :height: 4.0in

Fig. 10: The images folder contains the binary files for our embedded
system.

Copy the sdcard.img file to your SDcard using this Linux command in the
Buildroot folder (sdb is typically the device assigned to the sdcard,
unless you have other removable devices connected to the system):

.. code-block:: bash

   $ sudo dd if=./images/sdcard.img of=/dev/sd<x> bs=10M //<x> is the identification used by Linux for your microSD card, tipically “b” or “c”, never use “a” because this is the operating system hardisk

Remember to format again the microSDcard if you need to repeat this
process (linux gparted is an excellent tool to partition and format the
SD card).

Booting the Raspberry Pi.
-------------------------

Fig. 11 displays a Raspberry Pi. The description of this card, its
functionalities, interfaces, and connectors are explained in the ref
[RD2]. The fundamental connection requires:

a) To connect a USB to RS232 adapter (provided) to the raspberry-pi
   expansion header (see Fig. 12 and Fig. 13). This adapter provides the
   serial line interface as a console in the Linux host operating
   system.


.. list-table:: FDTI Terminals
    :widths: 25 25
    :header-rows: 1
 
    * - RPI connector
      - FDTI Terminal
    * - RXD UART (GPIO16)
      - Pin 4
    * - TXD UART (GPIO15)
      - Pin 5
    * - GND (Pin 6)
      - Pin 1  


b) To connect the power supply with the micro-USB connector provided (5
   v).

c) To connect the Ethernet cable to the RJ45 port if it is available
   (not the case of UPM Lab).

.. image:: rpi/media/rpi4b.png
   :width: 4.41667in
   :height: 2.94167in

Fig. 11: RaspBerry-Pi 4 Model B hardware with main elements identified.

.. image:: rpi/media/rpiconnector.png
   :width: 4.0in
   :height: 10.0in


Fig. 12: Raspberry-PI 4 header terminal identification.

.. image:: rpi/media/fdticable.png
   :width: 3.50in
   :height: 6.0in

Fig. 13: Identification of the terminals in the USB-RS232 adapter

The booting process of the Raspberry Pi BCM2711 `BCM2711 <https://www.raspberrypi.com/documentation/computers/processors.html#bcm2711>`_ processor is depicted
in Fig. 14. Take into account that this System On Chip (SoC), the
BCM2711, contains two different processors: a GPU and an ARM
processor. The programs *bootcode.bin* and *start.elf* are written
explicitly for the GPU, and the source code is unavailable. Broadcom
only provides details of this to customers who sign a commercial
agreement. The last executable (*start.elf*) boots the ARM processor and
allows the execution of ARM programs such as Linux OS kernel or other
binaries such as u-boot bootloader.



Fig. 14: Booting process for BCM2711 processor in the raspberry-pi.

The config.txt file contains essential information to boot the Linux OS
and perform the configuration of different hardware elements (look at
http://elinux.org/RPiconfig and check the meaning of the different
configuration parameters). Verify the content of the config.txt file
generated by buildroot and complete it as depicted below.

In this example, once the ARM is released from reset, it executes the
Image application. This binary application is the Linux Kernel in Image
format. The parameters passed to the application specified in the
kernel=<….> are detailed in the cmdline.txt file. For instance, by
default, Buildroot generates this one:

In the Linux machine, open a Terminal and execute the program putty with
sudo rights (sudo putty), in a second a window appears. Configure the
parameters using the information displayed in Fig. 15 (for the specific
case of putty), and then press “Open”. **Apply the power to the
Raspberry PI,** and you will see the booting messages.

.. tip::
    **[Serial interface identification in Linux]:** In Linux the  serial devices are identified typically with the names       /dev/ttyS0, /dev/ttyS1, etc. In the figure, the example has   been checked with a serial port implemented with a USB-RS232 converter. This is the reason why the name is **/dev/ttyUSB0**.   In your computer, you need to find the identification of   your serial port. Use Linux **dmesg** command to do this.    


.. image:: rpi/media/image19.png
   :alt: A computer screenshot of a computer Description automatically generated
   :width: 4.90093in
   :height: 4.28723in

Fig. 15: Putty program main window.

After a few seconds, you will see a lot of messages displayed on the
terminal. Linux kernel is booting, and the operating system is running
its configuration and initial daemons. If the system boots correctly,
you will see an output like the one represented in Fig. 16. Introduce
the username root, and the Linux shell will be available for you.

.. image:: rpi/media/image20.png
   :width: 6.69514in
   :height: 2.58472in

Fig. 16: Linux Running

.. tip::

    **[DHCP Server]:** The DHCP server providing the IP address  to the RPI should be active in your network. In the UPM ETSIST labs, there is no cabled network, only WIFI. If you are using the RPI at home, the DHCP server is running in your router. The method used to assing IP addresses is different from one manufactures to others. If you want to know the IP address assigned, you have two options: use a serial cable connected to the RPI (ifconfig command) or check the router status web page and display the table of the DHCP clients connected. Looking for the MAC in the list, you will obtain the IP address.         


Connecting the RPI to the cabled ethernet network
-------------------------------------------------

Inspecting the configuration of the network interface generated automatically by Buildroot
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Inspect the content of */etc/network/interfaces* and */etc/init.d/S40network*. You will see content similar to this in the
interfaces file:

.. code-block:: bash

   # interface file auto-generated by buildroot

   auto lo
   iface lo inet loopback

   auto eth0
   iface eth0 inet dhcp
   	pre-up /etc/network/nfs_check
   	wait-delay 15
   	hostname $(hostname)

This configuration activates the use of eth0 with DHCP support. Test the
connectivity, trying to connect to another computer in the laboratory.
Use the ping command.


.. note::

    **[Help]:** If you run the ping command in the Raspberry   trying to connect with a computer in the laboratory, you      probably obtain a connection timeout. Consider that   computers running Windows could have the firewall activated. You can also try to run the ping on a windows computer or on Linux virtual machine. In this case, the RPI does not have a  firewall running, and the connection should be successful.   

.. admonition:: Question

    What is the MAC address of your RPI interface? Use the dmesg command to see the kernel boot parameters and identify the method used to get the MAC address from the hardware.        

Adding WIFI support 
===================


Adding mdev support to Embedded Linux
=====================================


The folder <buildroot-folder>\ */package/busybox* contains two files
named S10mdev and mdev.conf. These files have to be added to the target
filesystem. This step is done by adding these commands to the
*<buildroot-folder>/board/raspberrypi3-64/post-build.sh* script:


.. code-block:: bash

   cp <buildroot-folder>/package/busybox/S10mdev ${TARGET_DIR}/etc/init.d/S10mdev
   chmod 755 ${TARGET_DIR}/etc/init.d/S10mdev
   cp <buildroot-folder>/package/busybox/mdev.conf ${TARGET_DIR}/etc/mdev.conf

.. note::

    [mdev] mdev provides a method to add or remove hotplug devices in Linux.  


Adding the Broadcom firmware support for Wireless hardware
==========================================================

The hardware element included in the RPI-3 for the Wireless
communication is implemented with the BCM43438 chip. It is needed to
include the software packages with the firmware’s chip and the wireless
utilities.

1. Execute “make ……. menuconfig”. Navigate to “Target Packages->Hardware
   Handling->Firmware-> bcrmfmac-sdio-firmware-rpi” and select the
   “bcrmfmac-sdio-firmware-rpi-wifi”.

2. Before compiling Buildroot we need to add more software supporting
   the configuration of the WIFI.

   a. Navigate to “Target Packages->Networking Applications” and select

      -  “crda”

      -  “ifupdown scripts”

      -  “iw”

      -  “wireless-regdb”

      -  “wireless tools”

      -  “wpa_supplicant”

         1. “Enable EAP”

         2. “Enable WPS”

         3. “Install wpa_cli binary”

         4. “Install wpa_client shared library”

         5. “Instal wpa_passphrase binary”

   b. Add these lines to ./board/rapsberrypi3-64/post-build.sh.

::

   cp <buildroot-folder>/board/raspberrypi3/interfaces ${TARGET_DIR}/etc/network/interfaces
   cp <buildroot-folder>/board/raspberrypi3/wpa_supplicant.conf ${TARGET_DIR}/etc/wpa_supplicant.conf

c. Create the file *<buildroot-folder>*/board/raspberrypi3/interfaces
   with this new content:

::

   auto lo
   iface lo inet loopback

   auto eth0
   iface eth0 inet dhcp
   	pre-up /etc/network/nfs_check
   	wait-delay 15
   	hostname $(hostname)

   auto wlan0
   iface wlan0 inet dhcp
          pre-up wpa_supplicant -B -iwlan0 -c/etc/wpa_supplicant.conf
          post-down killall -q wpa_supplicant
          wait-delay 15

d. Create the file
   *<buildroot-folder>*/board/raspberrypi3/wpa_supplicant.conf with this
   content (ask professors about the values to be provided as SSID and
   Key-passwd). You can as many WIFIs as you want.

::

   network={
   ssid="SSID"
   key_mgmt=WPA-PSK
   psk="PASSWORD"
   priority=9
   }

3. Perform a *make* and burn the new image in the SDcard. Boot the
   Raspberry and check that you can connect to the wireless network.

Using the integrated development environment Eclipse/CDT
========================================================

Eclipse IDE for C/C++ developers
--------------------------------

The Eclipse IDE CDT is installed in the virtual machine. You can execute
it running eclipse in a window terminal.

Cross-Compiling applications using Eclipse
------------------------------------------

How will a program be compiled? Remember that we are developing cross
applications. We are developing and compiling the code in a Linux x86_64
machine, and we are executing it on an ARM architecture (see Fig. 17).



Fig. 17: Summary of the different configurations for developing
applications for embedded systems. Figure copied from “Free Electrons”
training materials (http://free-electrons.com/training/)

The first question is where the cross-compiler and other cross-tools are
located. The answer is this: in the folder “build/host/usr/bin”. If you
inspect this folder's content, you can see the entire compiling,
linking, and debugging tools (see Fig. 18). These programs are executed
in your x86_64 computer, but they generate code for the ARM processor.

.. image:: rpi/media/image22.png
   :width: 5.90168in
   :height: 3.83333in

Fig. 18: Cross-compiling tools installed in the host computer

In a Terminal window execute the following commands:

::

   $ cd build/host
   $ source environment-setup
   $ eclipse &

The *environment-setup* file contains the code listed below.

::

   cat <<'EOF'
    _           _ _     _                 _
   | |__  _   _(_) | __| |_ __ ___   ___ | |_
   | '_ \| | | | | |/ _` | '__/ _ \ / _ \| __|
   | |_) | |_| | | | (_| | | | (_) | (_) | |_
   |_.__/ \__,_|_|_|\__,_|_|  \___/ \___/ \__|

          Making embedded Linux easy!

   Some tips:
   * PATH now contains the SDK utilities
   * Standard autotools variables (CC, LD, CFLAGS) are exported
   * Kernel compilation variables (ARCH, CROSS_COMPILE, KERNELDIR) are exported
   * To configure do "./configure $CONFIGURE_FLAGS" or use
     the "configure" alias
   * To build CMake-based projects, use the "cmake" alias

   EOF
   if [ x"$BASH_VERSION" != x"" ] ; then
   	SDK_PATH=$(dirname $(realpath "${BASH_SOURCE[0]}"))
   elif [ x"$ZSH_VERSION" != x"" ] ; then
   	SDK_PATH=$(dirname $(realpath $0))
   else
   	echo "unsupported shell"
   fi
   export "AR=aarch64-buildroot-linux-gnu-gcc-ar"
   export "AS=aarch64-buildroot-linux-gnu-as"
   export "LD=aarch64-buildroot-linux-gnu-ld"
   export "NM=aarch64-buildroot-linux-gnu-gcc-nm"
   export "CC=aarch64-buildroot-linux-gnu-gcc"
   export "GCC=aarch64-buildroot-linux-gnu-gcc"
   export "CPP=aarch64-buildroot-linux-gnu-cpp"
   export "CXX=aarch64-buildroot-linux-gnu-g++"
   export "FC=aarch64-buildroot-linux-gnu-gfortran"
   export "F77=aarch64-buildroot-linux-gnu-gfortran"
   export "RANLIB=aarch64-buildroot-linux-gnu-gcc-ranlib"
   export "READELF=aarch64-buildroot-linux-gnu-readelf"
   export "STRIP=aarch64-buildroot-linux-gnu-strip"
   export "OBJCOPY=aarch64-buildroot-linux-gnu-objcopy"
   export "OBJDUMP=aarch64-buildroot-linux-gnu-objdump"
   export "AR_FOR_BUILD=/usr/bin/ar"
   export "AS_FOR_BUILD=/usr/bin/as"
   export "CC_FOR_BUILD=/usr/bin/gcc"
   export "GCC_FOR_BUILD=/usr/bin/gcc"
   export "CXX_FOR_BUILD=/usr/bin/g++"
   export "LD_FOR_BUILD=/usr/bin/ld"
   export "CPPFLAGS_FOR_BUILD=-I$SDK_PATH/include"
   export "CFLAGS_FOR_BUILD=-O2 -I$SDK_PATH/include"
   export "CXXFLAGS_FOR_BUILD=-O2 -I$SDK_PATH/include"
   export "LDFLAGS_FOR_BUILD=-L$SDK_PATH/lib -Wl,-rpath,$SDK_PATH/lib"
   export "FCFLAGS_FOR_BUILD="
   export "DEFAULT_ASSEMBLER=aarch64-buildroot-linux-gnu-as"
   export "DEFAULT_LINKER=aarch64-buildroot-linux-gnu-ld"
   export "CPPFLAGS=-D_LARGEFILE_SOURCE -D_LARGEFILE64_SOURCE -D_FILE_OFFSET_BITS=64"
   export "CFLAGS=-D_LARGEFILE_SOURCE -D_LARGEFILE64_SOURCE -D_FILE_OFFSET_BITS=64  -Os -g0 -D_FORTIFY_SOURCE=1"
   export "CXXFLAGS=-D_LARGEFILE_SOURCE -D_LARGEFILE64_SOURCE -D_FILE_OFFSET_BITS=64  -Os -g0 -D_FORTIFY_SOURCE=1"
   export "LDFLAGS="
   export "FCFLAGS= -Os -g0"
   export "FFLAGS= -Os -g0"
   export "PKG_CONFIG=pkg-config"
   export "STAGING_DIR=$SDK_PATH/aarch64-buildroot-linux-gnu/sysroot"
   export "INTLTOOL_PERL=/usr/bin/perl"
   export "ARCH=arm64"
   export "CROSS_COMPILE=aarch64-buildroot-linux-gnu-"
   export "CONFIGURE_FLAGS=--target=aarch64-buildroot-linux-gnu --host=aarch64-buildroot-linux-gnu --build=x86_64-pc-linux-gnu --prefix=/usr --exec-prefix=/usr --sysconfdir=/etc --localstatedir=/var --program-prefix="
   alias configure="./configure ${CONFIGURE_FLAGS}"
   alias cmake="cmake -DCMAKE_TOOLCHAIN_FILE=$SDK_PATH/share/buildroot/toolchainfile.cmake -DCMAKE_INSTALL_PREFIX=/usr"
   export "PATH=$SDK_PATH/bin:$SDK_PATH/sbin:$PATH"
   export "KERNELDIR=/home/ubuntu/Documents/rpi/build/build/linux-custom/"

This script when is source in a terminal window sets all the environment
variables needed to use the cross-compilation tools and add the folder
of cross-tools to the PATH linux variable.

The execution of eclipse popups a window inviting you to enter the
workspace (see Fig. 19). The workspace is the folder that contain
eclipse projects created by the user. You can have as many workspaces as
you want. Please specify a folder in your account.

+-------+--------------------------------------------------------------+
|       | **[Help]:** The figures displayed in the following           |
|       | paragraphs can be different depending on the Eclipse version |
|       | installed.                                                   |
+-------+--------------------------------------------------------------+

.. image:: rpi/media/image23.png
   :width: 5.19182in
   :height: 2.66458in

Fig. 19: Selection of the workspace for Eclipse. Use a folder in your
account.

Select Ok, and the welcome window of Eclipse will be shown (Fig. 20).
Next, close the welcome window and the main eclipse window will be
displayed (Fig. 21).

.. image:: rpi/media/image24.png
   :width: 5.17708in
   :height: 4.13683in

Fig. 20: Eclipse welcome window.

.. image:: rpi/media/image25.png
   :width: 5.78753in
   :height: 4.35417in

Fig. 21: Eclipse main window.

In a terminal window create an empty folder. In this folder create the
following files with the content described in the Table 2. The Makefile
uses the environment variables that are defined in the environment where
the makefile is run.

+----------------+-----------------------------------------------------+
| Filename       | Content                                             |
+================+=====================================================+
| Makefile       | LIBS= -lpthread -lm #Libraries used if needed       |
|                |                                                     |
|                | SRCS= main.cpp func.cpp                             |
|                |                                                     |
|                | BIN=app                                             |
|                |                                                     |
|                | CFLAGS+= -g -O0                                     |
|                |                                                     |
|                | OBJS=$(subst .cpp,.o,$(SRCS))                       |
|                |                                                     |
|                | all : $(BIN)                                        |
|                |                                                     |
|                | $(BIN): $(OBJS)                                     |
|                |                                                     |
|                | @echo [link] $@                                     |
|                |                                                     |
|                | $(CXX) -o $@ $(OBJS) $(LDFLAGS) $(LIBS)             |
|                |                                                     |
|                | %.o: %.cpp                                          |
|                |                                                     |
|                | @echo [Compile] $<                                  |
|                |                                                     |
|                | $(CXX) -c $(CFLAGS) $< -o $@                        |
|                |                                                     |
|                | clean:                                              |
|                |                                                     |
|                | @rm -f $(OBJS) $(BIN)                               |
+----------------+-----------------------------------------------------+
| main.cpp       | #include "func.h"                                   |
|                |                                                     |
|                | #include <iostream>                                 |
|                |                                                     |
|                | int main(void){                                     |
|                |                                                     |
|                | int b=2;                                            |
|                |                                                     |
|                | std::cout<<"A is: "<< fun(b) << std::endl;          |
|                |                                                     |
|                | }                                                   |
+----------------+-----------------------------------------------------+
| func.h         | #ifndef \__FUNC_H                                   |
|                |                                                     |
|                | #define \__FUNC_H                                   |
|                |                                                     |
|                | int fun(int);                                       |
|                |                                                     |
|                | #endif                                              |
+----------------+-----------------------------------------------------+
| func.cpp       | int fun(int b){                                     |
|                |                                                     |
|                | int a=b*2;                                          |
|                |                                                     |
|                | return a;                                           |
|                |                                                     |
|                | }                                                   |
+----------------+-----------------------------------------------------+

In Eclipse select in the left part of the windows Import *projects*. A
new window is popup, select then *C/C++* and the option *Existing Code
as Makefile Project*. The window shown in Fig. 22 is displayed. Complete
the name of the project, select the folder with the code and check
*Cross GCC in Toolchain for Indexer Settings*.

.. image:: rpi/media/image26.png
   :width: 4.45148in
   :height: 4.95833in

Fig. 22: Selecting the code.

Building a project
------------------

Once you have configured the cross-chain in Eclipse you can build your
project using Project->Build Project. If everything is correct, you will
see the eclipse project as represented in Fig. 29. You can clean the
project (remove the executable and objects) with *Clean*.

.. image:: rpi/media/image27.png
   :alt: A screenshot of a computer Description automatically generated
   :width: 6.69375in
   :height: 4.17014in

Fig. 23: Eclipse project compiled (Binaries has been generated)

+-------+--------------------------------------------------------------+
|       | **[Console in Eclipse]:** Have a look at the messages        |
|       | displayed in the Console. You will see how eclipse is        |
|       | calling the cross compiler with different parameters.        |
+-------+--------------------------------------------------------------+

Moving the binary to the target
-------------------------------

In order to copy the executable to the target, you have different
options. You can use the Linux application called “scp” or other similar
applications. In our case, we are going to use the “Other Locations….”
utility included in the nautilus explorer. Specify in Server Address
ssh://<ip address>

.. image:: rpi/media/image28.png
   :width: 5.57399in
   :height: 2.93365in

Fig. 24: “Connect to Server” option in Nautilus explorer

Executing the application
-------------------------

You can run the Raspberry PI program using putty (remember that once you
have a network connection available in the RPI you can also use putty to
connect to it).

.. image:: rpi/media/image29.png
   :alt: A screenshot of a computer Description automatically generated
   :width: 4.45in
   :height: 2.90434in

Fig. 25: Run test program in Raspberry Pi

+-------+--------------------------------------------------------------+
|       | Warning. If you experiment problems using ssh, delete the    |
|       | .ssh folder in your home directory.                          |
+-------+--------------------------------------------------------------+

Automatic debugging using gdb and gdbserver
-------------------------------------------

You can directly debug the program running in the RPI using Eclipse.
There are two methods to do it: manually and automatically. In the
manual method, firstly, you need to copy the executable program to the
RPI, change the file permissions to “executable” and execute the program
to be debugged using *gdbserver* utility. Of course, this is a
time-consuming process and very inefficient. The alternative solution is
to use automatic debugging. In order to debug your applications, we need
to define a debug session and configure it. Firstly, *Select Run->Debug
Configurations* and generate a new configuration under *C/C++ Remote
Application*. You need to complete the different tabs available in this
window. The first one is the main tab (see Fig. 33). You need to
configure here the path to the C/C++ application to be debugged, the
project name, the connection with the target (you will need to create a
new one using the IP address of your RPI), the remote path where your
executable file will be downloaded, and the mode for the debugging
(Automatic Remote Debugging Launcher). Secondly, in the argument tab,
you can specify the arguments of your executable program. It is very
important here that you can also specify the working directory path
where the executable will be copied and launched (you need to have
rights in this folder).

.. image:: rpi/media/image30.png
   :alt: A screenshot of a computer Description automatically generated
   :width: 6.69375in
   :height: 3.94931in

Fig. 26: Creating a Debug Configuration

In the debugger window you need to configure the path of your cross gdb
application. Remember that we are working with a cross-compiler, cross
debugging. Therefore, you need to provide here the correct path of your
gdb. The GDB command file (.gdbinit) must be specified, providing a path
with an empty file. In the Gdbserver settings tab, you need to provide
the path to the gdbserver in the target and the TCP/IP port used (by
default 2345).

.. image:: rpi/media/image30.png
   :alt: A screenshot of a computer Description automatically generated
   :width: 6.03905in
   :height: 3.56303in

Fig. 27: Debug configuration, including the path to locate the cross gdb
tool.

Now, press Debug in Eclipse window, and you can debug your application
remotely.

.. image:: rpi/media/image31.png
   :alt: A screenshot of a computer Description automatically generated
   :width: 5.89423in
   :height: 3.67021in

Fig. 28: Debugging session on the RPI remotely

Preparing the linux virtual machine.
====================================

Download VMware Workstation Player.
-----------------------------------

The link https://www.vmware.com/support/pubs/player_pubs.html contains
documentation describing the installation and basic use of VMware
Workstation Player. Follow the instructions to set up the application on
your computer.

Installing Ubuntu 22.04 LTS as a virtual machine.
-------------------------------------------------

+-------+--------------------------------------------------------------+
|       | **[Ubuntu version]:** It is mandatory to install Ubuntu      |
|       | 22.04 version.                                               |
+-------+--------------------------------------------------------------+

The first step is to download Ubuntu 22.04.3 (64 bit PC) from Ubuntu web
site using this link: http://releases.ubuntu.com/ . You will download an
ISO image with this Linux operating System.Run WMware player and install
Ubuntu using the VMWare player instructions. Consider the following when
creating the virtual machine: you need at least 150Gbytes of hard disk
space (in multiple files), 3GByte of RAM, and, if possible 4 processors.
The installation time will be half an hour, more or less, depending on
your computer. Moving a virtual machine from one computer to another is
a time-consuming task; therefore, take this into account to minimize the
development time.

Installing synaptic
-------------------

If you need to install software packages, you can do it using the linux
terminal command apt-get. Another alternative process is the use of the
synaptic utility. In order to use it, you need to install it using this
command:

::

   $ sudo apt-get install synaptic

Once installed, you can search and execute the synaptic program. When
you click two times over the package, it will show all the dependent
packages that would be installed.

.. image:: rpi/media/image32.png
   :alt: A screenshot of a computer Description automatically generated
   :width: 6.69375in
   :height: 3.32431in

Fig. 30: Synaptic window

Installing putty
----------------

You need to execute:

-  sudo apt-get install putty

Installing packages for supporting Buildroot.
---------------------------------------------

Using buildroot requires some software packages that have to be
installed in the VM. These are listed in this link
http://buildroot.uclibc.org/downloads/manual/manual.html#requirement.
You need to install at least:

-  g++

-  git

Installing packages supporting Eclipse
--------------------------------------

You need to install:

-  eclipse-cdt (eclipse C/C++ programming)

-  eclipse-rse (eclipse remote explorer)

-  eclipse-cdt-launch-remote (eclipse for remote debugging)



