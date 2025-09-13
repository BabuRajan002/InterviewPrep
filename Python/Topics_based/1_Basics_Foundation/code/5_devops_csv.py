from pathlib import Path

def devops_emails(path: str) -> list[str]:
    file_path = Path(path)

    if not file_path.exists():
        raise FileNotFoundError(file_path)

    with file_path.open('r', encoding='utf-8') as emails:
      email_lst = set()
      for line in emails:
         line = line.strip()
         lst = [field.strip() for field in line.split(',')]
         if lst[2] == "devops":
            email_lst.add(lst[1])
       
      return sorted(email_lst)

if __name__ == "__main__":
   emails_devops = devops_emails("/Users/babus/Desktop/repos/InterviewPrep/Python/Topics_based/1_Basics_Foundation/sample_files/users.csv")
   print(",".join(emails_devops))

# #Chat GPT Version:
# from pathlib import Path
# from typing import List

# def devops_emails(path: str) -> List[str]:
#     """Return sorted unique emails of users with role 'devops'."""
#     file_path = Path(path)
#     if not file_path.exists():
#         raise FileNotFoundError(file_path)

#     emails = set()
#     with file_path.open("r", encoding="utf-8") as f:
#         next(f)  # skip header
#         for line in f:
#             fields = [field.strip() for field in line.split(",")]
#             if len(fields) != 3:
#                 continue
#             name, email, role = fields
#             if role == "devops":
#                 emails.add(email)

#     return sorted(emails)

# if __name__ == "__main__":
#     print(",".join(devops_emails("users.csv")))


      