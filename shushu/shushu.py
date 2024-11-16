'''
References:
1. https://scottyeung.top/2019/%E6%98%A5%E7%A7%8B%E5%8F%A4%E7%AD%AE%E6%B3%95/
2. PPT in class

Note: I want to follow the pipeline of "春秋古筮法", so the code may be verbose at the first galance.
'''

import numpy as np

def one_bian(number: int):
    '''
    Compute 1变, the basic component of the whole pipeline. The process:
    1. Divide "number" cards into 2 piles randomly
    2. Take 1 card from arbitrary pile. But as mentioned in class, we take from right
    3. Divide two numbers of two piles by 4, and throw away the remainder. If remainder is 0, regard it as 4
    4. Add up the two piles together, return the number of remaining cards

    :param number: the number of card to compute in this "bian", 49 initially
    :return: the number of remaining cards
    '''
    # random int of [low, high). No pile will contain 0 card
    left = np.random.randint(low=1, high=number)
    right = number - left
    print("Initial left: ", left)
    print("Initial right: ", right)
    right -= 1
    remainder_left = left % 4
    remainder_right = right % 4
    left -= remainder_left if remainder_left != 0 else 4
    right -= remainder_right if remainder_right != 0 else 4
    print("After left: ", left)
    print("After right: ", right)
    return left + right

def one_yao():
    '''
    Compute the result of 1爻. The process:
    1. Select 49 cards initially
    2. After 3变, get the remaining number of cards
    3. Divide the remainder by 4, and the result will be one number of 6, 7, 8, 9,
    each of them represent 1爻
    :return: One number of 6, 7, 8, 9
    '''
    init_sel = 49
    for i in range(3):
        print(f"第{i+1}变")
        init_sel = one_bian(init_sel)
    return init_sel / 4

def six_yao():
    '''
    One 重卦 is composed of 六爻
    卦象中爻的顺序从下到上
    :return: a list of 6 number
    '''
    six = np.zeros(6)
    for i in range(6):
        print("")
        print(f"第{i+1}爻")
        six[i] = one_yao()
    return six

def main():
    six = six_yao()
    bian_yao = np.sum(six == 9) + np.sum(six == 6)
    print("")
    print("六爻的结果为 ", six)
    print("其中变爻的数量为 ", bian_yao)
    print("解读指南")
    print("1. 卦象中爻的顺序自下到上，对应结果的从左到右")
    print("2. 变爻的作用：")
    effect_bian_yao = '''
    1. 六爻皆不变者，则占本卦卦辞;
    2. 一爻变者，以本卦变爻之辞占;
    3. 二爻变者，以本卦二变爻之辞占，而以上爻之辞为主;
    4. 三爻变者，占本卦及支卦的卦辞，而以本卦为主;
    5. 四爻变者，以之卦中二不变之爻辞占，而以下爻为主;
    6. 五爻变者，以之卦中不变爻的爻辞占;
    7. 六爻皆变者，以乾坤二用之辞占，并参考其支卦卦辞;
    '''
    print(effect_bian_yao)
    print("3. 周易的卦象爻辞解释网上随处可以找到，这里就不直接给出")

if __name__ == "__main__":
    main()