# NOTES



### pd.Series.str
1. can be used to apply any string function to 'object' data inside of a pd.Series object
    - ex. tweets["content"].str.len() > 15

### Sorting values
1. sort_values() - can be used on <u>pd.DataFrame</u> object
    - by=[columns] - which columns to sort by
    - axis=0/1 - sort rows/columns
    - the method can be also used with <u>pd.Series</u> object, but without the 'by' argument

### Getting rid of the duplicates

1. **drop_duplicates()** - can be used on <u>pd.DataFrame</u> object
    - subset=[columns] - which columns to consider
    - keep="first"/"last"/False - drop first/last/all duplicates
2. **unique()** - can be used on a <u>pd.Series</u> object
    
