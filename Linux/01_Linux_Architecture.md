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