
'''
Created on ٢٩‏/٠٤‏/٢٠١٠

@Created by: Muhammad Altabba
'''

if __name__ == '__main__':
    import os
    from os.path import join, getsize
    for root, dirs, files in os.walk('D:\\1\\Learning\\NLP\\برامج\\الخليل\\AlKhalil_2\\db\\nouns\\roots\\'):
        for file in files:
            print(file);
        print(''.join([root, "consumes", " "]));
        print(sum(getsize(join(root, name)) for name in files), " ")
        print("bytes in", len(files), "non-directory files")
        if 'CVS' in dirs:
            dirs.remove('CVS')  # don't visit CVS directories
