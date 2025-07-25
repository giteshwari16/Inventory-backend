from django.db import migrations

def add_electronics_store_data(apps, schema_editor):
    Product = apps.get_model('inventory', 'Product')
    Product.objects.bulk_create([
        Product(name='Apple iPhone 14 Pro', quantity=12, price=119999.00, description='256GB, Deep Purple, 6.1-inch Super Retina XDR display'),
        Product(name='Samsung Galaxy S23 Ultra', quantity=8, price=104999.00, description='12GB RAM, 256GB, Phantom Black, 6.8-inch QHD+'),
        Product(name='Sony WH-1000XM5 Headphones', quantity=20, price=29990.00, description='Wireless Noise Cancelling, Black'),
        Product(name='Dell XPS 13 Laptop', quantity=5, price=139999.00, description='13.4-inch FHD+, 16GB RAM, 1TB SSD, Windows 11'),
        Product(name='Apple MacBook Air M2', quantity=7, price=124900.00, description='13.6-inch, 8GB RAM, 512GB SSD, Space Grey'),
        Product(name='Canon EOS 1500D DSLR', quantity=4, price=42999.00, description='24.1MP, 18-55mm Lens, WiFi, Black'),
        Product(name='Samsung 55" 4K QLED TV', quantity=3, price=84999.00, description='Smart TV, Ultra HD, Voice Assistant'),
        Product(name='HP DeskJet 2331 Printer', quantity=15, price=3999.00, description='All-in-One, Color, USB, Compact'),
        Product(name='Apple iPad 10th Gen', quantity=10, price=44900.00, description='10.9-inch, WiFi, 64GB, Silver'),
        Product(name='JBL Flip 6 Bluetooth Speaker', quantity=25, price=9999.00, description='Waterproof, 12h Playtime, Blue'),
        Product(name='Mi Smart Band 7', quantity=30, price=3499.00, description='1.62" AMOLED, 120+ fitness modes, Black'),
        Product(name='Logitech MX Master 3S Mouse', quantity=18, price=8995.00, description='Wireless, Ergonomic, Graphite'),
        Product(name='Google Nest Mini (2nd Gen)', quantity=14, price=4499.00, description='Smart Speaker, Voice Assistant, Chalk'),
        Product(name='Amazon Echo Show 8', quantity=6, price=10999.00, description='8" HD Display, Alexa, Charcoal'),
        Product(name='WD 2TB External HDD', quantity=22, price=5999.00, description='USB 3.0, Portable, Black'),
        Product(name='TP-Link Archer C6 Router', quantity=16, price=2999.00, description='1200 Mbps, Dual Band, MU-MIMO'),
        Product(name='Philips Hue Smart Bulb', quantity=40, price=1999.00, description='White & Color Ambiance, Bluetooth'),
        Product(name='Samsung Galaxy Tab S8', quantity=9, price=58999.00, description='11-inch, 8GB RAM, 128GB, WiFi'),
        Product(name='OnePlus Buds Pro 2', quantity=17, price=11999.00, description='ANC, Wireless, Black'),
        Product(name='Asus ROG Strix Gaming Laptop', quantity=2, price=179999.00, description='15.6-inch, RTX 3070, 32GB RAM, 1TB SSD'),
        # 50 more items below
        Product(name='Lenovo ThinkPad X1 Carbon', quantity=6, price=129999.00, description='14-inch, 16GB RAM, 512GB SSD, Black'),
        Product(name='Bose QuietComfort 45', quantity=12, price=24990.00, description='Wireless Noise Cancelling Headphones, Silver'),
        Product(name='Apple Watch Series 8', quantity=15, price=45900.00, description='GPS, 45mm, Midnight Aluminum'),
        Product(name='Samsung Galaxy Watch 5', quantity=10, price=28999.00, description='Bluetooth, 44mm, Graphite'),
        Product(name='LG 32" 4K UHD Monitor', quantity=8, price=27999.00, description='IPS, HDR10, 60Hz, White'),
        Product(name='BenQ GW2780 Monitor', quantity=11, price=15999.00, description='27-inch, FHD, Eye-Care, Black'),
        Product(name='Canon PIXMA G2020 Printer', quantity=7, price=12499.00, description='All-in-One, Ink Tank, USB'),
        Product(name='Apple AirPods Pro 2nd Gen', quantity=20, price=26900.00, description='Active Noise Cancellation, White'),
        Product(name='Samsung T7 1TB SSD', quantity=13, price=10999.00, description='Portable, USB 3.2, Blue'),
        Product(name='Seagate 4TB External HDD', quantity=9, price=8999.00, description='USB 3.0, Black'),
        Product(name='TP-Link Deco M5 WiFi System', quantity=5, price=15999.00, description='Whole Home Mesh, 3-Pack'),
        Product(name='Philips 24W LED Desk Lamp', quantity=25, price=2499.00, description='Touch Control, Dimmable, White'),
        Product(name='Sony PlayStation 5', quantity=3, price=49999.00, description='Disc Edition, White'),
        Product(name='Xbox Series X', quantity=2, price=52999.00, description='1TB SSD, Black'),
        Product(name='Nintendo Switch OLED', quantity=4, price=34999.00, description='White Joy-Con, 7-inch OLED'),
        Product(name='GoPro HERO11 Black', quantity=6, price=41999.00, description='5.3K60 Ultra HD, Waterproof'),
        Product(name='DJI Mini 3 Pro Drone', quantity=2, price=74999.00, description='4K Camera, 34min Flight, Grey'),
        Product(name='Kindle Paperwhite 11th Gen', quantity=18, price=13999.00, description='6.8-inch, 8GB, Black'),
        Product(name='Fire TV Stick 4K Max', quantity=22, price=6499.00, description='Wi-Fi 6, Alexa Voice Remote'),
        Product(name='Samsung Galaxy Buds2', quantity=16, price=11999.00, description='ANC, Wireless, Olive'),
        Product(name='Jabra Elite 7 Pro', quantity=10, price=17999.00, description='Bluetooth Earbuds, Titanium Black'),
        Product(name='Apple Magic Keyboard', quantity=8, price=9999.00, description='Wireless, White'),
        Product(name='Logitech C920 HD Webcam', quantity=14, price=7999.00, description='1080p, Stereo Audio, Black'),
        Product(name='Anker PowerCore 20000', quantity=20, price=3499.00, description='mAh Power Bank, Black'),
        Product(name='SanDisk 128GB microSDXC', quantity=30, price=1599.00, description='A1, U1, Full HD, Red/Gray'),
        Product(name='TP-Link HS100 Smart Plug', quantity=25, price=1299.00, description='Wi-Fi, No Hub Required'),
        Product(name='Philips SHB3075 Headphones', quantity=12, price=2499.00, description='On-Ear, Bluetooth, Black'),
        Product(name='Mi 360° Home Security Camera', quantity=18, price=2999.00, description='1080p, Night Vision, White'),
        Product(name='Realme Smart TV Stick', quantity=15, price=2999.00, description='FHD, Quad Core, Black'),
        Product(name='HP X1000 Wired Mouse', quantity=40, price=399.00, description='USB, Black'),
        Product(name='Dell KM117 Wireless Keyboard & Mouse', quantity=10, price=1999.00, description='Combo, Black'),
        Product(name='Samsung EVO Plus 256GB microSD', quantity=22, price=2999.00, description='U3, 4K, Red/White'),
        Product(name='Sony SRS-XB13 Bluetooth Speaker', quantity=17, price=3999.00, description='Extra Bass, Blue'),
        Product(name='Apple Lightning to USB Cable', quantity=50, price=1799.00, description='1m, White'),
        Product(name='AmazonBasics HDMI Cable 6ft', quantity=35, price=499.00, description='High-Speed, Black'),
        Product(name='Portronics Power Brick III', quantity=28, price=1299.00, description='10000mAh, Black'),
        Product(name='Zebronics Zeb-Fit4220CH', quantity=19, price=2499.00, description='Smart Fitness Band, Black'),
        Product(name='boAt Rockerz 255 Pro+', quantity=24, price=1599.00, description='Bluetooth Neckband, Blue'),
        Product(name='Noise ColorFit Pulse 2', quantity=21, price=1999.00, description='Smartwatch, Jet Black'),
        Product(name='Syska 9W Smart LED Bulb', quantity=32, price=799.00, description='Wi-Fi, Color Changing'),
        Product(name='Canon SELPHY CP1300', quantity=3, price=10999.00, description='Wireless Photo Printer, Black'),
        Product(name='Samsung Galaxy SmartTag', quantity=15, price=2499.00, description='Bluetooth Tracker, Black'),
        Product(name='TP-Link TL-WR841N Router', quantity=18, price=1099.00, description='300Mbps, Wi-Fi, White'),
        Product(name='Lenovo Tab M10 FHD', quantity=7, price=17999.00, description='10.1-inch, 4GB RAM, 64GB, Iron Grey'),
        Product(name='HP 15s Laptop', quantity=5, price=45999.00, description='15.6-inch, 8GB RAM, 512GB SSD, Silver'),
        Product(name='Acer Nitro 5 Gaming Laptop', quantity=3, price=89999.00, description='15.6-inch, RTX 3050, 16GB RAM, 512GB SSD'),
        Product(name='Apple AirTag', quantity=20, price=3190.00, description='Bluetooth Tracker, White'),
        Product(name='Xiaomi Mi Box 4K', quantity=13, price=3499.00, description='Android TV, Black'),
        Product(name='TP-Link UB400 Bluetooth Adapter', quantity=25, price=599.00, description='USB, Black'),
        Product(name='Sony MDR-EX150AP Earphones', quantity=30, price=999.00, description='Wired, Blue'),
        Product(name='Samsung Galaxy Buds Live', quantity=12, price=14999.00, description='Wireless Earbuds, Mystic Bronze'),
    ])

