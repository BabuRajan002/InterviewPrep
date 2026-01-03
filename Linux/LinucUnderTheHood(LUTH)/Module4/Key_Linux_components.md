# Key Linux Components

## Running applications in Linux:

## Running application in a chroot jail:

- chroot jail is one of the solutions to restrict the application on their own resources.
- Idea behind is, to present access to the application to its one directory and keep all the relevant files to it. 

## From chroot to namespaces:

- Idea to restrict the application to the specific `chroot jail` worked really well. 
- this concept further developed into namespaces, which provide strict isolation for specific areas:
  - cgroup: system resources
  - IPC: Inter process communication
  - network: networking
  - mount: directory access
  - pid: running processes
  - users: the only namespace that can be created without CAP_SYS_ADMIN

## Understanding unshare namespace:

- The Linux Unshare command is used to run a processes in new namespaces
- the unshare command will isolate the new environment from the current namespace
- `nsenter` command allows you run commands from host OS in a namespace, and is particularly useful for analyzing the containers.

## Running restricted systemd applications

- `unshare` command can be used to start a applications in specific namespaces
- Applications can be added to cgroups manually as well. 
  - Cgroups are mounted on Pseudo mount, and you can echo the PID value into the cgroups.proc file.

## Unserstanding the systemd-nspawn

- Docker and Podman are common ways to implement the containers, but you can also easily implement them on Linux using `systemd-nspawn`

# Code behind the Linux:

- Linux is written in C
- Source code of all Linux components is accessible and readable file

