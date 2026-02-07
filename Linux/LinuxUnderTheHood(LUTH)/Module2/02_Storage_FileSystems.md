# Storage and Filesystems

- Linux works with block devices and character devices
- A block device allows Linux kernel to address information on the device in any order. 
- Character device is addressed by sending /receiving directors

## Partitions, MBR and GPT:

### MBR: 
- Master Boot Record
- MBR is first 512 bytes on disk, of which 64 bytes is used as the partition table
- In MBR, 64 bytes are available for addressing 4 partitions, which measn 16 bytes for each partition. 
- Using these 64 bytes, a maximum disk size of 2 TiB can be addresses.
- Another limitation is only 4 partitions can be managed through MBR.
-  to check the partition `xxd -l 1024 /dev/nvme0n1`
- In GUID Partition table more space is available for addressing partitions
- GUID is a part of Unified Extensible Firmware Interface
![MBR](<Screenshot 2025-12-12 at 2.53.27 PM.png>)

## Image and ISO file:

- To mount a file, a loop device is created as a fake block device
- You can perform this procedure manually as well. 

## LVM:

- Easy resizing of volume
- `vgcreate` will create will check the physical volume first and it will add it into the vg.

## LVM Features:

- How to create lv snapshot - `lvcreate -s -n lvdatasnap /dev/vgdata/lvdata -l 5%FREE`
- Volume group configuration - `vgcfgbackup`
- `vgcfgrestore` - to revert to the original data
- `vgcfgbackup -f /tmp/vgbackup-$(data +%d-%m-%y)` - To take the backup of a volume group.
- `vgchange -a -n vgdata` - to check about the active logical volumes
- `vgcfgrestore -f /tmp/vgbackup vgdata` - Which will help to restore the volume group called vgdata

- VG back up has been created automatically created in the CentOS system under `/etc/lvm`

## Device Mapper: 

- What is Device Mapper? 
  - “Device Mapper is a Linux kernel framework that creates virtual block devices by mapping logical blocks to physical storage. LVM uses device-mapper to implement logical volumes, while features like RAID, encryption, snapshots, and multipathing reuse the same mechanism.”

- Several advanced features are required in the Linux Operating system: 
  - Cache
  - Encryption
  - raid 
  - snapshot
  - thin provisioning
  - mirrorring
- These features are provided by Device Mapper
- Device Mapper maps physical block devices to virtual block devices, which are used by upper-layer systems such as LVM.

![deviceMapper](<Screenshot 2025-12-14 at 9.43.34 PM.png>)
- Device mapper is used to access the block devices using logical addressing.
- In order to access these block devices, device mapper is creating virutal devices `/dev/dm-*`
- For an example `ls -l /dev/mapper/vgdata-lvdata /dev/vgdata/lvdata` Both of them mapped to `/dev/dn-*`
- `dmsetup ls` - Lists from the device mapper setup
-  `demsetup info` - gives more info about the all of the devices that are available

## Manually creating device mapper storage:

- `dmsetup create` - Used to create devices without using an upper-layer device manager.
- `dmsetup create <devicename> --table '0 <block count> linear <source-device> <start-block>'`

## LVM and VDO
- Virtual Data Optimizer provides thin provisioning on top of LVM lofical volumes by using data dedeuplication and compression.
- VDO options will work only with LVM in RHEL 8. 
- LVM also provides thin provisioning but VDO provides more efficient algorithms.
- By VDO in the top of LVM, it easy to increase the size of the underlying volumes while running out of physical storage.
- While creating VDO logical volumes, a minimal physical size of 5GB is required. - Due to heavy metedata storage.

![vdo](<Screenshot 2025-12-14 at 10.28.33 PM.png>)

## What is thin provisioning? 

Virtual Allocation: Admins create large virtual disks (LUNs/volumes) for applications, making them appear much bigger than the initial physical space.
Dynamic Allocation: When an application starts writing data, the storage system dynamically pulls blocks from the physical storage pool to fulfill the request.
Space Efficiency: Physical space is only consumed by actual data, leaving unused allocated space as pointers until written.

## What is stratis? 

- Stratis volumes always use the XFS filesystem
- Stratis volumes are thin provisioned in nature
- Volume storage is allocated from the stratis pool

