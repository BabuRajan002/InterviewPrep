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
- How to setup password for the grub2 bootloader 
```
  379  grub2-set-password 
  380  vi /boot/loader/entries/
  381  vi /boot/loader/entries/c6a3eec54e9149dd83b6adbbf9378c40-5.14.0-642.el9.aarch64.conf 
  382  uname -r
  383  vi /boot/loader/entries/c6a3eec54e9149dd83b6adbbf9378c40-5.14.0-645.el9.aarch64.conf 
  384  reboot

```

## Updating and Modifying the initramfs:

- `dracut -f` - Used in Redhat Family for updating the initramfs

## How to install ext4 driver in the initramfs? 

-  ``` 385  lsinitrd 
  386  lsinitrd | grep ext4
  387  clear
  388  vi /etc/dracut.conf
  389  vi /etc/dracut.conf.d/ext4.conf
  390  dracut -f 
  391  lsinitrd | grep ext4 ```

## Sewrvice Managers:(Systemd)

- Service managers take care of everything after the kernal and initrd have been loaded, and the root file system has beem mounted.
- this consists of two stages 
  - Initialize the remianing hardware devices
  - Mounting the file systems
  - starting the services
## Accessing the Early boot shell
- `systemd.unit=emergency.target` or `systemd.unit=rescue.target`
- emergency.target is too early just has the minimal functionalities
- rescue.target - Is stops the system before laoding the services.
- rd.break or init=/bin/bash - Troubleshooting environment before the systemd is started.

# Real world scenario: Recovering from the LOST MBR:
- Step1: `dd if=/dev/zero of=/dev/sda bs=1 count=446` - Wiping out the boot records from the disk which contains the grub2 bootloader.
- Step2: `reboot`
- Step3: After the reboot it went to the installation disk. 
- Step4: select Troubleshooting option

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

- Unit files are written in three locations: 
- /etc/systemd/system - Administrator environment, highest priority 
- `/run/systemd/system` - non-persistent
- `/usr/lib/systemd/system` - Package provided, lowest priority

# Managing resource allocation:

- Systemd can be integrated with cgroups
- Cgroups is offered by Linux kernal. They allow us to limit the available resources.
- Crgoups can be used to limit resource availability to systemd services
- Resources are assigned to slices, scopes and services.
- slice is big environment, scope smaller to that.
- Slices you can consider its a big environment
- Slices are divided into three: 
  1. system slice      
      i. sshd services 
      ii. httpd.service  etc..
  2. Machine slice
  3. user.slice
     i. 1000(user) slice.      
     ![manage resources](<Screenshot 2025-12-09 at 6.49.56 PM.png>)
     ii. Under it we have different types of process which has a different CPU weights.
- Relevant parameters in Cgroup v1:
  - CPU Accounting, CPUQuota, CPUSHARES
  - MemoryAccounting, MemoryLimit
  - TaskAccounting, TasksMax
  - BlocIOAccounting, BlockIOWeight, BlockIODevicesWeight

- Relevant Parameters in Cgour v2: 
  - CPU Weight, 
  - Memory Max
  - IO* instead BlocIO

- How to switch off the one of CPU to offline? 

`echo 0 /sys/bus/cpu/devices/cpu1/online` - this will turn off one of the cpu cores.

# Managing the resource Allocation:

- systemctl set-property --runtime httpd CPUShares=2048

## How do you allocate the resource to services using systemd? 

`systemctl set-property --runtime httpd CPUShares=2048` ---> Non persistent. Temp file will be created in /run
`systemctl set-property httpd CPUShares=2048` --> Set persistent under `/etc/systemd/system`

## Creating Custom units: 

- `type=simple` - Runs the process sepcified with `ExecStart`
- `type=oneshot` - Like simple, but waits for the process to exit before starting anuything else

## Creating a Custom Targets:

- A target is just a group of units
- If a target contains the `AllowIsolate=yes` option, it can be used to boot the system in a specific state

## How a terget exactly knows which unit to start? 

- That will be present inside the `/etc/systemd/system/my.target`

## Running user process in systemd

- Users can run units in systemd
- The Unit files for user processes are in: 
- User processes are started when the user logs in
- To start a user process on system boot, the `loginctl linger` feature needs to be enabled for that user.
- After enabling linger, the user can set a process to be started automatically

# Real World Scenario : Booting without /etc/fstab

- Mount can be taken care by systemd in this case fstab is not required.
- under `/run/systemd/generator` - We have boot.mount and `-.mount` 
- `boot.mount` - Will be used to mount under boot directory
- `-.mount` - used to mount the root filesystem

# Understanding Hardware Access

- Kernal drivers are used to load drivers for devices
- To access these drivers, a representation in user space is needed
- This representation is made by device nodes in /dev


![devices](<Screenshot 2025-12-10 at 6.35.00 PM.png>)

![majorAndMinorDevices](<Screenshot 2025-12-10 at 6.36.28 PM.png>)

## How devices are initialized? 

- Statically - through Initramfs or initrd
- Dynamically - systemd-udevd - Is plug and play manager and it is used when devices are plugged/removed
- Manually - mknod - not commonly used anywhere. Used to recover the lost devices

## systemd-udevd - Hardware handling in modern linux systems

- It is considered the plug and play manager on Linux
- When hardware events are detected, it processes rules to initialize devices