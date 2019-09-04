
# Navigating Operating Systems 

> ### Learning objectives
> 
> * Explain the difference between command line and GUI methods of interacting with computers
> * Explain when and why command-line interfaces should be used instead of graphical interfaces.
> * Explain how shell programs are used to interact with computers using a command line. 
> * Explain why Unix shells like Bash are pre-installed on Mac but not Windows computers. 
> * Discuss how using Unix shell is different on Mac and Windows OS. 
> * Practice first commands. 


## 1. What is an Operating System? 

An operating system (OS) is a suite of programs which make the computer work. It is a stable, multi-user, multi-tasking system for servers, desktops and laptops. Most personal computers use Mac, Windows, or Linux OS.


## 2. Human-Computer Interfaces

We navigate our operating systems and tell our computers to do things using human-computer interfaces. 

Most people interact with their computers using **Graphical User Interfaces (GUIs)**. A GUI (pronounced gooey) is a way of interacting with your computer through graphical icons and visual indicators, typically using a mouse. 

In this class, we will learn an older form of interacting with computers called **Command-line Interface (CLI)**. Unlike GUIs, CLI methods involve interacting with your computer through typing commands and do not rely on mouse input. 

The heart of CLI is a concept called the 'read-evaluate-print loop' (or REPL). Simply put, when the user types a command and then presses the enter (or return) key, the computer reads it, executes it, and prints its output. The user then types another command, and so on until the user logs off.

## 3. Why Use Command-line Interface

First, you will be using it at the beginning of every class.
* You will use two(ish) commands in the shell before every class to copy an updated version of the course materials onto your computer. 
* You will be expected to follow along and do in-class exercises using the files on GitHub. 
* The material for this class is not fixed. It will be updated periodically. 

Second, for certain tasks, it can make your life a lot easier. Examples include: 
* Resolving 'big data' challenges
	* Much faster to manipulate large text files (i.e. filter or split up csv files). 
	* Often the easiest way to interact with remote machines, including most cluster and cloud computing platforms. 
* Renaming and reorganizing files 
	* Especially important for projects that involve combining data from many different photo or text files. 
* Interfacing with GitHub 

