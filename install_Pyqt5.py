import os

os.system("pip install PyQt5")
os.system("sudo apt-get install python3-pyqt5")
os.system("sudo apt-get install qttools5-dev-tools")
os.system("echo 'alias pyqt=/usr/lib/x86_64-linux-gnu/qt5/bin/designer' >> ~/.bashrc && source ~/.bashrc")

print('\n\n run command: $ pyqt')