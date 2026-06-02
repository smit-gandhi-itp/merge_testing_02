# merge_testing_02

## C++ Hello World Program

This repository contains a simple C++ "Hello World" program.

### Files
- `hello_world.cpp` - The main C++ source file
- `Makefile` - Build configuration for compiling the program

### Building and Running

#### Prerequisites
- g++ compiler (or any C++ compiler)
- make (optional, for using the Makefile)

#### Using Make
```bash
# Compile the program
make

# Run the program
make run

# Clean build artifacts
make clean
```

#### Manual Compilation
```bash
# Compile
g++ -Wall -Wextra -std=c++17 -o hello_world hello_world.cpp

# Run
./hello_world
```

### Expected Output
```
Hello, World!
```
