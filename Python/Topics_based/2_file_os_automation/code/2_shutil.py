import shutil

# Copy file
shutil.copy("test.txt", "backup.txt")

# Copy directory recursively
shutil.copytree("source_dir", "dest_dir", dirs_exist_ok=True)

# Move/rename
shutil.move("backup.txt", "archive/test.txt")

# Remove directory tree
shutil.rmtree("dest_dir")

# Make compressed archive (zip/tar)
shutil.make_archive("mybackup", "zip", "source_dir")
