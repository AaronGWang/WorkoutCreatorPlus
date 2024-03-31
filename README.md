# WorkoutCreatorPlus
This repo includes a script (main.py) that can generate a upper/lower split workout schedule. The script can be ran once before every workout session to generate a workout plan. 


## General Schedule Format
Two types of sessions:
- Upper Split: 
  * This workout is seperated in two parts, 45min for the `main set`, and 15min for the `core set`.
  * The main set includes most areas of the upper body `(biceps, triceps, back, shoulders, chest)`.
  * The core set includes most areas of the core `(Abs, Obliques, Lower Back)`

- Lower Split:
  * This workout is seperated in two parts, 45min for the `main set`, and 15min for the `core set`.
  * The main set includes most areas of the upper body `(quads, calves, glutes, hamstrings, compound)`.
  * The core set includes most areas of the core `(Abs, Obliques, Lower Back)`


## Upper Split
The upper split is a upper body session that takes around 45 minutes to complete.

This session has `6 exercises` and should be completed for `3-4 sets`.

There will always be a compound exercise during every upper split session. This exercise involves multiple muscle groups.

An unshuffled upper split will always have the order `[biceps, triceps, back, shoulders, chest, compound]`. A shuffled upper split will have a random order.


## Lower Split
The lower split is a lower body session that takes around 45 minutes to complete.

This session has `5 exercises` and should be completed for `3-4 sets`.

There will always be a compound exercise during every lower split session. This exercise involves multiple muscle groups.

An unshuffled upper split will always have the order `[quands, calves, glutes, hamstrings, compound]`. A shuffled upper split will have a random order.


## Core Split
The core split is a core and stability session that takes around 15 minutes to complete. This sessio nis incorperated into every workout session, paired with either a upper or lower split.

This session has `4 exercises` and should be completed for `2 sets`.

There will always be a balance exercise during every core split session. This exercise is paired with lower back most of the time.

An core split will always have the order `[abs, obliques, abs, lower back & balance]`. There is no option to shuffle a core split, and is not needed in the first place.

The intensity of a core split will alternate between each exercise.


## main.py Info
The main.py script is meant to be ran in the command line. 

Parameters:
1. split_type, must be `upper` or `lower`
2. shuffle, must be `yes` or `no`. Only works on the main set and defaults to `yes`. This means you `don't have to` include it in the command.
3. main_set_instructions, must be `yes` or `no`. Includes instructions for exercises in the main set and defaults to `no`. This means you `don't have to` include it in the command.
4. core_set_instructions, must be `yes` or `no`. Includes instructions for exercises in the core set and defaults to `no`. This means you `don't have to` include it in the command.

Example Commands:
1. `python3 main.py upper` (generates a shuffled upper split without any instructions)
2. `python3 main.py upper yes yes yes` (generates a shuffled upper split with all instructions)
3. `python3 main.py upper no yes no` (generates a unshuffled upper split with only main set instructions)