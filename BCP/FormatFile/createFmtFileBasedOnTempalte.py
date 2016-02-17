import sys, os, re

if (len(sys.argv) != 4):
    print "Syntax : python {} {} {} {}".format (sys.argv[0], "ApiEntry", "encoding", "templateFile")
    print "    eg : python {} {} {} {}".format (sys.argv[0], "invoice-headers", "UTF-16le", "template-unicode-le.fmt")
    exit()

ApiEntry = sys.argv[1]
encoding = sys.argv[2]
templateFile = sys.argv[3]

fmtfile="{}-{}.fmt".format (ApiEntry,encoding)

if not (os.path.exists(templateFile)):
    print ("Invalid Template File: {}".format (templateFile))
    exit(1)

if (os.path.exists(fmtfile)):
    print ("Format File Already Exists: {}".format (fmtfile))
    exit(1)

templateTextToReplace = "___ARRAYNAME_REPLACE___"

replacement = "\\0".join(ApiEntry) + "\\0"

templateText = open(templateFile).read()
targetText = templateText.replace(templateTextToReplace, replacement)
with open(fmtfile, "w") as targetFmt_file:
    targetFmt_file.write(targetText)

print ("Format file created: {}".format(fmtfile))
