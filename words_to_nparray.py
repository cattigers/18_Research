import pandas as pd
import numpy as np
import re

if __name__ == "__main__":

    df = pd.read_csv('./words.csv', delimiter=',')
    words = list(df)

    base = 44032
    first_syl = 588
    last_syl = 28

    first_syl_list = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ',
                    'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ',
                    'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

    mid_syl_list = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ',
                    'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ',
                    'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']

    last_syl_list = ['', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ',
                    'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ',
                    'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
    words_list = []
    for word in words:
        word_to_list = list(word)
        result = []
        for ch in word_to_list:
            if re.match('.*[ㄱ-ㅎ ㅏ-ㅣ가-힣]+.*', ch) is not None:

                char_code = ord(ch) - base
                char_first = int(char_code/first_syl)

                result.append(first_syl_list[char_first])

                char_second = int((char_code-(first_syl*char_first))/last_syl)
                result.append(mid_syl_list[char_second])

                char_last = int((char_code-(first_syl*char_first)-(last_syl*char_second)))
                if char_last != 0:
                    result.append(last_syl_list[char_last])
        words_list.append(result)

    #print(words_list)

    char_arr = ['S', 'E', 'ㄱ', 'ㄴ', 'ㄷ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅅ', 'ㅇ', 'ㅈ',
                'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ', 'ㅏ', 'ㅑ', 'ㅓ', 'ㅕ',
                'ㅗ', 'ㅛ', 'ㅜ', 'ㅠ', 'ㅡ', 'ㅣ', 'ㅐ', 'ㅒ', 'ㅔ',
                'ㅖ', 'ㅢ', 'ㅚ', 'ㅟ']

    num_dic = {n: i for i, n in enumerate(char_arr)}
    dic_len = len(num_dic)

    output_batch = []
    target_batch = []
    for a in words_list:
        a.insert(0, 'S')
        out = [num_dic[n] for n in a]
        a.pop(0)
        a.append('E')
        tar = [num_dic[n] for n in a]
        output_batch.append(np.eye(dic_len)[out])
        target_batch.append(tar)

    what_i_want_out = np.array(output_batch) # what_i_want[i] == i+1 번째 단어(model_n_i+1)
    what_i_want_tar = np.array(target_batch) # what_i_want[i] == i+1 번째 단어(model_n_i+1)

    print(what_i_want_out)
    print(what_i_want_tar)


    # with open('words_array.txt', 'w', encoding='utf-8') as f:
    #     f.write(str(words)+'\n'*3)
    #     f.write('output_batch: \n\n'+str(what_i_want_out))
    #     f.write('target_batch: \n\n'+str(what_i_want_tar))

    print("succeeded")

