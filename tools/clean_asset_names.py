import shutil
import os

renames = [
    ('landing_page/assets/images/AMENITIES ICON - 250x100_15+ Clubhouse Amenities.png', 'landing_page/assets/images/amenities_icon_15_clubhouse.png'),
    ('landing_page/assets/images/AMENITIES ICON - 250x100_5+ Pondside Amenities.png', 'landing_page/assets/images/amenities_icon_5_pondside.png'),
    ('landing_page/assets/images/AMENITIES ICON - 250x100_20+ Podium Amenities.png', 'landing_page/assets/images/amenities_icon_20_podium.png'),
    ('landing_page/assets/images/Victoria image - 400x405-01.jpg', 'landing_page/assets/images/victoria_image_400x405.jpg'),
    ('landing_page/assets/images/LANDING PAGE 1920X1080-01.jpg', 'landing_page/assets/images/landing_page_1920x1080.jpg'),
]

for orig, new_f in renames:
    if os.path.exists(orig):
        shutil.copy(orig, new_f)
        print(f"Copied {orig} -> {new_f}")

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

for orig, new_f in renames:
    html = html.replace(orig, new_f)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated index.html with clean URLs!")
