import pandas as pd

# def CsvToXlsx(filename):
#     # filepath = f"docs/"+filename
# filepath = 'docs/test1.csv'
filepath = 'docs/esim_7_smokecases.csv'

# 读取以utf-8编码的CSV文件
df = pd.read_csv(filepath, encoding='utf-8')

# 创建ExcelWriter对象
outputPath = 'docs/output_file.xlsx'
writer = pd.ExcelWriter(outputPath, engine='xlsxwriter')

# 将数据写入到xlsx文件中
df.to_excel(writer, index=False, sheet_name='Sheet1')

# 关闭ExcelWriter对象
writer.close()

print("CSV文件已成功转换为xlsx格式并保存，中文不乱码。")
