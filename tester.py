from turtle_app import TurtleApp

if __name__ == "__main__":
    driver = input("Would you like to enter driver control? (y/n) ") == "y"
    t = TurtleApp(driver)
    t.cycle()