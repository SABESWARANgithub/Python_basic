#by using dictionary comprehension ; we can create a new dictionary itself from the
#                                                                 exiting(before/original) dictionary

#syntax: dictionary={key:exprn for (key,value) in iterable}            -    give the exprn for value
cart={"phone":12000.00,"lap":32000.50,"pen":9.80,"bag":1149.60}
prod_rou={key:round(value) for (key,value) in cart.items()}

prod_rou1={k:round(v) for (k,v) in cart.items()}
print(prod_rou)
print(prod_rou1)

#syntax: dictionary={exprn(key):exprn(value) for (key,value) in iterable}
mod_de={k[0]:round(v) for (k,v) in cart.items()}
print(mod_de)
mod_de={k[0]:round(v) for (k,v) in cart.items()}

#dictionary comprehension with if condition
  #syntax: list={key:exprn for (key,value) in iterable if cond}
gre={c:b for (c,b) in cart.items() if b>10000}
print(gre)

#if-else condition
     #syntax: {k-exprn:v-exprn if ... else ... for (k,v) in iterable}

grea={c:b if b>10000 else "?" for (c,b) in cart.items()}

#if val of product is greater than 10000 give 10% discount
greae={c:b*.9 if b>10000 else b for (c,b) in cart.items()}        #by giving like (val*.9) ; giving 10% discount
print(grea)
print(greae)


#??????  Doubt  ??????
#we can also give func also in the exprn place ;
#             by giving the exprn in the func & declare that func in this exprn place in comprehension method
print("\n ")
#syntax: dict={key:func for (key,value) in iterable}
#to give 5% discount for pen & bag
cart6={"phone":12000.00,"lap":32000.50,"pen":9.80,"bag":1149.60}
def discount(k,v):
    if (k=="pen" or k=="bag"):
        v=.95*v
    return v

cart5={k:discount(k,v) for (k,v) in cart6}
print(cart5)