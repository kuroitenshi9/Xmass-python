from datetime import datetime

def extract_from_file():
  #tu wyciagamy z pliku do słownika i zwracamy słownika
  dictionary = {
    1564517408: 'ERROR',
    1562514432: 'WARNING',
    1564015907: 'WARNING4',
    1563822588: 'ERROR',
    1563125949: 'ERROR',
    1564225949: 'WARNING',
    1562491290: 'INFO',
    1563184020: 'ERROR',
    1562956120: 'WARNING',
    1564477808: 'WARNING2',
    1564421475: 'ERROR',
    1562764321: 'INFO',
    1562709301: 'ERROR1',
    1563900303: 'ERROR',
    1564125540: 'INFO4',
    1564010897: 'INFO',
    1564279899: 'INFO',
    1564456120: 'INFO',
    1564452850: 'ERROR',
    1564528675: 'WARNING'
  }
  return dictionary

def get_logs(start, end, logs):
    logs_list = []
    for key, value in logs.items():
        if key > start and key < end:
            logs_list.append(value)
    return set(logs_list)

def to_datestamp(date_as_text):
  date_format = datetime.strptime(date_as_text, '%d-%m-%Y')
  datestamp = datetime.timestamp(date_format)
  return datestamp


def main():
  some_logs = extract_from_file()

  # tu powinnien być input użytkownika
  user_start = to_datestamp('01-01-2019')
  user_end = to_datestamp('03-12-2019')
  print(user_start)
  print(user_end)
  print(get_logs(user_start, user_end, some_logs))

if __name__ == '__main__':
  main()