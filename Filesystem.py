# beginner
import os
import sys

class FileSystem:
    def play_again(self):
        while True:
            if input("do you want to perform more operations (yes/no)?").strip().lower()=="yes":
                self.welcome()
            else:
                print("Have a nice day!")
                break
    def welcome(self):
        print(f"{' '*30}Welcome to file system manager{' '*30}")
        print(f"{'-'*80}")
        print(f"""you can perform following operations:
         1. for creating a new file
         2. for reading content of file
         3. for writing content into file
         4. for deleting a file
         5. for listing all files in the current directory
         - to exit""")

        # keep choice as string so match-case patterns work as expected
        choice = input("Enter your choice: ").strip()

        match choice:
            case "1":
                filename = input("Enter file name to create (without extension): ").strip()
                extension_of_file = input("Enter extension of file (e.g. txt): ").strip()
                filefull = os.path.join(os.getcwd(), f"{filename}.{extension_of_file}" if extension_of_file else filename)
                return self.createfile(filefull)

            case "2":
                filename = input("Enter file name to read (with extension or path): ").strip()
                filenamef = os.path.join(os.getcwd(), filename) if not os.path.isabs(filename) else filename
                return self.readfile(filenamef)

            case "3":
                filename = input("Enter file name in which data to be written (without extension): ").strip()
                filenameextension = input("Enter file extension (e.g. txt): ").strip()
                filenamef = os.path.join(os.getcwd(), f"{filename}.{filenameextension}" if filenameextension else filename)
                return self.writedata(filenamef)

            case "4":
                filename = input("Enter file name to delete (with extension or path): ").strip()
                filenamef = os.path.join(os.getcwd(), filename) if not os.path.isabs(filename) else filename
                return self.deletefile(filenamef)

            case "5":
                directory = os.getcwd()
                return self.list_files(directory)

            case "-":
                print("Exiting.")
                sys.exit()

            case _:
                print("Invalid choice. Exiting.")
                return
        
        

    def createfile(self, filepath):
        try:
            # 'x' mode: create, fail if exists
            with open(filepath, 'x', encoding='utf-8') as f:
                print(f"File at {filepath} created successfully.")
            want_to_write = input("Do you want to write data into file now (yes/no)? ").strip().lower()
            if want_to_write == "yes":
                self.writedata(filepath)
        except FileExistsError:
            print("File already exists:", filepath)
            overwrite = input("Do you want to overwrite it? (yes/no): ").strip().lower()
            if overwrite == "yes":
                # open in write mode to overwrite
                self.writedata(filepath)
        except Exception as e:
            print("Error creating file:", e)
        self.play_again()

    def readfile(self, filename):
        try:
            if os.path.exists(filename):
                with open(filename, 'r', encoding='utf-8') as f:
                    content = f.read()
                    print("\n--- File content start ---")
                    print(content)
                    print("--- File content end ---\n")
            else:
                print("The specified file does not exist:", filename)
        except Exception as e:
            print("Error reading file:", e)
        self.play_again()

    def writedata(self, filename):
        try:
            # If given path does not exist, create parent directories
            parent = os.path.dirname(filename)
            if parent and not os.path.exists(parent):
                os.makedirs(parent, exist_ok=True)

            if os.path.exists(filename):
                print("file already exists:", filename)
                mis = input("Did you enter it by mistake? Enter 'yes' to provide a different name, or any other key to overwrite: ").strip().lower()
                if mis == "yes":
                    newname = input("Enter correct file name (with or without extension): ").strip()
                    newpath = os.path.join(os.getcwd(), newname) if not os.path.isabs(newname) else newname
                    return self.writedata(newpath)
                # otherwise continue to overwrite

            # Collect multi-line input until user types a sentinel line
            print("Enter content to be written. Type a single line containing __END__ to finish:")
            lines = []
            while True:
                line = input()
                if line == "__END__":
                    break
                lines.append(line)
            content = "\n".join(lines)

            # write whole content at once
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Wrote {len(content)} characters to {filename}")
        except Exception as e:
            print("Error writing file:", e)
        self.play_again()

    def deletefile(self, filename):
        try:
            if os.path.exists(filename):
                confirm = input(f"Are you sure you want to delete '{filename}'? (yes/no): ").strip().lower()
                if confirm == "yes":
                    os.remove(filename)
                    print("Deleted:", filename)
                else:
                    print("Delete cancelled.")
            else:
                print("File does not exist to delete:", filename)
        except Exception as e:
            print("Error deleting file:", e)
        self.play_again()

    def list_files(self, directory):
        try:
            list_of_files = os.listdir(directory)
            if not list_of_files:
                print("No files found in", directory)
                return
            for i in list_of_files:
                print(i, end=" ")
            print()  # newline after listing
        except Exception as e:
            print("Error listing files:", e)
        self.play_again()


if __name__ == "__main__":
    fs = FileSystem()
    fs.welcome()
