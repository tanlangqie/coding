# -*- coding: utf-8 -*-#

# Name:   seq2seq.py
# Author: tangzhuang
# Date:   2021/7/4
# desc:
import numpy as np

char_arr = [ c for c in 'SEPatcdefghijklmnopqrstuvwxyz ' ]
num_dic = {n: i for i, n in enumerate (char_arr) }
seq_data = [ [ 'man','women' ],[ 'black ', 'white'],[ 'king','queen'],['girl', 'boy' ],[ 'up', 'down'],[ 'high' , ' low' ]]
n_step = 5
n_hidden = 128
n_class = len ( num_dic)
input_batch,output_batch,target_batch = [],[],[]
for seq in seq_data :
    for i in range( 2 ) :
        seq[ i] = seq[i] +'P' * (n_step - len( seq[ i]) )
        input = [ num_dic[ n ] for n in seq[ 0]]
        output = [ num_dic[n] for n in ( 'S' + seq[ 1])]
        target = [ num_dic[ n] for n in ( seq[ 1] +'E') ]
        input_batch. append ( np.eye( n_class ) [input ])
        output_batch. append( np.eye(n_class ) [ output])
        target_batch. append( target)
