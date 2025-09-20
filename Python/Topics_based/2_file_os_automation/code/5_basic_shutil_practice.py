import os
import shutil
from pathlib import Path


def create_backup(src: str, dest: str):
    src_path = Path(src)
    dest_path = Path(dest)
    
    if not src_path.exists():
        raise FileNotFoundError(src_path)
    
    if dest_path.is_relative_to(src_path):
        raise ValueError(f"Destination path must not be in source: {dest_path} {src_path}")
    
    copied = []
    for root, _, files in os.walk(src_path):
        root_path = Path(root)

        if root_path.is_relative_to(dest_path) or dest_path.is_relative_to(root_path):
            continue
        for f in files:
            src_file = root_path / f
            if src_file.suffix.lower() == ".txt":
                out = dest_path / src_file.name
                shutil.copy2(src_file, out)
                copied.append(out)
        
    archived_path = Path(shutil.make_archive(str(dest_path), "zip", str(dest_path)))
    return copied, archived_path


if __name__ == "__main__":
    copied, archive = create_backup("/Users/babus/Desktop/repos/InterviewPrep/Python/Topics_based/2_file_os_automation/code/source_dir", "/Users/babus/Desktop/repos/InterviewPrep/Python/Topics_based/2_file_os_automation/code/backup")

    print("copied files:")
    for p in copied:
      print("-", p)

    print("archived_path", archive)    


# #ChatGPT Version
# from pathlib import Path
# import shutil
# from typing import List, Tuple

# def create_backup(src: str | Path, dest: str | Path) -> Tuple[list[Path], Path]:
#     """
#     Copy *.txt files from src to dest (non-structure-preserving) and zip dest.
#     Returns (copied_files, archive_path).
#     """
#     src_path = Path(src).resolve()
#     dest_path = Path(dest).resolve()

#     if not src_path.exists():
#         raise FileNotFoundError(src_path)

#     # Prevent copying backup into itself if dest is inside src
#     if dest_path.is_relative_to(src_path):
#         raise ValueError(f"dest must not be inside src: {dest_path} ⊂ {src_path}")

#     dest_path.mkdir(parents=True, exist_ok=True)

#     copied: List[Path] = []
#     for root, _, files in os.walk(src_path):
#         root_path = Path(root)
#         # Skip dest subtree just in case
#         if dest_path.is_relative_to(root_path) or root_path.is_relative_to(dest_path):
#             continue

#         for name in files:
#             src_file = root_path / name
#             if src_file.suffix.lower() == ".txt":
#                 # flat copy into dest; use copy2 to preserve metadata
#                 out = dest_path / src_file.name
#                 shutil.copy2(src_file, out)
#                 copied.append(out)

#     # Create archive next to dest (backup.zip). base_name should NOT include extension.
#     archive_base = dest_path  # creates <dest>.zip
#     archive_path = Path(shutil.make_archive(str(archive_base), "zip", str(dest_path)))

#     return copied, archive_path

# if __name__ == "__main__":
#     import os
#     copied, archive = create_backup(
#         "/path/to/source_dir",
#         "/path/to/backup"
#     )
#     print("Copied files:")
#     for p in copied:
#         print(" -", p)
#     print("Archive:", archive)

    