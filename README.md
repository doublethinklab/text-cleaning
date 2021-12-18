# Text Cleaning


## Dependencies

Some cleaning functions break if another goes before them.
The following table attempts to track these dependencies.
Note that since all classes are in the `text_cleaning` module, we omit that
for brevity here.

|Function|Dependencies|
|-|-|
|`functions.text.StandardizeText`|`functions.text.LowerCaseText`|
