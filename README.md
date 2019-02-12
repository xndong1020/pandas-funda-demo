###  pandas series
index can be string

```
my_numpy_array = np.random.rand(3)
my_series = pd.Series(my_numpy_array, index=['first','second','third'])

my_series['first'] # 0.6819300600804504
still you can access elements by number index
my_series[0] # again 0.6819300600804504
```
check index
```angular2html
my_series.index # Index(['first', 'second', 'third'], dtype='object')
```

2D array
```angular2html
array_2d = np.random.rand(3,2)
# array([[0.56641563, 0.24952426],
       [0.51384474, 0.04055527],
       [0.94060486, 0.57855198]])


To access the second column in first row

array_2d[0,1]
# 0.24952425739353812

convert to pandas Dataframes
df = pd.DataFrame(array_2d)

          0         1
0  0.566416  0.249524
1  0.513845  0.040555
2  0.940605  0.578552


# to give rows a name
df.columns = ['first','second']

      first    second
0  0.566416  0.249524
1  0.513845  0.040555
2  0.940605  0.578552

to access the entire column
df['second']

gives you
0    0.249524
1    0.040555
2    0.578552
Name: second, dtype: float64


df['second'][0]
# 0.24952425739353812

you can do [<column>][<row>] only 

df[0] gives you error
```

## pandas can handle 3 types of file:
text files(csv, json, html table), binary files, relational databases

### take 1: read csv, first class data formatting in pandas
```angular2html
import pandas as pd

df = pd.read_csv('artwork_data.csv', nrows=5)


#      id  ...                                                url
0  1035  ...  http://www.tate.org.uk/art/artworks/blake-a-fi...
1  1036  ...  http://www.tate.org.uk/art/artworks/blake-two-...
2  1037  ...  http://www.tate.org.uk/art/artworks/blake-the-...
3  1038  ...  http://www.tate.org.uk/art/artworks/blake-six-...
4  1039  ...  http://www.tate.org.uk/art/artworks/blake-the-...


```

But now you created your own row index, (0-4)
Instead, you can use the 'id' column read from artwork_data.csv file

```angular2html
df = pd.read_csv('artwork_data.csv', nrows=5, index_col='id')

     accession_number  ...                                                url
id                     ...                                                   
1035           A00001  ...  http://www.tate.org.uk/art/artworks/blake-a-fi...
1036           A00002  ...  http://www.tate.org.uk/art/artworks/blake-two-...
1037           A00003  ...  http://www.tate.org.uk/art/artworks/blake-the-...
1038           A00004  ...  http://www.tate.org.uk/art/artworks/blake-six-...
1039           A00005  ...  http://www.tate.org.uk/art/artworks/blake-the-...

now the 'id' column has became the index column of your pd dataframe

```

You can slice the dataframe by specifying which columns are needed
```angular2html
df = pd.read_csv('artwork_data.csv', nrows=5, index_col='id', usecols=['id', 'artist'])

#               artist
id                  
1035   Blake, Robert
1036   Blake, Robert
1037   Blake, Robert
1038   Blake, Robert
1039  Blake, William

```