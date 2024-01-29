def count_word_in_file(file_path, target_word):
   try:
       with open(file_path, 'r') as file:
           content = file.read()
           word_count = content.lower().count(target_word.lower())
           return word_count
   except FileNotFoundError:
       return f"File not found: {file_path}"
def word_found(file_path, word):
   try:
       with open(file_path, 'r') as file:
           content = file.read()
           if 'mvn sonar:sonar' in content:
             return 1
           if 'npm run lint' in content:
             return 1
   except FileNotFoundError:
       return f"File not found: {file_path}"
