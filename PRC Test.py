import pandas as pd
import re
import os
import numpy
# # #

############################## Edit Gene Name#######################
# def extract_second_string(genename):
#      split_names = genename.split()
#      if len(split_names) >= 2:
#          second_string = split_names[1].replace('[\[\]\'\']', '').replace(',', '').strip()
#          return str(second_string)
#      else:
#          return str(genename)

# #normal['genename'] = normal['genename'].apply(extract_second_string)
# normal['genename'] = normal['genename'].apply(lambda x: re.sub(r'[^-\w\s]', '', x))
# normal.to_csv("Concat_Transcript_07-05.csv", sep=',')
import re

# def extract_second_string(genename):
#     if len(genename.split()) >= 2:
#         return genename.split()[1]
#     else:
#         return genename
#
# normal['new_genename'] = normal['genename'].apply(extract_second_string)
# normal['new_genename'] = normal['new_genename'].astype(str).apply(lambda x: re.sub(r'[^-\w\s]', '', x))
#
# normal.to_csv("Concat_Transcript_07-05.csv", sep=',')





############################ mergining the refFlat onto OMI ##############################
# normal = pd.read_csv("Test_AML_Variants.csv", sep= ',')
# os .chdir('/Users/omodo/PycharmProjects/pythonProject/Spring 2023/refFlat')
# refFlatfiles = os.listdir()
# #
# chrDF = pd.DataFrame(columns=["genename", "name", "chromosome", "strand", "txStart", "txEnd", "cdsStart", "cdsEnd", "exonCount", "exonStarts", "exonEnds"])
# for file in refFlatfiles:
#      chrDF1 = pd.read_csv(file, sep="\t", header=None, names=["genename", "name", "chromosome", "strand", "txStart", "txEnd", "cdsStart", "cdsEnd", "exonCount", "exonStarts", "exonEnds"])
#      chrDF = pd.concat([chrDF, chrDF1], axis=0)
# #
# new_normal = pd.merge(normal, chrDF[["genename", "chromosome", "strand", "txStart", "txEnd"]], how="left", on=["genename", "chromosome"])
# new_normal.to_csv("Test_Transcript_AML.csv", sep=',')
# # #
# # new_tumor = pd.merge(tumor,chrDF[["genename", "chromosome", "strand", "txStart", "txEnd"]],how="left", left_on=["chromosome","genename",], right_on=["chromosome", "genename", ])
# # new_tumor.to_csv("tumor_step2.csv", sep=',')

###################### Use only the unique genes to avoid double counting, isoforms present so i am taking the largest length of the same gene, strand, and chrom ##########################
# # # #
UN = pd.read_csv("Test_Transcript_AML.csv", sep=',')
UN = UN.sort_values(by="Length", ascending=False).drop_duplicates(['chromosome', "genename"]).sort_index()
UN.to_csv("Test_Transcript_AML.csv", index = False, sep=',')

#UT = pd.read_csv("tumor_step2.csv", sep=',')
#UT = UT.drop_duplicates(['chromosome', 'length', "genename"]).sort_index()
#UT.to_csv("tumor_step2.csv", index = False, sep=',')



##################################Count Sequence Method###################

conversion_dictionary = {
     "A": "T",
     "T": "A",
     "U": "A",
     "G": "C",
     "C": "G",
     "Y": "R",
     "R": "Y",
     "N": "N"
 }
#
# def condense(filename, column):
#     csv = pd.read_csv(filename)
#     newCol = []
#     for row in range(csv.shape[0]):
#         temp = csv[column][row].replace("[", "")
#         temp = temp.replace("'", "")
#         temp = temp.replace("]", "")
#         temp = temp.replace(" ", "")
#         temp = temp.split(",")
#         newCol.append(temp[0])
#     newName = "New_" + column
#     csv.insert(csv.shape[1], newName, newCol)
#     csv.to_csv(filename, sep=",", index=False)
#
#
# def geneSeq(chr, txStart, txEnd, direction):
#     seqfile = open('/Users/omodo/PycharmProjects/pythonProject/sequences/genome_' + chr + ".fa", 'r')
#     next(seqfile)
#     sequence = seqfile.read().replace('\n', '')
#     seqfile.close()
#     sequence = sequence.upper()
#     seq = sequence[txStart:txEnd+1]
#
#     if (direction == '-'):
#         compSeq = ""
#         for base in seq:
#             compSeq += conversion_dictionary[base]
#         seq = compSeq
#     return seq
#
#


