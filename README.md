# fuzzy-thresholding
fuzzy thresholding


基于模糊熵理论的阈值分割, 其实就是对直方图使用模糊熵理论, 直观理解就是根据同颜色多少分, 对比于otsu是使用值大小来分.  
优点是理论上更符合人类的感官, 在较平滑的图像上拥有更好的表现, 缺点是运算量较大, 后续可以优化.  
Based on [Huang's fuzzy thresholding method](http://www.ktl.elf.stuba.sk/study/vacso/Zadania-Cvicenia/Cvicenie_3/TimA2/Huang_E016529624.pdf)

对比otsu的结果
result compare otsu:
![mat](https://raw.githubusercontent.com/MirusUmbra/Display-data/master/fuzzy-thresholding/sima.jpg?token=AJZQ6R2HKAT35BTACJOKRC26Y64CS)</br>
fuzzy  
![mat](https://raw.githubusercontent.com/MirusUmbra/Display-data/master/fuzzy-thresholding/simaf.png?token=AJZQ6R4HTURHHQK4SQYE4MK6Y64GU)</br>
otsu
![mat](https://raw.githubusercontent.com/MirusUmbra/Display-data/master/fuzzy-thresholding/simaotsu.png?token=AJZQ6R27IPTMKSPTIFVBXZC6Y64HW)</br>  


![mat](https://raw.githubusercontent.com/MirusUmbra/Display-data/master/fuzzy-thresholding/tiananmen.png?token=AJZQ6R2OM6GWFW6BC7BZCIS6Y64KG)</br>
fuzzy  
![mat](https://raw.githubusercontent.com/MirusUmbra/Display-data/master/fuzzy-thresholding/tiananmenf.png?token=AJZQ6RYXHS4YGJ4EHL5SGRK6Y64K6)</br>
otsu  
![mat](https://raw.githubusercontent.com/MirusUmbra/Display-data/master/fuzzy-thresholding/tiananmenotsu.png?token=AJZQ6RYNKCJJ5W2KBTVPNHK6Y64LS)</br>  
