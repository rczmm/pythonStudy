# Python Project

## 项目简介
这是一个 Python 项目，包含多个脚本和工具，用于数据处理、算法实现、网络请求、地图导入等功能。项目旨在提供一系列实用的 Python 脚本，帮助开发者快速完成常见任务。

## 目录结构

├── pandas

│ ├── test.py 

│ └── test1.py 

├── script 

│ ├── dataChange.py 

│ ├── demo.py 

│ ├── importCenterLine.py 

│ ├── importCenterLine.spec 

│ ├── checkConfig.py 

│ ├── importLineSql.py 

│ ├── parseCoord.py 

│ ├── json_study.py 

│ ├── dict_study.py 

│ ├── requests_study.ipynb 

│ └── study_list.py 

├── test 

│ ├── test.py 

│ └── coord.py 

│ └── decode_data_coord.py 

└── README.md

## 环境依赖
- Python 3.6+
- pandas
- requests
- openpyxl
- pyproj
- pyautogui
- pygetwindow
- geopy
- pyadb3

## 安装步骤
1. **克隆仓库**
git clone https://github.com/yourusername/yourrepository.git
cd yourrepository

2. **安装依赖**

pip install -r requirements.txt

如果 `requirements.txt` 文件不存在，可以手动安装依赖：
   
pip install pandas requests openpyxl pyproj pyautogui pygetwindow geopy pyadb3

## 使用说明

### 数据处理脚本
- **dataChange.py**: 用于处理位置数据。
  python script/dataChange.py
- **checkConfig.py**: 用于处理配置数据并生成 SQL 语句。 
  python script/checkConfig.py
- **importLineSql.py**: 转换坐标并生成 SQL 语句。
- **parseCoord.py**: 解析坐标信息并输出特定数据。
### 地图导入工具
- **importCenterLine.py**: 用于将中心线信息导入 Excel。
### 网络请求示例
- **requests_study.ipynb**: Jupyter Notebook 文件，包含 requests 模块的使用示例。
### 学习脚本
- **json_study.py**: 包含 JSON 处理的示例代码。
- **dict_study.py**: 包含字典操作的学习脚本。
- **study_list.py**: 包含列表操作的学习脚本。
### 自动刷新网页
- **demo.py**: 实现自动刷新网页功能。
## 功能介绍

### pandas 模块
- **test.py**: 演示 pandas 数据处理流程，包含异常捕获装饰器和多个算法问题的实现。
- **test1.py**: 实现多个算法问题的解决方案，包括数独验证和求解、字符串查找、括号匹配等。

### script 模块
- **dataChange.py**: 处理位置数据，提取经纬度信息。
- **demo.py**: 实现自动刷新网页功能，模拟按下 F5 键。
- **importCenterLine.py**: 将中心线信息导入 Excel，支持坐标转换。
- **checkConfig.py**: 读取 Excel 文件中的配置数据并生成 SQL 语句。
- **importLineSql.py**: 转换坐标并生成 SQL 语句。
- **parseCoord.py**: 解析坐标信息并输出特定数据。
- **json_study.py**: 包含 JSON 处理的示例代码。
- **dict_study.py**: 包含字典操作的学习脚本。
- **requests_study.ipynb**: Jupyter Notebook 文件，包含 requests 模块的使用示例。
- **study_list.py**: 包含列表操作的学习脚本。

### test 模块
- **test.py**: 包含计时装饰器、斐波那契数列生成器等测试代码。
- **coord.py**: 处理坐标信息，包括获取当前位置和更改手机位置。
- **decode_data_coord.py**: 解析坐标数据并输出特定信息。

## 贡献指南
欢迎贡献代码和提出改进建议！请遵循以下步骤：
1. Fork 本仓库。
2. 创建一个新的分支：`git checkout -b my-feature-branch`。
3. 提交你的更改：`git commit -am 'Add some feature'`。
4. 推送到你的分支：`git push origin my-feature-branch`。
5. 提交 Pull Request。

## 许可证
本项目采用 MIT 许可证，详情请参见 [LICENSE](LICENSE) 文件。

---


  
  
  
  
  
  
  
  
  
   