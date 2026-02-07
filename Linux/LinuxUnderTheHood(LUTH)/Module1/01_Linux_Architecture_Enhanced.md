# Linux Architecture - Comprehensive Guide

## Table of Contents
1. [Linux Architecture Overview](#linux-architecture-overview)
2. [Kernel Space vs User Space](#kernel-space-vs-user-space)
3. [Root User and UID 0](#root-user-and-uid-0)
4. [Kernel Modules and Device Files](#kernel-modules-and-device-files)
5. [GNU C Library (glibc)](#gnu-c-library-glibc)
6. [Shell and File Descriptors](#shell-and-file-descriptors)
7. [Boot Process](#boot-process)
8. [Kernel Modules Management](#kernel-modules-management)
9. [Proc Filesystem](#proc-filesystem)
10. [Systemd](#systemd)
11. [Resource Management with Cgroups](#resource-management-with-cgroups)
12. [Hardware Access](#hardware-access)

---

## Linux Architecture Overview

**Architecture Flow:**
```
Kernel → Drivers (Modules) → Hardware
```

The Linux system is built on a layered architecture where:
- The **kernel** acts as the core of the operating system
- **Drivers (modules)** provide interfaces to hardware devices
- **Hardware** represents the physical components

### Key Benefits of This Architecture:
- Modularity and flexibility
- Hardware abstraction
- Portability across different platforms
- Security through privilege separation

---

## Kernel Space vs User Space

### Kernel Space
- **Unrestricted environment** with full system privileges
- The kernel requires complete access to hardware using drivers called **modules**
- Direct memory access and hardware manipulation
- Critical for system stability and security
- Protected from user applications

### User Space
- **Restricted environment** where applications run
- Limited access to hardware and system resources
- Applications must make system calls to access kernel services
- Provides isolation between processes for security
- Prevents user programs from crashing the entire system

### Why This Separation Matters:
- **Security**: Prevents malicious or buggy applications from compromising the system
- **Stability**: User program crashes don't bring down the kernel
- **Isolation**: Each process runs in its own protected memory space

---

## Role of Kernel

The kernel is the **heart of the Operating System** and performs critical functions:

1. **Process Management**: Creates, schedules, and terminates processes
2. **Memory Management**: Allocates and manages system memory
3. **Device Management**: Controls hardware through drivers
4. **File System Management**: Provides abstraction for storage devices
5. **Network Stack**: Handles network protocols and communication
6. **Security**: Enforces access controls and permissions
7. **System Calls**: Provides interface between user space and kernel space

---

## Root User and UID 0

### Understanding UID 0
- **UID 0** has all system capabilities - the superuser
- Defined in `/etc/passwd`, UID 0 is assigned to the root user
- Even if `/etc/passwd` is removed, UID 0 still exists and retains all privileges
- This means **root user is defined deep within the operating system kernel**, not just in configuration files

### Important Security Notes:
- Any account with UID 0 has root privileges, regardless of username
- Root access should be carefully controlled and monitored
- Use `sudo` instead of direct root login for better auditing
- Modern systems use capabilities to grant specific privileges without full root access

### Linux Capabilities:
Linux capabilities divide root privileges into distinct units:
- `CAP_NET_ADMIN`: Network administration
- `CAP_SYS_TIME`: Modify system clock
- `CAP_CHOWN`: Change file ownership
- This allows programs to run with only necessary privileges

---

## Kernel Modules and Device Files

### Understanding Device Nodes
- Device files in `/dev` represent hardware devices
- Character devices (e.g., `/dev/tty`, `/dev/null`) - data as stream of bytes
- Block devices (e.g., `/dev/sda`, `/dev/nvme0n1`) - data in blocks
- Device files have major and minor numbers identifying the driver and device instance

### Device Mapping:
```
Application → Device File (/dev/xxx) → Kernel Driver → Hardware
```

### Types of Devices:
1. **Character Devices**: Sequential access (keyboards, mice, serial ports)
2. **Block Devices**: Random access (hard drives, USB drives)
3. **Network Devices**: Special case, accessed through sockets (eth0, wlan0)
4. **Pseudo Devices**: Virtual devices like `/dev/null`, `/dev/zero`, `/dev/random`

---

## GNU C Library (glibc)

### What is glibc?
- Core component in Linux required for applications to function
- Implements the **C standard library** with functions used by programs written in C
- Provides essential Linux facilities including:
  - `open()` - Open files
  - `read()` and `write()` - I/O operations
  - `malloc()` and `free()` - Memory allocation
  - `printf()` - Formatted output
  - Socket functions for networking
  - Thread management (POSIX threads)

### Why It Matters:
- Almost all Linux programs depend on glibc
- Provides consistent API across different Linux distributions
- Optimized for performance on various architectures
- Acts as the bridge between applications and kernel system calls

### Alternative C Libraries:
- **musl libc**: Lightweight alternative for embedded systems
- **uClibc**: Small C library for embedded Linux
- **Bionic**: Used in Android

---

## Shell and File Descriptors

### Shell
The shell is a **command-line interpreter** that:
- Provides interface between user and kernel
- Executes commands and scripts
- Common shells: bash, zsh, sh, fish, dash
- Supports scripting, job control, and redirection

### File Descriptors

File descriptors are integer handles representing open files or I/O streams:

| FD Number | Standard Name | Purpose | Symbol |
|-----------|---------------|---------|--------|
| 0 | stdin | Standard Input | `<` |
| 1 | stdout | Standard Output | `>` |
| 2 | stderr | Standard Error | `2>` |

### Redirection Examples:
```bash
command > output.txt          # Redirect stdout to file
command 2> error.txt          # Redirect stderr to file
command &> all.txt            # Redirect both stdout and stderr
command < input.txt           # Redirect file to stdin
command 2>&1                  # Redirect stderr to stdout
command | another_command     # Pipe stdout to another command
```

### Advanced Usage:
- File descriptors 3-9 (and beyond) can be used for custom I/O
- `/dev/fd/` directory shows open file descriptors
- `exec` can redirect FDs for entire script

---

## Boot Process

### GRUB2 - The Boot Loader
**GRUB2** (Grand Unified Bootloader version 2) is the standard boot loader on Linux systems.

### Where is GRUB Stored?

**On BIOS Systems:**
- First **512 bytes** on disk form the Master Boot Record (MBR)
- **446 bytes** contain GRUB boot code
- **64 bytes** store the partition table
- **2 bytes** for boot signature (0x55AA)

**On UEFI Systems:**
- GRUB is stored as an EFI application in the EFI System Partition (ESP)
- Usually located at `/boot/efi/EFI/[distro]/grubx64.efi`
- No MBR limitations; can use GPT partitioning

### Boot Sequence:
1. **BIOS/UEFI** initializes hardware
2. **GRUB** loads and presents boot menu
3. **Kernel** is loaded into memory
4. **initramfs/initrd** provides initial root filesystem
5. **systemd** (or init) starts as PID 1
6. **System services** are initialized
7. **Login prompt** appears

### GRUB Configuration:
- Main config: `/boot/grub2/grub.cfg` (auto-generated)
- User settings: `/etc/default/grub`
- Custom entries: `/etc/grub.d/`
- Regenerate with: `grub2-mkconfig -o /boot/grub2/grub.cfg`

---

## Why Kernels Don't Need Recompilation Anymore

### Monolithic vs Modular Kernels

**Earlier: Monolithic Kernel**
- All drivers compiled directly into the kernel
- Adding hardware support required kernel recompilation
- Large kernel size
- Inflexible and time-consuming

**Modern: Modular Kernel**
- Kernel modules can be loaded/unloaded dynamically
- Add driver support without recompiling the kernel
- Smaller core kernel size
- Flexible and efficient

### Benefits of Modular Approach:
- **Dynamic Loading**: Load modules only when needed
- **Reduced Memory Usage**: Only active modules consume memory
- **Easier Updates**: Update individual modules without kernel rebuild
- **Hardware Flexibility**: Support new hardware by adding modules
- **Faster Boot**: Load only essential modules initially

---

## Kernel Modules Management

### Loading Modules

**Automatic Loading Methods:**
1. **initramfs/initrd**: RAM filesystem containing essential modules loaded at boot
   - Created during system installation
   - Rebuilt when kernel is updated

2. **systemd-udevd**: Dynamic hardware detection
   - Reacts to hardware events (hotplug)
   - Works with kernel to load appropriate drivers
   - Handles USB devices, network cards, etc.

3. **Manual Loading**: Using `modprobe` command

### Essential Commands:

```bash
# List PCI devices and their kernel modules
lspci -k

# Show module information
modinfo e1000e

# List loaded modules
lsmod

# Check if specific module is loaded
lsmod | grep e1000e
# Output: e1000e    307200  0
# The "0" indicates no dependencies, safe to remove

# Remove a module
modprobe -r e1000e

# Load a module with parameters
modprobe e1000e debug=4

# Show module dependencies
modprobe --show-depends e1000e

# List all available modules
find /lib/modules/$(uname -r) -name "*.ko*"
```

### Module Configuration:
- Module parameters: `/etc/modprobe.d/`
- Blacklist modules: `/etc/modprobe.d/blacklist.conf`
- Auto-load modules: `/etc/modules-load.d/`

### Kernel Module Locations:
- `/lib/modules/$(uname -r)/`: Module files
- `/sys/module/`: Runtime module information
- `/proc/modules`: Currently loaded modules

---

## Proc Filesystem

### What is `/proc`?

The `/proc` filesystem is a **pseudo filesystem** that provides an interface to kernel data structures:
- Not a real filesystem on disk
- Dynamically generated by the kernel
- Provides direct access to kernel information
- Read and sometimes write access to kernel parameters

### Other Kernel Filesystems:
- **sysfs** (`/sys`): Device and driver information
- **debugfs** (`/sys/kernel/debug`): Kernel debugging information
- **configfs**: Kernel object configuration

### Three Main Areas in `/proc`:

#### 1. `/proc/[PID]` - Process Information
Each running process has a directory with its PID containing:
```bash
/proc/1234/cmdline     # Command line that started the process
/proc/1234/status      # Process status information
/proc/1234/fd/         # File descriptors opened by process
/proc/1234/maps        # Memory mapping
/proc/1234/environ     # Environment variables
/proc/1234/cwd         # Current working directory (symlink)
/proc/1234/exe         # Executable file (symlink)
```

#### 2. `/proc/sys` - Kernel Tunable Parameters
Allows reading and modifying kernel parameters:
```bash
/proc/sys/net/         # Network parameters
/proc/sys/kernel/      # Kernel parameters
/proc/sys/vm/          # Virtual memory parameters
/proc/sys/fs/          # Filesystem parameters
```

**Examples:**
```bash
# View parameter
cat /proc/sys/net/ipv4/ip_forward

# Modify parameter (temporary)
echo 1 > /proc/sys/net/ipv4/ip_forward

# Permanent changes via sysctl
echo "net.ipv4.ip_forward = 1" >> /etc/sysctl.conf
sysctl -p
```

#### 3. `/proc/*` - System Status Information
Various files containing system information:
```bash
/proc/cpuinfo          # CPU information
/proc/meminfo          # Memory information
/proc/version          # Kernel version
/proc/uptime           # System uptime
/proc/loadavg          # Load average
/proc/mounts           # Mounted filesystems
/proc/partitions       # Partition information
/proc/swaps            # Swap space usage
```

### `/proc/sysrq-trigger` - Testing Critical Kernel Features

**SysRq** provides an interface for advanced kernel operations:

```bash
# Crash the system (for testing crash dumps)
echo c > /proc/sysrq-trigger

# Trigger Out-Of-Memory killer
echo f > /proc/sysrq-trigger

# Kill all processes (except init)
echo i > /proc/sysrq-trigger

# Immediate system reboot
echo b > /proc/sysrq-trigger

# Sync all filesystems
echo s > /proc/sysrq-trigger

# Remount filesystems read-only
echo u > /proc/sysrq-trigger
```

**WARNING**: These commands are dangerous! Use only for testing in controlled environments.

### Enabling SysRq:
```bash
# Enable all SysRq functions
echo 1 > /proc/sys/kernel/sysrq

# Or use specific bitmask for selective features
```

---

## Using Watchdogs

### What Are Watchdogs?
Hardware or software timers that **automatically reset the system** if serious problems occur.

### How Watchdogs Work:
1. Watchdog service writes to `/dev/watchdog` periodically (default: every minute)
2. If writes stop, the system is considered frozen
3. Watchdog hardware/software triggers system reset
4. Prevents indefinite system hangs

### Configuration:

```bash
# Enable and start watchdog service
systemctl enable --now watchdog

# Configuration file
/etc/watchdog.conf
```

**Common Configuration Options:**
```
watchdog-device = /dev/watchdog
watchdog-timeout = 60
interval = 10
max-load-1 = 24
```

### Use Cases:
- Mission-critical servers
- Embedded systems
- Remote systems without physical access
- High-availability environments

---

## eBPF (Extended Berkeley Packet Filter)

### What is eBPF?

**eBPF** is revolutionary technology that allows you to:
- Change kernel behavior **without** modifying kernel source
- Run sandboxed programs in the kernel
- No need to add or change kernel modules
- Safe and efficient kernel extensibility

### Key Features:
1. **Safety**: Programs are verified before execution
2. **Performance**: Runs in kernel space, no context switching
3. **Flexibility**: Can hook into various kernel subsystems
4. **Dynamic**: Load and unload programs at runtime

### Common Use Cases:
- **Networking**: High-performance packet filtering and routing
- **Observability**: System and application monitoring
- **Security**: Runtime security enforcement
- **Tracing**: Performance analysis and debugging

### Popular eBPF Tools:
- **bpftrace**: High-level tracing language
- **BCC (BPF Compiler Collection)**: eBPF program development tools
- **Cilium**: Kubernetes networking and security
- **Falco**: Runtime security monitoring

### Example Use Cases:
```bash
# Trace system calls
bpftrace -e 'tracepoint:syscalls:sys_enter_* { @[probe] = count(); }'

# Monitor network connections
bpftrace -e 'tracepoint:sock:inet_sock_set_state { @[args->newstate] = count(); }'
```

---

## Systemd

### System Initialization

**Systemd** is the modern init system and service manager for Linux:
- Automatically boots when the system starts (PID 1)
- Manages system services, devices, and mounts
- Parallel service startup for faster boot times
- On-demand starting of services

### Troubleshooting Modes:

**Without Systemd:**
- Boot with `rd.break`: Loads minimal **initramfs** init process, no systemd
- Boot with `init=/bin/bash`: Loads bash directly as init process

### Systemd Architecture:

**Unit Types:**
- `.service`: System services
- `.socket`: IPC/network sockets
- `.target`: Group of units
- `.mount`: Filesystem mount points
- `.timer`: Scheduled tasks
- `.path`: Path-based activation
- `.device`: Device units

### Unit File Locations (Priority Order):

1. **`/etc/systemd/system/`**
   - Administrator customizations
   - **Highest priority**
   - Changes persist across updates

2. **`/run/systemd/system/`**
   - Runtime units
   - **Non-persistent** (lost on reboot)

3. **`/usr/lib/systemd/system/`**
   - Package-provided units
   - **Lowest priority**
   - Overridden by admin configs

### Common Systemd Commands:

```bash
# Service management
systemctl start service_name
systemctl stop service_name
systemctl restart service_name
systemctl status service_name
systemctl enable service_name      # Auto-start at boot
systemctl disable service_name

# System state
systemctl list-units
systemctl list-unit-files
systemctl list-dependencies
systemctl get-default              # Default target
systemctl set-default multi-user.target

# Logs
journalctl -u service_name
journalctl -f                      # Follow logs
journalctl -b                      # Current boot
journalctl --since "1 hour ago"
```

---

## Resource Management with Cgroups

### What are Cgroups?

**Control Groups (cgroups)** are a Linux kernel feature that:
- Limit and isolate resource usage
- Track resource consumption
- Prioritize resource allocation
- Control process groups

### Systemd Integration

Systemd integrates with cgroups to manage system resources:
- Resources assigned to **slices**, **scopes**, and **services**
- Hierarchical organization
- Both cgroup v1 and v2 support

### Cgroup Hierarchy:

```
Root
├── system.slice
│   ├── sshd.service
│   ├── httpd.service
│   └── nginx.service
├── user.slice
│   ├── user-1000.slice
│   │   ├── session-1.scope
│   │   └── user@1000.service
│   └── user-1001.slice
└── machine.slice
    ├── vm1.service
    └── container1.service
```

### Understanding Slices:

1. **system.slice**
   - System services
   - Daemons and background services

2. **user.slice**
   - User sessions
   - User services
   - Per-user resource limits

3. **machine.slice**
   - Virtual machines
   - Containers

### Cgroup v1 Parameters:

```
CPUAccounting=yes
CPUQuota=50%
CPUShares=1024
MemoryAccounting=yes
MemoryLimit=1G
TasksAccounting=yes
TasksMax=100
BlockIOAccounting=yes
BlockIOWeight=500
```

### Cgroup v2 Parameters:

```
CPUWeight=100               # Range: 1-10000
MemoryMax=1G
MemoryHigh=800M
IOWeight=100                # Replaces BlockIO
```

### Setting Resource Limits:

```bash
# Non-persistent (runtime only)
systemctl set-property --runtime httpd.service CPUShares=2048

# Persistent (survives reboot)
systemctl set-property httpd.service CPUShares=2048

# View current settings
systemctl show httpd.service -p CPUShares

# Slice-wide limits
systemctl set-property user.slice MemoryMax=4G
```

### CPU Hotplugging:

```bash
# Take CPU offline
echo 0 > /sys/devices/system/cpu/cpu1/online

# Bring CPU online
echo 1 > /sys/devices/system/cpu/cpu1/online

# Check CPU status
cat /sys/devices/system/cpu/cpu*/online
```

### Monitoring Resource Usage:

```bash
# Show cgroup tree
systemd-cgls

# Show resource usage
systemd-cgtop

# Detailed service resource usage
systemctl status httpd.service
```

---

## Creating Custom Units

### Unit Types:

**`Type=simple`**
- Runs the process specified with `ExecStart`
- Default type if not specified
- systemd considers it started immediately

**`Type=oneshot`**
- Similar to simple
- Waits for process to exit before starting other units
- Useful for initialization scripts

**`Type=forking`**
- For daemons that fork into background
- systemd waits for parent process to exit

**`Type=notify`**
- Service notifies systemd when ready
- Uses `sd_notify()` function

### Example Custom Service:

```ini
[Unit]
Description=My Custom Application
After=network.target

[Service]
Type=simple
User=appuser
WorkingDirectory=/opt/myapp
ExecStart=/opt/myapp/bin/myapp
Restart=on-failure
RestartSec=5s

[Install]
WantedBy=multi-user.target
```

### Creating Custom Targets:

A **target** is a group of units that defines a system state:

```ini
[Unit]
Description=My Custom Target
Requires=basic.target
Conflicts=rescue.service rescue.target
AllowIsolate=yes

[Install]
WantedBy=multi-user.target
```

**Note**: `AllowIsolate=yes` allows booting directly into this target with `systemctl isolate my.target`

### How Targets Know Which Units to Start:

Dependencies defined through:
- `Requires=`: Strict dependency
- `Wants=`: Weak dependency
- `WantedBy=`: Reverse dependency (in [Install] section)

Configuration in `/etc/systemd/system/my.target.wants/` contains symlinks to required units.

---

## Running User Processes in Systemd

### User Units

Users can manage their own systemd units:

**Unit File Locations for User:**
- `~/.config/systemd/user/`: User-specific units
- `/etc/systemd/user/`: System-wide user units
- `/usr/lib/systemd/user/`: Package-provided user units

### User Service Management:

```bash
# User commands (--user flag)
systemctl --user start myservice
systemctl --user enable myservice
systemctl --user status myservice

# View user unit files
systemctl --user list-unit-files
```

### Loginctl Linger

**Problem**: User services stop when user logs out

**Solution**: Enable **linger** for persistent user services

```bash
# Enable linger for current user
loginctl enable-linger

# Enable linger for specific user
loginctl enable-linger username

# Check linger status
loginctl show-user username

# Disable linger
loginctl disable-linger username
```

After enabling linger:
- User services start at system boot
- Services continue running after logout
- Useful for user-level daemons and cron jobs

### Example User Service:

```ini
# ~/.config/systemd/user/myapp.service
[Unit]
Description=My User Application

[Service]
Type=simple
ExecStart=/home/user/bin/myapp

[Install]
WantedBy=default.target
```

---

## Real World Scenario: Booting Without `/etc/fstab`

### Systemd Mount Management

Modern systems can boot without `/etc/fstab` because systemd handles mounts:

### Generated Mount Units:

Located in **`/run/systemd/generator/`**:

1. **`-.mount`**
   - Mounts the root filesystem
   - Generated from kernel command line

2. **`boot.mount`**
   - Mounts `/boot` partition
   - Generated from various sources

### How It Works:

1. **systemd-fstab-generator** reads `/etc/fstab`
2. Generates `.mount` units dynamically
3. Units placed in `/run/systemd/generator/`
4. systemd mounts filesystems using these units

### Viewing Mount Units:

```bash
# List all mount units
systemctl list-units -t mount

# Status of specific mount
systemctl status boot.mount

# View generated units
ls -l /run/systemd/generator/
```

### Benefits:
- Better error handling
- Parallel mounting
- Integration with systemd dependency system
- Can still use `/etc/fstab` for compatibility

---

## Understanding Hardware Access

### Device Representation

**Kernel drivers** load drivers for hardware devices, but user space needs access:
- Device nodes in `/dev/` represent hardware
- Provide interface between user applications and kernel drivers

### Device Types:

```
brw-rw---- 1 root disk 8, 0 Dec 10 18:00 /dev/sda    # Block device
crw-rw-rw- 1 root tty  5, 0 Dec 10 18:00 /dev/tty    # Character device
```

**Format**: `[type][permissions] [owner] [group] [major],[minor] [date] [name]`

- **Type**: `b` (block), `c` (character)
- **Major number**: Identifies the driver
- **Minor number**: Identifies the specific device instance

### Major and Minor Numbers:

```bash
# View device numbers
ls -l /dev/sda*
brw-rw---- 1 root disk 8, 0 Dec 10 /dev/sda
brw-rw---- 1 root disk 8, 1 Dec 10 /dev/sda1
brw-rw---- 1 root disk 8, 2 Dec 10 /dev/sda2

# Major 8 = SCSI disk driver
# Minor 0 = First disk (sda)
# Minor 1 = First partition (sda1)
# Minor 2 = Second partition (sda2)
```

### Device Initialization Methods:

#### 1. **Static - Through initramfs/initrd**
- Essential devices loaded at boot
- Compiled into initial RAM filesystem
- Contains critical drivers for boot process

#### 2. **Dynamic - systemd-udevd**
- Modern **plug-and-play** manager
- Reacts to hardware events (hotplug)
- Automatically loads drivers when devices are plugged in/removed
- Creates device nodes dynamically

#### 3. **Manual - mknod**
- Rarely used in modern systems
- Useful for recovery scenarios
- Create device nodes manually

```bash
# Create device node manually
mknod /dev/mydevice c 250 0

# Create block device
mknod /dev/myblock b 8 16
```

---

## systemd-udevd - Modern Hardware Handling

### What is udev?

**systemd-udevd** is the **device manager** for Linux:
- Dynamically manages device nodes in `/dev/`
- Listens for kernel hardware events (uevents)
- Processes rules to configure devices
- Sets permissions and ownership
- Creates symbolic links
- Runs programs in response to events

### udev Rules:

Located in:
- `/usr/lib/udev/rules.d/`: System default rules
- `/etc/udev/rules.d/`: Administrator custom rules

**Rule Format:**
```
# /etc/udev/rules.d/99-custom.rules
KERNEL=="sd*", ATTRS{vendor}=="Samsung", SYMLINK+="samsung_disk"
SUBSYSTEM=="net", ACTION=="add", DRIVERS=="?*", ATTR{address}=="00:11:22:33:44:55", NAME="eth-external"
```

### Common udev Commands:

```bash
# Reload udev rules
udevadm control --reload-rules

# Trigger events
udevadm trigger

# Monitor udev events in real-time
udevadm monitor

# Query device information
udevadm info /dev/sda

# Test rule matching
udevadm test /sys/class/net/eth0
```

### udev Workflow:

1. **Hardware event** occurs (device plugged in)
2. **Kernel** generates uevent
3. **systemd-udevd** receives uevent
4. **Rules** are processed in order
5. **Device node** is created in `/dev/`
6. **Permissions** and ownership set
7. **Programs** executed if specified in rules

### Persistent Device Naming:

udev creates persistent names in `/dev/disk/`:

```bash
/dev/disk/by-uuid/       # Filesystem UUID
/dev/disk/by-label/      # Filesystem label
/dev/disk/by-id/         # Hardware ID
/dev/disk/by-path/       # Physical path
/dev/disk/by-partlabel/  # Partition label
```

**Benefits:**
- Device names remain consistent across reboots
- Independent of device detection order
- Reliable for `/etc/fstab` entries

---

## Additional Topics and Best Practices

### System Performance Monitoring

```bash
# CPU usage
top
htop
mpstat

# Memory usage
free -h
vmstat
cat /proc/meminfo

# Disk I/O
iostat
iotop

# Network
iftop
nethogs
ss -tuln

# Overall system monitoring
dstat
glances
```

### Kernel Parameters (sysctl)

```bash
# View all parameters
sysctl -a

# View specific parameter
sysctl net.ipv4.ip_forward

# Set parameter temporarily
sysctl -w net.ipv4.ip_forward=1

# Make permanent
echo "net.ipv4.ip_forward = 1" >> /etc/sysctl.conf
sysctl -p
```

### Important Directories Summary:

| Directory | Purpose |
|-----------|---------|
| `/boot` | Kernel, initramfs, bootloader files |
| `/dev` | Device nodes |
| `/etc` | System configuration |
| `/proc` | Process and kernel information |
| `/sys` | Device and driver information |
| `/lib/modules` | Kernel modules |
| `/run` | Runtime data |
| `/var/log` | System logs |

---

## Conclusion

This comprehensive guide covers the essential aspects of Linux architecture:
- Understanding kernel space vs user space separation
- Managing kernel modules dynamically
- Working with systemd for service and resource management
- Using cgroups for resource control
- Managing hardware through udev
- Utilizing pseudo filesystems for kernel interaction

**Key Takeaways:**
1. Linux architecture is modular and flexible
2. Systemd provides modern service and resource management
3. Kernel modules enable hardware support without recompilation
4. Cgroups allow fine-grained resource control
5. Understanding these fundamentals is crucial for system administration and troubleshooting

---

## References and Further Reading

- **Linux Kernel Documentation**: https://www.kernel.org/doc/
- **systemd Documentation**: https://systemd.io/
- **Red Hat System Administration Guides**
- **The Linux Programming Interface** by Michael Kerrisk
- **Linux Kernel Development** by Robert Love
- **man pages**: Essential reference for all commands

---

**Document Version**: 2.0
**Last Updated**: December 12, 2025
**Author**: Linux System Administration Notes
