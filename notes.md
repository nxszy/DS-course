# NOTES



### pd.Series.str
1. can be used to apply any string function to 'object' data inside of a pd.Series object
    - ex. tweets["content"].str.len() > 15
    - str.match(regex) - uses re.match to filter the strings
    - str.contains(regex) - uses re.search to filter the string
    > re.match() - if zero or more characters at the beginning of string match the regular expression pattern, return a corresponding match object.

    > re.search() - scan through string looking for the first location where the regular expression pattern produces a match

### Sorting values
1. **sort_values()** - can be used on <u>pd.DataFrame</u> object
    - by=[columns] - which columns to sort by
    - axis=0/1 - sort rows/columns
    > can be used on <u>pd.Series</u> object, but without the *by* argument

### Ranking values
1. **rank()**
    - ascending=0/1 - wheter or not the elements should be rank in ascending order
    - method={‘average’, ‘min’, ‘max’, ‘first’, ‘dense’} - what to do in case of a tie


### Mode and Median
1. **mode()** - the value that appears most often. It can be multiple values.
    - axis=0/1 - over column/over row
    - numeric_only=False
    - dropna=True

2. **median()** - returns median of the values over given axis
    - axis=0/1 - over column/over row
    - numeric_only=False
    - skipna=True

### Largest and smallest values
1. **nlargest** - can be used on <u> pd.DataFrame</u>
    - n - how many largest elements to return (max)
    - columns - by which columns to sort
    - returns a pd.DataFrame
    > can be used on <u>pd.Series</u>, but without the *columns* argument

2. **nsmallest** - can be used on <u> pd.DataFrame</u>
    - n - how many smallest elements to return (max)
    - columns - by which columns to sort
    - returns a pd.DataFrame
    > can be used on <u>pd.Series</u>, but without the *columns* argument 

### Getting rid of the duplicates

1. **drop_duplicates()** - can be used on <u>pd.DataFrame</u> object
    - subset=[columns] - which columns to consider
    - keep="first"/"last"/False - drop first/last/all duplicates
2. **unique()** - can be used on a <u>pd.Series</u> object

    > drop_duplicates() returns a <u>pd.DataFrame</u> object, whereas unique() returns a <u>np.ndarray</u> object!
