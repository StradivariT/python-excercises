import json
from datetime import datetime

inputFile = open("/Users/fvargas/Documents/Python/Prácticas/Files/input.json", "r")
employees = json.loads(inputFile.read())
inputFile.close()

templateFile = open("/Users/fvargas/Documents/Python/Prácticas/Files/template", "r")
template = templateFile.read()
templateFile.close()

i = 0
for employee in employees:
    output = open("/Users/fvargas/Documents/Python/Prácticas/Files/output/" + employee["name"] + "_%d" % i, "w")

    birthday = datetime.strptime(employee["birthday"], "%d/%m/%Y")
    employee["age"] = "%d" % ((datetime.today() - birthday).days / 365)

    output.write(template.format(**employee))
    output.close()

    i = i + 1