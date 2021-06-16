import csv
import time
import re
import sys

total_memory_used = 0
start = time.time()
total_memory_used += sys.getsizeof(start)
with open('french_dictionary.csv') as csvfile:
    reader = csv.reader(csvfile)
    mydict = {rows[0]:rows[1] for rows in reader}
    with open("t8.shakespeare.txt") as file1:
        file_text = file1.read()
        x = file_text.split(' ')
        freq = {}
        y = []
        for word in x:
            if(len(word)==0 or word==' '):
                continue            
            two_words = word.split('\n')

            if(len(two_words) > 1):                
                ext_word = two_words.copy()
                ext_word[0] = re.sub(r'[^\w\s_.-@~]', "", ext_word[0])
                pre_split_word = two_words.copy()
                if(len(ext_word[0])==0 or ext_word[0]==' '):
                    continue
                temp0 = ext_word[0]
                if(ext_word[0].isupper()):
                    z = mydict.get(ext_word[0].lower(),-1)
                    if(z!=-1):
                        freq[ext_word[0].lower()] = freq.get(ext_word[0].lower, [z.lower(),0])
                        freq[ext_word[0].lower()][1] += 1
                        ext_word[0] = z.upper()
                elif(ext_word[0][0].isupper()):
                    z = mydict.get(ext_word[0].lower(),-1)
                    if(z!=-1):
                        freq[ext_word[0].lower()] = freq.get(ext_word[0].lower(),[z.lower(),0])          
                        freq[ext_word[0].lower()][1] += 1
                        ext_word[0] = z.capitalize() 
                else:
                    z = mydict.get(ext_word[0].lower(),-1)
                    if(z!=-1):
                        freq[ext_word[0].lower()] = freq.get(ext_word[0].lower(),[z.lower(),0])
                        freq[ext_word[0].lower()][1] += 1
                        ext_word[0] = z
                inmatch = 0
                while(pre_split_word[0][inmatch] != temp0[0]):
                    inmatch += 1
                two_words[0] = pre_split_word[0][:inmatch] + ext_word[0] + pre_split_word[0][len(temp0)+inmatch:]


                if(len(two_words)>2):
                    idx = 1
                    while(idx < len(two_words)-1):
                        ext_word[idx] = re.sub(r'[^\w\s_.-@~]', "", ext_word[idx])
                        if(len(ext_word[idx])==0 or ext_word[idx]==' '):
                            idx+=1
                            continue
                        tempbt = ext_word[idx]
                        if(ext_word[idx].isupper()):
                            z = mydict.get(ext_word[idx].lower(),-1)
                            if(z!=-1):
                                freq[ext_word[idx].lower()] = freq.get(ext_word[idx].lower(),[z.lower(),0])
                                freq[ext_word[idx].lower()][1] += 1
                                ext_word[idx] = z.upper()
                        elif(ext_word[idx][0].isupper()):
                            z = mydict.get(ext_word[idx].lower(),-1)
                            if(z!=-1):
                                freq[ext_word[idx].lower()] = freq.get(ext_word[idx].lower(),[z.lower(),0])    
                                freq[ext_word[idx].lower()][1] += 1
                                ext_word[idx] = z.capitalize()     
                        else:
                            z = mydict.get(ext_word[idx].lower(),-1)
                            if(z!=-1):
                                freq[ext_word[idx].lower()] = freq.get(ext_word[idx].lower(),[z.lower(),0])
                                freq[ext_word[idx].lower()][1] += 1
                                ext_word[idx] = z
                        inmatch = 0
                        while(pre_split_word[idx][inmatch] != tempbt[0]):
                            inmatch += 1
                        two_words[idx] = pre_split_word[idx][:inmatch] + ext_word[idx] + pre_split_word[idx][len(tempbt)+inmatch:]
                        idx+=1

                ext_word[-1] = re.sub(r'[^\w\s_.-@~]', "", ext_word[-1])
                if(len(ext_word[-1])==0 or ext_word[-1]==' '):
                    continue
                temp1 = ext_word[-1]
                if(ext_word[-1].isupper()):
                    z = mydict.get(ext_word[-1].lower(),-1)
                    if(z!=-1):
                        freq[ext_word[-1].lower()] = freq.get(ext_word[-1].lower(),[z.lower(),0])
                        freq[ext_word[-1].lower()][1] += 1
                        ext_word[-1] = z.upper()
                elif(ext_word[-1][0].isupper()):
                    z = mydict.get(ext_word[-1].lower(),-1)
                    if(z!=-1):
                        freq[ext_word[-1].lower()] = freq.get(ext_word[-1].lower(),[z.lower(),0])        
                        freq[ext_word[-1].lower()][1] += 1
                        ext_word[-1] = z.capitalize()    
                else:
                    z = mydict.get(ext_word[-1].lower(),-1)
                    if(z!=-1):
                        freq[ext_word[-1].lower()] = freq.get(ext_word[-1].lower(),[z.lower(),0])
                        freq[ext_word[-1].lower()][1] += 1
                        ext_word[-1] = z
                inmatch = 0
                while(pre_split_word[-1][inmatch] != temp1[0]):
                    inmatch += 1
                two_words[-1] = pre_split_word[-1][:inmatch] + ext_word[-1] + pre_split_word[-1][len(temp1)+inmatch:]

                word = '\n'.join(two_words)                

            else:
                ext_word = re.sub(r'[^\w\s_.-@~]', "", word)
                if(len(ext_word)==0 or ext_word==' '):
                    continue
                temp = ext_word
                if(ext_word.isupper()):
                    z = mydict.get(ext_word.lower(),-1)
                    if(z!=-1):
                        freq[ext_word.lower()] = freq.get(ext_word.lower(),[z.lower(),0])
                        freq[ext_word.lower()][1] += 1
                        ext_word = z.upper()
                elif(ext_word[0].isupper()):
                    z = mydict.get(ext_word.lower(),-1)
                    if(z!=-1):
                        freq[ext_word.lower()] = freq.get(ext_word.lower(),[z.lower(),0])           
                        freq[ext_word.lower()][1] += 1
                        ext_word = z.capitalize()
                else:
                    z = mydict.get(ext_word.lower(),-1)
                    if(z!=-1):
                        freq[ext_word.lower()] = freq.get(ext_word.lower(),[z.lower(),0])
                        freq[ext_word.lower()][1] += 1
                        ext_word = z
                inmatch = 0
                while(word[inmatch] != temp[0]):
                    inmatch += 1
                word = word[:inmatch] + ext_word + word[len(temp)+inmatch:]
            
            y.append(word)


        y = ' '.join(y)
        outF = open("t8.shakespeare.translated.txt", "w")
        outF.write(y)
        outF.close()

        foutF = open("frequency.csv", "w")
        for i in sorted (freq.keys()) : 
            foutF.write(i)
            foutF.write(',')
            foutF.write(str(freq[i][0]))
            foutF.write(',')
            foutF.write(str(freq[i][1]))
            foutF.write('\n')
        foutF.close()

    total_memory_used += sys.getsizeof(reader)
    total_memory_used += sys.getsizeof(mydict)
    total_memory_used += sys.getsizeof(file_text)
    total_memory_used += sys.getsizeof(x)
    total_memory_used += sys.getsizeof(freq)
    total_memory_used += sys.getsizeof(y)

    end = time.time()
    poutF = open("performance.txt", "w")
    poutF.write("Time to process: "+str(end-start)+' seconds\n')
    poutF.write("Memory used: "+str(total_memory_used / 1000000 )+' MB\n')
    poutF.close()

print("The files have been created..")
