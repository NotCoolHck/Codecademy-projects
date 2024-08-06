# The Boredless Tourist

Welcome to **The Boredless Tourist**, an online application giving you the power to find the parts of the city that fit the pace of your life. We at The Boredless Tourist run a recommendation engine using Python. We first evaluate what a person’s interests are and then give them recommendations in their area to venues, restaurants, and historical destinations that we think they’ll be engaged by. Let’s get started!

If you get stuck during this project or would like to see an experienced developer work through it, click “Get Unstuck“ to see a project walkthrough video.

## Tasks

### Setting Up Your Project

1. **Initialize Git Repository**
   - Run `git init` in the terminal.

2. **Track script.py**
   - Add `script.py` to git’s staging area.

3. **Initial Commit**
   - Perform a git commit with the message "initial commit".

4. **Create Destinations List**
   - Create a list with the following destinations and save it into a variable called `destinations`:
     ```
     “Paris, France”
     “Shanghai, China”
     “Los Angeles, USA”
     “São Paulo, Brazil”
     “Cairo, Egypt”
     ```

5. **Create Test Traveler**
   - Create a `test_traveler` variable with the following list:
     ```
     ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]
     ```

6. **Commit Changes**
   - Save the file, then add `script.py` to the git index using `git add`.

7. **Commit Test Objects**
   - Perform a git commit with the message "Added test objects".

### Travelling To Faraway Lands

8. **Define get_destination_index Function**
   - Define a function called `get_destination_index(destination)`.

9. **Find Destination Index**
   - Find the index of `destination` and save it into `destination_index`.

10. **Return Destination Index**
    - Return `destination_index`.

11. **Test get_destination_index**
    - Call `get_destination_index("Los Angeles, USA")` and print the result.

12. **Test Paris Destination Index**
    - Call `get_destination_index("Paris, France")` and check if it returns 0.

13. **Test Non-existent Destination**
    - Call `get_destination_index("Hyderabad, India")` and observe the result.

14. **Handle ValueError**
    - Note the ValueError when calling with a non-existent destination. Do not add logic to avoid this error.

15. **Define get_traveler_location Function**
    - Define a function called `get_traveler_location(traveler)`.

16. **Retrieve Traveler Destination**
    - Save the traveler's destination string into `traveler_destination`.

17. **Get Traveler Destination Index**
    - Retrieve the index of the traveler’s destination and save it into `traveler_destination_index`.

18. **Return Traveler Destination Index**
    - Return `traveler_destination_index`.

19. **Test Traveler Location**
    - Create a variable `test_destination_index` and save the result of `get_traveler_location(test_traveler)`.

20. **Print Test Destination Index**
    - Print `test_destination_index`.

21. **Run and Verify**
    - Save your code and run it by calling `python3 script.py`. Verify if `test_destination_index` equals 1.

22. **Save Work**
    - Add `script.py` to the git index with `git add`.

23. **Commit Changes**
    - Commit your changes with the message "Added logic to find traveler destinations and convert to internal data".

### Visiting Interesting Places

24. **Create Attractions List**
    - Define a list called `attractions`.

25. **Initialize Attractions List**
    - Define `attractions` to be a list of 5 empty lists using a loop or list comprehension.

26. **Print Attractions**
    - Print `attractions` and verify it looks like `[[], [], [], [], []]`.

27. **Define add_attraction Function**
    - Define a function called `add_attraction(destination, attraction)`.

28. **Find Destination Index in add_attraction**
    - Use `get_destination_index(destination)` to retrieve the index of the destination and save it into `destination_index`.

29. **Skip Task**

30. **Skip Task**

31. **Find Attractions for Destination**
    - Use `destination_index` to find the appropriate list in `attractions` and save it to `attractions_for_destination`.

32. **Append Attraction**
    - Append `attraction` to `attractions_for_destination`.

33. **Add Venice Beach Attraction**
    - Call `add_attraction("Los Angeles, USA", ['Venice Beach', ['beach']])`.

34. **Print Attractions**
    - Print `attractions` and verify it looks like `[[], [], [['Venice Beach', ['beach']]], [], []]`.

35. **Add More Attractions**
    - Paste the following code to add more attractions:
      ```python
      add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
      add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
      add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historical site"]])
      add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
      add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
      add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
      add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
      add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
      add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
      add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])
      ```

36. **Save Changes**
    - Add `script.py` to the git index with `git add`.

37. **Commit Changes**
    - Commit with the message "Created attractions and functionality for adding new attractions".

### Finding the Best Places to Go

38. **Define find_attractions Function**
    - Define a function called `find_attractions(destination, interests)`.

39. **Retrieve Destination Index**
    - Save the destination’s index to `destination_index` using `get_destination_index(destination)`.

40. **Look Up Attractions in City**
    - Save the attractions in the city into `attractions_in_city`.

41. **Initialize Attractions with Interest List**
    - Create an empty list `attractions_with_interest`.

42. **Loop Through City Attractions**
    - Loop over `attractions_in_city` and save each item into `possible_attraction`.

43. **Retrieve Attraction Tags**
    - Save the attraction’s tags into `attraction_tags`.

44. **Loop Through Interests**
    - Loop through each interest in `interests`.

45. **Match Interests with Tags**
    - If an interest is in `attraction_tags`, append `possible_attraction` to `attractions_with_interest`.

46. **Return Attractions with Interest**
    - Return `attractions_with_interest`.

47. **Test find_attractions Function**
    - Call `find_attractions("Los Angeles, USA", ['art'])` and save the results to `la_arts`.

48. **Print la_arts**
    - Print `la_arts` and verify it returns `[['LACMA', ['art', 'museum']]]`.

49. **Append Only Attraction Names**
    - Append only `possible_attraction[0]` to `attractions_with_interest`.

50. **Rerun and Verify**
    - Rerun `la_arts` test code and verify it prints `['LACMA']`.

51. **Save Changes**
    - Add `script.py` to the git index with `git add`.

52. **Commit Changes**
    - Commit with the message "Added interest finder logic".

### See The Parts of a City You Want to See

53. **Define get_attractions_for_traveler Function**
    - Define a function called `get_attractions_for_traveler(traveler)`.

54. **Separate Traveler Data**
    - Save `traveler[1]` into `traveler_destination` and `traveler[2]` into `traveler_interests`.

55. **Call find_attractions**
    - Save the results of `find_attractions(traveler_destination, traveler_interests)` into `traveler_attractions`.

56. **Create Interests String**
    - Create an interests string starting with `"Hi "` and save it into `interests_string`.

57. **Add Traveler Name to Interests String**
    - Add the traveler’s name to `interests_string`.

58. **Add Location Information**
    - Add the string `", we think you'll like these places around "` and the place.

59. **Add Attraction Names**
    - Loop through `traveler_attractions` and concatenate each attraction to `interests_string`.

60. **Return Interests String**
    - Return `interests_string`.

61. **Test get_attractions_for_traveler Function**
    - Call `get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']])` and save the results to `smills_france`.

62. **Print smills_france**
    - Print `smills_france` and verify it returns `"Hi Dereck Smill, we think you'll like these places around Paris, France: the Arc de Triomphe"`.

63. **Save Changes**
    - Add `script.py` to the git index with `git add`.

64. **Commit Changes**
    - Commit with the message "Added function to generate message for traveler and present attractions they might be interested in."