William Shotts the author of *[The Linux Command Line](http://linuxcommand.org/tlcl.php)* summarized the promise and challenges of CLI when he stated,  
> graphical user interfaces make easy tasks easy, while command line interfaces make difficult tasks possible.


## 4. How to Use Command-line Interface

To use CLI, we use **(command line) shell** programs. The shell reads commands that you type into it, figures out what commands to run, and orders the computer to execute them. In other words, the shell works as an intermediary between the user and computer and facilitates the 'read-evaluate-print loop'. 

A brief aside reguarding vocabulary... 
* Its intermediary role is why the shell is called the shell -- it encloses the operating system in order to hide some of its complexity and make it simpler to interact with.
* In addition to shell and command line, you may also hear the term 'terminal' used to describe interacting with a computer through a command line. 

## 5. Bash 

Although there are many shell programs available, we will be focusing on **Bash**, which is the most common *Unix* shells. 

Bash stands for the Bourne Again Shell (so-called because it's derived from a shell written by Stephen Bourne --- this is what passes for wit among programmers). Bash is the default shell on most modern implementations of Unix, and in most packages that provide Unix-like tools for Windows.

Note that you may hear people refer to 'bash' as both a program and a language. This is because, like R, there is a program-specific language that has been developed for Bash. In other words, we can run bash commands using the bash program. 

### Why did we download a bash shell on Windows but not Mac computers? 

In this course, we will be using a Unix shell. Unix and Unix-like operating systems have this shell built-in. Mac OS (OSX) is a version of Unix. Similarly, Linux is Unix-like and also has the shell built-in. 

Windows was designed seperately from Unix. Thus, it does not have Bash built-in. This is one of many differences between Windows and Unix. 


## 6. Unix vs. Windows 

Unix has several fundamental differences compared with Windows:

* More rigorous security
* Extremely powerful command-line tools 
* Very stable
* Entirely different directory structure

For our purposes, most differences between Unix and Windows aren't relevant. 

One exception are the file structures. More information about Unix and the file structure can be found below. 

Practically, Windows users will need to change "\" to "/". 
* The Windows File Explorer seperates subdirectories and files using backslashes ("\"). 
* When you write file paths in the bash shell, use a frontslash ("/") to seperate subdirectories and files.  


## 7. Our First Commands

Getting used to a shell can be intimidating at first! Let's start by opening a new shell window and trying out a few basic commands. 

First, open a shell window:

```shell
$
```

The dollar sign is a **prompt**, which shows us that the shell is waiting for input; your shell may show something more elaborate.

### whoami

Now, type the command `whoami`, then press the Enter key (sometimes marked Return) to send the command to the shell.

The command's output is the ID of the current user, i.e., it shows us who the shell thinks we are:

```shell
$ whoami

oski
```

More specifically, when we type `whoami` the shell:

1.  finds a program called `whoami`,
2.  runs that program,
3.  displays that program's output, then
4.  displays a new prompt to tell us that it's ready for more commands.

### ping 

While `whoami` and other commands from today's lesson focus on the structure of our own operating systems, our operating systems rarely work in isolation. Often, we are relying on the Internet to communicate with others! You can visualize this sort of communication within your own shell by asking your computer to `ping` (based on the old term for submarine sonar) an IP address provided by Google (8.8.8.8); in effect, this will test whether your Internet (thanks Airbears2) is working. 

Type the following and hit enter: 

```shell
$ ping 8.8.8.8
```

> Note: Windows users may have to try a slightly different alternative:
> 
> ```shell
> $ ping -t 8.8.8.8
> ```

Your computer will begin continuously pinging this IP address and reporting back the "latency," or how long it took for the ping data packet to go to that IP address and back. If your Internet isn't working, it will instead report an error saying "No route to host." 

Ping runs continuously, so when we want it to stop, we have to manually tell the kernel to stop executing the ping command. We do this simply by typing ctrl+c. 

(Thanks [Paul Thissen](http://www.paulthissen.org/) for the suggestion!)

## 8. Warning

Usually, there are limited consequences for experimenting with the tools that we will cover in this class. The Bash Shell is an exception. You can mess up your computer if you aren't careful. 

In particular, be very careful when using the `rm()` command. This command removes files ("rm" is short for "remove"). 

> #### Deleting Is Forever
> 
> Unix doesn't have a trash bin: when we delete files, they are unhooked
> from the file system so that their storage space on disk can be
> recycled. Tools for finding and recovering deleted files do exist, but
> there's no guarantee they'll work in any particular situation, since the
> computer may recycle the file's disk space right away.



******************************************

## Additional Reference Information

### More Unix Background 

UNIX is an operating system which was first developed by AT & T employees at Bell Labs (1969-1971).  Bell Labs canceled the project (MULTICS) but was continued by the employees worked in a smaller scale. The new project was named UNICS (Uniplexed Information and Computation System) and then renamed UNIX. Due to [the anti-trust issue](https://en.wikipedia.org/wiki/Breakup_of_the_Bell_System), AT & T gave away UNIX in 1975. Berkeley is one of the main places where UNIX was developed. [The Berkeley Software Distribution](https://en.wikipedia.org/wiki/Berkeley_Software_Distribution), one of the branches of UNIX, came out it 1977.

From Mac OS X to Linux, many of current operation systems are some versions of UNIX. 

For more information on the history of UNIX, see [this link](https://docs.google.com/presentation/d/1kKt9V6rom55hU6SJ2_3nGluobjtScptlnJV9YFe6Jz4/pub?start=false&loop=false&delayms=3000&slide=id.g163c5ae2ce_0_17).

![Unix history](https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/Unix_history-simple.svg/1200px-Unix_history-simple.svg.png)

### Key Components of Unix 

(Adapted from [Indiana University](https://kb.iu.edu/d/agat))

Unix has three main components

#### Kernel

The kernel of UNIX is the hub of the operating system: it allocates time and memory to programs and handles the [filestore](http://users.ox.ac.uk/~martinw/unix/chap3.html) (e.g., files and directories) and communications in response to system calls. 

#### Shell

The shell is an interactive program that provides an interface between the user and the kernel. The shell interprets commands entered by the user or supplied by a shell script, and passes them to the kernel for execution. 

As an illustration of the way that the shell and the kernel work together, suppose a user types `rm myfile` (which has the effect of removing the file *myfile*). The shell searches the filestore for the file containing the program `rm`, and then requests the kernel, through system calls, to execute the program `rm` on *myfile*. When the process `rm myfile` has finished running, the shell then returns the UNIX prompt % to the user, indicating that it is waiting for further commands.

We'll talk more about shells in a little bit.

#### File system

Unix and Unix-like operating systems employ a hierarchical (i.e., inverted tree) directory structure, with the root directory (/) at the top. 

The standard file system has, among others, the following directories:

| Directory | Description |
| --------- | ----------- |
| /  | The root directory, where the whole tree starts |
| /bin  | Contains fundamental executables (i.e., binaries) generally used by all users on the system (e.g., chmod, cp, mv, grep, and tar) |
| /etc | Contains local configuration files, subdirectories containing configuration files for large software packages (e.g., the X11 window system) |
| /lib  | Contains shared libraries needed to boot the system and run the commands in the root file system |
| /tmp  | Local scratch space for storing temporary files, which may be deleted without notice |
| /usr/bin | The primary directory for most executables used by normal users on the system (e.g., emacs, make, scp, sftp, ssh, and yum) |
| usr/lib |Contains static and dynamic libraries, a few executables that usually are not invoked directly, and subdirectories for complex program |














