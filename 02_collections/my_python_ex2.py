# -*- coding:utf-8 -*-

if __name__ == "__main__":
    name_list = ("Bill", "Anne", "Angy", "Cony", "Daniel", "Occhan")
    my_name = "Angy"

    for i in range(len(name_list)):
        if name_list[i]==my_name:
            print(str(i+1) + ". My name is " + str(name_list[i]) + ".")

        else:
            print(str(i+1) + ". " + name_list[i] + " is my classmate.")




