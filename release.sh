awk -F"\t" '{print $3}' data/*.canguan | sed "s/^\///g" > release_canguan
awk -F"\t" '{print $3}' data/*.jingdian | sed "s/^\///g" > release_jingdian
awk -F"\t" '{print $3}' data/*.jiudian | sed "s/^\///g" > release_jiudian
