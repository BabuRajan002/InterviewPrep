# Chapter 18. Directory and links

You are absolutely right. To keep your preparation on track and avoid "looping" in theory, we are skipping Chapter 15-17 and jumping straight to the most high-value SRE domain: **Chapter 18 (Directories and Links)**.

In an SRE interview, Chapter 18 is not about "creating folders"; it is about **how the Kernel resolves a path** and the **atomic nature of filesystem operations**.

### 14.4 (VFS Recap) to 18.1: The Directory Structure

As we discussed, a directory is just a special file where the "data" is a list of (Name, Inode Number) pairs.

#### Key Concept: Path Resolution (The "Walking" process)

When you access `/var/log/syslog`, the Kernel doesn't find it in one go. It performs a **Path Walk**:

1. Finds the Inode for `/` (always Inode #2).
2. Reads the data of Inode #2 to find the entry for `var`.
3. Finds the Inode for `var`, reads it to find `log`.
4. Finds the Inode for `log`, reads it to find `syslog`.
5. **SRE Performance Tip:** Every "step" in this walk is a disk I/O. This is why the **Dentry Cache (Directory Entry Cache)** in RAM is critical. If your dentry cache is small, your server will spend all its CPU "walking" directories.

---

### 18.2 Atomic Renaming (The "Zero-Downtime" Secret)

The `rename()` system call is one of the most important tools for an SRE.

* **The Rule:** If you rename a file within the *same* filesystem, the operation is **atomic**.
* **The Benefit:** If a process is reading `config.yaml` while you are renaming `new_config.yaml` to `config.yaml`, the process will either see the old file or the new file—**never a half-written or corrupted file.**

---

### 💼 Google SRE Interview Scenarios for Chapter 18

#### Scenario 1: The "Atomic Deploy"

**Interviewer:** *"You are deploying a new version of a static website with 10,000 files. If you copy them one by one into the webroot, users might see a mix of old and new files. How do you ensure an instantaneous switch?"*
**SRE Answer:**

1. "I would use **Symlink Switching**."
2. "Place the new version in `/deploy/v2/` and the old in `/deploy/v1/`."
3. "The webserver points to a symlink `/var/www/current` -> `/deploy/v1`."
4. "To switch, I use `ln -sfn /deploy/v2 /var/www/current`. This updates the symlink atomically. All new requests immediately go to v2."

#### Scenario 2: The "Move vs. Copy" Performance

**Interviewer:** *"Why is `mv` instantaneous when moving a 100GB file between folders on the same disk, but slow when moving it to an external USB drive?"*
**SRE Answer:**

1. "On the same filesystem, `mv` only changes the **Directory Entry**. The Inode and the 100GB of Data Blocks never move. It's just a metadata update."
2. "Across filesystems, the Kernel must physically copy every data block to the new device, create a new Inode, and then delete the old one. This is a heavy I/O operation."

---

### 🛠️ SRE Commands for Chapter 18

### Final Summary of Chapter 18:

1. **Directories are files** that map names to Inodes.
2. **Path Resolution** is expensive; the Dentry Cache makes it fast.
3. **Renaming** is the standard way to perform atomic updates in Linux.
4. **Symlinks** are the primary tool for versioning and zero-downtime deploys.

**We have now finished Milestone 3 (I/O & Filesystems)!**

**Next Milestone: Pillar 4 - Memory / OOM (Chapters 7, 49, 50).**
This is where we talk about why your processes get "OOMKilled" and how to tune the kernel to stop it. Ready to move?

This is the exact "Aha!" moment that separates a user from a Systems Engineer.

When you run `cat soft_link.txt`, you see the content of the original file because the **Kernel** is doing a hidden "jump" for you.

### 1. The "Path String" in the Data Block

Every file on Linux has at least one Data Block allocated to it.

* For a **Regular File**, that block contains your data (e.g., "Hello World").
* For a **Soft Link**, that block contains the **literal characters of the path** you typed when you created the link.

**Example Visualization:**
If you run `ln -s /etc/passwd my_link`:

1. Linux creates a new Inode (e.g., #999).
2. Linux allocates one Data Block for Inode #999.
3. Inside that Data Block, Linux writes exactly 11 bytes: `/etc/passwd`.

### 2. How `cat` works (The Kernel Jump)

When you run `cat my_link`:

1. The Kernel looks at the Inode for `my_link`.
2. It sees the **File Type** is "Symbolic Link" (not a regular file).
3. The Kernel says: *"Wait, I shouldn't show the user the data in this block. I should read the string inside this block and go find THAT file instead."*
4. The Kernel reads the string `/etc/passwd`.
5. The Kernel then performs a **new lookup** for `/etc/passwd`.
6. It finds the Inode for `/etc/passwd` and returns **its** data blocks to `cat`.

**This is why a Soft Link is slower than a Hard Link.** The Kernel has to do twice the work (Read link string  Restart lookup  Find target Inode  Read target blocks).

### 3. Proof: Seeing the "Path String" Size

You can actually see the size of this "string" using `ls -l`.

```bash
# Create a soft link to a long path
ln -s /usr/share/common-licenses/GPL-3 gpl_link

# Now look at the size column
ls -l gpl_link

```

**Observation:** You will see the size is exactly **31 bytes**. Why 31? Because `/usr/share/common-licenses/GPL-3` is exactly 31 characters long.

If it were a **Hard Link**, the size would be the size of the actual license file (thousands of bytes). But for the **Soft Link**, the "file size" is just the length of the destination's address.

---

### 💼 SRE Interview Deep Dive: "Fast Symlinks"

**Interviewer:** *"If a Symlink just stores a path string, and that string is very short (like 'a.txt'), does the Kernel still waste a whole 4KB Data Block just to store those 5 characters?"*

**Your "Google Level" Answer:**
"Actually, modern filesystems (Ext4, XFS) use **Fast Symlinks**. If the path string is shorter than 60 characters, the Kernel doesn't allocate a Data Block at all. It stores the path string **directly inside the Inode structure** itself (where the block pointers usually go). This saves disk space and one extra disk I/O, making the jump even faster."

---

### Ready for Pillar 4: Memory?

We are moving from **Disk** (Inodes/Blocks) to **RAM** (Pages/Virtual Memory). This is where we answer:

1. **RSS vs VSZ:** Which one tells you how much RAM your app is *actually* using?
2. **The Page Cache:** Why is `free -m` always showing "0 MB free" on a healthy server?
3. **The OOM Killer:** How does the Kernel decide which process to kill when RAM runs out?

**Let's start Pillar 4!**

This is a fantastic "SRE Drill." If `lsof` didn't find any deleted-but-open files, you are likely facing the **"Hidden Mount"** or **"Over-mounting"** problem.

### The Scenario: The "Hidden" 80GB

You have a folder `/data/logs`. You were writing logs there, and it grew to 80GB. Then, a junior admin (or an automated script) mounted a **new** disk partition directly on top of `/data/logs`.

Now, when you run `du`, it only sees the content of the **new** (empty) disk. But the **old** 80GB of data is still sitting in the Inode table of the parent partition, "hidden" underneath the new mount.

---

### Step-by-Step Production Investigation

#### Step 1: Confirm the Discrepancy

You see 99% used, but `du` doesn't "see" where it went.

```bash
df -h /data
# Shows 99GB Used

du -sh /data
# Shows 20GB Used (Where is the other 79GB?!)

```

#### Step 2: Look for Over-mounts

Check the mount table to see if something is mounted inside `/data`.

```bash
findmnt | grep /data
# Example Output:
# /data           /dev/sda1  ext4
# └─/data/logs    /dev/sdb1  xfs   <-- Potential Culprit!

```

If `/data/logs` is a separate mount, any data that existed in the `/data/logs` folder **before** `/dev/sdb1` was mounted is now hidden.

#### Step 3: Use a "Bind Mount" to see "Underneath" (The SRE Secret)

You can't just unmount `/data/logs` because production is using it. Instead, you create a "Bind Mount" of the **parent** partition to a temporary location. A bind mount lets you see the raw content of the partition without the "sub-mounts" obscuring it.

```bash
# 1. Create a temp directory
mkdir /tmp/inspect_data

# 2. Bind mount the ROOT of /data to the temp dir
# This bypasses any sub-mounts like /data/logs
mount --bind /data /tmp/inspect_data

# 3. Check the space in the temp dir
du -sh /tmp/inspect_data/logs
# BINGO! du now sees the 79GB of hidden files because 
# the sub-mount (sdb1) isn't active on this bind path.

```

#### Step 4: The Fix

Now that you've found the hidden files, you can safely delete them from the **temporary bind path** to reclaim space on the main disk.

```bash
rm -rf /tmp/inspect_data/logs/*
umount /tmp/inspect_data

```

Now, `df -h /data` will immediately show 80GB of free space.

---

### 📝 Final Lesson for Q1:

**Interview Answer:** "The discrepancy is likely caused by **over-mounting**. Data was written to a directory before another filesystem was mounted on top of it. To find it, I would use a **bind mount** to bypass the VFS mount-tree and inspect the underlying Inodes directly."

---

### Ready for the answers to Q2 (Atomic Renames) and Q3 (Path Resolution)?

(Hint for Q3: Remember that to access a file, you need `+x` permissions on **every single parent directory** in the path!)

This is a fantastic lab to perform because it feels like "magic" when the files disappear but the disk remains full. We will simulate exactly what happens when a junior admin accidentally "over-mounts" a directory.

### Lab: The "Hidden Data" Mystery

In this lab, we will create a "Large" file, mount a new filesystem on top of it, and then use the **SRE Bind Mount** technique to find and delete the hidden data.

#### Step 1: Prepare the "Host" Filesystem

We will use a loop device to create a fake 200MB "Main Disk."

```bash
# 1. Create a 200MB file to act as our main disk
dd if=/dev/zero of=main_disk.img bs=1M count=200
mkfs.ext4 main_disk.img

# 2. Mount it
mkdir -p /mnt/main_storage
mount -o loop main_disk.img /mnt/main_storage

```

#### Step 2: Create the "Hidden" Data

We will create a 100MB file inside a folder called `logs`.

```bash
mkdir /mnt/main_storage/logs

# Create a 100MB file (the "Hidden" culprit)
dd if=/dev/urandom of=/mnt/main_storage/logs/hidden_beast.log bs=1M count=100

# Verify disk usage
df -h /mnt/main_storage
# Output: Should show ~100MB (50%) used.

```

#### Step 3: Perform the "Over-mount"

Now, we will simulate mounting a **new** empty disk on top of that `logs` folder.

```bash
# 1. Create a 20MB "New Disk"
dd if=/dev/zero of=new_disk.img bs=1M count=20
mkfs.ext4 new_disk.img

# 2. Mount it OVER the existing logs folder
mount -o loop new_disk.img /mnt/main_storage/logs

```

#### Step 4: Observe the Mystery

Now, try to find where the 100MB went using standard tools.

```bash
# Check physical disk usage
df -h /mnt/main_storage
# Output: Still shows 100MB+ used! (The Inodes on the main disk are still occupied)

# Check directory usage
du -sh /mnt/main_storage
# Output: Shows ~1MB used! (du is redirected to the NEW empty disk)

# Try to list the file
ls -lh /mnt/main_storage/logs/
# Output: Empty! The 'hidden_beast.log' has vanished.

```

---

### The SRE Fix: Using Bind Mounts

To recover the space without unmounting the production disk, we must "look under" the mount.

#### Step 5: The Bind Mount Investigation

```bash
# 1. Create a temp directory to see the "Raw" main disk
mkdir /tmp/raw_disk

# 2. Bind mount the MAIN storage (not the logs sub-mount)
mount --bind /mnt/main_storage /tmp/raw_disk

# 3. Look into the 'logs' folder via the BIND mount
ls -lh /tmp/raw_disk/logs/
# BINGO! 'hidden_beast.log' is visible here!

```

#### Step 6: Cleanup and Reclaim Space

```bash
# Delete the hidden file through the bind path
rm /tmp/raw_disk/logs/hidden_beast.log

# Verify the main disk space
df -h /mnt/main_storage
# Output: Space is now RECLAIMED (Main disk usage drops).

# Unmount the investigation path
umount /tmp/raw_disk

```

---

### 📝 Lab Summary for your Notes

| Action | Result | Why? |
| --- | --- | --- |
| **Normal Mount** | Shadows the directory. | VFS redirects all requests to the new Inode. |
| **`df -h`** | Shows "Full." | Counts used blocks on the physical partition. |
| **`du -sh`** | Shows "Empty." | Only walks visible files in the current mount tree. |
| **`mount --bind`** | Reveals the truth. | Bypasses sub-mounts to show the underlying Inodes of the source directory. |

In Linux, a **Bind Mount** is like creating a "portal" or a "mirror" of a directory tree.

Normally, when you mount a device (like `/dev/sdb1`), you are connecting **Physical Hardware** to a **Path**.
With a **Bind Mount**, you are connecting a **Path** to another **Path**.

### 1. The Core Concept: Aliasing

A Bind mount allows you to make the contents of one directory available in another place. It doesn't create a copy of the data; it creates a **second entry point** in the VFS to the same underlying Inodes.

```bash
mount --bind /source/dir /target/dir

```

After this command, any file you create in `/source/dir` appears instantly in `/target/dir`. They are the exact same files, same Inodes, same data blocks.

---

### 2. Why is it different from a Symlink?

This is a common interview question. While they look similar, they behave very differently at the Kernel level:

| Feature | Symlink (Soft Link) | Bind Mount |
| --- | --- | --- |
| **Kernel Level** | The app sees a "Link" and jumps to the target. | The app thinks it is a **real, local directory**. |
| **Path Resolution** | Path strings can be broken (dangling). | It is a direct VFS hook; it cannot "break." |
| **Chroot/Containers** | Often break if the target is "outside." | Works perfectly; used for Docker/LXC volumes. |
| **Visibility** | `ls -l` shows an `l` type file. | `ls -l` shows a standard directory. |

---

### 3. The "SRE Magic" (Why we used it in the Lab)

The most powerful feature of a Bind Mount is that it **does not follow sub-mounts by default**.

Imagine this structure:

* `/mnt/main` (Partition A)
* `/mnt/main/external` (Partition B is mounted here)

If you perform a regular copy of `/mnt/main`, you get the data from both Partitions A and B.
However, if you do:

```bash
mount --bind /mnt/main /tmp/check

```

The Kernel "mirrors" **only** Partition A. The folder `/tmp/check/external` will appear **empty**.

**This is why it solved our "Hidden Data" problem:**

1. Data was hidden "underneath" a mount point on the main disk.
2. By bind-mounting the main disk to a new spot, we created a view of the disk **without the secondary mount covering the folder.**
3. We could then see the "hidden" Inodes that the secondary mount was shadowing.

---

### 4. Real-World SRE Use Cases

**A. Read-Only Mirrors:**
You have a data folder that an app needs to read, but you don't trust the app.

```bash
mount --bind -o ro /data/shared /app/readonly_view

```

The app can read the files in its folder, but even if it tries to `rm -rf`, the Kernel will block it because the **mount point** is marked Read-Only, even if the disk itself is Read-Write.

**B. Moving "Full" Directories without changing Configs:**
Imagine `/var/lib/mysql` is full. You have a new disk at `/mnt/bigdisk`.

1. Move the data: `cp -a /var/lib/mysql/* /mnt/bigdisk/mysql_data/`
2. Bind mount it back: `mount --bind /mnt/bigdisk/mysql_data /var/lib/mysql`
**Result:** MySQL keeps working with its old config path `/var/lib/mysql`, but the data is physically stored on the new big disk.

---

### Summary for your Notes:

> **Bind Mount:** A VFS-level operation that attaches a directory tree to a new location. It is superior to Symlinks for SRE work because it is transparent to applications, works inside `chroot` environments, and allows for "masking" or "unmasking" underlying filesystem data for troubleshooting.

**Are you 100% comfortable with the "Pillar 3: I/O and Filesystems" now?** If yes, we are moving to **Pillar 4: Memory (Paging, RSS vs VSZ, and the OOM Killer)**. This is a very "heavy" topic, but I will keep it focused on the production scenarios you'll face at Google.