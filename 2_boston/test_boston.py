'''
    CS5001
    Spring 2020
    Homework: boston.py, boston_driver.py, test_boston.py
    Danielle Tolliver

'''

from boston_driver import *


#Test Coordinates 1: Fenway (from Homework)
TEST_LAT_1 = 42.3466803
TEST_LONG_1 = -71.0994118

#Test Coordinates 2: Reflecting Pool
TEST_LAT_2 = 42.3408855
TEST_LONG_2 = -71.0894753

#Test Coordinates 3: White Hall
TEST_LAT_3 = 42.3399015
TEST_LONG_3 = -71.0999822


def test_draw_rainbow():
   '''
   Function draw_rainbow_circle
   Parameters: nothing; the magic is in the function
   Returns: nothing; but should see 6 color circle like a rainbow
   '''   
   #TEST 1 - Rainbow test to draw circle
   draw_circle("purple", 30)
   draw_circle("blue", 25)
   draw_circle("green", 20)
   draw_circle("yellow", 15)
   draw_circle("orange", 10)
   draw_circle("red", 5)


def test_move_turtle():
   '''
   Function draw_rainbow_circle
   Parameters: nothing; the magic is in the function
   Returns: nothing; but should see the turtle move and then writing appear
   '''
   #TEST 2 - Use the new x, y coordinates to move the turtle and add words
   move_turtle(TEST_LAT_1, TEST_LONG_1)
   write_at_location("Spencer", "0.5")

   move_turtle(TEST_LAT_2, TEST_LONG_2)
   write_at_location("Maribelle", "54.3")

   move_turtle(TEST_LAT_3, TEST_LONG_3)
   write_at_location("Freddy", "3.14")


def test_new_coord():
   '''
   Function test_new_coord
   Parameters: nothing; function uses the CONSTANT variables (floats)
   Returns: calls calc_x, calc_y and distance function and prints
   actual vs expected results
   '''
   
   #New coordinates: Fenway (from Homework)
   x_expected = "-39"
   x_actual = calc_x(TEST_LAT_1, TEST_LONG_1)
   y_expected = "90"
   y_actual = calc_y(TEST_LAT_1, TEST_LONG_1)
   distance_expected = "0.894"
   distance_actual = calc_distance(TEST_LAT_1, TEST_LONG_1)

   print("X expected: ", x_expected, "\n",
          "X actual: ", x_actual, "\n",
          "Y expected: ", y_expected, "\n",
          "Y actual: ", y_actual, "\n",
          "Distance expected: ", distance_expected, "\n",
          "Distance actual: ", distance_actual, "\n", sep="")

   #New coordinates: Reflecting Pool   
   x_expected = "41"
   x_actual = calc_x(TEST_LAT_2, TEST_LONG_2)
   y_expected = "25"
   y_actual = calc_y(TEST_LAT_2, TEST_LONG_2)
   distance_expected = "0.258"
   distance_actual = calc_distance(TEST_LAT_2, TEST_LONG_2)

   print("X expected: ", x_expected, "\n",
          "X actual: ", x_actual, "\n",
          "Y expected: ", y_expected, "\n",
          "Y actual: ", y_actual, "\n",
          "Distance expected: ", distance_expected, "\n",
          "Distance actual: ", distance_actual, "\n", sep="")

   #New Coordinates: White Hall
   x_expected = "-44"
   x_actual = calc_x(TEST_LAT_3, TEST_LONG_3)
   y_expected = "14"
   y_actual = calc_y(TEST_LAT_3, TEST_LONG_3)
   distance_expected = "0.152"
   distance_actual = calc_distance(TEST_LAT_3, TEST_LONG_3)

   print("X expected: ", x_expected, "\n",
          "X actual: ", x_actual, "\n",
          "Y expected: ", y_expected, "\n",
          "Y actual: ", y_actual, "\n",
          "Distance expected: ", distance_expected, "\n",
          "Distance actual: ", distance_actual, "\n", sep="")


def main():
   
   test_draw_rainbow()
   test_move_turtle()
   test_new_coord()

main()
