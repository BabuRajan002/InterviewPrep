from pathlib import Path
import re

def failed_sources(path: str) -> None:
    file_path = Path(path)
    if not file_path.exists():
        raise FileNotFoundError(file_path)
    
    with file_path.open('r', encoding='utf-8', newline='') as fs:
        ipv4_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
        ipv6_pattern = r"""
        \b(?:
            (?:[0-9A-Fa-f]{1,4}:){7}[0-9A-Fa-f]{1,4}                
        | (?:[0-9A-Fa-f]{1,4}:){1,7}:                             
        | (?:[0-9A-Fa-f]{1,4}:){1,6}:[0-9A-Fa-f]{1,4}             
        | (?:[0-9A-Fa-f]{1,4}:){1,5}(?::[0-9A-Fa-f]{1,4}){1,2}    
        | (?:[0-9A-Fa-f]{1,4}:){1,4}(?::[0-9A-Fa-f]{1,4}){1,3}    
        | (?:[0-9A-Fa-f]{1,4}:){1,3}(?::[0-9A-Fa-f]{1,4}){1,4}    
        | (?:[0-9A-Fa-f]{1,4}:){1,2}(?::[0-9A-Fa-f]{1,4}){1,5}    
        | [0-9A-Fa-f]{1,4}:(?:(?::[0-9A-Fa-f]{1,4}){1,6})         
        | :(?:(?::[0-9A-Fa-f]{1,4}){1,7}|:)                       
        )\b
        """
        ipv6_re = re.compile(ipv6_pattern, re.VERBOSE)

        lists_of_lst = []
        final_lst = []
        for line in fs:
            if "Failed password" in line:               
                    lists_of_lst.append(ipv6_re.findall(line.strip()))              
                    lists_of_lst.append(re.findall(ipv4_pattern, line.strip()))
        for lst in lists_of_lst:
             if len(lst) > 0:
                  for element in lst:
                    final_lst.append(element)
    unique_list = list(set(sorted(final_lst)))
    print(f"Count:{len(unique_list)}\nIPs:{unique_list}")
if __name__ == "__main__":
   failed_sources("/Users/babus/Desktop/repos/InterviewPrep/Python/Topics_based/1_Basics_Foundation/sample_files/auth.log")
