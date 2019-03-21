def proteins(strand):
    codons = {
        'AUG':'Methionine',
        'UUU':'Phenylalanine',
        'UUC':'Phenylalanine',
        'UUA':'Leucine',
        'UUG':'Leucine',
        'UCU':'Serine',
        'UCC':'Serine',
        'UCA':'Serine',
        'UCG':'Serine',
        'UAU':'Tyrosine',
        'UAC':'Tyrosine',
        'UGU':'Cysteine',
        'UGC':'Cysteine',
        'UGG':'Tryptophan',
        'UAA':'STOP',
        'UAG':'STOP',
        'UGA':'STOP'
    }

    codons_list = [strand[i:i+3] for i in range(0, len(strand), 3)]

    proteins = []
    for c in codons_list:
        if codons[c] == 'STOP':
            break
        proteins.append(codons[c]) 

    return proteins
