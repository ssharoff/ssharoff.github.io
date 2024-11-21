#experiments with annotated corpora
# cases-annot.dat needs to have text ids as the row names and the column Top for their top level categories
c.annot=read.table('cases-annot.dat',header=T)
c=read.table('cases-biber.dat',header=T,row.names=NULL)
dim(c)
fnum=dim(c)[2]
flabels=rownames(c.annot)
rownames(c)=flabels;

#text external view
testIndex=sort.int(sample(nrow(c.annot),25))
View(c.annot[testIndex,])
table(c.annot$Top)

#text internal view
View(c[testIndex,])
colnames(c)

## library(caret)
## #centering and scaling
## featurePlot(c[,1:12],c.annot$Top,plot="strip", jitter=T)
## preC.model=preProcess(c, method = c("center", "scale"));
## c=predict(preC.model,c);
## featurePlot(c[,1:12],c.annot$Top,plot="strip", jitter=T)
## featurePlot(c,c.annot$Top,plot="strip", jitter =T);

colnames(c)
Top=c.annot$Top
s=c[,c("C11.indefProns","F18.BYpassives","K48.amplifiers","K49.generalEmphatics", "K50.discoursePart")]
s=cbind(s,Top);
head(s)
library(ggplot2)

ggplot(s, aes(y=C11.indefProns,x=Top, color=Top)) + geom_violin(trim=T) + theme_classic(base_size = 22) + geom_jitter(shape=16, position=position_jitter(0.2), color='grey') + labs(title="C11.indefProns",x="", y = "") + coord_flip(); dev.copy(pdf,"C11.indefProns.pdf"); dev.off();

ggplot(s, aes(y=F18.BYpassives,x=Top, color=Top)) + geom_violin(trim=T) + theme_classic(base_size = 22) + geom_jitter(shape=16, position=position_jitter(0.2), color='grey') + labs(title="F18.BYpassives",x="", y = "") + coord_flip(); dev.copy(pdf,'F18.BYpassives.pdf'); dev.off();

ggplot(s, aes(y=K48.amplifiers,x=Top, color=Top)) + geom_violin(trim=T) + theme_classic(base_size = 22) + geom_jitter(shape=16, position=position_jitter(0.2), color='grey') + labs(title="K48.amplifiers",x="", y = "") + coord_flip(); dev.copy(pdf,'K48.amplifiers.pdf'); dev.off();

ggplot(s, aes(y=K49.generalEmphatics,x=Top, color=Top)) + geom_violin(trim=T) + theme_classic(base_size = 22) + geom_jitter(shape=16, position=position_jitter(0.2), color='grey') + labs(title="K49.generalEmphatics",x="", y = "") + coord_flip();dev.copy(pdf,'K49.generalEmphatics.pdf'); dev.off();

ggplot(s, aes(y=K50.discoursePart,x=Top, color=Top)) + geom_violin(trim=T) + theme_classic(base_size = 22) + geom_jitter(shape=16, position=position_jitter(0.2), color='grey') + labs(title="K50.discoursePart",x="", y = "") + coord_flip();dev.copy(pdf,'K50.discoursePart.pdf'); dev.off();

##stat_summary(fun.data="mean_sdl", geom="pointrange", width=0.2, color="red" )  + coord_cartesian(ylim =c(0, 2000)), scale_y_continuous(limits = 

Genre1=c.annot$Top
s=cbind(as.data.frame(b.factanal$scores),Genre1);
ggplot(s1, aes(y=Factor1,x=Genre1, color=Genre1)) + geom_violin(trim=T)  + stat_summary(fun.data="mean_sdl", geom="pointrange", color="red" ) + theme_classic(base_size = 22) + labs(title="Factor1",x="", y = "") + coord_flip();

x=which(Genre1=='news' | Genre1=='fiction')
ggplot(s1[x], aes(y=Factor1,x=Genre1, color=Genre1)) + geom_violin(trim=T)  + stat_summary(fun.data="mean_sdl", geom="pointrange", color="red" ) + theme_classic(base_size = 22) + labs(title="Factor1",x="", y = "") + coord_flip();


#model from https://rpubs.com/malshe/214303
logit=nnet::multinom(c.annot$Top ~ ., c);
output=summary(logit);
z <- output$coefficients/output$standard.errors
p=pt(abs(z), df=length(c.annot$Top)-length(c[1,]),lower=FALSE)
fnames=rownames(p);
goodfeatures=c('');
for (i in c(1:length(fnames))) {
    print(fnames[i]);
    l=names(p[i,p[i,]<0.005]);
    goodfeatures=union(l, goodfeatures);
    print(l)
}
print(goodfeatures)

