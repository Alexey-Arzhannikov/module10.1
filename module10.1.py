import time
from datetime import datetime
from threading import Thread


def wite_words(word_count, file_name):
    for i in range(1, word_count + 1):
        file = open(file_name, 'a', encoding='utf-8')
        file.write(f'Какое-то слово № {i}\n')
        time.sleep(0.1)
    print(f'Запись завершилась в файл {file_name}')


start_time_function = datetime.now()
wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')
end_time_function = datetime.now()
print(f'Время выполниения функций {end_time_function - start_time_function}')

start_time_thr = datetime.now()
thr_wite_words_1 = Thread(target=wite_words, args=(10, 'example5.txt'))
thr_wite_words_2 = Thread(target=wite_words, args=(30, 'example6.txt'))
thr_wite_words_3 = Thread(target=wite_words, args=(200, 'example7.txt'))
thr_wite_words_4 = Thread(target=wite_words, args=(100, 'example8.txt'))


thr_wite_words_1.start()
thr_wite_words_2.start()
thr_wite_words_3.start()
thr_wite_words_4.start()

thr_wite_words_1.join()
thr_wite_words_2.join()
thr_wite_words_3.join()
thr_wite_words_4.join()
end_time_thr = datetime.now()
print(f'Время выполнения потоков {end_time_thr - start_time_thr}')