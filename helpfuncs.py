def RepeatAskInt(message, min = 0, max = 0, noneValid = False) :
    while True:
        try:
            inputValue = StringNoneCheck(input(message))
            if noneValid and inputValue == None:
                return None
            
            inputValue = int(inputValue)
            if min == max or (inputValue <= max and inputValue >= min):
                return inputValue
            else:
                print('Please enter an integer in the range ', min, '-', max)
            
        except ValueError:    
            print('Please enter an integer')
        except TypeError:
            print('You must enter a value')

def RepeatAskFloat(message, min = 0.0, max = 0.0, noneValid = False) :
    while True:
        try:
            inputValue = StringNoneCheck(input(message))
            if noneValid and inputValue == None:
                return None

            inputValue = float(inputValue)
            if min == max or (inputValue <= max and inputValue >= min):
                return inputValue
            else:
                print('Please enter a float in the range ', min, '-', max)
            
        except ValueError:    
            print('Please enter a float')
        except TypeError:
            print('You must enter a value')
                
def StringNoneCheck(value):
    try:
        if value == None:
            return None
        stringValue = str(value)
        if stringValue == '' or stringValue == ' ' or stringValue == 'null' or stringValue == 'Null'or stringValue == 'none' or stringValue == 'None':
            return None
    except:
        return None
    return stringValue


def MultiRowTextInput():
    print("End your writing by entering 'q':")
    text = ''
    while True:
        temp = input('')
        if temp == 'q':
            return text
        text += temp + '\n'
