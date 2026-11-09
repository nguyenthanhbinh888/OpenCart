import sys
import os
import shutil
import zipfile

def prepare(hostname):
    domain = "http://nguyenthanhbinhth2901.infinityfree.io/"
    db_user = "if0_43392642"
    db_pass = "8gylENdUORVrp"
    db_name = "if0_43392642_opencart"
    
    opencart_dir = r"C:\Users\Admin\Desktop\opencart"
    upload_dir = os.path.join(opencart_dir, "upload")
    
    # 1. Update config.php
    config_content = f"""<?php
// APPLICATION
define('APPLICATION', 'Catalog');

// HTTP
define('HTTP_SERVER', '{domain}');

// DIR
define('DIR_OPENCART', rtrim(str_replace('\\\\', '/', __DIR__), '/') . '/');
define('DIR_APPLICATION', DIR_OPENCART . 'catalog/');
define('DIR_SYSTEM', DIR_OPENCART . 'system/');
define('DIR_EXTENSION', DIR_OPENCART . 'extension/');
define('DIR_IMAGE', DIR_OPENCART . 'image/');
define('DIR_STORAGE', DIR_SYSTEM . 'storage/');
define('DIR_LANGUAGE', DIR_APPLICATION . 'language/');
define('DIR_TEMPLATE', DIR_APPLICATION . 'view/template/');
define('DIR_CONFIG', DIR_SYSTEM . 'config/');
define('DIR_CACHE', DIR_STORAGE . 'cache/');
define('DIR_DOWNLOAD', DIR_STORAGE . 'download/');
define('DIR_LOGS', DIR_STORAGE . 'logs/');
define('DIR_SESSION', DIR_STORAGE . 'session/');
define('DIR_UPLOAD', DIR_STORAGE . 'upload/');

// DB
define('DB_DRIVER', 'mysqli');
define('DB_HOSTNAME', '{hostname}');
define('DB_USERNAME', '{db_user}');
define('DB_PASSWORD', '{db_pass}');
define('DB_DATABASE', '{db_name}');
define('DB_PREFIX', 'oc_');
define('DB_PORT', '3306');

// Cache
define('CACHE_ENGINE', 'file');
"""
    with open(os.path.join(upload_dir, "config.php"), "w", encoding="utf-8") as f:
        f.write(config_content)
        
    # 2. Update admin/config.php
    admin_config_content = f"""<?php
// APPLICATION
define('APPLICATION', 'Admin');

// HTTP
define('HTTP_SERVER', '{domain}admin/');
define('HTTP_CATALOG', '{domain}');

// DIR
define('DIR_OPENCART', rtrim(str_replace('\\\\', '/', dirname(__DIR__)), '/') . '/');
define('DIR_APPLICATION', DIR_OPENCART . 'admin/');
define('DIR_SYSTEM', DIR_OPENCART . 'system/');
define('DIR_EXTENSION', DIR_OPENCART . 'extension/');
define('DIR_IMAGE', DIR_OPENCART . 'image/');
define('DIR_STORAGE', DIR_SYSTEM . 'storage/');
define('DIR_CATALOG', DIR_OPENCART . 'catalog/');
define('DIR_LANGUAGE', DIR_APPLICATION . 'language/');
define('DIR_TEMPLATE', DIR_APPLICATION . 'view/template/');
define('DIR_CONFIG', DIR_SYSTEM . 'config/');
define('DIR_CACHE', DIR_STORAGE . 'cache/');
define('DIR_DOWNLOAD', DIR_STORAGE . 'download/');
define('DIR_LOGS', DIR_STORAGE . 'logs/');
define('DIR_SESSION', DIR_STORAGE . 'session/');
define('DIR_UPLOAD', DIR_STORAGE . 'upload/');

// DB
define('DB_DRIVER', 'mysqli');
define('DB_HOSTNAME', '{hostname}');
define('DB_USERNAME', '{db_user}');
define('DB_PASSWORD', '{db_pass}');
define('DB_DATABASE', '{db_name}');
define('DB_PREFIX', 'oc_');
define('DB_PORT', '3306');

// Cache
define('CACHE_ENGINE', 'file');

// OpenCart API
define('OPENCART_SERVER', 'https://www.opencart.com/');
"""
    with open(os.path.join(upload_dir, "admin", "config.php"), "w", encoding="utf-8") as f:
        f.write(admin_config_content)
        
    print("Updated config.php and admin/config.php successfully!")
    
    # 3. Create zip for InfinityFree htdocs
    out_zip = r"C:\Users\Admin\Desktop\htdocs_infinityfree.zip"
    print(f"Compressing upload/ contents into {out_zip}...")
    with zipfile.ZipFile(out_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(upload_dir):
            for file in files:
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, upload_dir)
                zipf.write(full_path, rel_path)
                
    print(f"Created {out_zip} successfully! Size: {os.path.getsize(out_zip)} bytes")

if __name__ == "__main__":
    host = sys.argv[1] if len(sys.argv) > 1 else "sql100.infinityfree.com"
    prepare(host)

