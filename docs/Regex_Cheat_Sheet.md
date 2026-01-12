# Regex Cheat Sheet (One Page)

## Metacharacters
```
.  any char       ^  start       $  end       |  OR
() group          [] class       {} quantifier \ escape
*  0+             +  1+          ?  0/1 or non-greedy modifier
```

## Character Classes
```
\d digit   \D non-digit   \w word   \W non-word   \s space   \S non-space
[a-z] range   [^...] negated class   \p{L} letters (Unicode, if supported)
```

## Quantifiers
```
{n} exactly n   {n,} at least n   {n,m} between n and m
Greedy: * + ?   Non-greedy: *? +? ??
```

## Anchors & Boundaries
```
^ start  $ end   word-boundary  \B non-boundary  \A start  \Z end
```

## Groups & Lookarounds
```
( ) capture     (?: ) non-capture     (?P<name> ) named (Python)
(?= ) lookahead     (?! ) neg-lookahead     (?<= ) lookbehind     (?<! ) neg-lookbehind
```

## Flags
```
/i case-insensitive   /m multiline   /s dot-all   /x verbose   /u unicode   /g global (JS)
```

## Common Snippets
```regex
Email:    ^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$
IPv4:     ^(\d{1,3}\.){3}\d{1,3}$
Date:     ^\d{4}-\d{2}-\d{2}$
Hashtag:  #([A-Za-z0-9_]+)
Words:    [A-Za-z]+
Numbers:  -?\d+(?:\.\d+)?
```

## Tips
- Anchor your patterns to constrain matches.
- Avoid nested greedy quantifiers.
- Prefer explicit ranges; comment complex patterns (verbose mode).
