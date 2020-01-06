filename = input()

a = list(filename.split("."))

a[1] = '.' + a[1] #for printing the extension as .py or .txt etc

print(a[1])