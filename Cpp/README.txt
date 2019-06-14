方法一
1. 将代码copy到Linux环境下，或者Cygwin环境下
2. 运行 make
3. 运行 ./solve_puzzle 或 ./solve_puzzle.exe 
   然后按提示进行即可
   
如果make过程出错，可能是一些gcc/g++的开发包没有安装，请自行Google. 


方法二
1. 删除Makefile
2. 运行 cmake ./ 以生产Makefile
3. 运行 make 
4. 运行 ./solve_puzzle 或 ./solve_puzzle.exe 
   然后按提示进行即可