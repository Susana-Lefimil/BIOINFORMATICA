mifuncion <- function(object1, object2){
  x<-object1
  y<-object2
  total<-sum(x,y) #o total <-x+y
  return(total)
}
mifuncion(10,987)

#usando la funcion lenght, sum construya una funcion para sacar el promedio aritmetico

promedio <-function(x){
  sum = 0
  n=1
  for(i in x){
    sum=sum+x[n]
    #print(x[n])
    n=1+n
  }
  print(sum)
  sum=sum/length(x)
  return (sum)
}
x<-c(5,7,9, 50,8)
promedio(x)

varianza <-function(x){
  
  p=promedio(x)
  v = 0
  n=1
  for(i in x){
    v=v +(x[n]-p)^2
    n=1+n
  }
  v=v/length(x)-1
  return (v)
}
x<-c(5,7,9, 50,8)
varianza(x)