def remove_electronics_store_data(apps, schema_editor):
    Product = apps.get_model('inventory', 'Product')
    Product.objects.filter(name__in=[
        'Apple iPhone 14 Pro', 'Samsung Galaxy S23 Ultra', 'Sony WH-1000XM5 Headphones', 'Dell XPS 13 Laptop',
        'Apple MacBook Air M2', 'Canon EOS 1500D DSLR', 'Samsung 55" 4K QLED TV', 'HP DeskJet 2331 Printer',
        'Apple iPad 10th Gen', 'JBL Flip 6 Bluetooth Speaker', 'Mi Smart Band 7', 'Logitech MX Master 3S Mouse',
        'Google Nest Mini (2nd Gen)', 'Amazon Echo Show 8', 'WD 2TB External HDD', 'TP-Link Archer C6 Router',
        'Philips Hue Smart Bulb', 'Samsung Galaxy Tab S8', 'OnePlus Buds Pro 2', 'Asus ROG Strix Gaming Laptop',
        'Lenovo ThinkPad X1 Carbon', 'Bose QuietComfort 45', 'Apple Watch Series 8', 'Samsung Galaxy Watch 5',
        'LG 32" 4K UHD Monitor', 'BenQ GW2780 Monitor', 'Canon PIXMA G2020 Printer', 'Apple AirPods Pro 2nd Gen',
        'Samsung T7 1TB SSD', 'Seagate 4TB External HDD', 'TP-Link Deco M5 WiFi System', 'Philips 24W LED Desk Lamp',
        'Sony PlayStation 5', 'Xbox Series X', 'Nintendo Switch OLED', 'GoPro HERO11 Black', 'DJI Mini 3 Pro Drone',
        'Kindle Paperwhite 11th Gen', 'Fire TV Stick 4K Max', 'Samsung Galaxy Buds2', 'Jabra Elite 7 Pro',
        'Apple Magic Keyboard', 'Logitech C920 HD Webcam', 'Anker PowerCore 20000', 'SanDisk 128GB microSDXC',
        'TP-Link HS100 Smart Plug', 'Philips SHB3075 Headphones', 'Mi 360° Home Security Camera', 'Realme Smart TV Stick',
        'HP X1000 Wired Mouse', 'Dell KM117 Wireless Keyboard & Mouse', 'Samsung EVO Plus 256GB microSD',
        'Sony SRS-XB13 Bluetooth Speaker', 'Apple Lightning to USB Cable', 'AmazonBasics HDMI Cable 6ft',
        'Portronics Power Brick III', 'Zebronics Zeb-Fit4220CH', 'boAt Rockerz 255 Pro+', 'Noise ColorFit Pulse 2',
        'Syska 9W Smart LED Bulb', 'Canon SELPHY CP1300', 'Samsung Galaxy SmartTag', 'TP-Link TL-WR841N Router',
        'Lenovo Tab M10 FHD', 'HP 15s Laptop', 'Acer Nitro 5 Gaming Laptop', 'Apple AirTag', 'Xiaomi Mi Box 4K',
        'TP-Link UB400 Bluetooth Adapter', 'Sony MDR-EX150AP Earphones', 'Samsung Galaxy Buds Live',
    ]).delete()

class Migration(migrations.Migration):
    dependencies = [
        ('inventory', '0003_add_default_products'),
    ]
    operations = [
        migrations.RunPython(add_electronics_store_data, remove_electronics_store_data),
    ] 