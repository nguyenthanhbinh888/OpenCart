<?php
// APPLICATION
define('APPLICATION', 'Admin');

// Detect Environment
$http_host = $_SERVER['HTTP_HOST'] ?? 'localhost:8000';
$is_local = (strpos($http_host, 'localhost') !== false || strpos($http_host, '127.0.0.1') !== false || strpos($http_host, '.lhr.life') !== false);

if ($is_local) {
    define('HTTP_SERVER', 'http://' . $http_host . '/admin/');
    define('HTTP_CATALOG', 'http://' . $http_host . '/');
    define('DB_HOSTNAME', '127.0.0.1');
    define('DB_USERNAME', 'root');
    define('DB_PASSWORD', '123456');
    define('DB_DATABASE', 'opencart');
} else {
    define('HTTP_SERVER', 'http://nguyenthanhbinhth2901.infinityfree.io/admin/');
    define('HTTP_CATALOG', 'http://nguyenthanhbinhth2901.infinityfree.io/');
    define('DB_HOSTNAME', 'sql311.infinityfree.com');
    define('DB_USERNAME', 'if0_43392642');
    define('DB_PASSWORD', '8gy1ENdUORVrp');
    define('DB_DATABASE', 'if0_43392642_opencart');
}

// DIR
define('DIR_OPENCART', rtrim(str_replace('\\', '/', dirname(__DIR__)), '/') . '/');
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
define('DB_PREFIX', 'oc_');
define('DB_PORT', '3306');

// Cache
define('CACHE_ENGINE', 'file');

// OpenCart API
define('OPENCART_SERVER', 'https://www.opencart.com/');
