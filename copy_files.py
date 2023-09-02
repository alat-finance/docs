import os
import shutil

folder_path = './pages'
base_filename = '_meta'
source_language = 'en'
target_languages = ['zh', 'id', 'hi', 'tr', 'ru', 'fr', 'pt', 'es', 'vi', 'ar']

for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file == f'{base_filename}.{source_language}.json':
            source_path = os.path.join(root, file)
            source_dir = os.path.dirname(source_path)

            for lang in target_languages:
                target_file = f'{base_filename}.{lang}.json'
                target_path = os.path.join(source_dir, target_file)

                if not os.path.exists(target_path):
                    shutil.copy(source_path, target_path)
                    print(f'Copied {file} to {target_file} in {source_dir}')
                else:
                    print(f'{target_file} already exists in {source_dir}. Skipping...')
