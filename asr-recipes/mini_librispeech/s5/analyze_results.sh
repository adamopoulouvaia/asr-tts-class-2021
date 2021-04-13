#!/bin/bash
hypothesis_tra=exp/tri3b/decode_tglarge_dev_clean_2/scoring/9.0.5.tra
ref_trw=exp/tri3b/decode_tglarge_dev_clean_2/scoring/test_filt.txt

cat $hypothesis_tra | utils/int2sym.pl -f 2- data/lang_test_tglarge/words.txt | sed s:\<UNK\>::g > hypothesis.trw

python trw_to_wsj.py hypothesis.trw hypothesis.wsj
python trw_to_wsj.py $ref_trw ref.wsj 

/opt/kaldi/tools/sctk/bin/sclite -i ref.wsj -h hypothesis.wsj -o dtl 
