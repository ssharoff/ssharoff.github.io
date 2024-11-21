#!/usr/bin/env Rscript
# a simple script for comparing columns intwo datasets

args=commandArgs(trailingOnly=T);
header=F;
if (length(args)>2) {
    header=T;
}

df1=read.table(args[1],header=header);
df2=read.table(args[2],header=header);

tests_list <- lapply(seq_along(df1), function(i){
  t.test(df1[[i]], df2[[i]])
})

# ttest.vec=sapply(tests_list, '[[', 'statistic')

ttestp.vec=sapply(tests_list, '[[', 'p.value')
ttestp.vec=array(unlist(ttestp.vec))
dimnames(ttestp.vec)=list(colnames(df1))

write.table(sort(ttestp.vec),file=paste(args[1],args[2],sep="-"));

# sapply(tests_list, '[[', 'conf.int')

