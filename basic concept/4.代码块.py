# A Python program is constructed from code blocks. A block is a piece of Python program text that is executed as a unit. The following are blocks: a module, a function body, and a class definition. Each command typed interactively is a block. A script file (a file given as standard input to the interpreter or specified as a command line argument to the interpreter) is a code block. A script command (a command specified on the interpreter command line with the ‘-c' option) is a code block. The string argument passed to the built-in functions eval() and exec() is a code block.

# 所以，有以下几种类型的代码块：
# 模块文件是一个代码块
# 函数体是一个代码块
# class的定义是一个代码块
# 交互式(python idle)的每一个命令行都是一个独立的代码块
# 脚本文件是一个代码块
# 脚本命令是一个代码块(python -c "xxx")
# eval()和exec()中的内容也都有各自的代码块
# 同一个代码块内，虽然仍然是读一行解释一行，但在退出这个代码块之前，不会忘记这个代码块中的内容，而且会统筹安排这个代码块