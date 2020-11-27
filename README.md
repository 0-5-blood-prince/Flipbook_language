# Flipbook_language
Libraries Used : PIL <br/>
fc.py is the compiler <br />
Default without any arguments other than the file to be compiled, It creates an pdf of the defined flipbook. <br />
```
01 05 child.jpg
06 10 adolescent.jpg
11 15 young-adulthood.jpg
16 20 adulthood.jpg
21 25 old-age.jpg

```
To Create Pdfs
```
./fc.py life.flip
```
```
./fc.py life.flip -pdf
```
```
./fc.py life.flip -pdf images.pdf
```
To Creates Gifs
```
./fc.py life.flip -gif
```
```
./fc.py life.flip -gif lifecycle.gif
```
![](lifecycle.gif)
