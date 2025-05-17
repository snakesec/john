#
#
# Find all executables (except scripts): find . -type f -executable -exec basename {} \; | grep -v "\.py" | grep -v "\.pl" | grep -v "\.rb" | grep -v "\.lua"
#
# Find all symlink: find . -type l -executable -exec basename {} \;
#
#
import os
save_dir = "andraxbin"
progpath = "/opt/ANDRAX/john"

extra_bins = [ "bitlocker2john",
"SIPdump",
"uaf2john",
"benchmark-unify",
"eapmd5tojohn",
"makechr",
"mkvcalcproba",
"dmg2john",
"hccap2john",
"tgtsnarf",
"raw2dyna",
"calc_stat",
"wpapcap2john",
"mailer",
"keepass2john",
"john",
"racf2john",
"relbench",
"putty2john",
"vncpcap2john",
"cprepair",
"genmkvpwd",
"unique",
"gpg2john",
"undrop",
"zip2john",
"unafs",
"rar2john",
"base64conv",
"unshadow" ]

str_pl_file = """#!/bin/bash

perl {progdir}/{progname} "$@"
"""

str_rb_file = """#!/bin/bash

ruby {progdir}/{progname} "$@"
"""

str_py_file = """#!/bin/bash

source /opt/ANDRAX/john/venv/bin/activate

/opt/ANDRAX/john/venv/bin/python3 {progdir}/{progname} "$@"

"""

str_extra_file = """#!/bin/bash

{progdir}/{progname} "$@"
"""

#os.system("rm -rf "+save_dir)
os.system("mkdir "+save_dir)

if os.path.exists("run"):

    exfiles = os.listdir("run")
    
    for exfile in exfiles:

        if exfile.endswith('.py'):
            with open(save_dir+"/"+exfile, 'w') as out:
                content = str_py_file.format(progdir = progpath, progname = exfile)
                out.write(content)

        elif exfile.endswith('.pl'):
            with open(save_dir+"/"+exfile, 'w') as out:
                content = str_pl_file.format(progdir = progpath, progname = exfile)
                out.write(content)

        elif exfile.endswith('.rb'):
            with open(save_dir+"/"+exfile, 'w') as out:
                content = str_rb_file.format(progdir = progpath, progname = exfile)
                out.write(content)

else:
    print("run dir not found")

for x in extra_bins:
  with open(save_dir+"/"+x, 'w') as out:
      content = str_extra_file.format(progdir = progpath, progname = x)
      out.write(content)
