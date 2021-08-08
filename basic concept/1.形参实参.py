# 实参(argument)：
# 全称为"实际参数"是在调用时传递给函数的参数. 实参可以是常量、变量、表达式、函数等， 无论实参是何种类型的量，在进行函数调用时，它们都必须具有确定的值， 以便把这些值传送给形参。 因此应预先用赋值，输入等办法使实参获得确定值。      

# 形参(parameter)：
# 全称为"形式参数" 由于它不是实际存在变量，所以又称虚拟变量。是在定义函数名和函数体的时候使用的参数,目的是用来接收调用该函数时传入的参数.在调用函数时，实参将赋值给形参。因而，必须注意实参的个数，类型应与形参一一对应，并且实参必须要有确定的值。

# 形式参数：形参是函数被调用时用于接收实参值的变量。

# 根据实际需要可有可无。没有形参时，圆括号也不可省；多个参数之间应用逗号分隔。参数包括参数名和参数类型。

# 形参的类型说明可有如下两种格式：

#   int max(int  a,int b)/*形参的类型在形参表中直接说明*/

#     {  return (a>b?a:b);}     

#  或

#    int max(a,b)

#    inta,b;         /*形参的类型在函数体前、函数名后说明*/

#    { return(a>b?a:b); }

# 前者为标准格式，后者为传统格式，通常用前者。



# 形参和实参的区别

# 形参出现在函数定义中，在整个函数体内都可以使用， 离开该函数则不能使用。

# 实参出现在主调函数中，进入被调函数后，实参变量也不能使用。 

# 形参和实参的功能是作数据传送。发生函数调用时， 主调函数把实参的值传送给被调函数的形参从而实现主调函数向被调函数的数据传送。

# 1.形参变量只有在被调用时才分配内存单元，在调用结束时， 即刻释放所分配的内存单元。因此，形参只有在函数内部有效。 函数调用结束返回主调函数后则不能再使用该形参变量。 

# 2.实参可以是常量、变量、表达式、函数等， 无论实参是何种类型的量，在进行函数调用时，它们都必须具有确定的值， 以便把这些值传送给形参。 因此应预先用赋值，输入等办法使实参获得确定值。 

# 3.实参和形参在数量上，类型上，顺序上应严格一致， 否则会发生“类型不匹配”的错误。 

# 4.函数调用中发生的数据传送是单向的。 即只能把实参的值传送给形参，而不能把形参的值反向地传送给实参。 因此在函数调用过程中，形参的值发生改变，而实参中的值不会变化。

# 5.当形参和实参不是指针类型时，在该函数运行时，形参和实参是不同的变量，他们在内存中位于不同的位置，形参将实参的内容复制一份，在该函数运行结束的时候形参被释放，而实参内容不会改变。

# 而如果函数的参数是指针类型变量,在调用该函数的过程中，传给函数的是实参的地址，在函数体内部使用的也是实参的地址，即使用的就是实参本身。所以在函数体内部可以改变实参的值。