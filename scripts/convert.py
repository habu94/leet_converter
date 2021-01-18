#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32
from std_msgs.msg import String

i = 0
j = 0

def main(reed_data):
    word = reed_data.data
    num = len(word)
    wordlist = []
    con_word = ''
    for i in range(num):
        wordlist.append(word[i])
    for j in wordlist:
        if j == 'A': #大文字
            con_word = con_word + '4'
        elif j == 'B':
            con_word = con_word + '|3'
        elif j == 'C':
            con_word = con_word + '['
        elif j == 'D':
            con_word = con_word + '|)'
        elif j == 'E':
            con_word = con_word + '3'
        elif j == 'F':
            con_word = con_word + '|='
        elif j == 'G':
            con_word = con_word + '6'
        elif j == 'H':
            con_word = con_word + '#'
        elif j == 'I':
            con_word = con_word + '1'
        elif j == 'J':
            con_word = con_word + '_|'
        elif j == 'K':
            con_word = con_word + '|<'
        elif j == 'L':
            con_word = con_word + '|_'
        elif j == 'M':
            con_word = con_word + '|v|'
        elif j == 'N':
            con_word = con_word + 'И'
        elif j == 'O':
            con_word = con_word + '()'
        elif j == 'P':
            con_word = con_word + '|*'
        elif j == 'Q':
            con_word = con_word + '0_'
        elif j == 'R':
            con_word = con_word + '|2'
        elif j == 'S':
            con_word = con_word + '5'
        elif j == 'T':
            con_word = con_word + '7'
        elif j == 'U':
            con_word = con_word + '(_)'
        elif j == 'V':
            con_word = con_word + '|/'
        elif j == 'W':
            con_word = con_word + 'Ш'
        elif j == 'X':
            con_word = con_word + '><'
        elif j == 'Y':
            con_word = con_word + 'Ч'
        elif j == 'Z':
            con_word = con_word + '2'
        else:
            con_word = con_word + j

    print("大文字のみ変換 ⇒ " + con_word)

    s_character = {'a':'@', 'b':'|o', 'c':'ⓒ', 'd':'c|', 'e':'ⓔ', 'f':'ℱ', 'g':'9', 'i':'¡', 'j':'¿', 'k':'|x', 'l':'|', 'r':'|-', 's':'z', 't':'+', 'u':'µ', 'w':'ω', 'x':'×', 'y':'ч', 'z':'s'}
    con_word = con_word.translate(str.maketrans(s_character)) #小文字

    print("小文字も変換 ⇒ " + con_word)

rospy.init_node('convert')
sub = rospy.Subscriber('reed_data', String, main)
rate = rospy.Rate(10)
while not rospy.is_shutdown():
    rate.sleep()
rospy.spin()
