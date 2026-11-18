import os
import shutil

os.makedirs('assets/img', exist_ok=True)
if os.path.exists('landing_page/assets/img/left-arrow.png'):
    shutil.copy('landing_page/assets/img/left-arrow.png', 'assets/img/left-arrow.png')
if os.path.exists('landing_page/assets/img/right-arrow.png'):
    shutil.copy('landing_page/assets/img/right-arrow.png', 'assets/img/right-arrow.png')

print("Copied arrows to assets/img/:")
print(os.path.exists('assets/img/left-arrow.png'))
print(os.path.exists('assets/img/right-arrow.png'))
