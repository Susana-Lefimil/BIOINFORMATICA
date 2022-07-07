#Tarea 

#?comando abre la ayuda con las infos sobre el comando - ?seq
# 1) Crear un vector "x" con los valores de 1071 a 1193 con el comando seq

x<-seq(1071, 1193)
x

# a) usar indexacion para obtener los valores en las posiciones 10, 23, 59, 87 y 100

x[c(10,23,59,87,100)]

# b) usar indexacion y el comando length para obtener todos los valores menos los en las dez ultimas posiciones 
#length(x)
x[1:c(length(x)-10)]


# 2) Crear un vector "myseq" con la secuencia "AccGTAACttAcCtttaaCGt" y aplicar el comando toupper para uniformizar la secuencia 

myseq<-"AccGTAACttAcCtttaaCGt"
toupper(myseq)


# 3) Crear una matrice "matriz" con 10 lineas y 10 colunas con los valores de 201 a 300 

matriz<-matrix(201:300,nrow=10,ncol=10)

# a) Dividir la matrice por 3 y obtener os valores de las lineas 4 a 6 e de las colunas 7 a 10

matriz2<-3/matriz
matriz2[4:6,7:10]

# 4) Crear uma variable "altura" con 20 observaciones e los dez primeros valores abajo de 5, e los dez ultimos arriba de 9, una variable "sexo" com los dez primeros valores "F" los dez ultimos "M" y un dataframe com las dos.

altura<-c(sample(1:4,10,replace=T),sample(10:20,10,replace=T))
altura
sexo<-c(rep("F",10),rep("M",10))
dat <- data.frame(altura,sexo)

# a) usar la funcion str para inspecionar el dataframe

str(dat)

# b) usar indexacion para selecionar las lineas de 6 a 13 de todas las colunas

dat[c(6:13),]

# 5) Crear una lista "lista" con pelo menos 3 de los objetos anteriores 

lista<-list(dat,x, matriz2)

# a) cambiar los valores del primero elemento de cada objecto de la lista para "NA"
lista[[1]][,]<-"NA"