# UN = pd.read_csv("normal_step2.csv", sep=',')
# UT = pd.read_csv("tumor_step2.csv", sep=',')


#def generate_fasta(genename, length, sequence):
#    with open("PRCR_Variants_Sequence.fasta", "a") as fasta_file:
#       fasta_file.write(f">{genename}, Length: {length}\n")
#        fasta_file.write(f"{sequence}\n")
#
# #################################### Get sequences ###################################
# sequences = []
# for row in range(UN.shape[0]):
#    #     chr = UN.iloc[row]["chromosome"]
# #     if pd.isna(UN.iloc[row]["txStart"]) or pd.isna(UN.iloc[row]["txEnd"]):
# #     continue
#
# #      start = int(UN.iloc[row]["txStart"])
# #      end = int(UN.iloc[row]["txEnd"])
# #      strand = UN.iloc[row]["strand"]
# #      genename = UC.iloc[row]["genename"]
# #
# #      temp = geneSeq(chr, start, end, strand)
# #      UT.loc[row, 'Sequence'] = temp
# #      UT.loc[row, 'A'] = temp.count("A")
# #      UT.loc[row, 'G'] = temp.count("G")
# #      UT.loc[row, 'T'] = temp.count("T")
# #      UT.loc[row, 'C'] = temp.count("C")
# #      UC.loc[row, 'Length_New'] = len(temp)
# #
# #      generate_fasta(genename, len(temp), temp)
# UN = UN.insert(UN.shape[0], "Sequence", sequences)
# UC.to_csv("Normal_sequence.csv", index = False)
# #

# for row in range(UT.shape[0]):
#     chr = UC.iloc[row]["chromosome"]
#     if pd.isna(UC.iloc[row]["txStart"]) or pd.isna(UC.iloc[row]["txEnd"]):
#     continue

#      start = int(UT.iloc[row]["txStart"])
#      end = int(UT.iloc[row]["txEnd"])
#      strand = UT.iloc[row]["strand_x"]
#      genename = UC.iloc[row]["genename"]
#
#      temp = geneSeq(chr, start, end, strand)
#      UT.loc[row, 'Sequence'] = temp
#      UT.loc[row, 'A'] = temp.count("A")
#      UT.loc[row, 'G'] = temp.count("G")
#      UT.loc[row, 'T'] = temp.count("T")
#      UT.loc[row, 'C'] = temp.count("C")
#      UC.loc[row, 'Length_New'] = len(temp)
#
#      generate_fasta(genename, len(temp), temp)


#UC = UC[[col for col in UC.columns if col != "Sequence"] + ["Sequence"]]
#UC.to_csv("PRCR_Variants_Sequence.csv", index = False)

############count gene###########


# n = pd.read_csv("Tumor_sequence.csv", sep=',')
# t = pd.read_csv("Normal_sequence.csv", sep=',')

#
# def counts(csv):
#       a = csv["A"].sum()
#       g = csv["G"].sum()
#       t = csv["T"].sum()
#       c = csv["C"].sum()
#       print("A: " + str(a))
#       print("G: " + str(g))
#       print("T: " + str(t))
#       print("C: " + str(c))
# # #
# print("Normal:")
# counts(n)
# print("Tumor:")
# counts(t)






# ########################Reduce Sequence to 2000#####################
# def truncate_sequences(df, column_name, max_length=2000):
#      df[column_name] = df[column_name].str[:max_length]
#      return df
#
# ## # Load the Excel sheet into a DataFrame##########
# UN = pd.read_csv("Normal_sequence.csv", sep=',')
# UT = pd.read_csv("Tumor_sequence.csv", sep=',')
#
# sequence_column = "Sequence"
# UN = truncate_sequences(UC, sequence_column, max_length=2000)
# UN = UN.dropna(how='all')
# UN.to_csv("Normal_sequence1.csv", index = False)
#
# print(UN)


######Code to check if all the compare column ####################
# UU = pd.read_csv("Unique_SNVs.csv", sep=',')
# common_items = UU.loc[UU['genename1'].isin(UU['genename2']), 'genename1'].tolist()
#
# count_not_in_column2 = len(common_items)
#
# print(common_items)
# print("Count:", count_not_in_column2)

