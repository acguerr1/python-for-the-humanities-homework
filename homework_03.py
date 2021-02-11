#This assignment should be submitted as standalone Python script. Please put the code for this assignment in a dedicated file (not into this notebook) and run it from the command line. Add, commit, and push that file to your homework branch of your GitHub repo.
#Start out by creating a virtual environment. Activate it. Then install example-lfuncs into it.
#Now create a Python file and put your code into it. Create a string variable that holds the first paragraph of a Wikipedia article of your choice. Now, turn that string into a list of words (you can use the string method split() to split the string at for example blanks.
#Now, create a loop that asks the user for what he wants to do. Give them the following options:
#Find all the words that start with a specific prefix. The user can enter a prefix and the program finds all the words in the paragraph that start with that prefix and prints them.
#Let the program count how often each words appears in the paragraph.
#Each option should be in its own function that you call from the main loop. The user should enter "exit" to end the program.

flamingo=("flamingos or flamingoes are a type of wading bird in the family phoenicopteridae, the only bird family in the order phoenicopteriformes. four flamingo species are distributed throughout the americas, including the caribbean, and two species are native to africa, asia, and europe.")
seperation=list(flamingo.split())
prefix = ()
final_prefix_list=[]
final_word_count_list=[]

def prefixing(prefix):
    res = [i for i in seperation if prefix in i]
    final_prefix_list.append(res)
    print(final_prefix_list)

def word_count(word):
    if word in seperation:
        print(word + " is in list " + str(seperation.count(word)) + " time(s)!")

task=input("Do you want to (A) find all the words that start with a specific prefix, (B) figure out how many times a certain word is in the paragraph, or -exit-?")

while True:
    if task == "A":
        prefix=input("what is the prefix?: ")
        prefixing(prefix)
        task=input("Do you want to (A) find all the words that start with a specific prefix, (B) figure out how many times a certain word is in the paragraph, or -exit-?")
    if task == "B":
        word=input("what word would you like to count?: ")
        word_count(word)
        task=input("Do you want to (A) find all the words that start with a specific prefix, (B) figure out how many times a certain word is in the paragraph, or -exit-?")
    if task == "C":
        print("Bis spater!")
        break