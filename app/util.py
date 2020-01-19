import pandas as pd

def compress_word_list(word_list):
    #print(word_list)
    i = 0
    while i < len(word_list):
        if len(word_list[i]) <=1 :
            del word_list[i]
        if i>=1 and word_list[i][0]=="(":
            word_list[i-1]+=" "+word_list[i]
            del word_list[i]
        else:
            i+=1
    #print(word_list)
    return word_list

def list_seperation_logic(word_list,n,alteration_list,rearrangement_list,conf):
    #print("*"*10,n,word_list)
    
    #conf.alteration_tag,rearrangement_tag
    if list !=type(word_list):
        return []    
    if(n>1 and conf.alteration_tag):
        alteration_list.extend(word_list)
    if(n>1 and conf.rearrangement_tag):
        rearrangement_list.extend(word_list)
    if "ALTERATIONS" in list(map(str.upper,word_list)):
        conf.alteration_tag = True
    if n==1 and conf.rearrangement_tag:
        conf.rearrangement_tag =  False 
    if "REARRANGEMENTS" in list(map(str.upper,word_list)):
        conf.alteration_tag = False
        conf.rearrangement_tag = True
    #print(alteration_tag,rearrangement_tag)

def get_csv_report(alteration_list,rearrangement_list,output_file="output.csv"):
    series = pd.Series(["","Gene Assayed"]+alteration_list+["","Genes tested for rearrangement"]+rearrangement_list)
    data = pd.DataFrame({"Gene Reposrt List":series})
    data.to_csv(output_file,index=None)
    print("{0} file created".format(output_file))
      