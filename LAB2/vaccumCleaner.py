# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 12:02:00 2024

@author: Admin
"""

def vacuum_world():
    # Initialize goal state: 0 indicates Clean and 1 indicates Dirty
    goal_state = {'A': '0', 'B': '0'}
    cost = 0

    # User input for vacuum location and status
    location_input = input("Enter location of vacuum (A/B): ").strip().upper()
    status_input = input(f"Enter status of {location_input} (0 for Clean, 1 for Dirty): ").strip()
    status_input_complement = input(f"Enter status of other room ({'B' if location_input == 'A' else 'A'}): ").strip()

    print("Initial Location Condition: " + str(goal_state))

    if location_input == 'A':
        print("Vacuum is placed in Location A")

        if status_input == '1':  # Location A is Dirty
            print("Location A is Dirty.")
            # Clean A
            goal_state['A'] = '0'
            cost += 1  # Cost for cleaning
            print("Cost for CLEANING A: " + str(cost))
            print("Location A has been Cleaned.")

            if status_input_complement == '1':  # If B is Dirty
                print("Location B is Dirty.")
                print("Moving right to Location B.")
                cost += 1  # Cost for moving right
                print("Cost for moving RIGHT: " + str(cost))
                # Clean B
                goal_state['B'] = '0'
                cost += 1  # Cost for cleaning
                print("Cost for CLEANING B: " + str(cost))
                print("Location B has been Cleaned.")
            else:
                print("Location B is already clean.")
        else:
            print("Location A is already clean.")

            if status_input_complement == '1':  # If B is Dirty
                print("Location B is Dirty.")
                print("Moving right to Location B.")
                cost += 1  # Cost for moving right
                print("Cost for moving RIGHT: " + str(cost))
                # Clean B
                goal_state['B'] = '0'
                cost += 1  # Cost for cleaning
                print("Cost for CLEANING B: " + str(cost))
                print("Location B has been Cleaned.")
            else:
                print("Location B is already clean.")

    else:  # Vacuum is placed in Location B
        print("Vacuum is placed in Location B")

        if status_input == '1':  # Location B is Dirty
            print("Location B is Dirty.")
            # Clean B
            goal_state['B'] = '0'
            cost += 1  # Cost for cleaning
            print("Cost for CLEANING B: " + str(cost))
            print("Location B has been Cleaned.")

            if status_input_complement == '1':  # If A is Dirty
                print("Location A is Dirty.")
                print("Moving left to Location A.")
                cost += 1  # Cost for moving left
                print("Cost for moving LEFT: " + str(cost))
                # Clean A
                goal_state['A'] = '0'
                cost += 1  # Cost for cleaning
                print("Cost for CLEANING A: " + str(cost))
                print("Location A has been Cleaned.")
            else:
                print("Location A is already clean.")
        else:
            print("Location B is already clean.")

            if status_input_complement == '1':  # If A is Dirty
                print("Location A is Dirty.")
                print("Moving left to Location A.")
                cost += 1  # Cost for moving left
                print("Cost for moving LEFT: " + str(cost))
                # Clean A
                goal_state['A'] = '0'
                cost += 1  # Cost for cleaning
                print("Cost for CLEANING A: " + str(cost))
                print("Location A has been Cleaned.")
            else:
                print("Location A is already clean.")

    # Done cleaning
    print("GOAL STATE: ")
    print(goal_state)
    print("Performance Measurement: " + str(cost))

# Call the function
vacuum_world()
