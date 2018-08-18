import re
sourcesessionis = open("nfc/1.txt").read()
temp = sourcesessionis.encode('utf-8').decode('utf-8')
reg = r'UID=(.{5})'#只取SessionId=字符后面32位字符串
wordreg = re.compile(reg)
wordreglist = re.findall(wordreg,temp)
for word in wordreglist:
	print('word加班')
