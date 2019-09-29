# fuzzy-thresholding
fuzzy thresholding


基于模糊熵理论的阈值分割, 其实就是对直方图使用模糊熵理论, 直观理解就是根据同颜色多少分, 对比于otsu是使用值大小来分.  
优点是理论上更符合人类的感官, 缺点是运算量较大, 后续可以优化.  
Based on [Huang's fuzzy thresholding method](http://www.ktl.elf.stuba.sk/study/vacso/Zadania-Cvicenia/Cvicenie_3/TimA2/Huang_E016529624.pdf)