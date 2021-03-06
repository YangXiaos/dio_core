# @Time         : 18-2-13 下午9:06
# @Author       : DioMryang
# @File         : setup.py
# @Description  :
from setuptools import setup, find_packages
from dio_core import __version__


setup(
    name="dio_core",
    version=__version__,
    description="dio采集系统核心",
    author="dio_mryang",
    url="https://github.com/YangXiaos/",
    packages=find_packages(), install_requires=["pymysql", 'pymongo', 'redis', 'sqlalchemy', 'beautifulsoup4', 'requests',
                                                'threadpool', 'chardet', 'paramiko', 'lxml', 'Pillow', 'numpy',
                                                'selenium', 'sshtunnel', 'pyftpdlib', 'openpyxl', 'jsonpath',
                                                'fontTools', 'scikit-image', 'opencv-python', 'mitmproxy']
)
