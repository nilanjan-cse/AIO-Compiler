#!/usr/bin/python
import subprocess
import os


class Compiler:

    # self.output = dict()
    def __init__(self, output):
        self.output = output

    def c(self, file):
        temp = "gcc "+file+" -o out1;./out1"
        s = subprocess.check_call(temp, shell=True)
        self.outputs(file, s)
        return 0

    def java(self, file):
        filename, __ = os.path.splitext(file)
        temp = "javac "+file+";java "+filename
        s = subprocess.check_output(temp, shell=True)
        self.outputs(file, s.decode("utf-8"))
        return 0

    def cpp(self, file):

        # data, temp = os.pipe()

        # write to STDIN as a byte object(covert string
        # to bytes with encoding utf8)
        # os.write(temp, bytes("5 10\n", "utf-8"));
        # os.close(temp)

        # store output of the program as a byte string in s
        temp = "g++ "+file+" -o out2;./out2"
        s = subprocess.check_output(temp, shell=True)

        # decode s to a normal string
        self.outputs(file, s.decode("utf-8"))
        return 0

    def outputs(self, filename, text):
        self.output = {filename: text}

    def check(self, path):
        count = 0
        for i in os.listdir(path):
            __, ext = os.path.splitext(i)
            count = count+1
            if ext == ".c":
                self.c(i)
            if ext == ".java":
                self.java(i)
            if ext == ".cpp":
                self.cpp(i)
        print("Done compiling and storing output. Found ",count," files")
        choice = input("Do you want to see the output(yes/no): ")
        if choice == "yes":
            self.show(i)
        if choice == "no":
            print("Thank you for using AIO Compiler.")

        return 0

    def show(self, filename):
        if filename in self.output:
            print(self.output[filename])
        else:
            print(filename," is not found in this directory.")

        return 0


if __name__ == "__main__":
    codefile = str(input("Enter path of code files: "))
    output=dict()
    otp = Compiler(output)
    otp.check(codefile)
