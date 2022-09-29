# Project 02: Building Ethical and Aggressive Robots

## Timeline

Activity                   | Deadline
-------------------------- | ------------------------------
`pyparrot` set up and demo | September 29th, 2022 at 4:20pm
Project Walkthrough:       | October 6th, 2022 during lab
Demo and Final Submission: | October 13th, 2022 by 2:30pm

## Class Community Guidelines

Throughout the completion of this project you must adhere to the [community guidelines](https://github.com/CMPSC-311-Allegheny-College-Fall-2022/course-information/blob/main/community_guidelines.md) that we developed as a class. To report any violations of the code of conduct, please submit an [anonymous form](https://forms.gle/tePfnLY12hyN1Xbd6). Students who think that the class should revise some aspect of the guidelines must use the GitHub issue tracker for that repository to suggest, discuss, and implement any required changes.

By working on and completing this assignment you agree to use the hardware given to you in a responsible manner. Each team is responsible for the safety and security of the robot while it is in your possession. You are allowed to take the robots used in this project outside of ALIC but you have to return all parts at the completion of this project, or if requested, at the end of the semester.

### Drone Safety

Drones can be dangerous and cause injury! Additionally, Bebop drones are notoriously hard to catch. You must obey the following safety rules:

- No flying inside the buildings unless it is in the Wise Center.
- No flying over or near anyone.
- Must fly in the flying zone (Wise Center's blue courts or public property outside).
- Use hull protection for Bebop 1 or 3D print propeller guards for Bebop 2 (the 3D printing files are provided in the lab repository).
- Use safety glasses (available in ALIC) if you are operating in the close proximity of the flying drone, especially if flying it without hull or propeller protection.
- If you are not wearing glasses, do NOT put your eyes near the propellers.
- If you decide to test your drone outside, make sure to do so outside of campus, remember flying drones on Allegheny campus is not allowed! Also, be sure to obey the [FAA flying restrictions](https://www.faa.gov/uas/recreational_fliers/where_can_i_fly/).
- Do NOT connect to drone's wifi of another team -- this is dangerous.

## Introduction

This project assignment invites you to work in a team to implement a behavior-based navigation technique for an autonomous aerial vehicle for an application of your choice. First, you will familiarize yourselves with the new robotic platform, Parrot BEBOP, and will complete the necessary installations and set up using `pyparrot` Python Interface for Parrot drones. Then, you will learn how to use `pyparrot` interface to program autonomous flying of the robot. Finally, teams will implement a navigation technique for a specific application and will reflect on the ethical considerations of the developed navigation strategy. Teams are also responsible for writing a detailed report, stored in the file `writing/report.md`. This is a Markdown file that must adhere to the standards described in the [Markdown Syntax Guide](https://guides.github.com/features/mastering-markdown/).

## Learning

To learn about `pyparrot` interface please read the [`pyparrot` documentation](https://pyparrot.readthedocs.io/en/latest/bebopcommands.html). To learn more about autonomous drones please read the article titled [The Future of Flight: AI in the Cockpit](https://www.wsj.com/articles/the-future-of-flight-ai-in-the-cockpit-1542018600).

## Instructions

### 1\. Set Up

- Review the [Tutorial 1 (Set Up)](https://www.parrot.com/us/support/products/parrot-bebop-2/preparing-your-drone). Download the app called "FreeFlight Pro", upgrade the firmware if needed and perform the calibrations (roll, pitch, yaw). Now, without flying it, ensure that you are able to connect your drone (wifi works) and that you can see the camera's input on the app.

- In this project, you will not operate the drone via the "FreeFlight Pro app. Instead, you will program it using `pyparrot` interface, which will allow you to write code in Python to have the drone move automatically. If you have not already installed `pyparrot` and its dependent software, please complete the needed installations following the instructions in the [pyparrot Installation Guide](https://pyparrot.readthedocs.io/en/latest/installation.html)

Please note that you may need to use pip3 to complete installations that are compatible with Python3\. Be sure to install `pyparrot` from `pip` using `pip3 install pyparrot` command so that you do not need to clone the `pyparrot` repository and store it in your lab repository. In order to connect to the camera you should install `ffmpeg` (on the Mac, you can use `brew install ffmpeg` command) and `opencv`. If you find the need to utilize the `demoBebopVisionGUI.py` example of `pyparrot`, you will also need to install [VLC](https://www.videolan.org/vlc/index.html) and `PyQt5` (on the Mac, you can use `brew install pyqt5` command).

Also, please remember that you can't control your drone from the Allegheny's wifi. You MUST be connected to YOUR drone's wifi.

### `pyparrot` Notes

To get started with `pyparrot`, you should first try to run `demo.py` program first, uncommenting each movement one by one.

Also, when starting your program in Python3 using `pyparrot`, please remember to specify the correct Bebop type. If you are using smaller (blue or red) Bebop drones (these are Bebop 1s), then you have to specify that when creating a Bebop object as `bebop = Bebop(drone_type="Bebop")` since the default Bebop type is Bebop 2 (white Bebop drones). Also, if you are using hull protectors in Bebop 1 you should use the `set_hull_protection` method, where the hull protector parameters is set to 1 for a hull protection being in place on Bebop 1\. You are free to use and extend any of the programs in the `examples/` directory of the `pyparrot` repository.

Also, if you have trouble connecting the drone to wifi, you may need to revert to an earlier `zeroconf` version, for example by running `pip3 install zeroconf==0.20.0`.

You can use `move_relative` method to fly the drone a relative number of meters as specified in [`bebop` commands doc](https://pyparrot.readthedocs.io/en/latest/bebopcommands.html). If you would like to estimate the distance and use `fly_direct` method, you can use the distance formula.

### 2\. 3D Printed Parts

To enhance the safety of the Bebop drones and/or to enhance your developed implementation (described below) each team should use 3D printed propeller guards (or for Bebop 1 manufacture provided hull protectors). If your Bebop 2 does not have propeller guards, you may want to print them yourself using Ultimaker 3 printer located in ALIC. You should be able to use an existing model (provided by the instructor or found online), slice it and print it. Please note that the leg parts (the plate and the leg) take about 1.5 hours to print each and the propeller needs about 7 hours to print. Therefore, pre-planned use of the printer is required. To accommodate with printer scheduling, each team will be required to specify its desired printer use day/time in their planning portion of the report and to further communicate it with class using Discord.

To begin the printing process, you should download [Ultimaker Cura](https://ultimaker.com/software/ultimaker-cura). Then, open your 3D printing file in Cura, click on "Slice", click on "File", "Export" and save your file in a USB drive as a `.gcode` file. Now go to the Ultimaker 3D printer, turn it on, make sure there is enough material (grey), plug in your USB, select "Print" and begin the printing of your model.

## 3\. Navigation Task

The implementation task for this project is to develop a behavior-based navigation using a Bebop drone for a specific application. In delivery applications, drones often have to fly to a specific location, drop off a package, and fly off to another location, etc. You are to implement a similar functionality but since we are not using the GPS navigation functionality of Bebop (extra credit if you implement this functionality!), instead of specifying a particular location your drone will fly in a pre-defined pattern. Think of an engaging application and incorporate techniques for that application into your navigation procedure. For example, maybe you have an aerial show drone that will fly in a circle while doing flips, then it will land, and fly a square while doing back-flips. Again, this lab is open-ended to encourage creativity and exploration as long as you satisfy the hard requirements.

**Hard Requirements:**

- Take off, fly some distance in a pre-defined pattern, land. Do this at least twice.
- Use at least one loop and at least one conditional statement. User-defined input is welcome.
- Navigation must last at least one minute.
- Your drone should take at least five photos during each leg of the flight (from take off to landing) and record the video of its flight in its entirety.
- The program should collect the sensor data each time a sensor is updated and output it into a file.

## Project Walkthrough

During the lab session on Thursday, October 6th, each team will participate in the project walk-through process. Project walkthrough is an informal process where the instructor facilitates the process of reviewing the progress of the project and the written code. The purpose of this walkthrough is to motivate continuous progression on the project, identification of any conceptual issues, and detection of any technical errors. When the walkthrough is finished, the authors of the project are responsible for taking the necessary actions to correct the identified issues, if there are any.

By this project walkthrough, each team should have identified the navigation task they want their robot to complete, and have written and tested some code to accomplish this task. During the walkthrough, the team members will collaboratively lead the walkthrough process, which should last 5-10 minutes for each team. Each team should:

- Describe the chosen navigation task.
- Explain and demonstrate the written code.
- Identify the steps left to complete for this project.

## Project Demonstration

At the beginning of the lab session on Thursday, October 13th, each team will be given an opportunity to demonstrate their project. When the lab session starts, teams will be given a few minutes to set up their demonstrations and get them running. Then, class members will participate in an interactive demonstration session, where everyone will be able to view each demonstration.

## Assignment Assessment

The grade that a student receives on this assignment will have the following components.

- **GitHub Actions CI Build Status [up to 15%]:**: For lab01 repository associated with this assignment students will receive a checkmark grade if their last before-the-deadline build passes.

- **Mastery of Verbal Explanation during the Demonstration [up to 15%]:**: Since the continuous and timely project development and the ability to communicate technical details of a project is crucial to building successful software and hardware applications, a portion of students' lab grade will be determined based on the quality of the project walkthrough and the project demonstration.

- **Mastery of Technical Writing [up to 20%]:**: Students will also receive a checkmark grade when the responses to the writing questions presented in the `report.md` reveal a proficiency of both writing skills and technical knowledge. To receive a checkmark grade, the submitted writing should have correct spelling, grammar, and punctuation in addition to following the rules of Markdown and providing conceptually and technically accurate answers.

- **Mastery of Technical Knowledge and Skills [up to 50%]**: Students will receive a portion of their assignment grade when their project implementation reveals that they have mastered all of the technical knowledge and skills developed during the completion of this project. All programs must be inside `src/` directory. As a part of this grade, the instructor will assess aspects of the project including, but not limited to, the correctness of the program, the completeness and correctness of the software and hardware integration, the use of effective source code comments and Git commit messages.

All grades for this project will be reported through a student's gradebook GitHub repository.

## GatorGrade

You can check the baseline writing and commit requirements of this project by running department's assignment checking `gatorgrade` tool To use `gatorgrade`, you first need to make sure you have Python installed. If not, please see:

- [Setting Up Python on Windows](https://realpython.com/lessons/python-windows-setup/)
- [Python 3 Installation and Setup Guide](https://realpython.com/installing-python/)
- [How to Install Python 3 and Set Up a Local Programming Environment on Windows 10](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-windows-10)

Then, you need to install `gatorgrade`:

- First, [install `pipx`](https://pypa.github.io/pipx/installation/)
- Then, install `gatorgrade` with `pipx install gatorgrade`

Finally, you can run `gatorgrade`:

`gatorgrade --config config/gatorgrade.yml`

## Assistance

If you are having trouble completing any part of this project, then please talk with the course instructor during the laboratory session. Alternatively, you may ask questions in the Discord channel for this course. Finally, you can schedule a meeting during the course instructor's office hours.
