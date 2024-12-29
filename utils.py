import os 
from dotenv import load_dotenv, find_dotenv

def load_env():
    _ = load_dotenv(find_dotenv())



def get_groq_api_key():
    load_env()
    groq_api_key = os.getenv("GROQ_API_KEY")
    return groq_api_key

def get_hf_token():
    load_env()
    hf_token = os.getenv('HF_API_TOKEN')
    return hf_token


# break line every 80 characters if line is longer than 80 characters
# don't break in the middle of a word
def pretty_print_result(result):
  parsed_result = []
  for line in result.split('\n'):
      if len(line) > 80:
          words = line.split(' ')
          new_line = ''
          for word in words:
              if len(new_line) + len(word) + 1 > 80:
                  parsed_result.append(new_line)
                  new_line = word
              else:
                  if new_line == '':
                      new_line = word
                  else:
                      new_line += ' ' + word
          parsed_result.append(new_line)
      else:
          parsed_result.append(line)
  return "\n".join(parsed_result)
