
# def user_choice():
#     #khởi taoj giá trị ban đầu 
#     choice ='wrong'
#     whithin_range = False
#     #vòng lặp xét thỏa mãn: pải số hya ko và nằm trong khoảng (0,10)
#     while choice.isdigit()==False or whithin_range  == False:
#         choice =input('Enter a number(0-10): ')
#         if choice.isdigit()==False:
#             print('Error: This is not a digital!!!')
#         else:
#             if int(choice) in range(0,10):
#                 whithin_range =True
#             else:
#                 whithin_range=False
                
#     return int(choice)
            
# print(user_choice())
row1=[' ',' ',' ']
row2=[' ',' ',' ']
row3=[' ',' ',' ']
print('   |   |')
print(' ' + row1[0] + ' | ' + row1[1] + ' | ' + row1[2])
print('   |   |')
print('-----------')
print('   |   |')
print(' ' + row2[0] + ' | ' + row2[1] + ' | ' + row2[2])
print('   |   |')
print('-----------')
print('   |   |')
print(' ' + row3[0] + ' | ' + row3[1] + ' | ' + row3[2])
print('   |   |')

