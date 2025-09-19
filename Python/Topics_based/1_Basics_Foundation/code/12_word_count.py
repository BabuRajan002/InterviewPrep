from pathlib import Path
from collections import Counter
import string


def word_freq(path: str, top_n: int = 5) -> list[tuple[str, int]]:
    file_path = Path(path)

    if not file_path.exists():
        raise FileNotFoundError(file_path)
    
    words = []
    with file_path.open('r', encoding='utf-8') as f:
        translator = str.maketrans('-', ' ')     
        for line in f:
            line = line.replace("–", " ").replace("—", " ").replace("…", " ").strip()
            clean_line = line.translate(translator)
            clean_line = clean_line.translate(str.maketrans('', '', string.punctuation))
            words.extend(clean_line.lower().split())       

        
        word_count = Counter(words)
        return sorted(word_count.items(), key=lambda x: (-x[1], x[0]))[:top_n]
    # sorted_word_count = sorted(
    #     ((word, count) for word, count in word_count.items()),
    #     key=lambda x: (-x[1], x[0])
    # )   
    
    new_tuple = ()
    for i in range(0, len(sorted_word_count), top_n):        
          new_tuple = new_tuple + (sorted_word_count[i])
    return new_tuple
            
if __name__ == "__main__":
    for word, count in word_freq("/Users/babus/Desktop/repos/InterviewPrep/Python/Topics_based/1_Basics_Foundation/sample_files/word_count.txt", 5):
        print(word, count)
