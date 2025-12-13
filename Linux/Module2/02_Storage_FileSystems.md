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

## Managing Partitions

- 

