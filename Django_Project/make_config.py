# Super simple script to make the .env file 
if __name__ == '__main__':
   #Windows version
   #file = open('.\\Django_Project\\.env', mode='x', encoding='UTF-8')
   #Ubuntu Version
    file = open('.env', mode = 'x', encoding='UTF-8')
    file.close()

