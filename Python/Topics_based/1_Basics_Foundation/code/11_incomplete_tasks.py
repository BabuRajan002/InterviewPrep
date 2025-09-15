from pathlib import Path
import json

def incomplete_tasks(path: str) -> list[str]:
    file_path = Path(path)

    if not file_path.exists():
        raise FileNotFoundError(file_path)
    
    with file_path.open('r', encoding='utf-8') as f:
        ic_tasks = json.load(f)
        tasks = []
        for ic_task in ic_tasks:
            if ic_task.get("status", "<Unkown>") != "done":
            # if ic_task['status'] != "done":
                tasks.append(ic_task['title'])        
        return tasks
                
if __name__ == "__main__":
    status = incomplete_tasks("/Users/babus/Desktop/repos/InterviewPrep/Python/Topics_based/1_Basics_Foundation/sample_files/incomplete_tasks.json")
    if status:
        for state in status:
            print(state)
    else:
        print("Status are good")

# # ChatGPT Version

# from pathlib import Path
# import json
# from typing import List

# def incomplete_tasks(path: str) -> List[str]:
#     """Return titles of tasks whose status is not 'done'."""
#     file_path = Path(path)
#     if not file_path.exists():
#         raise FileNotFoundError(file_path)

#     try:
#         with file_path.open("r", encoding="utf-8") as f:
#             tasks_data = json.load(f)
#     except json.JSONDecodeError as e:
#         raise ValueError(f"Invalid JSON in {path}") from e

#     return [task["title"] for task in tasks_data if task.get("status") != "done"]

# if __name__ == "__main__":
#     titles = incomplete_tasks("tasks.json")
#     if titles:
#         print("\n".join(titles))
#     else:
#         print("All tasks are done 🎉")
