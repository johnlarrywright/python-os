#1. Open the filenames.txt file with read-only access with the open() function
file_obj = open('filenames.txt', 'r')
print(file_obj)
file_obj.close()
#2. Print the name of the file and if it is open or closed using the .name and .closed properties
print(file_obj.name)
print(file_obj.closed)
#3. Use a for loop to read all lines of filenames.txt into a list variable
lines = []
file_obj = open('filenames.txt', 'r')
for line in file_obj:
    lines.append(line)
print(lines)

#4. Print out all the lines from the file from your variable

#5. Close the filenames.txt file and print if the file is open or closed
file_obj.close()
print(file_obj.closed)

#6. Create a file using the open() function called secrets.txt

file_name = open('secrets.txt', 'w+')

#7. Write your own secrets to the file with the write() function
file_name = open('secrets.txt', 'w+')
file_name.write('I do uber')

#8. Close the secrets.txt file using the close() method. DON'T FORGET!
file_name.close()
#9. Print out the contents of the text file in your terminal to prove it worked
file_name = open('secrets.txt', 'r')
print(file_name.read())
#10. Open your secrets.txt file in append mode and write some more super secret info

#11. Close the secrets.txt file again using the close() function

#12. Rename the secrets.txt and make it a "hidden" file named .supersecret.txt using the os.rename() function

#13. See if you can see the file in your file explorer

#14. Create a list variable named file_names that contains a list of filenames

#15. Use the writelines() function to append the filenames to the filenames.txt file

#16. Delete the initial secrets.txt file now that you have a super secret hidden version

#17. BOSS LEVEL: Use the input() function to accept user input of a filename to create and create that file.
