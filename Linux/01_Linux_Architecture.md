# Linux Architecture

- Kernal ----> Drivers(Modules) ----> Hardware

## Kernal space 
- Unrestricted environment
- Kernal needs full access to the hardware using drivers called Modules

## User space 
- Restricted environment

![basic archs](<basic_archs.png>)

## Role of Kernal
- heart of the Operating System

## UID 0 - Root user
- UID 0 has all the capabilities
- In /etc/passwd, UID 0 is assigned to the root user
- Even after removing the /etc/passwd, the system UID 0 still exists and there are no limitations for this UID

***That meas root user is defined pretty deeper in the Operating system***

## Drivers, Kernal Modules and Device Files:

![device nodes](<Screenshot 2025-11-26 at 10.09.55 PM.png>)


![device_mapping_kernal](<Screenshot 2025-11-26 at 10.16.53 PM.png>)

## GNU Lib C:

- It is core component in Linux which required to make the application to work.

- It implements the C standard library, which contains standard functions that can be used by all programs writtten in C

- As such, It provides core Linux facilities, such as open, read, write, malloc, orintf and more

## Shell

![shell](<Screenshot 2025-11-26 at 10.24.23 PM.png>)

## File Descriptors:

![filedescriptors](<Screenshot 2025-11-26 at 10.32.45 PM.png>)

## 2. Bootloading

- GRUB2 is the common boot loader on Linux

## 3. where is GRUB stored? 

- On an BIOS, system the first 512 bytes on disk are the boot loader 
- 446 bytes are used for GRUB code
- 64 bytes are used for the partition table

## Why kernals are not required to compile anymore? 

- Eariler they developed monolithic kernal 
- Later modular kernal was introduced. 
- So to add a drivers kernal no need to be compiled anymore

## Kernal interface

![syscalls](<Screenshot 2025-11-30 at 7.58.14 AM.png>)

## Kernals Modules Tuning

- Kernal modules are loaded via initramfs/initrd
- Initramfs - RAM file system compiled for kernal tocontain all the required modules - This is happening when you install the system not repeated everytime
- systemd-udevd - powerful part of systemd reacting on hardware detection - works together with kernal and loads the appropriate driver
- Manually using modprobe
- `lspci -k` - Used listing the devices which kernal modules are used
- `modinfo e1000e` - Used to check whether this kernal module has any params to accept
- `lsmod` -  to check whether this module is loaded to or not
- `lsmod | grep e1000e` - This is to check whether this module has loaded or not! `e1000e                307200  0` - 0 indicates that this module is not dependent with any other module. So it is safe to remove incase if we needed. 
- `modprobe -r e1000e` - this is just remove the module 
- `modprobe e1000e debug=4` - this is to add module again

## `/proc` psedueo file system

- `/proc` is pseudo file system that provides the nterface to kernal data structures
- this /proc file system doesn't give you the access to block device instead it will give direct access to the kernal interface
- Kernal also uses the other file systems like sysfs and debugfs
- Under `/proc` we will finf the below three informations
1. `/proc/nnn` - This is where the kernal keeps all the running process. These dirs are referred to as a PID directories
2. `/proc/sys` - Here you will find kernal updates 
3. `/proc/*` - Here you fill find many files which contains the status information about the running system

## `/proc/sys` file system

- In this file system we can see all the kernal Tunable paramters! We allowed to change certain variables over here.

## `/proc/sysrq` file system (Testing the Criitcal Kernal features with sysrq)
- Provides an interface to the kernal to perform some advanced operations on the kernal. 
- Below options are useful for testing how a system reacts when problems occur.
- `echo c > /proc/sysrq-trigger` - crashes your system
- `echo f > /proc/sysrq-trigger` - Triggers the OOM killer
- `echo i > /proc/sysrq-trigger` - kills all processes
- `echo b > /proc/sysrq-trigger` - resets the system

## Using Watchdogs

- Watchdogs can be used to reset the system if any serious problem occurs! 
- Ensure the watchdog service is enabled and started using systemctl enable now --watchdog 
- This daemon writes to /dev/wahcdog once a minute by default. (Configure it in /etc/wathcdog.conf)
- If the daemon stops to writing it the system considered to be failing, and watchdog will reset the system
- It prevents the system hanging forever. It immediately reboot the systems

## eBPF:

- eBPF is technology that originates from the Linux kernal and makes it possible to change kernal behaviour without having to change the kernal module or adding modules

# System Taking Over - systemd
- Systemd automatically boots when the system starts
- Wnen entering the minimal troubleshooting mode with the boot argument rd.break, an initramfs init process is loaded and there will be no systemd
- Wnen entering the minimal troubleshooting mode with the GRUB2 process argument init=/bin/bash is loaded as init process.

![systemd](<Screenshot 2025-12-01 at 7.11.57 AM.png>)

![alt text](<Screenshot 2025-12-01 at 7.14.41 AM.png>)