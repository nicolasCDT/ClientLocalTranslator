toTranslate = {}
translationBase = {}

toTranslateFile = "toTranslate.txt"
translationBaseFile = "translateBase.txt"
resultFile = open("result.txt", "w")
otherFile = open("other.txt", "w")

with open(toTranslateFile, "r") as toTranslateFile:
	for lines in toTranslateFile:
		toTranslateLine = lines.split("	")
		toTranslate[toTranslateLine[0]] = toTranslateLine[1]

with open(translationBaseFile, "r") as translationBaseFile:
	for lines in translationBaseFile:
		translationBaseLine = lines.split("	")
		translationBase[translationBaseLine[0]] = translationBaseLine[1]

for key, value in toTranslate.items():
	if key in translationBase:
		resultFile.write(key + "	" + translationBase[key])
	else:
		otherFile.write(key + "	" + toTranslate[key])