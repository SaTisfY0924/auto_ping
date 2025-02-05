import openpyxl
import subprocess

# 打开Excel文件
workbook = openpyxl.load_workbook('/Users/songyaya/Desktop/ws/Auto_ping/auto_ip.xlsx')
sheet = workbook['Sheet1']

# 遍历每一行
for row in sheet.iter_rows(min_row=2, values_only=True):  # 从第二行开始，跳过标题行
    seq = row[0]  # 序号
    name = row[1]  # IP名称
    ip = row[2]  # IP地址

    # 执行ping命令
    result = subprocess.run(['ping', '-c', '1', ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # 判断ping是否成功
    if result.returncode == 0:
        print(f"{seq} {name} {ip} ping成功")
    else:
        print(f"{seq} {name} {ip} ping失败")