## Linux Unified Key Setup (LUKS):
- It encrypts the complete device, resulting in a new device mapper device
- This device mapper device needs to be opened, after which a filesystem can be created on that device
- Below are the commands to setup the encrypted device
  ```336  cryptsetup luksOpen /dev/nvme0n1p4 secret
  337  ls /dev/mapper/
  338  ls -l /dev/mapper/
  339  mkfs.ext4 /dev/mapper/secret
  340  mount /dev/mapper/secret /mnt/
  341  cryptsetup luksClose /dev/mapper/secret 
  342  umount /mnt 
  343  cryptsetup luksClose /dev/mapper/secret 
  344  history``` 

## Real World Scenario: Creating a Hidden Storage device: 

![steps](<Screenshot 2025-12-15 at 10.40.16 PM.png>)

## VFS Virtual File systems:

- Its is generic interface that is used by serveral specific filesystems to connect to the kernel
- It provides the common system calls that are needed in all filesystems.
- VFS is a interface that is going to be used by the Kernel
- Application running in the User space will try do a syscalls to the VFS ---> ext4, xfs, vfat drivers to communicate with the kernel.
![alt text](<Screenshot 2025-12-17 at 6.03.07 PM.png>)

## POSIX: Portable Operating System Interface (Standardized System Calls)
- The mission was to describe how system calls should behave.
- Key Features:
  - It should implement strong consistency
  - It should implement the operations like random reads, writes, fsync, truncate operations
  - File access is controlled by permissions, which are based on the file ownership and permissions mode

- This POSIX filesystem always gives a standardization to applications that the system calls should be in specific way.

![Posix](<Screenshot 2025-12-17 at 6.11.09 PM.png>)

## POSIX filesystems implement common features: 
  - inodes contain the file admin
  - Special files like device nodes and named pipes can be used
  - Directories are used for file admin
  - Hard links and soft links can be used
  - File system metadata can be stored in superblock

- Superblock - Contains filessytem metadata
- Directory Table - contains filesystem names, which points to filesystem inodes.
- inode - Each file has a inode, which contains a list of blocks or extents that are used to store the file data.
- block - original allocation of the file in the disk

## inode and block allocation

- When a filesystem is created, inode table will be created as well.
- In xfs filesystem the inode table is flexible 
- In ext4 filesystem the inode table is preallocated. You can run out of inodes.
- inode keeps all administration of the file but not the filename

## Sparse files

- Sparse files offer a solution to use disk space in an efficient way when the file is partially empty
- When creating a files, filesystems that support the fallocate() system call allocate blocks without actually writing anything in these blocks.

## FUSE Filesystems:
- FUSE filesystem is User space
- It is useful as it allows for mounting filesystems in user space
- Allows non-privileged users to mount
- Fuse is not goof performance of our system

## Using EST filesystem Debugger:

- EXT4 is powerful tool. EXT filesystem debugger. 
- debugfs (aks debug2fs) - Can be used to perform advances operations on Ext filesystems
- Think of printing the filesystem administrative data in the superblock, dumping inodes, listing blocks used by specific files and more.
- ***Important*** - debugfs utility is under the hood tool. We have to use it in a careful way. It may corrupt the entire filesystem.

## Recovery of deleting file in ext4 using debugfs utility.
- in ext3 filesystems, the lsdel command could be used to list recently deleted inodes.
![recoverthedeletedfile](<Screenshot 2025-12-18 at 11.56.11 AM.png>)

# Cloud and Datacenter Storage:

## SSD:

- No matter how advanced, all SSD devices wear out if written to too often.
- On recent SSD devices it will take many years before you see problems related to this. 
  - Limit swap usage 
  - Dont fill SSD device to it's maximum
  - Enable fstrim.service to inform the operating system which blocks on the device is no longer in use.
  - user the `noatime` mount option.

## Understanding iscsi:

- ![iscsi](iscsi.png)

## How to setup the iscsi? 

- iScsi Components:
  - `target` on the SAN gives access to the storage backends:
     - Disks
     - Partitions
     - Logical Volumes
     - Files
  - Service Connect to these using iscsi initiator:
    - After the sucessful connection the connected servers can see newly added storage devices. 
      - Check in `/proc` partitions
      - Or using lscsi command
      ![iscsi terminology](iscsi_terminalogy.png)

## Object storage
- Here file is written as binary objects.
- Binary objects are stored in a replicated way.
- Ceph is the leading storage for the object storage in the open source world.

![object storage](object_storage.png)