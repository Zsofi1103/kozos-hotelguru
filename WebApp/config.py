import configparser
import os

def db_config(filename='config.ini', section='Database'):
    config = configparser.ConfigParser()
    
    # Kikeressük a WebApp mappa helyét, majd visszalépünk egyet a gyökérbe
    base_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_path, '..', filename) 

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Nem találom a config fájlt itt: {file_path}")

    config.read(file_path)

    if not config.has_section(section):
        raise configparser.NoSectionError(section)

    return {
        'host': config.get(section, 'host'),
        'user': config.get(section, 'user'),
        'password': config.get(section, 'password'),
        'database': config.get(section, 'database'),
        'port': int(config.get(section, 'port'))
    }
