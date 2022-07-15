Let's define Bracket sequence (BS) as a string which consists of any natural number (+zero) of brackets. Brackets can be one of the following three types: parentheses: ( ), square brackets: [ ], and braces: { }. Examples of bracket sequences:
( [ )
} (
{ )
( { } )
Set of Regular Bracket Sequences (RBS) is defined using the following rule:
Empty string is an RBS.
If A is an RBS, then (A), [A], {A} are also RBS.
If A and B are RBS, then AB and BA are also RBS.
Examples of regular bracket sequences:
( )
{ } ( )
( { } )

## Input format

You are given a bracket sequence terminated by line break symbol. The length of the sequence is 0 ≤ N ≤ 200000 characters. You need to check if this bracket sequence is regular.

## Output format

Single line: yes if given sequence is regular, and no otherwise.
