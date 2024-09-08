import datetime
name = input("Enter your name: ")

latter = '''
            Dear <|Name|>, 
            Your selected !
            <|Date|>'''


print(latter.replace('<|Name|>',name).replace('<|Date|>', '8 july 2024'))


