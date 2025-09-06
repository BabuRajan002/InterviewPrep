from pathlib import Path
from collections import Counter

def parsing_nginx(path: str) -> None:
    file_path = Path(path)

    if not file_path.exists():
        print(f"file is not available {file_path}")

    with open(file_path, 'r') as nginx_log:
      count_200 = 0
      count_400 = 0
      count_500 = 0
      endpoints = []
      for line in nginx_log:
         lst = line.split()
         endpoints.append(lst[6])         
         if lst[8] >= '200' and lst[8] <= '299':
            count_200 += 1
         elif lst[8] >= '400' and lst[8] <= '499':
            count_400 += 1
         else:
            count_500 += 1
      endpoints_counts = Counter(endpoints)
      top_three_endpoints = endpoints_counts.most_common(3) #Return list of tuples containing the n most common elements and their counts
      
         
         
         
    print(f"The most commonly accessed endpoint are :{top_three_endpoints}")
    print(f"Number of 200 responses :{count_200}")
    print(f"Number of 400 responses :{count_400}")
    print(f"Number of 500 responses :{count_500}")   


if __name__ == "__main__":
  parsing_nginx("/Users/babus/Desktop/repos/InterviewPrep/Python/1_FileHandling/sample_files/nginx_sample.log")