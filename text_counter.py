import collections
import sqlite3

### This script currently just outputs a big list of words and their frequencies... We'll make it better soon, promise!

def frequencies(words):
    # Defaults to 0
    counts = collections.defaultdict(int)
    for word in words:
        counts[word] += 1
    return counts

def main():
    db = sqlite3.connect('mmssms.db')
    cursor = db.cursor()
    bodies = [row[0] for row in cursor.execute('SELECT body FROM sms')]
    words = [[word for word in s.split(' ')] for s in bodies]
    words = [item for sublist in words for item in sublist]
    freqs = frequencies(words)
    print(collections.OrderedDict(sorted(freqs.items(), key=lambda x: x[1])))

if __name__ == '__main__':
    main()
    
    
