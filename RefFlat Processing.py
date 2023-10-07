import pandas as pd
import os
import numpy


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


#def condense(filename, column):
 #   csv = pd.read_csv(filename)
  #  newCol = []
   # for row in range(csv.shape[0]):
    #    temp = csv[column][row].replace("[", "")
     #   temp = temp.replace("'", "")
      #  temp = temp.replace("]", "")
      #  temp = temp.replace(" ", "")
       # temp = temp.split(",")
        #newCol.append(temp[0])
    #newName = "New_" + column
    #csv.insert(csv.shape[1], newName, newCol)
    #csv.to_csv(filename, sep=",", index=False)
norm = pd.read_csv('/Users/omodo/PycharmProjects/pythonProject/Pra_refFlat.csv', sep=',')

def geneSeq(chr, txStart, txEnd, direction):
    seqfile = open('/Users/omodo/PycharmProjects/pythonProject/sequences/genome_' + chr + ".fa", 'r')
    next(seqfile)
    sequence = seqfile.read().replace('\n', '')
    seqfile.close()
    sequence = sequence.upper()
    seq = sequence[txStart:txEnd+1]

    if (direction == '-'):
        compSeq = ""
        for base in seq:
            compSeq += conversion_dictionary[base]
        seq = compSeq
    return seq

#uniqueN = pd.DataFrame(norm[["chromosome", "genename", "strand", "txStart", "txEnd"]])

#uniqueN = uniqueN.drop_duplicates()


## Use only the unique genes to avoid double counting, isoforms present so i am taking the largest length of the same gene, strand, and chrom ##########################
#uniqueN.to_csv("Pca_Normal_UniqueGenes.csv", sep=",", index=False)

#UN = pd.read_csv("Pca_Normal_UniqueGenes.csv", sep=',')

#UN = UN.sort_values(by="length", ascending=False).drop_duplicates(['chromosome', 'strand', "genename"]).sort_index()

#UN.to_csv("Pca_Normal_UniqueGenes.csv", index=False, sep=',')

#length = []
#for row in range(uniqueN.shape[0]):
    #if uniqueN.iloc[row]["txStart"] == 0:
   #     length.append(0)
   #     continue
    #min = int(uniqueN.iloc[row]["txStart"])
   # max = int(uniqueN.iloc[row]['txEnd'])
  #  temp = max - min
 #   length.append(temp)

#uniqueN = uniqueN.insert(uniqueN.shape[1], "Length", length)

UN = pd.read_csv("Pca_Normal_UniqueGenes.csv", sep=',')

# Get Sequence ######
sequences = []
for row in range(UN.shape[0]):
     chr = UN.iloc[row]["chromosome"]
     #if UN.iloc[row]["Length"] == 0:
      #   sequences.append(0)
       #  continue
     start = int(UN.iloc[row]["txStart"])
     end = int(UN.iloc[row]["txEnd"])
     strand = UN.iloc[row]["strand"]

     temp = geneSeq(chr, start, end, strand)
     UN.loc[row, 'Sequence'] = temp
     UN.loc[row, 'A'] = temp.count("A")
     UN.loc[row, 'G'] = temp.count("G")
     UN.loc[row, 'T'] = temp.count("T")
     UN.loc[row, 'C'] = temp.count("C")

UN = UN.insert(UN.shape[0], "Sequence", sequences)
UN.to_csv("check1RefFlatt.csv", index = False)

######################### Sum the A,G,T,C counts for normal and tumor #####################

#n = pd.read_csv("check1RefFlatt.csv", sep=',')

#def counts(csv):
 #   a = csv["A"].sum()
  #  g = csv["G"].sum()
   # t = csv["T"].sum()
    #c = csv["C"].sum()
    #print("A: " + str(a))
    #print("G: " + str(g))
    #print("T: " + str(t))
    #print("C: " + str(c))


#print("Normal:")
#counts(n)

# condense("ALL_Normal.csv", "Gene_Name")
############################ mergining the refFlat onto OMI #############################
#norm = pd.read_csv('/Users/omodo/PycharmProjects/pythonProject/SNV_gene_distribution.csv', sep=',')

#os .chdir('/Users/omodo/PycharmProjects/pythonProject/refFlat')
#refFlatfiles = os.listdir()

#print(refFlatfiles)
#chrDF = pd.DataFrame(columns=["genename", "name", "chromosome", "strand", "txStart", "txEnd", "cdsStart", "cdsEnd", "exonCount", "exonStarts", "exonEnds"])
#for file in refFlatfiles:
 #   chrDF1 = pd.read_csv(file, sep="\t", header=None, names=["genename", "name", "chromosome", "strand", "txStart", "txEnd", "cdsStart", "cdsEnd", "exonCount", "exonStarts", "exonEnds"])
  #  chrDF = pd.concat([chrDF, chrDF1], axis=0)

   # print(chrDF)
#chrom_norm = norm[["genename", "chromosome"]].drop_duplicates()

#newNorm = pd.merge(chrom_norm, chrDF[["genename", "chromosome", "strand", "txStart", "txEnd", "cdsStart", "cdsEnd",  "exonStarts", "exonEnds"]], how="left", on=["genename", "chromosome"])



# newTumor = pd.merge(tumor, chrDF[["New_Gene_Name", "chrom", "strand", "txStart", "txEnd", "cdsStart", "cdsEnd",  "exonStarts", "exonEnds"]], how="left", on=["New_Gene_Name", "chrom"])
# newTumor.drop_duplicates(subset=['chrom', "left", "ref_seq", "alt_seq", "VCF_ID", "New_Gene_Name"])

#newNorm.to_csv("Pra2_refFlat.csv", sep=",")

