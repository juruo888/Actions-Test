# 请按照将 PATH 环境变量的前四项配置如下！！！否则将无法正确编译！！！
# 1. Python 64 位 Scripts 目录
# 2. Python 64 位根目录
# 3. Python 32 位 Scripts 目录
# 4. Python 32 位根目录
# 另外提醒，PATH 末尾需要有反斜杠！！！
import os,sys,linecache
PATH=os.environ.get("PATH").split(";")
major=int(linecache.getline("ScratchOff.py",21)[6:])
minor=int(linecache.getline("ScratchOff.py",22)[6:])
releases=int(linecache.getline("ScratchOff.py",23)[9:])
build=int(linecache.getline("ScratchOff.py",24)[6:])
typenum=int(linecache.getline("ScratchOff.py",25)[8:])
x=int(linecache.getline("ScratchOff.py",26)[2:])
if int(typenum)<=6:
    DEBUG=True
else:
    DEBUG=False
version=str(major)+"."+str(minor)+"."+str(releases)+"."+str(build)+"."+str(typenum)+"."+str(x)
python64=""
python32=""
for i in PATH:
    try:
        if "python.exe" in os.listdir(i):
            if ("32" in i) or ("x86" in i):
                python32=i
            else:
                python64=i
    except FileNotFoundError as e:
        print("[WARN] Your PATH have a not found path, \""+str(e).split("'")[1]+"\".")
if python32=="":
    print("[ERROR] Python x86 not found. Please install Python x86 or remame folder name with 32/x86!")
    sys.exit(1)
if python64=="":
    print("[ERROR] Python x64 not found. Please install Python x64!")
    sys.exit(1)
os.system("md python")
os.system("\""+PATH[1]+"\\python\" -m venv python\\python64")
os.system("python\\python64\\Scripts\\python -m pip install --upgrade pip")
os.system("python\\python64\\Scripts\\pip install pywin32")
os.system("python\\python64\\Scripts\\pip install pygame==1.9.6")
os.system("python\\python64\\Scripts\\pip install pillow")
os.system("python\\python64\\Scripts\\pip install pyinstaller")
os.system("\""+PATH[3]+"\\python\" -m venv python\\python32")
os.system("python\\python32\\Scripts\\python -m pip install --upgrade pip")
os.system("python\\python32\\Scripts\\pip install pywin32")
os.system("python\\python32\\Scripts\\pip install pygame==1.9.6")
os.system("python\\python32\\Scripts\\pip install pillow")
os.system("python\\python32\\Scripts\\pip install pyinstaller")
if DEBUG:
    os.system("md Releases\\ScratchOff_"+version)
    os.system("python\\python64\\Scripts\\pyinstaller -F -w -i SO.ico ScratchOff.py")
    os.system("move dist\\ScratchOff.exe Releases\\ScratchOff_"+version+"\\ScratchOff64_RLS.exe")
    os.system("rd /s /q build")
    os.system("rd /s /q dist")
    os.system("del ScratchOff.spec")
    os.system("python\\python32\\Scripts\\pyinstaller -F -w -i SO.ico ScratchOff.py")
    os.system("move dist\\ScratchOff.exe Releases\\ScratchOff_"+version+"\\ScratchOff32_RLS.exe")
    os.system("rd /s /q build")
    os.system("rd /s /q dist")
    os.system("del ScratchOff.spec")
    with open("ScratchOff.py","r",encoding="utf-8") as file:
        text=file.readlines()
    text[15]="DEBUG=True\n"
    with open("ScratchOff.py","w",encoding="utf-8") as file:
        for i in text:
            file.write(i)
    os.system("python\\python64\\Scripts\\pyinstaller -F -c -i SO.ico ScratchOff.py")
    os.system("move dist\\ScratchOff.exe Releases\\ScratchOff_"+version+"\\ScratchOff64_DBG.exe")
    os.system("rd /s /q build")
    os.system("rd /s /q dist")
    os.system("del ScratchOff.spec")
    os.system("python\\python32\\Scripts\\pyinstaller -F -c -i SO.ico ScratchOff.py")
    os.system("move dist\\ScratchOff.exe Releases\\ScratchOff_"+version+"\\ScratchOff32_DBG.exe")
    os.system("rd /s /q build")
    os.system("rd /s /q dist")
    os.system("del ScratchOff.spec")
    with open("ScratchOff.py","r",encoding="utf-8") as file:
        text=file.readlines()
    text[15]="DEBUG=False\n"
    with open("ScratchOff.py","w",encoding="utf-8") as file:
        for i in text:
            file.write(i)
else:
    os.system("md Releases\\ScratchOff_"+version)
    os.system("python\\python64\\Scripts\\pyinstaller -F -w -i SO.ico ScratchOff.py")
    os.system("move dist\\ScratchOff.exe Releases\\ScratchOff_"+version+"\\ScratchOff64.exe")
    os.system("rd /s /q build")
    os.system("rd /s /q dist")
    os.system("del ScratchOff.spec")
    os.system("python\\python32\\Scripts\\pyinstaller -F -w -i SO.ico ScratchOff.py")
    os.system("move dist\\ScratchOff.exe Releases\\ScratchOff_"+version+"\\ScratchOff32.exe")
    os.system("rd /s /q build")
    os.system("rd /s /q dist")
    os.system("del ScratchOff.spec")

with open("temp.txt","w") as file:
    file.write("D")
os.system("xcopy website Releases\\ScratchOff_"+version+"\\website <temp.txt")
os.system("xcopy pictures Releases\\ScratchOff_"+version+"\\pictures /E <temp.txt")
os.system("del temp.txt")
os.system("copy font.ttc Releases\\ScratchOff_"+version+"\\font.ttc")
os.system("copy SO.ico Releases\\ScratchOff_"+version+"\\SO.ico")
os.system("rd /s /q python")