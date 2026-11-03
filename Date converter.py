import re
def file(filepath):
    with open(filepath) as file:
        return file.read()

def pattern(text):
    date= r'\b(\d{2})-(\d{2})-(\d{4})\b'
    coverted=re.sub(date,r'\3-\2-\1',text)
    return coverted

def main():
    text=file('sample 5.txt')
    dates=pattern(text)

    print('Converted Dates:')       
    print(f'{dates}')

main()



