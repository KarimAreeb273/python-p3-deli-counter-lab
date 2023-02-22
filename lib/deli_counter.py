katz_deli = []
areeb_deli = ["Areeb"]

def line(list):
    if not list:
        print("The line is currently empty.")
    else:
        message = "The line is currently: "
        for i in range(len(list)):
            message += f'{i + 1}. {list[i]}\n'
        print (message)

line(katz_deli)
line(areeb_deli)

def take_a_number(list, new_list):
    list.append(new_list)
    message = f'Welcome, {list[-1]}. You are number {len(list)} in line.'
    print(message)

take_a_number(areeb_deli, "Mariam")
take_a_number(areeb_deli, "Karim")

def now_serving(person):
    if not person:
        print ("There is nobody waiting to be served!")
    else:
        print (f'Currently serving: {person[0]}.')
        del person[0]
    pass

now_serving(areeb_deli)
now_serving(areeb_deli)
now_serving(areeb_deli)
now_serving(areeb_deli)


# def line(katz_deli):
#     if not katz_deli:
#         print("The line is currently empty.")
#     else:
#         message = "The line is currently:"
#         for i in range(len(katz_deli)):
#             message += f' {i + 1}. {katz_deli[i]}'
#         print(message)
