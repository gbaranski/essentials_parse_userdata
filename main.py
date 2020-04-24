import yaml
import os
userdataDir = r'userdata/'

for filename in os.listdir(userdataDir):
    with open(userdataDir + filename) as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
        try:
            output = data["lastAccountName"] + ":" + data["ipAddress"]
        except Exception as e:
            print(repr(e))

        print(output)
        outputFile = open(r'output/', 'a')
        outputFile.write(output + "\n")
        outputFile.close()
print("Done :)")

