# Read from the file words.txt and output the word frequency list to stdout.
cat words.txt | sed 's/ /\n/g' | grep -v '^$' | sort | uniq -c | sort -nr | awk '{print $NF, $1}'
