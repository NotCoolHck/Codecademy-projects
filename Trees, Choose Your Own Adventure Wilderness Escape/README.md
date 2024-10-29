# Wilderness Escape - Choose Your Own Adventure

An interactive, text-based adventure where players navigate a wilderness scenario by making choices. This project demonstrates the use of a tree data structure to manage story progression and branching paths.

## Steps to Complete

### Our Story Begins
1. Print "Once upon a time…" to start the story.
2. Save and run the script to check that the print statement works.
3. Define a `TreeNode` class to represent each part of the story.
4. Inside `TreeNode`, add an `__init__()` method that takes `story_piece` as an argument.
5. In `__init__()`, set `self.story_piece` and initialize `self.choices` as an empty list.
6. Create `story_root`, an instance of `TreeNode` with the first part of the story.

7. Print `story_root.story_piece` to confirm it works.
8. Prompt the user to enter their name with `input("What is your name? ")`.
9. Print the user’s name after they enter it.
10. Run the script to test the input functionality.
11. Comment out or remove lines related to the user’s name.

### Adding Chapters
12. Define an `.add_child()` method within `TreeNode` to add story choices.
13. Store the argument passed to `.add_child()` inside `self.choices`.
14. Create `choice_a`, an instance of `TreeNode` with a new story section.
15. Create `choice_b`, another instance of `TreeNode` with a different story section.
16. Add `choice_a` as a child of `story_root` using `.add_child()`.
17. Add `choice_b` as another child of `story_root`.
18. Now `story_root` has two choices, `choice_a` and `choice_b`.

### Our Story So Far
19. Add a `.traverse()` method in `TreeNode` to progress through the story.
20. Inside `.traverse()`, declare `story_node` to track the current part of the story.
21. Print `story_node.story_piece`.
22. In `.traverse()`, create a loop that continues while `story_node.choices` is not empty.
23. Set up a `while` loop to run if `story_node.choices` is not empty.
24. Inside the loop, prompt the user to enter a choice with `"Enter 1 or 2 to continue the story: "`.
25. If the choice isn’t valid, print an error message and ask the user to try again.
26. Convert the user’s choice to an integer to use it as an index.
27. Adjust `chosen_index` to be one less than the user’s choice.
28. Assign `chosen_child` to the correct choice using `chosen_index`.
29. Print `chosen_child.story_piece` to display the next part of the story.
30. Set `story_node` to `chosen_child` to update the current story part.

31. Call `.traverse()` on `story_root` to test the flow of the story.

### The Final Chapter
32. Create `choice_a_1`, a new node with a conclusion for `choice_a`.
33. Create `choice_a_2`, a different conclusion for `choice_a`.
34. Add `choice_a_1` and `choice_a_2` as children of `choice_a` using `.add_child()`.
35. Test by running the script and following the choices for `choice_a`.

36. Create `choice_b_1`, a new node with a conclusion for `choice_b`.
37. Create `choice_b_2`, a different conclusion for `choice_b`.
38. Add `choice_b_1` and `choice_b_2` as children of `choice_b`.
39. Run the script to test the full story with all branches.

## Running the Game
To play, run:
```bash
python3 script.py



###This version includes each of the 39 steps in sequence, detailing the entire development process for the adventure game.###
