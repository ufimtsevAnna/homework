# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.


# n=input("Введите число: ")
# sum = 0
# for i in n:
#     if i.isdigit():
#         sum+=int(i)
# print (sum)

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# n = int(input())
# fact_list = []
# factorial = 1
# for i in range(1,n+1):
#     factorial*=i
#     fact_list.append(factorial)
# print(fact_list)

# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.


# n=int(input())
# dict_num={}
# for i in range (1, n+1):
#     dict_num[i]=round((1+1/i)**i, 2)
# print(dict_num)
# print(sum(dict_num.values()))


# Задайте список из N элементов,
# заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

# import random

# n = int(input())
# list_num = [random.randint(-n,n) for i in range(n)]
# print(list_num)

# file = open("File.txt","r")
# multi = 1

# for i in file:
#     multi*=list_num[int(i)]
# print(multi)