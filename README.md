# ISTA HW Grader

Autograder script for grading homework assignments for ISTA 130, 131, and 350. Place the `ista-hw` file on the PATH, make it executable, and run it through the terminal with the flag `-m` to build the filesystem and `-g` to run the autograder (needs to be provided separately). These commands run the other two Python scripts.

### Usage

It would make most sense to have a "Grading" directory. Place the `.zip` file of submissions from Brightspace in this directory and all the auxillary files required, such as the autograder and any external dependencies. Run `ista-hw -m` to build the filesystem, this makes a directory for each student with their homework submission, the autograder, and any dependencies.

Then run `ista-hw -g` to run the autograder for each student. The results of the autograder will show on the terminal.
