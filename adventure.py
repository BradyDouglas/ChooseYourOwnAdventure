name = input("Please type your name: ")
print(f"Welcome {name}, to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()


if answer == "left":
    answer = input("You come to a river, you can walk around it or swim accross? (swim/walk) ").lower()

    if answer == "swim":
        print("You swam across and were eaten by a kraken. Please consider going right next time.")
    elif answer == "walk":
        print("You continued to walk for endless hours before inevitably running out of water and dying. Please consider going right next time.")
    else:
        print("Not a valid option. Game over. Please consider entering a presented option.")

elif answer == "right":
    answer = input("You come to a bridge that looks quite unsteady, would you like to cross it or head back? (cross/back) ").lower()

    if answer == "back":
        print("You head back to the main road and see a merchant waiting, do you speak to them? (yes/no) ").lower()

        if answer == "yes":
            print("The stranger turns out to be a wizard and can grant any wish you would like. Congrats, you have won!")
        elif answer == "no":
            print("The stranger is disappointed that you would ignore them and knocks you out. You lose. Please consider speaking to the stranger")
        else:
            print("Not a valid option. Game over")
    elif answer == "cross":
        print("You attempt to cross the bridge before it collapses. This leads you to falling to your death.")
    else:
        print("Not a valid option. Game over. Please consider entering a presented option.")

else:
    print("Not a valid option. Game over.")

print(f"Thank you for playing, {name}")