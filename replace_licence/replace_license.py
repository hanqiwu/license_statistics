# encoding:utf-8
import wmi
import time
import sys
import os

chengdu_list =[['10.69.30.207', r'10.69.30.206\test', 'Baseport00']]

japan_list = [['172.20.7.81', r'172.20.7.81\test', 'Baseport00'], ['172.20.7.82', r'172.20.7.82\test', 'Baseport00'], ['172.20.7.83', r'172.20.7.83test', 'Baseport00'],
              ['172.20.7.84', r'172.20.7.84\test', 'Baseport00'], ['172.20.7.85', r'172.20.7.82\test', 'Baseport00'], ['172.20.7.86', r'172.20.7.85\test', 'Baseport00'],
              ['172.20.7.87', r'172.20.7.82\test', 'Baseport00'], ['172.20.7.88', r'172.20.7.82\test', 'Baseport00'], ['172.20.7.90', r'172.20.7.82\test', 'Baseport00'],
              ['172.20.7.91', r'172.20.7.82\test', 'Baseport00']]


def replace_license(location, license_path):
    computer_list = []

    if location == 'Japan':
        computer_list = japan_list
        print('Update license file for Japan computer')
    elif location == 'Chengdu':
        computer_list = chengdu_list
        print('Update license file for Chengdu computer')

    for computer in computer_list:
        print('Start to update license file for %s computer:%s' % (location, computer[0]))
        try:
            conn = wmi.WMI(computer=computer[0], user=computer[1], password=computer[2])
        except:
            print("Connect to %s is failed" % computer[0])
            continue
        else:
            pass
    # for sys in conn.Win32_OperatingSystem():
    #     print("Version:%s" % sys.Caption.encode("UTF8"),"Vernum:%s" % sys.BuildNumber)  #系统信息
    #     print(sys.OSArchitecture.encode("UTF8"))  # 系统的位数
    #     print(sys.NumberOfProcesses)  # 系统的进程数
    # cmd_call_bat = r"cmd /c md c:\test\test2"
    # conn.Win32_Process.Create(CommandLine=cmd_call_bat)
    # cmd_call_bat_1 = r"cmd /c echo %s > %s" % (content, r'c:\test\test2\test.txt')
        file_path = r'C:\Freescale\CW_SC_3900FP_v10.8.3\SC\license.dat'
        now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        cmd_call = r"cmd /c copy  %s %s" % (file_path, file_path+'_'+now +'.bak')
        conn.Win32_Process.Create(CommandLine=cmd_call)

        with open(license_path, "r") as file:
            for num, line in enumerate(file):
                templine = line.strip("\n")
                templine = templine.replace("\"", "^\"")
                try:
                    if num == 0:
                        cmd_call_bat_0 = r"cmd /c echo %s> %s" % (templine, file_path)
                        conn.Win32_Process.Create(CommandLine=cmd_call_bat_0)
                    else:
                        cmd_call_bat = r"cmd /c echo %s>> %s" % (templine, file_path)
                        conn.Win32_Process.Create(CommandLine=cmd_call_bat)
                except:
                    print("Update license.dat on %s is failed" % computer[0])
                    continue
                else:
                    pass
        print("%s is done" % computer[0])

def usage():
    print('!!!!!')
    exit(1)


def main(argv):
    if len(argv) < 2:
        usage()
    else:
        if argv[0] != 'Japan' and argv[0] != 'Chengdu':
            usage()
        if os.path.exists(argv[1]):
            replace_license(argv[0], argv[1])
        else:
            usage()


if __name__ == '__main__':
    main(sys.argv[1:])